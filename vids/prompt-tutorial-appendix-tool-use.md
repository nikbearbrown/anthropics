## prompt-tutorial-appendix-tool-use

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/10.2_Appendix_Tool Use.ipynb
- **Teachable claim:** Tool use is not just for calling APIs — it's the fundamental mechanism that lets Claude interact with the outside world deterministically; understanding the four-message loop (user → assistant:tool_call → user:tool_result → assistant:final) is the prerequisite for all agent work.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The four-message loop animated: user asks → Claude emits tool_call → code runs → result returned → final answer
2. Tool definition schema: `name`, `description`, `input_schema` — the three fields Claude uses to decide when to call
3. Multi-tool example: Claude picks the right tool from a set, explaining its reasoning
4. Tool call + result in raw JSON: showing developers exactly what's in the messages array at each step

### Score
- Teachability: 5/5 — the four-message loop is the one thing every agent developer must understand
- Visual: 4/5 — the loop animation makes the protocol tangible
- Pull: 5/5 — tool use is the gateway to all agentic Claude work
- Freshness: 3/5 — established but still a common stumbling block
- **Total: 17/20**
