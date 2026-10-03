#!/usr/bin/env python3
"""Read a run's stream-json and report main-session token usage.

The key metric: what the MAIN session had to hold. In stream-json, every
assistant turn carries usage {input_tokens, cache_creation_input_tokens,
cache_read_input_tokens, output_tokens}. We report the peak input
(cache_creation + cache_read + input) of the last MAIN assistant turn —
that is the size of the main context on its last thinking pass. Sidebar
messages from subagents (type=user with subtype='tool_result') don't
carry usage; the Task tool's return summary is the only text that
enters the main context, which is exactly the point of the film.

Also lists the tools called at the top level (Read/Task/Edit/Write/Bash).
"""
import json, sys, os

path = sys.argv[1]
turns = []
tools = []
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
        u = m.get("usage", {})
        content = m.get("content", [])
        for c in content:
            if c.get("type") == "tool_use":
                tools.append((c.get("name"), c.get("input", {}) or {}))
        if u:
            turns.append(u)
    if t == "result":
        result = j

if not turns:
    print("no assistant turns", file=sys.stderr); sys.exit(1)
last = turns[-1]
total_in = last.get("input_tokens", 0) + last.get("cache_creation_input_tokens", 0) + last.get("cache_read_input_tokens", 0)
peak_ctx = max((u.get("input_tokens",0)+u.get("cache_creation_input_tokens",0)+u.get("cache_read_input_tokens",0)) for u in turns)
print(f"run: {os.path.basename(path)}")
print(f"assistant turns: {len(turns)}")
print(f"peak main-context input tokens: {peak_ctx}")
print(f"last-turn main-context input tokens: {total_in}")
print(f"total output tokens: {sum(u.get('output_tokens',0) for u in turns)}")
print(f"tool calls (main session, in order):")
seen_read = 0
for name, args in tools:
    if name == "Read":
        seen_read += 1
        p = args.get("file_path", "?")
        print(f"  Read  {os.path.relpath(p, os.getcwd()) if os.path.isabs(p) else p}")
    elif name == "Task":
        desc = args.get("description", "?")
        prompt = (args.get("prompt", "") or "").splitlines()[0][:80]
        print(f"  Task  {desc}  |  {prompt}")
    elif name == "Bash":
        cmd = (args.get("command", "") or "").splitlines()[0][:80]
        print(f"  Bash  {cmd}")
    else:
        print(f"  {name}  {list(args)[:3]}")
print(f"Read calls: {seen_read}")
try:
    r = result
    print(f"turns={r.get('num_turns')} duration_ms={r.get('duration_ms')} cost=${r.get('total_cost_usd',0):.3f}")
except Exception:
    pass
