# FACTCHECK — claude-liam-vercel-mcp

| Claim in narration | Verdict | Note |
|---|---|---|
| Two distinct things share the name "Vercel MCP" | HOLDS | hosted connector vs self-deployed server — both in Vercel docs |
| Hosted grant = same reach as your account, no read-only mode | HOLDS | Vercel docs; framed as mechanism, not dated |
| Write surface now includes purchases/domains | HOLDS (mechanism) | date stripped; the ESCALATION is the point, not when |
| Quote-then-confirm, agent walks it itself | HOLDS | echo-price mechanism real; "no human required" is the honest read |
| Prompt injection is the dominant threat | HOLDS | matches MCP security guidance + the source's own framing |
| Split identities / deny rules / PreToolUse hook / sandbox | HOLDS | general unattended-agent hygiene, not Vercel-specific |
| Protocol shifting stateless | HOLDS (direction) | version + ship date stripped; "verify before hardcoding" kept |
| permission-downgrade bug w/ flag names | EXCLUDED | source self-flagged unverified; not in the reel |

No numbers appear in narration except "two things / one question." Every
capability claim is stated as a durable mechanism, not a dated changelog.
