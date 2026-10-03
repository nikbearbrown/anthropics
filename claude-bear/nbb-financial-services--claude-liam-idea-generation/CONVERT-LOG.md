# CONVERT-LOG — nbb-financial-services--claude-liam-idea-generation

Register conversion Plain → Teardown (NikBearBrown), 2026-09-03.
Source: `../financial-services--claude-liam-idea-generation/beat_sheet.json`.

## What changed

- Rewrote `narration_text` on every beat (B00–B07, BCRY, BHTF, BOUT) in the
  Teardown register — take-it-apart mechanism + design-choice naming, per
  `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Facts, numbers,
  ordering, and the FCF-up + insider-buying anchor are unchanged; only the
  voice moved.
- BHTF: repurposed the "your turn handoff" beat into the LLM EXERCISE beat
  (second-to-last, per SKILL.md §Step 3). Added the `llm_exercise` block —
  paste-ready SKILL.md-authoring prompt keyed to five viewer-choice screens
  (undervalued small-caps, sector rotation, earnings-momentum longs,
  insider-buying names, dividend-growth) + a "go deeper" question that
  surfaces the seam between what a screen finds and what the viewer's own
  judgment finds. Estimated duration bumped 23 → 42s to fit the fuller prompt.
- BOUT: kept the outro line ("Claude, Idea Generation. Liam, in for Bear.")
  per IN-FOR-BEAR LAW; flipped `handle` to `@NikBearBrown`.
- Metadata: `folderLabel` and `channel_title` flipped from `@HumanitariansAI`
  to `@NikBearBrown` (matches sibling nbb reels + AUTHOR.MD :: NikBearBrown).
  BHTF `folderLabel` prop flipped the same way. `purpose` rewritten to name
  the Teardown mission (mechanism + trade-off).
- BCRY: extended the WantQuote quote/narration by one clause to carry the
  Teardown trade-off — "…and the taste that says which candidate is actually
  worth owning isn't in the file." Same fact set; register-shifted.
- Removed `_variant_todo`.

## Preserved exactly

- All 11 `beat_id`s and their order.
- All `shot` / `graphic` / `remotion` props (visual media is already rendered
  in the source palette; not our job to re-skin or re-render).
- B00's `BrutalistHesitantWriter` props — `triggerWords: brainstorms`,
  `replacementWords: screens for` — and the narration still names the
  correction ("brainstorms" → "screens for") so the writer's visible fix
  matches what Liam reads.
- `estimated_duration_s` on B00–B07, BCRY, BOUT; `voice: am_onyx`,
  `engine: kokoro` throughout.

## Judgement calls

- **Kept `ground` `#F3EBDD` and Manim `colors` at the humanitarians triple.**
  Metadata declares `palette: teardown` (per scaffold), but the Manim scenes
  and the B00 writer already rendered in the source palette. Matches the
  sibling `nbb-financial-services--claude-liam-deal-sourcing/beat_sheet.nbb.json`,
  which does the same. Re-tinting the palette without a re-render would only
  make the sheet lie about what's on disk.
- **BHTF estimated_duration bumped 23 → 42s.** The upgraded prompt is longer
  (naming quant screen + thematic check + pattern rule + all five screen
  options) and matches the sibling's 36s scale. Actual duration comes from
  the audio pass; this is a hint, not the clock.
- **BCRY quote-and-narration were extended, not just re-voiced.** The
  original carry-out closed on reproducibility; the Teardown version has to
  name the trade-off (what the file does NOT contain) or it's just the Plain
  sentence with harder consonants. The `WantQuote` card renders the quote
  literally, so quote and narration were kept identical.

## Not done (per supervisor scope)

- No audio generation, no compile, no render. Deliverable is
  `beat_sheet.nbb.json` only.
