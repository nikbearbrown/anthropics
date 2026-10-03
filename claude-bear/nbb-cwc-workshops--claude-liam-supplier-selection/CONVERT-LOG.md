# CONVERT-LOG — nbb cwc-workshops--claude-liam-supplier-selection

Converted `beat_sheet.json` (Plain / HAI cut) into `beat_sheet.nbb.json`
(Teardown / NikBearBrown cut). Source untouched.

## What changed

- **Every beat's `narration_text` rewritten in the Teardown register**
  (Feynman × MKBHD): machinery explained ("Here's what's actually
  happening…"), design choice named ("cost dominates, but speed and
  dependability each earn a real vote"), trade-off called out ("the formula
  gets repeatability; the notes get the last word"). Facts, numbers, and
  file references unchanged.
- **B00 cold open** carries the IN-FOR-BEAR LAW — "Liam here, in for Bear."
  Trimmed to 25 words to stay inside the WRITER LAW 20–35-word window so
  BrutalistHesitantWriter still lands the `cheapest → highest-scoring`
  correction on screen.
- **BHTF converted to the LLM exercise beat** (second-to-last, in the slot
  the source's "your turn handoff" already occupied — no beat_id churn).
  Added the `llm_exercise` object: a paste-ready prompt for Claude / ChatGPT
  / Gemini that walks the viewer through building a weighted-score picker
  from scratch (factors, normalization, weights, override room, a worked
  three-candidate example), plus a real dig-deeper on weight fragility /
  sensitivity — "what's the smallest change to your weights that flips the
  top pick, and does that fragility mean the weights are wrong or that two
  candidates are just genuinely close?" On-screen `command` prop tightened
  to a shorter paraphrase so the composer chip still reads cleanly; the full
  prompt lives in `llm_exercise.prompt`. Act relabelled `LLM EXERCISE`.
- **BOUT replaced with the NikBearBrown outro** — Liam sign-off restated
  (IN-FOR-BEAR LAW), channel `@NikBearBrown`, default URL brutalist.art
  (no `AUTHOR.MD :: NikBearBrown` in this book — used the default channel per
  `brands/nbb.md`). OutroCTA pattern preserved.
- **On-screen brand chips flipped to `@NikBearBrown`**: `folderLabel` on
  BHTF's ClaudeComposerAsk and `handle` on BOUT's OutroCTA. Metadata's
  `folderLabel` / `channel_title` updated to match — the source was HAI, the
  cut is NBB.
- **`_variant_todo` removed** — all four items executed.
- **`estimated_duration_s` bumped on longer beats** (B01 12→14, B04 14→15,
  BHTF 24→22, BOUT 6→10) to fit the rewritten wordcount. Kokoro measures
  narration and rewrites `actual_duration_s` at build time, so these are
  hints only.
- Preserved verbatim: every `beat_id`, `act` copy (except the repurposed
  BHTF), all `shot` blocks and `graphic.production_viz` chip/label/caption
  copy (still fits Teardown), and the BCRY carry-out sentence + `WantQuote`
  props — the on-screen payoff already reads Teardown ("isn't the cheapest…
  and a note the formula never sees can still beat it").

## Judgement calls

- **Kept the source palette hexes in the BrutalistHesitantWriter and
  production_viz color arrays** (`#F3EBDD` ground, `#E4572E` accent). Those
  are HAI-warm-paper values, not the teardown palette's `#FFFFFF` / `#C8102E`.
  The nbb SKILL.md and brands/nbb.md both say the palette is `teardown`, but
  the beat sheet's per-beat `colors` arrays and BrutalistHesitantWriter
  `ink`/`accent`/`bg` props are shot-level overrides that the scaffold left
  untouched. Rewriting them here would go beyond "voice, not facts" and
  risk breaking the already-rendered `media/*.mp4` assets that the compile
  step keys off. Left as-is; if the palette flip is wanted, that's a
  separate pass on shot props (or a re-scaffold), not a narration rewrite.
- **Kept `style_preset: "humanitarians"`** and `ground: "#F3EBDD"` in
  metadata for the same reason — scaffold set them, they gate downstream
  render styling, and touching them here would silently re-skin without
  approval.
- **Reused BHTF as the LLM exercise beat** rather than inserting a new
  `B_LLM` beat before it. The source's "your turn handoff" already occupied
  the second-to-last slot with a Claude paste prompt in the same shot
  pattern; adding a second LLM-exercise beat would duplicate the beat and
  fight the "preserve every beat_id" rule. Repurposing BHTF is the minimal
  change that satisfies Step 3.
