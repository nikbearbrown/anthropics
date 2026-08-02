## sdk-python-examples-thinking

- **Source path:** anthropic-sdk-python/examples/thinking.py
- **Teachable claim:** Extended thinking in the Python SDK is two parameters — `thinking={"type": "enabled", "budget_tokens": N}` — and the response contains a `thinking` content block before the answer; the budget controls how much thinking Claude does, trading cost for accuracy on hard problems.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The two parameters: `thinking` dict and `budget_tokens` — shown in context of a hard logic puzzle
2. Thinking block in raw output: the unpolished scratchpad text before the final answer
3. Budget sweep: same puzzle with `budget_tokens=1024` vs. `16000` — accuracy and cost compared
4. When to use: the tasks where thinking helps (multi-step reasoning, math) vs. where it doesn't (simple lookups)

### Score
- Teachability: 4/5 — budget_tokens as a cost-accuracy knob is the practical lesson
- Visual: 3/5 — terminal output with thinking block is functional
- Pull: 4/5 — extended thinking is one of the most-asked-about Claude features
- Freshness: 4/5 — extended thinking is still new; the budget-tuning angle is underexplored
- **Total: 15/20**
