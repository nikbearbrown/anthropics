# CONVERT-LOG — healthcare--claude-liam-fhir → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced, tradeoffs named. Facts untouched —
every EHR name (Epic, Oracle Health/Cerner, MEDITECH, athenahealth), the
SMART-on-FHIR / FHIR R4 scope, the SKILL.md-as-instructions mechanism, the
retrieval-vs-judgment carry-out, and the pipeline nodes all survive from the
source; only the voice changed. Preserved every `beat_id`, act structure,
`shot`/remotion blocks, prop values, scene names, and on-screen text.
`_variant_todo` removed.

## Ending order (verified)
`B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) treated as the LLM exercise beat.** The source already
  used BHTF as a "your turn handoff" with a paste-ready Claude prompt via the
  `ClaudeComposerAsk` scene — exactly the shape SKILL.md §Step 3 requires.
  Rather than insert a new beat and double the composer card, re-slotted BHTF:
  retitled `act` to `LLM EXERCISE`, added the structured
  `llm_exercise: { prompt, dig_deeper }` field, and folded a new "Go deeper:"
  follow-up into the spoken narration. The shot block (composer visual,
  greeting, command text, folder chip) is preserved verbatim so the render is
  unchanged. `estimated_duration_s` bumped 22 → 42s to fit the added
  Teardown framing and "Go deeper" sentence.

- **Dig-deeper prompt content.** Chose "what would a clinician still have to
  do after fhir hands back the structured record — and which of those steps a
  different skill could realistically hold, versus the ones that will always
  stay with a human." A real next question, not a summary; it pushes the
  viewer to map the boundary between retrieval and clinical judgment, which is
  the video's own animating tension (B03, BCRY).

- **Outro left as OutroCTA with @HumanitariansAI handle** (not swapped to
  @NikBearBrown / www.brutalist.art). Two reasons: (1) this reel lives in the
  HAI "Claude Basics" playlist per metadata.playlist, and every sibling
  nbb-books--claude-liam-* / nbb-healthcare-* sheet in this tree preserves the
  HAI handle; (2) IN-FOR-BEAR LAW is satisfied by the existing "Liam, in for
  Bear" sign-off. Line was already clean Teardown (title callback + Liam
  disclosure), so no rewrite.

- **B00 word budget respected.** Rewrite is 34 words; the beat's own TIMING
  LAW note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing
  window. The on-screen "diagnoses → pulls records for" correction is
  preserved verbatim; the narration frames it in Teardown register ("Wrong
  lane… the reading is somebody else's job") without changing the underlying
  setup.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it
  would break lip-sync between voiceover and typed quote. The source sentence
  already reads as clean Teardown (declarative, machinery-focused, no
  "innovative"), so no rewrite was warranted.

- **B03 mechanism beat: named the tradeoff explicitly.** Source ended "…and
  that's a different skill." Teardown rewrite makes the design philosophy
  visible: "This skill optimized for reach across every major EHR at the
  expense of interpretation." That is the MKBHD lens the register requires,
  and it's honest — the fhir skill's whole point is coverage across
  heterogeneous endpoints, which is precisely why it can't do clinical
  judgment. `estimated_duration_s` bumped 20 → 22s for the added sentence.

- **`metadata.purpose` register tag** flipped from "Plain register" to
  "Teardown register" to match the actual voice now on the sheet. Every other
  metadata key (skill=hai-simple, style_preset=humanitarians, ground color,
  channel, playlist, gate_c/gate_h/gate_p, build block) is preserved
  unchanged. The scaffold-added keys (audience, derived_from, outro_source,
  typography) are kept.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files still reflect the old
  Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- No compile / no render. Deliverable is the beat sheet only.
