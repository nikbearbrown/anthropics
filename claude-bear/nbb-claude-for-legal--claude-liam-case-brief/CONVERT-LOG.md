# CONVERT-LOG — claude-for-legal--claude-liam-case-brief → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
explain the machinery, surface the design intent, name the trade-offs. Facts
untouched — case-brief is still one folder wrapping one SKILL.md, plain-language
steps, top-to-bottom execution, facts/issue/rule/conclusion output. Preserved
every `beat_id`, act structure, `shot`/`graphic` blocks, chip labels, captions,
Manim scene names, and the anchor pair (B03 → B06). `_variant_todo` removed.

## Ending order (verified)
`… B07 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF re-slotted as the LLM exercise beat** (same move as the sibling
  `nbb-books--claude-liam-building-plugins` conversion). The source already used
  BHTF as a "your turn handoff" with a paste-ready Claude prompt via the
  `ClaudeComposerAsk` scene — exactly the shape SKILL.md §Step 3 requires.
  Rather than insert a new beat and duplicate the composer card, I retitled its
  `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, and folded a "Go deeper:"
  follow-up into the spoken narration. The shot block (composer visual,
  greeting, folder chip) is preserved verbatim; `command` was updated to reflect
  the new, more general prompt. `estimated_duration_s` bumped 20 → 46s to fit
  the paste-ready prompt + dig-deeper follow-up (matching the ~42s the
  building-plugins reel used for the same structure).

- **New LLM prompt generalizes past "case brief".** The source's handoff was
  narrow ("pick one document I produce the same way every time"). Widened it to
  make explicit that the exercise applies to any repeated document
  (reports, briefs, meeting notes) — the video's actual carry-out is not
  about case briefs specifically, it's about the file-of-steps mechanism. A
  legal viewer still recognizes their brief in the prompt; a non-legal viewer
  isn't gated out.

- **Dig-deeper prompt content.** Chose "run the same skill against a case that
  almost fits but not quite — where does the file's structure force the wrong
  shape, and what would you have to add to catch that case without breaking the
  easy ones?" This is a genuinely explorable next question, not a summary; it
  pushes the viewer directly into B05's "off the map" territory and B07's
  "neither one is proof" — the failure mode the video itself surfaces.

- **BCRY narration kept identical to the WantQuote `props.quote`.** Same
  rationale as the plugins conversion: the carry-out sentence is what appears
  on-screen; drifting the audio off it would break lip-sync between voiceover
  and typed quote. The source sentence already reads as clean Teardown
  (declarative, machinery-focused, no forbidden phrases), so no rewrite was
  warranted.

- **B00 word budget respected.** Rewrite is 32 words; the beat's own TIMING LAW
  note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window.
  Preserved the "learned → was given" on-screen correction as the animation
  hinge; the narration frames it in Teardown register ("Wrong branch") without
  disturbing the underlying setup.

- **Outro left as OutroCTA with `@HumanitariansAI` handle** (not swapped to
  `@NikBearBrown` / `www.brutalist.art`). Same reasoning as the plugins reel:
  (1) this sheet lives inside the HAI "Claude Basics" playlist per
  `metadata.playlist`, and every sibling `nbb-books--claude-liam-*` sheet in
  this tree preserves the HAI handle; (2) IN-FOR-BEAR LAW is already satisfied
  by the "Liam, in for Bear" sign-off. The line was already clean Teardown
  (title callback + Liam disclosure), so I did not rewrite it.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (skill=hai-simple, style_preset=humanitarians, ground color,
  channel, playlist, anchor_pair, one_flag, gate_c/gate_h, build block) is
  preserved unchanged. The scaffold's `register`/`palette`/`audience`/
  `engine`/`voice_kokoro` already read "Teardown"/"teardown"/"NikBearBrown"/
  "kokoro"/"am_onyx" — left as scaffolded.

- **Anchor pair preserved intact.** B03 plants "one file / SKILL.md" as THE
  ANCHOR; B06 returns to it as THE ANCHOR RETURNS. Both rewrites keep the
  planting/returning gesture explicit ("Here is what a skill actually is. One
  file." → "Which is why case-brief never taught Claude how to read case law.
  The trick is guarantee, not knowledge."). Chip labels ("case-brief/",
  "SKILL.md") unchanged.

## Not done (intentional, out of scope for this pass)

- No audio regenerated. Existing `mp3/beat-*.mp3` files (if any exist in this
  new dir) still reflect the old Plain-register narration; the sibling reel's
  media/ folder isn't copied here. Audio must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` (voice `am_onyx`) before compile.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
