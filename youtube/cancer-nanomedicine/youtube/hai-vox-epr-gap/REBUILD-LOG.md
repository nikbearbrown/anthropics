# REBUILD-LOG.md — hai-vox-epr-gap

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.
Date: 2026-08-28.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B14) is VERBATIM from the pre-rebuild sheet — same words, same order, same illustrative-number hedges.
- B15/B16 OUTRO narration ("This is part of the Cancer Nanomedicine series from Humanitarians AI." / "Find more at humanitarians.ai.") unchanged.
- Beat order and act labels: B01/B02/B03 COLD OPEN · B04 THE QUESTION · B05/B06 THE PROBLEM · B07/B08/B09 THE MECHANISM · B10/B11 THE IMPLICATION · B12/B13 THE EXAMPLE · B14 RECAP · B15/B16 OUTRO.
- Metadata identity: title, topic, source pointer, color semantics, exclusions note, audience (HAI), register (Pragmatist), palette (humanitarians), outro_source.
- HAI channel skin retained: OutroSeries (B15) and OutroCTA (B16) — NOT Claude-washed. No B00/BVDT/BHTF/BOUT bookends (correct for non-Claude channel).

## REBUILT (regenerated)

### Envelope
- DROPPED `metadata.voice_id: "qdEb53HLreRBCD1FQE30"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED `metadata.clock: "narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` — ElevenLabs-era prose; the clock is now measured Kokoro audio (mp3/timings.json + per-beat actual_duration_s).
- DROPPED `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all four items are done (register set to Pragmatist, tangent not required, outro is HAI, audio locked to Kokoro).
- DROPPED `metadata.build` — stale 2026-07-16 stamp claiming filled: 2/16 with slates for B01–B14 and VIDEO for B15/B16, but no `media/` directory on disk. Fresh compile re-stamps.
- DROPPED every `beats[].build` per-beat stamp — every SLATE stamp was from 2026-07-16 and B15/B16 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- ADDED `metadata.voice: "nbbhuman"` — voice-lock envelope consistent with sibling `hai-vox-delivery-funnel`.
- ADDED `metadata.folderLabel: "@humanitariansai"` — HAI channel handle.
- ADDED `metadata.channel_title: "@HumanitariansAI"` — required per `skills/make/hai/SKILL.md`; compile.py burns as first-beat overlay.
- ADDED `metadata.short_title: "The EPR Gap"` — pull-quote length (§8.5); full title is 11 words.
- CORRECTED `metadata.slug` from `vox-epr-gap` to `hai-vox-epr-gap` (matches folder).
- SET `metadata.derived_from` to `beat_sheet.pre-rebuild.json`.

### Body — punt sweep (PIPELINE-SLATE-IN-CUT would refuse compile)
The pre-rebuild sheet had every body beat B01–B14 as a SLATE with one of three punt costumes, all pipeline-owned per `beat_plan.fill_plan`:
  - `shot.type: CARD` (B01, B04, B09, B14) — author-owned scripting-gap, not pipeline, but blank slates read poorly in a review cut.
  - `shot.type: STILL, source: ai` + `shot.remotion.pattern: FormACard` with TRUNCATED narration lines ending in `…` (B02, B06) — pipeline-owned via the FormACard pattern; the truncated line is a card punt.
  - `shot.type: GRAPHIC` + `graphic.manim: BXX_*` scene name (B03, B05, B07, B08, B10, B11, B12, B13) — pipeline-owned Manim, but no scenes.py exists in this reel folder.

Every body beat reshaped to `shot.type: REMOTION` + `shot.remotion.pattern: FormBCard` with 3 items each. Items derived from the beat's own narration (props reshape; narration UNTOUCHED). Icons drawn from `public/form-b-icons/*.svg` — target / circle-check / circle-x / layers / ruler / shield / shield-alert / crosshair / list-checks / zap.

Mapping:
- B01 (was CARD title) → FormBCard: "Same molecule, two biological worlds" (mice / patients / same chemistry).
- B02 (was FormACard with truncated `…` line) → FormBCard: "The preclinical result" (docetaxel NP / mice respond / ~8% ID/g).
- B03 (was Manim `B03_AccumComparison`) → FormBCard: "Phase II — the same particle in patients" (drops and scatters / near-zero lesions / chemistry unchanged).
- B04 (was CARD question) → FormBCard: "The question" (in mice / in patients / same molecule).
- B05 (was Manim `B05_EPRMechanism`) → FormBCard: "EPR — how tumors trap particles" (leaky vessels / broken drainage / passive uptake).
- B06 (was FormACard truncated) → FormBCard: "Where EPR is maximum — the xenograft" (the model / thin walls / no stroma).
- B07 (was Manim `B07_DesmoplasiaSqueeze`) → FormBCard: "Human tumors — the stromal squeeze" (desmoplastic stroma / compressed vessels / closed gaps).
- B08 (was Manim `B08_PressureFlow`) → FormBCard: "High interstitial pressure — the outward push" (sustained flow / outward direction / no mouse analog).
- B09 (was CARD section) → FormBCard: "The core contrast" (mouse model / patient average / the gap).
- B10 (was Manim `B10_ModelVsPatient`) → FormBCard: "Not the mechanism — the experimental logic" (EPR is real / logic failed / wrong population).
- B11 (was Manim `B11_LiverDefault`) → FormBCard: "Where the missed particles go" (liver default / spleen too / healthy tissue dosed).
- B12 (was Manim `B12_TwoTumors_Left`) → FormBCard: "Left panel — mouse xenograft (illustrative)" (fenestrations ~200 nm / ~8% ID/g / the system).
- B13 (was Manim `B13_TwoTumors_Right`) → FormBCard: "Right panel — human desmoplastic tumor" (vessels / ~0.3% ID/g / the label).
- B14 (was CARD endcard) → FormBCard: "Same molecule. Different biological world." (xenograft / patient tumor / the lesson).

### Outros (HAI skin — NOT Claude-washed)
- B15 `OutroSeries` props REWRITTEN from the wrong schema `{seriesTitle, tagline, githubSlug}` to the current schema `{eyebrow, line}` — the old props silently fell back to Root.tsx defaults (`CLAUDE COWORK` / `Part of the Claude Cowork series.`), which would have Claude-washed a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.`. Same fix pattern as sibling `hai-vox-delivery-funnel` REBUILD-LOG line 51.
- B16 `OutroCTA` props REWRITTEN from `{authorName, handle, ctaText}` to current schema `{line, handle}` → `Find more at humanitarians.ai.` / `@humanitariansai`.

### Datable-claim edits (narration)
None. The mechanism is timeless (EPR max in xenograft; blocked in desmoplastic human tumors). Illustrative numbers (8% / 0.3% ID/g, 200 nm) are labeled illustrative in the narration itself ("These are illustrative numbers." / "Numbers are illustrative."). No model names, prices, or "as of" phrasing. No datable-claim rot to fix.

## Dropped fields (summary)

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; replaced by measured Kokoro audio.
- `metadata._variant_todo` — legacy migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim (no "Liam, in for Bear" prefix that the claude-liam sibling carries); outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (Kokoro `am_onyx`) is coherent.
- Audio validity: mp3s date 2026-07-16 with narration matching the current locked script (verified by diff against `beat_sheet.json.bak-slatecard` — only whitespace/indentation changed between backup and current sheet before this rebuild). No re-generation needed.
- Card-only reel: FormBCard-only rebuild is the same pattern the sibling `claude-liam-vox-epr-gap` used successfully (2026-08-27, `filled: 18/18`) — vox_scenes.py does not exist in this reel folder, so the alternative (authoring 8 Manim scenes from scratch inside a single invocation) would sink the whole invocation. Each FormBCard IS the drawn figure of its beat: item labels + subs form the schematic and the icon glyphs carry the color-semantic emphasis.
- Lens: four moves earned — Descartes (what would falsify "EPR fails in patients" → the 8% vs 0.3% ID/g contrast, same chemistry, ~8× less delivery, the exact test that would confirm or refute), Hume (mouse-model confidence is not world confidence: the xenograft is a best-case system, not the average case), Popper (interpatient EPR variability as the pre-stated failing framing — a nanoparticle optimized in the EPR-max system is not tested under the conditions it will face), Plato (the artifact is the xenograft-EPR effect; the world is the desmoplastic + high-IFP human tumor; the relationship is "same molecule, different biological world").
