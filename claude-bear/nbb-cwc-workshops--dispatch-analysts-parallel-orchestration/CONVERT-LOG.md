# CONVERT-LOG — cwc-workshops--dispatch-analysts-parallel-orchestration → nbb

**Source:** `../cwc-workshops--dispatch-analysts-parallel-orchestration/beat_sheet.json`
**Output:** `beat_sheet.nbb.json`
**Register:** Plain → Teardown (Feynman × MKBHD)
**Voice:** Kokoro `am_onyx` — Liam, in for Bear (unchanged from scaffold)

## What changed

- Rewrote every beat's `narration_text` in the Teardown register per `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Every fact, number, ticker, name, and mechanism claim from the source survives verbatim (NVDA 9 / AMD 6 / MU 4, twenty pages of SEC filings, fifty analysts × thirty seconds = twenty-five minutes serial vs ~thirty seconds parallel, task-ID/findings/confidence/sources contract). Only the voice moved — from Plain description to Teardown machinery-and-design-judgment.
- B00 cold open now opens with "Liam, in for Bear" per IN-FOR-BEAR LAW (SKILL.md and brands/nbb.md). BOUT sign-off already carried it; now both bookends do.
- Removed `_variant_todo` (checklist done).

## Judgement calls

**BHTF promoted to serve as the LLM exercise beat (rather than inserting a separate B_LLM).**
The source already had a "your turn handoff" beat (BHTF) that visually presented a paste-into-Claude prompt via `ClaudeComposerAsk`. Rather than insert a second, functionally-identical beat (`B_LLM`) directly beside it — which would give two consecutive `ClaudeComposerAsk` scenes with overlapping "paste this into Claude" narration — I promoted BHTF: rewrote its narration in the SKILL.md §Step 3 paste-ready + "Go deeper:" format, added the required `llm_exercise` object (`prompt` + `dig_deeper`), and updated the on-screen `command` and `topic` to match. Beat_id preserved (per SKILL.md "Preserve exactly: every beat_id"). Beat position is second-to-last (per SKILL.md §Step 3/5). Trade-off: `act` field changed from "your turn handoff" to "LLM EXERCISE" to reflect the beat's new function — the only `act` change in the sheet.

**BOUT re-branded to NikBearBrown outro.**
Source BOUT signed off with handle `@HumanitariansAI` and no site URL. SKILL.md §Step 4 requires the NikBearBrown outro (default channel: `www.brutalist.art`). I did not have the book's `AUTHOR.MD` to source exact text from, so I inferred a minimal NBB outro: kept the existing "Liam, in for Bear" sign-off, appended "More at brutalist dot art" to the narration and "More at brutalist.art." to the on-screen `OutroCTA` line, and swapped the handle to `@NikBearBrown`.

**folderLabel / channel_title switched to `@NikBearBrown`.**
The scaffold left `folderLabel` and `channel_title` at `@HumanitariansAI` (source reel's destination). Since the audience is `NikBearBrown` and the outro is now NBB-branded, I made the on-screen chip in the promoted LLM-exercise beat (`ClaudeComposerAsk.folderLabel`) match, and set the metadata `folderLabel` / `channel_title` to `@NikBearBrown` for consistency. `ground` (`#F3EBDD`) and `style_preset` (`humanitarians`) left as the scaffold set them — the palette is `teardown` per SKILL.md but the reel-body Remotion patterns were built against the HAI ground; changing that would demand a re-render of every body beat and is out of scope for a voice-only conversion.

## Beat ordering (final)

B00 → B01 → B02 → B03 → B04 → B05 → B06 → B07 → B08 → BCRY → **BHTF (LLM exercise, second-to-last)** → **BOUT (NBB outro, last)**.

## What I did NOT do

- Did not render, compile, or generate audio. Beat sheet only.
- Did not touch source (`../cwc-workshops--dispatch-analysts-parallel-orchestration/`).
- Did not fabricate facts. Every claim is from the source sheet.
- Did not modify `shot` blocks, `graphic` blocks, `build` blocks, `remotion.rendered` paths, or `estimated_duration_s` values (rendering pass will recompute against the rewritten narration audio).
