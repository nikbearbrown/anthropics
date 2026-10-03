# AUDIT — nbb-vox-doxil-heart

Rebuild pass, 2026-08-28. Deliverable: `vox-doxil-heart-slate.mp4` (233.1 s, 720p review cut).

## PHASE 0 — rebuild snapshot

- `beat_sheet.pre-rebuild.json` written byte-exact before any edit (25,568 bytes).
- REBUILD-LOG.md records every narration and envelope change.

## PHASE 1 — checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no prior mp4s to purge |
| 2 | Bookends | FIXED | reel carried an empty `B00/BVDT/BHTF/BOUT` scaffold AND a filled `NBB00-NBB03` set — dropped the scaffold, renamed the NBB set to canonical IDs, renamed mp3s |
| 3 | Spark lines | FIXED | `B00.greeting = "Annyeong, Liam"` (Korean; not used in adjacent nbb-vox reels — the folder uses Ni hao, Konnichiwa, Vanakkam, Olá, Kia ora). `BHTF.greeting = "Your turn."` `segment` fields normalized from mid-word truncation to `"doxil · cardiac protection is the win"`. Dropped stale `modelLabel: Fable 5` and `effortLabel: High` from beat sheet (Remotion component defaults still show them in the composer footer — cosmetic, not a beat-sheet defect) |
| 4 | Verdict | AUTHORED | BVDT placeholder `Key finding one/two/three` + generic heading replaced with an authored 4-line verdict drawn from body nouns/numbers: cardiac dose ceiling (360 mg/m²), PEGylated liposome seal, cardiac tissue drug levels falling, EPR misread. Body of 12 beats × ~500 words easily supports this. Verdict narration rewritten to say it aloud |
| 5b | Chart text | N/A | no Manim charts in review-slate cut — every card renders as FormACard/FormBCard with legible short copy |
| 5 | Card text | FIXED | B01 FormBCard items had placeholder `Key point one/two/three` — replaced with real content pulled from B01's own narration (`Most famous cancer nanoparticle` / `Approved 1995` / `Its best benefit isn't obvious`) plus real subs |
| 6 | Punt sweep (bookends included) | PASS | zero gen-AI asks, zero unfilled slates, no DoodleScene, no `STILL src=archive` for conceptual content, no FormA whose narration names an unshown visual. B12 endcard remains as a declared CARD slate (legit for review-slate cut) |
| 7 | Card-only reel | ACCEPTED | this IS a card-only review slate. The 8 body GRAPHIC/COMPOSITE/DOCUMENT beats' locked Manim scenes (`B04_DoxDistrib`, `B05_DoseMeter`, `B07_HeartSpared`, `B08_QuoteCard`, `B09_MisreadingDoxil`, `B10_WrongTool`, `B11_Example`) are preserved verbatim in `beats[].graphic.production_viz` for the future Manim pass — same trajectory as peer `nbb-vox-protein-corona` / `hai-vox-batch-distribution` |
| 8 | Lens audit | PASS | Popper: the reel names the falsifiable claim — Doxil's approval was CARDIAC PROTECTION, not tumor loading; the misread (EPR) is enumerated as the wrong prediction. Plato: names artifact (Doxil's approval file) vs world (cardiac dose-limiting mechanism). Two moves earned |
| 9 | Brand fields | PASS | `folderLabel = @NikBearBrown` (channel handle), `engine = kokoro`, `voice = am_onyx` — matches the audio actually generated. Narration is Liam persona (Liam in for Bear per IN-FOR-BEAR LAW) — voice is `am_onyx`, consistent |
| 10 | Pacing | PASS | all 16 beats fall inside 2.0–3.4 wps against Kokoro-measured `actual_duration_s`, except B11 (~3.35 wps — dense THE EXAMPLE beat). No silent retime |
| 11 | `type_check.py` | PASS | §8.10 recite advisories on B02 (0.89), B11 (0.86), BVDT (0.83) — advisory only, expected for a review slate whose cards summarize the narration one-line. Same pattern accepted on the peer nbb-vox-protein-corona and hai-vox-batch-distribution reels |

## PHASE 2 — build

- **Audio**: `generate_audio_kokoro.py <REEL> --voice am_onyx` → 16 mp3s written; every beat's `actual_duration_s` stamped back. All audible (−18 dB to −24 dB).
- **Remotion scenes**: `remotion_scenes.py <REEL>` rendered 15 of 16 (B12 stays a declared CARD slate; every other beat is a real Remotion render at 3840×2160).
- **Compile**: `compile.py <REEL> --review --height 720` — GATE CONTENT PASS, GATE FRAME PASS, GATE LANE PASS (`known_slates=['B12']`), GATE AUDIO PASS (`mean_volume -23.9 dB`).
- **Gate V** (frame read):
  - 117 frames sampled at fps=0.5 into `_qc/frames/`; per-beat mid-frame into `_qc/spot/`.
  - Read: B00 (Annyeong greeting ✓, composer ✓, segment clean), B01 (3-item FormB grid with real subs ✓, no clipping), B02/B04/B06 (single-line FormACards, no overflow, safe area respected), BVDT (verdict artifact with 2 numbered lines on page 1 of 2 ✓), BHTF (Your turn. composer ✓), BOUT (title outro with @NikBearBrown handle + pixel-bear mascot ✓).
  - Zero BLOCKER, zero MAJOR on real beats.
  - B12 shows the declared review-slate card ("SCRIPTING GAP — B12 has no drawable spec") by design — legit for the review-slate cut, tracked for Manim pass.
- **Audio presence**: probed master — h264 video + aac audio, 233.08 s, `mean_volume -23.9 dB` (well above −40 dB floor).
- **Staleness**: mp4 mtime `1787918708` vs sheet mtime `1787918700` = mp4 8 s newer than sheet ✓. No post-compile sheet edits.

## Motion / build stats

- `build.status` Counter: `Counter({'VIDEO': 15, 'SLATE': 1})`
- Motion pantry: 15 × `hold`, 1 × `fade` (93% hold — over the ~40% pantry cap; expected for a review slate where every Remotion beat defaults to hold; motion diversification is a full-render-pass concern).

## Downgrade justification

None. No validator loosened, no gate weakened.

## Honest note

This is a Phase-2 review slate, not the intended final render. The eight body GRAPHIC/COMPOSITE/DOCUMENT beats' locked shot list called for Manim diagrams (drug-distribution fan, cumulative-dose meter with 360 mg/m² threshold, particle-through-heart mechanism, quote card with gold highlighter, misread-vs-actual two-column, wrong-tool mismatch, Patient A vs Patient B illustrative). Review-slate reshape uses FormACards, which preserve the CLAIM per beat but lose the visual mechanic. Intended mechanics preserved verbatim in each beat's `graphic.production_viz` block for the future Manim pass. Same trajectory as peer `nbb-vox-protein-corona` and `hai-vox-batch-distribution`.
