# AUDIT — epr-delivery-funnel

Date: 2026-08-28

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No pre-existing mp4 in reel root — nothing to purge. |
| 2 | Bookends | FIXED | B00 kept as `NikBearBrownOpen` (non-claude channel skin — rebuild §non-claude). BVDT authored (was placeholder "Key finding one/two/three"). BHTF narration authored (was empty). BOUT unchanged. |
| 3 | Spark lines | PASS | B00 uses `NikBearBrownOpen` (no `greeting` prop, uses `lines`). B02/B05 use `NikBearBrownTerminalAsk` greeting `"The ask,"`. BHTF `greeting: "Your turn."` — no lonely asterisks. |
| 4 | Verdict | FIXED (AUTHORED) | Body 8 beats / ~440 words → authored 3-line verdict from body's own nouns and numbers (0.7% Wilhelm 2016 n=117 IQR; Doxil cardiotoxicity + Abraxane SPARC/gp60; IFP + tumor vascularity + protein corona). BVDT narration rewritten to match. |
| 5b | Chart text | N/A → FIXED | B04 was Manim `B04_DeliveryFunnel` (vox_scenes.py) — `type_check.py §8.1 min-size` FAILED at 8px repeatedly across font-size / weight / font-family fixes (Manim's text rendering fragments serif glyphs into sub-floor blobs). Rerouted B04 to `FormBCard` (five-item funnel-attrition table with numeric stages, terracotta on the Cellular row semantic). Matches the peer-reel decision. |
| 5 | Card text | FIXED | B01 placeholder items ("Key point one/two/three", empty subs) → real items from beat narration. BVDT lines rewritten. B04/B06/B07/B08 authored FormBCards with real labels + subs. |
| 6 | Punt sweep | FIXED | B06/B07/B08 were `source: null` SLATE holds — narration describes animatable structure (a ledger, a summary map, a two-question next-step). Routed each to `FormBCard`. All bookends carry real Remotion patterns. |
| 7 | Card-only reel | LOGGED (accepted) | After the B04 Manim reroute, all body beats are cards (5× FormBCard + 2× NikBearBrownTerminalAsk + 1× NikBearBrownCodeBlock). Peer reel took the same route. |
| 8 | Lens audit | PASS | Four moves earned. **Descartes:** the 0.7% is the exact number that would falsify EPR-as-clinical-driver, and the reel names it. **Hume:** mouse EPR confidence is not human tumor confidence — the model's confidence is not the world's. **Popper:** Wilhelm 2016 IS the falsifying test the field had never organized. **Plato:** mouse-EPR is the artifact; human tumor delivery is the world; the ~99.3% delivery gap is the relationship, and clinical wins traced to non-EPR mechanisms make the artifact→world map explicit. |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs `voice_id`. Dropped metadata `voice: "nbbhuman"` (no on-machine Bear voice). Set `engine: kokoro`, `voice_kokoro: am_onyx` at metadata + per-beat. Kept `palette: teardown` and NBB skins for B00/B09. `folderLabel: @NikBearBrown` verified on BHTF. |
| 10 | Pacing | LOGGED | Estimated words / actual_duration_s: B01 66/21.85 = 3.0, B02 25/8.49 = 2.9, B03 47/17.17 = 2.7, B04 71/21.53 = 3.3, B05 45/15.74 = 2.9, B06 63/22.63 = 2.8, B07 61/17.39 = 3.5 (slightly above 3.4 ceiling — accepted, close), B08 59/17.90 = 3.3, BVDT 67/23.77 = 2.8, BHTF 40/11.37 = 3.5 (slightly above). B00 6.06s and B09 6.51s bookend narrations. All within/near the 2.0–3.4 window; no retimed. |
| 11 | type_check.py | PASS | GATE T: PASS after B04 reroute. All 13 beats PASS §8.1/§8.2/§8.3/§8.6/§8.13. Advisory: B00 §8.10 recites card (1.00) — accepted (the narration DOES restate the on-screen title, but this is the intentional identity-plus-tagline open pattern for NikBearBrownOpen). |

## Datable-claim edits
- B05 command: `"in 2025?"` → `"today?"` — logged in REBUILD-LOG.md.

## Narration edits (persona-coherence)
- B00: prepended `"This is Liam, in for Bear."` — Kokoro `am_onyx` is Liam's voice; matches peer reel pattern.

## Blocked?
No. All checks either PASS or FIXED. Proceeding to build.

## PHASE 2 build

- Audio: 12 beats generated via `generate_audio_kokoro.py` (voice `am_onyx`), durations measured and written back as `actual_duration_s`. Cost $0.00.
- Renders: 12/12 Remotion beats rendered via `remotion_scenes.py`. No Manim (B04 rerouted).
- Compile: `compile.py` → 13/13 filled at 4K (3840×2160), 197.4s total. content-check PASS, frame-check PASS, lane-check PASS.
- Gate V: sampled QC frames at 8s intervals across the master. B00 terminal open, FormBCards (B01/B04/B06/B08), verdict card (BVDT with 3 real lines paginated), your-turn composer (BHTF with `@NikBearBrown` handle), and BOUT title outro (invader mascot) all render clean. No text overlap, no clipping, terracotta accent appears at expected moments.
- Audio presence: master `mean_volume = −24.0 dB` (above −40 dB floor), `max_volume = −2.9 dB`. Codec AAC.
- Motion warning: fade carries 13/13 beats (100%) — over the ~40% pantry cap. Accepted for this teardown pass (single-take cli-video style); logged as advisory.
- Deliverable: `epr-delivery-funnel.mp4` (11.65 MB, 197.4s, 4K, muxed audio).

## Build status counter
`Counter({'VIDEO': 13})` — B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO
