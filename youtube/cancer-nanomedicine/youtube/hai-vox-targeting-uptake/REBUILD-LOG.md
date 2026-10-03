# REBUILD-LOG.md — hai-vox-targeting-uptake

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B12) is verbatim from the pre-rebuild sheet. Zero words moved.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07 THE MECHANISM · B08 THE IMPLICATION · B09 THE EXAMPLE · B10 RECAP · B11/B12 OUTRO.
- Metadata identity: title, topic, source pointer, color semantics, style bible, audience, register, palette, exclusions note.
- Non-Claude channel skins retained: OutroSeries (B11) and OutroCTA (B12) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle`).
- Metadata `channel_title: "@HumanitariansAI"` added — required per HAI SKILL for first-beat overlay burn-in.
- Metadata `short_title: "Uptake Is Not Accumulation"` added (§8.5 pull-quote limit; full title is 12 words).
- Metadata `slug` corrected from `vox-targeting-uptake` to `hai-vox-targeting-uptake` (matches folder; matches peer reel convention).
- Metadata `_variant_todo` block DROPPED — legacy migration checklist from the pragmatist/HAI variant rewrite; all four items done (register, tangent, outro, audio) prior to this pass.
- Metadata `build` block DROPPED before compile — claimed `filled: 2/12` at 2026-07-16 with slates for B01–B10 and no per-beat mp4 renders on disk. Fresh compile re-stamps.
- Per-beat `build` stamps DROPPED on all 12 beats — every SLATE stamp was from 2026-07-16 and B11/B12 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on all remotion beats — set by remotion_scenes.py during this rebuild.

## Datable-claim edits

None. Narration cites biology mechanism (nanoparticle binding, circulation half-life, vessel permeability, cellular internalization, targeting ligands, folate example) and one illustrative comparison block (B09) explicitly labeled "illustrative" in the FormA card. No model names, prices, or "as of" phrasing. Folate example numbers (2.1% vs 1.9%; 68% vs 12%) are illustrative per source-chapter conventions and are labeled as such on the card.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- GRAPHIC beats (B03, B04, B05, B06, B07, B08, B09) had `shot.type: "GRAPHIC"` with `graphic.manim` scene names (`B03_Question`, `B04_DeliveryChain`, `B05_CultureVsBody`, `B06_AccumulationDrivers`, `B07_LastStep`, `B08_WrongFix`, `B09_FolateExample`) but no `scenes.py` on disk — pipeline-owned SLATES which lane_check refuses. Reshaped per rebuild contract (props may be re-shaped, intent locked):
  - B03 → `CARD kind=question` (short question card; matches peer hai-vox-delivery-funnel B03 pattern; a text-only question is not a pipeline-owned graphic).
  - B04 → `FormBCard` "Delivery Chain — Ligand Acts Last" (4 items: 1. Blood / 2. Vessel wall / 3. Tumor tissue / 4. Cell surface).
  - B05 → `FormBCard` "What Culture Sees — and What It Misses" (2 items: Step 4 visible / Steps 1–3 invisible).
  - B06 → `FormBCard` "What Sets Tumor Accumulation" (3 items: Circulation half-life / Vessel permeability / Targeting ligand [no effect]).
  - B07 → `FormBCard` "The Ligand's Moment — After Arrival" (2 items: Arrival / Internalization).
  - B08 → `FormBCard` "Fix Must Match the Failure Mode" (2 items: Bottleneck at steps 1–2 / Ligand fixes step 4).
  - B09 → `FormACard` (4 lines compressing the illustrative folate comparison — flagged "illustrative" in line 1).
- Icon-set constraint: FormBCard icons must resolve to `runtime/remotion/public/form-b-icons/*.svg`. Used: life-buoy, frame, layers, hand, circle-x, shield, target — all in the library.
- B02 FormACard `lines` rewritten from a near-verbatim narration paraphrase (§8.10 recite-the-card score high) to a compressed two-line pair contrasting dish and animal.
- B11 `OutroSeries` and B12 `OutroCTA` props corrected to the current schema (`eyebrow`+`line` / `line`+`handle`). Pre-rebuild passed `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` which Remotion silently falls back to Root.tsx defaults `CLAUDE COWORK` — Claude-washing a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. Props reshape; intent (HAI series sign-off, HAI CTA) is locked.
- Card beats (B01 title, B03 question, B10 endcard) render as slate request cards — legit for this review-slate cut; not pipeline-owned. A future full-render pass will bind them to Remotion patterns.
