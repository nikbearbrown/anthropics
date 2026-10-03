# REBUILD-LOG — medhavy-vox-epr-gap

Cohort: C (legacy vox). Skin: MEDHAVY (non-claude — Claude bookends never forced).
Rebuild pass: 2026-08-31.

## Locked (carried over verbatim)
- All `narration_text` per beat — no changes.
- Act structure and beat order (B01→B16).
- Shot INTENT: CARD `card:{...}`, GRAPHIC `production_viz` mechanics, STILL·ai scene
  descriptions, and the pre-existing FormACard scaffolds on B02/B06 — all kept.
- Metadata identity: title, slug, topic, audience, register, palette, outro source.

## Rebuilt (envelope normalize only, this pass)

| Field | Before | After | Why |
|---|---|---|---|
| `metadata.voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | *(dropped)* | ElevenLabs id — medhavy runs on Kokoro `af_kore`. VOICE-LOCK rule §2 drops dead ElevenLabs fields. |
| `metadata.clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | `"narration (Kokoro af_kore, VOICE-LOCK) — actual_duration_s measured from mp3/beat-*.mp3"` | Old prose was ElevenLabs-era ("until GATE 0"); measured mp3s already exist (Jul 16). |

## Datable-claims pass over narration

No datable claims found. The reel talks about EPR (mechanism, ~30 years old), a
"phase two trial" (generic — the sheet's `metadata.note` explicitly excludes
BIND-014 specifics), and illustrative accumulation numbers (8% ID/g, 0.3% ID/g)
labeled as such in the beat's `production_viz.note`. No model names, versions,
or prices. Narration untouched.

## Not touched (out of scope this pass)

- `shot.form` derivation per beat — deferred (batch job).
- Author `scenes.py` for the eight `production_viz` Manim scenes — deferred; those
  beats slate honestly for the review cut.
- Convert CARD beats (B01/B04/B09/B14) to `shot.remotion.pattern` — deferred.
- Fresh Kokoro audio regeneration — existing mp3s' narration matches current sheet
  exactly (verified against `beat_sheet.pre-rebuild.json` and `.bak-slatecard`
  backup); reusing them preserves the measured clock.

## Reversible

`beat_sheet.pre-rebuild.json` is a byte-exact copy of the pre-envelope-fix sheet.
Restore with `cp beat_sheet.pre-rebuild.json beat_sheet.json`.
