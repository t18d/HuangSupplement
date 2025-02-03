# © 2023. This program is free software: you can
# redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.txt

import csv
import operator

# read preface so that we can keep it before the table
preface_lines = []
with open("docs/orthography.md", "r", encoding="utf8") as readme:
    for line in readme.readlines():
        preface_lines.append(line)
        if "<!-- Anything" in line:  # 2nd line because we need to keep the line with comment in
            break

# open files to create new readers
with open("orthography.csv", "r", encoding="utf8") as supplement_csv:
    supplement_reader = csv.reader(supplement_csv)
    with open("docs/orthography.md", "w", encoding="utf8") as conj_md:  # WARNING: rewrites the file!
        conj_md.writelines(preface_lines)
        conj_md.write("\n")
        # first line is headers
        first_first_row = True
        first_row = True
        for row in supplement_reader:
            if first_row and not first_first_row:
                first_row = False
                continue
            # [:-1] to remove the unneeded | at the end
            new_row = "".join(col + "|" for col in row)[:-1] + "\n"
            conj_md.write(new_row)
            if first_first_row:
                delimiter_row = "---|" * (len(new_row.split("|")))
                delimiter_row = delimiter_row[:-1] + "\n"  # [:-1] as above
                conj_md.write(delimiter_row)
                first_first_row = False
                # delimiter needs to be written after headers (which are the first row)
                first_row = False
