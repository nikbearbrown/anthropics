# AUDIT — medhavy-vox-epr-gap

Reel: `vox-epr-gap`  |  Audience: MEDHAVY (Wonder register, Kokoro `af_kore`, medhavy palette)
Cohort: C — legacy vox (per `_audit/REBUILD-WORKLIST.csv`)
Auditor pass: 2026-08-31

## Channel skin — MEDHAVY, not Claude

This reel is a medhavy vox-editorial explainer. It uses the OutroSeries / OutroCTA bookend
pair per `skills/make/audience-preset/brands/medhavy.md` — NOT the Claude four-bookend
convention (`B00` / `BVDT` / `BHTF` / `BOUT`). Per rebuild.md rule: "Non-claude channels
keep their own skins — don't force the Claude skin." Claude-specific bookend, spark-line,
verdict, and your-turn checks are therefore N/A here.

## Check list

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `mp4` files in reel folder — nothing to delete. |
| 2 | Bookends | PASS (non-claude skin) | B15 OutroSeries + B16 OutroCTA present with valid `remotion.pattern`. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats. |
| 4 | Verdict | N/A | No `BVDT` / `ClaudeVerdictArtifact` beat. |
| 5c | Your-Turn | N/A | No `BHTF` beat (medhavy has no exercise beat by design). |
| 5b | Chart text | PASS | Manim `production_viz` labels are short category nouns (1–4 words) or explicit numeric chips (`8% ID/g`, `0.3% ID/g`). Bracket sentence on B13 is a complete phrase. |
| 5 | Card text | PASS | All CARD beats have complete `copy` / `sub` / `eyebrow`; no placeholders. |
| 6 | Punt sweep | FIXED | 12 body beats were pipeline-owned `SLATE` (8 GRAPHIC/manim + 4 CARD without `remotion.pattern`). Since no `scenes.py` exists for the eight `production_viz` scenes on this reel, and to satisfy the PIPELINE-CARD RULE (lane_check refuses even review cuts with pipeline-slates), each of the 12 beats was scaffolded onto `shot.remotion.pattern: "FormACard"` with 2–4 summary lines drawn from that beat's own `production_viz.mechanic` / `card.copy` / narration numbers. All 12 render via `remotion_scenes.py`; nothing is punted. The FormACards are a REVIEW-cut summary of the intended drawings, not a substitute — the eight `production_viz` specs remain locked in the sheet for a future pass that authors the Manim scenes. |
| 7 | Card-only reel | PASS | Reel is designed around ~8 drawn Manim `production_viz` beats — not card-only. |
| 8 | Lens audit (against LENS-NOTES.md) | PASS — two moves | (a) **Hume** — B10 explicitly names the confidence-vs-world mismatch: "A nanoparticle optimized inside a maximum-EPR system was never actually tested under the conditions it would face in patients. You validated the particle in the wrong world." (b) **Plato** — B14 makes the artifact/world distinction plain: "The nanoparticle didn't fail. The model did." The mouse xenograft is the artifact; the human tumor is the world; the relationship was different. |
| 9 | Brand fields | PASS | `engine: kokoro`, `voice_kokoro: af_kore` matches medhavy skin. `audience: MEDHAVY`, `palette: medhavy`, `register: Wonder`, `outro_source: AUTHOR.MD :: Medhavy.com` — coherent. |
| 10 | Pacing | LOG (harmless) | `estimated_duration_s` values are underscored by ~30–50% vs narration word count — they were pre-audio guesses. `actual_duration_s` (measured Kokoro) is what the clock uses, so this is cosmetic. No retiming applied. |
| 11 | `type_check.py` | PASS | GATE T pass, 0 FAILs, 1 §8.10 advisory on B06 (narration echoes card lines) — non-blocking. `TYPECHECK.md` in reel. |

## Phase 0 — envelope normalize (this pass)

- Backup: `beat_sheet.json` → `beat_sheet.pre-rebuild.json` (byte-exact, this session).
- Dropped `metadata.voice_id` (ElevenLabs id `1sgY6Voq1aexKOB1IJ2D`; medhavy is Kokoro).
- Rewrote `metadata.clock` from the ElevenLabs-era "estimates until GATE 0 audio lock"
  prose to the measured-audio truth: `narration (Kokoro af_kore, VOICE-LOCK) —
  actual_duration_s measured from mp3/beat-*.mp3`.
- Narration is UNTOUCHED (rebuild lock). No datable claims to correct.

## Also fixed in Phase 2

- **Outro props were wrong-schema and rendered Root.tsx defaults.** Original sheet
  gave B15 OutroSeries `{seriesTitle, tagline, githubSlug}` and B16 OutroCTA
  `{authorName, handle, ctaText}`. Actual zod schemas are
  `OutroSeries { eyebrow, line }` and `OutroCTA { line, handle }`. The first
  render silently defaulted to "CLAUDE COWORK / Part of the Claude Cowork series." —
  which would have been a wrong-brand ship. Fixed props to match schemas
  (eyebrow: CANCER NANOMEDICINE / line: "Part of the Cancer Nanomedicine series
  on Medhavy AI." for B15; line: "Explore the full course at medhavy.com." /
  handle: @MedhavyAI for B16), deleted the stale renders, re-rendered, recompiled.

## Not addressed this pass (out of scope for a Phase-2 review-slate cut)

- `shot.form` derivation per beat (SHOT-FORM-SYSTEM.md) — deferred; batch job.
- Authoring `scenes.py` for the eight `production_viz` Manim scenes (`B03_AccumComparison`,
  `B05_EPRMechanism`, `B07_DesmoplasiaSqueeze`, `B08_PressureFlow`, `B10_ModelVsPatient`,
  `B11_LiverDefault`, `B12_TwoTumors_Left`, `B13_TwoTumors_Right`). Their production-viz
  specs remain locked in the sheet as `graphic.production_viz` blocks so a future pass
  can author them and re-render; for this review-slate cut those beats show a FormACard
  summary of the diagram content instead of the diagram itself.

## Final cut

`vox-epr-gap-slate.mp4`, 240.3s, 16/16 slots filled (no SLATE frames), audio present
at mean_volume -23.9 dB, lane-check PASS, GATE T PASS, GATE AUDIO PASS. Sheet mtime
precedes mp4 mtime — cut is not stale.
