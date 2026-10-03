# CONVERT-LOG — financial-services--claude-liam-macro-rates-monitor → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-macro-rates-monitor/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every body-beat `narration_text` rewritten in the Teardown register**
  (Feynman × MKBHD). Every number, name, file path, and factual claim from the
  source survives unchanged: four named inputs (macro indicators, yield curve,
  inflation breakevens, swap rates), real-vs-nominal decomposition of the
  yield, breakevens defined as the market's implied inflation number priced
  off nominal against inflation-protected yields, the central-bank-next-quarter
  question being "not one of the four things the file combines", the anchor
  (one market-data pull walking through four blocks in sequence to a finished
  dashboard), and the two-directions split (ran-correctly ≠ reads-reality;
  missing swap-rate data = data gap, not evidence the other three blocks are
  wrong). Voice-only edit throughout — revealed the actual machinery ("four
  blocks, wired in order… every block reads only from the definition the file
  hands it"), named the design choice ("they built it to be identical every
  run, at the cost of ever being clever" / "they optimized for reproducible
  combination; the price is any original forecast"), and drew the trade-off
  line ("ran-correctly and reads-reality are not the same claim").

- **B00 (BrutalistHesitantWriter) narration rewritten in Teardown voice
  and kept inside the 20-35-word TIMING LAW window.** New narration is 35
  words. `lead_silence_s: 0.8` preserved. IN-FOR-BEAR-LAW ("Liam, in for
  Bear") declared in the cold open. All Remotion props (`text`,
  `triggerWords`, `replacementWords`, palette hexes, seed) preserved
  verbatim per the shot-blocks preserve rule — the typing animation and
  its correction ('predict' → 'combine four indicators about') stay
  frozen.

- **BCRY (carry-out) narration preserved verbatim.** The on-screen
  `WantQuote` props render that exact sentence, and the source narration
  already lands the Teardown carry-out cleanly (mechanism / reality
  split). Rewriting the narration would have desynced it from the
  rendered quote for no register gain. Same call as the sibling
  `nbb-financial-services--claude-liam-deal-sourcing`.

- **BHTF upgraded to the LLM EXERCISE beat** (already at second-to-last
  position, so no reorder needed). `act` renamed `your turn handoff` →
  `LLM EXERCISE`. Added a structured `llm_exercise` object with `prompt`
  (paste-ready for Claude / ChatGPT / Gemini — self-contained: names the
  four inputs, defines breakevens inline, asks for each input's
  definition before combining, then splits the central-bank question into
  what-the-combination-can-vs-cannot-answer) and `dig_deeper` follow-up
  (which piece of the dashboard would move most if the market repriced
  the central bank's next move — "the seam where mechanical combination
  stops and forecasting judgment would have to begin"). Narration
  expanded to include the "Go deeper: …" line and the paste-ready
  language ("a prompt you can paste directly into Claude, ChatGPT, or
  Gemini"). `beat_id` preserved. Shot (`ClaudeComposerAsk`) preserved;
  `folderLabel` updated to `@NikBearBrown`, `runningText` broadened to
  `paste this into Claude, ChatGPT, or Gemini…`, and `command` rewritten
  to match the paste-ready `llm_exercise.prompt`.
  `estimated_duration_s` bumped 26 → 46 to accommodate the fuller prompt
  + dig-deeper appendage.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle
  changed `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props.
  Narration kept as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in
  for Bear") and re-reads the title.

- **Metadata `_variant_todo` removed** (checklist complete). Sheet-level
  `channel_title` and `folderLabel` flipped to `@NikBearBrown` for
  consistency with the outro handle. `purpose` rewritten to reflect the
  Teardown lens (opens with "Take the macro-rates-monitor skill apart",
  names the machinery in terms of blocks + fixed order + file-only
  definitions, and calls the design choice by name — reproducible
  mechanical combination at the expense of any original forecast).

- **`estimated_duration_s` on B00, B01, B02, B03, BCRY, BOUT preserved
  from the source** — these beats already have `actual_duration_s`
  measurements in the source sheet (the source is a fully built master).
  Only BHTF's estimate moved, because its content grew.

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL
   calls for a new beat with `beat_id: "B_LLM"` and `act: "LLM
   EXERCISE"`. The source sheet already had `BHTF` at second-to-last
   position doing the your-turn handoff. The preserve-beat-ids rule wins:
   kept `BHTF` as the beat_id, adopted the `LLM EXERCISE` act name and
   the structured `llm_exercise` field. No new beat inserted; no reorder.
   Matches the `nbb-financial-services--claude-liam-deal-sourcing`
   precedent exactly.

2. **Handle on BOUT.** Source used `@HumanitariansAI`. The NBB brand
   spec (`brands/nbb.md`, SKILL Step 4) makes the NikBearBrown identity
   the default channel for an NBB cut. Flipped to `@NikBearBrown` on the
   outro handle and on the sheet-level `channel_title` / `folderLabel`.
   `playlist: Claude Basics` kept — the series identity travels with the
   topic ("what does a Claude skill actually do?"), not the audience cut.

3. **BCRY narration kept verbatim to preserve the WantQuote sync.**
   Rewriting the audio to sound more Teardown would have desynced it
   from the on-screen card copy, which is explicitly a preserve-block
   under SKILL.md's Step 2. The existing sentence already names the
   mechanism-vs-reality split cleanly ("combined by one fixed, repeatable
   procedure. A finished dashboard means the combination ran correctly,
   not that reality will follow it") — that IS the Teardown carry-out,
   so nothing was gained by editing it.

4. **B00 word budget was tight (35 words, right at the ceiling).** The
   TIMING LAW note bounds cold-open narration to 20–35 words so the
   BrutalistHesitantWriter typing animation has a ≥9s window. Landing
   Teardown attack ("sounds like Claude forecasts where rates head
   next. It doesn't"), the machinery preview ("runs a fixed combination
   on four named inputs"), and IN-FOR-BEAR-LAW ("Liam, in for Bear —
   let's take the file apart") in 35 words was the ceiling. Kept it in
   spec; verified with a word count before writing.

5. **B01 uses "The natural reading of 'macro rates dashboard' is…"**
   The source opened "The natural guess is that asking Claude for a
   macro rates dashboard…". Reframed as reading the dashboard's name
   rather than making a guess, so the beat opens where design critique
   actually starts — with what the name promises vs what the file
   delivers. Fact content (four inputs, real/nominal split, central bank
   next quarter is off-spec) unchanged.

6. **Breakevens definition kept in narration on both B01 (short) and
   B02 (long).** The source had "inflation breakevens — the market's
   implied inflation expectation" only on B02. Teardown register asks
   for "strip jargon" — the reader hears "breakevens" three times across
   the video, so B02's fuller definition ("the market's own implied
   inflation number, priced off nominal against inflation-protected
   yields") repays that. The LLM-exercise prompt carries the same
   definition inline so the paste is self-contained.

7. **LLM exercise question is domain-honest, not domain-generic.** The
   `dig_deeper` line names the seam specific to this skill — which piece
   of the dashboard would move most if the central bank's next move were
   repriced — because that is the exact place where mechanical
   combination stops and forecasting judgment would have to begin. A
   generic "what did you learn?" would have fit any video; this fits the
   claim of the video.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
