## cookbooks-prompt-caching

- **Source path:** claude-cookbooks/misc/prompt_caching.ipynb
- **Teachable claim:** Prompt caching cuts API costs by up to 90% and latency by 2x — and you enable it with a single `cache_control` field, but most developers leave it off entirely.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Side-by-side timing bars: no cache vs. cache write vs. cache hit — the speedup is visceral
2. Code diff: adding `cache_control={"type": "ephemeral"}` at top level vs. placing it on individual blocks
3. Multi-turn conversation timeline: cache breakpoint auto-advancing with each new turn
4. Decision table: automatic caching vs. explicit breakpoints — when to use each

### Score
- Teachability: 5/5 — a clear mechanical claim (90% cost reduction) viewers can verify immediately
- Visual: 4/5 — timing comparisons and code diffs are inherently visual
- Pull: 5/5 — every Claude API user overpays without this; instant self-interest
- Freshness: 4/5 — automatic caching is new (previously required manual markers)
- **Total: 18/20**
