## cookbooks-session-memory-compaction

- **Source path:** claude-cookbooks/misc/session_memory_compaction.ipynb
- **Teachable claim:** "Speculative compaction" eliminates the jarring pause when a long conversation hits the context limit — you warm the memory summary in a background thread while the user types their next message, so compaction is instant when it fires.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Timeline diagram: reactive compaction (wait → pause → resume) vs. speculative compaction (background → instant)
2. Threading code: background thread updating memory summary while main thread handles user input
3. Prompt caching applied to background memory updates: 80% cost reduction on repeated compaction calls
4. Cost comparison: per-compaction cost with and without caching

### Score
- Teachability: 4/5 — the speculative/proactive distinction is the aha moment
- Visual: 4/5 — timeline comparison is clear and the background threading pattern is visual
- Pull: 4/5 — anyone building a chatbot or long-running assistant needs this
- Freshness: 4/5 — speculative caching is a novel pattern not yet widely known
- **Total: 16/20**
