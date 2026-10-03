# CONVERT-LOG — nbb-financial-services--claude-liam-earnings-analysis

Converted `beat_sheet.json` (Plain, hai-simple) → `beat_sheet.nbb.json` (Teardown, NikBearBrown).

## What changed

- **All 7 source narrations rewritten in the Teardown register** (Feynman × MKBHD).
  Explain the machinery of a Claude skill (folder + SKILL.md, Steps section,
  linear execution, narrow scope), name the design bets (briefing beats retraining
  for one-off jobs; linearity trades flexibility for predictability; scope
  narrowness is the point). Facts unchanged — every spec (8–12 pages, 1–3 tables,
  8–12 charts, "earnings-analysis" name, SKILL.md, Steps section) preserved.
- **B00 cold open** now opens with "Liam here, in for Bear." per IN-FOR-BEAR LAW.
  Source cold open did not carry the identification. `estimated_duration_s` bumped
  from 14 → 20 to fit the longer teardown line while keeping the ≥9s typing window
  the WRITER LAW note requires.
- **B_LLM inserted as second-to-last beat** (new `beat_id: "B_LLM"`, `act: "LLM
  EXERCISE"`). Paste-ready prompt asks the model to place Claude skills against
  fine-tuning and RAG and force the trade-offs into the open — produces a useful
  output on its own without the video. `dig_deeper` asks the viewer to draft a
  SKILL.md for their own repeatable job. Shot type CARD / own / hold.
- **BOUT rewritten as NikBearBrown outro**. Points to `@NikBearBrown` (YouTube)
  and `nikbearbrown.com` (web), sourced from
  `anthropics/youtube/ai-1/AUTHOR.MD` :: NikBearBrown. `OutroCTA.handle` swapped
  from `@HumanitariansAI` → `@NikBearBrown`.
- **`_variant_todo` removed** from metadata.
- Every `beat_id`, act label, shot block, graphic block, on-screen card copy,
  Remotion pattern name and prop values preserved intact.
- `estimated_duration_s` values raised on rewritten beats to reflect longer
  Teardown narrations; `actual_duration_s` values (stripped by the scaffold) not
  re-added — audio pass will measure and write them back.

## Judgement calls

- **BHTF kept + B_LLM added, rather than converting BHTF into B_LLM.**
  Preserve-exactly rule for `beat_id`s forbids renaming BHTF. The two are
  complementary: BHTF is the concrete Claude prompt for the earnings-analysis
  skill itself; B_LLM is the abstract comparative-thinking prompt (skills vs
  fine-tuning vs RAG) plus a viewer-side design exercise. No content overlap.
- **Outro handle changed to `@NikBearBrown`.** Metadata `folderLabel` /
  `channel_title` still read `@HumanitariansAI` (scaffold set them; not touching
  what the scaffold set), but the outro is the NBB brand outro and must point at
  the NBB channel. Downstream render will show `@NikBearBrown` on the outro card
  and `@HumanitariansAI` on the composer folder chip — that split is correct for
  a cross-posted NBB variant.
- **Palette / hex mismatch left alone.** `metadata.palette` is `teardown`
  (white / ink / one red) but shot props on B00 and the graphic blocks still
  carry the humanitarians hexes (`#F3EBDD` ground, `#E4572E` accent).
  Preserve-shot-blocks rule wins; a render pass will retint if needed. Flagged
  here so the render side doesn't miss it.
- **B_LLM has no `audio_file` yet** and `build.status: "PLANNED"`. Audio
  generation is a separate pass.
