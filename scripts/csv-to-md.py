#!/usr/bin/env python3

# © 2025. This program is free software: you can
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

import sys
import os
import csv
import re
from datetime import datetime, timezone

MARKER = "<!-- Anything"  # stop copying preface after this line
LAST_MODIFIED_KEY = "last_modified_at:"

def escape_markdown_cell(cell: str) -> str:
    """Escape pipes in markdown table cells."""
    return cell.replace("|", "\\|")

def update_last_modified(lines: list, filename: str) -> list:
    """Update last_modified_at line; error if not found."""
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    found_key = False
    updated_lines = []
    for line in lines:
        if line.strip().startswith(LAST_MODIFIED_KEY):
            updated_lines.append(f"{LAST_MODIFIED_KEY} {timestamp}\n")
            found_key = True
        else:
            updated_lines.append(line)
    if not found_key:
        raise RuntimeError(f"'{LAST_MODIFIED_KEY}' not found in {filename}")
    return updated_lines

def update_markdown_from_csv(csv_path: str, counts: dict):
    base_name = os.path.splitext(os.path.basename(csv_path))[0]

    md_path = os.path.join("build", f"{base_name}.md")

    preface_lines = []
    marker_found = False
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf8") as md_file:
            for line in md_file:
                preface_lines.append(line)
                if MARKER in line:
                    marker_found = True
                    break

    if not marker_found:
        raise RuntimeError(f"Marker '{MARKER}' not found in {md_path}")

    os.makedirs(os.path.dirname(md_path), exist_ok=True)

    with open(csv_path, "r", encoding="utf8", newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    if (len(base_name) == 1 and 'a' <= base_name <= 'z') or base_name == 'letter':
        count = sum(1 for row in rows[1:] if row and row[0] != '')
        label = base_name.upper() if len(base_name) == 1 else 'Lettered'
        counts[label] = count

    table_lines = []
    if rows:
        header = [escape_markdown_cell(cell) for cell in rows[0]]
        table_lines.append("|".join(header) + "|\n")
        table_lines.append("|".join("---" for _ in header) + "|\n")
        for row in rows[1:]:
            escaped_row = [escape_markdown_cell(cell) for cell in row]
            table_lines.append("|".join(escaped_row) + "|\n")

    preface_lines = update_last_modified(preface_lines, md_path)

    with open(md_path, "w", encoding="utf8") as md_file:
        md_file.writelines(preface_lines)
        md_file.write("\n")
        md_file.writelines(table_lines)

def update_readme(counts: dict):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return

    with open(readme_path, "r", encoding="utf8") as f:
        lines = f.readlines()

    content = "".join(lines)
    for label, count in counts.items():
        pattern = re.compile(r'{}\s*\(([^)]*)\)'.format(re.escape(label)))
        content, _ = pattern.subn(f"{label} ({count})", content)

    updated_lines = update_last_modified(content.splitlines(keepends=True), readme_path)

    with open(readme_path, "w", encoding="utf8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: csv-to-md.py file1.csv [file2.csv ...]")

    counts = {}
    for csv_filename in sys.argv[1:]:
        update_markdown_from_csv(csv_filename, counts)

    update_readme(counts)
