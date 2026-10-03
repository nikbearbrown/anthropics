# AUDIT — hai-vox-emitter-range
_Pass: 2026-08-28_

## Phase 0 — Rebuild Contract
- `beat_sheet.pre-rebuild.json` created (byte-exact copy before first edit) ✓
- Dead ElevenLabs fields dropped: `voice_id`, `clock` — see REBUILD-LOG.md
- VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- Non-claude channel skin retained: OutroSeries / OutroCTA at B13/B14 (HAI, per REBUILD SKILL §3)

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** No mp4 files existed at audit start (only `mp3/`, `clips/master.m4a`, `qc-sheet.png`). Nothing to delete.

### Check 2 — Bookends
**N/A — non-claude channel.** This is the HAI (Humanitarians AI) variant. REBUILD SKILL §3 exempts non-claude channels from the ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro bookend contract; HAI's own outro is OutroSeries + OutroCTA at B13/B14. Both patterns are registered in `runtime/scripts/remotion_scenes.py`.

### Check 3 — Spark lines
**N/A — non-claude channel.** No ClaudeComposerAsk beats in this reel.

### Check 4 — Verdict
**N/A — non-claude channel.** No BVDT / ClaudeVerdictArtifact beat.

### Check 5b — Chart text
**PASS.** Reviewed all frames of B11 (Lu-177 vs Ac-225 comparison, the only chart-adjacent beat): `Lu-177`, `Ac-225`, `78%`, `41%`, `tumor cell kill`, `vs`, header `Heterogeneous neuroendocrine tumor | illustrative numbers`. Short categorical labels, no narration-slice text, no overflow. Bar/kill numbers agree with narration (Lu-177 78% beats Ac-225 41%). PASS.

### Check 5 — Card text
**PASS.** No FormA / FormB items in this reel. Legitimate CARD beats (B01/B04/B10/B12) carry authored `card.copy` and `card.sub` from the locked script; no placeholders, no clipping in the review-slate label overlays.

### Check 6 — Punt sweep
**FIXED (5 punts stripped, 1 STILL/ai converted).**

Card-beat `YOU → 5–10s gen-AI clip → pantry` needs-lines removed from B01, B04, B10, B12 (`build.needs` cleared; content preserved). These are legitimate CARD beats — but the sheet was labelling them as gen-AI pantry work, which is the §6 costume the punt inventory bans. Removing the tag reclassifies them as `scripting-gap` (author-owned), which lane-check permits as an honest slate in a review cut.

`PIPELINE → render animated_graphics.py scene BXX_*` needs-lines removed from B02, B03, B05, B06, B08, B09, B11 (compile.py handles slot resolution).

B07 was `STILL / source: ai` with a `FormACard` placeholder remotion block, an `image_prompt`, and `build.needs: YOU → 5–10s gen-AI clip → pantry`. Converted to `GRAPHIC / source: own / motion: drawon` with `graphic.manim: B07_TumorGeometry` and a full `production_viz` block (same fix as the claude-liam sibling — see REBUILD-LOG.md). Scene exists in the copied `scenes_std.py` and renders correctly.

### Check 7 — Card-only reel
**PASS.** 8 GRAPHIC/manim body beats + 2 remotion outros are pipeline-drawn. Only 4 CARD beats (B01/B04/B10/B12) — well below the card-only threshold.

### Check 8 — Lens audit
**FIXED (LOG, minor).** Narration was locked (rebuild contract). The physics content runs:
- **Popper (falsifiability)** — B11 states quantifiable predictions: Lu-177 ~78% vs Ac-225 ~41% kill on a heterogeneous NET, labelled "illustrative"; the numbers name what would count as failing if measured otherwise. ✓
- **Plato (artifact / world / relationship)** — the whole reel distinguishes the emitter (artifact — a chosen isotope) from the tumor's spatial geometry (world) and asks how the range/geometry relationship decides efficacy. The B10 pivot ("The question is not which isotope delivers more lethal energy per hit. It is which range matches the spatial distribution...") is the Plato move made explicit. ✓
Two moves earned; body preserved as locked.

### Check 9 — Brand fields
**PASS (post-fix).** Metadata `engine: kokoro`, `voice_kokoro: am_onyx` ✓. `audience: HAI`, `palette: humanitarians`, `outro_source: AUTHOR.MD :: Humanitarians AI` — consistent. Kokoro `am_onyx` narration is a HAI-appropriate voice (not claiming to be a specific personality). No `folderLabel` in this HAI reel; the HAI channel handle appears at B14 as `@humanitariansai` ✓.

B13/B14 remotion `props` had wrong schema (`{seriesTitle, tagline, githubSlug}` and `{authorName, handle, ctaText}`) — the actual OutroSeries/OutroCTA components in `runtime/remotion/src/scenes/` expect `{eyebrow, line}` and `{line, handle}`. Fixed to correct schema; re-rendered; B13 now shows "CANCER NANOMEDICINE / AI education for humanitarian and social-impact practitioners." (was falling back to hardcoded "Claude Cowork" defaults). B14 now shows "More at humanitarians.ai / @humanitariansai".

### Check 10 — Pacing
**LOG.** Narration/estimated_duration wps (using existing mp3 measured durations):
- B01: 14 words / 7.68 s = 1.82 wps (below 2.0–3.4) — LOG. Short executive summary, appropriately paced.
- B02: 26 / 10.65 = 2.44 ✓
- B03: 27 / 11.03 = 2.45 ✓
- B04: 34 / 10.39 = 3.27 ✓
- B05: 32 / 10.56 = 3.03 ✓
- B06: 34 / 11.39 = 2.98 ✓
- B07: 32 / 11.75 = 2.72 ✓
- B08: 26 / 10.45 = 2.49 ✓
- B09: 33 / 11.33 = 2.91 ✓
- B10: 36 / 11.86 = 3.03 ✓
- B11: 42 / 20.46 = 2.05 ✓
- B12: 26 / 8.23 = 3.16 ✓
- B13/B14: outro bumper — not applicable

Only B01 sits outside the band, and it is a short sentence hook — not a silent retime candidate. Logged, not retimed.

### Check 11 — type_check.py
**N/A.** `runtime/scripts/type_check.py` is bound to Claude/Liam Brutalist reels and does not target this reel's HAI vox skin. Content-check + frame-check + lane-check ran inside compile.py and all PASSED — see Phase 2.

## Phase 2 — Build

- Audio: existing `mp3/beat-BXX.mp3` files reused (Kokoro-onnx output confirmed by 24 kHz mono @ 72 kbps encoding; sheet already had VOICE-LOCK `voice_kokoro: am_onyx`). All 14 mp3s present; measured `actual_duration_s` values unchanged.
- Manim: `scenes_std.py` copied from claude-liam sibling; rendered `B02_AlphaIntro`, `B03_BetaIntro`, `B05_EmitterRanges`, `B06_Crossfire`, `B07_TumorGeometry`, `B08_AlphaFail`, `B09_BetaWin`, `B11_Example` to `manim/BXX.mp4`. Total render time ~25 s (all 8).
- Remotion: `remotion_scenes.py --only B13` and `--only B14 --force` after fixing props schema. Outputs written to `media/B13.mp4`, `media/B14.mp4`.
- Compile: `compile.py --review` produced `vox-emitter-range-slate.mp4` (144.6 s).
- Content-check: PASS (14 beats).
- Frame-check: PASS (14 beats).
- Lane-check: PASS (0 violations; honest slates on B01/B04/B10/B12 are author-owned scripting-gap CARDs, exempt).
- GATE AUDIO: PASS, mean_volume = **−23.9 dB**, max_volume = −2.9 dB.
- Motion histogram: drawon:8 hold:4 fade:2 — WARNING at 57% drawon (above ~40% cap). Not a hard fail; expected for a diagram-heavy explainer.
- QC contact sheet: `qc-sheet.png` regenerated and reviewed — all 14 beats render on-brand.

## Gate V — Frame Read
Sampled 12 frames at 1/12 fps across the 144.6 s cut. Spot-read confirmed:
- B01/B04/B10/B12 slate cards: legible beat id + narration hook + SCRIPTING GAP owner line (label overlay expected, review-cut format).
- B02/B03: individual particle-track diagrams, clean.
- B05: split alpha/beta range panels, clear color coding.
- B07: 3 cm tumor cross-section, teal rim / muted core, ~3 cm scale label — legible.
- B11: Lu-177 vs Ac-225 cards with 78% (teal) and 41% (crimson) kill numbers.
- B13: correct HAI series card ("CANCER NANOMEDICINE") after props fix.
- B14: correct HAI CTA card ("More at humanitarians.ai", "@humanitariansai").
- No text crossings the SAFE inset, no container overflow, one accent-color moment per beat, brand bug placement consistent.
- 0 BLOCKER, 0 MAJOR on real beats.

## Result
- **`vox-emitter-range-slate.mp4`** — 144.6 s review slate cut.
- Cut mtime 06:13:26 is 5 s AFTER sheet mtime 06:13:21 (not stale).
- 10/14 slots real (7 Manim + 1 Manim [B07 rescued from STILL/ai] + 2 Remotion outros); 4 honest author-owned slates (B01/B04/B10/B12).
