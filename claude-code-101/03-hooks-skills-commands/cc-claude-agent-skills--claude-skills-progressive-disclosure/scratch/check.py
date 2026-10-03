#!/usr/bin/env python3
"""check.py — enforce the exec-summary shape on summary.md."""
import sys, re, pathlib
path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "summary.md")
if not path.exists():
    print(f"FAIL: {path} missing"); sys.exit(1)
text = path.read_text()
want = ["## What", "## Why it matters", "## What's new", "## What to do"]
heads = re.findall(r"^## .+$", text, re.M)
if heads != want:
    print(f"FAIL: headings — got {heads}"); sys.exit(1)
FORBID = ["welcome", "seamless", "robust", "leverage", "synergy", "delight"]
for w in FORBID:
    if re.search(rf"\b{w}\b", text, re.I):
        print(f"FAIL: forbidden word {w!r}"); sys.exit(1)
if "!" in text:
    print("FAIL: exclamation mark"); sys.exit(1)
print("PASS")
