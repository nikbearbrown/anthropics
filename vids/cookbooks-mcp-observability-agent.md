## cookbooks-mcp-observability-agent

- **Source path:** claude-cookbooks/claude_agent_sdk/02_The_observability_agent.ipynb
- **Teachable claim:** MCP (Model Context Protocol) lets your agent connect to any external system — Git, databases, SaaS APIs — with no custom tool code; add an MCP server and the agent gains those tools instantly.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Agent with no MCP: only built-in tools available — the filesystem boundary
2. Adding Git MCP server: one config change → agent now has 13 Git-specific tools
3. Live demo: agent reads git log, spots a pattern across commits, opens a PR — all via MCP tools
4. MCP architecture: agent ↔ Anthropic proxy ↔ MCP server ↔ external service — one diagram

### Score
- Teachability: 5/5 — MCP as "plug in any SaaS API" is the key conceptual unlock
- Visual: 4/5 — tool availability before/after MCP connection is visually clear
- Pull: 5/5 — every agent builder wants to reach external services without writing adapters
- Freshness: 5/5 — MCP is the current ecosystem story and this is its clearest demo
- **Total: 19/20**
