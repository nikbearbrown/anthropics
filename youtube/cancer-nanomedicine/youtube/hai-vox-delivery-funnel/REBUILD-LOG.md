# REBUILD-LOG.md — hai-vox-delivery-funnel

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04 THE PROBLEM · B05/B06/B07 THE MECHANISM · B08/B09 THE IMPLICATION · B10 THE EXAMPLE · B11 RECAP · B12/B13 OUTRO.
- Metadata identity: title, topic, source pointer, color semantics, style bible, audience, register, palette, exclusions note.
- Non-Claude channel skins retained: OutroSeries (B12) and OutroCTA (B13) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle: "@humanitariansai"`).
- Metadata `short_title: "The Delivery Funnel"` added (§8.5 pull-quote limit; the full title is 12 words).
- Metadata `slug` corrected from `vox-delivery-funnel` to `hai-vox-delivery-funnel` (matches folder).
- Metadata `_variant_todo` block DROPPED — legacy migration checklist from the pragmatist/HAI variant rewrite; all four items were done (register, tangent, outro, audio) prior to this pass.
- Metadata `build` block (top-level) DROPPED before compile — claimed `filled: 2/13` at 2026-07-16 with slates for B01–B11 and VIDEO for B12/B13, but no per-beat mp4 renders existed on disk. Fresh compile re-stamps.
- Per-beat `build` stamps DROPPED on all 13 beats — every SLATE stamp was from 2026-07-16 and B12/B13 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on all remotion beats — set by remotion_scenes.py during this rebuild.

## Datable-claim edits

None. Narration cites biology mechanism (liver/spleen clearance, extravasation, cellular uptake, endosomal release, targeting ligands) and one illustrative example block (B10) explicitly labeled "illustrative" in the narration. No model names, prices, or "as of" phrasing. The 0.7% figure is from the source chapter (Cancer Nanomedicine Ch1); kept.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- GRAPHIC beats (B04, B05, B06, B07, B08, B10) had `shot.type: "GRAPHIC"` with `graphic.manim` scene names (`B04_FiveSteps`, `B05_Drain1`, `B06_Drain2`, `B07_Drain345`, `B08_TargetingFix`, `B10_Example`) but no `scenes.py` on disk — pipeline-owned SLATES which lane_check refuses. Reshaped each to a real Remotion pattern per rebuild contract (props may be re-shaped, intent locked):
  - B04 → `FormBCard` "Syringe to Tumor Cell: Five Sequential Steps" (5 items: 1. Circulate / 2. Extravasate / 3. Penetrate / 4. Uptake / 5. Release)
  - B05 → `FormBCard` "Step 1 — Circulation Loss" (2 items: Liver clearance / Spleen filtration)
  - B06 → `FormBCard` "Step 2 — Extravasation Loss" (2 items: Cross the wall / Degrade or trap)
  - B07 → `FormBCard` "Steps 3, 4, 5 — Funnel Ends at 0.7%" (3 items: 3. Penetrate matrix / 4. Cell uptake / 5. Release payload)
  - B08 → `FormBCard` "Targeting Ligand: One Step of Five" (2 items: Steps 1–3 upstream / Step 4 uptake)
  - B10 → `FormACard` (5 lines: 100 units injected — illustrative; 18 cleared; 14 degrade / 12 fail; 55 non-tumor; 0.7 reaches tumor)
- Icon-set constraint: FormBCard icons must resolve to `public/form-b-icons/*.svg`. Initial pass used `circle-dot / arrow-right / download` which 404'd on the Remotion dev server. Fixed to `life-buoy / frame / hand` (available icons); re-rendered B04/B06/B07.
- B02 FormACard `lines` rewritten from a near-verbatim narration paraphrase (§8.10 recite-the-card score 1.00) to a distinct compressed line pair (recite score 0.50). Not a narration edit — a card-side edit only.
- B12 `OutroSeries` and B13 `OutroCTA` props corrected to the current schema (`eyebrow`+`line` / `line`+`handle`). Old sheet passed `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` which Remotion silently fell back to Root.tsx defaults `CLAUDE COWORK` / `Part of the Claude Cowork series.` / `@nikbearbrown` — Claude-washing a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. This is a props reshape (intent — HAI series sign-off, HAI CTA — is locked).
- Card beats (B01 title, B03 question, B09 quote, B11 recap endcard) render as slate request cards — legit for this review-slate cut; not pipeline-owned. A future full-render pass will bind them to Remotion patterns.
