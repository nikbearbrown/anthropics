## cookbooks-memory-context-editing

- **Source path:** claude-cookbooks/tool_use/memory_cookbook.ipynb
- **Teachable claim:** Claude 4 models have a native memory tool and context editing system — `memory_20250818` writes cross-session notes to `/memories`, while `clear_tool_uses` and `clear_thinking` automatically prune the context before it overflows.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Diagram: agent across sessions without memory (re-explains from scratch) vs. with memory (reads notes, continues)
2. Memory tool output: the file written to `/memories/` shown in the terminal after a session
3. Context editing trigger: token counter hits the threshold → tool results cleared → agent keeps going
4. Code review assistant demo: agent notes style preferences across sessions, applies them next time

### Score
- Teachability: 5/5 — solves the #1 agent complaint (amnesia between sessions)
- Visual: 4/5 — before/after session behavior is dramatically different on screen
- Pull: 5/5 — every long-running agent builder needs this
- Freshness: 5/5 — memory tool is new in Claude 4 family
- **Total: 19/20**
