# CONVERT-LOG — claude-plugins-official--claude-liam-configure → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent named ("secrets change rarely, so cache;
policy changes mid-conversation, so re-read"), trade-offs surfaced ("no
validation over brittle validation"). Facts untouched — every mode, both file
roles, the pairing→allowlist flow, the read-once-vs-per-message asymmetry, and
the missing-validator gap all survive from the source; only the voice changed.
Preserved every `beat_id`, act structure, `shot`/`graphic` blocks, chip labels,
captions, Manim scene names, and the `note` on B00's TIMING LAW. `_variant_todo`
removed.

## Ending order (verified)
`… NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) reslotted as the LLM exercise beat.** Same move as
  sibling nbb-books--claude-liam-building-plugins. Source already used BHTF as
  a paste-ready Claude prompt via `ClaudeComposerAsk`, which is exactly the
  shape SKILL.md §Step 3 wants. Retitled `act` to `LLM EXERCISE`, added the
  structured `llm_exercise: { prompt, dig_deeper }` field, and folded a "Go
  deeper:" follow-up into the spoken narration. The composer shot (greeting,
  topic, folder chip, output block) is preserved; only the `command` and
  `segment` strings changed to carry the new prompt. Estimated duration bumped
  20 → 42s to fit the longer paste-ready prompt plus follow-up.

- **LLM prompt generalized off the video's teaching.** The reel's animating
  observation is that credential-based tools have two visibility clocks — one
  cached at startup, one live per-request — and often skip validation. The
  prompt asks the LLM to audit any tool the viewer actually uses along those
  same axes (which values cache, which reload, mid-session mutation behavior,
  validation gaps). It produces a useful output on its own, without the video,
  and it's a real reusable audit prompt — not a summary of what was just
  watched.

- **Dig-deeper: minimally invasive validator.** Chose "what would a minimally
  invasive validation layer look like — one that catches obviously-broken
  pastes without becoming brittle every time the credential format changes."
  It's a real next design question (the exact trade-off the configure skill
  itself punted on at NB03), not a recap.

- **BCRY narration kept identical to `WantQuote.props.quote`.** Same reason as
  sibling: the carry-out sentence is what appears on-screen typed; drifting
  the voiceover off the printed text would break sync. The source sentence
  already reads as clean Teardown (declarative, mechanism-first, no forbidden
  phrases), so no rewrite was warranted.

- **B00 word budget respected.** Rewrite is 34 words; the beat's own note
  requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window.
  Preserved the "now → after restart" correction as the animation hinge (props
  `triggerWords`/`replacementWords` unchanged). Reframed the setup in Teardown
  register by naming the mechanism directly up front ("the credential file
  gets read once, at startup") rather than the source's third-party framing
  ("someone assumed…").

- **Outro left as OutroSeries with @HumanitariansAI eyebrow** (not swapped to
  @NikBearBrown / www.brutalist.art). Same rationale as sibling: reel sits
  inside the HAI "Extending Claude — Skills, Plugins & Connectors" playlist,
  metadata.channel_title / folderLabel are HAI, and IN-FOR-BEAR LAW is
  satisfied by the existing "Liam, in for Bear" sign-off. The line was
  already clean Teardown (title callback + Liam disclosure), so I did not
  rewrite it.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (skill=hai-simple, style_preset=humanitarians, ground color,
  channel, playlist, anchor_pair, one_flag, gate_c/gate_h, build block) is
  preserved unchanged.

- **Estimated durations bumped for expanded beats.** NB01 26 → 36s, NB02 24 →
  30s, NB03 16 → 22s, BHTF 20 → 42s. Teardown rewrites add the "why they made
  this choice" clause, which lengthens narration; the estimates leave room for
  Kokoro's ~220wpm pace observed on the source. Real durations will come from
  `generate_audio_kokoro.py` in the render pass and will replace these.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` still reflect the Plain
  narration and must be re-run with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- No compile / no render. Deliverable is the beat sheet only.
