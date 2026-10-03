# CONVERT-LOG — nbb-claude-code--claude-liam-claude-opus-4-5-migration

Register conversion from the source Plain-register beat sheet to the NikBearBrown
(Teardown) cut. Voice, facts, beat IDs, act structure, `shot` blocks and every
on-screen card copy are unchanged. Kokoro `am_onyx` — Liam, in for Bear.

## Rewrites

Every `narration_text` was rewritten in the Teardown register (Feynman × MKBHD)
per `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Every fact — numbers,
model names, platforms, header names, parameter names, sequence of edits —
survives unchanged. The rewrites explain the actual machinery (what "migrate"
does versus what "upgrade" would promise), reveal the design philosophy (four
mechanical edits and no prompt words, by design), and judge the trade-offs
(never silently rewrite your prompt vs you have to notice the drift yourself;
no accidental tier swap vs Haiku is one more thing to migrate by hand).

Beats rewritten: `B00`, `NB01`, `NB02`, `NB03`, `NB04`, `NB05`, `NB06`, `NB07`,
`NB08`, `NB09`, `NB10`, `BHTF`.

## Two intentional non-rewrites (judgement calls)

- **BCRY (carry-out)** — the source narration is identical, word for word, to
  the `WantQuote` on-screen `quote` and lives in that scene's prop. The SKILL.md
  explicitly preserves on-screen card copy that still fits the register, and
  this sentence — "only touches the model string, a header, and one parameter —
  never changes your prompts unless you ask it to" — is already a bare
  mechanical Teardown claim (mechanism + trade-off, no forbidden phrases).
  Rewriting narration alone would desync it from the on-screen quote card;
  rewriting both would drop the on-screen quote the beat exists to display.
  Kept aligned.

- **BOUT (outro)** — "Migrating to Opus 4.5. Liam, in for Bear." is the
  NikBearBrown outro line pattern used by every other converted reel in
  `anthropics/claude-bear/nbb-*/` (verified against
  `nbb-cwc-workshops--claude-liam-reorder-policy`,
  `nbb-claude-basics--feature-list-checkpoint-persistence`). Title +
  IN-FOR-BEAR sign-off is the canonical form; `OutroCTA` reads the same line
  from the on-screen prop, so preserving keeps sign-off + on-screen line in
  sync.

## Inserted beat — `B_LLM` (second-to-last)

A paste-ready LLM exercise beat, in the schema shown in `skills/make/nbb/SKILL.md
§Step 3`:

- **prompt** — asks any frontier LLM to write a full migration playbook a coding
  agent could follow to sweep Sonnet 4.5 → Opus 4.5 across a multi-platform
  Python service (Anthropic API + Bedrock + Vertex), covering call-site
  discovery, per-platform strings, beta headers, per-file reviewable edits, and
  Haiku. Explicitly asks for the pre-flight checks and the acceptance test.
  Produces something useful without the video.
- **dig_deeper** — "what would this playbook have to add before it could safely
  handle a codebase that mixes typed SDK calls with raw HTTPS POSTs, both
  hitting the same endpoint?" A real next question about a real corner case
  (call-site discovery misses raw HTTPS calls), not a recap.
- `shot: { type: "CARD", source: "own", motion: "hold" }` per SKILL.md.
- `estimated_duration_s: 65` — ~175 narrated words at Kokoro pace.

## Palette / voice metadata

`brand_variant.py` set `audience`, `register`, `palette`, `engine`,
`voice_kokoro`, `typography`, `derived_from`, `outro_source` at scaffold time.
Left exactly as scaffolded. `_variant_todo` removed.

Residual `style_preset: "humanitarians"` and `ground: "#F3EBDD"` from the source
sheet were **not** touched — the SKILL.md's rule is "do not re-scaffold" and
those fields are downstream of the `palette: "teardown"` resolver anyway.

## What was NOT changed

- Beat IDs, act labels, ordering (except the required `B_LLM` insertion).
- Every `shot` block, `graphic.production_viz`, Remotion `pattern` and `props`
  (including on-screen text: `code_lines`, `chips`, `caption`, `label`, `quote`,
  `sparkLine`, `command`, `folderLabel`).
- All build/audio metadata (`audio_file`, `build`, `actual_duration_s` where
  present from the source; new B_LLM has no build metadata yet).
- Nothing was rendered, compiled, or narrated. Audio and video generation is a
  separate pass.
