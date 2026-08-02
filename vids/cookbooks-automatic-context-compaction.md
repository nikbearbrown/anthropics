## cookbooks-automatic-context-compaction

- **Source path:** claude-cookbooks/tool_use/automatic-context-compaction.ipynb
- **Teachable claim:** SDK-based automatic context compaction keeps a long-running agent's context window from overflowing by summarizing conversation history at a configurable token threshold — critical for agents on older models or when you want a cheaper model to do the summarizing.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. When to use SDK vs. server-side: Opus 4.6+ → server-side compaction (one flag); older model or custom summarizer model → SDK-based compaction; show the decision tree
2. SDK config: `ClaudeAgentOptions(compaction={"threshold_tokens": 80000, "model": "claude-haiku-4-5"})` — the cheaper model summarizes; the main model continues from the summary
3. Before/after: run a 50-turn research task; without compaction it hits the window at turn 38; with compaction it completes all 50 turns; show the summary checkpoint in the message log
4. Compaction quality check: print the generated summary and verify key facts from early turns survive; the `model` parameter choice affects summary fidelity

### Score
- Teachability: 5/5 — the "server-side for new models, SDK for older/custom" decision rule is immediately actionable
- Visual: 3/5 — token counter + turn completion chart is measurable but not dramatic
- Pull: 4/5 — every developer with a multi-turn agent wants to prevent context overflow
- Freshness: 4/5 — compaction exists but the SDK pattern is new and underdocumented
- **Total: 16/20**
