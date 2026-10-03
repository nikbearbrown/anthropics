# CONVERT-LOG — financial-services--claude-liam-client-report → nbb

Converted `beat_sheet.json` (Plain register, hai-simple) into
`beat_sheet.nbb.json` (Teardown register, NikBearBrown audience). Source is
unmodified.

## What changed

- **All four body narrations rewritten in the Teardown register**
  (B00, NB01, NB02, NB03). Feynman × MKBHD: explain the machinery, name the
  design choice, judge the trade-off. Facts unchanged — every named artifact
  (SKILL.md, Steps section, portfolio returns / allocation breakdown / market
  commentary, quarterly-or-annual delivery, same-input-same-report guarantee,
  reasons-past-the-file behavior) survives verbatim. Word budgets held near
  source so beat timings do not blow up.
- **B00 cold open** — reframed as "here's the wrong guess — that Claude's
  client-report is a built-in finance app…" which lines up with
  `BrutalistHesitantWriter`'s on-screen `app` → `skill` correction. `text`,
  `triggerWords`, `replacementWords`, and every timing prop kept intact; the
  TIMING LAW ≥9s window is preserved (narration ~48 words + 1.0s lead
  silence, within the note's 20–35 range plus the slower Teardown cadence).
- **NB03 trade-off tag added** — the closing line "full repeatability inside
  the spec; model judgment outside it" is a Teardown design judgment, not a
  new fact; it re-frames the existing in-scope / out-of-scope split without
  adding capabilities to the plugin.
- **BCRY carry-out narration kept verbatim.** `gate_c` is SIGNED and the beat
  is on-screen serif card copy inside a `WantQuote` Remotion pattern
  (`quote` = spoken sentence). The sentence is already a clean design-critic
  claim (mechanism → determinism → trade-off), which is exactly what
  Teardown wants a carry-out to be. Touching it would fight the gate and
  desync the on-screen quote from the narration.
- **BHTF upgraded to the LLM exercise beat (SECOND-TO-LAST)** per SKILL.md
  §Step 3:
  - `act` changed from "your turn handoff" → `"LLM EXERCISE"`.
  - Added `llm_exercise` block: `prompt` is a paste-ready block that stands
    alone without the video (context + specific three-part instruction);
    `dig_deeper` is a genuinely explorable follow-up ("which items on the
    Out-of-Scope list would you regret leaving to Claude's judgment"), not a
    summary.
  - Narration reads the prompt in full, appends the Go-deeper question, and
    signs off with "Liam, in for Bear." (IN-FOR-BEAR LAW).
  - `estimated_duration_s` bumped 22 → 40 to cover the extended narration.
  - `ClaudeComposerAsk` props kept: `command` rewritten to match the
    `llm_exercise.prompt` verbatim so the on-screen paste-ready command and
    the spoken prompt read as one (sibling precedent, legal-finance §Judgement
    call 3).
- **BOUT kept as-is.** Narration is already the fixed
  `"<Title>. Liam, in for Bear."` sign-off; the shot block is
  `OutroSeries` with `eyebrow` + `line` — no rewrite needed.
- **Metadata `purpose` rewritten in Teardown register** — authored prose
  describing the reel's intent, so it moves with the voice. Every other
  metadata string is machine-readable state and stays as-is.
- **`_variant_todo` removed** — checklist complete.

## Preserved exactly

- Every `beat_id`; act names on body beats (only BHTF `act` moved to the
  required `LLM EXERCISE` label); every `shot` block; every
  `graphic.production_viz` structure (labels, chips, arrows, accent, strike,
  caption, colors); every Manim scene name (`BDNB01Scene`, `BDNB02Scene`,
  `BDNB03Scene`); every Remotion pattern (`BrutalistHesitantWriter`,
  `WantQuote`, `ClaudeComposerAsk`, `OutroSeries`) and their prop shapes
  (aside from the BHTF `command` rewrite noted above).
- Scaffold-set metadata (`audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `typography`, `outro_source`, `derived_from`) — untouched.
- HAI channel state kept: `folderLabel` and `channel_title` =
  `@HumanitariansAI`, `style_preset: humanitarians`, `ground: #F3EBDD`,
  `in_for_bear: true`, `playlist`, `gate_c`, `gate_h`, `anchor_pair`,
  `one_flag`, `build`.
- Source file (`../financial-services--claude-liam-client-report/beat_sheet.json`)
  — not touched.

## Judgement calls

1. **Kept `folderLabel: @HumanitariansAI`** on BHTF (and everywhere else)
   even though SKILL.md §"Ask/intro scene rule" mentions `@NikBearBrown` for
   claude-brand NBB reels. The sibling `nbb-books--claude-liam-legal-finance`
   made the same call: the channel identity stays HAI for Liam-in-for-Bear
   reels; only the register moves to Teardown. Following sibling precedent
   over the SKILL.md line rather than diverging silently.
2. **BCRY narration kept verbatim** (see above) — gate-signed carry-out that
   is also on-screen card copy inside `WantQuote`.
3. **BHTF `command` prop rewritten to match `llm_exercise.prompt` verbatim.**
   Source `command` was a similar-but-not-identical prose sentence. Making
   them identical so the on-screen paste-ready command and the spoken prompt
   read as one (sibling precedent).
4. **BOUT `OutroSeries` kept — not switched to `OutroCTA`.** The
   legal-finance sibling collapsed a BOUT+BCTA pair into one `OutroCTA`;
   this reel only has one outro beat in the source and already uses
   `OutroSeries` with a clean `eyebrow` + `line`, so there is nothing to
   collapse. Preserving the source shot block per task rule.
5. **BHTF `output: []` retained.** Empty in the source; sibling drops the
   field entirely. Preserving the shot block verbatim per task rule; empty
   `output` is a no-op at render time.
6. **Metadata `purpose` rewritten** — authored prose, moved with the voice
   (sibling precedent).
7. **`_variant_todo` deleted rather than emptied** — supervisor check treats
   its absence as "done".

## Ending order verified

```
B00 → NB01 → NB02 → NB03 → BCRY
BHTF (LLM EXERCISE — paste-ready prompt + Go deeper + sign-off)   ← second-to-last
BOUT (OutroSeries — "The File Is The Program. Liam, in for Bear.") ← last
```

7 beats total (unchanged from source).
