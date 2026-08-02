## cwc-workshop-production-ready-agent

- **Source path:** cwc-workshops/production-ready-agent/
- **Teachable claim:** The Deal Desk multi-agent system shows that a coordinator agent + four parallel sub-agents + memory store + MCP + gated tool calls is a complete production architecture — and every piece maps to a specific Managed Agents API primitive.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Architecture: coordinator → four parallel research sub-agents → memory store → gated Linear MCP call
2. Streaming events in the UI: sub-agent progress appearing inline, each session linking to Console
3. Gate confirmation: coordinator proposes to create a Linear ticket → human confirms in the UI → fires
4. Starter vs. solution diff: the seven API route handlers stubbed vs. filled — the workshop's teaching structure

### Score
- Teachability: 5/5 — maps a real M&A research workflow to every Managed Agents primitive
- Visual: 4/5 — multi-agent progress streams and gated tool calls are both visual
- Pull: 4/5 — enterprise multi-agent architecture is the most valuable build-with-Claude topic
- Freshness: 5/5 — this is the most advanced Managed Agents reference architecture available
- **Total: 18/20**
