# CONVERT-LOG — nbb-claude-for-legal--claude-liam-diligence-issue-extraction

Voice conversion pass. Facts unchanged; register only.

## What changed

- **B00 (cold open)** — rewrote naive framing into a Teardown open. Names the design choice ("that's a design choice, not a limit") and previews the machinery. Kept the ~35-word budget so the BrutalistHesitantWriter's 9s typing window still fits (TIMING LAW).
- **B01 (anatomy)** — rewrote to expose the machinery (plain-English file, no hidden code, nothing to grep) and name what was optimized for ("something a lawyer can audit"). Shot props unchanged.
- **B02 (pipeline)** — condensed to "linear — no branching unless a step spells it out. Predictable, not adaptive. That's the trade." Shot props unchanged.
- **B03 (mechanism)** — named the interesting constraint ("closed list") and the flip side ("miss the list, and the skill misses the issue"). Shot props unchanged.
- **BCRY (carry-out)** — same operational fact, sharper judgment: "the skill isn't a lawyer; it's a screening pass that never gets tired." Trimmed the WantQuote card copy so the on-screen line lands cleanly.
- **BHTF → LLM EXERCISE (second-to-last)** — converted the "your turn handoff" into a paste-ready LLM prompt beat per §Step 3. Added the `llm_exercise` block with a fully-formed Claude/ChatGPT/Gemini prompt (build a six-item diligence checklist → screen the pasted contract → quote clauses → one follow-up for counterparty) plus a real dig-deeper follow-up (which flag actually kills the deal, and why that judgment is the lawyer's job, not the checklist's). Kept ClaudeComposerAsk pattern; updated `folderLabel` to `@NikBearBrown`, `runningText` to "paste this into Claude, ChatGPT, or Gemini…", and `segment` to the title-cased episode line.
- **BOUT (outro, last)** — swapped OutroSeries for OutroCTA, folded the "…Liam, in for Bear." sign-off (previously BCTA) into a single consolidated outro line, `handle: @NikBearBrown`. `tail_silence_s: 1.0` preserved.
- **BCTA** — dropped. Its copy folds into BOUT so the LLM EXERCISE lands as SECOND-TO-LAST and the outro is the true last beat, per SKILL.md §Step 5.
- **Metadata** — `_variant_todo` removed. `audience`, `register`, `palette`, `engine`, `voice_kokoro`, `derived_from`, `outro_source`, `typography` all left as the scaffold set them (no re-scaffold).

## Judgement calls

1. **Merged BCTA into BOUT rather than keeping both outro beats.** The two-beat outro (BOUT OutroSeries + BCTA OutroCTA) would push the LLM EXERCISE to third-to-last, violating the SECOND-TO-LAST rule in SKILL.md §Step 5. Referenced `nbb-books--claude-liam-data/beat_sheet.nbb.json` for the consolidation pattern.
2. **Kept `folderLabel`/`channel_title` on the metadata as `@HumanitariansAI`.** These weren't in the "do not re-scaffold" fence list, but touching them looked scaffold-adjacent. Instead I only updated the visible chip in the LLM EXERCISE beat and the OutroCTA handle to `@NikBearBrown` — the NBB brand chrome now shows on the two beats that render on-screen brand marks. The metadata field can be updated by a later pass without touching narration.
3. **Kept the humanitarians palette hex values in shot props** (`bg #F3EBDD`, `accent #E4572E`, `ink #2F2A26`). Reference reel `nbb-claude-for-legal--claude-liam-ip-clause-review` does the same — the palette override is metadata-driven at render time; shot-level hexes are preserved verbatim per SKILL.md §Step 2.
4. **Tuned estimated_duration_s per beat** based on rough Kokoro rate (~2.7 wps) — actual_duration_s will be set by regenerated audio, so these are hints only.

## Not done (out of scope for this pass)

- No audio generated. `audio_file` paths preserved; regeneration is a separate pass (Kokoro `am_onyx`).
- No re-render. `media/*.mp4` files reference the source's humanitarians-palette renders; the NBB teardown palette wants different card visuals. Handled by the compile pass.
