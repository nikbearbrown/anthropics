# AUDIT.md — vox-batch-distribution (2026-08-28)

Legacy Cohort C vox reel. Full rebuild + build pass.

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` — WRITTEN (byte-exact snapshot, 16,017 bytes).
- Envelope normalized: dropped `metadata.voice_id` (ElevenLabs), added
  `metadata.engine = "kokoro"`, `metadata.voice = "am_onyx"`, rewrote
  `metadata.clock` prose from pre-audio placeholder to measured-audio
  ground-truth phrasing.
- Missing module fixed: `vox_scenes.py` imports `from vox_graphics import *`;
  no such module was reachable via the sys.path insert, so a copy of the
  vox_graphics library from the sibling reel `vox-emitter-range` was placed
  in this reel's directory. Envelope-level dependency plumbing, no shot-
  intent change.
- Narration LOCKED verbatim. No datable claims (all quantitative values
  are illustrative and labeled as such in FACTCHECK.md).

## PHASE 1 — Audit
1. **Stale renders** — PASS. No pre-existing mp4 in reel folder.
2. **Bookends** — PASS (vox skin). B01 title CARD, B12 endcard CARD,
   B13 OutroSeries, B14 OutroCTA. Non-Claude channel, own skin kept.
3. **Spark lines** — N/A. No ClaudeComposerAsk beats in this vox skin.
4. **Verdict** — N/A. No BVDT beat in this vox skin; verdict responsibility
   sits with B12's endcard summary + B09's document quote.
5b. **Chart text** — FIXED. B08 originally placed three region sub-labels
    ("rapid clearance / designed behavior / liver/spleen") on the same
    horizontal band under three close-set braces; the mid label overran
    the flanking labels. Fixed by shortening to single-noun tags
    ("clearance", "designed", "liver/spleen"), moving the mid group to
    a lower band, and bumping font_size back to 17/18 so no ligature
    rendering artifacts. Every other chart's axis and category labels
    are short category nouns / numeric chips (BATCH A PDI 0.07, BATCH B
    PDI 0.31, ~0.2 threshold, MATCH THE MEAN, MATCH THE DISTRIBUTION,
    tumor delivery: 100% / ~60%, ILLUSTRATIVE). All bar heights agree
    with narration meaning (batch A tight narrow spike, batch B wide bell).
5. **Card text** — FIXED. B02 remotion.FormACard.props.lines was a
    truncated narration head; replaced with an honest three-line slate.
    B12 endcard `sub` is "CANCER NANOMEDICINE" (topic, not a placeholder).
    All other card kind/copy/sub values name real content.
6. **Punt sweep** — FIXED. Only structural punt was B02 (see above); the
    Remotion pipeline is not present here, so B02/B13/B14 render as
    PIL-drawn still cards that name the artifact each beat needs.
7. **Card-only reel** — PASS. 11 real manim graphics + 3 slate cards.
8. **Lens audit** — PASS. Popper move: the reel states in advance what
    would count as the "same mean = same product" claim failing — the
    45min/6hr clearance gap between two batches carrying identical
    labels. Plato move: names the artifact ("a nanoparticle's average
    diameter"), names the world ("the actual population of particles
    hitting the tumor"), interrogates the relationship ("the average
    matches the center point of a distribution; matching the distribution
    is what proves the product"). Two moves earned.
9. **Brand fields** — FIXED. `metadata.voice_id` (ElevenLabs) DROPPED;
    `engine = kokoro`, `voice = am_onyx` set. No folderLabel field on
    this vox schema.
10. **Pacing** — Advisory. B11 has 90 words in 27.73 s ≈ 3.24 wps
    (upper end of the 2.0–3.4 range); the illustrative-example beat is
    dense but within bounds. B03 is 32 words in 9.45 s ≈ 3.39 wps —
    also within bounds. All other beats between 2.4 and 3.0 wps.
11. **type_check.py** — GATE T: PASS. Only advisory: §8.10 B02 card/
    narration overlap = 0.25 (short slate lines share vocabulary with
    the narration; below the 0.6 flag threshold).

## PHASE 2 — Build
- **Audio.** Regenerated all 14 beats via Kokoro `am_onyx`; measured
  durations written to `actual_duration_s` per beat. Total: 179.2 s.
- **Renders.** Manim scenes rendered at 1280×720 (upscaled by compile
  to 4K):
    B01, B03–B12 → `manim/B*.mp4` (11 clips).
  PIL-drawn PNG cards for the three no-Remotion beats:
    B02 two-vials slate, B13 OutroSeries, B14 OutroCTA
    → `media/B{02,13,14}.png`.
- **Compile.** `--allow-slates` present. Master compiled at 3840×2160
  (4K LAW enforced). Slot fill 14/14:
    B01, B03–B12: MANIM · B02, B13, B14: STILL · zero SLATE.
- **Gate LANE.** PASS. No pipeline-slate violations (Remotion patterns
  fulfilled by the PNG stills at their beat-id slot).
- **Gate V.** Contact sheet `_qc/qc-sheet.png` and per-second frames in
  `_qc/frames/` reviewed. First pass caught B08 sub-label horizontal
  overlap; fixed and re-rendered. Re-check clean. All other beats:
  labels legible, safe insets respected, single accent per beat (teal
  for batch-A / monodisperse / kept panels, crimson for batch-B /
  heterogeneous / lost panels, both together only in the intended
  side-by-side compares where the contrast IS the information; gold
  reserved for mean tick + editor's-pen highlight). Advisory: B10's
  right-panel histogram peak grazes the underline of the "MATCH THE
  DISTRIBUTION" chip's "I" letter — chip remains fully legible, not a
  BLOCKER or MAJOR. No overflow, no clipping.
- **Gate AUDIO.** PASS — master mean_volume −23.9 dB.
- **Motion pantry.** Advisory: `drawon` at 4/14 (29%) is under the
  ~40% cap. Motion histogram: drawon:4 hold:3 compare:3 fade:2
  kenburns:1 highlight:1 — balanced.

## Output
- `vox-batch-distribution.mp4` — master (179.2 s, 4K, per-beat narration
  muxed).
- mp4 mtime (13:16:13) is 22 s newer than beat_sheet.json (13:15:51).
- No further sheet edits after the final compile.
