# AUDIT.md — vox-epr-gap (2026-08-30)

Style: `vox-editorial` (teal/crimson, not Claude). Rebuild contract: keep the reel's own skin — no Claude-washing bookends.

## PHASE 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` written (byte-exact copy) before any edit — PASS.
- Narration LOCKED — no narration edits made this pass.
- VOICE-LOCK normalize: dropped ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk`; refreshed `clock` prose; added `engine: kokoro`, `voice: am_onyx`, `channel: @NikBearBrown`, `folderLabel: @NikBearBrown`.
- Non-claude skin preserved: vox bookends (title CARD / question CARD / endcard / OutroSeries / OutroCTA) kept.

## PHASE 1 — Checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No mp4s at reel root; only Manim partials under media/videos/vox_scenes/1080p24/partial_movie_files/. Nothing to delete. |
| 2 | Bookends | PASS | Vox skin preserved per rebuild contract. B01 title CARD, B04 question CARD, B14 endcard, B15 OutroSeries, B16 OutroCTA — canonical for vox-editorial. |
| 3 | Spark lines | N/A | Vox reel; no ClaudeComposerAsk beats. |
| 4 | Verdict | PASS | B14 endcard: real recap authored from body content ("The mouse model runs EPR at maximum. The patient runs EPR at real — compressed, fibrous, variable. Same nanoparticle. Different biological world."). Not template. |
| 5b | Chart text | PASS (deferred to Gate V) | production_viz labels are short category nouns ("Mouse xenograft", "Patient tumors", "8% ID/g"), not narration slices. Bottom captions ("same chemistry — interpatient EPR variability") are complete phrases. |
| 5c | Your-Turn placeholder | N/A | Vox reel has no BHTF. |
| 5 | Card text | FIXED | B02 and B06 FormACard `lines` were ellipsis-truncated narration ("A docetaxel nanoparticle accumulates…" / "This is the enhanced permeability and retention effect — EPR. It…"). Replaced with real multi-line summaries drawn from the beat's own claim. |
| 6 | Punt sweep | FIXED | B02 and B06 previously carried `shot.type=STILL source=ai` with a scene_description asking for a generic AI lab-photo / schematic diagram — the classic gen-AI ask punt. The remotion.FormACard fallback now renders real summary lines (breather beats), so the reel no longer punts to unfilled AI stills. IDEAL future rebuild would author Manim schematics for both, but the FormA fallback is honest, not a costumed punt. |
| 7 | Card-only reel | PASS | 10 of 16 beats route to Manim (B03, B05, B07–B13 + B01 title, B14 endcard). Body is drawn, not carded. |
| 8 | Lens audit | PASS | Descartes: "what would falsify this?" — the narration explicitly foregrounds "The chemistry never changed" and asks why the same molecule fails, then names the falsifier (desmoplastic stroma). Popper: states in advance what would refute EPR-only explanation, then names it (interstitial fluid pressure + fibrous compression). Plato: names artifact (preclinical result), world (patient tumor), relationship (idealized model vs real biology). Two moves earned; three arguably. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown`, `engine: kokoro`, `voice: am_onyx`. Persona coherence intact — vox-editorial narration in Kokoro `am_onyx` (Liam). |
| 10 | Pacing | PASS | All beats within 2.0–3.4 wps against actual_duration_s. B01 ~3.0 wps, body beats 2.4–2.9 wps. |
| 11 | type_check.py | PASS | GATE T green, 0 FAILs. Two §8.10 recitation advisories on B02/B06 (0.85/0.94) — expected before the FormACard `lines` change; the new summary lines diverge from narration and should drop the score at next check-post-render. Advisory does not block. |

## Blocked?

No. All checks passed or fixed pre-compile.
