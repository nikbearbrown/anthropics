# REBUILD-LOG — medhavy-vox-complexity-yield
_Pass: 2026-08-27_

## Snapshot

`beat_sheet.pre-rebuild.json` written byte-exact before any edit.

## LOCKED (verbatim from pre-rebuild)

- All 13 `narration_text` fields.
- Beat order (B01–B13), act structure, `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, source, register, palette, audience, `outro_source`.
- `graphic.production_viz` blocks on B04–B07/B09/B10 (kept as the shot-list intent for a future Manim pass).

## REBUILT

### Envelope
| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED | ElevenLabs-era prose |
| `_variant_todo` | 4-item migration checklist | DROPPED | Migration is done |
| `build` | Old build stamp claiming B12/B13 VIDEO with hashes | DROPPED (compile regenerates) | media/ did not exist → false stamp |
| `folderLabel` | (missing) | `"@MedhavyAI"` | Was missing; channel handle for Medhavy |
| `engine` | `"kokoro"` | KEPT |  |
| `voice_kokoro` | `"af_kore"` | KEPT |  |

### Datable claims in narration
None. All narration references (Doxil, Abraxane, radioligands, 0.9⁶, 90%/95% quality thresholds) are timeless mechanism claims from the source chapter; no dated model names, prices, or "as of" phrasing.

### Beat-level rebuilds

| Beat | Old shot | New shot | Reason |
|------|----------|----------|--------|
| B01 | CARD (unfilled) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` `{lines:[title, sub, 0.9⁶ problem]}` | Punt costume; rendered as real title card |
| B02 | STILL src=ai (schematic — no source) | REMOTION `FormACard` naming the six components | AI-still punt; no Manim schematic exists; honest text substitute |
| B03 | CARD (unfilled) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — the question | Punt costume; rendered as real question card |
| B04 | GRAPHIC `manim:B04_GateMultiply` (scene does not exist) | REMOTION `FormACard` — "Reproducibility doesn't add — it multiplies / Six gates. Every one must open." | No scenes_std.py; would fail lane-check |
| B05 | GRAPHIC `manim:B05_YieldCollapse` (scene does not exist) | REMOTION `FormACard` — the six percentages written literally | Same — honest text substitute for the collapse chart |
| B06 | GRAPHIC `manim:B06_MathCard` (scene does not exist) | REMOTION `FormACard` — "0.9⁶ = 53% / 0.95⁶ = 74% / one batch in four still fails" | Same — the math written out |
| B07 | GRAPHIC `manim:B07_OneVsSix` (scene does not exist) | REMOTION `FormACard` — Doxil-vs-six-function contrast | Same — the contrast written as text |
| B08 | CARD — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — the design/manufacturing distinction | Punt costume; rendered as real section card |
| B09 | GRAPHIC `manim:B09_ProgramAB` (scene does not exist) | REMOTION `FormACard` — Program A/B batch counts, labeled illustrative | Same — the counts written explicitly |
| B10 | COMPOSITE `manim:B10_DesignChoice` (scene does not exist) | REMOTION `FormACard` — "Design choice multiplied the failure modes" | Same — the annotation written as text |
| B11 | CARD — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — endcard tagline | Punt costume; rendered as real endcard |
| B12 | OutroSeries `{seriesTitle, tagline, githubSlug}` (wrong schema — would Claude-wash) | OutroSeries `{eyebrow: "CANCER NANOMEDICINE", line: "Part of the Cancer Nanomedicine series on Medhavy AI."}` | Schema fix; Medhavy branding restored |
| B13 | OutroCTA `{authorName, handle, ctaText}` (wrong schema) | OutroCTA `{line: "Explore the full course at medhavy.com", handle: "@MedhavyAI"}` | Schema fix; Medhavy handle |

### Audio
Old ElevenLabs-era mp3s (Jul 16) deleted. Fresh Kokoro af_kore mp3s generated for all 13 beats. Measured durations written back to `actual_duration_s` (kokoro measurement equals the pre-existing sheet values within tolerance, since audio timing was already Kokoro-locked in this reel).

### Renders
All 13 beats → `media/B*.mp4` via `remotion_scenes.py`. No `manim/` renders (no scenes on disk). No pantry/gen-AI clips.

## Not rebuilt (kept from pre-rebuild)

- Every narration line, verbatim.
- The `graphic.production_viz` intent blocks for B04–B07/B09/B10 (they document the visual a future Manim pass should draw).
- `card.copy`/`card.sub` on the CARD beats (kept as the shot-list intent alongside the new remotion.props).
- All shot-list identifiers (`new_visual_element`, `scene_description`, `chosen_media`).

## Scripting gaps flagged for a future pass

- B02 wants a real 6-function nanoparticle schematic (Manim structure diagram).
- B04 wants six-gates animation.
- B05 wants the yield-collapse bar chart (core visual of the film).
- B06 wants the 0.9⁶=53% math card with gold highlight.
- B07 wants the one-vs-six TEAL-vs-CRIMSON contrast.
- B09/B10 want the Program A/B batch grid + annotation.

None of these blocks the current review cut — they upgrade it. The text substitutes name what should be drawn.
