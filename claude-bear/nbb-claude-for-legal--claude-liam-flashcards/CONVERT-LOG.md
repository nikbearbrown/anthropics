# CONVERT-LOG — nbb-claude-for-legal--claude-liam-flashcards

Converted `beat_sheet.json` → `beat_sheet.nbb.json` per `skills/make/nbb/SKILL.md`.
Voice/facts contract: every fact preserved; narration re-voiced only.

## Narration rewrites (all 11 beats)

Every `narration_text` rewritten in the Teardown register (Feynman × MKBHD):
mechanism first, name the trade-off, no "innovative"/"seems like"/"one could argue."

- **B00** cold open — the naming misdirection made explicit ("The name does a
  bit of misdirection… here's what's actually happening"). Kept inside the
  20–35 word / ≥8s timing law noted on the source beat.
- **B01** stakes — kept the intuitive-but-wrong framing; sharpened the closer
  ("That reading is intuitive. It's also wrong.").
- **B02** wrong guess — reframed as an experiment ("Test the intuition: delete
  the folder"), Feynman-style falsification.
- **B03** anchor planted — mechanism-first ("Here's the mechanism, stripped").
- **B04** mechanism — named the design choice out loud: "The execution model
  is deliberately dumb… trades cleverness for reproducibility."
- **B05** mechanism — added the trade-off summary MKBHD-style: "They
  optimized for structure at the expense of range."
- **B06** anchor payoff — "That's not learning. That's a specification being
  enforced — and it's the whole trick."
- **B07** both directions — kept the two-part symmetric fallacy; tightened.
- **BCRY** carry-out — "the structure is written down, not learned."
- **BHTF** repurposed (see below).
- **BOUT** outro (see below).

## Structural changes

- **BHTF was already the second-to-last "paste this into Claude" beat** with a
  `ClaudeComposerAsk` shot — the LLM-exercise slot in all but name. Judgement
  call: rather than insert a redundant new beat, **converted BHTF in place**
  into the proper LLM-exercise beat. Beat id `BHTF` preserved (per "preserve
  every beat_id"); `act` changed to `LLM EXERCISE`; added the required
  `llm_exercise: { prompt, dig_deeper }` block. Ending order verifies:
  `… BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`.
- **LLM prompt** is paste-ready for any frontier LLM (not a CLI command),
  self-contained (yields a real SKILL.md the viewer can use tomorrow without
  the video), and interactive by design — it asks the viewer three questions
  before writing, matching the video's own point that a skill is a
  specification, not a power.
- **`dig_deeper`** points at "where the specification really lives" — a real
  next question, not a summary.

## On-screen card copy

Left the `graphic.production_viz` labels/chips/captions **untouched** — they
already read as Teardown ("SPEC, NOT POWER", "NOTHING TO FORGET", "NEITHER ONE
IS PROOF") and preservation is required where the copy still fits the register.
Updated the `WantQuote` props on **BCRY** to match the new narration so the
on-screen quote and the audio line are the same sentence.

## Outro

Per `outro_source: "AUTHOR.MD :: NikBearBrown"` (set by the scaffold) and the
brand spec (default channel `www.brutalist.art`), the outro line now names the
brutalist.art destination: *"Claude, Flashcards. Liam here, in for Bear. Full
teardown at brutalist dot art."* IN-FOR-BEAR LAW preserved — Liam is in for
Bear, never claiming to be him.

**Judgement call — handle kept as `@HumanitariansAI`.** The scaffold left every
publishing-metadata field (`folderLabel`, `channel_title`, `OutroCTA.handle`,
`ground: #F3EBDD`) at HAI, i.e. this NBB-register cut is intended to publish on
the HAI channel. Register conversion should not silently rebrand the
publishing target. The outro *narration* names brutalist.art (per the SKILL.md
outro contract); the on-screen handle stays HAI (per the scaffold's intent).
If a full rebrand is wanted, a downstream pass should also update
`folderLabel`, `channel_title`, `ground`, and `handle` in one motion.

## Not touched

- `metadata.build`, `estimated_duration_s`, `actual_duration_s` (audio is the
  master clock; measurement happens at render time, not here).
- Every `beat_id`, every `shot` block's structure, `graphic.manim` scene
  names, `build` blocks, `note` fields (B00's TIMING LAW note still applies to
  the rewritten cold open).

## Removed

- `metadata._variant_todo` — the register rewrite, LLM-exercise insertion,
  outro, and ending-order verification are all done.

## Not done (out of scope)

- No rendering, audio generation, or compile. `mp3/`, `manim/`, `media/`
  reference the source paths from the pre-scaffold reel; the next pass has to
  run `generate_audio_kokoro.py` on this nbb sheet and re-render the beats
  whose narration or on-screen copy changed (all 11).
