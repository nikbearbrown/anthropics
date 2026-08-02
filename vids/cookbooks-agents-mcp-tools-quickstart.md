## cookbooks-agents-mcp-tools-quickstart

- **Source path:** claude-quickstarts/agents/README.md
- **Teachable claim:** The entire Claude API agent loop — tool registration, conversation management, MCP server connection — fits in under 300 lines of Python; the `agent.py` backbone runs with custom Python tools, MCP stdio servers, or both, and deliberately omits production features so the mechanics are fully visible.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. `agent.py` anatomy: the tool registry, the message history manager, the API call loop — 300 lines annotated in under 2 minutes; "this is everything a framework hides from you"
2. Python tool via `@tool` decorator: `ThinkTool` as the reference — name, description, and sync function; the agent decides when to call it; show the tool call and result in the log
3. MCP stdio server: `calculator_mcp.py` spawned as a subprocess; `ClientSession.initialize()` → tool discovery; the agent calls `add` and `multiply` exactly as if they were Python tools
4. Combine both: run the `agent_demo.ipynb` with calculator MCP + web search MCP + ThinkTool; show the agent composing across tool types on one task

### Score
- Teachability: 5/5 — "under 300 lines, no framework, fully visible mechanics" is the sharpest possible framing for a reference implementation
- Visual: 3/5 — Python terminal output; the MCP tool call is the most interesting moment
- Pull: 5/5 — every developer who "wants to understand agents without a framework" lands here
- Freshness: 3/5 — reference agents exist but the 300-line + MCP composition is new and clean
- **Total: 16/20**
