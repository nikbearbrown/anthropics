# REBUILD-LOG — claude-liam-vox-trial-failure-tree

Rebuild pass 2026-08-31.

## Pre-rebuild snapshot
`beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json` before any edit.

## Envelope
- Dropped dead ElevenLabs field `voice_id` (was `TyW6NH39JcFb5M3xdIIk`).
- Dropped ElevenLabs-era `clock` prose (`"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"`).
- Added top-level `folderLabel: "@NikBearBrown"` (channel handle).
- VOICE-LOCK confirmed: engine=kokoro, voice=am_onyx, voice_kokoro=am_onyx.

## Legacy outros dropped
- `B14 OutroSeries` and `B15 OutroCTA` REMOVED. Reason: Claude-brand reel — `BOUT ClaudeTitleOutro` replaces them (Aug-19 skin_warnings already flagged B15). BVDT → BHTF → BOUT is now the close.

## Narration (edits, per rebuild contract)
Narration is LOCKED except for datable-claim fixes and audit-authorized additions.

- **B00** — was `""`, authored 44-word cold open (Habari greeting + one-sentence hook + one-sentence stakes).
- **BVDT** — was `""` with template `Key finding one/two/three` on-card; authored 60-word verdict recap that says the actual finding aloud (three failure modes, tracer cohort, 7% → 21% Program B example).
- **BHTF** — was `""` (card body was the 3,472-sheet placeholder `Take what you learned from [X] and apply it to your own work`); authored 55-word real exercise built on the reel's own three-failure-modes framework.
- **BOUT** — was `""`, authored 15-word title-restate outro.
- Body B01–B13 narration unchanged. Datable-claims pass: no rot found (illustrative numbers are labeled as such in metadata).

## Card / props edits (envelope, non-narration)
- **B00 ClaudeComposerAsk**: `greeting` `"Liam"` → `"Habari, Liam"` (Swahili — unused by adjacent claude-liam-vox-* reels in the batch: Bonjour, Ciao, Habari, Merhaba, Yassou etc. already in log; picked one not yet used). `segment` compressed from mid-word truncation `"The Cancer Trial That Couldn't Diagnose Its…"` to 4-word line `"Trial that couldn't diagnose failure"`. `command` rewritten from title-question to a direct question.
- **B01 FormBCard**: three placeholder items `Key point one/two/three` with empty `sub` → three real items grounded in B01 narration (`Elegant particle · Targeting ligand, chemo payload`; `6% response · Worse than standard of care`; `Program closed · No one can say why it failed`).
- **B02 FormACard**: single mid-word-truncated line (`"The particle was elegant — a polymeric nanoparticle with a targeting…"`) → two complete sentences.
- **B11 FormACard**: single mid-word-truncated line (`"Building delivery measurement into the trial — an imaging tracer cohort,…"`) → two complete sentences.
- **BVDT ClaudeVerdictArtifact**: `artifactHeading` `"Key findings"` (generic) → `"diagnosable failure vs unattributable failure"`. `artifactLines` template → 4 body-grounded lines.
- **BHTF ClaudeComposerAsk**: `command` template `Take what you learned from [X]…` → real 4-step exercise; `output` populated with 4-line rubric so the artifact is scaffolded, not empty.

## Punt sweep
- Cleared 5 stale `YOU → gen-AI clip → pantry` `needs` costumes on B02, B03, B05, B11, B13. Each now points at the pipeline renderer for its actual `shot.*` block (FormACard / CARD / DOCUMENT).
- No gen-AI asks remain. No Doodle*. No archive stills.
- All 7 Manim beats (B04, B06–B10, B12) already carried `PIPELINE → render animated_graphics.py scene B*_*` needs — unchanged.

## Locked (unchanged)
- Beat order, act labels, all body narration (B01–B13), all Manim scene names, all `production_viz` blocks, `card.copy` texts, `document.quote`, illustrative-number labeling.
