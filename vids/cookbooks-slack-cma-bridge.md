## cookbooks-slack-cma-bridge

- **Source path:** claude-cookbooks/managed_agents/slack/README.md
- **Teachable claim:** A five-file webhook bridge routes a Slack @mention to a Claude Managed Agent session — the session `metadata` fields `slack_channel` and `slack_thread_ts` are the entire routing state, and the `session.status_idled` webhook is the only hook needed to post the reply back.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The flow: Slack @mention → `/slack/events` → `sessions.create` with metadata → 200; Claude runs to idle on Anthropic infra → `session.status_idled` webhook → `sessions.retrieve` → `chat.postMessage`
2. The routing contract: show the metadata field on `sessions.create` — two fields, `slack_channel` + `slack_thread_ts` — and the retrieve-then-filter on the webhook handler
3. `beta.webhooks.unwrap()` verification: one SDK call validates the Slack signature and returns the event; show the alternative (manual HMAC) to explain why this is the right path
4. End-to-end: type `@bot explain this error in #ops`; the reply appears in the thread; open the Console to show the full session trace behind it

### Score
- Teachability: 5/5 — the "metadata as routing state" pattern is the reusable design insight
- Visual: 4/5 — Slack → Anthropic → Slack flow with live trace is inherently demonstrable
- Pull: 4/5 — Slack is where most teams want their agent
- Freshness: 5/5 — CMA webhooks + metadata routing is new and underexplained
- **Total: 18/20**
