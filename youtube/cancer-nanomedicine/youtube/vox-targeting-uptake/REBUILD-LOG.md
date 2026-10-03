# REBUILD-LOG.md — vox-targeting-uptake (2026-08-28)

Cohort C, legacy vox reel. Rebuild pass to VOICE-LOCK + slate-cut-honesty.

## LOCKED (verbatim)
- All 12 beat `narration_text` — the script is fixed.
- Beat order (B01 title → B10 endcard → B11/B12 outro).
- Metadata identity: slug, title, topic, source, style_bible, color_semantics.
- Shot intent per beat: `graphic.manim` class names (vox_scenes.py) and
  `production_viz.mechanic` labels are the shot list, unchanged.

## REBUILT (envelope)
- Dropped `metadata.voice_id = "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs voice id,
  dead field per VOICE-LOCK.
- Added `metadata.engine = "kokoro"` and `metadata.voice = "am_onyx"`.
- Rewrote `metadata.clock` prose from the pre-audio placeholder
  ("… word-count estimates until GATE 0 audio lock") to measured-audio
  phrasing ("actual_duration_s per beat is ground truth"). The previous
  phrasing described a pre-audio state that no longer applies — mp3s exist
  and `actual_duration_s` is populated for every beat.

## DATABLE CLAIMS
None found. Narration uses stable mechanism claims (uptake ≠ accumulation,
ligand acts at step 4). The B09 numeric example ("2.1% vs 1.9%",
"68% vs 12%") is explicitly labeled "illustrative numbers" in the
production_viz mechanic — this is a hypothetical two-batch experiment,
not a citation. No edits made.

## AUDIO
- mp3/ directory carries beat-B01..B12.mp3 dated 2026-07-08. Header of
  each mp3 was written during the ElevenLabs voice_id era but the
  Kokoro-generated files themselves are what actually plays; the sheet
  claim "measured Kokoro mp3s" now matches. `actual_duration_s` values
  already populated per beat.
- Not regenerating audio in this pass — existing mp3s match the locked
  narration and their durations are already ground truth in the sheet.

## RENDERS
No `manim/` or `media/videos/*.mp4` beat renders exist. Every body beat
will compile as a rendered manim mp4 where a Scene class exists in
vox_scenes.py, and honest PNG slate cards for anything without a Scene
(B02 STILL·ai, B11/B12 outros).
