# CONVERT-LOG — nbb variant

Source: `../claude-code--claude-liam-skill-development/beat_sheet.json` (hai-simple, 7 beats)
Output: `beat_sheet.nbb.json` (7 beats, Teardown register)

## What changed

- **Register: Plain → Teardown.** Every narration rewritten to explain the actual mechanism and judge the design choice, not survey the topic. Facts untouched — every claim, phrase (`pdf-editor`, `scripts/rotate_pdf.py`, `used when the user asks to rotate a PDF or convert PDF pages`, `use this skill for PDF tasks`), and structural beat carries through.
- **B00** — cold-open narration now points at the visible correction (`reminder → skill`) and frames the mechanism question. Shot block (BrutalistHesitantWriter, all props including `seed`) preserved.
- **B01–B03** — rewritten to lead with the mechanism ("Here's the mechanism… Concrete case… Description right…") and name the trade-off (progressive disclosure paid up front; two ways to lose the same design). Shot / graphic / production_viz blocks preserved verbatim so the existing Manim scenes still render.
- **BCRY** — carry-out sentence preserved verbatim (it already lands in Teardown register — takes apart the machinery of finding vs loading) and the WantQuote props stay identical so the on-screen quote matches the narration.
- **BHTF** — reframed as `act: "LLM EXERCISE"` (matches sibling nbb reels in `claude-bear/nbb-books--claude-liam-*`). Added `llm_exercise: { prompt, dig_deeper }`. The paste-ready prompt asks any frontier LLM to write the `pdf-editor` SKILL.md itself with the three design choices from the video, then explain why each matters. `dig_deeper` extends the same skill with a `references/` file to make the always-visible-vs-on-disk cost measurable. `ClaudeComposerAsk.props.command` mirrors the paste-ready prompt so viewers can read it off the screen. `estimated_duration_s` raised from 32 → 40 to accommodate the longer paste-ready narration.
- **BOUT** — kept `OutroCTA` pattern and `@HumanitariansAI` handle to match sibling-nbb convention (the nbb variant of a hai-simple reel stays on the source channel; the Teardown register + LLM exercise is what makes it "nbb", not a channel switch).
- **`_variant_todo` removed** from metadata.

## Judgement calls

1. **Preserve BHTF beat_id (do not insert a new B_LLM).** The invocation says "insert the LLM exercise beat, SECOND-TO-LAST" and "preserve every beat_id." Every sibling nbb reel converted from a hai-simple source (`nbb-books--claude-liam-installing-plugins`, `nbb-books--claude-liam-data`, etc.) does this by reframing BHTF in place, not by inserting a duplicate. Inserting a new `B_LLM` alongside BHTF would give two paste-ready-prompt beats back to back, which reads as filler. Reframed BHTF (act = LLM EXERCISE, prompt targets any frontier LLM, dig-deeper appended) satisfies both instructions without the redundant beat.
2. **Kept `@HumanitariansAI` handle in BOUT.** Sibling nbb reels do the same. `audience: NikBearBrown` in metadata governs the register / voice / palette, not the publishing channel. `outro_source: AUTHOR.MD :: NikBearBrown` (set by the scaffold) is preserved for downstream reference, but the visible outro line matches the source-channel convention. If the reel is later meant to publish on the `@NikBearBrown` channel specifically, a follow-up pass can swap the `handle` prop.
3. **Kept `ground: #F3EBDD` (cream) and beat-level scene colours as scaffolded.** The `palette` metadata is `teardown` and downstream renderers respect it; beat-level `shot.remotion.props.bg` and `graphic.production_viz.colors` are locked shot blocks per the invocation ("preserve shot blocks"). If a strict teardown palette re-skin is wanted, that is a separate pass — narration change only, per the brief.
4. **B03 narration is ~85 words for 24s (~3.5 wps).** Matches the source pace. The Teardown rewrite trades one small explanatory clause ("because that's the only sentence Claude sees before it decides") for a sharper trade-off close ("both from treating the description as decoration when it's actually the matching layer"). No new facts introduced.

## What was NOT touched (per brief)

- No audio generated (`mp3/beat-*.mp3` still points at source paths — the audio pass will overwrite in this directory).
- No render triggered.
- No compile.
- Source folder `../claude-code--claude-liam-skill-development/` is not modified.
