# CONVERT-LOG — claude-for-legal--claude-liam-client-letter → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced, trade-offs named. Facts untouched
— every claim about skill mechanics, the SKILL.md file, the delete-the-folder
test, and the client-letter document shape survives from the source; only the
voice changed. Preserved every `beat_id`, act structure, `shot`/`graphic`
blocks, chip labels, captions, Manim scene names, and Remotion props.
`_variant_todo` removed. `metadata.purpose` retag from "Plain register" to
"Teardown register" to match the actual voice on the sheet.

## Ending order (verified)
`… B07 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) re-slotted as the LLM exercise beat.** The source
  already used BHTF as a "your turn handoff" with a paste-ready prompt via the
  `ClaudeComposerAsk` scene, which is exactly the shape SKILL.md §Step 3 asks
  for. Rather than insert a new beat and duplicate the composer card, I retitled
  the act to `LLM EXERCISE`, added the structured `llm_exercise: { prompt,
  dig_deeper }` field, and folded a new "Go deeper:" sentence into the spoken
  narration. The shot block (composer visual, greeting, command text, folder
  chip) is preserved verbatim so the render is unchanged.
  `estimated_duration_s` bumped 20 → 32 s to fit the added "Go deeper" sentence.
  Follows the sibling precedent set by
  `nbb-books--claude-liam-building-plugins/`.

- **Dig-deeper prompt content.** Chose "hand the same model a case that doesn't
  fit your usual template and ask where it silently starts filling in judgment
  you never wrote down — because that's the seam where a skill quietly goes off
  the map." It's a real next question, not a summary; it pushes the viewer to
  probe the "off the map" limit the video itself set up in B05 and B07 (the
  animating tension: consistency is what a skill buys you; anything the file
  didn't anticipate is where it breaks).

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the voiceover off the
  typed quote would break lip-sync. The source sentence already reads as clean
  Teardown (declarative, machinery-focused, no "innovative"), so no rewrite was
  warranted. Verified programmatically that narration_text == props.quote.

- **BOUT left as OutroCTA with @HumanitariansAI handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel sits in the HAI
  playlist "Claude Basics" per `metadata.playlist`, and every sibling
  `nbb-*--claude-liam-*` sheet in this tree preserves the HAI handle; (2)
  IN-FOR-BEAR LAW is already satisfied by the "Liam, in for Bear" sign-off. The
  line was already clean Teardown (title callback + Liam disclosure), so I did
  not rewrite it, and verified narration_text == props.line so the OutroCTA
  render is unchanged.

- **B00 word budget respected.** Rewrite is 32 words; the beat's own TIMING LAW
  note requires 20–35 to give BrutalistHesitantWriter its ≥9 s typing window.
  Preserved the "learned → was given" correction as the on-screen animation
  hinge (the `triggerWords`/`replacementWords` props are unchanged); the
  narration frames it in Teardown register ("Wrong branch. Nothing in the model
  changed — it was handed a file to follow.") without changing the underlying
  setup.

- **Body-beat rewrites kept close to source length.** B01–B07 gained a sentence
  each to surface the design intent (what the "skill" label optimizes for and
  what it costs), but no beat grew enough to blow past its
  `estimated_duration_s`. Nudged B01 10→14, B02 11→13, B04 11→12, B05 14→15, B06
  13→14, B07 17→20 to reflect the added Teardown clauses; each new estimate is
  still well within the beat's slot.

- **register / palette / engine / voice metadata:** all four are the scaffold
  defaults (`Teardown`, `teardown`, `kokoro`, `am_onyx`); left as scaffold set
  them. Kept every source metadata field otherwise intact
  (`skill=hai-simple`, `style_preset=humanitarians`, `ground=#F3EBDD`,
  `channel_title=@HumanitariansAI`, `anchor_pair`, `one_flag`, `gate_c/gate_h`,
  `build` block).

## Not done (intentional, out of scope for this pass)

- **No audio regenerated.** Existing `mp3/beat-*.mp3` files reflect the old
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the render
  pass.
- **No compile / no render.** Deliverable is the beat sheet only.
