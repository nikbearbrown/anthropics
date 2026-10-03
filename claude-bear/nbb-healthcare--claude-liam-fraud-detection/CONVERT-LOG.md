# CONVERT-LOG — healthcare--claude-liam-fraud-detection → nbb

Converted `beat_sheet.json` (Plain register, hai-simple) into
`beat_sheet.nbb.json` (Teardown register, NikBearBrown audience). Source is
unmodified.

## What changed

- **All 5 body narrations rewritten in Teardown register** (Feynman × MKBHD):
  explain the machinery, name the design choice, judge the trade-off. Facts
  unchanged — the eight files in the fraud-detection folder, the ranked-and-
  cited output shape (NPI, suspected scheme, dollar exposure, confidence
  score), the SIU / program-integrity team consumer, and the same-input /
  same-output determinism all survive verbatim.
- **B00 cold open** — reframed as "here's the wrong verb — thinking Claude
  convicts a Medicare claim of fraud," which lines up with the
  BrutalistHesitantWriter's on-screen `convict` → `flag` correction. `text`,
  `triggerWords`, `replacementWords`, and every timing prop kept exactly.
  New narration = 33 words at ~2.72 wps → ~12s + 1.0s lead silence, holds the
  TIMING LAW ≥9s typing window (source was 29 words / 10.65s actual).
- **NB01 / NB02 / NB03 mechanism beats** rewritten to explain the actual
  machinery (folder-as-program, one relayed output shape, deterministic
  screen) and judge the design choice ("the design bet is legibility",
  "they optimized for one output at the cost of exploratory tools",
  "pattern-matching at machine speed; judgment kept human"). `estimated_
  duration_s` bumped modestly (22→25, 18→22, 24→26) to match the slightly
  longer word counts.
- **BCRY carry-out narration kept verbatim.** `gate_c` is SIGNED —
  CARRY-OUT.md and the sentence is also the on-screen quote copy in
  WantQuote; Teardown-ifying it would fight both the gate and the visual.
  The sentence is already a clean judgment framed as a trade-off, which is
  exactly what Teardown wants a carry-out to be.
- **BHTF upgraded to the LLM EXERCISE beat (SECOND-TO-LAST)** per SKILL.md
  §Step 3, following the books--claude-liam-legal-finance sibling pattern:
  - `act` changed from "your turn handoff" → `"LLM EXERCISE"`.
  - Added `llm_exercise` block: `prompt` is the paste-ready block (four
    numbered asks that produce useful output on their own, without the
    video); `dig_deeper` is a real next question about the pipeline's
    systematic blind spots — not a summary.
  - Narration reads the prompt in full, appends "Go deeper: …", and signs
    off with "Liam, in for Bear." (IN-FOR-BEAR LAW).
  - `estimated_duration_s` 21 → 45 to account for the extended narration
    (paste-ready prompt + Go deeper + sign-off, ~140 words).
  - `ClaudeComposerAsk` props kept intact; `command` rewritten to match
    `llm_exercise.prompt` verbatim so the on-screen paste-ready command and
    the spoken prompt read as one.
- **`_variant_todo` removed** — checklist complete.
- **Metadata `purpose` rewritten in Teardown register** — it's authored
  prose describing the reel's intent, so it moves with the voice. Every
  other metadata string is machine-readable state and stays as-is.

## Preserved exactly

- Every `beat_id` (B00, NB01, NB02, NB03, BCRY, BHTF, BOUT), every `shot`
  block, every `graphic.production_viz` structure (labels, chips, colors,
  captions, accent indices), every Manim scene name (BKNB01Scene,
  BKNB02Scene, BKNB03Scene), every Remotion pattern (BrutalistHesitantWriter,
  WantQuote, ClaudeComposerAsk, OutroSeries), all on-screen card copy (the
  BrutalistHesitantWriter text, the WantQuote quote + sparkLine, the OutroSeries
  eyebrow + line).
- Scaffold-set metadata (`audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `typography`, `outro_source`, `derived_from`) — untouched.
- Original HAI channel state kept intact per book precedent: `folderLabel`
  and `channel_title` = `@HumanitariansAI`, `style_preset: humanitarians`,
  `ground: #F3EBDD`, `playlist: Claude Basics`, `in_for_bear: true`,
  `anchor_pair`, `one_flag`, `gate_c`, `gate_h`, `mode`, `source_sheet`,
  `build`.

## Judgement calls

1. **Kept `folderLabel: @HumanitariansAI`** on BHTF and OutroSeries eyebrow
   `FRAUD-DETECTION · @HumanitariansAI` even though SKILL.md §"Ask/intro
   scene rule" mentions `@NikBearBrown` for claude-brand NBB reels. Every
   completed sibling nbb- sheet in this book (books--claude-liam-legal-finance
   verified) keeps `@HumanitariansAI` — channel identity stays HAI for
   Liam-in-for-Bear reels; only the register moves to Teardown. Following
   precedent over the SKILL.md line rather than diverging silently.
2. **BCRY narration kept verbatim.** Gate-signed carry-out that is also
   on-screen WantQuote copy. Same call as the sibling.
3. **BHTF beat_id kept as `BHTF`** (not renamed to `B_LLM` per the SKILL.md
   example schema). Following sibling precedent — renames would break the
   `mp3/beat-BHTF.mp3` and `media/BHTF.mp4` path conventions on the rebuild
   without meaningful benefit. `act` moves to `"LLM EXERCISE"` to satisfy
   the spec's semantic intent.
4. **BHTF shot pattern kept as `ClaudeComposerAsk`** rather than switching
   to the SKILL.md example schema's `{type: CARD, source: own, motion:
   hold}`. ClaudeComposerAsk IS the canonical paste-into-Claude visual
   (per the Ask/intro scene rule 2026-07) and already renders the prompt
   as a paste-ready block. Sibling reel does the same.
5. **BOUT `OutroSeries` retained** (not switched to `OutroCTA` as the
   sibling did). This reel's source uses `OutroSeries` with `eyebrow` +
   `line` props, which is a valid outro pattern; switching without knowing
   the OutroCTA props for this exact eyebrow line risks a silent render
   drift. The source outro copy is already Teardown-clean and satisfies the
   IN-FOR-BEAR LAW sign-off ("Liam, in for Bear.").
6. **`_variant_todo` deleted rather than emptied** — supervisor check
   treats its absence as done.

## Ending order verified

```
B00 → NB01 → NB02 → NB03 → BCRY
BHTF (LLM EXERCISE — paste-ready prompt + Go deeper + Liam sign-off)  ← second-to-last
BOUT (OutroSeries — "It Flags and Ranks. It Never Convicts. Liam, in for Bear.")  ← last
```

7 beats total (unchanged from source).
