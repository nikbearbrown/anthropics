#!/usr/bin/env python3
"""fixture.py — the DOM contract for workshop.html. Definition of done from PROJECT/brief.md."""
import re, sys, pathlib
p = pathlib.Path("workshop.html")
if not p.exists():
    print("FAIL: workshop.html missing"); sys.exit(1)
h = p.read_text()
def fail(msg): print("FAIL:", msg); sys.exit(1)

# No external assets — the page is self-contained.
if re.search(r'<(link|script)\b[^>]*\bsrc=|<link\b[^>]*\bhref=', h):
    if not re.search(r'<link\b[^>]*rel="icon"', h):
        fail("external <link>/<script> src or href (no external assets)")

# Fixed-width type (the tool it teaches).
if not re.search(r"font-family:[^;]*(monospace|Courier|Menlo|Monaco|Consolas)", h, re.I):
    fail("no monospace font-family (voice: terminal)")

# One <h1>, exactly one.
h1s = re.findall(r"<h1\b", h)
if len(h1s) != 1: fail(f"want exactly one <h1>, got {len(h1s)}")

# A form with a #register submit and a name field only (no email wall).
if not re.search(r'<form\b', h): fail("no <form>")
if re.search(r'type=["\']email["\']|name=["\']email["\']', h):
    fail("email field forbidden (no sign-up wall)")
if not re.search(r'id=["\']register["\']|name=["\']register["\']', h):
    fail("no #register control")
if not re.search(r'<input\b[^>]*name=["\']name["\']', h):
    fail("missing <input name=\"name\">")

# Banned words (voice: dry, no ad copy).
for banned in ("welcome", "amazing", "awesome", "join us", "excited"):
    if re.search(rf"\b{banned}\b", h, re.I):
        fail(f"banned word: {banned}")

# Under 200 lines (design brief).
n = len(h.splitlines())
if n > 200: fail(f"{n} lines > 200 (brief: keep it small)")

print(f"PASS: workshop.html meets brief.md's definition of done ({n} lines)")
