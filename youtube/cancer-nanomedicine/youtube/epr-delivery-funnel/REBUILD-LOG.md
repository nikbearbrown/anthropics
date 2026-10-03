# REBUILD-LOG — epr-delivery-funnel

Date: 2026-08-28

## Snapshot
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet (Aug 19 13843B).

## Envelope changes (VOICE-LOCK, drop dead fields)
- Dropped metadata `voice: "nbbhuman"` — ElevenLabs is dead; no on-machine Bear voice.
- Dropped metadata `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs).
- Added metadata `engine: "kokoro"`, `voice_kokoro: "am_onyx"`.
- Each beat now carries `voice: "am_onyx"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`.
- Kept `palette: "teardown"` (teardown register) — did NOT Claude-wash the NBB skin.
- Kept NBB channel skins for B00 open + B09 outro (channel-skin rule for non-claude channels).

## Narration edits — logged one per line (old → new → reason)
- B00: `"Nik Bear Brown. The EPR effect — the number that nearly broke a field."`
  → `"This is Liam, in for Bear. Nik Bear Brown. The EPR effect — the number that nearly broke a field."`
  → **Reason:** persona coherence — Kokoro `am_onyx` is Liam's voice; without the prepend Liam reads a Bear self-salute. Matches peer reel pattern (`claude-liam-epr-delivery-funnel`).
- B05 command: `"in 2025?"` → `"today?"` — **Reason:** datable-claim generalization.

## Placeholders filled (PHASE 1 §5 — no placeholder card text)
- B01 FormBCard items: `"Key point one/two/three"` (subs empty) → real items from the beat's own narration (premise / measurement / question).
- BVDT ClaudeVerdictArtifact lines: `"Key finding one/two/three"` → three real verdict lines built from body numbers (0.7% Wilhelm 2016 n=117 IQR 0.3–1.4%; Doxil cardiotoxicity + Abraxane SPARC/gp60; IFP + vascularity + protein corona).
- BVDT narration: EMPTY → new verdict narration (built from the sheet's own content, per rebuild §closing-block).
- BHTF narration: EMPTY → new your-turn narration.

## Punt sweep
- B06/B07/B08 were `source: null` SLATE holds — the narrations describe animatable structure (a ledger, a two-column comparison, a next-steps list). Routed each to `FormBCard` with real labels + subs (per nopunt catalog, enumerated concepts → FormB).
- B04 kept as Manim `B04_DeliveryFunnel` (vox_scenes.py exists in this reel, unlike peer).

## Lens check (LENS-NOTES.md)
- Descartes: names the exact number (0.7%) that would falsify EPR-as-clinical-driver.
- Hume: mouse-EPR confidence is not human-tumor confidence.
- Popper: Wilhelm 2016 IS the falsifying test the field had never organized.
- Plato: mouse-EPR is the artifact; human tumor delivery is the world; the relationship is the ~99.3% gap.
Four moves earned.

## Kept locked
- All body-beat narration (B01, B02, B03, B04, B06, B07, B08, B09) — verbatim from pre-rebuild.
- Beat order, act labels, source-pointer, title, slug, topic.
- Manim scene class `B04_DeliveryFunnel` and file `vox_scenes.py`.
