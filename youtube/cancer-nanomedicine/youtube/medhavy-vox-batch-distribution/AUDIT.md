# AUDIT — medhavy-vox-batch-distribution
_Pass: 2026-08-28_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` snapshot created byte-exact BEFORE any edit ✓
- Envelope stripped of dead ElevenLabs-era fields:
  - DROPPED `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs voice id)
  - DROPPED `clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below…" — ElevenLabs migration artifact)
  - DROPPED `_variant_todo[]` (migration-scaffolding checklist, obsolete)
  - DROPPED stale `build{}` block (falsely claimed B13/B14 as `VIDEO` with `filled_by: "media"` though no `media/` dir existed)
- KEPT: `engine: kokoro`, `voice_kokoro: af_kore` (VOICE-LOCK); title/slug/subtitle/topic/purpose/aspect_ratio/style_preset/isotype_mark/accents/ground/style_bible/color_semantics/note/audience/register/palette/outro_source intact
- ADDED: `folderLabel: "@MedhavyAI"` (missing — same fix as sibling `medhavy-vox-complexity-yield`)
- Narration LOCKED — every B01–B14 `narration_text` verbatim from pre-rebuild. Zero narration edits.
- Shot envelope: every body beat converted from CARD/GRAPHIC/STILL/DOCUMENT slate carrying a punt-costume `build` block to `shot.type = REMOTION` with `shot.remotion.pattern = FormACard`. The original `card`/`graphic`/`document`/`scene_description` blocks are preserved alongside as authoring intent (mirrors sibling pattern).

## Phase 1 Audit

### 1. Stale renders — PASS
No `*.mp4` in the reel folder pre-run. Only `clips/master.m4a` from Jul 16 (audio-only assembly, not a video render — informational). Nothing deleted.

### 2. Bookends — PASS (legitimately absent)
Non-Claude channel (medhavy palette, `af_kore` voice, Wonder register). Rebuild contract §3 exempts non-claude channels from Claude bookends (`B00`/`BVDT`/`BHTF`/`BOUT`). Format is body beats (B01–B12) + `OutroSeries` (B13) + `OutroCTA` (B14). Matches sibling vox medhavy pattern.

### 3. Spark lines — PASS (N/A)
No `ClaudeComposerAsk` beats in this reel (channel design).

### 4. Verdict — PASS (N/A)
No BVDT beat by channel design. Closing FormACard B12 carries the compressed claim in its own words ("A nanoparticle is a distribution, not a molecule."). `verdict_audit.py` — nothing to audit; no template default text present.

### 5b. Chart text — PASS (N/A after conversion)
No Manim charts on disk. B04–B08, B10, B11 originally called out Manim scenes (`B04_SmallMolecule`, `B05_NanoCloud`, `B06_TwoHistograms`, `B07_PDIScale`, `B08_ThreePopulations`, `B10_MatchMeanVsDistribution`, `B11_ExampleComparison`) but no `scenes_std.py` / `vox_scenes.py` / equivalent exists in the folder or its neighbors. Converted to FormACard text summaries (see Check 6). Card lines use 1–5 word tokens with one full-sentence lead line each. Numbers written literally (PDI 0.07, PDI 0.31, 98 nm). Bars-heights disagreement risk (LENS-NOTES.md 5b) N/A — no bars rendered.

### 5. Card text — FIXED (all beats)
B02's old FormACard `props.lines` was a single narration slice truncated with `"…"` ("A clinical-grade liposomal batch clears from a patient's bloodstream in forty-five…") — a placeholder stripe, not a real card layout. Rewritten to a real 3-line card: "Two liposome batches — both 100 nm / one clears in 45 minutes / one circulates for 6 hours". Every other FormACard authored fresh from the beat's own narration nouns/numbers, no placeholder subs, no truncation.

### 6. Punt sweep — FIXED (12 beats)
Original sheet: 5 gen-AI-clip punt costumes on B01/B02/B03/B09/B12 (`"YOU → 5–10s gen-AI clip → pantry"`) and 7 pipeline punts on B04–B08/B10/B11 (`"PIPELINE → render animated_graphics.py scene B*"` — with zero scene classes ever authored on disk). Fixed as follows:

- **B01, B03, B12** — CARD beats → converted to FormACard with real lines drawn from `card.copy`/`card.sub` (title / question / endcard).
- **B02** — was `STILL src=ai` for an editorial-illustration vial photograph. No such illustration exists on disk. Converted to FormACard naming the two batches explicitly with their clearance-time contrast. Logged as a photography gap (a real dual-vial editorial illustration would upgrade this beat).
- **B04–B08, B10, B11** — were `GRAPHIC` with named Manim scenes that do not exist on disk. Converted to FormACard text summaries of what each chart should show, with the narration's key numbers written explicitly (98 nm, PDI 0.07, PDI 0.31, ~60% delivery, ≥0.2 threshold, three population regions). Honest text substitutes — each logged as needing a Manim upgrade in a future scenes_std.py pass.
- **B09** — was `DOCUMENT` (highlighted quote). No document-highlight pipeline exists. Converted to FormACard rendering the NCI framework principle as a 3-line card with attribution.
- **B13, B14** — OutroSeries/OutroCTA props were wrong schema (`seriesTitle`/`tagline`/`githubSlug`, `authorName`/`handle`/`ctaText`) — the Remotion components would silently fall back to Claude defaults, Claude-washing a Medhavy reel. Fixed to correct schema (`{eyebrow, line}` for OutroSeries, `{line, handle}` for OutroCTA) with Medhavy content ("CANCER NANOMEDICINE" eyebrow, "Explore the full course at medhavy.com" line, "@MedhavyAI" handle). Same fix pattern as sibling `medhavy-vox-complexity-yield`.

Zero remaining `YOU → gen-AI clip`, zero `DoodleScene`/`DoodleChart`, zero `STILL src=archive/ai` on animatable content, zero unfilled `remotion_scenes` slates in the final build. Zero pipeline-owned SLATE in the master.

### 7. Card-only reel — LOGGED
Every body beat now renders as FormACard (text). This IS a card-only reel in this pass — a consequence of no Manim scene library existing for the seven visualization beats and no illustration for B02. Scripting gap logged: the reel wants at least three drawn figures (the side-by-side histograms B06, the PDI number line B07, the Batch A/B comparison B11). Would upgrade to a mixed-media reel with a proper scenes_std.py pass.

### 8. Lens audit — PASS (2+ moves present)
Scientific mechanism explainer (mean ≠ distribution, PDI as the polydispersity metric). Moves earned:
- **Descartes (checklist):** B08 decomposes the wide distribution into three pharmacokinetically distinct populations (small / mid / large) — a Cartesian split of a compound object into independently characterizable parts. ✓
- **Popper (falsification stated in advance):** B03 states the falsifying observation directly: "Regulators say they are not the same product." B04–B10 then walk through what fails when you use one-number identity for a distribution-shaped object. ✓
- **Hume (confidence is a property of the model):** B11 labels the Batch A / Batch B numbers "illustrative" explicitly in both narration ("An illustrative example") and card ("illustrative — both label 98 nm"). The 40% delivery gap is a modeled prediction, not an empirical measurement. ✓
- **Plato (artifact vs world):** B02, B09, B11 distinguish the artifact (the "100 nm" label, the reported mean, the specification document) from the world (the actual distribution of particle sizes, the actual clearance behavior, the actual delivery). ✓

### 9. Brand fields — FIXED
- `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs id) → DROPPED ✓
- `clock` (ElevenLabs prose) → DROPPED ✓
- `folderLabel: "@MedhavyAI"` ✓ (added)
- `engine: kokoro`, `voice_kokoro: af_kore` ✓ (medhavy voice)
- B13/B14 Medhavy channel branding restored (was silently Claude-defaulting)
- Persona: narration is third-person / question ("Two injectable nanoparticles…", "Here's why…"). No Bear/Liam persona claim → no voice-swap risk. `af_kore` is a female Kokoro voice; consistent with medhavy channel default.

### 10. Pacing — LOG
Using measured Kokoro af_kore durations vs word counts:

| Beat | ~Words | actual_duration_s | ~wps | Note |
|------|--------|-------------------|------|------|
| B01  | 36     | 12.97             | 2.78 | ✓    |
| B02  | 48     | 17.75             | 2.70 | ✓    |
| B03  | 37     | 12.89             | 2.87 | ✓    |
| B04  | 45     | 14.95             | 3.01 | ✓    |
| B05  | 49     | 15.74             | 3.11 | ✓    |
| B06  | 46     | 16.73             | 2.75 | ✓    |
| B07  | 45     | 17.69             | 2.54 | ✓    |
| B08  | 49     | 17.47             | 2.80 | ✓    |
| B09  | 48     | 16.13             | 2.98 | ✓    |
| B10  | 50     | 16.87             | 2.96 | ✓    |
| B11  | 89     | 28.25             | 3.15 | ✓    |
| B12  | 55     | 19.14             | 2.87 | ✓    |
| B13  | 11     |  4.29             | 2.56 | ✓    |
| B14  |  6     |  2.50             | 2.40 | ✓    |

All beats within 2.0–3.4 wps. No pacing flags.

### 11. type_check.py — GATE T: PASS
Ran on final sheet. Six §8.10 REDUNDANCY ADVISORIES (B03 0.88, B04 1.00, B05 1.00, B06 0.89, B07 1.00, B10 0.83 — narration recites the card). Structural, expected: narration is LOCKED verbatim (rebuild contract §2) and the FormACard text is a compressed transcript of the narration by construction (the numbers/nouns/labels in the narration ARE the visual since the Manim charts do not exist). Advisories only — do not block cut. Same pattern as sibling `medhavy-vox-complexity-yield`. Zero validators loosened.

## Phase 2 — Build

- **Audio:** Kokoro `af_kore`, 14/14 mp3 files regenerated fresh, durations measured back into sheet (obsoleted the Jul 16 ElevenLabs-era mp3s).
- **Remotion:** all 14 pattern beats rendered → `media/B*.mp4` (FormACard × 12 + OutroSeries + OutroCTA).
- **Compile:** `compile.py . --review` — content-check PASS, frame-check PASS, lane-check PASS (14/14 filled, `known_slates=[]`). No lane violations.
- **Output:** `vox-batch-distribution-slate.mp4` — 214.4 s, 1280×720 review cut with per-beat labels and timecodes.
- **Gate audio:** `mean_volume -24.0 dB`, `max_volume -6.5 dB` (threshold: > −40 dB) ✓
- **Gate V — frame read (7+ sampled frames across timeline):**
  - B01 (0s) — title, cream ground, EB Garamond serif, "Same Average Size," / "Different Product" / "why batches aren't like pills", legible, well within safe area ✓
  - B03 (30s) — question card ("Same mean particle size. / Regulators: not the same product. / Why isn't the average enough?"), legible ✓
  - B05 (58s) — "A nanoparticle is a population, / not a single structure / the cloud IS the product", legible ✓
  - B07 (91s) — "PDI = polydispersity index / near 0 → narrow, monodisperse / above 0.2 → regulatory problem", legible; arrow glyph renders clean ✓
  - B08 (108s) — "A high-PDI batch is three products / small → rapid clearance / mid → designed behavior / large → liver and spleen", 4-line variant renders within safe area ✓
  - B11 (159s) — "Batch A · PDI 0.07 · full delivery / Batch B · PDI 0.31 · ~60% delivery / illustrative — both label 98 nm", middle-dot separator legible, numbers legible ✓
  - B12 (187s) — endcard, cream ground, "A nanoparticle is a distribution, / not a molecule. / CANCER NANOMEDICINE", legible ✓
  - B13 (207s) — Medhavy OutroSeries — CANCER NANOMEDICINE eyebrow + "Part of the Cancer Nanomedicine series on Medhavy AI." + crimson hairline underline. Renders on WHITE (component default; consistent across siblings). ✓
  - B14 (211s) — Medhavy OutroCTA — "Explore the full course at medhavy.com" + SUBSCRIBE pill + @MedhavyAI handle. Renders on WHITE (component default). ✓
  - Zero BLOCKER, zero MAJOR on any beat.
- **Post-build punt sweep:** `build.status` Counter reported by compile: `{VIDEO: 14}`. Zero slates. Zero pipeline-owned SLATE, zero gen-AI-in-master, zero remaining punts.
- **Stale check:** mp4 mtime `1787950646` vs sheet mtime `1787950639` — mp4 is 7 s NEWER ✓

## Output

`vox-batch-distribution-slate.mp4` — 214.4 s, audio present (−24.0 dB), mp4 newer than beat_sheet.json (Δ+7s). DONE (as a text-heavy card-only review slate cut; seven drawn-graphic beats and one editorial illustration are honest FormACard text substitutes pending a `scenes_std.py` / illustration pass).
