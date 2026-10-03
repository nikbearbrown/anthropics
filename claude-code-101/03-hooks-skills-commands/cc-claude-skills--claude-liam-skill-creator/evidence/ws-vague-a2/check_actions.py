#!/usr/bin/env python3
"""actions.md's definition of done: every line is `- <owner> — <what> — by <when>|ongoing`."""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "actions.md")
if not p.exists():
    print("FAIL: actions.md not found"); sys.exit(1)
lines = [l.rstrip() for l in p.read_text().splitlines() if l.strip()]
if not lines:
    print("FAIL: actions.md is empty"); sys.exit(1)
row = re.compile(r"^- [A-Z][a-z]+ — .+ — (by .+|ongoing)$")
bad = [l for l in lines if not row.match(l)]
if bad:
    print(f"FAIL: {len(bad)} row(s) not in `- <Owner> — <what> — by <when>` shape")
    for b in bad[:3]: print(f"  offending: {b[:80]}")
    sys.exit(1)
print(f"PASS: {len(lines)} action(s), every one has owner, task, and due date.")
