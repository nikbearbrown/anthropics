# REBUILD-LOG — claude-liam-epr-delivery-funnel

Date: 2026-08-27
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet)

## Locked (carried over verbatim)
- All body narration on B00–B09 (script — the point of the reel).
- Beat order and act labels.
- Shot INTENT per body beat (patterns/props/topic strings).
- Metadata identity: title, slug, topic, register, source pointer, channel `@NikBearBrown`.

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED metadata `voice: "nbbhuman"` — inconsistent with the narration's Liam persona.
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam voice per persona statement in B00.
- DROPPED metadata `build` block — a Jul 16 build record that never survived
  (referenced `media/*.mp4` files that don't exist and now-stale slate list).

### Bookends
- B00 (NikBearBrownOpen): KEPT as channel's own open (rebuild contract:
  "Non-claude channels keep their own skins — never Claude-wash an open or outro").
- B09 (NikBearBrownOutro): KEPT as channel's own outro (same rule).
- BVDT (ClaudeVerdictArtifact): placeholder lines "Key finding one/two/three"
  and empty narration → AUTHORED from the body (below).
- BHTF (ClaudeComposerAsk): empty narration → AUTHORED short spoken close.
- BOUT (ClaudeTitleOutro): unchanged, no narration needed.

### Card content — SLATE beats converted to real Remotion cards
The pre-rebuild sheet had B01 as a placeholder FormBCard ("Key point one/two/three",
empty subs) and B04/B06/B07/B08 as unfilled slates with `shot.source: null` and
"YOU → 5–10s gen-AI clip" needs strings — the exact class of punt PHASE 1 §6 bans.

- B01 (FormBCard): items rewritten from B01's own narration (0.7% median dose,
  Wilhelm 2016).
- B04 (was: Manim `B04_DeliveryFunnel` — vox_scenes.py does not exist in the
  reel folder): converted to FormBCard (funnel-attrition table, 5 stages).
- B06 (was: slate): converted to FormBCard (Doxil/Abraxane honest ledger).
- B07 (was: slate): converted to FormBCard (mice vs humans summary).
- B08 (was: slate): converted to FormBCard (your-move next steps).

### Datable-claim edits (narration)
- B05 command text: `"still a viable design principle in 2025?"` →
  `"still a viable design principle today?"` (the "as of 2025" phrasing had
  rotted; the question stands without the date).
  Source: today is 2026-08-27 and Wilhelm's 2016 dataset plus the field's
  ongoing debate outdate a "in 2025" framing inside a demo prompt.

No other narration edits.

## Notes
- Card-only reel: this rebuild routes every body beat to a Remotion card
  (no Manim). PHASE 1 §7 flags card-only reels as a punt in a costume, but
  the funnel-stages card in B04 IS the drawn figure — a five-stage funnel
  table with numeric attrition per row. If a future pass restores a Manim
  scene, B04 should be re-routed.
- Lens (PHASE 1 §8): four moves earned — Descartes (what would falsify the
  EPR claim → the 0.7% number), Hume (mouse-model confidence doesn't extend
  to humans), Popper (Wilhelm 2016 was the falsifying test the field had
  never run), Plato (EPR-in-mice is the artifact; human tumor delivery is
  the world; the relationship is the disciplined field).
