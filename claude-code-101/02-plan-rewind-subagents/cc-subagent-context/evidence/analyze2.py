#!/usr/bin/env python3
"""Compare what NEW tokens each run added to the main session context."""
import json, sys, os

def analyze(path):
    total_create = 0
    total_output = 0
    policy_reads = 0
    subagent_calls = 0
    subagent_return_words = 0
    turns = 0
    tool_calls = []
    for line in open(path):
        if not line.strip():
            continue
        try:
            j = json.loads(line)
        except Exception:
            continue
        t = j.get("type")
        if t == "assistant":
            m = j.get("message", {})
            u = m.get("usage", {}) or {}
            total_create += u.get("cache_creation_input_tokens", 0)
            total_output += u.get("output_tokens", 0)
            turns += 1
            for c in m.get("content", []):
                if c.get("type") == "tool_use":
                    name = c.get("name")
                    args = c.get("input", {}) or {}
                    tool_calls.append((name, args))
                    if name == "Read":
                        fp = args.get("file_path", "")
                        if "policies/" in fp or "\\policies\\" in fp:
                            policy_reads += 1
                    if name in ("Task", "Agent"):
                        subagent_calls += 1
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
                                    tc = x.get("text", "")
                                    break
                        if isinstance(tc, str) and (
                            "late" in tc.lower() and "grace" in tc.lower()
                        ):
                            subagent_return_words = max(subagent_return_words, len(tc.split()))
    print(f"{os.path.basename(path)}:")
    print(f"  assistant turns: {turns}")
    print(f"  cache_creation TOTAL (new tokens added to main context): {total_create}")
    print(f"  output tokens (assistant thinking/action): {total_output}")
    print(f"  main-session Reads of policies/*.md: {policy_reads}")
    print(f"  Agent/Task (subagent) calls: {subagent_calls}")
    print(f"  words in subagent's summary (returned to main): {subagent_return_words}")

for p in sys.argv[1:]:
    analyze(p)
    print()
