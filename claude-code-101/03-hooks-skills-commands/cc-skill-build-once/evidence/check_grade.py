#!/usr/bin/env python3
"""check_grade.py — the grading-workflow skill's definition of done.

Reads a feedback markdown file and enforces the shape the skill promises:
four rubric headings, a bolded verdict on each, a Growth line, no letter
grade, no numeric grade. Prints PASS or FAIL and exits 0/1.
"""
import re, sys, pathlib

def check(path: str) -> tuple[bool, list[str]]:
    text = pathlib.Path(path).read_text()
    fails: list[str] = []
    for h in ("## 1. Mechanism", "## 2. Example", "## 3. Argument", "## 4. Precision of language"):
        if h not in text:
            fails.append(f"missing heading: {h}")
    if text.count("**pass**") + text.count("**needs work**") < 4:
        fails.append("need four bolded verdicts (**pass** or **needs work**)")
    if "## Growth" not in text:
        fails.append("missing Growth heading")
    if re.search(r"\b[Gg]rade\s*[:\-]\s*[A-DF][+\-]?\b", text) or re.search(r"\b[A-DF][+\-]?\s*\(", text):
        fails.append("letter grade present — this skill is feedback-only")
    if re.search(r"\b\d{1,3}\s*/\s*100\b", text) or re.search(r"\b\d{1,3}\s*%\b", text):
        fails.append("numeric grade present — this skill is feedback-only")
    return (not fails, fails)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_grade.py <feedback-file>"); sys.exit(2)
    ok, fails = check(sys.argv[1])
    if ok:
        print("PASS")
    else:
        for f in fails: print(f"FAIL: {f}")
    sys.exit(0 if ok else 1)
