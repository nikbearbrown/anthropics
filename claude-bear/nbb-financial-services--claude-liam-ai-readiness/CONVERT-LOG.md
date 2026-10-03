# CONVERT-LOG — nbb-financial-services--claude-liam-ai-readiness

Register conversion: source `beat_sheet.json` (Plain, claude-liam / @HumanitariansAI)
→ `beat_sheet.nbb.json` (Teardown, NikBearBrown).

## What changed

- **Removed** `_variant_todo` from metadata.
- **Rewrote every `narration_text`** in the Teardown register (Feynman × MKBHD):
  named the mechanism, named the design trade-off ("optimized for grounding in
  the operator's own words, at the cost of catching opportunities the operator
  forgot to write down"), kept every fact — the four-stage pipeline (ingest →
  identify → score → rank), the Portco A / Q3 anchor, both-directions read on
  the ranking, and the operating-partner sign-off gate.
- **Preserved** every `beat_id`, `act`, `shot`, `graphic`, `remotion` block, and
  the BCRY `WantQuote` on-screen quote (already carry-out register).
- **Inserted `B_LLM`** as the second-to-last beat: paste-ready prompt that asks
  a frontier LLM to play the ai-readiness skill against a pasted quarterly
  update (extract, score, rank, then name what it did NOT invent) + one
  dig-deeper follow-up on private-notes access and defensibility. `CARD /
  own / hold` shot per SKILL.md schema.
- **Replaced BOUT** with the NikBearBrown outro — narration and `OutroCTA.line`
  now end "Take it apart at brutalist.art.", `handle` swapped from
  `@HumanitariansAI` to `www.brutalist.art` (default NBB channel per
  `brands/nbb.md` + SKILL.md, no `AUTHOR.MD` exists in this book).
  `estimated_duration_s` bumped 6 → 8 to fit the added CTA phrase.

## Judgement calls

- **BCRY narration & `WantQuote` prop left unchanged** — the source carry-out
  sentence already reads Teardown-clean (direct, machinery-named, no forbidden
  phrases). Rewriting it risked drifting from the on-screen quote.
- **`folderLabel` / `channel_title` / `style_preset` in metadata left as
  `@HumanitariansAI` / `humanitarians`** — SKILL.md prohibits re-scaffolding, and
  those fields are set by `brand_variant.py`. Only the outro's audience-facing
  line and handle were switched to the NBB channel, which is what the audio
  actually says.
- **`estimated_duration_s` on rewritten beats left at source values** — narration
  word counts are within a couple of seconds of the originals (all beats have
  higher word density where the mechanism required naming, but rendering will
  regenerate audio and rewrite `actual_duration_s` from Kokoro).
