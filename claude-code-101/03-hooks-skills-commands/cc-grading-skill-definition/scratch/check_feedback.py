#!/usr/bin/env python3
"""check_feedback.py — the skill's definition of done.

Fails a feedback file if it assigns any final grade (letter, percent,
X/N, X pass/Y needs work), or if any rubric heading or Growth is missing.
"""
import re, sys, pathlib

REQUIRED = ["Mechanism", "Example", "Argument", "Precision"]
BAD = [
    (re.compile(r"^#+\s*Final grade", re.I | re.M), "'Final grade' heading"),
    (re.compile(r"\b[A-DF][+\-]?\s*(?:$|\-|\s+—)", re.M), "letter grade"),
    (re.compile(r"\b\d{1,3}\s*%"), "percent"),
    (re.compile(r"\b\d{1,3}\s*/\s*\d{1,3}\b"), "X/N score"),
    (re.compile(r"\b\d+\s+pass\b", re.I), "aggregated pass count"),
]

def check(path: pathlib.Path) -> int:
    text = path.read_text()
    for heading in REQUIRED:
        if heading.lower() not in text.lower():
            print(f"FAIL: missing heading '{heading}' in {path.name}")
            return 1
    if "growth" not in text.lower():
        print(f"FAIL: missing Growth section in {path.name}")
        return 1
    for pat, kind in BAD:
        m = pat.search(text)
        if m:
            print(f"FAIL: {kind} in {path.name} — '{m.group(0).strip()}'")
            return 1
    print(f"PASS: {path.name} — rubric complete, no grade, Growth named.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_feedback.py feedback/<name>.md"); sys.exit(2)
    sys.exit(check(pathlib.Path(sys.argv[1])))
