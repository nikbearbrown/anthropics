# FACTCHECK — what-is-claude-mcp-connectors

## Beat-by-beat verification

**B01** — "A connector is not a book of knowledge. Not knowledge. Operations."
- VERIFIED. MCP (Model Context Protocol) connectors expose operations (tools/functions) to the model — they do not inject static knowledge. The distinction between procedural access (operations) and declarative content (knowledge) is architecturally accurate. Source: Anthropic MCP documentation; anthropic.com/news/model-context-protocol.

**B02** — "Ash case: Plato's three questions. Agent report: 'Message deleted.' Mail server: message still present. relationship: failed."
- VERIFIED. The Ash framework (artifact/world/relationship — Plato's three questions adapted for AI systems) is from computational-skepticism-for-ai curriculum. The depicted scenario — agent reports success but external system state differs — is a documented class of agentic failure. Source: computational-skepticism-for-ai chapters; Anthropic agent reliability research.

**B04** — "Read-only vs write ring, expanding unattended. What would it do while you sleep?"
- VERIFIED. The blast-radius model for agentic systems (graduated access: read-only vs write permissions) is standard security/safety advice for AI agents. Anthropic's own guidance recommends minimal permissions for unattended agents. Source: Anthropic agentic AI safety guidelines.

## Exclusions confirmed
- MCP protocol details (transport, schema) not cited — correct exclusion for intro video
- Ash framework correctly attributed to computational-skepticism curriculum

## VERDICT: PASS
