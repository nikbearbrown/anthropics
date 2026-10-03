# REBUILD-LOG.md — medhavy-vox-delivery-diagnosis

Contract: `skills/make/rebuild/SKILL.md`. The narration is a LOCKED SCRIPT; the
envelope and machinery around it get rebuilt.

## Pre-rebuild backup

`beat_sheet.pre-rebuild.json` — byte-exact copy of `beat_sheet.json` as of
2026-08-31, made before any edit.

## Locked (unchanged)

- Every `narration_text` field, verbatim.
- Beat order, act labels, slug, title, topic, source pointer.
- `register: Wonder`, `palette: medhavy`, `audience: MEDHAVY`, `engine: kokoro`,
  `voice_kokoro: af_kore` — this is a MEDHAVY-channel reel, not Claude.

## Dead fields dropped (ElevenLabs-era envelope)

| Field | Value | Why dropped |
|---|---|---|
| `metadata.voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | ElevenLabs voice pointer — engine is Kokoro |
| `metadata.clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | ElevenLabs-era prose; `actual_duration_s` (measured) is the clock now |

## Datable-claim pass over narration

**No edits.** The reel is scientific mechanism (particles, biodistribution,
liver/spleen clearance, PEGylation). It names no models, no versions, no
prices, no "as of" claims. B11 numbers (7%, 21%, 75%, <3%, 10-patient cohort)
are already flagged in metadata as illustrative and are labelled as such in
the on-screen chart. Nothing rots.

## Shot / template rebuild

- B02, B08: `shot.remotion.pattern = FormACard` — locked pattern kept; the
  `props.lines[0]` were placeholder truncations of the narration (ended in "…").
  Rewrote as compressed insight lines drawn from the beat's own content:
  - B02: `"Where did the particles actually go?"` — the beat's driving question
  - B08: `"One image sorts the failure."` — the beat's meta-claim
- B04, B05, B07, B09, B11: `shot.type = GRAPHIC`, `graphic.manim = B0X_*` —
  scenes route to `runtime/manim/animated_graphics.py` per the standing
  pipeline. Not touched here.
- B06, B10: `shot.type = DOCUMENT` — quote cards with `highlight_words`,
  handled by the pipeline card renderer. Not touched.
- B01, B03, B12: `shot.type = CARD` — title / question / endcard, all with
  real copy in `card.copy` + `card.sub`.
- B13, B14: `remotion.pattern = OutroSeries` / `OutroCTA` — canonical medhavy
  outro block, unchanged.

## Non-Claude channel preserved

Per the rebuild contract: "Non-claude channels keep their own skins — never
Claude-wash an open or outro." No B00/BVDT/BHTF/BOUT added. The medhavy
open (B01 title card) and outro (B13→B14) stay.

## Audio

`mp3/beat-B01..B14.mp3` already generated (Kokoro `af_kore`, 2026-07-16).
Narration_text unchanged this pass → no regeneration needed. `actual_duration_s`
values recorded per beat are the clock.
