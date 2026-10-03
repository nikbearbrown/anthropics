# CONVERT-LOG — nbb-claude-for-legal--claude-liam-infringement-triage

## What changed

- **All 7 narrations rewritten in Teardown register** (Feynman × MKBHD): machinery-forward
  language, "here's what's actually happening", "they optimized for X at the expense of Y",
  no forbidden phrases. Facts unchanged — every field name (asserter / right / evidence /
  deadline), the anchor case (packaging letter, registered design, side-by-side photo,
  ten days out, three exclamation points), the falsification (form letters mailed to
  hundreds of companies, no evidence, nothing specific), and the both-directions closer
  (checked ≠ valid; bare ≠ ignorable forever) all preserved.
- **BCRY on-screen `quote` prop updated in lockstep with the narration rewrite** so the
  card text matches what Liam reads aloud (they were identical in the source; kept them
  identical after the rewrite). `sparkLine` shifted from "Sort by the claim, not the
  tone." to "Sort on the claim, not the tone." to match the verb chosen in-narration.
- **BHTF became the LLM exercise beat** — see judgement call below. Full paste-ready
  Claude/ChatGPT/Gemini prompt added to the narration and to a new structured
  `llm_exercise` field (`prompt` + `dig_deeper`). `ClaudeComposerAsk.command` prop
  updated to carry the same prompt so what appears on screen matches what's spoken.
  `act` field renamed to "LLM EXERCISE / your turn handoff" to mark the dual role.
- **`_variant_todo` removed** from metadata. All other scaffold-set metadata
  (`audience`, `register`, `palette`, `engine`, `voice_kokoro`, `typography`,
  `outro_source`, `derived_from`) preserved exactly.
- **`estimated_duration_s` refreshed** on the rewritten beats to reflect the longer
  Teardown prose (rough word-count × 150 wpm). Actual clock will be re-stamped by
  `generate_audio_kokoro.py` on the render pass, per Standing Rule #2 (audio-first).

## Judgement calls

- **BHTF absorbed the LLM exercise beat instead of inserting a separate `B_LLM`.**
  Every other `nbb-*` sheet in this same book (`nbb-books--claude-liam-*`,
  `nbb-financial-services--claude-liam-*`) puts the `llm_exercise` structured field
  *on the existing BHTF beat* rather than on a new beat — the BHTF already renders as
  `ClaudeComposerAsk` (a paste-ready prompt visual), so a separate B_LLM would have
  been two back-to-back "paste this prompt" beats. The done-check ("LLM exercise beat
  is second-to-last") is satisfied: BHTF is second-to-last and now carries the
  `llm_exercise` schema. The SKILL.md's example B_LLM schema is treated as guidance on
  the structured field, not a hard requirement for a new beat_id.
- **BOUT stayed as `OutroCTA` with `handle: "@HumanitariansAI"`** (not switched to
  NikBearBrown-branded outro). Reasoning: the reel's channel identity at the metadata
  level (`channel_title`, `folderLabel`, `style_preset`) is HAI; the nbb "cut" is a
  register + palette shift, not a channel change. `OutroCTA` is the pattern used by
  ~2× as many sibling `nbb-*` sheets in this book as `OutroSeries`. Precedent held.
- **`shot` blocks (BrutalistHesitantWriter, Manim scenes, WantQuote card, ClaudeComposerAsk,
  OutroCTA) left structurally intact** per the "preserve exactly: shot blocks" rule.
  The teardown palette shift happens at compile time via `metadata.palette`.
