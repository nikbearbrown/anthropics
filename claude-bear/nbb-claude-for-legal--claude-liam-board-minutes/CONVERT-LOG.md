# CONVERT-LOG — nbb-claude-for-legal--claude-liam-board-minutes

Conversion: hai-simple (Plain register) → nbb (Teardown register, Liam / Kokoro am_onyx).

## What changed

- **Every body-beat narration rewritten in Teardown register** (B00, B01, B02, B03, BCRY). Same facts, same visuals, same beat_ids, same act tags, same durations, same shot/graphic blocks, same on-screen `text` and card labels. Voice only:
  - B00 — reframed as "Here's what's actually happening…", kept ~30-word budget for the BrutalistHesitantWriter 9s window; hand-off to Liam preserved.
  - B01 — added the design-critic beat: "optimized for legal defensibility at the expense of fidelity." The trade-off was implicit in the original; the Teardown register names it.
  - B02 — opened with "Here's how a minutes handoff actually works — three parts, not two"; added the design-intent line "That last piece is the whole design." Anchor stamp text unchanged.
  - B03 — "Two ways people misread this step" replaces the softer "But…". Made the approval-catches-errors line explicit: "the approval step doing exactly the job it exists for."
  - BCRY — kept the carry-out sentence intact (already sharp); split into two shorter clauses so the WantQuote line reads cleanly. Updated the `quote` prop to match.

- **BHTF converted from "your turn handoff" to LLM EXERCISE beat**, matching the pattern used by nbb-books--claude-liam-building-plugins:
  - `act` → "LLM EXERCISE"
  - `narration_text` reads the paste-ready prompt aloud and closes with a "Go deeper:" follow-up
  - Added `llm_exercise: { prompt, dig_deeper }` block
  - `ClaudeComposerAsk.props.command` mirrors the `llm_exercise.prompt` verbatim
  - `topic` unchanged; `segment` shortened to "Board Minutes"
  - Reframed the prompt to be model-agnostic (Claude / ChatGPT / Gemini) rather than Claude-specific, and to produce a useful artifact on its own (the drafted minutes) without needing the video
  - `dig_deeper` follow-up asks the design-philosophy question the video doesn't answer: what the approval step is actually protecting against, and who gets exposed if you skip it

- **BOUT unchanged** — scaffold's OutroCTA + "When Are Board Minutes Actually Official? Liam, in for Bear." + @HumanitariansAI handle. Same line was already Bear-branded and IN-FOR-BEAR compliant.

- **`_variant_todo` removed** from metadata.

## Judgement calls

- **No AUTHOR.MD found** in `anthropics/claude-bear/` (checked the book dir and grep). Kept the scaffold's OutroCTA + existing outro line — matches what other nbb reels in this book use (e.g. `OutroCTA` with the title + "Liam, in for Bear."). Not falling back to a fabricated NikBearBrown/www.brutalist.art tag when the existing line is already correct and consistent with sibling nbb reels.
- **BHTF as the LLM exercise beat, not a separately inserted B_LLM.** Pattern precedent: `nbb-books--claude-liam-building-plugins/beat_sheet.nbb.json` uses this exact shape — BHTF's `act` is renamed to "LLM EXERCISE", `llm_exercise` object added, narration reads the prompt + Go deeper. Total beat count stays 7, matching the source's `filled: 7, of: 7`. Inserting a separate B_LLM would leave BHTF orphaned as a duplicate "your turn" beat.
- **Preserved all `estimated_duration_s`, `actual_duration_s` where present** — audio isn't being regenerated in this pass, so old timings stay accurate for the beats whose narration length is roughly unchanged. BHTF's `estimated_duration_s` bumped to 42s (matching the building-plugins nbb) because the LLM-exercise narration is roughly 2× the old handoff text. The rendering pass will regen its audio and correct actual_duration_s.
- **`palette` set to `teardown`** by the scaffold, kept. `style_preset` and `ground` kept at `humanitarians` / `#F3EBDD` — these are the render preset the existing media/*.mp4 files were rendered with, and this pass is not re-rendering. If the compile step later re-skins to the pure teardown palette (white/ink/red), swap `ground` to `#FFFFFF` and `accent` to `#C8102E` at that time.

## Not touched

- No rendering, no audio regen, no compile.
- Source `beat_sheet.json` and all media files unchanged.
