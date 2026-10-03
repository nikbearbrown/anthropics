# CONVERT-LOG — books--claude-liam-building-plugins → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced, tradeoffs named. Facts untouched —
every step count, plugin part, folder structure, and workflow example survives
from the source; only the voice changed. Preserved every `beat_id`, act
structure, `shot`/`graphic` blocks, chip labels, captions, and Manim scene names.
`_variant_todo` removed.

## Ending order (verified)
`… B22 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" with a paste-ready Claude prompt via the
  `ClaudeComposerAsk` scene, which is exactly the shape SKILL.md §Step 3
  requires. Rather than insert a new beat and duplicate the composer card, I
  re-slotted BHTF: retitled its `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, and folded a new "Go deeper:"
  follow-up into the spoken narration. The shot block (composer visual, greeting,
  command text, folder chip) is preserved verbatim so the render is unchanged.
  Estimated_duration bumped 30 → 42s to fit the added "Go deeper" sentence.

- **Dig-deeper prompt content.** Chose "what would break if a new hire tried to
  run this plugin cold — where does it quietly rely on judgment you never wrote
  down?" It's a real next question, not a summary; it pushes the viewer to
  audit the tacit-knowledge gap between operator-in-head and encoded-text, which
  is the video's own animating tension (B02–B04, B19).

- **Outro left as OutroCTA with @HumanitariansAI handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel is inside the
  HAI playlist "Extending Claude — Skills, Plugins & Connectors" per
  metadata.playlist, and every sibling nbb-books--claude-liam-* sheet in this
  tree preserves the HAI handle; (2) IN-FOR-BEAR LAW is satisfied by the
  existing "Liam, in for Bear" sign-off. The line was already clean Teardown
  (title callback + Liam disclosure), so I did not rewrite it.

- **B00 word budget respected.** Rewrite is 32 words; the beat's own TIMING LAW
  note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window.
  Preserved the "code → describe it" correction as the on-screen animation
  hinge; the narration frames it in Teardown register ("Wrong branch") without
  changing the underlying setup.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it
  would break lip-sync between voiceover and typed quote. The source sentence
  already reads as clean Teardown (declarative, machinery-focused, no
  "innovative"), so no rewrite was warranted.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (skill=hai-simple, style_preset=humanitarians, ground color,
  channel, playlist, anchor_pair, one_flag, gate_c/gate_h, build block) is
  preserved unchanged.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the old
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- No compile / no render. Deliverable is the beat sheet only.
