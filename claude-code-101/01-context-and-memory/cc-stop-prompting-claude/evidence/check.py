#!/usr/bin/env python3
"""check.py — Bear's voice rules, as a script. Argv: one or more text files.
Prints FAIL:<rule> for every violation, then PASS or FAIL total per file."""
import re, sys, unicodedata

BANNED_WORDS = ["delve","leverage","robust","unlock","empower","unleash","harness"]
BANNED_PHRASES = ["I hope this finds you well","excited to announce","in today's world"]
BANNED_ADDRESS = ["students","folks","team","y'all","everyone","hi all","hey all"]
BAD_SIGNOFF = ["Prof. Brown","Prof Brown","Dr. Brown","Dr Brown"]
GOOD_SIGNOFF = "— Bear"

def has_emoji(s):
    for ch in s:
        if unicodedata.category(ch) == "So": return True
        cp = ord(ch)
        if 0x1F300 <= cp <= 0x1FAFF: return True
    return False

def check(path):
    text = open(path).read()
    fails = []
    if "!" in text: fails.append("exclamation")
    if has_emoji(text): fails.append("emoji")
    low = text.lower()
    for w in BANNED_WORDS:
        if re.search(r"\b"+w+r"\b", low): fails.append("word:"+w)
    for p in BANNED_PHRASES:
        if p.lower() in low: fails.append("phrase:"+p)
    for a in BANNED_ADDRESS:
        if re.search(r"\b"+re.escape(a)+r"\b", low): fails.append("address:"+a)
    for s in BAD_SIGNOFF:
        if s in text: fails.append("signoff:"+s)
    if GOOD_SIGNOFF not in text: fails.append("missing:sign-as-— Bear")
    if any(h in text for h in ["# ","## ","**","- "]): fails.append("markdown")
    return fails

if __name__ == "__main__":
    for p in sys.argv[1:]:
        f = check(p)
        for x in f: print(f"FAIL: {p}: {x}")
        print(f"{'FAIL' if f else 'PASS'}: {p}")
