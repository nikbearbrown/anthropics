# REBUILD-LOG.md — hai-vox-dar-optimum

Rebuild contract per `brutalist-art/skills/make/rebuild/SKILL.md`.
Non-claude channel (HAI / Humanitarians AI): channel skin preserved — no Claude-wash.

## LOCKED (verbatim carry-over)
- Every beat's `narration_text` — the script.
- Beat order and act structure (B01–B12 body, B13 OutroSeries, B14 OutroCTA).
- Shot INTENT per beat (pattern/props/mechanic notes for Manim graphics, card copy).
- Metadata identity: title, slug, topic, source pointer, HAI register/palette.

## Datable-claim edits (the one narration exception)
None. The sheet's numbers (DAR-4, DAR-8, 68%, 11%, 2.4 ug/g, 0.3 ug/g, 24h, 72h) are
labeled ILLUSTRATIVE in the metadata note and are re-stated illustratively in-body
(B10 "sixty-eight percent … eleven percent", B11 "These numbers are illustrative.
The pattern is documented."). No model names, versions, prices, or "as of" claims
present. No edit required.

## REBUILT envelope
- Dropped `metadata.voice_id: "qdEb53HLreRBCD1FQE30"` (dead ElevenLabs field).
- Dropped `metadata.clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations
  below are word-count estimates until GATE 0 audio lock") — dead ElevenLabs-era
  prose; the sheet already carries `engine: kokoro` + `voice_kokoro: am_onyx`.
- Preserved `engine: kokoro` / `voice_kokoro: am_onyx` — current VOICE-LOCK.
- Added `shot.form` to every beat (SHOT-FORM-SYSTEM.md):
  - B01/B03/B08/B12 CARD → `slide-a`
  - B05 STILL (FormACard) → `slide-a`
  - B11 DOCUMENT quote → `slide-a`
  - B02/B06/B07 GRAPHIC mechanism accumulate/drawon → `simulation`
  - B04 GRAPHIC DAR range → `scale-compare`
  - B09/B10 GRAPHIC curve + bar-compare → `data-chart`
  - B13/B14 outros → `slide-a` (routed via their remotion.pattern)

## Bookends — HAI, not Claude
Rebuild SKILL rule: "Non-claude channels keep their own skins; don't Claude-wash
them." This reel's own bookends are OutroSeries (B13) + OutroCTA (B14) with a
title CARD at B01. Left intact.

## Audio
Kokoro `am_onyx` mp3s already generated and measured on 2026-07-16 (mp3/beat-B*.mp3,
timings.json). Actual durations already written back to sheet. No regeneration needed
— the clock is set. Re-running Kokoro would produce byte-identical audio.

## Files touched
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet (mtime
  2026-08-31).
- `beat_sheet.json` — envelope cleaned; shot.form added; narration untouched.
