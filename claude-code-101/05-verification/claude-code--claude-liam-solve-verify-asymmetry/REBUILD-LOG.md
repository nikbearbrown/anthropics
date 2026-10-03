# REBUILD-LOG.md — claude-liam-solve-verify-asymmetry

Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy of pre-edit sheet).

## LOCKED (carried verbatim)
Every body-beat narration string is byte-identical to the pre-rebuild sheet.
No datable-claim edits required (no rotted model names/versions/prices).

Verified locked narrations: B00, B01, B02, B03, B04, B05, B06, B07, B08.

## REBUILT (envelope + skin, per current doctrine)

### Metadata envelope
- Dropped intermediate `_variant_todo` scratch list.
- Dropped stale `build{...}` block from the pre-rebuild snapshot (compiler
  re-stamps it on the next build).
- Added top-level `folderLabel: "@NikBearBrown"` for the claude-liam persona
  on the @NikBearBrown channel.
- VOICE-LOCK: `engine: kokoro`, `voice: am_onyx`. No ElevenLabs fields to drop.

### Cold open (B00)
- Pattern: `NikBearBrownOpen` → `ClaudeComposerAsk` (COLD OPEN LAW; palette
  is claude — the sheet's own skin_warnings flagged this).
- Greeting: `"Ciao, Liam"` (world-language rotate; Liam persona, one-word cue;
  Wagwan reserved for Bear per IN-FOR-BEAR LAW).
- Props re-shaped to the current ClaudeComposerAsk zod schema (command / topic
  / segment / runningText / folderLabel / modelLabel / effortLabel).

### Inner composer beats (B02, B05)
- Pattern: `NikBearBrownTerminalAsk` (legacy dark terminal) → `ClaudeComposerAsk`
  (SKILL: same prop contract, swap the scene name for claude palette).
- Spark lines (≤4 words, compressed from the beat's own narration):
  - B02: `"Top three by GPA."`   (was `"The ask,"` — Bear-only arc cue)
  - B05: `"Audit the tie-break."`  (was `"The ask,"` — Bear-only arc cue)

### Code beat (B03)
- Pattern: `NikBearBrownCodeBlock` → `ClaudeCodeBeat` (claude palette parity).
- Code preserved verbatim, comments compressed for legibility on the card.
- sparkLine: `"Looks correct."` (from narration).

### Punt sweep — animated the slates
- B01 (was `PIPELINE → fill_slates/remotion_scenes` slate): FormBCard with
  three items (fixed the pre-rebuild's mid-word labels; `sub` is real content,
  not a placeholder).
- B04 (was Manim slate `B04_SolveVerifyBars` — scene class did not exist in
  runtime): FormBCard 3-item — `Solve / 8 seconds`, `Verify / 4 minutes`,
  `Gap / 30x`. Nopunt catalog row: "comparison / a winner" → drawn structure.
- B06 (was Manim slate `B06_AsymmetryTrend` — scene class did not exist):
  FormACard, three lines pulled from the narration.
- B07 (was `ClaudeTitleOutro` around synthesis narration — misuse of the
  outro pattern): FormBCard 2-item — `Solve / Pattern completion — fast` vs
  `Verify / Deliberate judgment — slow`. This is the mechanism split the
  narration argues.
- B08 (was FormBCard with truncated label `"Next: label the five supervisory"`):
  FormACard, two lines. Narration is locked.

### Deduplicated your-turn beat
- Pre-rebuild sheet had TWO your-turn beats: body `YOURTURN` (real content,
  ClaudeComposerAsk) and bookend `BHTF` (empty narration + placeholder
  `[Demonstrate...]` template command — the 3,472-sheet Your-Turn placeholder
  caught 2026-08-30).
- Consolidation: dropped the body YOURTURN slot; moved its LOCKED narration
  and its authored command into the BHTF bookend. No narration was lost.
- BHTF `command` no longer contains a placeholder `[bracket]`; carries the
  same specific ask the body YOURTURN carried, augmented with an `output`
  field (2 lines) that names the exercise concretely ("Time the solve pass.
  Time the verify pass. Post the ratio in the comments.").

### Verdict (BVDT) — authored (PHASE 1.4)
- Pre-rebuild lines were the template placeholder set: `"Key finding one",
  "Key finding two", "Key finding three"` — a `verdict_audit.py` reject.
  Narration was empty (Bear noted "here is what the evidence shows" is the
  matching placeholder register that this reel had never carried).
- Body is 9 beats and ~230 words — over the 5/180 authorship floor.
- Authored `artifactLines` from the body's own nouns/numbers:
  1. `"Solve: 8 seconds. Verify: 4 minutes. A 30x gap on one small task."`
  2. `"Solve speed doubles every ~18 months. Verify speed does not."`
  3. `"Fluent output is not correct output — probe every one."`
  4. `"Your job is not to solve faster. It is to verify better."`
- Authored `narration_text` reads the finding aloud (was empty).

### Outro (BOUT)
- Dropped `mascotSeed` (not in current schema); `slug` seeds the mascot per
  OUTRO-LOCK.md.
- Authored spoken narration for BOUT (was empty): title restate + IN-FOR-BEAR
  sign-off ("Liam, in for Bear.").

## Notes
- Non-claude channel skin rule: the reel's `channel` is `NikBearBrown`, but the
  slug/palette declares the claude-liam persona (@NikBearBrown channel, claude
  skin). Bookends are the four claude patterns; footer chip is `@NikBearBrown`
  per Liam / IN-FOR-BEAR LAW.
- No template misses were logged — every beat's form has a live component.
