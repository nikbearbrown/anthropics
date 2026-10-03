# CONVERT-LOG — claude-for-legal--claude-liam-matter-close

Source: `../claude-for-legal--claude-liam-matter-close/beat_sheet.json` (8 beats, Plain register).
Output: `beat_sheet.nbb.json` (7 beats, Teardown register).

## What changed

- **Register — every beat rewritten to Teardown (Feynman × MKBHD).** Explain the machinery, name what the design is optimized for and what it costs. Facts unchanged (matter-close archives out of the active portfolio without deleting; scope is outcome/final exposure/lessons; execution is linear).
- **B00 cold open.** Added the IN-FOR-BEAR sign-in ("Liam here, in for Bear.") — required by IN-FOR-BEAR LAW; the source omits it. Hesitant-writer visual (DELETE → archive) unchanged.
- **B01 anatomy.** Reframed as mechanism-first — "a folder Claude reads before it works" — and named the trade-off ("legibility over cleverness"). Card props untouched.
- **B02 pipeline.** Added the Teardown lens on linear execution ("what that buys you is predictability; what it costs is cleverness"). Phases and diagram unchanged.
- **B03 mechanism.** Named the design choice out loud: "reversibility over cleanliness — the archive stays lightly cluttered, but nothing you might need later is gone."
- **BCRY carry-out.** Reworded as design promise ("The file is the boundary; the file is the promise"). The on-card `quote` prop is left as the source line — that quote reads as a stand-alone carry-out and matches the WantQuote pattern.
- **BHTF → LLM EXERCISE.** Following the sibling `nbb-claude-for-legal--claude-liam-ip-clause-review` convention, the original "Your Turn handoff" beat is **repurposed** as the LLM exercise beat (rather than adding a second B_LLM beat). The prompt now works in any frontier LLM without depending on the matter-close skill file: it asks the model to walk through outcome / exposure / lessons on a pasted matter summary and draft an archive record; the dig-deeper follow-up pushes toward a seven-year privilege-log retention rule. `act` renamed `LLM EXERCISE`; `llm_exercise` object added; `ClaudeComposerAsk` retained.
- **BOUT + BCTA → single BOUT outro.** Also per the IP-clause-review sibling: the two source outro beats (OutroSeries "Claude, Matter Close." + OutroCTA "…Liam, in for Bear.") are **collapsed into one OutroCTA beat** so the LLM exercise sits literally at position `-2` (second-to-last) and the outro at position `-1` (last). Combined line: "Claude, Matter Close — archived, not deleted. Liam, in for Bear." Handle stays `@HumanitariansAI`.
- **Metadata.** `_variant_todo` removed. `metadata.build.filled/of` updated 8 → 7 to match the new beat count. Everything else the scaffold set (audience, register, engine, voice_kokoro, palette, typography, outro_source) left as-is.

## Judgement calls

1. **BHTF repurposed, not augmented.** Task instructions said "insert the LLM exercise beat"; the sibling convention says "repurpose the existing Your Turn beat". I followed the sibling — inserting a separate B_LLM would produce two back-to-back paste-into-Claude beats and split a single logical beat in half. The `beat_id` is preserved.
2. **Outro collapsed.** Same source: sibling reels drop OutroSeries and keep one OutroCTA whose `line` combines the series title with the Liam sign-off. This is what puts the LLM exercise literally at index `-2`, which is what the supervisor's "second-to-last / last" check reads.
3. **`@HumanitariansAI` kept as folder/channel/handle.** The scaffold left these as the source values, and the reference sibling (`nbb-claude-for-legal--claude-liam-ip-clause-review`) also keeps `@HumanitariansAI` throughout. Not swapping to `@NikBearBrown` even though `audience: NikBearBrown` — the two are separate axes here.
4. **Estimated durations bumped where narration lengthened.** These are hints for scheduling; the audio pass regenerates real durations from the MP3s, so this is not authoritative.
5. **`redo_of` line kept verbatim.** It documents the earlier Teardown source and where its `source_skill` path went missing — the note stays useful for a next writer.

## What I did not do

- Did not run `generate_audio_kokoro.py`, `compile.py`, or any renderer.
- Did not touch the source `beat_sheet.json` or any file under `../claude-for-legal--claude-liam-matter-close/`.
- Did not add build metadata for the new BHTF role (`build.at` etc. stayed at the scaffold's timestamps — the audio pass will overwrite them).
