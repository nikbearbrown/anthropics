# CONVERT-LOG — cwc-workshops--claude-liam-forecasting → nbb

Register conversion Plain → Teardown (Feynman × MKBHD). Voice change only; every fact, beat_id, act, shot block, and on-screen card copy from the source is preserved.

## Narration rewrites

- **B00** — cold open reframed as an assumption teardown ("Here's the assumption people bring in…"). Word count kept in the 20–35 window for BrutalistHesitantWriter TIMING LAW; on-screen text (always → sometimes) unchanged.
- **NB01** — mechanism opened with "Here's what's actually inside a skill" and closed with a design-judgment line ("The design isn't clever. It's a lookup table plus code.").
- **NB02** — branching rewritten as an optimization call ("They optimized for context economy — the subagent gets its own window, the main thread stays clean. The trade-off is real: every delegation is an extra call.").
- **NB03** — confidence + estimate section closed with the design-choice frame ("The design choice is reproducibility, not omniscience.").
- **BCRY** — narration prefixed "Here's what's actually happening." On-screen `quote` and `sparkLine` left unchanged (already fit the register).
- **BHTF** — closing line rewritten as a Teardown test criterion ("The honest test isn't whether Claude gives you a number. It's whether it names the flag that decided the path.").

## New beats

- **B_LLM (new, second-to-last)** — LLM EXERCISE per SKILL.md §Step 3. Paste-ready design brief (six flags + trade-offs + confidence-threshold reasoning) that produces useful output without the video. "Go deeper" follow-up: what breaks if the threshold is too high, and detection in production. Rendered via ClaudeComposerAsk in the teardown palette (the CARD schema in SKILL.md is a shape hint, not a literal renderer — ClaudeComposerAsk is the ASK-scene contract Step 1 pins for NBB sheets, so I reused it here to keep the paste-ready visual consistent with BHTF).
- **BOUT (replaced)** — NikBearBrown outro pulled from `books/anthropics/youtube/ai-1/AUTHOR.MD :: NikBearBrown`. Narration: "Flags Decide The Path. Liam, in for Bear. Find more at nikbearbrown.com, or on YouTube at @NikBearBrown." OutroCTA `handle` set to `@NikBearBrown` (was `@HumanitariansAI`).

## Judgment calls

- **Channel handle swap.** Source targeted @HumanitariansAI. The nbb variant belongs to Nik Bear Brown's channel per SKILL.md §Step 4 and `outro_source: AUTHOR.MD :: NikBearBrown`, so I switched `metadata.folderLabel`, `metadata.channel_title`, `BHTF.folderLabel`, and `BOUT.handle` to `@NikBearBrown`. The mining sibling still shows `@HumanitariansAI` — I'm reading that sibling as unfinished (its `_variant_todo` is still present) and following the SKILL.md, not the sibling.
- **B_LLM renderer.** SKILL.md's example schema uses `CARD` — I kept `shot.type: "CARD"` but populated a `remotion.pattern: "ClaudeComposerAsk"` block, which is the ASK/paste-in scene the Step 1 rule pins for every NBB beat sheet. Reason: the audio pass + compile expect a renderable pattern; ClaudeComposerAsk matches the BHTF visual and puts the paste-ready prompt on the composer surface.
- **AUTHOR.MD source of truth.** brands/nbb.md names `www.brutalist.art` as the default channel, but `outro_source` on this sheet is literally `AUTHOR.MD :: NikBearBrown`, and the AUTHOR.MD at `books/anthropics/youtube/ai-1/AUTHOR.MD` gives the website nikbearbrown.com and channel @NikBearBrown. Followed AUTHOR.MD.
- **Durations.** `estimated_duration_s` values kept from source where narration length is comparable; bumped B_LLM to 32 s and BOUT to 8 s for the new copy. `actual_duration_s` fields were already stripped by the scaffold and stay absent — they will be regenerated at the audio pass.

## Ending order (verified)

B00 → NB01 → NB02 → NB03 → BCRY → BHTF → **B_LLM (second-to-last)** → **BOUT (last)**.

## Untouched

Every `beat_id`, `act`, `shot.type`, Manim scene name, `production_viz` block, `remotion.pattern` (except B_LLM which was newly added), `voice`, and `engine`. Every factual claim: two Python scripts and their filenames, the four flag categories, ninety-day history requirement, 0.6 confidence threshold, `forecast_qty` as a computed estimate.
