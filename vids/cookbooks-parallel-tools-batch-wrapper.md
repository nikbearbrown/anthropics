## cookbooks-parallel-tools-batch-wrapper

- **Source path:** claude-cookbooks/tool_use/parallel_tools.ipynb
- **Teachable claim:** Claude 3.7 Sonnet is less likely to make parallel tool calls even when you've enabled them — a "batch tool" meta-wrapper that accepts an array of tool calls forces the model to fan out all required tools in a single turn.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Without batch tool: two sequential round-trips (weather → time → answer) — timeline showing added latency
2. With batch tool: one round-trip with both calls inside the batch — parallel execution diagram
3. Batch tool schema: the minimal wrapper tool definition in code
4. Latency comparison: wall-clock for sequential vs. parallel on a multi-tool query

### Score
- Teachability: 4/5 — a non-obvious workaround with a clear performance payoff
- Visual: 4/5 — sequential vs. parallel timeline is immediately legible
- Pull: 4/5 — anyone building tool-heavy agents benefits from this
- Freshness: 4/5 — the batch-wrapper pattern is not widely documented
- **Total: 16/20**
