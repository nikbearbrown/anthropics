# REBUILD-LOG.md — vox-spec-saves-time

Rebuilt: 2026-08-31 (nopunt filmloop).

Source: `beat_sheet.pre-rebuild.json` (byte-exact copy of incoming sheet).

## LOCKED (unchanged)
- Every body beat's `narration_text` (B01–B11, YOURTURN).
- Beat order and act labels for body beats.
- Metadata: title, slug, topic, source pointer, engine=kokoro, voice=am_onyx.

## REBUILT / EDITED

### 1. B00 greeting — spark-line audit fix
- old: `"greeting": "Liam"` (persona only — would render "* Liam")
- new: `"greeting": "Jambo, Liam"` (Swahili hello — one-word cue that fits the ClaudeComposerAsk serif line)
- rotation: no adjacent claude-code sibling uses Jambo (adjacent hellos: Sawadee, Ciao, Merhaba, Bonjour).

### 2. B07 — remove errant ClaudeTitleOutro / act:OUTRO
- old: `shot.type: REMOTION` with a `remotion.pattern: ClaudeTitleOutro` block bolted on top of the beat's real Manim `B07_ComparisonTable` graphic; beat also carried `act: OUTRO`.
- reason: BOUT is the reel's outro bookend. B07's narration ("The worked comparison. Request: Add a syllabus page. Specification: Create src/syllabus.html…") is body content, not an outro.
- new: `shot.type: GRAPHIC`, `motion: drawon`, `manim.scene_class: Scene_B07_VoxSpecSaves` kept; remotion block removed; `act: OUTRO` removed.
- narration untouched.

### 3. BVDT — author real verdict (was template placeholder)
- old artifactLines: `["Key finding one", "Key finding two", "Key finding three"]` (pure template).
- new artifactLines (2-4 lines, from body's own nouns/numbers):
  1. `Eight words → 45 minutes fixing Claude's defaults.`
  2. `Ninety words → 12 minutes total.`
  3. `Five cells — Operation, Invariants, Context, Output format, Negative constraint — reclaim the four decisions.`
- old artifactHeading: `Key findings` (placeholder). new: `Verdict`.
- old narration: empty. new: authored to DISCUSS the card, not recite it (§8.10 redundancy score 0.24, was 0.86 on a first draft that recited).
- estimated_duration_s: 20 → 22 (to fit authored narration at ~2.75 wps).
- audio_file: mp3/beat-BVDT.mp3 registered.

### 4. BHTF — author real exercise (was placeholder template)
- old command: `Take what you learned from [Why the 90-Second Request Takes 12 Minutes and the 8-Second Request Takes 45] and apply it to your own work. What's one thing you'll try first?` — the seeded placeholder with square brackets (matched the 3,472-sheet template caught 2026-08-30).
- new command: a real exercise using the video's own five-cell method — write Operation / Invariants / Context / Output format / Negative constraint on the viewer's next Claude Code task, time both spec and execution, report whether the 90s paid for itself.
- old output: `[]` (empty on a ClaudeComposerAsk BHTF is a slot-not-filled defect). new: 3 real next-step lines.
- old narration: empty. new: authored to speak the exercise.
- estimated_duration_s: 20 → 24 (to fit authored narration).
- audio_file: mp3/beat-BHTF.mp3 registered.

## DATABLE CLAIMS

None. Reel's numeric claims (90s / 12 min / 8 words / 45 min / 4 decisions / 5 cells) are the reel's own argument, not datable facts. `modelLabel: "Claude Sonnet"` on YOURTURN — a generic family label, not a version — kept.

## VOICE-LOCK

Envelope was already Kokoro `am_onyx` (metadata engine/voice + per-beat voice fields on every bookend). No dead ElevenLabs fields (voice_id / voice_env / clock prose) present to drop.
