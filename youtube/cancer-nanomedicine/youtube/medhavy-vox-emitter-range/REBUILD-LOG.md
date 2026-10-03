# REBUILD-LOG — vox-emitter-range (MEDHAVY)

**Rebuild date:** 2026-08-28
**Source cohort:** C (legacy vox, ElevenLabs-era envelope)
**Sibling pattern reference:** `medhavy-vox-batch-distribution/beat_sheet.json`

## Byte-exact backup
`beat_sheet.pre-rebuild.json` = pre-rebuild snapshot of `beat_sheet.json`.
Created 2026-08-28 before any edit. Reversible.

## Dropped fields (dead ElevenLabs envelope)
| Field | Old value | Reason |
|---|---|---|
| `metadata.voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | ElevenLabs voice id — VOICE-LOCK is kokoro |
| `metadata.clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | prose clock — replaced by measured mp3 durations already in `actual_duration_s` |
| `metadata._variant_todo` | array of variant todos | one-off task list from prior variant pipeline, superseded |

## Added / normalised metadata
- `subtitle`: "matching the emitter to the tumor's geometry"
- `folderLabel`: "@MedhavyAI" (channel handle, sibling standard)
- `metadata.build`: reset to review cut with slates initialised
- `total_estimated_duration_seconds`: recomputed 185.22s from measured mp3 sum

## VOICE-LOCK
- `engine`: `kokoro` (unchanged)
- `voice_kokoro`: `af_kore` (unchanged — Medhavy channel's Kore voice, matches sibling reels)
- Existing `mp3/beat-B01..B14.mp3` were generated with af_kore at kokoro 24kHz mono; retained, since narration is unchanged.

## Narration edits
NONE. Every `narration_text` is byte-identical to the pre-rebuild sheet. No datable claims required correction (energies, ranges, isotope names are physical constants; the illustrative case numbers are labelled "illustrative" and remain within the source chapter's own framing).

## Envelope rebuild — per beat
Every body beat's `shot` was rebuilt from the old CARD/GRAPHIC/STILL scaffolding to the current REMOTION FormACard pattern (matches sibling `batch-distribution`). Preserved as read-only production metadata:
- Old `graphic.manim` + `graphic.production_viz`: kept intact for future full-render pass
- Old `card`: kept as semantic reference
- Old `scene_description` (B07): kept as image-prompt reference

Each beat now has `shot.remotion.pattern: FormACard` with `props.lines` as a 3-line compression of the beat's own narration + `props.dark: false`. Acts assigned: COLD OPEN (B01) → THE PROBLEM (B02–B03) → THE QUESTION (B04) → THE MECHANISM (B05–B06) → THE IMPLICATION (B07–B10) → THE EXAMPLE (B11) → RECAP (B12) → OUTRO (B13–B14).

## Outros — new prop shape
- `B13 OutroSeries` props: `{seriesTitle, tagline, githubSlug}` → `{eyebrow, line}` (current zod schema in `runtime/remotion/src/scenes/OutroSeries.tsx`)
- `B14 OutroCTA` props: `{authorName, handle, ctaText}` → `{line, handle}` (current zod schema in `runtime/remotion/src/scenes/OutroCTA.tsx`)

## What is NOT locked-in yet
- `media/BXX.mp4` for every beat — REMOTION renders pending
- `clips/BXX.mp4` per-beat conforms — compile.py pending
- Master mp4 — pending
