#!/usr/bin/env python3
"""check_peek.py — definition of done for csv-peek."""
import sys, re
path = sys.argv[1] if len(sys.argv) > 1 else "peek.md"
txt = open(path).read()
headings = re.findall(r"^## (\w+):", txt, re.M)
required = ["FILE", "ROWS", "COLUMNS", "HEAD"]
if headings[:4] != required:
    print(f"FAIL: heading order {headings[:4]} != {required}")
    sys.exit(1)
rows_line = next((ln for ln in txt.splitlines() if ln.startswith("## ROWS:")), "")
if not re.search(r"## ROWS:\s*\d+", rows_line):
    print("FAIL: ROWS is not a number")
    sys.exit(1)
head_block = txt.split("## HEAD:", 1)[1].strip().splitlines()
if len([ln for ln in head_block if ln.strip()]) < 3:
    print("FAIL: HEAD has fewer than 3 rows")
    sys.exit(1)
print("PASS")
