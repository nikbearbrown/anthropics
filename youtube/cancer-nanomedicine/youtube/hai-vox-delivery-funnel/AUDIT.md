# AUDIT.md — hai-vox-delivery-funnel

Audit run 2026-08-27 per unattended film-factory phase 1 checklist.

## Phase 0 — rebuild contract

- **Snapshot** — `beat_sheet.pre-rebuild.json` written byte-exact before any edit. **FIXED.**
- **Narration lock** — every B01–B13 `narration_text` verbatim from pre-rebuild. Zero datable-claim rewrites needed. **PASS.**
- **Envelope** — `voice_id`/`clock`/`_variant_todo` DROPPED; `engine=kokoro`, `voice=nbbhuman`, `voice_kokoro=am_onyx`, `folderLabel=@humanitariansai` normalized. **FIXED.**
- **shot.form** — 6 GRAPHIC beats with fake manim scene names (`B04_FiveSteps`, `B05_Drain1`, etc.; no `scenes.py` on disk) reshaped to real Remotion patterns (FormBCard × 5, FormACard × 1). Details in REBUILD-LOG.md. **FIXED.**
- **Non-Claude skin retained** — B12 OutroSeries / B13 OutroCTA re-props'd to HAI channel (`CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`). Pre-rebuild used legacy `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` props that Remotion silently fell back to Claude Cowork defaults — that would have Claude-washed the HAI reel. **FIXED.**

## Phase 1 — audit

1. **Stale renders** — no `*.mp4` in folder pre-run; no delete needed. **PASS.**
2. **Bookends** — HAI reel has no Claude bookends by design (rebuild contract §Cold-Open exempts non-claude channels). Legit-absent. **PASS.**
3. **Spark lines** — N/A (no `ClaudeComposerAsk` beats in this reel). **PASS.**
4. **Verdict** — N/A (no BVDT beat; HAI reel closes with B11 RECAP endcard + HAI outros). `verdict_audit.py` reports no violations because there's nothing that looks like a verdict card to lint. **PASS.**
5b. **Chart text** — no Manim/D3 charts. FormBCard labels are short category nouns (1–3 words: "1. Circulate", "Liver clearance", "Cross the wall", etc.). Subs are single short sentences. **PASS.**
5. **Card text** — no FormA/FormB item has placeholder sub; every label fits within its card in the QC contact sheet (verified via `qc-sheet.png`). B02 FormACard rewritten to drop §8.10 recite-the-card score from 1.00 → 0.50. **FIXED.**
6. **Punt sweep** — zero gen-AI asks (`STILL·ai` beat B02 rendered as FormACard text; not a request for a gen-AI clip). Zero unfilled fill_slates/remotion_scenes slates for pipeline-owned beats. Zero DoodleScene/DoodleChart. Zero `STILL src=archive` for conceptual content. **PASS.**
7. **Card-only reel** — 9 of 13 beats are Remotion pattern draws (FormBCard × 5, FormACard × 2, OutroSeries, OutroCTA). Not card-only. **PASS.**
8. **Lens audit** — two moves run:
   - **Plato (artifact vs world):** B02 sets the artifact (ligand-labeled particle killing in cell culture). B01/B03/B10/B11 set the world (0.7% actually reaches the tumor in vivo). B08–B09 name the relationship: the culture dish reads only step 4; the world requires steps 1–5.
   - **Descartes (checklist / what would falsify):** the five-step chain (B04–B07) is Cartesian doubt made structural — the claim "targeting ligand delivers the payload" is broken into a five-item falsification checklist, each step of which can independently disprove the whole.
   **PASS.**
9. **Brand fields** — `folderLabel=@humanitariansai`, `engine=kokoro`, `voice_kokoro=am_onyx`. Outros carry HAI series + HAI CTA. Voice is explainer, no persona claim. Coherent. **FIXED.**
10. **Pacing** — all beats within 2.0–3.4 wps (B01 = 22 words / 8.7s = 2.53 wps; B10 = 47 words / 16.06s = 2.93 wps; …). **PASS.**
11. **type_check.py** — GATE T PASS. Two §8.10 advisories: B02 (0.50, softened) and B10 (0.83, the illustrative-numbers chart — the point of the visual is to show the numbers narration names, redundancy is structural). Zero FAILs. **PASS.**

## Phase 2 — build

- `remotion_scenes.py` — 9/9 Remotion beats rendered to `media/B*.mp4`. Initial pass failed 3 FormBCard beats (B04, B06, B07) on missing icon SVGs (`circle-dot`, `arrow-right`, `download`); swapped to `life-buoy`, `frame`, `hand` (present in `public/form-b-icons/`), re-rendered — all 9 OK.
- `compile.py --review` — 13/13 beats compiled; lane_check PASS; **GATE AUDIO PASS (mean_volume −24.2 dB)**; motion histogram warns fade @ 61% (informational, expected given FormBCard-heavy content).
- Output: `hai-vox-delivery-funnel-slate.mp4` — 123.5 s, 1280×720 review cut with per-beat labels + timecodes.
- Gate V (frame read) — sampled 13 frames across the timeline (B01–B13 span). All Remotion frames render within the safe area; text is legible; no overlap between title and items; HAI outro properly branded (no Claude-wash); slate cards are clean placeholders as intended. **PASS.**
- **MP4 mtime 4 s newer than beat_sheet.json** (stale-check: `mp4=1787862839.673`, `sheet=1787862835.983`). **PASS.**

## build.status Counter

```
VIDEO: 9   SLATE: 4   (B01 title, B03 question, B09 quote, B11 endcard)
```

## Blockers

None. Reel is a valid slate review cut.
