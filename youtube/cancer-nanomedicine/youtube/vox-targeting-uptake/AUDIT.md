# AUDIT.md — vox-targeting-uptake (2026-08-28)

Legacy Cohort C vox reel. Full rebuild + build pass.

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` — WRITTEN (byte-exact snapshot, 14,009 bytes).
- Envelope normalized: dropped `metadata.voice_id` (ElevenLabs), added
  `metadata.engine = "kokoro"`, `metadata.voice = "am_onyx"`, rewrote
  `metadata.clock` prose from pre-audio placeholder to measured-audio
  ground-truth phrasing.
- Missing module fixed: `vox_scenes.py` imports `from vox_graphics import *`;
  no such module was reachable from the reel folder relative path used
  in the header (walks four parents into a nonexistent `anthropics/vox/`),
  so a copy of the vox_graphics library from `books/vox/aspects/explainer/vox-explainer/manim/`
  was placed in this reel's directory. Envelope-level dependency plumbing,
  no shot-intent change.
- Narration LOCKED verbatim. No datable claims. B09 example numbers are
  labeled "illustrative" in the production_viz mechanic.

## PHASE 1 — Audit
1. **Stale renders** — PASS. No pre-existing mp4 in reel folder to purge.
2. **Bookends** — PASS (vox skin). B01 title CARD, B10 endcard CARD,
   B11 OutroSeries, B12 OutroCTA. Non-Claude channel, own skin kept.
3. **Spark lines** — N/A. No ClaudeComposerAsk beats in this vox skin.
4. **Verdict** — N/A. No BVDT beat in this vox skin.
5b. **Chart text** — PASS. Manim scene labels are short category nouns
    ("BLOOD", "VESSEL WALL", "TUMOR TISSUE", "CELL SURFACE", "TARGETED",
    "UNTARGETED", "TUMOR", "ACCUMULATION", "UPTAKE") and numeric % values
    (2.1%, 1.9%, 68%, 12%). Bar heights agree with narration meaning:
    equal accumulation bars ~equal; internalization bars very different
    (68% >> 12%), matching "same tumor, different cell entry."
5. **Card text** — FIXED. B02 `remotion.FormACard.props.lines` was a
    truncated narration head ("The antibody works beautifully in the lab.
    The tumor data tells…") — obvious placeholder AND caused §8.10
    recite-the-card warning (1.00 ratio). Rewrote to a three-line honest
    slate that names the artifact this beat needs:
    "SLATE — two petri dishes, targeted vs untargeted / left dish: dense
    teal dots bound to cancer cells / right dish: sparse teal dots, no
    ligand". Post-fix §8.10 ratio = 0.06 (PASS).
6. **Punt sweep** — PASS after B02 fix. Only punt was B02 (see above).
    All other beats render real manim scenes (B01, B03–B10) or honest
    PIL-drawn PNG slates for outros (B02/B11/B12 have no Remotion project
    locally, so the review cut uses honest slates).
7. **Card-only reel** — PASS. 9 real manim graphics + 3 slate cards.
8. **Lens audit** — PASS. Popper move: the reel states in advance what
    would count as "targeting works in the tumor" failing — a matched
    two-batch experiment where targeted and untargeted show identical
    tumor accumulation. B09 delivers exactly that test with the folate
    example. Plato move: names the artifact ("cellular uptake in a dish"),
    names the world ("total tumor accumulation in an animal"), interrogates
    the relationship ("uptake ≠ accumulation because the ligand acts last").
    Two moves earned.
9. **Brand fields** — FIXED. `metadata.voice_id` (ElevenLabs) DROPPED;
    `engine = kokoro`, `voice = am_onyx` set. This vox schema has no
    `folderLabel` field (non-Claude channel skin).
10. **Pacing** — Advisory. All beats within 2.0–3.4 wps:
    B01 30w/10.58s=2.83 · B02 27w/8.80s=3.07 · B03 26w/9.20s=2.83 ·
    B04 32w/13.64s=2.35 · B05 32w/12.20s=2.62 · B06 32w/10.68s=3.00 ·
    B07 27w/9.46s=2.85 · B08 32w/10.03s=3.19 · B09 33w/18.94s=1.74 (B09
    below the 2.0 floor — dense-number example beat with intentional beat
    pauses on the % pairs; logged, not fixed).
11. **type_check.py** — GATE T: PASS. Zero FAILs. §8.10 advisory cleared
    after B02 card fix (1.00 → 0.06).

## PHASE 2 — Build
- **Audio.** Existing mp3/beat-B01..B12.mp3 reused (all narration LOCKED,
  actual_duration_s already populated per beat). No regeneration needed.
  Master mean_volume = −24.3 dB (well above the −40 dB gate).
- **Renders.** 9 manim scenes rendered at 1280x720 via
  `VOX_PALETTE=newsprint python3 -m manim -qm --fps 24 -r 1280,720
  vox_scenes.py <SceneClass>`:
    B01 Title, B03 Question, B04 DeliveryChain, B05 CultureVsBody,
    B06 AccumulationDrivers, B07 LastStep, B08 WrongFix,
    B09 FolateExample, B10 End → `manim/B*.mp4`.
  PIL-drawn PNG slate cards for the three beats without a Scene class:
    B02 (STILL·ai — petri dishes photo slot),
    B11 (OutroSeries),
    B12 (OutroCTA) → `media/B{02,11,12}.png`.
- **Compile.** `brutalist-art/runtime/scripts/compile.py --review --height 720
  --fps 24 --allow-slates`. Slot fill 12/12:
    B01,B03-B10: MANIM · B02,B11,B12: STILL · zero SLATE.
- **Gate LANE.** PASS. No pipeline-slate violations.
- **Gate V.** Contact sheet `qc-sheet.png` reviewed frame-by-frame, plus
  per-beat mid/end frames pulled to `_qc/frames/`.
  FIRST PASS FOUND:
    B05 — annotation "steps 1-3 unmeasured in culture" ran off the right
    edge (BLOCKER). Fixed in `vox_scenes.py::B05_CultureVsBody`: shortened
    label to "steps 1-3 unmeasured" and repositioned from RIGHT-of-ring
    to DOWN-of-right-column, keeping it inside the SAFE inset.
    B07 — UNTARGETED chip stacked on the untargeted particle dot AND
    "stays in interstitium" label ran through the chip (MAJOR). Fixed in
    `vox_scenes.py::B07_LastStep`: moved the UNTARGETED chip to UP*0.4
    above its dot (matching TARGETED's chip position), and removed the
    redundant mid-tissue "same arrival" label (the bottom annotation
    "same amount arrives, different cell entry" already states the point).
  Re-rendered B05 and B07 → re-compiled → re-QC'd end frames. Both clean.
  SECOND PASS: zero BLOCKER, zero MAJOR on real beats. PASS.
- **Gate AUDIO.** PASS — master mean_volume −24.3 dB.
- **Motion pantry.** Advisory: `drawon` at 7/12 (58%) exceeds the ~40%
  cap. This is a vox-explainer's native language; downgrade not applied
  because the source pattern is intentional. Logged, not fixed.

## Output
- `vox-targeting-uptake-slate.mp4` — review cut (119.2s, 720p, per-beat
  narration muxed).
- mp4 mtime (16:30:37) is 4s newer than beat_sheet.json (16:30:33).
- No further sheet edits after compile.

