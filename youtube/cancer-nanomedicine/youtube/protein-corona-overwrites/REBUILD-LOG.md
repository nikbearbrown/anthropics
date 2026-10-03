# REBUILD-LOG — protein-corona-overwrites

Rebuild pass 2026-08-27. Locked-script contract observed (rebuild SKILL §Locked): no narration_text edits in body beats B01–B08. B00 and B09 narration also unchanged (Bear self-intro / sign-off, authored). Bookend narration (BVDT / BHTF / BOUT) was empty at start and was NEWLY authored per rebuild §5 "the close narration is NEW writing, built from the sheet's own sparkLines/verdict content".

## LOCKED (carried over verbatim)
- Body narration_text B01–B08 — byte-for-byte.
- B00 + B09 narration ("Nik Bear Brown. …" intro / outro) — unchanged.
- Beat order, act labels.
- Shot INTENT (NikBearBrown patterns for the CLI spine; Manim scene ref B04_ProteinCorona; visual_intent SLATE spec for the summary triplet, now materialized as FormBCards).
- Metadata identity: title, slug, topic, register=Teardown, palette=teardown.

## REBUILT
1. **VOICE-LOCK**: engine=kokoro, voice=am_onyx, voice_kokoro=am_onyx uniformly. Persona "Liam (in for Bear)" recorded. Dropped ElevenLabs `voice_id` and legacy top-level `voice: nbbhuman`.
2. **Bookends**: canonical B00 / BVDT / BHTF / BOUT preserved. NikBearBrownOpen / NikBearBrownOutro kept (channel-native, not Claude-washed). BVDT/BHTF/BOUT stay Claude-branded patterns per current NBB variant convention.
3. **Metadata**: added folderLabel + channel_title "@NikBearBrown", persona, variant "nbb-cli", built_at.
4. **Verdict body**: BVDT.artifactTitle, artifactHeading, artifactLines authored from body content (Vroman succession, MPS clearance, zwitterionic phase-2 record, apoA-I routing). Real narration authored to say the verdict aloud.
5. **Card content**: B01 FormBCard items rewritten (3 real items with sub lines from narration). B06/B07/B08 upgraded from `type: GRAPHIC, source: null` to real FormBCard patterns, each with 3 authored items drawn from beat narration + icons within the available public/form-b-icons/ set.
6. **Spark lines**: B02/B05 greeting replaced (3-word compression from beat narration).
7. **Audio**: fresh Kokoro generation (13 mp3s, ~240 s total). actual_duration_s measured and written back.
8. **Renders**: 12 Remotion + 1 Manim, all successful. B06/B07/B08 required an icon remap (route/compass/gauge/flask-conical → target/crosshair/ruler/clipboard-list — icons that actually ship in the public/form-b-icons/ directory).
9. **Gates**: content_check + frame_check + lane_check + GATE T (skip-pixels) + GATE AUDIO — all PASS.

## Datable-claims pass
- Scanned body narration for model names, versions, prices, "as of" claims.
- No model/version/price strings triggered edits.
- Numeric claims retained as authored (30 s, ~90% in vitro, ~50% in vivo, no zwitterionic phase-2 hits, DLS >30 nm threshold, 50% human serum protocol) — the 2026 nanomedicine record does not contradict any of these; FACTCHECK.md (existing since 2025-07-13) covers them.

## Narration edits
- None to any body beat (B00–B09).
- BVDT / BHTF / BOUT narration authored fresh (each was empty before this pass — permitted by rebuild §5).

## Envelope drops
- `metadata.voice_id` (ElevenLabs "TyW6NH39JcFb5M3xdIIk") — dropped.
- `metadata.voice` old value "nbbhuman" — replaced with kokoro voice envelope.

## vox_scenes.py patch
- Original: `sys.path.insert(0, parents[3] / "vox/aspects/explainer/vox-explainer/manim")` — resolved to a non-existent path in the anthropics/ tree.
- Patched: small loop walks parents[3..8], accepting either `parents[N] / "books/vox/…"` or `parents[N] / "vox/…"`.
- No scene class edits.
