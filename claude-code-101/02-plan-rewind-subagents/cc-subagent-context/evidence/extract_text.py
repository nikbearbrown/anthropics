#!/usr/bin/env python3
"""Extract the subagent's returned text and the main session's key sentences."""
import json, sys

path = sys.argv[1]
for line in open(path):
    if not line.strip(): continue
    try: j = json.loads(line)
    except Exception: continue
    t = j.get("type")
    if t == "user":
        m = j.get("message", {})
        content = m.get("content", [])
        if isinstance(content, list):
            for c in content:
                if c.get("type") == "tool_result":
                    tc = c.get("content", "")
                    if isinstance(tc, list):
                        for x in tc:
                            if x.get("type") == "text":
                                tc = x.get("text",""); break
                    if isinstance(tc, str) and ("grace" in tc.lower() or "late" in tc.lower()) and len(tc) > 200 and "@@" not in tc:
                        print("---- SUBAGENT RETURN ----"); print(tc); print()
    if t == "assistant":
        m = j.get("message", {})
        for c in m.get("content", []):
            if c.get("type") == "text":
                txt = c.get("text","").strip()
                if txt:
                    print("---- CLAUDE (main) ----"); print(txt); print()
            if c.get("type") == "tool_use" and c.get("name") in ("Agent","Task"):
                args = c.get("input",{}) or {}
                print("---- AGENT CALL ----")
                print("desc:", args.get("description"))
                print("prompt:", (args.get("prompt","")[:500]))
                print()
