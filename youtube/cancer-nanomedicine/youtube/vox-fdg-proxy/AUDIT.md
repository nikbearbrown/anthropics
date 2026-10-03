# AUDIT.md — vox-fdg-proxy
_Filmloop pass: 2026-08-30. Non-claude vox reel (@NikBearBrown)._

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No mp4s existed at start; no stale renders to delete. |
| 2 | Bookends | N/A | Non-claude channel — keeps own vox skins (B01 title Manim, B12 endcard Manim, B13 OutroSeries Remotion, B14 OutroCTA Remotion). Rule 5 of rebuild contract: do not Claude-wash. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats in this vox reel. |
| 4 | Verdict | PASS | No BVDT beat. B12 endcard functions as a real recap drawn from the body ("A PET scan measures metabolism, not malignancy — imaging suggests, biopsy confirms.") — not a template placeholder. |
| 5c | Your-Turn placeholder | N/A | No BHTF beat. Non-claude reel closes with vox OutroCTA. |
| 5b | Chart text | PASS | Manim scenes reviewed — B04, B05, B08, B10 use short serif category labels (LabelChip / SerifLabel), no narration-slice bar labels. B05 arrow crossout is intentional and marked `_qc_intentional`. |
| 5 | Card text | FIXED | B02 & B09 FormACard fallbacks had lone truncated-with-ellipsis narration lines ("…for staging cancer and checking for…") — rewrote each as two authored short lines drawn from the locked narration. B06 same treatment. B03 section-card copy was a full-paragraph recital of the narration — tightened to a headline + real sub. B01 title, B12 endcard already had real copy + sub. |
| 6 | Punt sweep | FIXED | B02 and B09 were `STILL/ai` (gen-AI clip for a PET scan / a case referral note) — punt costumes per the nopunt catalog. Converted both to `CARD` with authored FormACard content. No `fill_slates`/`remotion_scenes` slates, no DoodleScene, no `STILL src=archive`, no gen-AI ask remains. |
| 7 | Card-only reel | PASS | 4 Manim mechanism/quote beats (B04, B05, B07, B08, B10, B11) plus title/endcard Manim (B01, B03, B12) — well above the "one drawn figure" floor. |
| 8 | Lens audit | PASS | Descartes ("The scan is technically correct. The diagnosis is completely wrong." — what would falsify the intuitive claim). Popper ("A dark scan is not an empty scan." — the falsifying case named). Plato (B08 flow diagram: SIGNAL → PROXY → BIOLOGY, plus the aphorism "imaging suggests, biopsy confirms" — artifact, world, relationship). Three moves stated; threshold is two. |
| 9 | Brand fields | FIXED | Added `channel: "@NikBearBrown"`, `folderLabel: "@NikBearBrown"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"` to metadata. Each beat received `voice: "am_onyx"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`. Also fixed B13 OutroSeries and B14 OutroCTA prop names to match the components' zod schemas (they were rendering with wrong props → default text "Part of the Claude Cowork series."). |
| 10 | Pacing | LOG | B03 measures 3.58 wps (30 words / 8.39 s) — above the 3.4 ceiling. Every other beat is inside 2.05–3.36 wps. Kept the narration; do not silently retime. |
| 11 | `type_check.py` | PASS | GATE T PASS, 0 FAILs. Two §8.10 advisories: B06 (0.92) and B09 (0.94) — narration recites the FormACard lines because the lines are compressed from the narration itself; acceptable per the §8.10 exception note (advisory, not blocking). |

## Blocked reels
None — all checks resolved without loosening a validator.

## Rebuild-specific notes
- `beat_sheet.pre-rebuild.json` was saved byte-exact BEFORE any edit.
- Narration is locked. No datable-claim edits were needed.
- The upstream `vox/aspects/explainer/vox-explainer/manim/` toolkit no longer
  exists on disk. `vox_graphics.py` was copied in from the `vox-emitter-range`
  sibling so `vox_scenes.py` could resolve `from vox_graphics import *` via the
  script directory on `sys.path`. All 9 Manim scenes rendered on the first try.
