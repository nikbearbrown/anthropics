# REBUILD-LOG.md — vox-emitter-range (2026-08-28)

Cohort C, legacy vox reel. Rebuild pass to VOICE-LOCK + slate-cut-honesty.

## LOCKED (verbatim)
- All 14 beat `narration_text` — the script is fixed.
- Beat order (B01 title → B12 endcard → B13/B14 outro).
- Metadata identity: slug, title, topic, source, style_bible, color_semantics.
- Shot intent per beat: `graphic.manim` class names (vox_scenes.py) and
  `production_viz.mechanic` labels are the shot list, unchanged.

## REBUILT (envelope)
- Dropped `metadata.voice_id = "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs voice id,
  dead field per VOICE-LOCK.
- Added `metadata.engine = "kokoro"` and `metadata.voice = "am_onyx"`.
- Rewrote `metadata.clock` prose: was "narration (Kokoro (VOICE-LOCK)) —
  durations below are word-count estimates until GATE 0 audio lock"; now
  "measured Kokoro mp3s (VOICE-LOCK am_onyx) — actual_duration_s per beat is
  ground truth". The previous phrasing described a pre-audio state that no
  longer applies.

## DATABLE CLAIMS
None found. Narration uses stable isotope names (Lu-177, Ac-225, SSTR2)
and physical ranges (0.05–0.1 mm alpha, 1–2 mm beta); illustrative kill
percentages (78% / 41%) are already labeled "illustrative numbers" in the
production_viz mechanic. No edits made.

## PUNTS FIXED
- **B07 FormACard.props.lines** — was a single truncated narration head
  ("Now the geometry problem. Real tumors are not uniform. A three-centimeter…"),
  an obvious placeholder. Replaced with an honest three-line slate that names
  the artifact this beat needs: "SLATE — heterogeneous tumor cross-section /
  3 cm neuroendocrine tumor: receptor-positive rim, receptor-negative core /
  drug binds the rim; no drug reaches the center". This beat renders as a
  slate in this cut (no Remotion pipeline present) — the slate label comes
  from `new_visual_element`, which already names the artifact honestly.

## AUDIO
- Old mp3/ dir dates to 2026-07-08 with `voice_id` ElevenLabs metadata —
  those mp3s are pre-VOICE-LOCK. Regenerating via Kokoro am_onyx will
  overwrite mp3/beat-*.mp3 and update actual_duration_s.

## RENDERS
No `manim/` or `media/*.mp4` beat renders exist. Every body beat compiles
as an honest slate for this review cut. `--allow-slates` is the format,
per PHASE 2 slate-cut rules.
