# AUDIT.md — hai-vox-dar-optimum
Channel: @HumanitariansAI. Register: Pragmatist. Palette: humanitarians. Voice: Kokoro am_onyx.

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 files present (nothing to invalidate). |
| 2 | Bookends | PASS | HAI-channel reel keeps its own skin (B01 title CARD + B13 OutroSeries + B14 OutroCTA). Rebuild rule: non-claude channels are NOT Claude-washed. B00/BVDT/BHTF/BOUT pattern is not required here. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats in this reel. |
| 4 | Verdict | PASS-absent | No BVDT beat present, so no placeholder to strip. Endcard B12 carries the equivalent claim: "DAR is an optimum, not a maximum. Past the sweet spot, more warheads means less delivery." — specific, reel-authored, would not be true of another video. Amendment: absent is legal. |
| 5 | Card text | PASS | B01/B03/B08/B12 cards carry real copy/sub (no TBD/placeholder). B05 FormACard line "Too little is the first failure. Even if the antibody finds…" carries content — content-truth, though the ellipsis reads as a fragment. LOG-only. |
| 5b | Chart text | PASS | Manim graphics (B02/B04/B06/B07/B09/B10) specify short category-noun labels in `production_viz.mechanic` (antibody / DAR scale / plasma bars / optimum curve), not narration slices. Bar semantics agree with narration (DAR-4 taller, DAR-8 shorter). |
| 5c | Your-Turn placeholder | N/A | No BHTF beat (HAI outro pair instead). |
| 6 | Punt sweep | PASS | Zero gen-AI asks alive: legacy `build.needs` strings ("YOU → 5–10s gen-AI clip") on B01/B03/B08/B11/B12 are stale metadata; the actual shot spec on each is CARD/DOCUMENT with real copy and renders as such. No unfilled fill_slates or remotion_scenes slates. No DoodleScene/DoodleChart. No archive stills. Every card names a visual the render can draw. |
| 7 | Card-only reel | PASS | 6 of 12 body beats are Manim GRAPHIC (B02/B04/B06/B07/B09/B10) — not card-only. |
| 8 | Lens audit | PASS | Popper: two failure modes are stated in advance (under-payload underdose in B05; over-payload aggregation + rapid clearance in B06–B07) with numeric thresholds (DAR range 4–8) and mechanism (hydrophobicity → clearance). Hume: numbers are labeled "illustrative" and B11 explicitly separates instance from pattern ("These numbers are illustrative. The pattern is documented."). Two moves earned from source material. |
| 9 | Brand fields | PASS | engine=kokoro, voice_kokoro=am_onyx. Palette humanitarians. Register Pragmatist. No `folderLabel` field in this old-format sheet (schema does not require it). Persona coherent: Liam voice, HAI outro. |
| 10 | Pacing | PASS with 1 log | wps against measured audio: B01 2.86 / B02 3.15 / B03 2.98 / B04 3.16 / B05 3.05 / B06 2.79 / B07 3.03 / B08 3.16 / B09 2.99 / B10 2.93 / B11 2.73 / B12 2.81 / B13 2.50 — all in 2.0–3.4 window. **B14 1.65 wps** — outro CTA "Find more at humanitarians.ai." (5 words / 3.03s), natural cadence for a short outro. LOG-only. |
| 11 | type_check.py | PASS | GATE T: PASS (see TYPECHECK.md — B05 typography 0.67, others SKIP). |

## Envelope fixes applied
- Dropped `metadata.voice_id` (dead ElevenLabs id).
- Dropped `metadata.clock` prose (dead ElevenLabs-era text).
- Added `shot.form` on all 14 beats (`slide-a` / `simulation` / `scale-compare` / `data-chart`).
- `beat_sheet.pre-rebuild.json` written before any edit.

## Result
ALL CHECKS PASS. Cleared for review-slate compile.
