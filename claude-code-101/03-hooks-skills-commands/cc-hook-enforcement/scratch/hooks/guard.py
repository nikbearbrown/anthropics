#!/usr/bin/env python3
"""PreToolUse guard — blocks a Write or Edit whose content contains a final
letter grade. Reads the tool call as JSON on stdin. Exit 2 tells Claude Code
to block the tool call and shows the message on stderr to the agent."""
import json, re, sys

PAT = re.compile(
    r"(final\s+grade|overall\s+grade|overall\s+performance|suggested\s+grade|grade)"
    r"\s*[:\-]?\s*[A-F][+-]?\b",
    re.IGNORECASE,
)

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

tool = payload.get("tool_name", "")
inp = payload.get("tool_input", {}) or {}
if tool not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)

text = ""
if tool == "Write":
    text = inp.get("content", "") or ""
elif tool == "Edit":
    text = (inp.get("new_string", "") or "") + "\n" + (inp.get("old_string", "") or "")
elif tool == "MultiEdit":
    for e in inp.get("edits", []) or []:
        text += (e.get("new_string", "") or "") + "\n"

m = PAT.search(text)
if not m:
    sys.exit(0)

msg = (
    "BLOCKED by PreToolUse hook (hooks/guard.py): the content contains a "
    f"final letter grade pattern: {m.group(0)!r}. CLAUDE.md forbids assigning "
    "grades. Rewrite without any letter grade and try again."
)
print(msg, file=sys.stderr)
sys.exit(2)
