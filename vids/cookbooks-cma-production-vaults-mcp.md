## cookbooks-cma-production-vaults-mcp

- **Source path:** claude-cookbooks/managed_agents/CMA_operate_in_production.ipynb
- **Teachable claim:** Managed Agents Vaults solve the multi-tenant credential problem — each user's GitHub token lives in their own Vault, never in your code or on every request, with the audit trail tied to the Vault so you always know which user an agent was acting for.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. The problem: hardcoded token → works for one user, breaks for many; Vault → one container per user, referenced by ID
2. Vault creation: `client.beta.vaults.create` + `credentials.add` — two API calls shown
3. MCP toolset attached to Vault: agent now reaches GitHub server-side through Vault credential — no token in session create
4. Webhook pattern: agent fires tool → app receives event → human approves → app posts result — the production async pattern

### Score
- Teachability: 5/5 — multi-tenant credential management is a real production gap for everyone
- Visual: 4/5 — Vault architecture diagram + webhook flow are both clear
- Pull: 4/5 — anyone productionizing a multi-user agent needs this
- Freshness: 5/5 — Vaults and production webhook patterns are new Managed Agents features
- **Total: 18/20**
