# hai-vox-tumor-pressure — Rebuild + Slate-Cut Audit

**Date**: 2026-08-28
**Skill**: rebuild (Cohort C, legacy vox translated for HAI)
**Channel**: @humanitariansai · **Voice**: Kokoro `am_onyx`

## PHASE 0

- `beat_sheet.pre-rebuild.json` — created byte-exact (14402 B) BEFORE any edit.

## PHASE 1 checks

| # | Check | Result |
|---|---|---|
| 1 | Stale renders | PASS — no mp4s in the reel folder before this pass. |
| 2 | Bookends | PASS — this is a non-Claude HAI vox reel; bookends are its own skin (B01 title CARD, B03 question CARD, B11 endcard CARD, B12 OutroSeries, B13 OutroCTA). Contract explicitly says: non-Claude channels keep their own skins — never Claude-wash an open or outro. |
| 3 | Spark lines | N/A — no `ClaudeComposerAsk` bookends. |
| 4 | Verdict | N/A — no `ClaudeVerdictArtifact` slot to fill or strip. Reel carries its own stated recap in B11 (`"Accumulation is not delivery. Measure core IFP."`) — a real finding, drawn from body content, not a template default. |
| 5 | Card text | FIXED — every FormBCard/FormACard authored real `label`/`sub` from narration; zero placeholders. B01 title / B03 question / B11 endcard copy authored from narration. |
| 6 | Punt sweep | FIXED — 7 pipeline-owned GRAPHIC slates (B02/B04/B05/B06/B07/B08/B10) routed to real Remotion patterns (FormBCard × 6, FormACard × 2 counting B02). Remaining slates (B01 title, B03 question, B09 quote-DOCUMENT, B11 endcard) are legit human-owned CARD/DOCUMENT beats — legal declared slates in a review cut. |
| 7 | Card-only reel | LOG (accepted) — this is a legacy-vox translation; the source card explicitly excludes the diffusion-limit derivation, the 4-barrier list, and the 30-vs-150nm debate, which limits the amount of drawable structure. Body beats B04–B08 and B10 render as FormB/FormA cards with production_viz specs preserved for a future Manim pass. Peer `hai-vox-delivery-diagnosis` accepted the same tradeoff same session. |
| 8 | Lens audit | PASS — two moves earned. **Descartes**: the standard "leaky-vessels-enable-extravasation" claim, taken as a checklist claim, produces its own falsifier — the same anatomy that lets particles in also floods the interstitium (B04). **Plato**: names the artifact (nanoparticle drug), the world (net outward interstitial flow + hypoxic-core selection), and the relationship (accumulation is not delivery — B11 endcard states this aloud). |
| 9 | Brand fields | FIXED — `folderLabel=@humanitariansai`; `engine=kokoro`, `voice=nbbhuman`, `voice_kokoro=am_onyx`; slug corrected `vox-tumor-pressure → hai-vox-tumor-pressure`. Dropped ElevenLabs-era `voice_id=qdEb53HLreRBCD1FQE30`, dropped `_variant_todo` (migration is now done), dropped lying `metadata.build` (claimed filled 2/13 with SLATE stamps for beats never rendered). B12 `OutroSeries` and B13 `OutroCTA` props reshaped to current `eyebrow`/`line`/`handle` schemas (peer defect: legacy `seriesTitle`/`tagline`/`githubSlug`/`authorName`/`ctaText` props silently fell back to Claude Cowork defaults). |
| 10 | Pacing | PASS — body beats within 2.0–3.4 wps against Kokoro-measured `actual_duration_s`. |
| 11 | `type_check.py` | PASS — advisories on §8.10 for B02/B10 (narration recites card, similarity 0.93); non-blocking, same pattern as peer HAI reels. No validator loosened. |

## PHASE 2 build

- **Audio**: pre-existing Kokoro `am_onyx` mp3s from 2026-07-16; measured `actual_duration_s` values carried through. No regeneration needed (VOICE-LOCK envelope matches).
- **Icon substitutions** (icons not in `form-b-icons/`): `arrow-right` → `target`, `arrow-left` / `arrow-up` → `shield-alert`, `droplet` → `life-buoy`, `gauge` → `zap` (B06 core-pressure), `arrow-right` → `layers` (B06 flow), `circle-x` retained where valid.
- **Renders**: `remotion_scenes.py` filled B02/B04/B05/B06/B07/B08/B10/B12/B13 to `media/*.mp4`.
- **Compile**: `compile.py --review --height 720` → 9/13 VIDEO, 4/13 SLATE.
- **Gate CONTENT**: PASS (13/13)
- **Gate FRAME**: PASS (13/13, canvas 3840×2160)
- **Gate LANE**: PASS (0 violations; `known_slates=['B01','B03','B09','B11']` — all declared CARD/DOCUMENT lanes)
- **Gate T**: PASS
- **Gate AUDIO**: PASS — `mean_volume −23.9 dB`, `max_volume −2.9 dB`, aac stereo, duration 152.2 s.
- **Gate V**: not run — deferred to full-render pass; this is a Phase-2 review-slate cut with declared CARD/DOCUMENT slates. The 9 real Remotion beats render clean per compile output.

**Punts authored**: 7 (B02 gen-AI slate → FormACard, B04/B05/B06/B07/B08 non-existent-Manim-scene slates → FormBCard, B10 non-existent-Manim slate → FormACard). Remaining SLATE beats (B01/B03/B09/B11) are legit human-owned CARD/DOCUMENT lane placeholders in a review cut.

**Verdict authored or stripped**: N/A — see §4. B11 endcard carries an authored finding drawn from body body content.

**Duration**: 152.2 s.

**build.status Counter (verbatim)**: `Counter({'VIDEO': 9, 'SLATE': 4})`

**Staleness check**: mp4 mtime `Aug 28 04:06:43` vs sheet mtime `Aug 28 04:06:38` (+5 s) — mp4 newer than sheet ✓. No post-compile sheet edits.

**Downgrade / justification**: none. No validator loosened. Motion histogram advisory `fade` on 8/13 (61%) — over the ~40% pantry cap (compile WARNING only, non-blocking); noted for the future Manim-figure pass to diversify motion.

**Honest note**: card-only-plus-slates review cut, matching the pattern of the peer `hai-vox-delivery-diagnosis` shipped 2026-08-27. Six body beats that could be drawn Manim figures (leaky vessels, pressure buildup, radial outward flow, particles returning to rim, hypoxic core selection, week-3-vs-week-8 timeline) render as FormB/FormA cards. Intended mechanics are preserved verbatim in `beats[].graphic.production_viz` blocks for the future Manim pass. This is a Phase-2 review slate, not the intended final render.
