## cookbooks-speculative-prompt-caching

- **Source path:** claude-cookbooks/misc/speculative_prompt_caching.ipynb
- **Teachable claim:** Speculative prompt caching warms the cache while the user is still typing — by the time they submit, the cache is hot and TTFT drops to nearly zero; the trick is triggering the background cache warm on the first keystroke, not the submit.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Timeline comparison: reactive (user submits → wait for cache + response) vs. speculative (cache warms during typing → instant response)
2. Background warm trigger: the first keystroke fires a silent cache-write request — shown in code
3. TTFT measurement: with and without speculative caching on a large context — timing output
4. Cost: cache write happens whether or not user submits — the tradeoff and when to accept it

### Score
- Teachability: 4/5 — the proactive vs. reactive framing is the key insight
- Visual: 4/5 — timeline diagram makes the approach immediately legible
- Pull: 4/5 — any chat app over a large system prompt benefits from this
- Freshness: 5/5 — speculative caching is a novel pattern not yet widely documented
- **Total: 17/20**
