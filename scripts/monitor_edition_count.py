#!/usr/bin/env python3

import os
import re
import sys
import requests
from lxml import html

README      = os.path.join(os.getcwd(), "README.md")
WIKI_URL    = "https://github.com/t18d/HuangSupplement/wiki/Checklist-of-Editions"

def fetch_count() -> int:
    resp = requests.get(
        WIKI_URL,
        headers={"User-Agent": "edition-count-monitor/1.0"},
        timeout=5,
    )
    resp.raise_for_status()
    tree = html.fromstring(resp.content)
    return len(tree.xpath('//h2[@class="heading-element"]'))

def rewrite_readme(count: int) -> bool:
    link       = f'<a href="{WIKI_URL}">Checklist of Editions</a>'
    pattern    = re.compile(re.escape(link) + r"\s*\(\d+\)<br>")
    new_link   = f"{link} ({count})<br>"

    with open(README, encoding="utf-8") as f:
        content = f.read()

    updated, subs = pattern.subn(new_link, content)
    if subs == 0:
        unnum = link + "<br>"
        if unnum in content:
            updated = content.replace(unnum, new_link)
        else:
            updated = content.rstrip() + "\n\n" + new_link

    if updated == content:
        return False

    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)
    return True

def write_github_output(changed: bool, edition_count: int):
    out = os.getenv("GITHUB_OUTPUT")
    if not out:
        sys.exit(1)
    with open(out, "a") as fh:
        fh.write(f"changed={str(changed).lower()}\n")
        fh.write(f"edition_count={edition_count}\n")

def main():
    try:
        edition_count = fetch_count()
        changed = rewrite_readme(edition_count)
        write_github_output(changed, edition_count)   
        if not changed:
            sys.exit(1)
    except Exception as e:
        print(f"::error::{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
