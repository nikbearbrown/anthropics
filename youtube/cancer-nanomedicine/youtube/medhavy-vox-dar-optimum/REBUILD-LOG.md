# REBUILD-LOG — medhavy-vox-dar-optimum

Rebuild contract (skills/make/rebuild): old sheet is the LOCKED script + shot list;
machinery around it is regenerated. Backup at `beat_sheet.pre-rebuild.json` (byte-exact).

## Locked (verbatim)
- Every `narration_text`. No datable-claim rot found; drug pharmacology, DAR mechanism,
  and the illustrative numbers (DAR-4 / DAR-8, 68% / 11%, 2.4 / 0.3 ug/g, 24h / 72h)
  are already framed as illustrative in the sheet and are pattern-real, not model-dated.
- Beat order (B01–B14), act labels, medhavy channel skin.
- Metadata identity: slug, title, topic, source pointer, palette (medhavy),
  register (Wonder), audience (MEDHAVY), outro pattern (OutroSeries + OutroCTA).

## Rebuilt (envelope, no narration touched)
1. VOICE-LOCK envelope normalize — DROPPED dead ElevenLabs-era fields:
   - `metadata.voice_id: "1sgY6Voq1aexKOB1IJ2D"` — legacy ElevenLabs handle.
   - `metadata.clock: "narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` — ElevenLabs-era prose already superseded by measured `actual_duration_s`.
   Kept: `metadata.engine: "kokoro"`, `metadata.voice_kokoro: "af_kore"` (medhavy voice).
2. Bookends — non-Claude channel; medhavy skins kept (B01 title card, B12 endcard,
   B13 OutroSeries, B14 OutroCTA). Rebuild rule 3 says non-claude channels keep their
   own skins — never Claude-wash.
3. `shot.form` — not derived; medhavy-vox schema uses `shot.type` + `graphic.manim` / `card` / `document` blocks. Sheet-level normalization is the ElevenLabs envelope only.
4. Audio — kokoro `af_kore`, VOICE-LOCK, regenerated fresh to reset the clock.
5. Renders — beats without `media/<B>.mp4` compile to a review slate (this is a review
   slate cut by design; the reel folder has no `scenes.py`, so machine-buildable Manim
   beats stay slated with their intent card until a scenes.py author pass).

## Datable-claim edits
None. No model names, no versions, no prices, no "as of" claims in narration.
Pharmacology facts are illustrative-by-declaration in the sheet's own note.
