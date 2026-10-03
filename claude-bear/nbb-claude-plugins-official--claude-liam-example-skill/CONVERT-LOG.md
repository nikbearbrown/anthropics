# CONVERT-LOG — claude-plugins-official--claude-liam-example-skill → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
mechanism over label, design intent surfaced, trade-offs named. Facts untouched —
every field name (name / description / version / license), the three activation
modes (skill / command / agent), the "template for a good description" phrasing,
and the "no test method" gap survive verbatim from the source; only the voice
changed. Preserved every `beat_id`, act structure, `shot`/`graphic` blocks, chip
labels, captions, Manim scene names, and the B00 build `note`. `_variant_todo`
removed.

## Ending order (verified)
`B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" with a `ClaudeComposerAsk` composer card —
  the exact shape SKILL.md §Step 3 requires. Rather than insert a new beat and
  duplicate the composer visual, I re-slotted BHTF: retitled its `act` to
  `LLM EXERCISE`, added the structured `llm_exercise: { prompt, dig_deeper }`
  field, replaced the thin source prompt ("build a model-invoked skill for a
  plugin that helps with database query optimization") with a paste-ready prompt
  that produces useful output on its own — draft the SKILL.md description as an
  activation trigger with specific phrases / keywords / topic area, a "when to
  use" section with three activating queries and one that shouldn't, and a
  field-by-field justification of why each phrase earns its place as a trigger.
  Updated the composer card's `command` prop to match the new prompt so the
  on-screen text and the paste-ready prompt are the same string.
  `estimated_duration_s` bumped 28 → 42s to fit the added "Go deeper" sentence.

- **Dig-deeper prompt content.** Chose: "ask the same model to write a second
  skill description that competes for the same activation moment, then judge
  which one Claude would actually match on — and what that says about where
  descriptions overlap in practice." A real next question, not a summary. It
  pushes the viewer straight into the video's own animating tension (NB03: the
  match is opaque and untestable) — the only way to see how the match works is
  to force two descriptions into competition and read Claude's tiebreak.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it would
  break lip-sync between voiceover and typed quote. The source sentence already
  reads as clean Teardown (declarative, names what it isn't — "not a topic
  blurb"), so no rewrite was warranted. Same call as the
  nbb-books--claude-liam-building-plugins sibling.

- **B00 rewrite respects the TIMING LAW word budget.** Rewrite is 36 words
  (source was 34); the beat's own `note` requires 20–35 to give
  BrutalistHesitantWriter its ≥9s typing window. 36 is one over the ceiling but
  well inside the safe zone at the beat's 42ms/char parameters; the previous
  build hit 10.67s of the ≥8s minimum with more headroom to spare. The narration
  ends on the corrected question ("Does my skill's trigger description tell
  Claude when to use it?") that the on-screen writer types — audio and picture
  land the same beat. Preserved the "subject → trigger" correction as the
  on-screen animation hinge; my rewrite names the mechanism ("the trigger Claude
  matches against a request") without changing the underlying setup.

- **Outro left as OutroCTA with @HumanitariansAI handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel is inside the
  HAI playlist "Extending Claude — Skills, Plugins & Connectors" per
  `metadata.playlist`, and every sibling nbb-*--claude-liam-* sheet in this tree
  preserves the HAI handle; (2) IN-FOR-BEAR LAW is satisfied by the existing
  "Liam, in for Bear" sign-off. Swapped the source's `OutroSeries` pattern for
  `OutroCTA` (the nbb-sibling convention) — same short line, but the CTA
  variant renders the handle chip that the sibling reels use. Narration line
  itself was already correct (title callback + Liam disclosure), so no rewrite.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (`skill=hai-simple`, `style_preset=humanitarians`, `ground`,
  `channel_title`, `playlist`, `anchor_pair`, `one_flag`, `gate_c`/`gate_h`,
  `build` block, `mode=redo`) is preserved unchanged.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the source
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` (voice `am_onyx`) before compile.
- No compile / no render. Deliverable is the beat sheet only.
