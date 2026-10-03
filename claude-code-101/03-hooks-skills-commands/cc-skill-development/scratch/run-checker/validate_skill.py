#!/usr/bin/env python3
"""validate_skill.py — the skill's definition of done.

Rules (from Anthropic's own plugin-dev skill-development SKILL.md):
  1. Frontmatter with `name:` and `description:`
  2. Description must be third-person, i.e. start with "This skill should be used"
  3. Description must contain at least TWO trigger phrases in double quotes
  4. Body must not contain second-person forms: "you should", "you need", "you can"
  5. Body must reference csv_shape.py so Claude knows to use it
  6. Body must be 200-2000 words (progressive disclosure)
"""
import re, sys, pathlib

def main(path: str) -> int:
    p = pathlib.Path(path)
    if not p.exists():
        print(f"FAIL: {path} does not exist"); return 1
    text = p.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        print("FAIL: no YAML frontmatter"); return 1
    front, body = m.group(1), m.group(2)
    fails = 0
    if not re.search(r"^name:\s*\S", front, re.M):
        print("FAIL: no name in frontmatter"); fails += 1
    desc_match = re.search(r"^description:\s*(.+?)(?=\n[a-z_]+:|\Z)", front, re.M | re.S)
    if not desc_match:
        print("FAIL: no description in frontmatter"); fails += 1
        desc = ""
    else:
        desc = desc_match.group(1).strip()
    if desc and not re.search(r"this skill should be used", desc, re.I):
        print("FAIL: description not third-person"); fails += 1
    triggers = re.findall(r'"[^"]{3,}"', desc)
    if len(triggers) < 2:
        print(f"FAIL: description has {len(triggers)} trigger phrases; need >= 2"); fails += 1
    body_low = body.lower()
    for phrase in ("you should", "you need", "you can", "you must", "you may"):
        if phrase in body_low:
            print(f"FAIL: body uses second-person: '{phrase}'"); fails += 1
    if "csv_shape.py" not in body:
        print("FAIL: body does not reference csv_shape.py"); fails += 1
    words = len(re.findall(r"\S+", body))
    if not (200 <= words <= 2000):
        print(f"FAIL: body is {words} words; need 200-2000"); fails += 1
    if fails == 0:
        print(f"PASS: {path} meets all six rules ({words} words)"); return 0
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "skills/csv-shape/SKILL.md"))
