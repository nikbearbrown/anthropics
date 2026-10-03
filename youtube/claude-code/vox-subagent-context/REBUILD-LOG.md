# REBUILD-LOG — vox-subagent-context

Rebuild date: 2026-08-31
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the
2026-08-19 sheet made BEFORE the first edit).

## What was LOCKED (carried over verbatim)

- Beat-body narration for **B01, B02, B03, B04, B05, B06, B07, B08, B09** —
  every sentence identical to the pre-rebuild sheet's `narration_text`.
- Slug, title, source pointer (`claude-code-for-teachers/chapters/10-subagents.md`),
  topic label (`CLAUDE CODE FOR TEACHERS`), color semantics (TEAL = subagent,
  TERRA = research bloat).

## What was REBUILT

### Envelope
- Dropped legacy `clock` prose from metadata (ElevenLabs-era wording).
- Dropped stale `build` record + `design_version: v1` (compile re-stamps).
- Kept `voice_kokoro: am_onyx`; added `channel: claude-liam`,
  `folderLabel: @NikBearBrown` for clarity.

### Bookends
- **B00**: greeting was placeholder `Liam` → `Bonjour, Liam` (world-hello
  rotation; adjacent reels used Namaste/Aloha/Salam, so French clears the
  window). `modelLabel: Claude Sonnet` added; `command` rewritten to a real
  question ("Why did one subagent query save 48% of the context window?").
- **BVDT**: `artifactLines` was placeholder `Key finding one/two/three` →
  three lines authored from the body:
  1. "Reads in the main session's window stay there — the session cannot unread a file."
  2. "A subagent runs in its own window and returns only the summary."
  3. "Research moves from 48% of the window to about 2%."
  `artifactHeading` was placeholder `Key findings` → `What the mechanism says`.
  Narration was empty → authored: "The verdict. Reads in the main session's
  window stay there for the rest of the run. A subagent runs in its own window
  and returns only the summary. That is why one query moved the research from
  forty-eight percent of the context to two."
- **BHTF**: `command` was template `Take what you learned from [X] and apply
  it to your own work.` → authored a real, executable exercise built from
  this reel's own mechanism (launch a subagent to do the read the viewer
  would otherwise inline; report before/after context percentage). Narration
  authored to match.
- **BOUT**: silent + `silence_s: 6.0` explicit; `slug` prop kept.

### Structural changes
- Removed the legacy `YOURTURN` beat — it duplicated BHTF's job (both were
  ClaudeComposerAsk `Your turn.` composers). BHTF is the canonical
  your-turn bookend; the earlier design's inline copy was redundant.
- Reworked **B07**: was a slate (`form: A` FormACard whose narration named
  a visual it never drew + `image_prompt` for an AI still + a stray
  `ClaudeTitleOutro` pattern + `act: OUTRO`). Now a real Manim graphic
  (`Scene_B07_GradingComparison`): two panels of 25 tally marks each — LEFT
  degrades bottom rows into MAIN SESSION; RIGHT feeds all 25 into a SUBAGENT
  box that returns a single PATTERN REPORT arrow to MAIN SESSION with all 25
  marks intact. Same narration, real drawn scene.
- Body cards **B01, B03, B09** routed from ambiguous `type: CARD` + Manim
  scene_class hybrid to explicit Remotion `FormACard` patterns. Same intent
  (title / question / endcard), template-first execution.
- **Scenes rewritten** (`scenes_std.py`): the pre-rebuild scenes were a
  generic two-bar comparison template repeated for every beat, with labels
  built from `narration[:30]` (mid-word truncations everywhere) and bar
  heights hardcoded 65/35 regardless of the actual narration figures. Every
  Manim scene now has its own hand-authored geometry with SHORT CATEGORY
  LABELS in Helvetica ALL-CAPS, bar heights that match the narration
  (30% / 48% / 22% / etc.), and layouts tuned for the 4K safe inset.

### Datable claims
None found — the reel talks about percentages of the context window and a
teacher scenario; nothing referenced a specific model version, price, or
"as of" date that has rotted.

## Audio
Fresh Kokoro `am_onyx` for every beat with narration. Bookends B00, BOUT
are silent (silence_s carried by clip duration). Measured durations became
the clock; no hand-timing.

## Renders
- Remotion (7 beats): B00, B01, B03, B09, BVDT, BHTF, BOUT — via
  `remotion_scenes.py` at 4K.
- Manim (6 beats): B02, B04, B05, B06, B07, B08 — via `manim -qk` at 4K,
  moved to `manim/`.

## Gates
- **FACTCHECK**: no datable claims added or changed; nothing new to check.
- **GATE T** (`type_check.py`): PASS after two content iterations —
  1) initial pass FAILed on B04 and B08 for terra accent contrast (TERRA
  stack detected as text, TERRA arrows in B08 detected as accent); 2) fixed
  by overlapping B04 blocks so they merge into one structural terra column
  (aspect ratio fails text-run filter), switching B08 arrows to INK, and
  placing the one terra moment on an underline under DESIGN in the caption.
  3) Third re-render fixed a §8.2 safe-inset overflow on B07's bottom
  caption (buff 0.25 → 0.5). PASS.
- **Gate V** (frame audit): sampled frames every 12s + full qc-sheet.png.
  All 13 beats legible, safe-inset clean, one terra moment per beat, no
  text-figure overlap.
