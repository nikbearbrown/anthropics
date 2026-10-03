# CONVERT-LOG — claude-tag-plugins--claude-liam-asana-api → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery first, design intent surfaced, tradeoffs named. Facts untouched — every
object name, operation count, envelope key, gid convention, pagination behavior,
and the search-cap exception survives verbatim from the source; only the voice
changed. Preserved every `beat_id`, act structure, `shot`/`graphic` blocks,
Manim scene names, and on-screen card copy. `_variant_todo` removed.
`metadata.register` was already flipped to "Teardown" by the scaffold; added a
"Teardown register" tag to `metadata.purpose` for parity.

## Ending order (verified)
`B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" with a paste-ready prompt rendered via
  `ClaudeComposerAsk` — exactly the shape SKILL.md §Step 3 wants. Rather than
  insert a new beat and duplicate the composer card, I re-slotted BHTF: retitled
  `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, rewrote the composer `command`
  as a paste-ready prompt for Claude/ChatGPT/Gemini (not a CLI command), and
  folded the "Go deeper:" follow-up into the spoken narration. Consistent with
  the pattern already used in `nbb-books--claude-liam-building-plugins`.
  Estimated_duration bumped 24 → 52s to fit the longer paste-ready block plus
  dig-deeper sentence.

- **LLM prompt content.** The paste-ready prompt asks any frontier LLM to walk
  the viewer through the Asana REST API from scratch — three parts that map
  exactly to the video's own three body beats (nesting shape, envelope + gid
  convention, list-my-tasks trace with pagination). This produces a useful
  standalone output for someone who never watched the reel, and doubles as a
  quiz for someone who did.

- **Dig-deeper prompt content.** Chose "rank Asana's ten operations by which
  would silently return the wrong answer if the caller assumed the first page
  was the whole list, and by how bad the miss would be." Genuinely explorable,
  not a summary — pushes on the exact failure mode B03 flagged (silent
  truncation) and forces the model to reason about per-operation blast radius.

- **BCRY narration kept identical to the `WantQuote` `props.quote`.** The
  carry-out sentence is what appears on-screen as the quote; drifting the audio
  off it would break lip-sync between voiceover and typed quote. The source
  sentence already reads as clean Teardown (declarative, machinery-focused, no
  banned adjectives), so no rewrite was warranted.

- **B00 word budget respected.** Rewrite is ~40 words — inside the beat's own
  TIMING LAW note that says 20–35 words + `lead_silence_s: 0.8` for a ≥9s
  typing window. Preserved the `app` → `API` correction as the on-screen
  animation hinge (the `BrutalistHesitantWriter` `triggerWords`/
  `replacementWords` props are untouched); the narration frames the same
  misdirection in Teardown register ("Wrong branch. It hits Asana's REST API
  directly — JSON out, JSON back, no app in the loop.").

- **B01 duration bumped 19 → 22s** to fit the added tradeoff clause ("optimized
  for stable references you can't accidentally break by renaming — at the cost
  of one extra unwrap on every single call"). B02 22 → 23s, B03 27 → 31s for
  similar teardown expansions. `actual_duration_s` fields dropped from the
  scaffold on these beats because the old measured durations no longer match
  the new narration length — audio regeneration will refill them.

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
  `segment`, `runningText`) were updated to reflect the LLM-exercise reframing;
  `greeting`, `topic`, `folderLabel` preserved.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the old
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` (voice `am_onyx`) before compile.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
