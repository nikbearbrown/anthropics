# REBUILD-LOG.md — nbb-vox-size-paradox

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet, made 2026-08-31 03:10 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order and act labels for the body: B01 COLD OPEN · B02/B03 COLD OPEN · B04 THE QUESTION · B05/B06 THE PROBLEM · B07/B08/B09 THE MECHANISM · B10/B11 THE IMPLICATION · B12 THE EXAMPLE · B13 RECAP.
- B00 cold-open narration is the pre-rebuild NBB00 ask, verbatim (the paradox statement + the three-part request to Claude).
- Metadata identity: title, slug, topic, register, source pointer, palette.

## REBUILT (regenerated)

- **Bookend consolidation.** Pre-rebuild carried DUAL bookends: empty canonical `B00/BVDT/BHTF/BOUT` SLATE stubs with template placeholders alongside populated `NBB00–NBB03` beats with Jul-16 Kokoro audio. Merged: promoted NBB payloads into canonical B00/BVDT/BHTF/BOUT; deleted the four duplicate empties. Renamed `mp3/beat-NBB0[0-3].mp3` → `mp3/beat-{B00,BVDT,BHTF,BOUT}.mp3`.
- **B00 greeting.** Empty `props.greeting = "Liam"` (lonely-asterisk defect) → `"Yassou, Liam"` (Greek). Unused by adjacent cancer-nanomedicine reels.
- **BVDT narration + artifactLines.** Placeholder `Key finding one/two/three` replaced with four body-grounded lines (accumulation numbers, shrinkage numbers, IFP mechanism, 80% penetration). Narration rewritten to say the numbers aloud.
- **BHTF narration + command.** 3,472-sheet template `"Take what you learned from [X] and apply it to your own work"` replaced with a scaffolded exercise built on the size-vs-distribution framework: pick a paper, extract accumulation + distribution numbers, predict what a smaller diameter would move, name the axis the paper is silent about.
- **BOUT subline** set to `""` (opt-in; title carries the endcard on its own).
- **B01 FormBCard props** rewritten from `Key point one/two/three` + empty subs to three real items (bigger loads more · smaller cures more · why).
- **B02/B07 FormACard lines** split from mid-word `"…"` truncations to complete narration-derived sentences.
- **Metadata envelope normalized.** Added top-level `folderLabel: "@NikBearBrown"`. Dropped scaffold-era `built_at` and `old_outro_beats` (referenced B14/B15 which don't exist in this variant). `engine/voice/voice_kokoro` fields already Kokoro/am_onyx; no dead ElevenLabs fields to drop.
- **Bookend audio regenerated.** `generate_audio_kokoro.py --only B00 BVDT BHTF BOUT` via Kokoro `am_onyx`. Measured durations written back as ground truth: B00 28.63s, BVDT 32.51s, BHTF 19.86s, BOUT 4.18s.
- **Bookend renders.** `remotion_scenes.py --only B{00,VDT,HTF,OUT} --force` via the four proven-core patterns.
- **Body renders.** Symlinked `media/B{01..13}.mp4` → `../../vox-size-paradox/clips/B{01..13}.mp4` (source vox reel's Aug-27 rebuild).
- **Compile.** `compile.py --review --force` → `vox-size-paradox-slate.mp4` (277.3s, 17/17 VIDEO, GATE AUDIO PASS mean_volume -24.0 dB).

## Datable-claim edits

None. Narration cites tumor-transport biology (leaky vasculature, elevated interstitial pressure, hypoxic core, ~72% vs ~15% shrinkage as an illustrative case) — chapter-textbook mechanism, not versioned.

## Dropped fields

- `metadata.built_at` (scaffold-era timestamp; superseded by compile stamp).
- `metadata.old_outro_beats` (referred to B14/B15 which are not in this variant's beats).
- `props.modelLabel = "Fable 5"` / `props.effortLabel = "High"` from B00 & BHTF ClaudeComposerAsk (component defaults still render them in the composer footer — cosmetic).
- Duplicate empty stub beats: `B00/BVDT/BHTF/BOUT` (SLATE), `NBB00/NBB01/NBB02/NBB03` (their content preserved by promotion into canonical bookends).

## Reel-level notes

- Non-claude channel; canonical Claude bookends are correct for the nbb-variant vox reel (per sibling `nbb-vox-targeting-uptake` 03:03 build).
- Persona coherence: composer asks are first-person Bear (Bear writes the ask) but voiced by Liam (Kokoro am_onyx) — same pattern as sibling nbb-vox reels in this batch.
- Post-compile sheet edits: NONE. Cut mtime (03:20:02) > sheet mtime (03:19:30).
