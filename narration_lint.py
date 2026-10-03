#!/usr/bin/env python3
"""narration_lint.py <beat_sheet.json> [book_title]

The STANDALONE-IDEA LAW, made mechanical. Prose in a prompt loses to 1,200 lines of
book-shaped skill files and a chapter that names itself in its first sentence; a gate
does not. Exit 0 = clean, 1 = violations (the reel is not review-ready).

HARD set = unambiguous book apparatus. SOFT set = reported, never fatal, because a
phrase like "rubric-anchored critique" can be a legitimate citation rather than
course apparatus.
"""
import json, re, sys

HARD = [
    (r"\bchapters?\b",                      "says 'chapter'"),
    (r"\bpart (one|two|three|1|2|3)\b",     "part number"),
    (r"\b(this|the) book\b",                "refers to 'the book'"),
    (r"\bthe author\b|\bas we saw\b|\bearlier (?:chapter|we)\b", "back-reference to the text"),
    (r"\bword (count|band)\b|\b\d[,\d]{2,}\s*(?:to|–|-)\s*[\d,]+\s*words?\b", "word count"),
    (r"\bthe (assignment|course)\b|\byou will be graded\b|\bthis (exercise|deliverable)\b",
     "course apparatus addressed to a student"),
]
SOFT = [(r"\brubric\b|\bsubmission\b|\bgrad(e|es|ed|ing)\b", "course-ish wording")]

def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]

def main():
    sheet = sys.argv[1]
    title = sys.argv[2].strip() if len(sys.argv) > 2 and sys.argv[2].strip() else None
    b = json.load(open(sheet))
    pats = list(HARD)
    if title:
        pats.append((r"\b" + re.escape(title) + r"\b", f"names the book ({title})"))
    hard_hits, soft_hits = [], []
    for beat in b.get("beats", []):
        bid = beat.get("beat_id", "?")
        for s in sentences(beat.get("narration_text", "")):
            for rx, lab in pats:
                if re.search(rx, s, re.I):
                    hard_hits.append((bid, lab, s)); break
            for rx, lab in SOFT:
                if re.search(rx, s, re.I):
                    soft_hits.append((bid, lab, s)); break
    for bid, lab, s in soft_hits[:4]:
        print(f"  soft  [{bid}] {lab}: {s[:96]}")
    for bid, lab, s in hard_hits[:8]:
        print(f"  HARD  [{bid}] {lab}: {s[:96]}")
    if hard_hits:
        print(f"  STANDALONE-IDEA LAW: {len(hard_hits)} hard violation(s) — reel is NOT review-ready")
        return 1
    print(f"  STANDALONE-IDEA LAW: clean ({len(soft_hits)} soft note(s))")
    return 0

sys.exit(main())
