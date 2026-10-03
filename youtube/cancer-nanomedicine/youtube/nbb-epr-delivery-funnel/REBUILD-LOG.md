# REBUILD-LOG — nbb-epr-delivery-funnel

_Started 2026-08-31 · rebuild contract per `skills/make/rebuild/SKILL.md`_

## Phase 0 — backup + normalize

- Wrote `beat_sheet.pre-rebuild.json` (byte-exact copy of pre-edit `beat_sheet.json`).
- Envelope: `voice=am_onyx, engine=kokoro, folderLabel=@NikBearBrown`.
- No ElevenLabs fields present, none carried forward.

## Structural changes (bookends canonicalized)

Beat sheet before: 16 beats — `NBB00, B00, B01…B08, NBB01, NBB02, NBB03, BVDT, BHTF, BOUT`.
Two duplicate bookend layers coexisted: legacy `NBB00–03` (real narration) and
canonical `B00/BVDT/BHTF/BOUT` (empty slates + template `Key finding one/two/three`).

Resolution (same as sibling `nbb-vox-delivery-funnel`): dropped the legacy `NBB00–NBB03`.
Kept the canonical `B00/BVDT/BHTF/BOUT`. Also dropped standalone body-only `B00`
(NikBearBrownOpen intro) — canonical `B00` is now the ClaudeComposerAsk cold open.

Beat sheet after: 12 beats — `B00, B01…B08, BVDT, BHTF, BOUT`.

## Narration changes (locked script + datable claims)

- **B01–B08 narration**: LOCKED — copied verbatim from source reel
  `../epr-delivery-funnel/beat_sheet.json` (which is the canonical rebuilt version).
- **B05 narration**: source reel already generalized "in 2025" → "today"
  (datable-claim fix, carried in unchanged).
- **B00**: authored fresh for cold open — `"Kia ora, Liam. The EPR effect — the
  number that nearly broke a field."` (rebuild doctrine allows a new close;
  applied to open too since old `B00 NikBearBrownOpen` is replaced by
  ClaudeComposerAsk).
- **BVDT narration**: NEW — authored from body nouns/numbers: 0.7%, Wilhelm
  2016 n=117, Doxil cardiotoxicity, Abraxane SPARC/gp60, IFP + corona.
- **BHTF narration**: NEW — authored exercise using body vocabulary (funnel
  stages, MEASURED vs ASSUMED, EPR-vs-other-mechanism disguise).

## Shot form derivations

- B00 → ClaudeComposerAsk (cold open ask, Claude skin on nbb channel per sibling
  precedent).
- B01, B04, B06, B07, B08 → FormBCard (multi-item value cards from source).
- B02, B05 → NikBearBrownTerminalAsk (terminal-ask beat).
- B03 → NikBearBrownCodeBlock (code beat).
- BVDT → ClaudeVerdictArtifact.
- BHTF → ClaudeComposerAsk (your-turn handoff).
- BOUT → ClaudeTitleOutro (silent, 6.0s).

## Renders

- **B01–B08**: reused source-reel `media/BXX.mp4` via cp (source is
  `../epr-delivery-funnel/media/BXX.mp4`; matched mp3 copied to local
  `mp3/beat-BXX.mp3`).
- **B00, BVDT, BHTF, BOUT**: rendered fresh via `remotion_scenes.py` — 4
  new Remotion clips written into `media/`.
- Audio: `generate_audio_kokoro.py --only B00 BVDT BHTF` — 3 new mp3s, free.
