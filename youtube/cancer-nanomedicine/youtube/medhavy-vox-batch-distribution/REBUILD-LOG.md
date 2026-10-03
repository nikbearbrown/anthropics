# REBUILD-LOG — medhavy-vox-batch-distribution
_Pass: 2026-08-28 · rebuild contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`_

## Snapshot
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild `beat_sheet.json` (20,230 bytes) captured before any edit.

## Narration — LOCKED
Every B01–B14 `narration_text` verbatim from pre-rebuild. Zero narration edits, zero datable-claim edits needed (source text carries no dated claims — the PDI, DLS, NCI framework, and Doxil references are timeless).

## Envelope changes (metadata)
| Field | Before | After | Reason |
|---|---|---|---|
| `voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | *dropped* | ElevenLabs voice id — dead field per VOICE-LOCK. |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | *dropped* | ElevenLabs-migration prose — dead field. |
| `_variant_todo` | 4-line checklist | *dropped* | Migration-scaffolding checklist, obsolete after Kokoro conversion. |
| `build{}` | claimed B13/B14 as `VIDEO`, filled 2/14 at 2026-07-16 | *dropped (recomputed by compile.py)* | Stale — media/ dir did not exist. |
| `folderLabel` | absent | `"@MedhavyAI"` | Missing on this reel; matches sibling medhavy variant convention. |

Kept intact: `slug`, `title`, `subtitle`, `topic`, `purpose`, `aspect_ratio`, `style_preset`, `isotype_mark`, `accents`, `ground`, `style_bible`, `color_semantics`, `note`, `total_estimated_duration_seconds`, `audience`, `derived_from`, `register`, `palette`, `outro_source`, `engine`, `voice_kokoro`.

## Shot envelope conversions (per beat)

Each body beat's shot envelope moved from a punt costume (STILL src=ai / CARD-only-slate / DOCUMENT / GRAPHIC-with-nonexistent-manim-scene) to a proper Remotion FormACard beat, with the original `card`/`graphic`/`document`/`scene_description` block kept alongside as authoring intent (mirrors sibling `medhavy-vox-complexity-yield`).

- **B01** title CARD → FormACard `lines: ["Same Average Size,", "Different Product", "why batches aren't like pills"]`.
- **B02** STILL src=ai (photo of two vials — no illustration on disk) → FormACard `lines: ["Two liposome batches — both 100 nm", "one clears in 45 minutes", "one circulates for 6 hours"]`. Fixes the pre-rebuild placeholder stripe `["A clinical-grade liposomal batch clears from a patient's bloodstream in forty-five…"]`.
- **B03** question CARD → FormACard `lines: ["Same mean particle size.", "Regulators: not the same product.", "Why isn't the average enough?"]`.
- **B04** GRAPHIC `B04_SmallMolecule` (scene not on disk) → FormACard `lines: ["Small molecule = one structure", "batch matches, or it doesn't", "one measurement decides"]`.
- **B05** GRAPHIC `B05_NanoCloud` (scene not on disk) → FormACard `lines: ["A nanoparticle is a population,", "not a single structure", "the cloud IS the product"]`.
- **B06** GRAPHIC `B06_TwoHistograms` (scene not on disk) → FormACard `lines: ["Both batches: mean 98 nm", "Batch A — narrow spike", "Batch B — wide bell, same center"]`.
- **B07** GRAPHIC `B07_PDIScale` (scene not on disk) → FormACard `lines: ["PDI  =  polydispersity index", "near 0  →  narrow, monodisperse", "above 0.2  →  regulatory problem"]`.
- **B08** GRAPHIC `B08_ThreePopulations` (scene not on disk) → FormACard `lines: ["A high-PDI batch is three products", "small  →  rapid clearance", "mid  →  designed behavior", "large  →  liver and spleen"]` (4 lines — legibility verified in Gate V).
- **B09** DOCUMENT quote (no document-highlight pipeline) → FormACard `lines: ["Two batches, same mean, different PDIs", "are not the same product", "— NCI framework principle"]`.
- **B10** GRAPHIC `B10_MatchMeanVsDistribution` (scene not on disk) → FormACard `lines: ["Match the mean  →  one point", "Match the distribution  →  the population", "the distribution is the product"]`.
- **B11** GRAPHIC `B11_ExampleComparison` (scene not on disk) → FormACard `lines: ["Batch A · PDI 0.07 · full delivery", "Batch B · PDI 0.31 · ~60% delivery", "illustrative — both label 98 nm"]`.
- **B12** endcard CARD → FormACard `lines: ["A nanoparticle is a distribution,", "not a molecule.", "CANCER NANOMEDICINE"]`.
- **B13** OutroSeries props schema fixed: `{seriesTitle, tagline, githubSlug}` → `{eyebrow: "CANCER NANOMEDICINE", line: "Part of the Cancer Nanomedicine series on Medhavy AI."}`. Prevented silent Claude-default fallback.
- **B14** OutroCTA props schema fixed: `{authorName, handle, ctaText}` → `{line: "Explore the full course at medhavy.com", handle: "@MedhavyAI"}`. Prevented silent Claude-default fallback.

## Audio regeneration
Kokoro `af_kore` regen for all 14 beats. Cost $0. Durations written back into `actual_duration_s`. Displaces the Jul 16 ElevenLabs-era mp3s.

## Compile / Gate V
See `AUDIT.md` for full Phase 2 report. Compiled to `vox-batch-distribution-slate.mp4` (214.4 s, `-24.0 dB` mean_volume, mp4 7 s newer than sheet).
