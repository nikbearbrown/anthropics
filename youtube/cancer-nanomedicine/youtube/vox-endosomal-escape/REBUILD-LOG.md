# REBUILD-LOG.md — vox-endosomal-escape

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01 COLD OPEN · B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07 THE MECHANISM · B08 THE IMPLICATION · B09/B10 THE EXAMPLE · B11 RECAP · B12/B13 OUTRO.
- Metadata identity: title, slug, topic, source pointer, color semantics, style bible.
- Non-Claude channel skins retained: OutroSeries (B12) and OutroCTA (B13) — NOT Claude-washed. This reel has no Claude bookends (B00/BVDT/BHTF/BOUT) — legit for the legacy vox-explainer format on a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@NikBearBrown"` added (was implicit via OutroCTA `handle`).
- Metadata `short_title: "The pH-Triggered Lock"` added (§8.5 pull-quote limit; the full title is 12 words).
- Metadata `build` block (top-level) DROPPED — claimed `filled: 13/13` at 2026-07-16 but zero mp4 renders exist on disk. Fresh compile will re-stamp.
- Per-beat `build` stamps DROPPED — every one claimed `MANIM` or `VIDEO` status with `src: manim/B##.mp4` or `media/B##.mp4`, and none of those files exist. Fresh compile will re-stamp.
- Remotion `rendered.at` timestamps blanked on B02 (FormACard slot) and B12/B13 (OutroSeries/OutroCTA).

## Datable-claim edits

None. Narration cites biology mechanism (pH 7.4→5.5 endosome, ionizable-lipid charge flip, ~1-2% escape) that are chapter-textbook facts, not versioned; no model names, prices, or "as of" phrasing.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio.
- `metadata.build` — stale (claimed built, zero mp4s on disk).
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no persona claim; outros carry NikBearBrown attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent.
- `vox_scenes.py` already exists with Scene classes for all body Manim beats (B01_Title, B03_Question, B04_Endocytosis, B05_pHDrop, B06_ChargeFlip, B07_MembraneCrack, B08_EscapeFraction, B09_LNPComparison, B10_QuoteLock, B11_End). B02 is a FormACard slate (AI still slot). B12/B13 are Remotion OutroSeries/OutroCTA.
