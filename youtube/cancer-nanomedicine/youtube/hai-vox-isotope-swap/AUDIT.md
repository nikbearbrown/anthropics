# AUDIT — hai-vox-isotope-swap
_Filmloop invocation: 2026-08-31 (Kokoro am_onyx, HAI palette)_

Channel: HAI (Humanitarians AI Pragmatist) vox-explainer. Not Claude-branded; Claude bookends do not apply — the reel's own bookends are B01 title / B12 endcard / B13 OutroSeries / B14 OutroCTA.

## Phase 1 — audit checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS (trivial) | No mp4s existed in the folder before this run. |
| 2 | Bookends | PASS | Non-Claude channel — kept its own opens/outros. B13 OutroSeries + B14 OutroCTA present. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats in this reel. |
| 4 | Verdict | N/A | No `BVDT` — this is a vox reel with `B12` endcard (RECAP), not a Claude verdict beat. RECAP narration states a real claim ("The scan runs first because it determines whether the drug can work.") — not a placeholder. |
| 5c | Your-Turn placeholder | N/A | No `BHTF` — HAI outro is `OutroSeries` + `OutroCTA`. |
| 5b | Chart text | PASS | Manim scenes render 1–3 word category labels ("PSMA-positive: 4", "DIAGNOSIS", "BRIGHT on PET", etc.), never narration fragments. |
| 5 | Card text | FIXED | B02 and B09 FormACard `props.lines` were placeholder ellipsis lines ("His team orders a scan first — not as a formality,…" / "So the scan is not paperwork. It is patient selection. A…"). Rewrote as three short paraphrased summary lines each (see below). |
| 6 | Punt sweep | FIXED | Six GRAPHIC beats (B03, B05, B07, B08, B10, B11) were `PIPELINE → render animated_graphics.py scene B*_*` slate punts. Authored `scenes.py` with real Manim scenes for all six and rendered them (`manim/B03.mp4` … `manim/B11.mp4`). Two FormACard STILL beats (B02, B09) rendered via `remotion_scenes.py`. Two OUTRO beats (B13, B14) re-rendered after props fix. B01/B04/B06/B12 remain slate CARD beats — honest slates naming what belongs there (review-slate cut format). |
| 7 | Card-only reel | PASS | Six Manim scenes + two FormACards = eight drawn body beats. Not a card-only reel. |
| 8 | Lens audit | PASS | Two moves earned: (a) Descartes/Popper — B05 states the naive premise "diagnosis → treat" and B10 states in advance what falsifies it ("dark on the scan → cannot bind"); the framing is "This is the assumption the scan is designed to test — and often falsifies." (b) Plato — the reel names the artifact (PET scan image), the world (tumor PSMA expression), and the relationship (bright = binds, dark = misses); B12 restates it. |
| 9 | Brand fields | FIXED | Metadata carried dead ElevenLabs fields `voice_id: "qdEb53HLreRBCD1FQE30"` and ElevenLabs-era `clock` prose. Both dropped (VOICE-LOCK). Engine `kokoro`, voice `am_onyx`, palette `humanitarians`, register `Pragmatist` all present and coherent. B13 `OutroSeries` props were stale (`seriesTitle/tagline/githubSlug`) and rendered against the wrong schema → showed "Part of the Claude Cowork series." Rewrote to `eyebrow`/`line` per the current schema. B14 `OutroCTA` had unused `authorName/ctaText` — replaced with `line/handle`. |
| 10 | Pacing | PASS | All 14 beats fall in 2.6–3.1 wps against `actual_duration_s` — within the 2.0–3.4 window. |
| 11 | `type_check.py` | PASS | GATE T: 0 FAILs, 4 checked (B02/B09/B13/B14 have Remotion text payload); 10 SKIP (no video yet at check time). Two `§8.10 REDUNDANCY` advisories on B02/B09 (my new lines paraphrase the narration; advisory does not block). |

## Phase 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` written (byte-exact copy) BEFORE any edit.
- Narration LOCKED — no `narration_text` changed.
- Dead ElevenLabs envelope fields dropped from metadata.
- `shot.form` per beat: pre-existing `shot.type`/`shot.source` classifications intact; six GRAPHIC beats now have real Manim scene classes named in `scenes.py`.
- HAI open + outro retained (non-Claude channel — never Claude-washed).

## Card-line rewrites (FormACard `props.lines`)

- B02 (was): `["His team orders a scan first — not as a formality,…"]`
  B02 (now): `["Order the scan before the treatment.", "One question: is the target present?", "A whole-body image in minutes."]`
- B09 (was): `["So the scan is not paperwork. It is patient selection. A…"]`
  B09 (now): `["The scan is patient selection.", "PSMA-negative: dose to salivary glands, kidneys.", "No binding where it must bind."]`

## Phase 2 — build

- **Audio** — pre-existing Kokoro `am_onyx` mp3s (14/14), timings measured; reused (VOICE-LOCK, free — never a gate). `mp3/timings.json` matches `actual_duration_s` per beat.
- **Manim** — `scenes.py` authored (~230 lines) with six `Scene` classes matching the sheet's `scene_class` names: `B03_LesionMap`, `B05_NaiveLoop`, `B07_IsotopeSwap`, `B08_BindingLogic`, `B10_ScanPredicts`, `B11_Example`. Rendered at 1920×1080, 24fps, humanitarians palette. All six mp4s in `manim/`.
- **Remotion** — B02/B09 FormACard, B13 OutroSeries (post-props-fix), B14 OutroCTA (post-props-fix) rendered via `remotion_scenes.py --force`.
- **Compile** — `compile.py --review --force`. GATE LANE: PASS (no pipeline-owned slates). GATE AUDIO: PASS at −24.0 dB mean. Contact sheet written. Master: `vox-isotope-swap-slate.mp4` (160.6s, 10/14 filled, 4 honest slate cards on B01/B04/B06/B12).
- **Gate V (frames)** — sampled at 15/50/85% of master + selected beat midpoints. B03 lesion map, B05 naive-loop, B07 isotope morph, B08 binding logic, B10 decision split, B11 before/after all readable; category labels within safe box; two-accent (teal/crimson) restraint held. Slate cards (B01/B04/B06/B12) render as ink-on-charcoal review labels — declared slates by design in a review cut. B07 and B10 auto-slowed 1.06–1.07× to fill beat window (compile advisory, within pantry tolerance).

## Punts authored

| Beat | Before | After |
|---|---|---|
| B02 | `YOU → gen-AI clip → pantry` | Remotion FormACard (three real lines) |
| B03 | `PIPELINE → render animated_graphics.py scene B03_*` | Manim `B03_LesionMap` (torso + 4 teal + 2 crimson lesions) |
| B05 | `PIPELINE → …scene B05_*` | Manim `B05_NaiveLoop` (DIAGNOSIS → TREAT boxes + caption) |
| B07 | `PIPELINE → …scene B07_*` | Manim `B07_IsotopeSwap` (chip morph Ga-68 → Lu-177, roles swap in sync) |
| B08 | `PIPELINE → …scene B08_*` | Manim `B08_BindingLogic` (2 tumor cells, left binds / right misses) |
| B09 | `YOU → gen-AI clip → pantry` | Remotion FormACard (three real lines) |
| B10 | `PIPELINE → …scene B10_*` | Manim `B10_ScanPredicts` (BRIGHT/DARK decision split) |
| B11 | `PIPELINE → …scene B11_*` | Manim `B11_Example` (before/after chart, −60% teal / +40% crimson, illustrative) |

Four beats remain honest slates (B01, B04, B06, B12) — CARD-type beats routed to `scripting-gap` by `beat_plan.py`. They pass GATE LANE (not pipeline-owned) and label the intended card copy in the review cut.

## Result

- Master: `vox-isotope-swap-slate.mp4` (160.6s, 3.3 MB, aac+h264, audio mean −24.0 dB).
- Sheet mtime preserved by `stamp_sheet` (compile.py's post-2026-08-28 guard); mp4 mtime is later than sheet mtime — reel is DONE-eligible per the supervisor's staleness rule.
- Zero BLOCKER / MAJOR on real beats. Four declared review slates on card-only beats.
