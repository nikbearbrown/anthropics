# REBUILD-LOG — medhavy-vox-abraxane-solvent
_Pass: 2026-08-31, filmloop unattended_

## PHASE 0 rebuild contract

- `beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json` before any edit.
- Dead ElevenLabs-era fields DROPPED from metadata:
  - `voice_id: "1sgY6Voq1aexKOB1IJ2D"` — ElevenLabs voice slot, no longer used
  - `clock` string trimmed: `"...until GATE 0 audio lock"` → `"narration (Kokoro af_kore, VOICE-LOCK) — durations are measured actual_duration_s"` (audio is already measured; VOICE-LOCK gate is retired).
- VOICE-LOCK envelope retained: `engine: "kokoro"`, `voice_kokoro: "af_kore"` (Medhavy Wonder register default).
- Narration is LOCKED — zero narration text changed. All body beats keep their existing mp3s
  (`mp3/beat-B01..B17.mp3`) and measured `actual_duration_s` values.

## Shot-form derivation (GRAPHIC → REMOTION FormBCard/FormACard)

The pre-rebuild sheet routed 8 body beats (B03, B05, B07, B08, B09, B11, B13, B14) to
scaffolder-authored `graphic.manim` scene names (e.g. `B03_InsolubilityProblem`) with no
Remotion pattern, so compile could only stamp them as SLATE. Per SHOT-FORM-SYSTEM.md a form
without a template is a punt. The sister reel `hai-vox-abraxane-solvent` (same source card)
solved this by routing each `graphic.production_viz.mechanic` into a FormBCard/FormACard
pattern with real title + items. I transplanted the same conversion (register-neutral card
text carries over unchanged; palette stays medhavy via `dark: false` = cream ground).

| Beat | pre-rebuild `shot.type` | post `shot.type` | Remotion pattern |
|------|-------------------------|------------------|------------------|
| B02  | STILL (ai)              | STILL (ai)       | FormACard (compile fallback → real Remotion clip) |
| B03  | GRAPHIC (manim scaffold)| REMOTION         | FormBCard — "Paclitaxel Won't Dissolve in Water" |
| B05  | GRAPHIC                 | REMOTION         | FormBCard — "How Cremophor Triggers Reactions" |
| B07  | GRAPHIC                 | REMOTION         | FormBCard — "Abraxane: Protein Instead of Solvent" |
| B08  | GRAPHIC                 | REMOTION         | FormBCard — "Solvent Gone, Trigger Gone" |
| B09  | GRAPHIC                 | REMOTION         | FormACard — 4-line illustrative comparison |
| B10  | STILL (ai)              | STILL (ai)       | FormACard |
| B11  | GRAPHIC                 | REMOTION         | FormBCard — "Bag B — Abraxane" |
| B13  | GRAPHIC                 | REMOTION         | FormBCard — "Two Eras, One Drug" |
| B14  | GRAPHIC                 | REMOTION         | FormBCard — "Same Patient, Two Bags (Illustrative)" |

Stale `graphic` / `document` scaffold blocks removed from patched beats so the shot form is
unambiguous. B01 (title CARD), B04 (question CARD), B06 (DOCUMENT quote), B12 (section
CARD), B15 (endcard CARD) intentionally stay as declared slates — CARD/DOCUMENT beats are
the format for a review slate cut and remain the correct routing for these bookend-adjacent
beats in the medhavy skin.

## Non-Claude skin

Medhavy channel keeps its own skin per rebuild contract §5: no ClaudeComposerAsk /
ClaudeVerdictArtifact / ClaudeTitleOutro. B16 (`OutroSeries`) and B17 (`OutroCTA`) are the
medhavy outros already present and stamped `VIDEO`. No Claude-wash performed.
