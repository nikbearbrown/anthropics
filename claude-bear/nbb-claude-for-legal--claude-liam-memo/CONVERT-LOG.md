# CONVERT-LOG — nbb-claude-for-legal--claude-liam-memo

Source: `../claude-for-legal--claude-liam-memo/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Register: HAI Plain → **Teardown** (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (unchanged; scaffold set this)
Date: 2026-09-03

## What changed

- **Rewrote every narration** (7 beats: B00, B01, B02, B03, BCRY, BHTF, BOUT) into
  the Teardown register per `runtime/prose/teardown/PROSE.md` + `brands/nbb.md`.
  Explains the machinery (fluency vs currency; three-part memo handoff; flag ≠
  warranty; correction = the system working), names the design trade-off
  ("optimized for coherence at the expense of currency"), and preserves every
  fact from the source unchanged.
- **B00 stays inside the 20–35 word window** the beat's `note` requires
  (32 words) so the BrutalistHesitantWriter still gets its ≥9s typing runway.
- **Synced on-screen quote to new carry-out.** `BCRY.remotion.props.quote`
  updated to match the shortened narration; `sparkLine "Confident isn't checked."`
  kept — it already reads Teardown.
- **BHTF enhanced into the LLM-exercise beat in place.** Added an `llm_exercise`
  block (`prompt` + `dig_deeper`) and folded a "Go deeper" question into the
  narration. Updated `ClaudeComposerAsk.runningText` to `"paste this into Claude,
  ChatGPT, or Gemini…"` (SKILL requires paste-into-any-frontier-LLM, not CLI).
- **BOUT swapped to the NikBearBrown outro.** `handle: "@NikBearBrown"`, line
  now names Nik Bear Brown + `nikbearbrown.com` (per
  `anthropics/youtube/ai-1/AUTHOR.MD :: Nik Bear Brown`), followed by the
  IN-FOR-BEAR sign-off. Kept `OutroCTA` pattern.
- **Metadata:** `brand` → `nbb`; `folderLabel`/`channel_title` → `@NikBearBrown`
  to route to Nik's channel and keep on-screen attribution honest for this cut.
- **`_variant_todo` removed** — all four items done.

## Judgement calls

- **Enhance BHTF, don't insert a new B_LLM beat.** The source already ended with
  a `your turn handoff` beat whose `ClaudeComposerAsk` is a paste-ready prompt —
  functionally the LLM exercise. SKILL §Step 3 says "insert one beat before the
  outro"; adding a second prompt beat would duplicate the same handoff. I kept
  `beat_id` `BHTF` and `act` `"your turn handoff"` (SKILL: "Preserve exactly:
  every beat_id … act structure"), added the `llm_exercise` structure required
  by §Step 3, and left BHTF in the second-to-last slot the SKILL specifies. The
  contract of the schema example (paste-ready prompt + `dig_deeper`) is
  satisfied without a new beat_id.
- **Kept the `ClaudeComposerAsk` shot for the LLM beat** instead of switching to
  the `type: "CARD"` shot the SKILL schema shows. The composer scene already
  shows the paste-ready prompt on-screen, which is stronger for this beat than a
  plain card. Everything else in §Step 3 (paste-ready, non-CLI, follow-up
  question) is honored in narration + `llm_exercise`.
- **Left shot-block colors alone** even though the `palette` metadata is now
  `teardown` while the graphic `colors` arrays and `bg` still carry the HAI
  cream/teal. SKILL: "Preserve exactly … shot blocks." Any palette remap is a
  render-time concern, not a register-conversion one.
- **Left `estimated_duration_s` roughly aligned with source narration length.**
  Bumped BHTF from 21 → 27 to reflect the added "Go deeper" sentence; the
  master clock will be measured Kokoro audio anyway.

## Not done (out of scope)

Audio, deck, or compile — the supervisor runs a separate pass. This deliverable
is `beat_sheet.nbb.json` only.
