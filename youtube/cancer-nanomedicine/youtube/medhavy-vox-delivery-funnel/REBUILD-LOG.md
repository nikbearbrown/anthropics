# REBUILD-LOG — medhavy-vox-delivery-funnel
_Pass: 2026-08-28_

## Snapshot

`beat_sheet.pre-rebuild.json` written byte-exact before any edit.

## LOCKED (verbatim from pre-rebuild)

- All 13 `narration_text` fields — the script.
- Beat order (B01–B13), act structure, `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, purpose, register (Wonder), palette (medhavy), audience (MEDHAVY), `outro_source` (AUTHOR.MD :: Medhavy.com).
- `graphic.production_viz` intent blocks on B04–B08, B10 — the shot-list intent for a future Manim pass.
- `card.*` intent blocks on B01/B03/B09/B11.

## REBUILT (per current doctrine)

### Envelope
| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED | ElevenLabs-era prose |
| `style_bible` (visual_style / color_palette / lighting_style block) | present | DROPPED | Superseded by `style_preset:"vox-editorial"` + `color_semantics` line |
| `accents.data[]` list | `["#1F6F5C","#BF3339"]` | DROPPED | Superseded by `color_semantics` line; palette handled by `palette:"medhavy"` + Remotion tokens |
| `_variant_todo` | 4-item migration checklist | DROPPED | Migration is done |
| `build` | Jul 16 stamp claiming 11 slates | DROPPED (compile regenerates) | Stale — no rendered mp4s existed |
| `folderLabel` | (missing) | `"@MedhavyAI"` | Channel handle for Medhavy — was missing |
| `source` | (in `purpose` only) | separate `source` line | Peer standard (matches medhavy-vox-complexity-yield) |
| `engine` | `"kokoro"` | KEPT | |
| `voice_kokoro` | `"af_kore"` | KEPT | Medhavy channel voice |

### Datable claims in narration
None. The five-step delivery funnel (circulation → vessel → matrix → uptake → release) and the 0.7% mechanism are timeless. Illustrative numbers (18/14/12/55/0.7 of 100 units) are labeled illustrative both in narration and on card.

### Beat-level rebuilds

| Beat | Old shot | New shot | Reason |
|------|----------|----------|--------|
| B01 | CARD kind=title, `YOU → 5–10s gen-AI clip → pantry` | REMOTION `FormACard` `{lines:[title, sub, delivery funnel]}` | Punt costume; rendered as real title card |
| B02 | STILL src=ai, "YOU → 5–10s gen-AI clip" (truncated FormACard line `"The particle was designed carefully. It carries a targeting ligand that…"`) | REMOTION `FormACard` naming ligand / receptors / question | AI-still punt; no scenes on disk; honest text substitute |
| B03 | CARD kind=question, `YOU → 5–10s gen-AI clip → pantry` | REMOTION `FormACard` — Injected / Ligand working / where does 99.3% go | Punt costume; rendered as real question card |
| B04 | GRAPHIC `manim:B04_FiveSteps` (scene does not exist) | REMOTION `FormACard` — five sequential steps named | No `scenes_std.py`/`scenes.py` on disk; would fail lane-check |
| B05 | GRAPHIC `manim:B05_Drain1` (scene does not exist) | REMOTION `FormACard` — step 1 named + mechanism | Same — honest text substitute for drain chart |
| B06 | COMPOSITE `manim:B06_Drain2` (scene does not exist) | REMOTION `FormACard` — step 2 named + mechanism | Same |
| B07 | GRAPHIC `manim:B07_Drain345` (scene does not exist) | REMOTION `FormACard` — steps 3-4-5 + the 0.7% resolve | Same |
| B08 | GRAPHIC `manim:B08_TargetingFix` (scene does not exist) | REMOTION `FormACard` — targeting only helps at step 4 | Same |
| B09 | CARD kind=quote, `YOU → 5–10s gen-AI clip → pantry` | REMOTION `FormACard` — chain failed upstream | Punt costume; rendered as real quote card |
| B10 | GRAPHIC `manim:B10_Example` (scene does not exist) | REMOTION `FormACard` — 18/14/12/55/0.7 breakdown | Same — the numbers written explicitly |
| B11 | CARD kind=endcard, `YOU → 5–10s gen-AI clip → pantry` | REMOTION `FormACard` — endcard tagline | Punt costume; rendered as real endcard |
| B12 | OutroSeries `{seriesTitle, tagline, githubSlug}` (wrong schema — silently Claude-defaults) | OutroSeries `{eyebrow:"CANCER NANOMEDICINE", line:"Part of the Cancer Nanomedicine series on Medhavy AI."}` | Schema fix; Medhavy branding restored |
| B13 | OutroCTA `{authorName:"Nik Bear Brown", handle:"@MedhavyAI", ctaText:"Explore the full course at medhavy.com"}` (wrong schema) | OutroCTA `{line:"Explore the full course at medhavy.com", handle:"@MedhavyAI"}` | Schema fix; Medhavy handle |

### Bookends (non-Claude channel)
Rebuild contract §3 exempts non-Claude channels from Claude bookends. Medhavy skin format is body beats + `OutroSeries` + `OutroCTA` (peer template: `medhavy-vox-complexity-yield`). No `ClaudeComposerAsk`, no BVDT, no BHTF, no BOUT — as designed for this channel. The Medhavy outros (B12/B13) ARE the channel's bookend.

### Audio
Old ElevenLabs-era mp3s (Jul 16) deleted. Fresh Kokoro `af_kore` mp3s generated for all 13 beats. Measured durations written back to `actual_duration_s`. Total run: ~163s (13 beats × ~12s avg).

### Renders
All 13 beats → `media/B*.mp4` via `remotion_scenes.py` (FormACard × 11 + OutroSeries + OutroCTA). No `manim/` renders (no scenes on disk). No pantry/gen-AI clips.

## Not rebuilt (kept from pre-rebuild)

- Every narration line, verbatim.
- The `graphic.production_viz` intent blocks for B04–B08, B10 (document the visuals a future Manim pass should draw).
- `card.*` intent blocks on B01/B03/B09/B11 (kept as shot-list intent alongside new remotion.props).
- All shot-list identifiers (`new_visual_element`).

## Scripting gaps flagged for a future pass

- B04 five-step chain visualization (Manim graph flow).
- B05–B07 drain sequence (three bars shrinking with crimson loss chips).
- B08 targeting-fix annotation (gold bracket under step 4).
- B10 100-unit breakdown (two-column illustrative chart).

None of these blocks the current review cut — they upgrade it. The FormACard text substitutes name what should be drawn.

## Lens (PHASE 1 §8) — four moves earned

- **Descartes — falsification checklist:** what would falsify "the funnel leaks upstream"? Measure dose at each step; if the loss profile shows all 99.3% missing at step 4 alone, the framing is wrong. B04 states the five sequential steps as the checklist.
- **Hume — confidence is a property of the model:** the cell-culture kill result (B02) is a property of the assay, not of the mouse; the confidence transported from plate to animal is the failure mode. B10 labels the 100-unit numbers illustrative.
- **Popper — state failure criteria in advance:** which step's loss rate, if unchanged, would kill any downstream fix? B08 makes this Popperian move explicitly (step 4 fix is void if step 1 already killed the particle).
- **Plato — artifact vs world:** the artifact is the ligand-binds-receptors result; the world is an in-vivo delivery chain of five sequential filters; the relationship is that a step-4 artifact does no work if steps 1-3 have already cleared the dose. B09 states this directly.
