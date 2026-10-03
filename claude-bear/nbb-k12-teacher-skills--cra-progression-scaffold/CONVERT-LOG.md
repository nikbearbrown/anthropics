# CONVERT-LOG — k12-teacher-skills--cra-progression-scaffold → nbb

Source: `anthropics/claude-bear/k12-teacher-skills--cra-progression-scaffold/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Every fact from the source survives unchanged: 1/3 + 1/2 = 5/6 across
  fraction circles / tape diagram / equation; the three-entry-point mapping
  (below → Concrete, at → Representational, above → Abstract); the expertise-
  reversal effect (concrete support that helps a novice becomes noise for an
  expert); the scaffolding three-part contract (contingency, fading, transfer);
  the "support that once matched five sixths on the circles" anchor payoff; and
  the carry-out (one target, three rungs, no skipped steps). Voice-only edit
  throughout: named the design move explicitly ("the arrows between the rungs,
  not the rungs themselves"), surfaced the trade-off ("CRA buys upward mobility
  across representations; it costs you an evaluator that watches for the climb,
  not just the arrival"), and made intellectual-honesty tests concrete ("pull
  the rung out and see if the learning still holds — that separates a ladder
  from a prosthesis").

- **BHTF upgraded to the LLM EXERCISE beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added the
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini) and `dig_deeper` follow-up. Narration expanded to include
  the "Go deeper: …" line. `beat_id` preserved per the preserve-IDs rule.
  Shot (`ClaudeComposerAsk`) preserved; `folderLabel` updated to
  `@NikBearBrown` and `runningText` broadened to
  `paste this into Claude, ChatGPT, or Gemini…`. `command` prop rewritten to
  match the new prompt. `estimated_duration_s` bumped 19 → 42.

- **BOUT retargeted to the NikBearBrown channel.** Remotion pattern switched
  from `OutroSeries` (with eyebrow + line) to `OutroCTA` (with line + handle),
  matching the other nbb reels in this book. `handle` set to `@NikBearBrown`.
  Narration line lengthened from "The CRA Ladder. Liam, in for Bear." to
  include the CRA expansion ("Concrete, Representational, Abstract, one
  lesson") so the outro line stands on its own without the eyebrow.
  `estimated_duration_s` bumped 6 → 7.

- **Metadata `_variant_todo` removed** (checklist complete). `channel_title`
  and `folderLabel` at the sheet level flipped to `@NikBearBrown` for
  consistency with the outro handle.

- **`purpose` rewritten** in the Teardown register (was "in the Plain
  register" — now names the trade-off: "the tool has to watch the climb, not
  just the arrival").

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source already has `BHTF` at second-to-last position performing the
   handoff. Followed the sibling nbb reels' precedent: kept `BHTF` as the
   beat_id, adopted the `LLM EXERCISE` act name and the `llm_exercise`
   structured field. No new beat inserted; no reorder.

2. **BOUT pattern OutroSeries → OutroCTA.** SKILL says either is fine
   (Remotion `OutroSeries` / `OutroCTA` in the teardown palette). Switched to
   OutroCTA to match the other nbb reels in this book (nbb-books--claude-liam-*)
   — they all end on `OutroCTA` with a `handle` prop. Consistency wins.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per the
   shot-blocks preserve rule. Its `bg: #F3EBDD` and `accent: #E4572E` are
   humanitarians-palette colors, but this is a locked visual element (the
   hesitant-writer typing animation) and the on-screen text ("When I tier one
   lesson for three levels, do I run it separate?") is the ask being
   corrected — cannot be re-voiced without breaking the correction. New
   narration is 37 words — within the 20–35 window the note describes
   (source was 32; ran two words over on the tightening).

4. **`style_preset: humanitarians` and `ground: #F3EBDD` left as scaffold
   wrote them.** Not re-scaffolding was an explicit instruction; `palette`
   is now `teardown` and downstream compile reads that field. The residual
   humanitarians hints only affect the frozen B00 shot props, which stay.

5. **BCRY narration + WantQuote copy left unchanged.** The carry-out already
   fits the Teardown register (names the design contrast explicitly: "not
   three separate lessons — one shared target with three rungs"). Editing it
   would break the anchor with the sparkLine and force a re-write of the
   card copy for no register gain.

6. **`playlist: Claude Basics` preserved from source.** The series identity
   travels with the K-12 teacher-skills book, not with the audience cut.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
