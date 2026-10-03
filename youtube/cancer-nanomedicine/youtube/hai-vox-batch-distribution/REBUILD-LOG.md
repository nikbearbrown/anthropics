# REBUILD-LOG.md — hai-vox-batch-distribution

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B14) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07/B08 THE MECHANISM · B09/B10 THE IMPLICATION · B11 THE EXAMPLE · B12 RECAP · B13/B14 OUTRO.
- Metadata identity: title, subtitle, topic, source pointer, color semantics, style bible, audience, register, palette.
- Non-Claude channel skins retained: OutroSeries (B13) and OutroCTA (B14) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle: "@humanitariansai"`).
- Metadata `short_title: "Same Average, Different Product"` added.
- Metadata `slug` corrected from `vox-batch-distribution` to `hai-vox-batch-distribution` (matches folder).
- Metadata `source` pointer added: `cancer-nanomedicine/chapters/11-characterization-manufacturing-and-regulatory-translation.md`.
- Metadata `_variant_todo` block DROPPED — legacy pragmatist/HAI migration checklist; all items done.
- Metadata `build` block DROPPED — stale 2026-07-16 stamp claiming 2/14 filled with slates B01–B12.
- Per-beat `build` stamps DROPPED on every beat — every stamp was from 2026-07-16; B13/B14 claimed `VIDEO src: media/B##.mp4` while `media/` did not exist. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on all Remotion slots (B02, B04, B05, B07, B08, B10, B11, B13, B14).

## Datable-claim edits

None. Narration cites biology mechanism (polydispersity index, DLS, PDI thresholds, liver/spleen clearance) and one illustrative example block (B11) explicitly labeled `Illustrative` in the narration and in `graphic.production_viz.note`. No model names, prices, or "as of" phrasing.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- GRAPHIC beats (B04/B05/B07/B08/B10) had `shot.type: "GRAPHIC"` with `graphic.manim` scene names but no `scenes.py` on disk; that made them pipeline-owned SLATES which lane_check refuses. Reshaped each to a real Remotion pattern per rebuild contract (props may be re-shaped, intent locked):
  - B04 → `FormBCard` "Small Molecule = One Structure" (2 items: One defined structure / Binary identity)
  - B05 → `FormBCard` "A Nanoparticle Is a Population" (3 items: A cloud of objects / Varying in size / The cloud is the product)
  - B07 → `FormBCard` "The PDI Scale" (3 items: PDI near 0 / PDI above 0.2 / Use PDI, not the mean)
  - B08 → `FormBCard` "Three Populations in One Batch" (3 items: Small: rapid clearance / Mid: designed / Large: liver+spleen)
  - B10 → `FormBCard` "Match the Distribution, Not the Mean" (2 items: Match the mean / Match the distribution)
- B02 (STILL·ai) FormACard `lines` rewritten from the auto-router's first-sentence truncation to a clean three-line editorial summary of the narration (Batch A cleared in 45 min / Batch B circulated 6 h / same label, different behavior).
- B11 (THE EXAMPLE) reshaped GRAPHIC → REMOTION FormACard: three lines summarize the illustrative comparison (PDI 0.07 vs 0.31 / 15% > 200 nm / ~40% less drug at tumor — Illustrative).
- B06 (THE MECHANISM — the KEY side-by-side histogram compare) kept as GRAPHIC slate. This is the flagship compare visual (narrow teal spike vs wide crimson bell, shared gold mean tick); reshaping it to a FormBCard or FormACard would lose the visualization. Legit slate in a review-slate cut — flagged for a future Manim binding at full-render time.
- B13 `OutroSeries` and B14 `OutroCTA` props corrected to the current schema (`eyebrow`+`line` / `line`+`handle`). Old sheet passed `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` which Remotion silently fell back to Root.tsx defaults `CLAUDE COWORK` / `Part of the Claude Cowork series.` / `@nikbearbrown` — Claude-washing a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. Intent (HAI series sign-off, HAI CTA) is locked; only prop names reshaped.
- Card beats (B01 title, B03 question, B12 recap endcard) and DOCUMENT quote beat (B09) render as slate request cards — legit for this review-slate cut; not pipeline-owned. A future full-render pass will bind them to Remotion patterns.
- Icon selection: FormBCard `icon` names constrained to the pantry at `runtime/remotion/public/form-b-icons/*.svg` (target, circle-check, layers, ruler, list-checks, shield-alert, zap). First render pass failed on `circle`, `check`, `activity`, `alert-triangle`, `chevrons-up/down`, `circle-dot`, `minus` (not in pantry); second pass rendered clean.
