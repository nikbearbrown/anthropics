#!/usr/bin/env python3
"""PreToolUse hook: block Write/Edit/MultiEdit whose new content contains a final letter grade."""
import json, re, sys

LETTER = r'(?<![A-Za-z])[ABCDF][+-]?(?![A-Za-z])'
PATTERNS = [
    # Labeled: "grade: A", "Overall: B+", "Final grade — C-", "**Overall:** A"
    re.compile(rf'\b(?:grade|overall|final)\b[^\n:=\-]{{0,40}}[:=\-][^A-Za-z0-9\n]{{0,5}}{LETTER}', re.IGNORECASE),
    # Any line that mentions "grade" and contains a standalone letter grade
    re.compile(rf'(?im)^[^\n]*\bgrade\b[^\n]*?{LETTER}[^\n]*$'),
]

def new_text(ti):
    parts = [ti.get('content') or '', ti.get('new_string') or '']
    for e in ti.get('edits') or []:
        parts.append(e.get('new_string') or '')
    return '\n'.join(p for p in parts if p)

def main():
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        print(f"block-grades: bad JSON on stdin ({e})", file=sys.stderr)
        sys.exit(0)
    text = new_text(data.get('tool_input') or {})
    if not text:
        sys.exit(0)
    for p in PATTERNS:
        m = p.search(text)
        if m:
            snippet = m.group(0).strip().replace('\n', ' ')[:120]
            print(f"block-grades: refusing to write a final letter grade -> {snippet!r}", file=sys.stderr)
            sys.exit(2)

if __name__ == '__main__':
    main()
