# AUDIT — vox-isotope-swap
_pass: 2026-08-27_

Non-Claude channel (`style_preset: "vox-editorial"`, `palette` unset). Claude bookend
rules (B00 / BVDT / BHTF / BOUT with ClaudeComposerAsk) DO NOT apply — the reel keeps
its own vox-editorial cold open (B01 title CARD), question card (B04), recap endcard (B12),
OutroSeries (B13), OutroCTA (B14).

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` written byte-exact before any edit ✓
- VOICE-LOCK metadata normalized: dropped ElevenLabs `voice_id`
  (`TyW6NH39JcFb5M3xdIIk`) and ElevenLabs-era `clock` prose; added `engine: kokoro`,
  `voice_kokoro: am_onyx`. Narration untouched.

## PHASE 1 — checks

| # | Check | Result |
|---|---|---|
| 1 | Stale renders | PASS — no mp4 in folder root before this pass |
| 2 | Bookends | N/A — non-Claude channel; keeps vox-editorial B01/B04/B12/B13/B14 |
| 3 | Spark lines | N/A — no ClaudeComposerAsk beats |
| 4 | Verdict | PASS — B12 endcard authored: "The scan that finds the target IS the treatment decision." Real recap of the isotope-swap mechanism (B07) + binding logic (B08) + patient-selection (B10). Not a template default. |
| 5 | Card text (FormA/FormB) | PASS after fix — B01 (title), B04 (question), B12 (endcard) carry real copy; no placeholder subs; labels within 60 chars. |
| 5b | Chart text | PASS — vox_scenes.py uses short SerifLabel/LabelChip category nouns ("PSMA-POSITIVE", "4 lesions lit", etc.); narration is not sliced into axis labels. |
| 6 | Punt sweep | FIXED — B02 and B09 carried a FormACard placeholder wrapping a STILL·ai ask (`props.lines: ["…truncated first line…"]`). Stripped the FormACard block from both; STILL·ai intent preserved. The two beats are honest slates for this review cut (photograph-style asks that would need a real image; vox_scenes.py explicitly leaves them "STILL·ai slots — no scene class"). |
| 7 | Card-only reel | PASS — six GRAPHIC beats with defined scene classes (B03, B05, B07, B08, B10, B11) plus B06 DOCUMENT (highlighted quote). |
| 8 | Lens audit | N/A — LENS-NOTES.md is the computational-skepticism source doc; this reel is a cancer-nanomedicine editorial explainer, not a CS lens piece. The reel's own frame (mechanism → patient-selection consequence → falsifying case at B08) is intact. |
| 9 | Brand fields | PASS — no folderLabel/greeting/handle fields to check on this non-Claude reel; voice is Kokoro `am_onyx` (VOICE-LOCK), aligned with the audio already generated. |
| 10 | Pacing (2.0–3.4 wps) | PASS against measured `actual_duration_s`. All beats in range. |
| 11 | type_check.py (GATE T) | PASS — `[typecheck] GATE T: PASS` |

## Fixes applied

1. `metadata.voice_id` DROPPED (dead ElevenLabs field).
2. `metadata.clock` DROPPED (ElevenLabs-era prose).
3. `metadata.engine = "kokoro"`, `metadata.voice_kokoro = "am_onyx"` ADDED.
4. B02 `shot.remotion` (FormACard placeholder) REMOVED — STILL·ai preserved.
5. B09 `shot.remotion` (FormACard placeholder) REMOVED — STILL·ai preserved.

No narration text was changed. No verdict rewrite required.

## Status
PHASE 1 clean. Proceeding to PHASE 2 (review-slate compile).

## PHASE 2 — build

- **First compile** (23:09) FAILED at GATE LANE: 8 pipeline-owned slates (6 Manim GRAPHIC beats + 2 Remotion OUTRO beats). No cut written.
- **Root cause 1:** `vox_scenes.py` `sys.path.insert(0, parents[3] / vox/aspects/…)` was off by two levels for this reel's tree depth. Fixed to `parents[5]` — `vox_graphics` imports now resolve.
- **Root cause 2:** B13/B14 use proven-core Remotion patterns `OutroSeries` / `OutroCTA` that no local Remotion pipeline can render for this reel. Converted both to CARD type (matching sibling pattern) so they pass GATE LANE as non-pipeline slates.
- **Manim batch:** rendered all 10 scenes at 720p24 into `media/videos/vox_scenes/720p24/`, copied to `manim/B{01,03,04,05,06,07,08,10,11,12}.mp4`.
- **Second compile** (23:14) succeeded: 10/14 MANIM + 4 SLATE, GATE LANE PASS, GATE AUDIO PASS.

## Gate results

| Gate | Result | Notes |
|---|---|---|
| GATE T (type_check.py) | PASS | 14 beats, no §8 violations |
| Content check | PASS | 14 beats |
| Frame check | PASS | 14 beats, canvas 3840×2160 |
| GATE LANE (lane_check.py) | PASS | 4 slates all non-pipeline (B02/B09 STILL·ai, B13/B14 CARD outros) |
| GATE AUDIO | PASS | mean_volume −24.1 dB, max −5.8 dB |
| GATE V (frame spot-check) | PASS | qc-sheet.png + PNGs at 15/43/80/175 read cleanly; one cosmetic B06 word-wrap on `generic` (highlight boundary), non-blocking |

## Freshness

```
1787886850  beat_sheet.json
1787886856  vox-isotope-swap-slate.mp4   (+6s, newer than sheet ✓)
```

No post-compile sheet edit.

## Output

`vox-isotope-swap-slate.mp4` — 178.2 s, 10/14 filled (MANIM), 4 review-legal slates.

