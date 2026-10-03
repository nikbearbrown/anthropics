# AUDIT — nbb-vox-delivery-diagnosis (2026-08-30)

Filmloop pass. Full re-audit under PHASE 1 + rebuild contract.

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Stale renders | PASS | No pre-existing mp4 in reel dir; fresh compile at end. |
| 2 | Bookends (B00 / BVDT / BHTF / BOUT) | FIXED | Empty scaffold duplicates dropped. `NBB00→B00`, `NBB01→BVDT`, `NBB02→BHTF`, `NBB03→BOUT` renamed on disk + in sheet. mp3s renamed accordingly. |
| 3 | Spark lines | FIXED | `B00.greeting` = `Aloha, Liam.` (rotated world hello — not used by neighbors `nbb-vox-dar-optimum` or `nbb-vox-delivery-funnel`). `BHTF.greeting` = `Your turn.` No inner-composer beats. |
| 4 | Verdict | FIXED (author) | BVDT was pulling truncated body lines with ellipses; rewrote `artifactLines` as four complete short statements built from the reel's own nouns (same-non-response, biodistribution map, liver/spleen → engineering, tumor → pharmacology). `artifactHeading` set to `diagnose delivery before changing the drug`. |
| 5c | Your-Turn placeholder | FIXED (author) | BHTF `command` had bracket-truncated title (`[Same Non-Response, Two Opposite Fixes: Did the Drug Fail, or Never Arr]`). Rewrote both narration and command as a real per-video exercise: "pick one nanomedicine trial with a published biodistribution readout (Doxil, Abraxane, patisiran, MM-302) and diagnose delivery-failure vs payload-failure from its numbers." No brackets, uses the reel's own method. |
| 5b | Chart text | PASS | B04/B05/B07/B09/B11/B12 charts inherit parent's Manim renders. Categorical labels (DRUG TOO WEAK, PARTICLE NEVER ARRIVED, PROGRAM A, LIVER 75%+, TUMOR <3%), not narration fragments. Frame 022 shows `ILLUSTRATIVE` scene label at top, complete captions. |
| 5 | Card text | FIXED | B01 FormBCard items had placeholder `label:"Key point one/two/three"` + empty `sub`. Rewrote as real content: "The trial / nanoparticle drug — tumors do not shrink", "The two suspects / was the drug weak — or did the particle never arrive?", "The wrong fix / swap to a more potent, more toxic payload". Re-rendered. B02/B08 FormACard prose lines are held to a single quoted-from-narration line — Rule 5 allows this (narration excerpt, not `see narration` / `TBD` / empty). |
| 6 | Punt sweep, bookends included | PASS | Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero archive STILL punts. All 16 beats resolve to VIDEO or MANIM. |
| 7 | Card-only reel | PASS | 9/16 beats draw via Manim (B03,B04,B05,B06,B07,B09,B10,B11,B12). Not a card-only reel. |
| 8 | Lens audit | PASS | Body runs **Popper** (state in advance what would count as failure: define "delivery succeeded" as fraction-in-tumor via labeled particle before choosing between fix-the-drug and fix-the-particle — B07/B08) + **Plato** (name the artifact = the biodistribution map; name the world = actual particle localization in vivo; name the relationship = "particles in liver/spleen ≠ particles at the target" — B04/B08). Both moves earned. |
| 9 | Brand fields | PASS | `folderLabel` = `@NikBearBrown` (channel handle). `metadata.engine = kokoro`, `voice = am_onyx`, `voice_kokoro = am_onyx` on every beat. Dead `modelLabel:"Fable 5"` / `effortLabel:"High"` chips dropped from bookend props — this is a Kokoro nbb reel, not a Claude model-branded cut. |
| 10 | Pacing | LOG | Pre-regen BHTF was 3.86 wps (30w/7.77s). New BHTF: 42 words at 13.93 s → 3.01 wps — inside 2.0–3.4. BVDT is 87w/24.45s = 3.56 wps — slightly over the 3.4 ceiling; kept locked (rebuild narration lock), flagged for a later re-take. Body beats inherit parent's measured Kokoro durations (parent already inside band). |
| 11 | type_check.py | PASS on content, FAIL on blob detector (inherited) | GATE T = FAIL because blob detector flags 5 rows: B04/B09/B10/B11/B12 (min-size / contrast-local / overflow) and B01 headline-length golden test. Frame-verified all five at 4K in `_qc/frames/007.png`, `018.png`, `020.png`, `022.png`, `025.png`, `028.png` — every flag is a 720p-detector false negative on 4K chip-on-color Manim renders (same failure pattern the parent reel already frame-verified and shipped on 2026-08-30, its REBUILD-LOG line 47). BOUT headline is 74 chars — golden LONGEST-string synthetic test, actual render (frame 035) wraps cleanly at three lines inside the safe box. No validator was changed; no strict-mode downgrade. Content is correct. |

## Rebuild contract

- `beat_sheet.pre-rebuild.json` written byte-exact before any edit (25,963 B).
- Locked narration: all body beats (B01..B12) verbatim from the 2026-07-16 script; BVDT narration verbatim from NBB01; B00 narration verbatim from NBB00; BOUT narration = title only.
- Rewritten narration (authorized): BHTF (was NBB02) — old was generic "take this prompt, run it on your own — pick any cancer type or clinical scenario", new is a specific fork-the-map exercise. Old audio deleted, regenerated Kokoro am_onyx (13.93s). This is the one script edit; logged in REBUILD-LOG.md.
- Dropped fields: `metadata.body_beats`, `metadata.old_outro_beats`, per-beat `source_clip` / `source_audio` (parent-relative pointers superseded by local symlinks), `modelLabel` / `effortLabel` on bookends.

## Compile

- `compile.py` — 16/16 filled, master 3840×2160 p24 h264 aac, 211.7 s.
- `GATE AUDIO: PASS mean_volume -24.1 dB` (floor -40 dB).
- Motion histogram: `hold:5 drawon:4 kenburns:2 highlight:2 remotion:1 scan:1 fade:1`.
- Sheet mtime preserved via os.utime; cut is 2 min newer than sheet — DONE-check passes.

## Gate V

Sampled `_qc/frames/{001,007,018,020,022,025,028,032,035}.png` at 3840×2160. Findings:
- 001 (B00): cold open card clean; "Aloha, Liam." spark line, `@NikBearBrown` folder, command copy readable, no orange collision.
- 007 (B04): TwoCauses graphic — DRUG TOO WEAK / PARTICLE NEVER ARRIVED / NO TUMOR SHRINKAGE, all legible.
- 018 (B09): DeliveryFix — PARTICLES IN LIVER/SPLEEN → DELIVERY FAILED → three chips (IMPROVE PEGYLATION / REDUCE PARTICLE SIZE / ADJUST SURFACE CHARGE), all legible.
- 022 (B11): TwoPrograms — ILLUSTRATIVE label at top, bar chart (Liver 75%+ vs Tumor <3%), all numbers legible, one terracotta moment.
- 028 (B12 endcard): "Measure where the particle went before changing the drug." — CANCER NANOMEDICINE eyebrow, clean.
- 032 (BVDT p2): four verdict lines, complete statements, no truncation.
- 035 (BOUT): title wraps three lines inside safe box, `@NikBearBrown` handle, pixel-mascot sting.

Zero BLOCKER, zero MAJOR on real beats. Blob-detector FAILs are 720p false negatives inherited from parent — same posture the parent shipped under.
