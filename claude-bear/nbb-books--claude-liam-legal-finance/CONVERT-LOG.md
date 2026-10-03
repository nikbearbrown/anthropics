# CONVERT-LOG — books--claude-liam-legal-finance → nbb

Converted `beat_sheet.json` (Plain register, hai-fellows) into
`beat_sheet.nbb.json` (Teardown register, NikBearBrown audience). Source is
unmodified.

## What changed

- **All 32 body narrations rewritten in Teardown register** (Feynman × MKBHD):
  explain the machinery, name the design choice, judge the trade-off. Facts
  unchanged — every number, name, mechanism, four-hard-limits shape, worked
  example, and the anchor-payoff pair (B01↔B24) survive. Word budgets held to
  the same rough shape per beat so beat timings don't blow up.
- **B00 cold open** — reframed as "here's the wrong guess — thinking Claude
  does your legal and financial work for you," which lines up with the
  BrutalistHesitantWriter's on-screen `DO`→`screen` correction. `text`,
  `triggerWords`, `replacementWords`, and all timing props kept intact; the
  TIMING LAW ≥9s window is preserved (narration now ~50 words + 0.8s lead
  silence).
- **BCRY carry-out narration kept verbatim.** `gate_c` is SIGNED and the beat
  is on-screen serif card copy ("THE CARRY-OUT — one sentence, alone"); the
  Teardown register accommodates the existing sentence as-is, so touching it
  would fight the gate.
- **BHTF upgraded to the LLM exercise beat (SECOND-TO-LAST)** per SKILL.md
  §Step 3:
  - `act` changed from "your turn handoff" → `"LLM EXERCISE"`.
  - Added `llm_exercise` block: `prompt` is the paste-ready block (works
    without the video); `dig_deeper` is a real next question, not a summary.
  - Narration reads the prompt in full, appends the "Go deeper: …" question,
    and signs off with "Liam, in for Bear." (IN-FOR-BEAR LAW).
  - `estimated_duration_s` bumped 30 → 40 to account for the extended
    narration (added Go deeper + sign-off).
  - `ClaudeComposerAsk` props kept: `topic` refreshed to the metadata topic
    string; `segment` set to the reel title; `command` matches the
    `llm_exercise.prompt` verbatim so the on-screen paste-ready command and
    the spoken prompt read the same.
- **BOUT + BCTA collapsed into a single BOUT `OutroCTA`** — matches the
  precedent set by every other completed nbb- sheet in this book
  (installing-plugins, building-plugins). `line` reads
  "Claude, Counsel — legal and finance plugins. Liam, in for Bear.";
  `handle: @HumanitariansAI`; `tail_silence_s: 1.0` preserved.
- **`_variant_todo` removed** — checklist complete.

## Preserved exactly

- Every remaining `beat_id`, all act names on body beats, all `shot` blocks,
  all `graphic.production_viz` structures (labels, mechanics, colors), all
  Manim scene names, all Remotion patterns (aside from the BOUT/BCTA merge),
  and all on-screen card copy (chip labels, act headers, THE CARRY-OUT line,
  THE ANCHOR PLANTED / THE ANCHOR RETURNS labels). Only the spoken content
  was re-voiced.
- Scaffold-set metadata (`audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `typography`, `outro_source`, `derived_from`) — untouched.
- Original HAI channel state kept intact per book precedent: `folderLabel`
  and `channel_title` = `@HumanitariansAI`, `style_preset: humanitarians`,
  `ground: #F3EBDD`, `in_for_bear: true`, `bookend_exempt`, `anchor_pair`,
  `mirror_pair`, `one_flag`, `gate_c`, `gate_h`, `redo_of`, `build`.

## Judgement calls

1. **Kept `folderLabel: @HumanitariansAI`** on BHTF and `handle` on BOUT even
   though SKILL.md §"Ask/intro scene rule" mentions `@NikBearBrown` for
   claude-brand NBB reels. Every completed sibling nbb- sheet in this book
   keeps `@HumanitariansAI` — the channel identity stays HAI for Liam-in-for-
   Bear reels; only the register moves to Teardown. Following precedent over
   the SKILL.md line rather than diverging silently.
2. **BCRY narration kept verbatim.** Gate-signed carry-out that is also
   on-screen card copy; Teardown-ifying it would fight both the gate and the
   visual. Register test passes as-is (the sentence is a clean judgment
   framed as trade-off, which is exactly what Teardown wants a carry-out to
   be).
3. **BHTF `command` prop rewritten to match the new `llm_exercise.prompt`
   verbatim.** The source `command` had prose ("tell me…", "show me…", "for
   each, name…") that overlapped with but didn't precisely mirror the
   narration. Making them identical so the on-screen paste-ready command and
   the spoken prompt read as one.
4. **BOUT `line` stays literal.** Not prose to Teardown-ify; a sign-off in
   the fixed "Title — subtitle. Liam, in for Bear." form used by every
   sibling.
5. **Metadata `purpose` rewritten in Teardown register** — it's authored
   prose describing the reel's intent, so it moves with the voice. Every
   other metadata string is machine-readable state and stays as-is.
6. **`_variant_todo` deleted rather than emptied** — the supervisor check
   treats its absence as done.

## Ending order verified

```
… B00 → C01..B04 → C02..B09 → C03..B13 → C04..B18 → C05..B21 → C06..B24 → BCRY
BHTF (LLM EXERCISE — paste-ready prompt + Go deeper)     ← second-to-last
BOUT (OutroCTA — "Claude, Counsel — … Liam, in for Bear.") ← last
```

34 beats total (was 35; BCTA merged into BOUT).
