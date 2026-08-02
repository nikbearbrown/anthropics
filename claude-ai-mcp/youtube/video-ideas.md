# Claude.ai MCP Integration Video Ideas

## Candidate 1 — Why removing a fallback discovery path forces servers to implement a new standard instead of falling back to defaults

- Source: `drafts/announcement-auth-server-metadata-fallback-deprecation.md`
- Topic: OAuth metadata discovery chains in API integration
- Hook: A non-standard discovery fallback that servers depend on is being removed, forcing them to implement a standard instead.
- Key case: An MCP server at `https://mcp.example.com/v1/mcp` stops working after the path-aware fallback `/.well-known/oauth-authorization-server/v1/mcp` is removed; root-based discovery `/.well-known/oauth-authorization-server` fails, and default endpoints `(/authorize, /token, /register)` alone aren't enough.
- The Question: If three fallback levels remain (root-based discovery, defaults, PRM), why does removing one path-aware level require a completely new metadata implementation rather than just using the remaining fallbacks?
- Core idea: Fallback chains create implicit contracts; servers optimize to the least-reliable fallback, making removal of any level a breaking change that forces re-architecture rather than graceful degradation.
- Visual object: A branching discovery decision tree that collapses at one node, with a parallel flow showing what PRM adds.
- Manim move: collapse
- Example seed: A server at `auth.internal/oauth/tenant42` tried discovery at `/oauth/tenant42/.well-known/oauth-authorization-server` (removed path-aware); now must either return that endpoint via PRM or migrate to `auth.internal/.well-known/oauth-authorization-server` (root-based).
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: OAuth basics, HTTP discovery conventions
- Exclusions: OpenID Connect details, full MCP specification, OAuth 2.1 compliance
- Score: 8/10

## Candidate 2 — Why switching network transport protocols improves session lifetime for the same application

- Source: `drafts/announcement-sse-deprecation.md`
- Topic: Transport protocol characteristics and session durability in streaming APIs
- Hook: Replacing one streaming transport (SSE) with another (Streamable HTTP) reduces re-initialization even though the application logic is unchanged.
- Key case: An MCP server using SSE experiences "reduced session persistence" and "more frequent re-initialization" when Streamable HTTP becomes the preferred transport; the same server logic survives longer on the new transport.
- The Question: What property of Streamable HTTP versus SSE lets sessions persist longer, given that both are streaming transports and neither is under application control?
- Core idea: SSE uses single-direction long-polling with framework limitations on connection pooling and keepalive; Streamable HTTP allows bidirectional streaming and connection reuse, letting the platform maintain state across reconnects that would drop in SSE.
- Visual object: Dual timelines showing SSE connection lifecycle (periodic drops, re-initialize, state loss) versus Streamable HTTP (unbroken persistence, state retained).
- Manim move: compare
- Example seed: SSE server at example.com/mcp drops every 45 seconds requiring session reinit, losing cursor position; same logic on Streamable HTTP maintains state for hours, resuming from cursor.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: HTTP basics, streaming concepts, connection reuse
- Exclusions: HTTP/2 protocol details, detailed keepalive mechanics, full SSE specification
- Score: 7/10
