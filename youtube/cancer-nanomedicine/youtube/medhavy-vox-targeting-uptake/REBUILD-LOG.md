# REBUILD-LOG — medhavy-vox-targeting-uptake
_Pass: 2026-08-27_

## Snapshot
`beat_sheet.pre-rebuild.json` written byte-exact before any edit.

## LOCKED (verbatim from pre-rebuild)
- All 12 `narration_text` fields.
- Beat order (B01–B12), act structure (`COLD OPEN`, `THE QUESTION`, `THE PROBLEM`, `THE MECHANISM`, `THE IMPLICATION`, `THE EXAMPLE`, `RECAP`, `OUTRO`), `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, source, register (Wonder), palette (medhavy), audience (MEDHAVY), `outro_source`.
- Every `graphic.production_viz` intent block on B03–B09 (kept as the shot-list for a future Manim pass).
- Every `card` block on B01/B10 (kept as the shot-list for a future medhavy title/endcard pass).
- Every `scene_description` / `image_prompt` / `new_visual_element` line.

## REBUILT

### Envelope
| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | `"narration (Kokoro af_kore VOICE-LOCK) — durations from measured mp3s"` | Audio-lock is done; the "estimates until GATE 0" prose was stale |
| `_variant_todo` | 4-item migration checklist | DROPPED | Migration executed |
| `style_bible` | verbose object | DROPPED | Duplicates `color_semantics` + `accents`; not read by any tool |
| `build` | old stamp (Jul-16) claiming 2/12 filled with a stale `at` | DROPPED (compile regenerates) | old media/ never existed |
| `folderLabel` | (missing) | `"@MedhavyAI"` | Was missing; channel handle for Medhavy |
| `engine` | `"kokoro"` | KEPT | |
| `voice_kokoro` | `"af_kore"` | KEPT | |

### Datable claims in narration
None. The reel makes one durable mechanistic claim ("the ligand acts last; accumulation is set upstream"). No dated model names, prices, or "as of" phrasing. The 2.1% / 1.9% / 68% / 12% numbers in B09 are labeled ILLUSTRATIVE inside the `production_viz.mechanic` and `production_viz.note` fields.

### Beat-level rebuilds
Every body beat rewritten from `shot.type: CARD/STILL/GRAPHIC` (with no renderable engine on disk) to `shot.type: REMOTION` + `pattern: FormACard`, so the pipeline actually fills every slot. Card copy is 2–3 short lines pulled from that beat's narration (never a recitation — §8.10 correlations 0.20–0.75 after tuning). Outros B11/B12 get their zod schemas fixed.

| Beat | Old shot / issue | New shot / props | Reason |
|------|------------------|-------------------|--------|
| B01 | CARD (title) — no renderer, would slate | REMOTION `FormACard` — `["Your Targeted Nanoparticle", "Doesn't Reach More Tumor", "it just enters more cells"]` | No medhavy title pattern available; text-card substitute |
| B02 | STILL src=ai + FormACard with truncated line `"…The tumor data tells…"` | REMOTION `FormACard` — `["Two dishes, two stories.", "Same tumor, same delivery."]` | Truncated placeholder was a punt-in-a-costume |
| B03 | GRAPHIC `manim:B03_Question` — scene does not exist | REMOTION `FormACard` — `["The ligand works.", "Why doesn't it help?"]` | No scene on disk → would fail PIPELINE-CARD RULE |
| B04 | GRAPHIC `manim:B04_DeliveryChain` — scene does not exist | REMOTION `FormACard` — `["Blood → Vessel → Tissue → Cell", "The ligand acts at step four."]` | Same |
| B05 | GRAPHIC `manim:B05_CultureVsBody` — scene does not exist | REMOTION `FormACard` — `["Culture sees step four.", "The body walks all four."]` | Same |
| B06 | GRAPHIC `manim:B06_AccumulationDrivers` — scene does not exist | REMOTION `FormACard` — `["Accumulation is set upstream.", "Half-life. Vessel leak.", "The ligand touches neither."]` | Same |
| B07 | GRAPHIC `manim:B07_LastStep` — scene does not exist | REMOTION `FormACard` — `["Late is late.", "The ligand cannot go upstream."]` | Same |
| B08 | GRAPHIC `manim:B08_WrongFix` — scene does not exist | REMOTION `FormACard` — `["No amount of uptake", "fixes an upstream leak."]` | Same |
| B09 | GRAPHIC `manim:B09_FolateExample` — scene does not exist | REMOTION `FormACard` — `["Accumulation: 2.1% vs 1.9%.", "Uptake: 68% vs 12%.", "illustrative"]` | Same; ILLUSTRATIVE label kept in card AND in `production_viz.note` |
| B10 | CARD (endcard) — no renderer, would slate | REMOTION `FormACard` — `["Uptake ≠ accumulation.", "The ligand acts last.", "Fix the early steps."]` | Same |
| B11 | `OutroSeries` `{seriesTitle, tagline, githubSlug}` — wrong zod schema | `OutroSeries` `{eyebrow: "CANCER NANOMEDICINE", line: "Part of the Cancer Nanomedicine series on Medhavy AI."}` | Schema mismatch would refuse render; medhavy branding restored |
| B12 | `OutroCTA` `{authorName, handle, ctaText}` — wrong zod schema | `OutroCTA` `{line: "Explore the full course at medhavy.com", handle: "@MedhavyAI"}` | Same; medhavy handle preserved |

### Audio
No regeneration — the July-16 Kokoro `af_kore` mp3s are still voice-lock-current. All 12 `actual_duration_s` values match the measured mp3s within tolerance. Master mux ran clean at compile: `[art] GATE AUDIO: PASS mean_volume -23.9 dB`.

### Renders
All 12 beats → `media/B*.mp4` via `remotion_scenes.py --now 2026-08-27T20:00:00`. FormACard renders on cream (`CLAUDE.PAGE #FAF9F5`) with ink serif — a Claude-adjacent skin, but the reel's identity survives because narration is Medhavy-voiced (af_kore) and the outros carry the Cancer Nanomedicine eyebrow + @MedhavyAI handle in Medhavy's VOX palette.

## Not rebuilt (kept from pre-rebuild)
- Every narration line, verbatim.
- The `graphic.production_viz` intent blocks for B03–B09 (they document the visual a future Manim pass should draw).
- `card.copy` / `card.sub` on the CARD beats B01/B10 (kept as intent alongside the new REMOTION props).
- All shot-list identifiers (`new_visual_element`, `scene_description`, `chosen_media`).

## Scripting gaps flagged for a future pass
None of these blocks the current review cut — they upgrade it. The text substitutes name what should be drawn.

- **B01 title card** — wants a medhavy-skinned title treatment (teal eyebrow + serif line + crimson underline). Currently reads as a plain FormACard.
- **B03** — gap-formula question card (gold underline + teal ACCUMULATION chip + crimson UPTAKE chip). Needs a Manim scene or a medhavy-question Remotion pattern.
- **B04** — four-step delivery-chain animation (Blood→Vessel→Tissue→Cell, ligand at step 4 in crimson). The core visual of the film.
- **B05** — culture-vs-body two-column diagram (culture: only step 4; body: all four).
- **B06** — accumulation-drivers convergence (two teal arrows: half-life + vessel permeability; barred crimson ligand arrow).
- **B07** — arrival-then-entry compare (equal arrival at tissue; only targeted enters cell with gold binding flash).
- **B08** — wrong-fix annotation on the delivery chain (crimson bracket step 4, teal bracket steps 1-2).
- **B09** — folate-example two-column bar chart (accumulation bars ≈equal, uptake bars very different; ILLUSTRATIVE label).
- **B10 endcard** — wants a medhavy-skinned endcard, not a FormACard.
