# CONVERT-LOG — claude-tag-plugins--claude-liam-snowflake-api → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery first, design intent surfaced, tradeoffs named. Facts untouched — every
object name, API behavior, statement handle semantics, terminal-state distinction,
partition-fetch requirement, and cancel affordance survives verbatim from the
source; only the voice changed. Preserved every `beat_id`, act structure,
`shot`/`graphic` blocks, Manim scene names (SFB01/SFB02/SFB03), and on-screen
card copy. `_variant_todo` removed. Added "Teardown register." tag to
`metadata.purpose` for parity with sibling nbb sheets.

## Ending order (verified)
`B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" rendered via `ClaudeComposerAsk` — exactly
  the shape SKILL.md §Step 3 wants. Following the sibling `nbb-claude-tag-
  plugins--claude-liam-asana-api` precedent I re-slotted BHTF rather than
  inserting a new composer beat: retitled `act` to `LLM EXERCISE`, added the
  structured `llm_exercise: { prompt, dig_deeper }` field, rewrote the composer
  `command` as a paste-ready prompt for Claude/ChatGPT/Gemini (not a CLI
  command), swapped `segment` from "Your Turn" to "Paste this into Claude", and
  folded the "Go deeper:" follow-up into the spoken narration. Estimated_duration
  bumped 25 → 50s to fit the longer paste-ready block plus dig-deeper sentence.

- **LLM prompt content.** Three-part prompt that maps exactly to the video's
  three body beats — compute/storage separation (B02), submit-returns-handle
  design (B01), and the full call sequence with polling + terminal-state check +
  partition fetch (B03). Produces a useful standalone walk-through for a viewer
  who never watched the reel; doubles as a quiz for one who did.

- **Dig-deeper prompt content.** Chose "which failure mode costs a real team
  more: treating FINISHED as proof of success when the same field can read
  FAILED, or fetching only the first partition and calling it the whole
  answer." Real next question, not a summary — pushes on the two silent-wrong
  failure modes B03 flagged and forces the model to reason about blast radius.
  Deliberately leaves out the third failure (submitting without a warehouse)
  because that one errors loudly and doesn't fit the "silent wrong" category.

- **BCRY narration kept identical to the `WantQuote` `props.quote`.** The
  carry-out sentence is what appears on-screen as the quote; drifting the
  voiceover off it would break sync between narration and typed quote. The
  source sentence already reads as clean Teardown (declarative, machinery-
  focused: "treat the submit call as a receipt, not an answer", "stops meaning
  anything it doesn't") with no banned adjectives, so no rewrite was warranted.
  Same call the Asana sibling made.

- **B00 word budget respected.** Rewrite is ~37 words — right at the top of the
  beat's own TIMING LAW note (20–35 words + `lead_silence_s: 0.8` for a ≥9s
  typing window). Preserved the `answer` → `handle` correction as the
  on-screen animation hinge (the `BrutalistHesitantWriter` `triggerWords`/
  `replacementWords` props are untouched); the narration frames the same
  misdirection in Teardown register ("Wrong branch. Submit returns only a
  statement handle — a pointer to check later, not the rows.").

- **B01 duration bumped 23 → 30s** to fit the added tradeoff clause ("optimized
  for asynchronous compute where a query might run for minutes, at the expense
  of the obvious contract"). B02 25 → 33s and B03 36 → 42s for similar teardown
  expansions that name what the design choice bought and what it cost. All
  `actual_duration_s` fields dropped from every beat because the old measured
  durations no longer match the new narration length — audio regeneration will
  refill them.

- **B03 tradeoff framing.** Landed the design-judgment sentence pair explicitly:
  "What the decoupling buys: long queries that don't hold a connection open.
  What it costs you: three habits you can never skip — check status, don't
  trust FINISHED alone, fetch every partition." This is the MKBHD lens — name
  what was optimized for and what was sacrificed. The three-habit list mirrors
  the source's own summary but reframes it as the cost side of a trade.

- **Outro left as `OutroCTA` with `@HumanitariansAI` handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Consistent with every sibling
  `nbb-claude-tag-plugins--*` and `nbb-books--claude-liam-*` sheet in this
  tree, which all preserve the HAI handle because the reel is inside the HAI
  `Claude Basics` playlist per `metadata.playlist`. IN-FOR-BEAR LAW is
  satisfied by the "Liam, in for Bear" sign-off already in the source line,
  which is clean Teardown as-is (title callback + Liam disclosure), so it was
  not rewritten.

- **Ask-scene composition unchanged.** BHTF still uses `ClaudeComposerAsk` per
  the SKILL.md 2026-07 ask/intro-scene rule. Only the props (`command`,
  `segment`, `runningText`) were updated to reflect the LLM-exercise
  reframing; `greeting`, `topic`, `folderLabel` preserved.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the old
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` (voice `am_onyx`) before compile.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
