#!/usr/bin/env python3
"""Parse a hookify rule file and check it against the schema in SKILL.md."""
import re, sys, pathlib
def parse(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m: return None
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    key = None
    for line in fm_raw.splitlines():
        if re.match(r"^[a-z_]+:", line):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
            key = k.strip()
    return fm, body
def main():
    p = pathlib.Path(sys.argv[1])
    text = p.read_text()
    r = parse(text)
    if not r:
        print("FAIL: no YAML frontmatter"); sys.exit(1)
    fm, body = r
    fails = []
    for f in ("name","enabled","event"):
        if f not in fm: fails.append(f"missing {f}")
    if "pattern" not in fm and "conditions" not in text: fails.append("no pattern or conditions")
    if not body.strip(): fails.append("empty message body")
    if not p.name.startswith("hookify.") or not p.name.endswith(".local.md"):
        fails.append(f"filename {p.name} not hookify.<name>.local.md")
    if fails:
        for f in fails: print("FAIL:", f)
        sys.exit(1)
    print(f"PASS: hookify rule '{fm.get('name')}' schema OK — {p.name}")

if __name__ == "__main__":
    main()
