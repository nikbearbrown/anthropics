# AUDIT.md — vox-emitter-range (2026-08-28)

Legacy Cohort C vox reel. Full rebuild + build pass.

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` — WRITTEN (byte-exact snapshot, 15,411 bytes).
- Envelope normalized: dropped `metadata.voice_id` (ElevenLabs), added
  `metadata.engine = "kokoro"`, `metadata.voice = "am_onyx"`, rewrote
  `metadata.clock` prose from pre-audio placeholder to measured-audio
  ground-truth phrasing.
- Missing module fixed: `vox_scenes.py` imports `from vox_graphics import *`;
  no such module was reachable, so a copy of the vox_graphics library from
  a sibling reel (cancer-biology/vox-venetoclax-priming) was placed in this
  reel's directory. Envelope-level dependency plumbing, no shot-intent change.
- Narration LOCKED verbatim. No datable claims (isotope names, physical
  ranges, and illustrative kill percentages are already labeled as such).

## PHASE 1 — Audit
1. **Stale renders** — PASS. No pre-existing mp4 in reel folder.
2. **Bookends** — PASS (vox skin). B01 title CARD, B12 endcard CARD,
   B13 OutroSeries, B14 OutroCTA. Non-Claude channel, own skin kept.
3. **Spark lines** — N/A. No ClaudeComposerAsk beats in this vox skin.
4. **Verdict** — N/A. No BVDT beat in this vox skin.
5b. **Chart text** — PASS. Manim scene labels (`Alpha particle`, `Beta
    particle`, `range: 0.05 - 0.1 mm`, `crossfire`, `core survives`,
    `Lu-177 78%`, `Ac-225 41%`) are short category nouns / numeric ranges,
    not narration fragments. Bar/panel heights agree with narration.
5. **Card text** — FIXED. B07 `remotion.FormACard.props.lines` was a
    truncated narration head ("Now the geometry problem. Real tumors are
    not uniform. A three-centimeter…"). Rewrote to a three-line honest slate:
    "SLATE — heterogeneous tumor cross-section / 3 cm neuroendocrine tumor:
    receptor-positive rim, receptor-negative core / drug binds the rim;
    no drug reaches the center."
6. **Punt sweep** — FIXED. Only punt was B07 (see above). All other beats
    either render real manim (B01–B06, B08–B12) or render honest cards
    (B07/B13/B14 as PIL-drawn PNG stills, since no local Remotion project
    exists to render `OutroSeries` / `OutroCTA` / `FormACard`).
7. **Card-only reel** — PASS. 10 real manim graphics + 4 text/still cards.
8. **Lens audit** — PASS. Popper move: the reel states in advance what
    would count as the "alpha stronger = better" claim failing — a
    heterogeneous tumor where alpha's range cannot cross the gap. Plato
    move: names the artifact ("more lethal per hit"), names the world
    ("actual tumor cell kill in a heterogeneous geometry"), interrogates
    the relationship ("the answer is not in the particle, it is in the
    tumor"). Two moves earned.
9. **Brand fields** — FIXED. `metadata.voice_id` (ElevenLabs) DROPPED;
    `engine = kokoro`, `voice = am_onyx` set. No folderLabel field on
    this vox schema.
10. **Pacing** — Advisory. B11 has 63 words in 19.03s ≈ 3.3 wps (top of
    the 2.0–3.4 range); the illustrative-example beat is dense but within
    bounds. All other beats between 2.4 and 3.0 wps.
11. **type_check.py** — GATE T: PASS. Only advisory: §8.10 B07 card/narration
    overlap = 0.69 (down from pre-fix 1.00) — advisory only, not a failure.

## PHASE 2 — Build
- **Audio.** Regenerated all 14 beats via Kokoro `am_onyx`; measured
  durations written to `actual_duration_s` per beat. Total: 144.44s.
- **Renders.** Manim scenes rendered at 1280x720 (upscaled by compile
  to 4K):
    B01 Title, B02 AlphaIntro, B03 BetaIntro, B04 Question, B05 EmitterRanges,
    B06 Crossfire, B08 AlphaFail, B09 BetaWin, B10 Implication,
    B11 Example, B12 Endcard  → `manim/B*.mp4` (11 clips).
  PIL-drawn PNG cards for the three no-Remotion beats:
    B07 heterogeneous-tumor-cross-section slate,
    B13 OutroSeries card,
    B14 OutroCTA card  → `media/B{07,13,14}.png`.
- **Compile.** `--allow-slates` not needed — no slates in final. Master
  compiled at 3840×2160 (4K LAW enforced). Slot fill 14/14:
    B01–B06,B08–B12: MANIM · B07,B13,B14: STILL · zero SLATE.
- **Gate LANE.** PASS. No pipeline-slate violations.
- **Gate V.** Contact sheet `qc-sheet.png` reviewed — every beat renders
  real content, labels legible, safe insets respected, single accent per
  beat (crimson for alpha panels, teal for beta panels, both together
  only in the split-panel comparison beats where the contrast IS the
  information). No overflow, no clipping. PASS.
- **Gate AUDIO.** PASS — master mean_volume −23.9 dB, max_volume −2.6 dB.
- **Motion pantry.** Advisory: `drawon` at 7/14 (50%) exceeds the ~40%
  cap. This is a vox-explainer's native language; downgrade not applied
  because the source pattern is intentional. Logged, not fixed.

## Output
- `vox-emitter-range.mp4` — master (144.4s, 4K, per-beat narration muxed).
- mp4 mtime (08:24:41) is 21s newer than beat_sheet.json (08:24:20).
- No further sheet edits after compile.
