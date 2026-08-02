## cookbooks-linear-cma-bridge

- **Source path:** claude-cookbooks/managed_agents/linear/README.md
- **Teachable claim:** @mentioning a Claude Managed Agent in a Linear issue triggers a stateless webhook bridge that creates a CMA session, stores routing state in session metadata, and posts the agent's reply as a Linear comment when the session idles — zero database needed.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The flow: Linear `AgentSessionEvent` → `/linear-webhook` → `sessions.create` (metadata: `linear_session_id`, `linear_org_id`) → 200; Claude runs on Anthropic infra → `session.status_idled` CMA webhook → `sessions.retrieve` → `createAgentActivity`
2. `actor=app` OAuth: Linear requires the agent identity to be an app, not a user — show the OAuth setup that makes replies appear under the bot's identity
3. Webhook routing: the `cma-webhook` handler calls `sessions.retrieve`, reads the metadata, calls `createAgentActivity` — no session store, no DB, the metadata IS the routing
4. Extension options live on screen: GitHub repo resource, MCP tools, Outcomes, memory store — each as a one-field addition on `sessions.create`

### Score
- Teachability: 5/5 — "session metadata is the routing state" solves the DB question every webhook bridge builder asks
- Visual: 3/5 — the flow is logical but not intrinsically visual; the Linear comment reply is the payoff
- Pull: 4/5 — Linear users are power users who will build on this pattern
- Freshness: 5/5 — CMA + Linear webhook bridge is new and not documented elsewhere
- **Total: 17/20**
