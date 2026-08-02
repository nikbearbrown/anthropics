## cookbooks-roadtrip-planner-multiagent

- **Source path:** claude-cookbooks/managed_agents/roadtrip_planner/README.md
- **Teachable claim:** One Next.js app demonstrates four Claude Managed Agents features at once: live SSE streaming with token-by-token previews, vault credentials that inject API keys at egress (the model never sees the secret), per-session model overrides without creating a new agent version, and a multiagent coordinator that hands its draft to an Opus reviewer running as a session thread.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** long (8–12 min)

### Visual beats
1. Streaming beat: ask for a road trip plan; status line flips to "thinking..." on the first `agent.thinking` preview; reply text streams token by token via `event_deltas` — show the blank-then-paragraph failure mode first, then with previews enabled
2. Vault credential injection: `injection_location: {header: true, body: false}` on the NPS credential; flip it to `body: true` live — NPS rejects the misplaced key, the error lands in the tool rail; flip it back in one `ant` CLI command, next call succeeds
3. Model picker override: `agent_with_overrides` on session create with `model: "claude-opus-4-8"` — the header shows the resolved model from the API, not the client's request; the stored agent is unchanged
4. Multiagent review: ask for a multi-day itinerary; status line flips to "waiting on Plan reviewer..."; the right rail shows `session.thread_created` → `agent.thread_message_sent` (draft) → `agent.thread_message_received` (critique); two models in one session, zero extra plumbing

### Score
- Teachability: 5/5 — four production CMA patterns shown live in one working app is a masterclass
- Visual: 5/5 — streaming token diffs, credential flip failure, multi-agent thread rail are all intrinsically visual
- Pull: 5/5 — every CMA builder wants all four of these patterns
- Freshness: 5/5 — vault injection_location + multiagent threads are very new API surface
- **Total: 20/20**
