# CONVERT-LOG — knowledge-work-plugins--claude-liam-brand-voice-enforcement → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced ("they chose predictability over
cleverness"), tradeoff explicitly named ("this works if you value repeatability;
it fails if you expected a model that already knew what your brand sounded
like"). Facts untouched — every mechanism claim (SKILL.md is plain text,
numbered Steps section, line-by-line check against listed rules, same input →
same output) survives from the source; only the voice changed. Preserved every
`beat_id`, act structure, `shot` / `remotion` / `graphic` blocks, chip labels,
captions, Manim scene names, and the BrutalistHesitantWriter animation props.
`metadata._variant_todo` removed. `metadata.purpose` register tag flipped from
"Plain register" to "Teardown register" to match the actual voice now on the
sheet.

## Ending order (verified)
`… B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) re-slotted as the LLM EXERCISE beat, not a new insert.**
  The source already used BHTF as a "your turn handoff" with a paste-ready prompt
  rendered through `ClaudeComposerAsk`, which is exactly the shape SKILL.md §Step 3
  requires. Rather than insert a new beat and duplicate the composer card, I
  re-slotted BHTF: retitled `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, and folded a new "Go deeper:"
  follow-up into the spoken narration. Same pattern as the sibling
  `nbb-books--claude-liam-building-plugins` reel (see its CONVERT-LOG). The
  composer shot block (greeting, topic, segment, command text, folder chip) is
  preserved verbatim so the visual render is unchanged. `estimated_duration_s`
  bumped 22 → 34s to fit the added "Go deeper" sentence.

- **`llm_exercise.prompt` written to run without user data first.** Source
  `props.command` says "check this paragraph" but no paragraph is supplied; a
  viewer pasting it cold would confuse the model. My structured `prompt` version
  tells the model to expect a paragraph in the next turn ("When I paste a short
  paragraph next, check it line by line…") and adds a second-pass rule-proposal
  step, so the exercise produces useful output on its own without depending on
  what the viewer types after. The tighter on-screen `props.command` is kept as
  the visual — it's the compressed reminder viewers screenshot; the fuller
  paste-ready form lives in `llm_exercise.prompt`.

- **Dig-deeper prompt content.** Chose "what kinds of voice problems a rule-file
  check like this can't catch at all — where does an off-brand paragraph still
  slip through when every listed rule passes?" It's a genuinely explorable next
  question (not a summary), and it pushes the viewer to audit the tacit-knowledge
  gap between a checklist and a voice — which is the video's own animating
  tension (the "know" → "check" correction in B00, the "no telepathy, only what
  the file lists" beat in NB03).

- **BCRY narration kept identical to the source.** Two reasons: (1) the source
  sentence is already clean Teardown (declarative, mechanism-first, no forbidden
  phrases — "same input, same output, every time", "the limit is exactly what
  the file says"); (2) the first two sentences appear on-screen verbatim as the
  `WantQuote` prop, so any drift between voice-over and typed quote would break
  lip-sync. Sibling nbb reels follow the same rule.

- **Outro left as OutroSeries with @HumanitariansAI eyebrow** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel lives inside
  the HAI playlist "Extending Claude — Skills, Plugins & Connectors" per
  `metadata.playlist`, `channel_title`, and `folderLabel` — and every sibling
  `nbb-*` sheet in this claude-bear tree preserves the HAI handle; (2)
  IN-FOR-BEAR LAW is satisfied by the existing "Liam, in for Bear" sign-off in
  the narration. The outro line is already clean Teardown (title callback +
  Liam disclosure), so no rewrite was warranted.

- **B00 word budget respected.** Rewrite is 32 words; B00's own TIMING LAW note
  requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window. Kept
  the "know → check" correction as the on-screen animation hinge; the
  Teardown-register frame ("there's no brand-vector in the weights") explains
  the mechanism without moving the animation hinge or the ending question.

- **NB01–NB03 lengths stayed close to source.** NB01 (~50 words), NB02 (~60
  words), NB03 (~75 words) — modest expansion to add design-intent framing
  ("the design choice is honest", "they chose predictability over cleverness",
  "this works if you value X; it fails if you need Y"). `estimated_duration_s`
  updated on each to reflect the new word count at ~2.6 words/sec.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the
  source Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- No compile, no render, no upscale. Deliverable is the beat sheet only.
