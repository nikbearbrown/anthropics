# AUDIT.md — hai-vox-targeting-uptake

Audit run 2026-08-28 per unattended film-factory phase 1 checklist.

## Phase 0 — rebuild contract

- **Snapshot** — `beat_sheet.pre-rebuild.json` written byte-exact before any edit. **FIXED.**
- **Narration lock** — every B01–B12 `narration_text` verbatim from pre-rebuild. Zero datable-claim rewrites needed. **PASS.**
- **Envelope** — `voice_id`/`clock`/`_variant_todo`/`build` DROPPED; `engine=kokoro`, `voice=nbbhuman`, `voice_kokoro=am_onyx`, `folderLabel=@humanitariansai`, `channel_title=@HumanitariansAI` normalized. **FIXED.**
- **shot.form** — 7 GRAPHIC beats with fake manim scene names (`B03_Question`, `B04_DeliveryChain`, `B05_CultureVsBody`, `B06_AccumulationDrivers`, `B07_LastStep`, `B08_WrongFix`, `B09_FolateExample`; no `scenes.py` on disk) reshaped: B03 → CARD kind=question (like peer HAI B03); B04–B08 → FormBCard × 5; B09 → FormACard. Details in REBUILD-LOG.md. **FIXED.**
- **Non-Claude skin retained** — B11 OutroSeries / B12 OutroCTA re-props'd to HAI channel (`CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`). Pre-rebuild used legacy `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` props that Remotion silently fell back to Claude Cowork defaults — that would have Claude-washed the HAI reel. **FIXED.**

## Phase 1 — audit

1. **Stale renders** — no `*.mp4` in folder pre-run; no delete needed. **PASS.**
2. **Bookends** — HAI reel has no Claude bookends by design (rebuild contract §Cold-Open exempts non-claude channels). Legit-absent. **PASS.**
3. **Spark lines** — N/A (no `ClaudeComposerAsk` beats in this reel). **PASS.**
4. **Verdict** — N/A (no BVDT beat; HAI reel closes with B10 RECAP endcard + HAI outros). `verdict_audit.py` reports no violations for this slug because there is no `ClaudeVerdictArtifact` beat to lint. **PASS.**
5b. **Chart text** — no Manim/D3 charts. FormBCard labels are short category nouns (1–4 words: "1. Blood", "2. Vessel wall", "3. Tumor tissue", "4. Cell surface", "Step 4 visible", "Steps 1–3 invisible", "Circulation half-life", "Vessel permeability", "Targeting ligand", "Arrival", "Internalization", "Bottleneck at steps 1–2", "Ligand fixes step 4"). Subs are single short sentences. **PASS.**
5. **Card text** — no FormA/FormB item has placeholder sub; every label fits within its card (verified in sampled frames at t=42s / 65s / 88s / 105s). B02 FormACard rewritten to compress the narration (recite score 0.18). B09 FormACard shows 0.88 recite (advisory only — this is the illustrative-numbers example beat where the numbers narrated ARE what the card must display; type_check flags it as ADVISORY, not FAIL). **FIXED.**
6. **Punt sweep** — zero gen-AI asks (`STILL·ai` beat B02 rendered as FormACard text; not a request for a gen-AI clip). Zero unfilled fill_slates/remotion_scenes slates for pipeline-owned beats. Zero DoodleScene/DoodleChart. Zero `STILL src=archive` for conceptual content. **PASS.**
7. **Card-only reel** — 9 of 12 beats are Remotion pattern draws (FormBCard × 5, FormACard × 2, OutroSeries, OutroCTA). Not card-only. **PASS.**
8. **Lens audit** — two moves run:
   - **Plato (artifact vs world):** B01/B02 set the artifact (a ligand-labeled particle that binds ten-fold better *in culture*). B01/B02/B09 set the world (equal tumor accumulation *in the animal*, 2.1% vs 1.9%). B03–B08 name the relationship: the artifact reads step 4 only; the world requires all four steps, and steps 1–2 dominate accumulation.
   - **Descartes (checklist / what would falsify):** the four-step chain (B04) is Cartesian doubt made structural — the claim "targeting ligand increases tumor accumulation" is decomposed into a four-item chain, three of which are upstream of the ligand's action and can independently falsify the claim (B06 names circulation half-life + vessel permeability as the actual determinants).
   **PASS.**
9. **Brand fields** — `folderLabel=@humanitariansai`, `channel_title=@HumanitariansAI`, `engine=kokoro`, `voice_kokoro=am_onyx`. Outros carry HAI series + HAI CTA. Voice is explainer, no persona claim. Coherent. **FIXED.**
10. **Pacing** — spot-checked: B01 = 31 words / 11.43s = 2.71 wps; B04 = 32 words / 11.71s = 2.73 wps; B08 = 44 words / 12.95s = 3.40 wps; B09 = 34 words / 16.64s = 2.04 wps. All within 2.0–3.4 wps. **PASS.**
11. **type_check.py** — GATE T PASS (TYPECHECK.md). One §8.10 advisory: B09 recites 0.88 — the illustrative-numbers card; the numbers narration cites ARE the card content by design (2.1%, 1.9%, 68%, 12%). Advisory, not FAIL. Zero blocking violations. **PASS.**

## Phase 2 — build

- `remotion_scenes.py` — 9/9 Remotion beats rendered to `media/B*.mp4`. First pass succeeded with icons from the library (`life-buoy`, `frame`, `layers`, `hand`, `circle-x`, `shield`, `target`). Zero re-render needed.
- `compile.py --review --height 720` — 12/12 beats compiled; content-check PASS; frame-check PASS; lane_check PASS (known_slates=['B01','B03','B10'] — all CARD, not pipeline-owned); **GATE AUDIO PASS (mean_volume −23.8 dB)**; motion histogram warns fade @ 66% (informational — 8 Remotion-fade beats are expected on a FormBCard-heavy reel).
- Output: `hai-vox-targeting-uptake-slate.mp4` — 128.4s, 1280×720 review cut with per-beat labels + timecodes.
- Gate V (frame read) — sampled 8 frames across the timeline (contact sheet + t=42s B04 / t=65s B06 / t=82s B08 mid-reveal / t=88s B08 both items / t=105s B09 / t=125s B12 outro). All Remotion frames render within the safe area; text is legible; no overlap between title and items; HAI outro properly branded (no Claude-wash: "CANCER NANOMEDICINE", "Part of the Cancer Nanomedicine series from Humanitarians AI.", "@humanitariansai"); slate cards are clean placeholders as intended (B01 TITLE / B03 QUESTION / B10 ENDCARD). Zero BLOCKER, zero MAJOR on real beats. **PASS.**
- **MP4 mtime 4 s newer than beat_sheet.json** (stale-check: `mp4=1787933382`, `sheet=1787933378`). **PASS.**

## build.status Counter

```
VIDEO: 9   SLATE: 3   (B01 title, B03 question, B10 endcard)
```

## Blockers

None. Reel is a valid slate review cut.
