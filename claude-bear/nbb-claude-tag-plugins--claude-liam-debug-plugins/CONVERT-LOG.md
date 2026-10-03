# CONVERT-LOG — claude-tag-plugins--claude-liam-debug-plugins → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced ("evidence first, explanation
after"), tradeoffs named ("honest about what it can't reach; that honesty is
the feature"). Facts untouched — the three-step diagnostic order, the five
failure modes and their chip labels, the two limits, the /mnt/account-plugins
path, and the three "watch for" checks all survive from the source. Preserved
every `beat_id`, act structure, `shot`/`graphic` blocks, chip labels, captions,
and Manim scene names. `_variant_todo` removed.

## Ending order (verified)
`B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" with a paste-ready prompt via the
  `ClaudeComposerAsk` scene, which is the shape SKILL.md §Step 3 requires.
  Rather than insert a new beat and duplicate the composer card, I re-slotted
  BHTF: retitled its `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, folded a new "Go deeper:"
  follow-up into the spoken narration, and changed the intro from "Paste this
  into Claude Code" to "Paste this into Claude, ChatGPT, or Gemini" so it
  reads as a paste-ready frontier-LLM prompt, not a CLI command. The shot
  block (composer visual, greeting, command text, folder chip, three
  watch-fors) is preserved verbatim so the render is unchanged.
  `estimated_duration_s` bumped 26 → 42 to fit the added "Go deeper" sentence.

- **Dig-deeper prompt content.** Chose "which of your own everyday
  configurations get read once at session start and won't hot-reload — where
  might you be treating stale state as broken machinery without knowing it?"
  It's a real next question, not a summary; it pushes the viewer to generalize
  the video's central diagnosis (stale ≠ broken; some things read only at
  session start) to their own workflow, which is the animating tension across
  B00, NB03, and BCRY.

- **Outro left as OutroSeries with @HumanitariansAI eyebrow** (not swapped to
  OutroCTA / @NikBearBrown / www.brutalist.art). Two reasons: (1) the reel is
  inside the HAI playlist "Claude Basics" per metadata.playlist and every
  sibling nbb-* sheet in this tree preserves the HAI channel binding; (2)
  IN-FOR-BEAR LAW is already satisfied by the existing "Liam, in for Bear"
  sign-off. The line reads as clean Teardown (title callback + Liam
  disclosure), so no rewrite was warranted.

- **B00 word budget respected.** Rewrite is 33 words; the beat's own TIMING
  LAW note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing
  window. Preserved the "broken → stale" correction as the on-screen
  animation hinge; the narration frames it in Teardown register ("The reflex
  when a plugin won't show up is to call it broken. Usually it isn't — it's
  stale…") without changing the underlying setup or the composer's `text`,
  `triggerWords`, or `replacementWords`.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it
  would break sync between voiceover and typed quote. The source sentence
  already reads as clean Teardown (declarative, machinery-focused, no
  "innovative"/"seems as though"), so no rewrite was warranted.

- **NB01–NB03 lengthened moderately.** Each rewrite adds one design-critic
  clause after the mechanism ("Evidence first, explanation after. That
  sequence is the design choice…" / "Five causes, one usually to blame." /
  "The tool is honest about what it can't reach; that honesty is the
  feature."). Estimated durations bumped to reflect ≈30–40% longer narration
  (NB01 16 → 20; NB02 22 → 26; NB03 22 → 26). Chips, captions, accent
  indices, and Manim scene names untouched — the graphics still land on the
  same words they name.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (skill=hai-simple, style_preset=humanitarians, ground color,
  channel, playlist, anchor_pair, one_flag, gate_c/gate_h, build block) is
  preserved unchanged.

## Not done (intentional, out of scope for this pass)

- No audio regenerated. Existing `mp3/beat-*.mp3` files (if present in the
  scaffold) still reflect the old Plain-register narration and must be
  regenerated with `runtime/scripts/generate_audio_kokoro.py` before compile.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
