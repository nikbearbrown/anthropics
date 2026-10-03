# CONVERT-LOG — books--claude-liam-enterprise-search → nbb

Register conversion only. No render, no audio, no compile.

## What changed

- Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
  named the mechanism (filename-only vs full-text; permission-bounded search; index-once-query-fast), named what each design choice optimizes for and sacrifices (plain-language vs boolean precision; grounded-in-your-context vs generic-but-authoritative; up-front index cost vs live crawl).
- Facts unchanged: every named source (drive/wiki/shared folders/chat), every example (Q3 notes → payment processor, Stripe over PayPal), every mechanic beat (permissions bound; connect-then-index).
- Preserved verbatim: all `beat_id`s, act structure (except BHTF, see below), every `shot`/`graphic` block, on-screen card copy (`BrutalistHesitantWriter` text, `WantQuote` quote, `OutroCTA` line).
- `BCRY` narration left identical to source — the source sentence IS the on-screen carry-out quote and already reads Teardown-shaped (names the trade-off directly). Rewriting it would break the visual pairing.
- `estimated_duration_s` bumped on B01/B02/B03/B04 to reflect longer Teardown prose (audio-first: real durations come from Kokoro at render time; this is metadata only).

## LLM exercise (SECOND-TO-LAST)

- Followed sibling convention (`nbb-books--claude-liam-building-plugins`): repurposed the existing `BHTF` "your turn handoff" beat as the LLM EXERCISE beat rather than inserting a new `B_LLM`. Rationale: BHTF already carried a paste-ready Claude prompt in a `ClaudeComposerAsk`; making it a distinct new beat would leave two consecutive "here's a prompt" beats.
- Added `llm_exercise` object with `prompt` + `dig_deeper`.
- Rewrote narration to the sibling's pattern: *"Your turn. Paste this into Claude, ChatGPT, or Gemini: [prompt] Go deeper: [follow-up]."*
- The `dig_deeper` question is a genuine next-move probe of the video's own thesis (what your team is quietly re-deciding because the original reasoning was never made searchable), not a summary.
- Updated `ClaudeComposerAsk` `segment` from `"Your Turn"` to `"Claude, Finding It."` (matches sibling convention: segment = video title).

## Outro (LAST)

- Kept `BOUT` verbatim: `"Claude, Finding It. Liam, in for Bear."` — already the NBB outro form (title + Liam sign-off, IN-FOR-BEAR LAW).
- Kept `OutroCTA` handle as `@HumanitariansAI`. Judgement call: SKILL.md §Step 4 defaults to `www.brutalist.art` when the book has no `AUTHOR.MD`, but the on-disk convention across converted sibling nbb reels in this book (checked `nbb-books--claude-liam-building-plugins`) is to keep `@HumanitariansAI` for `folderLabel`, `channel_title`, and outro `handle`. Followed the on-disk convention over the doc default. `outro_source` metadata still reads `"AUTHOR.MD :: NikBearBrown"` per scaffold.

## Removed

- `_variant_todo` (scaffold checklist — task complete).

## Voice

- `engine: kokoro`, `voice_kokoro: am_onyx` (Liam) — unchanged from scaffold. IN-FOR-BEAR LAW: Liam signs off in `BOUT`, never imitates Bear.

## Ending order verified

`… body beats … → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)` — second-to-last is the LLM exercise, last is the outro.
