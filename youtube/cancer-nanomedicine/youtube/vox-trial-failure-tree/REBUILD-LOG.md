# REBUILD-LOG.md — vox-trial-failure-tree

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.
Run 2026-08-28, unattended film-factory pass.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B15) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06–B09 THE MECHANISM · B10/B11 THE IMPLICATION · B12 THE EXAMPLE · B13 RECAP · B14/B15 OUTRO.
- Metadata identity: title, slug, topic, source pointer, color semantics, style bible, key visual (split/tree).
- Non-Claude channel skins retained: OutroSeries (B14) and OutroCTA (B15) — NOT Claude-washed. This reel has no Claude bookends (B00/BVDT/BHTF/BOUT) — legit for the legacy vox-explainer format on the NikBearBrown channel (see AUDIT amendment #2 — BVDT may be legitimately ABSENT). A parallel `claude-liam-vox-trial-failure-tree/` sibling carries the Claude-washed variant.
- vox_scenes.py Scene classes (B01_Title, B03_Question, B04_BinaryEndpoint, B05_Quote, B06_ThreeFailures, B07_DeliveryFailure, B08_PayloadFailure, B09_BiologyFailure, B10_FullTree, B12_TwoPrograms, B13_End) — the shot list, unchanged.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@NikBearBrown"` added (matches OutroCTA `handle`).
- Metadata `short_title: "The Trial That Couldn't Diagnose Itself"` added (§8.5 pull-quote limit; the full title is 9 words + article).

## Datable-claim edits

None. Narration cites biology mechanism (three failure modes, response-only endpoint, tracer cohort) — chapter-textbook material, not versioned; no model names, prices, or "as of" phrasing. The $80M and illustrative example numbers (7%, 75%, 3%, 21%, 10 patients) are flagged in FACTCHECK.md as illustrative and stay.

## On-screen attribution edit (not a narration change)

- `B05.document.attribution` and `vox_scenes.py :: B05_Quote` attribution:
  - OLD: `— Cancer Nanomedicine, Chapter 12`
  - NEW: `— Cancer Nanomedicine`
  - SOURCE: Gate W SLATE-RUNNER W7 CHAPTER-ON-SLIDE — chapter numbers never appear on-screen; name the TOPIC, not the chapter.
  - Narration audio unchanged (attribution is on-slide text, not spoken).

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio.

## Reel-level notes

- Persona coherence: narration is explainer voice with no first-person claim; OutroCTA carries NikBearBrown attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent.
- `vox_scenes.py` already exists with Scene classes for every GRAPHIC/CARD/DOCUMENT body beat. B02 and B11 are STILL·ai slots (no scene). B14/B15 are Remotion OutroSeries/OutroCTA per non-Claude skin.
- Existing mp3s in mp3/ date to 2026-07-08 (ElevenLabs era). Being regenerated with Kokoro am_onyx per VOICE-LOCK. Existing partial Manim renders from earlier today (media/videos/vox_scenes/1080p24/, made against old timings) will be re-rendered against the new audio-measured durations.
