# REBUILD-LOG.md — hai-vox-delivery-diagnosis

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B14) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01 COLD OPEN · B02 COLD OPEN · B03 THE QUESTION · B04/B05/B06 THE PROBLEM · B07/B08 THE MECHANISM · B09/B10 THE IMPLICATION · B11 THE EXAMPLE · B12 RECAP · B13/B14 OUTRO.
- Metadata identity: title, topic, source pointer, color semantics, style bible, audience, register, palette.
- Non-Claude channel skins retained: OutroSeries (B13) and OutroCTA (B14) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle: "@humanitariansai"`).
- Metadata `short_title: "Delivery vs. Biology"` added (§8.5 pull-quote limit; the full title is 14 words).
- Metadata `slug` corrected from `vox-delivery-diagnosis` to `hai-vox-delivery-diagnosis` (matches folder).
- Metadata `_variant_todo` block DROPPED — legacy migration checklist from the pragmatist/HAI variant rewrite; all four items were done (register, tangent, outro, audio) prior to this pass.
- Metadata `build` block (top-level) DROPPED — claimed `filled: 2/14` at 2026-07-16 with slates for B01–B12 and VIDEO for B13/B14, but no per-beat mp4 renders exist on disk. Fresh compile re-stamps.
- Per-beat `build` stamps DROPPED on all 14 beats — every SLATE stamp was from 2026-07-16 and B13/B14 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on B02, B08 (FormACard slots) and B13, B14 (OutroSeries/OutroCTA).

## Datable-claim edits

None. Narration cites biology mechanism (biodistribution imaging, RES clearance, PEGylation, ionizable-lipid engineering) and one illustrative example block (B11) that is explicitly labeled `illustrative` in the narration and in `graphic.production_viz.note`. No model names, prices, or "as of" phrasing.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- GRAPHIC beats (B04/B05/B07/B09/B11) had `shot.type: "GRAPHIC"` with `graphic.manim` scene names but no `scenes.py` on disk; that made them pipeline-owned SLATES which lane_check refuses in any cut. Reshaped each to a real Remotion pattern per rebuild contract (props may be re-shaped, intent locked):
  - B04 → `FormBCard` "One Outcome, Two Opposite Causes" (2 items: Drug too weak / Particle never arrived)
  - B05 → `FormBCard` "Opposite Causes, Opposite Fixes" (2 items: Fix the drug / Fix the particle)
  - B07 → `FormBCard` "Label the Particle, Track It" (3 items: Fluorescent dye / Iron oxide MRI / Radiolabel PET)
  - B09 → `FormBCard` "Delivery Failure: Fix the Particle" (3 items: PEGylation / Particle size / Surface charge)
  - B11 → `FormACard` (3 lines: Program A closed at 7%, Program B biodistribution imaging, redesigned PEG → 21%)
- B13 `OutroSeries` and B14 `OutroCTA` props corrected to the current schema (`eyebrow`+`line` / `line`+`handle`). Old sheet passed `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` which Remotion silently fell back to Root.tsx defaults `CLAUDE COWORK` / `Part of the Claude Cowork series.` / `@nikbearbrown` — Claude-washing a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. This is a props reshape (intent — HAI series sign-off, HAI CTA — is locked).
- Card beats (B01 title, B03 question, B12 recap endcard) and DOCUMENT quote beats (B06, B10) render as slate request cards — legit for this review-slate cut; not pipeline-owned. A future full-render pass will bind them to Remotion patterns.
