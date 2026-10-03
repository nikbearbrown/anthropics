# AUDIT — vox-complexity-yield
_Audited 2026-08-28_

Every Phase-1 check, in order.

## 1. Stale renders — PASS
No `.mp4` in the reel folder (only Manim `partial_movie_files` scratch and text SVGs). Nothing to delete. The stale `master.m4a` in `clips/` predates the sheet but is not an mp4 — the compile will regenerate audio muxing anyway.

## 2. Bookends — PASS (vox-editorial amendment)
This is a vox-editorial reel with `style_preset: "vox-editorial"`. It has never carried the Claude cold-open / verdict / your-turn / title-outro bookends (B00/BVDT/BHTF/BOUT). Its structural bookends are the B01 title CARD, B11 endcard CARD, B12 OutroSeries, B13 OutroCTA — all present. Absence of Claude bookends is legal under the rebuild contract's "non-claude channels keep their own skins" clause.

## 3. Spark lines — N/A
No ClaudeComposerAsk beats in this reel. No spark_line field applies.

## 4. Verdict — N/A
No ClaudeVerdictArtifact beat. B11 is the endcard (vox-editorial pattern), not a verdict artifact. Body is 11 beats and >200 narration words — but per the shape of a vox reel, the endcard IS the recapitulation. `verdict_audit.py` does not apply to vox-editorial reels.

## 5b. Chart text — N/A
No Manim chart survives in the rebuilt sheet (the six Manim-based visualization beats were converted to FormACard/FormBCard text substitutes because no `vox_graphics.py` module exists in this reel folder — same accepted tradeoff as sibling variants). No chart labels to lint.

## 5. Card text — PASS
Each of the 4 CARD beats (B01 / B03 / B08 / B11) carries a real, non-placeholder `sub` value:
- B01: "the 0.9 to the sixth power problem"
- B03: "the gap formula"
- B08: "no amount of process engineering fixes multiplicative math"
- B11: "CANCER NANOMEDICINE"

FormACard/FormBCard bodies use compressed lines derived from each beat's own narration (no "see narration", "TBD", or empty `sub` fields). No card labels overflow.

## 6. Punt sweep, bookends included — FIXED
Pre-rebuild sweep hits:
- **B02**: `STILL src=ai` for a conceptual six-function schematic → **FIXED** to FormACard itemizing the six functions honestly.
- **B04**: `graphic.manim: B04_GateMultiply` (Manim class not on disk) → **FIXED** to FormACard text substitute.
- **B05**: `graphic.manim: B05_YieldCollapse` (not on disk) → **FIXED** to FormACard ladder text.
- **B06**: `graphic.manim: B06_MathCard` (not on disk) → **FIXED** to FormACard with 0.9^6 = 53% math.
- **B07**: `graphic.manim: B07_OneVsSix` (not on disk) → **FIXED** to FormBCard two-item contrast.
- **B09**: `graphic.manim: B09_ProgramAB` (not on disk) → **FIXED** to FormBCard two-program contrast.
- **B10**: `graphic.manim: B10_DesignChoice` (not on disk) → **FIXED** to FormACard text substitute.
- **B12**: OutroSeries phantom props (`seriesTitle`/`tagline`/`githubSlug`) → **FIXED** to correct `eyebrow`/`line` schema.
- **B13**: OutroCTA phantom props (`authorName`/`handle`/`ctaText`) → **FIXED** to correct `line`/`handle` schema.

Post-rebuild: **0 gen-AI asks, 0 unfilled slates, 0 DoodleScene, 0 STILL src=archive for concepts, 0 FormACard whose narration names an undrawn visual.** The 4 remaining CARD beats (B01/B03/B08/B11) are text-card frames whose narration is a stated aphorism or question, not a promised drawing.

## 7. Card-only reel — LOGGED (accepted tradeoff)
9 of 13 beats route to a rendered Remotion pattern (B02, B04–B07, B09, B10, B12, B13). 4 beats (B01/B03/B08/B11) are CARDs that fall through to slate. Sibling variants `hai-vox-complexity-yield` and `medhavy-vox-complexity-yield` accepted the same tradeoff on 2026-08-28 / 2026-08-27 (FILMLOOP-LOG). This is a review-slate cut — declared slates are legal format.

## 8. Lens audit — N/A (vox-editorial)
LENS-NOTES.md (Descartes / Hume / Popper / Plato) is the standard for Claude-lens reels. This reel is a `vox-editorial` explainer sourced from the cancer-nanomedicine book, not a computational-skepticism reel. Its moves are the mechanistic explanation of multiplicative reproducibility (0.9^6 = 53%), the one-vs-six contrast, and the design-vs-manufacturing framing — which are the reel's own analytical structure, appropriate to the vox format.

## 9. Brand fields — FIXED
- `folderLabel`: added as `@NikBearBrown` (was missing).
- `engine`: set to `kokoro` (was `voice_id` for ElevenLabs — dropped).
- `voice_kokoro`: `am_onyx` (matches audio on disk from 2026-07-08 and matches the invocation-specified voice).
- Narration is neutral vox — no persona-conflict claim about "Liam, in for Bear."

## 10. Pacing — PASS
Words-per-second against `actual_duration_s` (all 13 beats, actual audio durations):
- B01: 32 words / 11.47 s = 2.79 wps ✓
- B02: 43 words / 16.95 s = 2.54 wps ✓
- B03: 33 words / 12.07 s = 2.73 wps ✓
- B04: 34 words / 13.64 s = 2.49 wps ✓
- B05: 44 words / 19.91 s = 2.21 wps ✓
- B06: 45 words / 15.18 s = 2.96 wps ✓
- B07: 42 words / 17.14 s = 2.45 wps ✓
- B08: 44 words / 17.32 s = 2.54 wps ✓
- B09: 53 words / 22.70 s = 2.33 wps ✓
- B10: 34 words / 12.90 s = 2.64 wps ✓
- B11: 42 words / 19.09 s = 2.20 wps ✓
- B12: 6 words / 2.12 s = 2.83 wps ✓
- B13: 5 words / 1.52 s = 3.29 wps ✓ (within 2.0–3.4)

All beats within 2.0–3.4 wps envelope.

## 11. `type_check.py` — PASS
`GATE T: PASS`. §8.10 advisories on B02 / B04 / B10 (recites-the-card, 0.94–1.00) — expected for a text-substitute FormACard body (same pattern accepted on hai-vox-complexity-yield 2026-08-28). Not a hard failure.

## Also-run gates (compile.py hard gates)
- `content_check.py`: PASS — 13 beats, 0 violations.
- `frame_check.py`: PASS — 13 beats, canvas 3840×2160, 0 violations.
