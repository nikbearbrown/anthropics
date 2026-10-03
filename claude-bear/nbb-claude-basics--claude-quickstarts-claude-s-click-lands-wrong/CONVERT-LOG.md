# CONVERT-LOG — nbb-claude-basics--claude-quickstarts-claude-s-click-lands-wrong

Source: `../claude-basics--claude-quickstarts-claude-s-click-lands-wrong/beat_sheet.json`
Register: Plain → **Teardown** (Feynman × MKBHD)
Voice: Liam (Kokoro `am_onyx`), in for Bear
Channel: `@HumanitariansAI` → `@NikBearBrown`

## Changes

- **Metadata**
  - `folderLabel` and `channel_title` retargeted to `@NikBearBrown`
  - `purpose` rewritten to name the mechanism (API pre-resize) and the fix (inverse ratio applied before the OS driver)
  - `_variant_todo` removed
- **All 8 narration_texts rewritten in the Teardown register.** Every number, coordinate, resolution, formula, and mechanism from the source survives unchanged; the voice now takes the pipeline apart (API pre-resize as a design choice — cheaper tokens at the cost of a coordinate-space mismatch), names what was optimized for and what it cost, and evaluates the fix on its own terms (an inverse, not a heuristic).
- **BHTF repurposed as the LLM EXERCISE beat** (second-to-last, per SKILL.md §Step 3). Added an `llm_exercise` block with a paste-ready prompt for Claude / ChatGPT / Gemini derived from the whole video's subject, plus a genuinely explorable dig-deeper about aspect-ratio letterboxing. `act` renamed from `your turn handoff` → `LLM EXERCISE`. Kept the `ClaudeComposerAsk` scene contract intact; retargeted `segment` to "LLM Exercise" and `folderLabel` to `@NikBearBrown`.
- **BOUT (outro) preserved as the last beat**, retargeted to `@NikBearBrown`. Tagline unchanged — it already reads as the NikBearBrown carry-out.

## Judgement calls

- **Kept B00's `text` prop, colors, and BrutalistHesitantWriter mechanic verbatim.** The scaffold set `palette: teardown` in metadata, but sibling nbb reels (e.g. `nbb-books--claude-liam-data`) leave the humanitarians ground `#F3EBDD` / accent `#E4572E` untouched in scene props — visual retint is outside a register-conversion pass. Narration is what got the Teardown pass; shot blocks and card copy were preserved exactly as SKILL.md requires.
- **Kept the "Liam, in for Bear" sign-off in BOUT** per IN-FOR-BEAR LAW — Liam identifies as filling in for Bear, never as Bear.
- **LLM exercise prompt goes past the original "your turn" question**: it asks for the two-line formula, an explanation of *why* it's the inverse, and the Retina/DPR follow-up — a paste-ready block that produces a useful answer on its own, without the video. Dig-deeper reaches into the case the video doesn't cover (letterboxed aspect-ratio mismatch), a real next question rather than a summary.
- **Purpose statement updated** to reflect the Teardown lens (mechanism + design cost + fix), not just the Plain carry-out.

## Not touched

- Every `beat_id`, `act` (except BHTF), `shot.type`, `graphic` block, Remotion `pattern`, and card copy inside `props.text` / `mechanic` / `production_viz` — preserved verbatim.
- `estimated_duration_s`, `lead_silence_s`, `tail_silence_s`, `voice`, `engine`, `audio_file`, `build`, `note` — preserved verbatim.
- All facts: 1456×819, 1920×1080, (700,410), (960,540), 2560×1440, device pixel ratio 2 — verified survive intact in narration and in the LLM prompt.
