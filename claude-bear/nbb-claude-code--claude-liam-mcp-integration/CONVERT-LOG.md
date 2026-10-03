# CONVERT-LOG — claude-code--claude-liam-mcp-integration → nbb

Register conversion pass (nbb SKILL.md, Step 2–4). Source
`beat_sheet.json` untouched; this directory holds the derived NBB cut.

## What changed

- **All seven `narration_text` fields rewritten** in the Teardown register
  (Feynman × MKBHD): machinery first, design choice named, trade-off called out.
  Facts (four transports, `.mcp.json` vs inline `mcpServers`, the exact tool-name
  template, `mcp__plugin_asana_asana__asana_create_task`, silent-mismatch
  behavior, wildcard scope) preserved verbatim.
- **BHTF re-cast as the LLM EXERCISE beat** (second-to-last per Step 3): added a
  `llm_exercise` block with a paste-ready prompt (Claude/ChatGPT/Gemini) and a
  "Go deeper" follow-up on OAuth handshake, credential ownership, and silent
  mid-session token expiry. `ClaudeComposerAsk` props updated to match
  (segment "Exact, Or Silent.", folderLabel `@NikBearBrown`, `output: []`).
- **BOUT kept as the last beat** with the standard `MCP Integration. Liam, in
  for Bear.` sign-off; `handle` swapped to `@NikBearBrown`.
- **Metadata**: `folderLabel` and `channel_title` swapped from `@HumanitariansAI`
  to `@NikBearBrown` (nbb default channel per `brands/nbb.md`); `_variant_todo`
  removed; `purpose` rewritten in the Teardown register while preserving the
  same claims.
- Estimated durations bumped to reflect the longer Teardown narrations (B00 14→18,
  B01 20→30, B02 22→36, B03 22→38, BCRY 10→12, BHTF 28→60). All still
  narration-clocked; audio pass will overwrite `actual_duration_s`.

## Judgment calls

- **Shot blocks, on-screen graphic mechanics, and card copy left untouched** —
  the Teardown rewrite is voice, not visuals; the `production_viz.mechanic`
  strings and the anchor-return language already read as Teardown, and changing
  them would drift from what the Manim scenes actually render.
- **`playlist: "Claude Code"` kept** — SKILL.md doesn't force a rename, and the
  video is a Claude Code episode regardless of channel.
- **`skill: "hai-simple"` and `gate_h: "N/A - hai-simple ..."` kept** — those
  fields describe the source-sheet build lineage, not the nbb cut, and removing
  them would erase provenance the source-sheet field already implies.
- **`ClaudeComposerAsk` used at BHTF (not the legacy `NikBearBrownTerminalAsk`)**
  per the 2026-07 Ask/intro scene rule in SKILL.md; scaffold already had it.
