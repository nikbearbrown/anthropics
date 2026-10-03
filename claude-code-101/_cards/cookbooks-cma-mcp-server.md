## cookbooks-cma-mcp-server

- **Source path:** claude-cookbooks/managed_agents/cma-mcp/README.md
- **Teachable claim:** Nine tools wrapping the Managed Agents Sessions API — one `wait_for_idle` shim converts SSE streaming to request/response — let Claude Desktop or claude.ai web start and converse with your org's hosted agents as if they were MCP tools, with zero changes to the agents themselves.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The architecture: User → Claude Desktop → MCP: `send_message` + `wait_for_idle` → CMA session; show the shared `tools.ts` serving both stdio and HTTP transports
2. `wait_for_idle` as the design key: it opens the SSE stream, consumes events until `session.status_idle`, and returns the reply text — show the before (raw SSE) and after (request/response the MCP caller can use)
3. stdio path: add to Claude Desktop `claude_desktop_config.json`; ask Claude Desktop "what agents does my org have?" → `list_agents` fires → agent names appear
4. HTTP path for claude.ai: `bun run http` → deploy URL → add as a custom Connector; from claude.ai web, `create_session` + `send_message` to any org agent

### Score
- Teachability: 5/5 — "wrap any CMA agent as an MCP tool with one SSE→response shim" is immediately applicable
- Visual: 3/5 — the tool listing and reply flow are demonstrable but not dramatic
- Pull: 4/5 — anyone using Claude Desktop who also has Managed Agents wants this bridge
- Freshness: 5/5 — CMA-as-MCP is a novel composition not documented elsewhere
- **Total: 17/20**
