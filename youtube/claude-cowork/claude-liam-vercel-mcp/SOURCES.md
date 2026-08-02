# SOURCES — claude-liam-vercel-mcp

**Primary:** research doc "Claude + Vercel MCP Best Practices" (pasted
2026-07-22) — itself a synthesis flagged, by its own author, as mixing
verified mechanism with datable/unverified specifics.

## Re-verified before scripting (DOUBLE-CHECK LAW)

- Hosted Vercel MCP at mcp.vercel.com grants account-level access; two tool
  tiers (public docs vs authenticated account tools).
  - https://vercel.com/docs/agent-resources/vercel-mcp
  - https://vercel.com/blog/introducing-vercel-mcp-connect-vercel-to-your-ai-tools
- Streamable HTTP superseded SSE as the MCP remote transport (SSE deprecated);
  stateless-leaning direction is real.
  - https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http/
  - https://brightdata.com/blog/ai/sse-vs-streamable-http

## Deliberately STRIPPED (rule 4 — datable / will age the episode)

- "July 21, 2026" purchases changelog date → narration says "it grew to
  spending money," mechanism kept, date gone.
- "2026-07-28 spec ships in six days" / exact spec version → "the protocol is
  shifting toward stateless," no date, no version.
- CVE-2026-25536 / GHSA number / exact SDK+mcp-handler version pins → the
  cross-client-leak lesson is out of the reel entirely (it's a
  self-hoster's dependency-pin detail, not an explainer beat); the durable
  "verify the spec before you hardcode" advice stays.
- Exact supported-client allowlist, function timeout seconds, payload caps,
  cold-start p95 numbers → all cut; none are load-bearing for the thesis.

## NOT USED (source flagged as unverified — rule 5)

- The "permission-mode downgrade bug" with internal config-key and
  GrowthBook flag names: the source doc itself says it couldn't verify this
  and it reads fabricated. Excluded entirely, per the doc's own caution.
