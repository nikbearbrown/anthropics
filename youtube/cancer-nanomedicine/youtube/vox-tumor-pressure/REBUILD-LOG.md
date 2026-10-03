# REBUILD-LOG.md — vox-tumor-pressure

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B11) verbatim from the pre-rebuild sheet.
- Bookend narration (B12 series, B13 CTA) verbatim.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07 THE MECHANISM · B08/B09 THE IMPLICATION · B10 THE EXAMPLE · B11 RECAP · B12/B13 OUTRO.
- Metadata identity: title, slug, topic, source pointer, color semantics, note (exclusions).
- Non-Claude channel skins retained: OutroSeries (B12) + OutroCTA (B13) — NOT Claude-washed. This reel has no Claude bookends (B00/BVDT/BHTF/BOUT) — legit for the legacy vox-explainer format on the NikBearBrown channel (mirrors sibling `vox-endosomal-escape`).

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` DROPPED.
- Metadata `folderLabel: "@NikBearBrown"` added (was implicit via OutroCTA `handle`; matches sibling reel envelope).
- Metadata `short_title: "The Pressure That Pushed the Drug Back Out"` added.
- Metadata `source: "cancer-nanomedicine/chapters/02-tumor-transport-barriers.md"` promoted from `purpose` prose to top-level field (mirrors sibling envelope).
- `vox_scenes.py`: brittle `parents[3]`-relative toolkit import replaced with the parent-walk pattern used by the sibling reel (finds `books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` reliably regardless of reel depth under `books/anthropics/youtube/cancer-nanomedicine/youtube/…`, which was broken for this tree).
- Kokoro mp3s written to `mp3/beat-B*.mp3` on this pass — replaces the July-2025 ElevenLabs takes. `actual_duration_s` re-measured and written back beat-by-beat by `generate_audio_kokoro.py`.

## Datable-claim edits

None. Narration cites biology mechanism (leaky vessels, IFP 5–10× normal, hypoxic core selection) — chapter-textbook facts, not versioned.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.

## Reel-level notes

- Persona coherence: narration is explainer voice with no first-person claim ("The naive picture…", "Take an illustrative scenario…"). Outros carry NikBearBrown attribution — voice-lock `nbbhuman`/`am_onyx` is coherent.
- `vox_scenes.py` already exists with Scene classes for all 10 body Manim beats (B01_Title, B03_Question, B04_LeakyVessels, B05_PressureBuilds, B06_PressureFlow, B07_ParticlesPushedBack, B08_HypoxicCore, B09_InsideOutQuote, B10_Example, B11_Endcard). B02 is a FormACard slate (AI still slot). B12/B13 are Remotion OutroSeries/OutroCTA.
