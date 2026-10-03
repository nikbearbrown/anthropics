# REBUILD-LOG.md — vox-bystander-effect (2026-08-28)

Cohort C, legacy vox reel. Rebuild pass to VOICE-LOCK + slate-cut-honesty.

## LOCKED (verbatim)
- All 13 beat `narration_text` — the script is fixed.
- Beat order (B01 title → B11 endcard → B12 series-outro → B13 CTA).
- Metadata identity: slug, title, topic, source pointer, style_preset,
  color_semantics, EXCLUSIONS note.
- Shot intent per beat: `scene_class` names (vox_scenes.py) and the
  Remotion patterns on B12/B13 are the shot list, unchanged.

## REBUILT (envelope)
- Dropped `metadata.voice_id = "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs voice id,
  dead field per VOICE-LOCK.
- Added `metadata.engine = "kokoro"` and `metadata.voice = "am_onyx"`.
- Placed local `vox_graphics.py` (34,753 bytes, copied from sibling
  vox-emitter-range which had already been rebuilt) so the `vox_scenes.py`
  module actually imports. The prior `sys.path.insert` in vox_scenes.py
  pointed to a path that does not exist on this machine. Envelope-level
  plumbing; no shot-intent change.

## DATABLE CLAIMS
None found. Narration names durable drug identities (T-DM1, T-DXd,
trastuzumab, HER2) and general mechanism (charged fragment cannot cross
membrane, cleavable linker releases membrane-permeable payload). The
illustrative "~40 cells" / "5 entry points" figures are already framed
as illustrative-tumor-model numbers by the surrounding narration ("In a
HER2-low tumor patch"). No edits made.

## PUNTS FIXED
- **B07 FormACard.props.lines** — was a single truncated narration head
  ("So T-DM1 kills only the cell it entered. The HER2-negative cells…"),
  the classic scaffolder placeholder (ellipsis-terminated). Replaced with
  a three-line honest slate that names the artifact this beat needs:
  "SLATE — HER2-low tumor field, one confined kill /
  field of tumor cells: a few teal HER2-positive, majority ink-gray
  HER2-negative / one teal cell holds a crimson payload dot; surrounding
  gray neighbors survive untouched." B07 has no scene_class in
  vox_scenes.py; this beat renders as a slate in this cut.

## AUDIO
- Old `mp3/beat-*.mp3` dates to 2026-07-08 with `voice_id` ElevenLabs
  metadata — those mp3s are pre-VOICE-LOCK. Regenerating via Kokoro
  am_onyx overwrites them and updates `actual_duration_s`.

## RENDERS
- Manim classes present for B01–B06, B08–B11 (10 beats). B07 has no
  class → renders as an honest slate. B12/B13 use Remotion `OutroSeries`
  / `OutroCTA` — no local Remotion project in this reel dir, so those
  render as slate cards per PHASE 2 review-cut rules.
