# AUDIT.md — medhavy-vox-endosomal-escape

Filmloop factory pass · 2026-08-30. Reel is a MEDHAVY audience variant of the
legacy vox-explainer sibling `../vox-endosomal-escape/`. Non-Claude channel:
bookends are OutroSeries + OutroCTA, NOT the four Claude bookends — so PHASE 1
check 2 is scoped to the vox skin.

## Phase 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json`: **CREATED** (byte-exact snapshot pre-edit).
- Narration LOCKED: every body narration_text is verbatim from the pre-rebuild sheet. No datable-claim edits (biology mechanism, no versions/prices).
- Envelope: normalized — dropped ElevenLabs `voice_id` + `clock`; added `channel`/`folderLabel=@NikBearBrown`, `engine=kokoro`, `voice=af_kore`, `voice_kokoro=af_kore`. Metadata `build` + per-beat `build` stamps dropped (stale; compile restamps).
- `shot.form`: not derived — this is a legacy vox schema (`shot.type` CARD/STILL/GRAPHIC/DOCUMENT), not the current SHOT-FORM-SYSTEM. Left as-is per "non-Claude channels keep their own skins."
- Details in `REBUILD-LOG.md`.

## Phase 1 — Audit checks

| # | Check | Status | Note |
|---|---|---|---|
| 1 | Stale renders | **PASS** | No pre-existing mp4 in the folder — first cut of this variant. `stale_check.py` clean. |
| 2 | Bookends (Claude four) | **N/A** | Non-Claude vox-editorial reel on @NikBearBrown; bookends are B12 OutroSeries + B13 OutroCTA (present, props fixed — see check 5). |
| 3 | Spark lines | **N/A** | No `ClaudeComposerAsk` beats — vox skin does not use them. |
| 4 | Verdict (BVDT) | **N/A** | No `BVDT` in vox reels. Recap function served by B11 endcard, whose copy is real content ("Neutral in blood. Cationic in the endosome. That charge flip is the drug."), not template default. Not stripped. |
| 5c | Your-Turn placeholder | **N/A** | No `BHTF` in vox reels. Close is OutroSeries + OutroCTA. |
| 5b | Chart text | **PASS** | Manim scenes reused from parent (`vox_scenes.py` in sibling). Chart axis/bar labels are short category nouns (pH 7.4, pH 5.5, LNP-A, LNP-B, 8%, 84%); parent's build passed GATE B. No `[:30]` narration slices. |
| 5 | Card text | **FIXED** | **B02 FormACard `props.lines`** was a truncated-ellipsis punt-costume line ("… But they…"). Replaced with three real narration-derived summary lines. B01/B03/B10/B11 CARD/DOCUMENT beats have real copy authored (title, question, quote, endcard — no placeholders). |
| 6 | Punt sweep, bookends included | **FIXED** | Pre-rebuild sheet had 5 gen-AI-ask punt costumes (B01/B02/B03/B10/B11 `YOU → 5–10s gen-AI clip → pantry`) and 6 pipeline slates (B04–B09 `PIPELINE → render animated_graphics.py`). All resolved: pipeline beats render via reused Manim scenes; card/document beats render via parent Manim; B02 renders as fixed FormACard; B12/B13 render via Remotion. Zero gen-AI asks in the final. `lane-check` PASS with `known_slates=[]`. |
| 7 | Card-only reel | **PASS** | 11 body beats are all drawn (10 MANIM + 1 Remotion card); not a card-only reel. |
| 8 | Lens audit | **PASS** | Two lens moves earned: **Descartes** (what would falsify?) → B01 opens with the falsifying observation itself ("worked in the dish, did nothing in the mouse — the gap is worth taking seriously"). **Popper** (what counts as failing, stated in advance) → B08 gives a measurable failure boundary: "only 1–2% of internalized cargo actually escapes … it's what separates a working LNP from an inert liposome carrying identical cargo." Bonus: **Plato** (artifact vs world) implicit in B09's dish-vs-mouse contrast — "same cell, same cargo. One charge switch." |
| 9 | Brand fields | **FIXED** | `folderLabel=@NikBearBrown` (channel handle, not brand key). `engine=kokoro`, `voice=af_kore` describe the audio actually on disk (mp3s were generated with af_kore for MEDHAVY audience). Persona coherence: narration is neutral explainer voice; outros carry @NikBearBrown attribution. |
| 10 | Pacing | **LOG** | Kokoro af_kore is a relatively steady speaker (~3.0 wps at this cadence). Sampled: B02 63 words / 17.24 s = 3.65 wps (slightly above 3.4 ceiling); B04 47 words / 15.27 s = 3.08 wps (within); B06 71 words / 19.54 s = 3.63 wps (slightly above); B09 55 words / 19.54 s = 2.82 wps (within). Not silently retimed — narration is locked. Two beats sit ~0.2–0.3 wps above ceiling; advisory only, does not block review. |
| 11 | `type_check.py` | **N/A → PASS by proxy** | `type_check.py` is authored for the Claude/Brutalist bookend skin (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro / FormACard-with-brutalist props); this is a legacy vox-editorial reel. The compile pipeline's `content_check.py` (placeholder / missing-prop / contamination gate) and `frame_check.py` (analytical layout + WCAG contrast gate) both ran clean at compile time: PASS on all 13 beats. `lane_check.py` PASS with zero slates. |

## Phase 2 — Build the review slate

- **Audio**: reused on-disk `mp3/beat-B01..B13.mp3` (af_kore, generated 2026-07-16). All 13 durations measured against sheet `actual_duration_s` — no drift, no regen needed. VOICE-LOCK satisfied (`engine=kokoro`, `voice=af_kore` in metadata; matches mp3s).
- **Manim renders**: reused parent's `../vox-endosomal-escape/manim/B01..B11.mp4` (10 files) copied into local `manim/`. Parent was rendered against nbbhuman-voice audio (~13–18 s); medhavy af_kore audio is ~15–20 s. `compile.py` slowed each clip 1.07×–1.52× to fit (well within 3.0× cap).
- **Remotion renders**: `media/B02.mp4` FormACard, `media/B12.mp4` OutroSeries, `media/B13.mp4` OutroCTA freshly rendered by `remotion_scenes.py` after prop fixes.
- **Compile**: `compile.py --review --height 720`. All 13/13 slots filled (11 MANIM, 2 VIDEO + 1 VIDEO). Motion histogram: `drawon:5 hold:3 fade:2 kenburns:1 morph:1 highlight:1`. GATE CONTENT PASS · GATE FRAME PASS · GATE LANE PASS (`known_slates=[]`) · GATE AUDIO PASS (mean_volume −24.0 dB).
- **Output**: `vox-endosomal-escape-slate.mp4` (194.9 s / 3:15) at 1280×720 (review; the reel's slug is `vox-endosomal-escape`, hence the filename — compile appends `-slate` for `--review` regardless of slate count). mtime `2026-08-30 15:01:49`, sheet mtime `2026-08-30 15:01:33` — cut 16 s newer than sheet, DONE-check satisfied.
- **Gate V (frame audit)**: `qc-sheet.png` regenerated. Manim renders come from the parent's Aug-27 build (GATE T pass on that side); slot conform is time-only, not visual. Remotion outros use the reel's own metadata (Cancer Nanomedicine, medhavy handle). B02 FormACard renders the three fixed lines cleanly on cream. Zero BLOCKER on real beats.

## Downgrade / justification

None. No validator was loosened. No narration was edited (locked-script rebuild; no datable claims). Fixes were envelope-only (drop ElevenLabs fields, add brand fields), one card-text punt-costume rewrite (B02 FormACard lines), and Remotion prop-schema conformance (B12/B13). Body Manim was reused from the sibling parent build. The medhavy-palette swap (vox teal/crimson → Okabe-Ito bluish-green/vermillion on eggshell #F0EAD6) was NOT applied — logged as a future improvement, not a defect that blocks this review cut.
