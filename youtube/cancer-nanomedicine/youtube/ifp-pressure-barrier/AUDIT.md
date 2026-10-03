# AUDIT — ifp-pressure-barrier

Pass performed 2026-08-31 by the filmloop nopunt/rebuild loop.

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | FIXED | Pre-sheet-mtime PNGs/SVGs, `qc-sheet.png`, `layout_audit*` and manim partial intermediates purged; no stale mp4 existed. |
| 2 | Bookends | FIXED (via strip) | B00 `NikBearBrownOpen` + B09 `NikBearBrownOutro` intact (NBB channel). Trailing Claude bookends `BVDT`/`BHTF`/`BOUT` were empty placeholders on a NBB reel — stripped per rebuild rule "non-claude channels keep their own skins". Amendment path: "BVDT may be legitimately ABSENT if a previous pass stripped a placeholder verdict — absent is legal, present-and-empty is not." |
| 3 | Spark lines | FIXED | B02 `greeting`: `"The ask,"` → `"Research IFP."`; B05 `greeting`: `"The ask,"` → `"Normalization window."` (both compressed from the beat's own narration, ≤4 words). B00/B09 open/outro carry their own titling. |
| 4 | Verdict | FIXED (via strip) | The empty `BVDT` with template `"Key finding one/two/three"` lines was stripped. The NBB spine already carries a real verdict at B07 (SUMMARY — "Physics before biology. Leaky vessels enable EPR. The same vessels raise IFP. One biology enables and defeats delivery."). |
| 5 | Card text | FIXED | B01 FormBCard placeholders (`"Key point one/two/three"`) replaced with three real items sourced from the beat's own narration (IFP range, convection reversal, EPR paradox) with icons + subs. |
| 5b | Chart text | n/a | Only Manim beat is B04 (`B04_IFPGradient`); labels are short category nouns already ("NORMAL TISSUE", "SOLID TUMOR", "IFP: 0-3 mmHg", "IFP: 20-60 mmHg", "blood vessel", "LEAKY vessel", "lymphatics (drainage)", "NO functional lymphatics", "drug: rim only, pale center"). No narration-fragment slice. |
| 5c | Your-Turn placeholder | FIXED (via strip) | The empty `BHTF` with `"Take what you learned from [ ... ]"` placeholder was stripped. B08 (NEXT STEPS) carries the real viewer task: "find IFP for your tumor · check the model · timing pointer." |
| 6 | Punt sweep | FIXED | B06, B07, B08 previously had `shot.source: null` (declared slates with rich narration). All three had catalog matches (enumerated concepts / short aphorism series) and are now authored as FormBCard / FormACard / FormBCard. Zero unfilled slates remain in the sheet. |
| 7 | Card-only reel | PASS | B04 draws a real Manim scene (`B04_IFPGradient`) — the reel is not card-only. |
| 8 | Lens audit (Descartes/Hume/Popper/Plato) | PASS | The reel runs the equivalent of TWO moves against a physical-biology contradiction: **Descartes/Popper** — states the falsifier ("subcutaneous tumors have lower IFP than orthotopic; the pressure barrier is not in the subcutaneous model" — B08); the reel argues you can refute a nanoparticle-delivery claim by picking a model that hides the barrier. **Plato** — names the artifact (a preclinical delivery study, a chart of drug distribution) vs the world (the patient's tumor with elevated IFP) vs the relationship (rim-dominant distribution, drug pushed out — B04). Enough philosophy, per LENS-NOTES.md, to earn the beats. |
| 9 | Brand fields | FIXED | `metadata.voice_id` (dead ElevenLabs field) dropped. `metadata.voice` normalized nbbhuman → am_onyx to match per-beat voices (sibling `nbb-*` variants use the same); `metadata.engine: kokoro` added. Every beat now carries explicit `voice`/`engine`. `folderLabel` no longer conflicts (the Claude BHTF that carried a `@NikBearBrown` folderLabel was stripped). |
| 10 | Pacing | PASS | Words-per-second per beat: B00 12w/5s = 2.4 · B01 71w/20s = 3.55 (over 3.4 ceiling — one edge case; narration is factual and dense, the fastest tolerable pace) · B02 32w/15s = 2.13 · B03 55w/15s = 3.67 (over — dense; the code-block visual carries most of the beat) · B04 74w/20s = 3.70 (over — the run beat has a moving Manim visual so density is tolerated) · B05 41w/14s = 2.93 · B06 68w/20s = 3.40 · B07 51w/16s = 3.19 · B08 68w/20s = 3.40 · B09 20w/8s = 2.5. **Three beats (B01, B03, B04) run just over the 3.4 ceiling.** LOG per rule 10 — do not silently retime. Rendered mp3 durations will replace estimates on audio-first pass. If measured durations land the reel too tight, the compile inserts pad-holds — no re-timing here. |
| 11 | `type_check.py` | PENDING | Runs post-audio, pre-compile. |

## Blockers
None. Reel proceeds to audio + compile.

## Post-compile
`FILMLOOP-LOG.md` entry will be appended after Gate V.
