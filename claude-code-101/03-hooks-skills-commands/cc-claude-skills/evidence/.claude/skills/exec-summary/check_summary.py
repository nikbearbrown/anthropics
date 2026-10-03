#!/usr/bin/env python3
"""check_summary.py — definition of done for the exec-summary skill.
Usage: python3 check_summary.py summary.md
Prints PASS or the first FAIL line."""
import re, sys, pathlib

def check(p: pathlib.Path) -> str:
    if not p.exists():
        return f"FAIL: {p} does not exist"
    text = p.read_text(encoding="utf-8")
    needed = ["## What", "## Why it matters", "## What's new", "## What to do"]
    for h in needed:
        if h not in text:
            return f"FAIL: missing heading '{h}'"
    order = [text.index(h) for h in needed]
    if order != sorted(order):
        return "FAIL: headings out of order"
    if re.search(r"\b\d{1,3}\s*/\s*\d{1,3}\b|\b\d{1,3}%\b|Grade:\s*[A-DF][+\-]?", text):
        return "FAIL: numeric rating or letter grade found"
    if re.search(r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF]", text):
        return "FAIL: emoji found"
    if re.search(r"^\s*TL;DR", text, flags=re.MULTILINE|re.IGNORECASE):
        return "FAIL: TL;DR line before sections"
    if re.search(r"\bstar\s?rating\b|★|☆", text):
        return "FAIL: star rating found"
    return "PASS"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: check_summary.py <path>")
    print(check(pathlib.Path(sys.argv[1])))
