# CONVERT-LOG — claude-for-legal--claude-liam-matter-workspace → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
took the skill apart as a mechanism (one folder holding one SKILL.md, read then
executed top-to-bottom), surfaced the design intent (isolation-by-default at the
expense of frictionless cross-case recall), named the tradeoff explicitly at B02
and B05. Facts untouched — every reference to matter-workspace, SKILL.md, the
Steps section, CLAUDE.md, and the cross-matter switch survives from the source;
only the voice changed. Preserved every `beat_id`, act structure, `shot`/`graphic`
blocks, chip labels, captions, Manim scene names, and metadata (except `purpose`
register tag and the removed `_variant_todo`).

## Ending order (verified)
`B00 → B01 → B02 → B03 → B04 → B05 → B06 → B07 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF reslotted as the LLM exercise beat.** The source already used BHTF as
  a "your turn handoff" with a paste-ready Claude prompt via `ClaudeComposerAsk` —
  the same shape SKILL.md §Step 3 wants. Rather than insert a new beat and
  duplicate the composer card, I retitled the `act` to `LLM EXERCISE`, added the
  structured `llm_exercise: { prompt, dig_deeper }` field, folded the "Go deeper"
  follow-up into the spoken narration, and rewrote the prompt itself so it works
  in any frontier LLM (not just Claude-with-file-access). Bumped `estimated_duration_s`
  30 → 45s to fit the longer paste-ready prompt + dig-deeper sentence.

- **Rewrote the LLM prompt to be model-agnostic.** The source prompt asked Claude
  to "read the matter-workspace skill" — that only works in Claude with the file
  loaded, and produces nothing for a ChatGPT or Gemini viewer. Replaced it with a
  paste-ready ask that produces a useful output on its own: draft a SKILL.md for
  a legal-practice matter-isolation skill, showing file structure, Steps section,
  and the exact CLAUDE.md line to flip cross-matter context on. Also updated the
  ClaudeComposerAsk `command` prop and `runningText` ("paste this into any frontier
  LLM…") to match. The composer visual, greeting, topic, segment, and folder chip
  are otherwise preserved verbatim so the render layout is unchanged.

- **Dig-deeper prompt content.** Chose "what quiet mistake happens when a user
  forgets they left cross-matter context on — where does isolation-by-default
  protect them, and what does it fail to catch?" It's a real next question, not
  a summary; it points at the failure mode of the switch design (the user who
  turns it on for one job and forgets), which is the design's own quiet cost.

- **Outro left as OutroCTA with @HumanitariansAI handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel sits in the HAI
  playlist "Claude Basics" per `metadata.playlist`, and every sibling
  nbb-* sheet in this tree preserves the HAI handle for the same reason; (2)
  IN-FOR-BEAR LAW is satisfied by the existing "Liam, in for Bear" sign-off.
  The line was already clean Teardown (title callback + Liam disclosure), so I
  did not rewrite it.

- **B00 word budget respected.** Rewrite is 30 words; the beat's own TIMING LAW
  note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window.
  Preserved the "every → just this one" correction as the on-screen animation
  hinge (the single-token trigger rule from the fix note stays honored). Opened
  in Teardown register ("Natural read: … Wrong branch — …") without changing the
  underlying setup.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it would
  break sync between voiceover and typed quote. The source sentence already
  reads as clean Teardown (declarative, machinery-focused, names the constraint
  and the switch), so no rewrite was warranted.

- **`metadata.purpose` register tag** flipped from "Plain register" to "Teardown
  register" to match the actual voice now on the sheet. Every other metadata
  key (skill=hai-simple, style_preset=humanitarians, ground color, channel,
  playlist, anchor_pair, one_flag, gate_c/gate_h, build block) is preserved
  unchanged from the scaffold.

- **Nudged `estimated_duration_s` up on B02, B03, B05, B06, B07** to reflect
  the longer Teardown narrations (the source values were tuned to the tighter
  Plain-register lines). Ranges chosen from ~140 wpm speaking pace; the
  narration clock will be reset by real Kokoro durations at audio regen and
  these estimates are non-binding hints.

## Not done (intentional, out of scope for this pass)

- **No audio regenerated.** The existing `mp3/beat-*.mp3` files still reflect
  the old Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- **No compile / no render.** Deliverable is `beat_sheet.nbb.json` only.
