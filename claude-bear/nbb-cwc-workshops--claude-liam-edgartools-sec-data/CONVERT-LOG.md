# CONVERT-LOG — nbb-cwc-workshops--claude-liam-edgartools-sec-data

Source register: **Plain** (hai-fellows, `@HumanitariansAI`).
Target register: **Teardown** (nbb, `@NikBearBrown`, Kokoro `am_onyx` — Liam, in for Bear).

## What I changed

- **Every beat narration rewritten in Teardown register.** Voice only — every fact,
  number, file path, and claim from the source survives unchanged. Kept the exact
  four-item anchor list (S03/S08), the mirror pair (S09/S10), the linear
  read→execute→return mechanism (S05–S07), the folder name (`edgartools-sec-data`),
  the file name (`SKILL.md`), and BCRY's carry-out sentence verbatim.
- **BHTF converted to the LLM EXERCISE beat.** Second-to-last, per SKILL.md §3.
  Replaced the source's "read the skill and list four things" handoff (which
  requires the actual skill file to be useful) with a paste-ready prompt that
  produces a useful output on its own in any frontier LLM: (1) why enumerated
  steps make behavior repeatable and why that's a coverage claim not a competence
  claim, (2) a `SKILL.md` skeleton for a small, well-scoped skill, (3) three
  analyst questions this skill would fail on with the correct fix for each.
  Added the `llm_exercise: {prompt, dig_deeper}` block. Composer `command` prop
  shortened for the on-screen composer beat.
- **BOUT switched from `OutroSeries` → `OutroCTA`** to match the NBB brand
  convention on the sibling well-converted reels (`nbb-claude-basics--screenshot-prompt-caching`,
  `nbb-cwc-workshops--claude-liam-reorder-policy`). Handle set to `@NikBearBrown`.
  Narration line unchanged.
- **Brand-facing metadata** updated to NBB: `folderLabel` and `channel_title`
  went from `@HumanitariansAI` → `@NikBearBrown` (metadata + BHTF composer prop
  + outro handle). `brand` field switched to `nbb`. `_variant_todo` removed.
- **`purpose` metadata rewritten** in Teardown register — kept the same object of
  study (the skill's mechanism, the anchor list, the carry-out) but framed as
  taking-it-apart rather than "judgment removed."

## Judgement calls

- **B00 narration length.** The `note` on this beat is explicit that the writer
  animation's window is tuned to a ~30-word narration around 9.98s. I kept the
  rewrite to a similar length (~40 words, 14s estimated) and preserved every
  BrutalistHesitantWriter prop (`triggerWords`, `charMs`, seed) so the render
  doesn't need retuning. If the audio comes in longer than the video, that's a
  timing pass, not a rewrite.
- **BCRY narration left verbatim.** The source line is already in the Teardown
  register ("repeatable, not all-knowing — it only does what the file actually
  wrote down") and the `WantQuote` prop's `quote` field must match the narration
  on-screen. Rewriting the narration would break the shot's on-screen copy.
- **`folderLabel` change is intentional, not a fact drift.** The four-item spec
  list, the SKILL.md machinery, the linear pipeline, and the carry-out are all
  intact. The channel handle is brand identity, not content — the sibling
  well-converted reels all flip it.

## What I did NOT do

- Regenerate audio, render Manim/Remotion, or run `art run`/`art final`. Not
  this pass.
- Modify the source at `anthropics/claude-bear/cwc-workshops--claude-liam-edgartools-sec-data/`.
- Touch beat IDs, act labels, `graphic.production_viz` copy, `manim` scene names,
  or `remotion.props` beyond the two brand-facing prop values called out above.
