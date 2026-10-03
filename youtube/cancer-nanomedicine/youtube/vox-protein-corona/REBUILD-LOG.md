# REBUILD-LOG — vox-protein-corona (2026-08-30)

Legacy vox (Cohort C) reel, remastered under the current filmloop contract.

## Locked

- All 13 `narration_text` fields carried verbatim from `beat_sheet.pre-rebuild.json`.
- Beat order, act structure, and every card copy / production_viz description
  preserved.
- Metadata identity: title, slug, topic unchanged.

## Rebuilt

### Envelope (VOICE-LOCK normalize)

- DROPPED `metadata.voice_id: "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs-era field,
  banned under VOICE-LOCK.
- DROPPED `metadata.clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations
  below are word-count estimates until GATE 0 audio lock") — dead ElevenLabs-era
  phrasing.
- ADDED `metadata.channel: "@NikBearBrown"`.
- ADDED `metadata.folderLabel: "@NikBearBrown"`.
- ADDED `metadata.engine: "kokoro"`.
- ADDED `metadata.voice: "am_onyx"` (matches the Jul-8 Kokoro mp3s already on disk).

### B03 — routed off punt costume

- Old shot: `type=STILL, source=ai` + `remotion.pattern=FormACard` whose
  `props.lines[0]` was a truncated slice of narration ending in an ellipsis
  ("The moment a nanoparticle enters blood, plasma proteins begin adsorbing onto…").
  Punt under Amendment 6 (FormACard whose narration names a visual it never draws).
- New shot: `type=GRAPHIC, source=own, motion=drawon`, `graphic.manim=B03_ProteinsSwarm`.
- New scene added to `vox_scenes.py`: draws the four named proteins (albumin, IgG,
  fibrinogen, apolipoprotein) arriving in narration order and settling around the
  teal nanoparticle, with a "within seconds" caption on the last arrival.
- Narration UNCHANGED.

## Datable-claim edits

- None. The reel makes no model/version/price claims. The "illustrative numbers"
  in B09 (folate example: 87% / 72% / 3%) are already flagged illustrative in
  narration and on-screen — kept.

## Not carried

- Old `beat_sheet.json.bak-slatecard` (Aug 19) and `beat_sheet.hai.json` /
  `beat_sheet.medhavy.json` (audience-preset forks) are untouched; only the
  primary sheet was rebuilt.
