#!/bin/env python3

# Fontimize
# 
# A library to optimise font files for web use, by only including the characters used in the text.
# Author: David Millington, github.com/vintagedave
# License: GPLv3
#
# Optimised for FSung & blacksmith-4vcpu-ubuntu-2404.

import os
import sys
from bs4 import BeautifulSoup
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.subset import Options, Subsetter
from os import path
import typing
import pathlib
from pathvalidate import ValidationError, validate_filename
import multiprocessing as mp  # For parallel font processing

def _get_unicode_string(char : str, withU : bool = True) -> str:
    return ('U+' if withU else '') + hex(ord(char))[2:].upper().zfill(4) # eg U+1234

def _is_cjk_character(codepoint: int) -> bool:
    cjk_ranges = [
        (0x4E00, 0x9FFF),      # Main
        (0x3400, 0x4DBF),      # Ext A
        (0x20000, 0x2A6DF),    # Ext B
        (0x2A700, 0x2B73F),    # Ext C
        (0x2B740, 0x2B81F),    # Ext D
        (0x2B820, 0x2CEAF),    # Ext E
        (0x2CEB0, 0x2EBEF),    # Ext F
        (0x30000, 0x3134F),    # Ext G
        (0x31350, 0x323AF),    # Ext H
        (0x2EBF0, 0x2EE5F),    # Ext I
        (0x323B0, 0x3347F),    # Ext J
        (0x2E80, 0x2EFF),      # CJK Radicals Supplement
        (0x2F00, 0x2FDF),      # Kangxi Radicals
        (0x2F800, 0x2FA1F),    # CJK Compatibility Ideographs Supplement
        (0x2FF0, 0x2FFF),      # Ideographic Description Characters
        (0x3000, 0x303F),      # Symbols and Punctuation
        (0x3100, 0x312F),      # Bopomofo
        (0x31C0, 0x31EF),      # CJK Strokes
        (0x3200, 0x32FF),      # Enclosed CJK Letters and Months
        (0x3300, 0x33FF),      # CJK Compatibility
        (0xF900, 0xFAFF),      # CJK Compatibility Ideographs
        (0xFE10, 0xFE1F),      # Vertical Forms
        (0xFE30, 0xFE4F),      # CJK Compatibility Forms
        (0xF0000, 0xFFFFF),    # Plane 15: Full private use
        (0x100000, 0x10FFFF),  # Plane 16: Full private use
    ]
    return any(start <= codepoint <= end for start, end in cjk_ranges)

def _filter_cjk_only(chars: set[str]) -> set[str]:
    """Filter set to only CJK characters (including private planes)."""
    filtered = {c for c in chars if _is_cjk_character(ord(c))}
    if not filtered:  # Ensure at least space for subset if no characters found
        filtered.add(" ")
    return filtered

def _apply_special_characters(chars: set[str]) -> set[str]:
    # Check for some special characters and add extra variants
    if chars.intersection(set("\"")):
        chars.add('“')
        chars.add('”')
    if chars.intersection(set("\'")):
        chars.add('‘')
        chars.add('’')
    if chars.intersection(set("-")):
        chars.add('–') # en-dash
        chars.add('—') # em-dash
    return chars

class charPair:
    def __init__(self, first : str, second : str):
        self.first = first
        self.second = second

    def __str__(self):
        return "[" + self.first + "-" + self.second + "]" # Pairs are inclusive
    
    # For print()-ing
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, charPair):
            return self.first == other.first and self.second == other.second
        return False
    
    def get_range(self):
        if self.first == self.second:
            return _get_unicode_string(self.first)
        else:
            return _get_unicode_string(self.first) + '-' + _get_unicode_string(self.second, False) # Eg "U+0061-0071"

def _parse_unicode_ranges(uranges_str: str) -> list[int]:
    """Parse string ranges like 'U+0041-005A,U+0061' into a flat list of integer codepoints."""
    unicodes = []
    for part in uranges_str.split(', '):
        if '-' in part:
            start_str, end_str = part.split('-')
            # Strip 'U+' prefix if present
            start = int(start_str.replace('U+', ''), 16)
            end = int(end_str.replace('U+', ''), 16)
            unicodes.extend(range(start, end + 1))
        else:
            # Single codepoint
            unicodes.append(int(part.replace('U+', ''), 16))
    return unicodes

# Taking a sorted list of characters, find the sequential subsets and return pairs of the start and end
# of each sequential subset
def _get_char_ranges(chars : list[str]):
    chars.sort()
    if not chars:
        return []
    res : list[charPair] = []
    first : str = chars[0]
    prev_seen : str = first
    for c in chars[1:]:
        expected_next_char = chr(ord(prev_seen) + 1)
        if c != expected_next_char:
            # non-sequential, so time to start a new set
            pair = charPair(first, prev_seen)
            res.append(pair)
            first = c
        prev_seen = c
    # add final set if it hasn't been added yet
    if (not res) or (res[-1].second != prev_seen):
        pair = charPair(first, prev_seen)
        res.append(pair)

    return res

# Get the total size of multiple files (used for calculating font file sizes)
def _get_file_size_sum(files: list[str]) -> int:
    total_size = 0
    for f in files:
        total_size += path.getsize(f)
    return total_size
    
# Convert to human-readable size in MB or KB
def _file_size_to_readable(size : int) -> str:
    return str(round(size / 1024)) + "KB" if size < 1024 * 1024 else str(round(size / (1024 * 1024), 1)) + "MB" # nKB or n.nMB

def _generate_font_subset(args_tuple):
    """Worker function for parallel font generation."""
    font, uranges, assetdir, verbosity, subsetname = args_tuple
    uranges_str = uranges[0][1]  # Extract the unicode ranges string

    if verbosity >= 2:
        print(f"Subsetting font: {font}")
        print(f"Unicode ranges: {uranges_str}")

    # Parse string ranges to integer codepoints
    unicodes = _parse_unicode_ranges(uranges_str)
    if verbosity >= 2:
        print(f"Parsed {len(unicodes)} unique codepoints")

    options = Options()
    options.name_IDs = ['*']
    options.glyph_names = True
    options.notdef_glyph = True
    options.ignore_missing_unicodes = True
    options.layout_features = '*'
    options.recommended_glyphs = True  # Include space, NULL, etc.

    # Load font with TTFont for full control
    input_font = TTFont(font, checkChecksums=0, lazy=True)

    # Initialize and populate subsetter with parsed unicodes
    subsetter = Subsetter(options)
    subsetter.populate(unicodes=unicodes)

    # Perform subsetting
    subsetter.subset(input_font)

    base = path.basename(font)
    name, ext = path.splitext(base)
    output_file = path.join(assetdir, f"{name}.{subsetname}{ext}")

    # Save the subsetted font
    subset.save_font(input_font, output_file, options)

    if verbosity >= 2:
        print(f"Generated subset: {output_file} ({len(unicodes)} codepoints targeted)")

    input_font.close()  # Clean up
    return font, output_file

# Takes the input characters set (including specials), and the fonts, and generates new font files
# Other methods (eg taking HTML files, or multiple pieces of text) all end up here
def optimise_fonts(characters : set[str], fonts : list[str], fontpath : str = "", subsetname = "FontimizeSubset", verbose : bool = False, print_stats : bool = True, cjk_only : bool = True, parallel : bool = True) -> dict[str, typing.Any]:
    verbosity = 2 if verbose else 0 # subset has verbosity levels, match to off and on

    res : dict[str, typing.Any] = {}

    if cjk_only:
        characters = _filter_cjk_only(characters)
    if len(characters) <= 1:
        print("Error: No characters remain after filtering. Exiting.")
        res["fonts"] = {}
        res["chars"] = set()
        res["uranges"] = ""
        return res

    char_list = list(characters)
    if verbosity >= 2:
        print("Characters:")
        print("  " + str(char_list))
    res["chars"] = characters # set of characters used in the input text

    char_ranges = _get_char_ranges(char_list)
    if verbosity >= 2:
        print("Character ranges:")
        print("  " + str(char_ranges))
    
    uranges_str = ', '.join(r.get_range() for r in char_ranges)
    uranges = [[subsetname, uranges_str]] # subsetname here will be in the generated font name, eg 'Arial.FontimizeSubset.ttf'
    if verbosity >= 2:
        print("Unicode ranges:")
        print("  " + uranges_str)  
    res["uranges"] = uranges_str # list of unicode ranges matching the characters used in the input text

    # For each font, generate a new font file using only the used characters
    # By default, place it in the same folder as the respective font, unless fontpath is specified
    res["fonts"] = {} # dict of old font path -> new font path
    assetdir = fontpath or path.dirname(fonts[0]) or "."
    worker_args = [(font, uranges, assetdir, verbosity, subsetname) for font in fonts]
    
    max_workers = min(4, len(fonts), mp.cpu_count())  # Cap at 4 vCPUs for the target machine
    if parallel:
        with mp.Pool(processes=max_workers) as pool:
            results = pool.map(_generate_font_subset, worker_args)
    else:
        results = [_generate_font_subset(args) for args in worker_args]
    
    for font, new_font in results:
        res["fonts"][font] = new_font

    if verbosity >= 2:
        print("Generated the following fonts from the originals:")
        for k in res["fonts"].keys():
            print("  " + k + " ->\n    " + res["fonts"][k])

    if (verbosity >= 2) or print_stats:
        print("Results:")
        print("  Fonts processed: " + str(len(res["fonts"])))
        if (verbosity == 1): # If 2, printed above already
            print("  Generated (use verbose output for input -> generated map):")
            for k in res["fonts"].keys():
                print("    " + res["fonts"][k])
        sum_orig =  _get_file_size_sum(fonts)
        sum_new = _get_file_size_sum(list(res["fonts"].values())) 
        print("  Total original font size: " + _file_size_to_readable(sum_orig))
        print("  Total optimised font size: " + _file_size_to_readable(sum_new))
        if sum_orig > 0:
            savings = sum_orig - sum_new;
            savings_percent = savings / sum_orig * 100 
            print("  Savings: " +  _file_size_to_readable(savings) + " less, which is " + str(round(savings_percent, 1)) + "%!")
        print("Thank you for using Fontimize!") # A play on Font and Optimise, haha, so good pun clever. But seriously - hopefully a memorable name!

    return res

# Takes a list of strings, and otherwise does the same as optimise_fonts
def optimise_fonts_for_multiple_text(texts : list[str], fonts : list[str], fontpath : str = "", subsetname = "FontimizeSubset", verbose : bool = False, print_stats : bool = True, cjk_only : bool = True, parallel : bool = True) -> dict[str, typing.Any]:
    chars : set[str] = { " " }
    for t in texts:
        for c in t:
            chars.add(c)
    if len(chars) <= 1:
        print("Error: No text found in the input texts. Exiting.")
        res = {
            "fonts" : {},
            "chars": set(),
            "uranges": ""
        }
        return res
    chars = _apply_special_characters(chars)
    return optimise_fonts(chars, fonts, fontpath, verbose=verbose, print_stats=print_stats, cjk_only=cjk_only, parallel=parallel)

# Takes a list of HTML strings, and parses those to get the used text (ie ignoring HTML tags);
# then uses that to do the same as optimise_fonts
def optimise_fonts_for_html_contents(html_contents : list[str], fonts : list[str], fontpath : str = "", subsetname = "FontimizeSubset", verbose : bool = False, print_stats : bool = True, cjk_only : bool = True, parallel : bool = True) -> dict[str, typing.Any]:
    chars : set[str] = { " " }
    for html in html_contents:
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        for c in text:
            chars.add(c)
    if len(chars) <= 1:
        print("Error: No text found in the input HTML. Exiting.")
        res = {
            "fonts" : {},
            "chars": set(),
            "uranges": ""
        }
        return res
    chars = _apply_special_characters(chars)
    return optimise_fonts(chars, fonts, fontpath, verbose=verbose, print_stats=print_stats, cjk_only=cjk_only, parallel=parallel)

# Takes a list of files on disk
# HTML files are parsed; all others are treated as text
# First, collect all strings from those files.
def optimise_fonts_for_files(files : list[str], font_output_dir = "", subsetname = "FontimizeSubset", verbose : bool = False, print_stats : bool = True, fonts : list[str] = [], addtl_text : str = "", cjk_only : bool = True, parallel : bool = True) -> dict[str, typing.Any]:
    if (len(files) == 0) and len(addtl_text) == 0: # If you specify any text, input files are optional -- note, not documented, used for cmd line app
        print("Error: No input files. Exiting.")
        res = {
            "fonts" : {},
            "chars": set(),
            "uranges": ""
        }
        return res
    
    chars : set[str] = { " " }
    if addtl_text:
        for c in addtl_text:
            chars.add(c)

    font_files : set[str] = set()
    for f in fonts: # user-specified input font files
        font_files.add(f)

    for f in files:
        if not path.exists(f):
            continue  # Skip missing files silently for performance
        file_ext = pathlib.Path(f).suffix.lower()
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            if file_ext == '.html' or file_ext == '.htm':
                soup = BeautifulSoup(content, 'html.parser')
                piece = soup.get_text()
            else: # not HTML, treat as text
                piece = content
            for c in piece:
                chars.add(c)

    # Sanity check that there is any text to process
    if len(chars) <= 1:
        print("Error: No text found in the input files or additional text. Exiting.")
        res = {
            "fonts" : {},
            "chars": set(),
            "uranges": ""
        }
        return res

    chars = _apply_special_characters(chars)

    if verbose:
        print("Found the following fonts:")
        for font_file in font_files:
            print("  " + font_file)

    if len(font_files) == 0:
        print("Error: No fonts found in the input files. Exiting.")
        res = {
            "fonts" : {},
            "chars": set(),
            "uranges": ""
        }
        return res

    res = optimise_fonts(chars, list(font_files), fontpath=font_output_dir, subsetname=subsetname, verbose=verbose, print_stats=print_stats, cjk_only=cjk_only, parallel=parallel)
    return res;


# Note that unit tests for this file are in tests.py; run that file to run the tests
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Optimize fonts to only the specific glyphs needed for your text or HTML files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    fontimize.py 1.html 2.txt
    fontimize.py --outputdir output --subsetname MySubset --verbose 1.html 2.txt
    fontimize.py --text "The fonts will contain only the glyphs in this string" --fonts "Arial.tff" "Times New Roman.ttf"
                """)
    
    parser.add_argument('inputfiles', default=[], nargs='*', help='Input files to parse: .htm and .html are parsed as HTML to extract used text, all other files are treated as text')
    parser.add_argument('-t', '--text', type=str, help='Input text to parse, specified directly on the command line')
    parser.add_argument('-f', '--fonts', default=[], nargs='*', help='Input font files')

    group_output = parser.add_argument_group('Output', 'Specify font output directory and font subset phrase in the generated filenames')
    group_output.add_argument("-o", "--outputdir", type=str, 
                        help="Directory in which to place the generated font files (default is the same directory as the original font files)",
                        default="")
    group_output.add_argument("-s", "--subsetname", type=str, 
                        help="Phrase used in the output font filenames, eg 'Arial.SubsetName.ttf'",
                        default="FontimizeSubset")
    
    group_verb = parser.add_argument_group('Verbosity', 'Control how much Fontimize prints to the console')
    group_verb.add_argument("-v", "--verbose", help="Output significant / diagnostic info about discovered files and fonts, and generated fonts and their glyphs",
                    action="store_true")
    group_verb.add_argument("-n", "--nostats", help="Do not output info about the sizes of the original and generated fonts and the amount of space saved (shown by default)",
                    action="store_true")
    group_verb.add_argument("--no-cjk-only", help="Disable filtering to only CJK characters (default: enabled for East Asian optimization)",
                    action="store_true")

    args = parser.parse_args()

    # If both --text and inputfiles are specified, give an error
    if args.text and args.inputfiles:
        print("Error: Both --text and input files cannot be specified at the same time.")
        sys.exit(1)
     
    # If neither --text nor inputfiles are specified, give an error
    if not args.text and not args.inputfiles:
        print("Error: Either --text or input files must be specified.")
        sys.exit(1)

    _addtl_text = ""
    if args.text:
        _addtl_text = args.text

    # If inputfiles are specified, test they exist
    _inputfiles = []
    if args.inputfiles:
        for file in args.inputfiles:
            if not os.path.exists(file):
                print(f"Error: Input file '{file}' does not exist.")
                sys.exit(1)
        _inputfiles = args.inputfiles

    # If fonts are specified, test they exist
    _fonts = []
    if args.fonts:
        for file in args.fonts:
            if not os.path.exists(file):
                print(f"Error: Font file '{file}' does not exist.")
                sys.exit(1)
        _fonts = args.fonts

    # If outputdir is specified, test it exists
    _outputdir = ""
    if args.outputdir:
        if not os.path.exists(args.outputdir):
            print(f"Error: Output directory '{args.outputdir}' does not exist.")
            sys.exit(1)
        _outputdir = args.outputdir

    # Validate subsetname
    _subsetname = args.subsetname
    try:
        validate_filename(_subsetname)
    except ValidationError as e:
        print(f"Error: Subset name '{_subsetname}' is not valid: {e}")
        sys.exit(1)

    _verbose = args.verbose
    
    _printstats = not args.nostats

    _cjk_only = not args.no_cjk_only

    res = optimise_fonts_for_files(_inputfiles,
                                   font_output_dir=_outputdir, 
                                   subsetname=_subsetname, 
                                   verbose=_verbose, 
                                   print_stats=_printstats, 
                                   fonts=_fonts, 
                                   addtl_text=_addtl_text,
                                   cjk_only=_cjk_only,
                                   parallel=True)
    
    if args.verbose:              
        print("Done.")
