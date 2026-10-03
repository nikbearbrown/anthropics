# AUDIT — claude-liam-vox-complexity-yield
_2026-08-28 (unattended film factory)_

Output: `vox-complexity-yield-slate.mp4` (222.2 s, 3840×2160, mean_volume −27.5 dB).
14/17 beats rendered real; 3 honest slates (B03, B08, B11) as declared card beats.

## Phase 0 — rebuild contract
- `beat_sheet.pre-rebuild.json` created byte-exact (cksum match) BEFORE any edit.
- Envelope normalized: dropped dead `voice_id` (ElevenLabs) and legacy `clock` prose.
- Voice envelope confirms Kokoro `am_onyx` with narration "Liam, in for Bear."
- Non-claude outros B12/B13 (OutroSeries/OutroCTA) left in place — this reel carries
  BOTH the vox legacy outros and the anthropics lens BVDT/BHTF/BOUT bookends;
  reordering is a scripting choice for a future rebuild, not this pass.

## Phase 1 — audit
| # | Check | Result | Note |
|---|-------|--------|------|
| 1 | Stale renders | PASS | no orphaned mp4s from before this sheet mtime |
| 2 | Bookends | FIXED | B00/BVDT/BHTF/BOUT patterns present; verdict authored |
| 3 | Spark lines | FIXED | B00 was bare "Liam" — set to "Guten tag, Liam." (unused by adjacent reels: Aloha, Bonjour, Ciao, Hej, Hola, Kia ora, Konnichiwa, Merhaba, Namaste, Salaam, Sawubona). BHTF "Your turn." already correct. |
| 4 | Verdict | FIXED | Was `Key finding one/two/three` template + empty narration → authored 3 real lines and 55-word narration from the body's nouns/numbers. Second-pass fix: line 1 started with "0.9^6" which the ClaudeVerdictArtifact renderer stripped as ordinal marker; rewrote as "Six functions at 90% reproducibility multiplies to 53% batch pass." then re-rendered + recompiled. |
| 5 | Card text (B01) | FIXED | FormBCard had `Key point one/two/three` with empty `sub` — authored 3 items ("The particle / The paper / The batches") with real subs from B01 narration. |
| 5b | Chart text | PASS | Manim charts use SHORT category nouns (F1–F6, 90%, PASS, 53%) and captions are complete sentences. |
| 6 | Punt sweep | PASS | zero gen-AI asks, zero unfilled slates in bookends, zero FormA card promising an undrawn visual. B02 STILL src=ai is delivered as a FormACard Remotion render. |
| 7 | Card-only reel | PASS | 6 body beats are Manim (drawn), plus 5 Remotion, 3 declared slate cards. |
| 8 | Lens audit | PASS | Popper: falsification stated in advance (raise per-function yield to 95%: still 26% batch loss). Descartes: what would falsify the multiplicative model (a design where the six functions are independent post-hoc, not multiplicative gates). Two moves earned. |
| 9 | Brand fields | PASS | `folderLabel: @NikBearBrown`, `engine: kokoro`, `voice_kokoro: am_onyx`; persona matches "Liam, in for Bear." |
| 10 | Pacing | LOG | B05 estimated 12s for 54 words = 4.5 wps target, but Kokoro measured 14.57s = 3.71 wps (edge of 2.0–3.4 band). Not silently retimed — flagged for later trim of "Two: eighty-one percent. A third:" sequence. |
| 11 | type_check | (not run) | GATE CONTENT and GATE FRAME in compile.py both PASS on 17 beats; GATE LANE PASS; GATE AUDIO PASS. |

## Phase 2 — build
- Audio: BVDT generated with `generate_audio_kokoro.py --only BVDT` (19.29 s, am_onyx). B00/BHTF/BOUT bookends carry their own Remotion audio; NEVER-STRIP LAW respected.
- Rendered 8 Remotion beats (B00, B01, B02, B12, B13, BVDT, BHTF, BOUT) via `remotion_scenes.py`.
- Authored `scenes_std.py` with 6 Manim scenes: B04_GateMultiply, B05_YieldCollapse, B06_MathCard, B07_OneVsSix, B09_ProgramAB, B10_DesignChoice. Rendered all six at 720p24; moved to `manim/Bxx.mp4`.
- B03, B08, B11 are CARD beats with no drawable spec — declared slates. lane_check confirms these are NOT pipeline-owned, so no PIPELINE-SLATE-IN-CUT violation. Slates render honest request cards with the beat's narration prompt.
- Compiled with `--review` → `vox-complexity-yield-slate.mp4`. GATE LANE PASS. GATE AUDIO PASS. mean_volume −27.5 dB.
- Gate V: sampled 444 QC frames at 2 fps. Spot-checked B00 (composer widget clean), B04 (six gates + PASS bucket), B05 (yield collapse bar chart with 90% reference line), B06 (0.9^6 = 53% with gold highlight, 0.95^6 = 74% secondary), B07 (one-vs-six teal/crimson contrast), B09 (12-square grids), B10 (design-choice annotation ring), B11 (honest slate), BVDT (verdict with corrected line 1), BHTF (Your turn spark), BOUT (title outro with bear mascot). No text overflow, no SAFE-inset violations, no duplicate terracotta on real beats.

## Build stamp
```
14/17 filled — B00:VIDEO B01:VIDEO B02:VIDEO B03:SLATE B04:MANIM B05:MANIM B06:MANIM B07:MANIM B08:SLATE B09:MANIM B10:MANIM B11:SLATE B12:VIDEO B13:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO
```

## Files touched
- `beat_sheet.pre-rebuild.json` (new)
- `beat_sheet.json` (envelope + BVDT + B00 + B01 + then BVDT line-1 fix)
- `scenes_std.py` (new, 6 scenes)
- `mp3/beat-BVDT.mp3` (new)
- `media/B00.mp4 B01.mp4 B02.mp4 B12.mp4 B13.mp4 BVDT.mp4 BHTF.mp4 BOUT.mp4` (new)
- `manim/B04.mp4 B05.mp4 B06.mp4 B07.mp4 B09.mp4 B10.mp4` (new)
- `clips/*.mp4` (recompiled) + `clips/master.m4a` (regenerated)
- `vox-complexity-yield-slate.mp4` (new, newer than sheet)
- `qc-sheet.png` (regenerated)
