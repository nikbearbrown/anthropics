# REBUILD-LOG.md — vox-batch-distribution (2026-08-28)

Cohort C, legacy vox reel. Rebuild pass to VOICE-LOCK + slate-cut-honesty.

## LOCKED (verbatim)
- All 14 beat `narration_text` — the script is fixed.
- Beat order (B01 title → B12 endcard → B13/B14 outro).
- Metadata identity: slug, title, topic, source, style_bible, color_semantics.
- Shot intent per beat: `graphic.manim` class names in vox_scenes.py and
  `production_viz.mechanic` labels are the shot list, unchanged.

## REBUILT (envelope)
- Dropped `metadata.voice_id = "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs voice id,
  dead field per VOICE-LOCK.
- Added `metadata.engine = "kokoro"` and `metadata.voice = "am_onyx"`.
- Rewrote `metadata.clock` prose: was "narration (Kokoro (VOICE-LOCK)) —
  durations below are word-count estimates until GATE 0 audio lock"; now
  "measured Kokoro mp3s (VOICE-LOCK am_onyx) — actual_duration_s per beat
  is ground truth".
- Missing module fixed: `vox_scenes.py` imports `from vox_graphics import *`;
  the parents[3] path it referenced does not exist. Copied the vox_graphics
  library from the sibling reel `vox-emitter-range` into this reel's
  directory. Envelope-level dependency plumbing, no shot-intent change.

## DATABLE CLAIMS
None found. Narration uses stable regulatory concepts (PDI, monodisperse,
polydispersity), and every quantitative claim (98 nm mean, PDI 0.07/0.31,
15% > 200 nm, 40% less tumor delivery, 45-min/6-hr clearance) is already
labeled illustrative in FACTCHECK.md's "Illustrative Numbers Registry" and
in the narration itself ("An illustrative example"). No edits made.

## PUNTS FIXED
- **B02 FormACard.props.lines** — was a single truncated narration head
  ("A clinical-grade liposomal batch clears from a patient's bloodstream
  in forty-five…"), an obvious placeholder. Replaced with an honest
  three-line slate that names the artifact this beat needs:
  "SLATE — two amber vials, same 100 nm label / Batch A: 45-minute
  bloodstream clearance / Batch B (reference): 6-hour circulation". This
  beat renders as a still slate in this cut (no Remotion pipeline present) —
  media/B02.png is a PIL-drawn card carrying the same three lines.

## AUDIO
- Old mp3/ dir dated to 2026-07-08. ffprobe confirmed they were ElevenLabs
  encodes (44100 Hz, 128 kbps mono) — pre-VOICE-LOCK. Regenerated all 14
  beats via `generate_audio_kokoro.py` with the sheet-level am_onyx voice.
  New mp3s are 24000 Hz native Kokoro. `actual_duration_s` written back
  for every beat. Total: 179.2s.

## RENDERS
- `vox_scenes.py` classes rendered at 1280×720 → 24 fps → conformed to 4K
  by the compile step:
  B01 Title, B03 TheQuestion, B04 SmallMolecule, B05 NanoCloud,
  B06 TwoHistograms, B07 PDIScale, B08 ThreePopulations,
  B09 QuoteCard, B10 MatchMeanVsDistribution, B11 ExampleComparison,
  B12 End → `manim/B*.mp4` (11 clips).
- PIL-drawn PNG cards for the three no-Remotion beats:
  B02 two-vials slate, B13 OutroSeries, B14 OutroCTA → `media/B{02,13,14}.png`.
- B08 was re-rendered once after Gate V flagged small/mid/large label
  overlap (three sub-labels stacked on the same y-line under close-set
  braces). Layout fixed: single-word labels ("small clearance", "mid-range
  designed", "large liver/spleen"), mid-group offset lower so the three
  groups never share a horizontal band. Re-rendered, re-compiled.
