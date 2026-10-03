# CONVERT-LOG — nbb cut

Source: `anthropics/claude-bear/financial-services--claude-liam-nav-tieout/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)

## Changes made

- **Metadata** — `register: "Plain" → "Teardown"`; `palette: "humanitarians" → "teardown"`; `folderLabel` and `channel_title: "@HumanitariansAI" → "@NikBearBrown"` to match the NBB brand (`brands/nbb.md`); rewrote `purpose` to name the Teardown angle (the design choice that made nav-tieout a checker, not an auditor). Removed `_variant_todo`.
- **B00 (cold open)** — rewrote as Liam self-introducing (IN-FOR-BEAR LAW) inside the BrutalistHesitantWriter 20–35-word window; on-card copy ("proves"→"assumes") untouched — it *is* the teardown moment.
- **B01–B07** — every narration rewritten in Teardown register: name the machinery, name the design choice, name the trade-off. On-screen chip labels and captions preserved verbatim (they already read as Teardown). `estimated_duration_s` bumped where the rewrite runs longer than the original (B02, B03, B04, B05, B07) so the audio-first clock is honest.
- **BCRY (carry-out)** — narration slightly re-voiced; the on-card quote + sparkLine kept verbatim so the audio matches the card.
- **BHTF → LLM exercise (second-to-last)** — repurposed the existing BHTF handoff beat as the LLM-exercise beat per `nbb/SKILL.md` §Step 3. Added `llm_exercise: { prompt, dig_deeper }`. Prompt is a paste-ready block for any frontier LLM that produces useful output on its own (walk through the recomputation before doing it; spell out which NAV-pack line items feed which LP-statement fields; what a flag proves in each direction). Dig-deeper is a genuine next question, not a summary. `ClaudeComposerAsk` props updated: greeting "Try it yourself.", command shortened to fit the composer card, folderLabel switched to `@NikBearBrown`.
- **BOUT (outro)** — kept `OutroCTA` shot; switched handle to `@NikBearBrown` and added the brutalist.art CTA line per `brands/nbb.md` (default channel `www.brutalist.art`). Liam signs off "in for Bear" (IN-FOR-BEAR LAW).

## Judgement calls

1. **Reused BHTF as the LLM-exercise beat rather than inserting a new B_LLM.** The source already had BHTF sitting second-to-last as a "paste this into Claude" handoff — inserting a new beat would have left BHTF orphaned or forced a rename. Preserving `beat_id` (per the "preserve exactly" rule) and shaping the beat to the SKILL.md §Step 3 schema seemed cleaner than a structural insert. Same `beat_id`, same `ClaudeComposerAsk` shot, new payload.
2. **Switched the outro handle from `@HumanitariansAI` to `@NikBearBrown` in `metadata.channel_title`, `metadata.folderLabel`, BHTF `folderLabel`, and BOUT `handle`.** The scaffold left those as the source `@HumanitariansAI`, but the NBB brand spec is explicit that this cut ships on `@NikBearBrown` — leaving the HAI handle would have produced a beat sheet whose outro card announced the wrong channel. Every non-channel fact (numbers, mechanism, LP/NAV pack details) is unchanged.
3. **Bumped `estimated_duration_s` on beats whose rewrite runs longer than the source.** Audio-first: durations are outputs, but the estimate is what the clock uses before audio is generated. Left `actual_duration_s` off so the renderer regenerates it from the new Kokoro pass.

## Not done

Rendering, audio generation, compile — out of scope per supervisor instructions. Next pass: `generate_audio_kokoro.py` → recompile.
