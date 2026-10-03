# CONVERT-LOG — claude-for-legal--claude-liam-investigation-memo → nbb

**Source:** `anthropics/claude-bear/claude-for-legal--claude-liam-investigation-memo/beat_sheet.json` (Plain, hai-simple, 11 beats, filled/rendered)
**Target:** `beat_sheet.nbb.json` in this directory
**Sibling precedent followed:** `nbb-claude-for-legal--claude-liam-ip-clause-review/beat_sheet.nbb.json` (same book, same base skill, same brand)

## What changed

- Rewrote all 11 `narration_text` fields in Teardown register (Feynman × MKBHD): named the machinery ("the actual machinery," "the execution model"), the design choice ("a specification, not new judgment"), and the trade-off ("what that buys… / what it costs…"). No facts changed. Every specific — `investigation-memo/`, `SKILL.md`, "top to bottom," "no branching unless a step says branch," "delete the folder," "thorough memo / thin memo," "the same structure, every run" — carries through verbatim.
- BHTF (the "your turn handoff" beat) promoted in-place to the **LLM EXERCISE** slot (second-to-last): renamed `act` to `LLM EXERCISE`, added the `llm_exercise` object (`prompt` + `dig_deeper`), broadened the paste-target from "Claude" to "any frontier LLM — Claude, ChatGPT, or Gemini," and appended a real "Go deeper" — run the SKILL.md, delete one step, re-run, read the delta to see what the template was actually contributing. Follow-up is an explorable next question, not a summary.
- BOUT (outro) retained as the last beat; swapped `OutroCTA` → `OutroSeries` (matches the sibling reel's teardown-palette outro) with `eyebrow: "CLAUDE · SKILLS · @HumanitariansAI"` and `line: "Claude, Investigation Memo."` The narration keeps the IN-FOR-BEAR sign-off ("Liam, in for Bear.") verbatim.
- Updated `BCRY.remotion.props.quote` to match its rewritten narration (previously mirrored the Plain-register carry-out sentence).
- `metadata.purpose` reworded from "in the Plain register" → "in the Teardown register." Everything else in metadata left as the `brand_variant.py` scaffold set it.
- Removed `metadata._variant_todo`.

## Judgement calls

- **Kept `folderLabel` / `channel_title` / `style_preset` as `@HumanitariansAI` / `humanitarians`.** The sibling nbb reel in this book (`nbb-...-ip-clause-review`) did the same — this reel's audience surface is HAI even though the register is now Teardown; the sibling is the closest working precedent, so followed it rather than retargeting to `www.brutalist.art`.
- **Kept `ground: "#F3EBDD"` and the HAI accent `#E4572E` in per-beat props** (BrutalistHesitantWriter, Manim `production_viz.colors`) even though `palette: teardown` at the metadata level implies white/ink/crimson. The scaffold left these; the sibling did too. Changing them would rewire visual assets and drift beyond a voice-only conversion.
- **Reused BHTF as the LLM exercise beat rather than inserting a new `B_LLM` beat.** The source's "your turn handoff" was already a paste-into-LLM prompt in the correct slot — same call the sibling made. Renaming `beat_id` would break the audio/media file mapping (`mp3/beat-BHTF.mp3`, `media/BHTF.mp4`).
- **`_variant_todo` entry #5 ("build: generate_audio_kokoro.py … compile") ignored on purpose.** The supervisor prompt is explicit: this pass does not render, compile, or generate audio.

## Verification

- JSON parses.
- `metadata.audience == "NikBearBrown"`, `register == "Teardown"`, `palette == "teardown"`, `engine == "kokoro"`, `voice_kokoro == "am_onyx"` (all as scaffold set them; untouched).
- `metadata._variant_todo` removed.
- Beat order: B00 → B01 → B02 → B03 → B04 → B05 → B06 → B07 → BCRY → **BHTF (LLM exercise, 2nd-to-last)** → **BOUT (outro, last)**.
- Every beat's `narration_text` rewritten.
- No forbidden phrases ("one could argue," "it seems as though," "innovative"/"revolutionary" without saying what changed, unattached specs).
