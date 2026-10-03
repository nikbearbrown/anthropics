#!/usr/bin/env python3
"""Per-turn cache_creation, so we can attribute new tokens to actions."""
import json, sys, os

def analyze(path):
    print(f"=== {os.path.basename(path)} ===")
    for line in open(path):
        if not line.strip(): continue
        try: j = json.loads(line)
        except Exception: continue
        if j.get("type") != "assistant": continue
        m = j.get("message", {})
        u = m.get("usage", {}) or {}
        cc = u.get("cache_creation_input_tokens", 0)
        if cc == 0: continue
        actions = []
        for c in m.get("content", []):
            if c.get("type") == "text":
                txt = c.get("text","").strip().splitlines()
                if txt: actions.append(("TEXT", txt[0][:60]))
            if c.get("type") == "tool_use":
                name = c.get("name")
                args = c.get("input", {}) or {}
                if name == "Read":
                    fp = args.get("file_path","?")
                    actions.append(("Read", os.path.basename(fp)))
                elif name in ("Agent","Task"):
                    actions.append(("SUBAGENT", args.get("description","?")))
                elif name == "Edit":
                    fp = args.get("file_path","?")
                    actions.append(("Edit", os.path.basename(fp)))
                elif name == "Write":
                    fp = args.get("file_path","?")
                    actions.append(("Write", os.path.basename(fp)))
                elif name == "Bash":
                    actions.append(("Bash", (args.get("command","") or "")[:40]))
                else:
                    actions.append((name, ""))
        print(f"  +{cc:6d} tokens :: {actions}")

for p in sys.argv[1:]:
    analyze(p)
    print()
