# REBUILD-LOG.md — nbb-vox-abraxane-solvent

Rebuild ran under `skills/make/rebuild/SKILL.md`.

## Locked (verbatim carry-over)
- `narration_text` for all body beats B01..B15 — the July-16 script.
- Beat order and act structure (B00 cold open · B01..B15 body · BVDT verdict · BHTF your-turn · BOUT title outro).
- Shot INTENT per beat: patterns, viz mechanics, Manim class names, still prompts, document quote (B06) — all preserved.
- Metadata identity: title, slug, topic, source pointer.

## Rebuilt
1. **Voice envelope** — engine `kokoro`, voice `am_onyx` stamped on metadata + every beat. Legacy ElevenLabs body mp3s (44.1 kHz) at `../vox-abraxane-solvent/mp3/beat-B0X.mp3` REPLACED with fresh local Kokoro renders (24 kHz) at `mp3/beat-B0X.mp3`. `actual_duration_s` re-measured from the new mp3s.
2. **Bookends** — dropped the empty scaffold beats (`B00`, `BVDT`, `BHTF`, `BOUT` with `narration_text: ""`) that duplicated the already-authored `NBB00`-`NBB03` set. Renamed the filled NBB set to canonical ids so the sheet has exactly one authoritative bookend at each slot.
3. **Verdict (BVDT)** — placeholder `Key finding one/two/three` replaced by a three-line verdict built from body nouns and numbers.
4. **Spark lines** — `B00.greeting = "Olá, Liam"` (world-language hello, rotated across the batch); `BHTF.greeting = "Your turn."`; segments normalized to `"abraxane · the solvent hazard"` (no mid-word truncation).
5. **Card content (B01)** — placeholder FormBCard items replaced with real ones.
6. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from bookends: this is an nbb Kokoro reel, not a Claude model-branded cut.

## Datable-claim edits
- None. The body's quantitative claims ("~10%", "<1%") are labeled ILLUSTRATIVE inside the viz beats and the narration uses hedged language ("roughly", "under"). No versioned models, no tool version strings, no dated prices anywhere in the script.

## Dropped fields
- Every beat: `source_audio` (ElevenLabs-era pointer into `../vox-abraxane-solvent/mp3/`).
- Body beats: `actual_duration_s` from ElevenLabs measurement (re-measured after Kokoro regen).
- Metadata: `body_beats`, `old_outro_beats` (redundant with the beats array).
- BVDT/BHTF bookends: `modelLabel`, `effortLabel`.

## Renamed
- `NBB00` → `B00` (cold-open ClaudeComposerAsk)
- `NBB01` → `BVDT` (verdict)
- `NBB02` → `BHTF` (your-turn)
- `NBB03` → `BOUT` (title outro)
- `mp3/beat-NBB0X.mp3` renamed on disk to match new ids.
