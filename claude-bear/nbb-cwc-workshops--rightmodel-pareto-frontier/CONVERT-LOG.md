# CONVERT-LOG — cwc-workshops--rightmodel-pareto-frontier → nbb

**Source:** `../cwc-workshops--rightmodel-pareto-frontier/beat_sheet.json`
**Output:** `beat_sheet.nbb.json`
**Register:** Plain → Teardown (Feynman × MKBHD)
**Voice:** Kokoro `am_onyx` — Liam, in for Bear (unchanged from scaffold)

## What changed

- Rewrote every beat's `narration_text` in the Teardown register per
  `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Every fact and
  number from the source survives verbatim: three models (Opus, Sonnet,
  Haiku); customer-support classification; Opus 2× Sonnet's price; Haiku
  −8 accuracy points and −3¢; same eval-suite / two-numbers-per-model
  sweep; the non-dominated rule; per-million-token pricing
  ($15/$75, $3/$15, $0.25/$1.25); accuracy tiers (98/90/82%); real-dot
  positions ($0.01/82%, $0.04/90%, $0.08/98%); Sonnet-vs-Opus $4,000 per
  100K calls; 95% threshold → Opus-only; 82% threshold → Haiku is the
  frontier point. Only the voice moved — from Plain description to
  Teardown machinery-and-design-judgment.
- B00 cold open now opens with "Liam, in for Bear" per IN-FOR-BEAR LAW
  (SKILL.md and brands/nbb.md). BOUT sign-off already carried it; now
  both bookends do.
- Bumped `estimated_duration_s` on beats where the Teardown rewrite added
  meaningful length (e.g. S02 8s → 13s, S04 11s → 17s, S07 15s → 20s,
  S08 11s → 19s, BHTF 13s → 24s). Timing law is audio-first: the audio
  regenerator will overwrite these with measured durations, but a
  closer initial estimate helps the review-cut pipeline.
- Removed `_variant_todo` (checklist done).
- Removed stale `actual_duration_s` values from every beat (they refer
  to the OLD Plain-register audio; the Teardown pass will regenerate).

## Judgement calls

**BHTF promoted to serve as the LLM exercise beat (rather than inserting
a separate B_LLM).** The source already had a "your turn handoff" beat
(BHTF) that visually presented a paste-into-Claude prompt via
`ClaudeComposerAsk`. Rather than insert a second, functionally-identical
beat directly beside it — two consecutive `ClaudeComposerAsk` scenes with
overlapping "paste this into Claude" narration — I promoted BHTF:
rewrote its narration into the SKILL.md §Step 3 paste-ready +
"Go deeper:" format, added the required `llm_exercise` object (`prompt` +
`dig_deeper`), and updated the on-screen `command`, `topic`, `segment`,
and `folderLabel` to match. `beat_id` preserved per SKILL.md ("Preserve
exactly: every beat_id"). Beat position is second-to-last per SKILL.md
§Step 3/5. Trade-off: `act` field changed from "your turn handoff" to
"LLM EXERCISE" — the only `act` change in the sheet. Matches the same
choice made in the sibling
`nbb-cwc-workshops--dispatch-analysts-parallel-orchestration` reel.

**BOUT re-branded to NikBearBrown outro (`OutroCTA`, not `OutroSeries`).**
Source BOUT signed off with the title + "Liam, in for Bear" via
`OutroSeries` (`eyebrow` + `line`, `@HumanitariansAI`). SKILL.md §Step 4
requires the NikBearBrown outro (default channel: `www.brutalist.art`);
either `OutroSeries` or `OutroCTA` is allowed by the SKILL. I swapped to
`OutroCTA` (line + handle) to match the sibling nbb reels in this book
and to carry the site URL naturally, appended "More at brutalist dot art"
to the narration and "More at brutalist.art." to the on-screen `line`,
and set the handle to `@NikBearBrown`. Book has no `AUTHOR.MD :: NikBearBrown`
section directly (only `youtube/ai-1/AUTHOR.MD` at the book-tree root,
which lists the handle and the `nikbearbrown.com` / `@NikBearBrown`
channel — consistent with what I wrote).

**folderLabel / channel_title switched to `@NikBearBrown`.** The scaffold
left `folderLabel` and `channel_title` at `@HumanitariansAI` (the source
reel's HAI destination). Since the audience is `NikBearBrown` and the
outro is NBB-branded, I made the metadata `folderLabel` /
`channel_title` and the on-screen chip on BHTF's `ClaudeComposerAsk`
match `@NikBearBrown`. `ground` (`#F3EBDD`) and `style_preset`
(`humanitarians`) left as the scaffold set them — the palette is
`teardown` per SKILL.md but the reel-body Manim scenes were built
against the HAI ground; changing that would demand a re-render of
every body beat and is out of scope for a voice-only conversion.
Also set metadata `brand` to `nbb` (source had `hai-fellows`).

## Beat ordering (final)

B00 → S01 → S02 → S03 → S04 → S05 → S06 → S07 → S08 → S09 → S10 → BCRY
→ **BHTF (LLM exercise, second-to-last)** → **BOUT (NBB outro, last)**.

## What I did NOT do

- Did not render, compile, or generate audio. Beat sheet only.
- Did not touch source (`../cwc-workshops--rightmodel-pareto-frontier/`).
- Did not fabricate facts. Every claim is from the source sheet.
- Did not modify `shot.remotion.props` on B00 (BrutalistHesitantWriter
  props, including `text`, `triggerWords`, `replacementWords`, `seed`,
  and `bg` `#F3EBDD` — the HAI ground the writer was already built
  against), `graphic` blocks, `build` blocks, `remotion.rendered` paths,
  or `manim` scene names. The rendering pass will recompute against the
  rewritten narration audio.
