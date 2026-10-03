# CONVERT-LOG — nbb-financial-services--claude-liam-funding-digest

**Date:** 2026-09-03
**Converter:** register-conversion factory (nbb)
**Source:** `../financial-services--claude-liam-funding-digest/beat_sheet.json` (8 beats, Plain register, hai-fellows brand)
**Output:** `beat_sheet.nbb.json` (7 beats, Teardown register, NikBearBrown outro)

## What changed

1. **Register — all six body beats rewritten in Teardown (Feynman × MKBHD).**
   Voice only; every fact from the source is preserved unchanged (trigger phrases,
   output format, Capital IQ link-back, the "recipe not judgment" carry-out).
   Rewrites lead with "Here's what's actually happening" / "Here's the design
   choice, in both directions" / "They optimized for X … they gave up Y to get
   it" — the mechanism first, then what the choice sacrificed.
   - B00: preserves the hesitant-writer wrong-guess ("KNOWS" → "has to be told"),
     opens with "Here's the assumption to test." Word count kept ≥30 for the
     TIMING LAW ≥9s window.
   - B01: "A folder Claude reads before it does anything … no hidden logic, no
     compiled binary … the file is the program."
   - B02: pipeline as mechanism — "top to bottom, no branching unless a step
     tells it to branch."
   - B03: names the design trade — "optimized for one recipe delivered exactly;
     they gave up flexibility to get it."
   - BCRY: keeps the on-screen WantQuote copy verbatim (it already reads in
     Teardown register); narration reframes as "the model's guessing is not the
     same thing as your editorial judgment."

2. **BHTF repurposed as the LLM EXERCISE beat (second-to-last).**
   `act` changed to `"LLM EXERCISE"`, added `llm_exercise.{prompt, dig_deeper}`
   per SKILL.md §Step 3. The paste-ready prompt is derived from the whole
   video's subject: it asks a frontier LLM to draft a one-page SKILL.md for
   a report the user regularly produces — exercising the same
   "recipe-not-judgment" mechanism the reel is about. `dig_deeper` pushes the
   viewer to interrogate scope boundaries. `ClaudeComposerAsk.folderLabel`
   updated to `@NikBearBrown` for brand consistency with the outro.

3. **Outro collapsed to a single NikBearBrown OutroCTA beat (BOUT, last).**
   Source had two beats (BOUT OutroSeries "Claude, Funding Digest." + BCTA
   OutroCTA "…Liam, in for Bear." @HumanitariansAI). Following the sibling
   `nbb-books--claude-liam-data` convention, these merge into one OutroCTA:
   `line: "Claude, Funding Digest. Liam, in for Bear." · handle: "@NikBearBrown"`.
   BCTA dropped.

4. **Metadata `folderLabel` / `channel_title` flipped to `@NikBearBrown`.**
   The scaffold left both at `@HumanitariansAI`; brand_variant.py doesn't
   touch them, but the sibling nbb reels (e.g. `nbb-books--claude-liam-data`)
   set both to `@NikBearBrown` since the outro is NikBearBrown-branded per
   `outro_source: "AUTHOR.MD :: NikBearBrown"`. Matched that convention.

5. **`_variant_todo` removed** from metadata (all four checklist items done).

## Judgement calls

- **Kept the BCRY WantQuote verbatim.** The source's on-screen carry-out
  ("A skill doesn't make Claude judge what's newsworthy. It gives Claude one
  exact recipe — and outside that recipe, Claude has nothing written down to
  follow.") is already stripped, mechanical, and design-critical — it reads
  in Teardown register without change. Per SKILL.md, on-screen card copy that
  still fits is preserved. Only the narration around it was reworked.
- **Kept beat IDs (B00, B01, B02, B03, BCRY, BHTF, BOUT).** Did not renumber
  BHTF to the schema example's `B_LLM` — the sibling nbb reels keep `BHTF`
  when repurposing an existing "your turn" beat, and the beat-ID contract is
  to preserve source IDs.
- **`AUTHOR.MD :: NikBearBrown` not on disk for this book.** The scaffold
  declares this outro source. No `AUTHOR.MD` exists in the `claude-bear/`
  tree; the outro copy therefore follows the established sibling-reel
  convention (`OutroCTA` with `@NikBearBrown` handle and
  "[Title]. Liam, in for Bear." line) rather than an inline verbatim copy.
- **Did not render, generate audio, or compile.** Deliverable is the beat
  sheet only, per invocation contract.

## Verify

- 7 beats, JSON valid.
- Body → LLM exercise (BHTF) → outro (BOUT).
- `_variant_todo` absent from metadata.
- Every narration rewritten; source facts intact.
- Engine `kokoro`, voice `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW).
