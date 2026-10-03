# CONVERT-LOG — claude-for-legal--claude-liam-claim-chart → nbb

Rewrote every body beat's `narration_text` (B00–B03) in the Teardown register
(Feynman × MKBHD): explain the machinery, surface the design intent, name the
trade-off. Facts untouched — the chart still decomposes a claim into elements,
pin-cites what's supported (locking mechanism → manual, page twelve), flags what
isn't (temperature sensor → no citation found), and the carry-out is unchanged.
Preserved every `beat_id`, act structure, `shot`/`graphic`/`remotion` blocks,
Manim scene names (CLCB01/02/03Scene), the anchor pair (B02 → B03), the
`WantQuote` `sparkLine`, and all on-screen card copy. `_variant_todo` removed.

## Ending order (verified)

`… B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF re-slotted as the LLM exercise beat** (same move as the sibling
  `nbb-…-case-brief` and `nbb-…-ip-clause-review` conversions). The source
  already used BHTF as a "your turn handoff" with a paste-ready Claude prompt
  via the `ClaudeComposerAsk` scene — exactly the shape SKILL.md §Step 3
  requires. Rather than insert a duplicate composer card, I retitled the `act`
  to `LLM EXERCISE`, added the structured `llm_exercise: { prompt, dig_deeper }`
  field, and folded a "Go deeper:" follow-up into the spoken narration. The
  shot block (composer visual, greeting, folder chip, runningText) is preserved
  verbatim; `command` and `segment` were updated to reflect the new,
  generalized prompt. `estimated_duration_s` bumped 24 → 48s to fit the
  paste-ready prompt + dig-deeper follow-up (matches the ~46s used by the
  case-brief reel for the same structure).

- **LLM prompt generalized past "patent claim chart"**. The source's handoff
  was narrow ("paste in the claim language, element by element, along with the
  accused product's documentation"). Widened it to any element-based evidence
  check — a list of claim elements plus a source document — because the video's
  actual carry-out is not patent-specific, it's about the element-by-element
  routine with explicit gap flagging. A patent viewer still recognizes their
  claim chart in the prompt; a civil litigator, a compliance reviewer, or any
  non-legal viewer doing an element-vs-source cross-check isn't gated out.
  The output shape (two-column table: element, then pin cite or gap flag)
  reflects the two-row graphic the video plants at B02 and pays off at B03.

- **Dig-deeper prompt content.** Chose "what's the weakest cite that made it
  in, and what would a follow-up document need to say to close a gap without
  stretching the language you already have?" This is a genuinely explorable
  next question, not a summary. It pushes the viewer directly into B03's
  "filled != proven" side of the anchor payoff — the failure mode the video
  itself surfaces (a citation can be weak, or cover only part of the element).

- **BCRY narration kept identical to the `WantQuote.props.quote`.** Same
  rationale as the case-brief and plugins conversions: the carry-out sentence
  is what appears on-screen; drifting the audio off it would break lip-sync
  between voiceover and typed quote. The source sentence already reads as
  clean Teardown (declarative, machinery-focused, no forbidden phrases), so no
  rewrite was warranted. The `sparkLine` ("A pin cite for what's there. A flag
  for what isn't.") is also left intact.

- **B00 word budget respected.** Rewrite is 33 words; the beat's own TIMING LAW
  note requires 20–35 to give BrutalistHesitantWriter its ≥9s typing window.
  Preserved the "prove → map" on-screen correction as the animation hinge; the
  narration frames it in Teardown register ("Wrong verb.") without disturbing
  the underlying setup or the seed.

- **Outro left as OutroCTA with `@HumanitariansAI` handle** (not swapped to
  `@NikBearBrown` / `www.brutalist.art`). Same reasoning as the case-brief
  reel: (1) this sheet lives inside the HAI "Claude Basics" playlist per
  `metadata.playlist`, and every sibling `nbb-…-claude-liam-*` sheet in this
  tree preserves the HAI handle; (2) IN-FOR-BEAR LAW is already satisfied by
  the "Liam, in for Bear" sign-off. The BOUT line was already clean Teardown
  (title callback + Liam disclosure), so I did not rewrite it.

- **Anchor pair preserved intact.** B02 plants the two-row chart ("A LOCKING
  MECHANISM" cited, "A TEMPERATURE SENSOR" gapped); B03 returns to it,
  resolves both cells, and splits into "FILLED != PROVEN" / "GAP != FAILED".
  Both rewrites keep the planting/returning gesture explicit ("Two elements
  from the same claim, same manual" → "So the chart lands with both cells
  settled"). Graphic labels, `production_viz.mechanic` text, chip labels, and
  the palette hex list are all unchanged.

- **Metadata `register` was already "Teardown"** on the scaffold; left as
  scaffolded. Every other metadata key (skill=hai-simple,
  style_preset=humanitarians, ground color, channel, playlist, anchor_pair,
  gate_c/gate_h, build block, audience=NikBearBrown, engine=kokoro,
  voice_kokoro=am_onyx, palette=teardown, typography) is preserved unchanged.
  `metadata.purpose` still describes the video accurately (register-agnostic
  wording), so it was not touched.

## Not done (intentional, out of scope for this pass)

- No audio regenerated. Existing `mp3/beat-*.mp3` files (if any exist in this
  new dir) still reflect the old Plain-register narration. Audio must be
  regenerated with `runtime/scripts/generate_audio_kokoro.py` (voice `am_onyx`)
  before compile.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
