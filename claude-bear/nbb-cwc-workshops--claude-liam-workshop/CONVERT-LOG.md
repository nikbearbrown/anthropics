# CONVERT-LOG — cwc-workshops--claude-liam-workshop → nbb

**Date:** 2026-09-03
**Source:** `../cwc-workshops--claude-liam-workshop/beat_sheet.json`
**Output:** `beat_sheet.nbb.json`
**Voice:** Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW). No paid engine.

## What changed

- **Every `narration_text` rewritten** in the Teardown register (Feynman × MKBHD).
  Named the machinery ("Here's the machinery…"), the design choice ("They
  optimized for learning, not shipping"), and the trade-off ("at the expense of
  speed"). Facts unchanged — every count (seven acts, two modes, one file),
  every rule (no reading solutions or git history), and the five-part
  explanation shape (what changed / why it works / platform idea / where to see
  it / one thing to try) survive verbatim from the source.
- **B_LLM added as the second-to-last beat** with a paste-ready prompt keyed to
  the video's thesis: does a well-designed coaching script produce
  understanding, or only successful repetition? Prompt uses database indexes as
  the worked example (an approachable domain that the script/understanding
  split can be run on by any viewer). `dig_deeper` asks for a follow-up
  question a repeater couldn't answer.
- **BOUT retooled for NikBearBrown:** `eyebrow` swapped from
  `WORKSHOP · @HumanitariansAI` → `WORKSHOP · @NikBearBrown`; narration adds
  the default channel per SKILL.md ("brutalist dot art"). `line` and pattern
  (`OutroSeries`) preserved. `estimated_duration_s` nudged 6→7 for the extra
  channel line.
- **`_variant_todo` removed** from metadata (all four items completed).

## Preserved verbatim

- Every `beat_id`, every `act`, every `shot`/`remotion`/`graphic` block, every
  card-copy field (`text`, `label`, `chips`, `caption`, `quote`, `command`,
  `sparkLine`), every color hex, every `folderLabel`/`greeting`/`runningText`,
  `lead_silence_s` / `tail_silence_s`, and the B00 `note` (WRITER/TIMING LAW).
- BCRY narration matches its on-screen `WantQuote` verbatim — the source
  quote already sits in the Teardown register (names the mechanism and the
  ceiling in two sentences), so retouching it would drift the card from the
  narration for no register gain.
- BHTF narration = source card `command` verbatim — the source paste-prompt
  already runs the "understood vs. repeated" verdict move that is Teardown's
  bread and butter; rewriting it would just diverge card copy from narration.
  The narration's single word-choice sharpen ("understood the mechanism, or
  just that I could repeat the script" vs. source's "repeat you") lives in
  narration only, so the card copy is untouched.

## Judgement calls

- **Palette hex left as humanitarians (`#F3EBDD` / `#2F2A26` / `#E4572E`) in
  shot/graphic props.** Orders said "preserve exactly: shot blocks." Metadata
  already flips `palette` to `teardown`; the renderer decides how those
  literal hex values are interpreted (or if the palette metadata overrides
  them). If a later pass wants the cards physically retinted to teardown
  (`#FFFFFF` / `#2A1A0E` / `#C8102E`), that is a separate mechanical swap
  across `production_viz.colors[]`, `props.bg`, `props.ink`, `props.accent`.
- **BHTF kept in place, B_LLM inserted after it** rather than merging the two.
  BHTF is a Your-Turn handoff pointed at the video's specific worked example
  (off-by-one fix). B_LLM is the SKILL.md-required LLM exercise with structured
  `llm_exercise` object and a broader test — leaving both preserves the
  Your-Turn beat and adds the required schema-conformant beat second-to-last.
- **BOUT narration adds "brutalist dot art"** rather than only swapping the
  eyebrow. The SKILL calls out `www.brutalist.art` as the default channel; a
  one-word update to the on-camera eyebrow without any narration reference
  would leave the channel invisible to audio-only viewers. Kept it short (16
  words, ~7s window with `tail_silence_s: 1.0`).

## Not done (out of scope for this pass)

- No audio generation, no Manim/Remotion render, no compile. Per orders, the
  deliverable is `beat_sheet.nbb.json` only.
