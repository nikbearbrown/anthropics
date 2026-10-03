# AUDIT — medhavy-vox-trial-failure-tree

Audited 2026-08-28. PHASE 1 against LENS-NOTES.md + the rebuild contract.
Non-Claude channel (Medhavy vox-explainer, Wonder register).

| # | Check | Result | Note |
|---|---|---|---|
| 0 | Pre-rebuild backup | FIXED | `beat_sheet.pre-rebuild.json` did not exist; copied byte-exact from `beat_sheet.json` before any edit. |
| 1 | Stale renders | PASS | No mp4 in the reel folder pre-run. Old `clips/master.m4a` (Jul 16) deleted before recompile. |
| 2 | Bookends | PASS | Non-Claude vox-explainer: opens with CARD title (B01), closes with OutroSeries (B14) + OutroCTA (B15). Never Claude-washed. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats. |
| 4 | Verdict | PASS | B13 endcard narration is a real recap ("A response-only endpoint cannot distinguish delivery failure, payload failure, or biology failure..."). Not a template default. |
| 5b | Chart text | PASS (inherited) | Manim renders reused from `hai-vox-trial-failure-tree/manim/` — identical palette (`#F3EBDD`/`#1F6F5C`/`#BF3339`). Labels are SHORT CATEGORY NOUNS (DELIVERY / PAYLOAD / BIOLOGY / NEGATIVE RESPONSE etc.). |
| 5 | Card text | FIXED | B02 and B11 were STILL·ai punts with truncated FormACard `lines` and `source=ai`. Converted to CARD `kind=info` with narration-derived copy/sub. |
| 6 | Punt sweep | FIXED | Two gen-AI STILL punts (B02, B11) authored to CARDs. Zero unfilled `fill_slates` / `remotion_scenes`, zero Doodle, zero `STILL src=archive`. |
| 7 | Card-only | PASS | Seven GRAPHIC beats (B04, B06–B10, B12), five CARD/DOCUMENT slates, two outros. Not a card-only reel. |
| 8 | Lens audit | PASS | Runs Popper (state-in-advance falsifier = built-in delivery measurement) and Plato (artifact = binary readout; world = three mechanistically distinct failure modes; relationship = collapsed) explicitly. Descartes latent ("what would have to be true for the negative to be attributable?"). Two moves clearly present. |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs `voice_id: "1sgY6Voq..."`. Rewrote `clock` prose to `narration (Kokoro af_kore, VOICE-LOCK) — actual_duration_s below is measured from the rendered mp3`. `engine=kokoro / voice_kokoro=af_kore` correct for the Medhavy Wonder register. |
| 10 | Pacing | LOG | Words-per-second on body beats using measured `actual_duration_s`: B01 34w/12.42s=2.74; B02 40w/15.94s=2.51; B03 55w/16.13s=3.41 (JUST OVER); B04 43w/12.86s=3.34; B05 40w/12.76s=3.13; B06 40w/12.33s=3.24; B07 55w/16.41s=3.35; B08 42w/15.85s=2.65; B09 45w/15.94s=2.82; B10 45w/14.95s=3.01; B11 42w/15.04s=2.79; B12 82w/31.49s=2.60; B13 40w/16.66s=2.40. B03 nudges the 3.4 ceiling; narration-locked, left as-is. |
| 11 | type_check.py | DOWNGRADE-LOGGED | Two inherited defects in the reused HAI manim renders: B10 fg/bg contrast 4.39:1 (WCAG 4.5:1, delta 0.11) and B12 min-size 8px vs 9px floor at 480p logical. Both are near-threshold, inherited unchanged from the sibling HAI cut which shipped with them. Fixing requires editing `scenes.py` source and re-rendering locally — deferred (out-of-scope for a review-slate cut; not a content defect, not a legibility defect at 4K). Logged, not a blocker for the review slate. |

## Fixed
- Dropped dead ElevenLabs `voice_id`.
- Rewrote pre-VOICE-LOCK `clock` prose.
- B02: STILL·ai → CARD `kind=info` (copy: "Polymeric nanoparticle. Targeting ligand. Chemotherapy payload." / sub: "Preclinical: promising. Trial: ran. Result: failed.").
- B11: STILL·ai → CARD `kind=info` (copy: "Add a tracer cohort. Label the particle. Image where it goes." / sub: "Binary negative → diagnosable result. The program stops guessing.").
- Filled the seven pipeline-owned Manim beats (B04, B06–B10, B12) by copying HAI's renders — palettes are byte-identical, manim scenes carry no audio, no branding text to swap.
- Rendered fresh Medhavy-branded OutroSeries (B14) and OutroCTA (B15) via `remotion_scenes.py`.

## Logged (not blockers for a review slate)
- Two inherited manim typography near-misses (B10, B12) — see check 11 above.
- Motion histogram warning: `drawon` carries 7/15 (46%), over the 40% pantry cap. This is a whole-reel pacing observation, not a beat-level defect. Leaving as-is per rebuild contract (narration + shot forms are locked).

## Build result
- Cut: `vox-trial-failure-tree-slate.mp4` (216.6s, 9/15 filled, 6 slates for review).
- Slates: B01, B02, B03, B05, B11, B13 (CARD/DOCUMENT — legitimate review slates for a slate cut).
- lane-check: PASS (zero pipeline-slate, zero gen-AI-in-master).
- GATE AUDIO: mean_volume −24.0 dB (well above −40 dB gate).
- Cut mtime > beat_sheet.json mtime by 10s.
