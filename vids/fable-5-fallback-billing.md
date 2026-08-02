## fable-5-fallback-billing

- **Source path:** claude-cookbooks/fable_5_fallback_billing/guide.ipynb
- **Teachable claim:** When Claude Fable 5's safety classifiers block a request, a single `fallbacks` field triggers automatic server-side retry on Opus 4.8 — and client-side middleware handles the same pattern for providers that don't support server-side fallbacks.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The refusal shape: API returns 200 with `stop_reason: "refusal"` + `stop_details.category` — show the JSON block live; explain why branching on `stop_reason` beats checking `content`
2. Server-side fallback: one extra field `fallbacks:[{"model":"claude-opus-4-8"}]` + beta header → the API retries and annotates the fallback content block; the client code is unchanged
3. Client-side middleware: `BetaRefusalFallbackMiddleware` registered once; on a refusal it splices the fallback's events onto the open stream — streaming demo shows the `fallback` content block marking the model boundary
4. `BetaFallbackState` pinning: follow-up messages stay on the model that accepted — show `with state:` on back-to-back calls so the conversation doesn't ping-pong

### Score
- Teachability: 5/5 — the "refusal is 200, not 4xx; branch on stop_reason" rule is the key aha
- Visual: 4/5 — JSON diff before/after + live streaming splice is clean before/after cinema
- Pull: 5/5 — anyone shipping Fable 5 in production hits this on day one
- Freshness: 5/5 — Fable 5 + server-side fallback beta is brand-new API surface
- **Total: 19/20**
