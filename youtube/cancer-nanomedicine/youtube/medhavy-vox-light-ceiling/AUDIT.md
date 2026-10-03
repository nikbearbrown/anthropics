# AUDIT — medhavy-vox-light-ceiling

_Filmloop pass 2026-08-28. MEDHAVY vox-explainer, Kokoro `af_kore`, palette `medhavy`.
Slate-with-audio review cut (three author-owned CARD slates by design, nine
Remotion-rendered body beats). Same pattern as shipped peer `hai-vox-tumor-pressure`._

## PHASE 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` written (byte-exact backup, 17638 B).
- Envelope normalized: dropped `voice_id` (ElevenLabs), dropped `clock` prose.
  Kept `engine=kokoro`, `voice_kokoro=af_kore`, `audience=MEDHAVY`, `palette=medhavy`,
  `register=Wonder`, MEDHAVY outros in B11/B12.
- Narration LOCKED — no beat narration was rewritten.
- Props reshaped for B04-B09: `shot.type` GRAPHIC → REMOTION with FormBCard pattern
  (2-3 items compressed from the beat's own narration). `graphic.production_viz`
  blocks preserved verbatim for a future Manim authoring pass.

## PHASE 1 — check-by-check

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s in reel folder before this pass; nothing older than `beat_sheet.json` to delete. |
| 2 | Bookends | PASS (skin-appropriate) | Non-Claude channel (MEDHAVY). PHASE 0.5 keeps its own skin. Uses `OutroSeries` (B11) + `OutroCTA` (B12); no Claude B00/BVDT/BHTF/BOUT required. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats. |
| 4 | Verdict (audit/strip) | N/A | No BVDT beat; MEDHAVY vox uses B10 endcard, not a Claude verdict artifact. |
| 5b | Chart text | LOG (not rendered this pass) | The named Manim scenes `B04_PDTMechanism`, `B05_LightQuestion`, `B06_LightDepth`, `B07_OpticalWindow`, `B08_FormulationCeiling`, `B09_TwoPatients` are not present in `runtime/manim/animated_graphics.py`. Instead of authoring six one-off scenes (SKILL bans one-off components), the beats were routed to FormBCard with the intent compressed to `title` + `items[label/sub/icon]`. Original `production_viz.mechanic` and colors preserved for a future full-render pass. Category labels on each FormBCard item are short nouns (1–3 words); `sub` lines are single complete phrases from the narration; no mid-word truncation observed in QC frames. |
| 5 | Card text | FIXED | B01 title/sub, B03 question/dek, B10 endcard/sub all real; no placeholders. B02 `FormACard.lines[0]` was reciting the narration (§8.10 advisory) — compressed to `"10× tumor accumulation. Both lesions reached. Only one cleared."` — a real pointer, not the script. |
| 6 | Punt sweep | FIXED | Zero gen-AI asks. Nine pipeline-owned GRAPHIC/REMOTION slates (B02, B04–B09, B11, B12) routed to real Remotion patterns (FormACard × 1, FormBCard × 6, OutroSeries × 1, OutroCTA × 1). Remaining three slates (B01 title CARD, B03 question CARD, B10 endcard CARD) are author-owned CARD beats — legal declared slates in a review cut. |
| 7 | Card-only? | PASS | Body drives nine Remotion-rendered beats. |
| 8 | Lens audit | PASS (2 moves) | **Popper**: the sheet states in advance what would count as "better delivery fixes this" failing — the 15 mm lesion at same 10× accumulation clears 3% (B09). **Plato**: artifact = the nanoparticle drug report ("delivered 10×"); world = tumor at 12 mm; relationship = the report is about local drug concentration, not the light physics that actually kills. The whole reel is the artifact-vs-world distinction applied to PDT. |
| 9 | Brand fields | PASS | `engine=kokoro`, `voice_kokoro=af_kore` matches audience MEDHAVY / palette medhavy / register Wonder. No `folderLabel` present (not required for non-Claude vox); narration does not claim a persona the voice contradicts. |
| 10 | Pacing | PASS | Per-beat WPS against measured duration: B01 2.83, B02 2.41, B03 3.17, B04 2.89, B05 3.01, B06 2.60, B07 2.52, B08 2.84, B09 3.07, B10 2.44, B11 2.56, B12 2.40 — all inside 2.0–3.4. |
| 11 | `type_check.py` | PASS | GATE T: PASS after B02 card compression and FormBCard rewire. TYPECHECK.md written. §8.10 similarity ceiling 0.77 (B04); all others ≤ 0.60. No advisory flag over threshold. |

## PHASE 1 outcome

All PHASE 1 checks PASS or PASS-with-fix. `type_check.py` GATE T: PASS. Cleared to build.

## PHASE 2 — build

- Audio: pre-existing Kokoro `af_kore` mp3s (12 beats). `actual_duration_s` values
  carried through from earlier measurement; no regeneration needed (VOICE-LOCK
  envelope is `af_kore` / `kokoro`, matches current lock for MEDHAVY variant).
- Remotion renders (9): B02 FormACard, B04–B09 FormBCard × 6, B11 OutroSeries,
  B12 OutroCTA — all rendered to `media/<BID>.mp4` via `remotion_scenes.py`.
- Declared slates (3): B01 title, B03 question, B10 endcard — author-owned CARDs.
- `compile.py --review --force`: content-check PASS, frame-check PASS, GATE LANE
  PASS (0 violations; `known_slates=['B01','B03','B10']` — all author CARDs).
  GATE AUDIO PASS, `mean_volume −24.1 dB`. Motion pantry WARNING flagged
  `fade` at 8/12 (66%) — over the ~40% cap; acceptable for a review cut where
  every Remotion beat defaults to fade. Motion diversification is a
  full-render-pass concern.
- Deliverable: `vox-light-ceiling-slate.mp4` (166.6 s, 720p review cut, audio: AAC
  stereo, 166.62 s).

## Gate V — sampled frames

- 00001 (t≈00:00 B01 CARD SLATE): title slate reads as expected.
- 00004 (t≈00:39 B04 REMOTION VIDEO): FormBCard "Delivery alone isn't enough" title +
  "Drug at the tumor / Reaches the site and sits inert" item card; icon (target)
  in place, safe-inset clean, no truncation.
- 00008 (t≈01:26 B07 REMOTION VIDEO): "Even the best window ends in millimeters"
  title, item "Red (~630 nm) / ~3 mm effective depth" — legible, safe inset clean.
- 00013 (t≈02:22 B10 CARD SLATE): endcard declared slate.

No BLOCKER or MAJOR defects on real beats. Declared slates (B01/B03/B10) show the
review-cut informational card by design.

## Staleness check

- `beat_sheet.json` mtime: `2026-08-28T04:25:19`
- `vox-light-ceiling-slate.mp4` mtime: `2026-08-28T04:25:27`
- mp4 is 8 s newer than sheet ✓. No post-compile sheet edits.

## Files touched this pass

- `beat_sheet.pre-rebuild.json` — new (byte-exact 17638 B backup of the sheet).
- `beat_sheet.json` — dropped `voice_id` + `clock`; compressed B02 FormACard line;
  rewired B04–B09 shot.type GRAPHIC → REMOTION + FormBCard props (production_viz preserved).
- `TYPECHECK.md` — GATE T PASS written.
- `media/{B02,B04..B09,B11,B12}.mp4` — nine Remotion renders written.
- `clips/*.mp4`, `clips/master.m4a`, `clips/manifest.json` — per-beat conforms + master audio.
- `vox-light-ceiling-slate.mp4` — the review-slate deliverable.
- `qc-sheet.png` — QC contact sheet (compile.py).
- `_qc/frames/*.png` — 14 sampled frames (fps=1/12).
