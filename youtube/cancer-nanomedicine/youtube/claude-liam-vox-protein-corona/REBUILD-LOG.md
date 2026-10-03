# REBUILD-LOG — claude-liam-vox-protein-corona

Generated 2026-08-30. Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy of
prior `beat_sheet.json`, made before any edit).

## Envelope (VOICE-LOCK cleanup)
- DROPPED `metadata.voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs-era field.
- CHANGED `metadata.clock`:
  - old: `narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock`
  - new: `narration (Kokoro am_onyx) — measured mp3 durations are the master clock`
- Kept: `engine: kokoro`, `voice_kokoro: am_onyx` (Liam channel).

## Narration edits (authorized — spark line + verdict + your-turn)

### B00 — cold-open greeting
- old: `props.greeting: "Liam"` (renders lone asterisk)
- new: `props.greeting: "Namaste, Liam"` (world-language rotation)
- Added `props.output`: 3-line answer compressed from body (mirrors BVDT recap).
- Reason: SPARK-LINE LAW.

### B01 — FormBCard placeholder items
- old items: `label: "Key point one/two/three"`, all `sub: ""`.
- new items:
  - `engineered surface` — antibodies loaded onto the particle
  - `corona in seconds` — plasma proteins bury the ligand
  - `liver, not tumor` — opsonins flag it for macrophages
- Also shortened FormBCard `title` prop from the 13-word metadata title to
  "A nanoparticle vanishes under a coat of protein" (9 words) to clear
  §8.5 wordy-card FAIL. Metadata `title` unchanged.

### BVDT — verdict authored from body
- Body qualifies (11 beats, ~430 words) — verdict AUTHORED, not stripped.
- old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]`
- new `artifactLines` (5 lines, from body content):
  1. Corona forms in seconds — plasma proteins pile onto the engineered surface.
  2. Ligands stay attached but are physically buried; the receptor never sees them.
  3. Opsonins in the coat flag the particle for macrophages in liver and spleen.
  4. Culture medium has no corona — the ligand is naked, the result flips in blood.
  5. Verify in full plasma, not medium, before any in-vivo claim.
- old `narration_text`: `""` (empty; renders silent)
- new `narration_text`: authored recap that says the finding aloud (see sheet).
- `artifactHeading` changed from generic "Key findings" → "What the corona does".

### BHTF — your-turn authored from body (was template placeholder)
- old `command`: `"Take what you learned from [The Instant a Nanoparticle Hits
  Blood, It Vanishes Under a Coat of Protein] and apply it to your own work.
  What's one thing you'll try first?"` — bracketed template placeholder.
- new `command`: real exercise using body's nouns (albumin, immunoglobulins,
  complement, opsonins) and body's method (refute-the-culture-result plasma
  experiment). See sheet.
- old `narration_text`: `""` — new: authored to match the command (see sheet).
- Added `props.output`: 3-line scaffolded checklist for the exercise.

## Beat body narration — NO CHANGES
B01–B13 body narration is locked and byte-identical to `beat_sheet.pre-rebuild.json`.
No datable-claim fixes were needed (the folate-example numbers are explicitly
labeled "illustrative numbers" in the beat's `production_viz` note; the source
chapter authored them as such — not a datable-claim rot).
