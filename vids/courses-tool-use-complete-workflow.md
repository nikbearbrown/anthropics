## courses-tool-use-complete-workflow

- **Source path:** courses/tool_use/04_complete_workflow.ipynb
- **Teachable claim:** A complete tool-use workflow — define tools, get Claude's tool call, execute the function, return results, get final answer — requires a loop because Claude may call multiple tools in sequence before it has everything it needs to answer.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. The loop structure: while `stop_reason == "tool_use"`: execute → append result → call again → final answer
2. Multi-tool chain: Claude calls weather tool, reads result, decides to call time tool, then answers — two-tool sequence
3. Code: the minimal loop in 15 lines with annotation — the reusable agentic scaffold
4. Error handling: what to return when a tool fails and how Claude responds to a failed tool result

### Score
- Teachability: 5/5 — the while-loop is the one piece that trips up every tool-use beginner
- Visual: 4/5 — the loop structure diagram makes the protocol tangible
- Pull: 5/5 — anyone building agentic Claude code hits this
- Freshness: 2/5 — established pattern, but this is the cleanest tutorial presentation
- **Total: 16/20**
