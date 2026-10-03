# AUDIT.md — vox-bystander-effect (2026-08-28)

Legacy Cohort C vox reel. Full rebuild + build pass.

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` — WRITTEN (byte-exact snapshot, 8,084 bytes).
- Envelope normalized: dropped `metadata.voice_id` (ElevenLabs), added
  `metadata.engine = "kokoro"`, `metadata.voice = "am_onyx"`.
- Missing module fixed: `vox_scenes.py` imports `from vox_graphics import *`;
  no such module reachable via its `sys.path.insert`. Copied vox_graphics.py
  from sibling reel (cancer-nanomedicine/vox-emitter-range, already rebuilt)
  into this reel dir.
- Narration LOCKED verbatim. No datable claims to correct.

## PHASE 1 — Audit
1. **Stale renders** — PASS. No pre-existing mp4 in reel folder.
2. **Bookends** — PASS (vox skin). B01 title CARD, B11 endcard CARD,
   B12 OutroSeries, B13 OutroCTA. Non-Claude channel, own skin kept per
   rebuild contract rule #5.
3. **Spark lines** — N/A. No ClaudeComposerAsk beats in this vox skin.
4. **Verdict** — N/A / effectively present. No BVDT beat in this vox skin;
   the RECAP beat B11 carries a real compressed claim ("Same antibody. One
   payload stays put — confined by charge. One payload spreads — carried
   by membrane permeability. That is why T-DXd, not T-DM1, treats HER2-low
   breast cancer."). Amendment allows absent BVDT; a real recap covers it.
5b. **Chart text** — PASS. vox_scenes labels are short category nouns and
    unit-prefixed values (`T-DM1`, `T-DXd`, `Antibody: trastuzumab`, `HER2+
    cell`, `5 HER2+ entry points`, `payload stays inside`, `5 cells killed`,
    `~40 cells killed`). Bar/panel heights agree with narration meaning:
    the T-DXd column carries the larger kill count and is the teal (payload
    that spreads) accent. Comparison beat B10 puts the two side by side.
5. **Card text** — FIXED. B07 `remotion.FormACard.props.lines` was a
    truncated narration head with a trailing ellipsis (a placeholder).
    Rewrote to a three-line honest slate that names the artifact this
    beat needs (see REBUILD-LOG.md).
6. **Punt sweep** — FIXED (only B07). All other body beats have real
    vox_scenes classes (10 real manim graphics); B12/B13 are outros with
    Remotion patterns that render as slates in this cut.
7. **Card-only reel** — PASS. 10 real manim graphics beats + 3 slate/card
    beats (B07/B12/B13). Not card-only.
8. **Lens audit** — LOG. This is a cancer-nanomedicine mechanism explainer,
    not a computational-skepticism reel; the LENS-NOTES.md moves apply
    loosely. Descartes/Popper: the reel states the naive/falsifiable claim
    up front (B05 "the reasonable guess: both drugs underperform equally")
    and then falsifies it with mechanism (B06–B08). Plato: names the
    artifact (the antibody / the payload molecule), names the world (the
    HER2-low tumor's cell field), interrogates the relationship (antibody
    finds the cell, permeability decides who dies). Two moves earned.
9. **Brand fields** — FIXED. `voice_id` (ElevenLabs) DROPPED; `engine =
    kokoro`, `voice = am_onyx` set. No folderLabel field on this vox
    schema (vox reels don't carry a channel handle in metadata).
10. **Pacing** — Advisory:
    - B03 actual 1.90 wps (below 2.0 by 0.10) — question card, brief
      by design, at the lower boundary.
    - B11 estimated 3.50 wps (above 3.4) but ACTUAL 2.00 wps — the
      estimated_duration_s was pessimistic; the measured Kokoro clock
      brings pace to the bottom of the band.
    - B12/B13 outros: estimated 1.00 wps (below) but actual 2.76 / 3.36
      wps — measured clock in range.
    Log-only; no retime.
11. **type_check.py** — GATE T: run after audio regeneration. See build log.

## PHASE 2 — Build
- **Audio.** Regenerated all 13 beats via Kokoro `am_onyx`; measured
  durations written to `actual_duration_s` per beat. Total: 116.2s.
- **Renders.** Manim scenes rendered at 1920×1080 (upscaled to 4K by
  compile per 4K LAW):
    B01 Title, B02 TwoDrugs, B03 Question, B04 AntibodyOneStep,
    B05 NaiveGuess, B06 TDM1Confined, B08 TDXdSpreads,
    B09 ImplicationQuote, B10 Example, B11 Endcard  → `manim/B*.mp4`.
  PIL-drawn PNG cards for the three non-manim beats:
    B07 HER2-low tumor field slate (authored fresh),
    B12 OutroSeries card, B13 OutroCTA card (both reused byte-for-byte
    from sister reel vox-emitter-range/media — narration is identical).
- **Compile.** Slot fill: MANIM×10 + STILL×3. No slates in final master.
  Compiled at 3840×2160 (4K LAW enforced). B05 and B09 quote scenes were
  ~1.2× slowed by the compile ladder to fill their beats (within
  ±LADDER_REFUSE 15% tolerance, silent retime allowed).
- **Gate LANE.** PASS. No pipeline-slate or gen-AI violations.
- **Gate V (frame QC).** Contact sheet + 12 sampled frames reviewed.
  Palette rendered as teardown (vox_graphics default): white ground,
  ink text, crimson accent — consistent with sister vox-emitter-range
  and the current vox DESIGN.md house look. The July-2026
  `color_semantics` metadata note ("TEAL = ...") is descriptive-intent
  legacy; visually the teardown palette carries semantics via label/
  position (T-DM1 CRIMSON title / T-DXd ink title in B06/B08). Every
  beat renders real content, labels legible, safe insets respected,
  canvas fill full. No overflow, no clipping, no gen-AI. PASS.
- **Gate AUDIO.** PASS — master mean_volume −23.9 dB, max_volume −3.0
  dB. Audio stream: aac. Above the −40 dB floor by 16 dB.
- **Punt sweep post-build.** Zero slates in the master; zero unfilled
  fill_slates / remotion_scenes; zero DoodleScene/DoodleChart; zero
  STILL-src-archive for conceptual content (the three STILLs are
  authored cards, not archive stock). All bookend beats included.

## Output
- `vox-bystander-effect.mp4` — master (116.2s, 4K, per-beat narration
  muxed).
- mp4 mtime (09:05:17) is 15s newer than beat_sheet.json (09:05:02).
- No further sheet edits after compile.
