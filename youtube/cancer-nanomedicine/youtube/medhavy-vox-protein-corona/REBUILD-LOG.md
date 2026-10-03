# REBUILD-LOG — medhavy-vox-protein-corona

Rebuild pass 2026-08-30. Old sheet copied verbatim to
`beat_sheet.pre-rebuild.json` before any edit.

## Locked (no change)
- All 13 `narration_text` bodies (no datable claims — the illustrative folate
  numbers in B09 are already labelled "illustrative numbers" in narration).
- Beat order, act labels, `graphic.manim` scene intents, `card` copy/sub,
  metadata identity (title, slug, topic, register, palette=medhavy,
  audience=MEDHAVY, engine=kokoro, voice_kokoro=af_kore).

## Envelope normalized (dead ElevenLabs-era fields dropped)
- `metadata.voice_id: "1sgY6Voq1aexKOB1IJ2D"` → REMOVED (VOICE-LOCK: no
  ElevenLabs, ever). Voice is controlled by `metadata.engine` + `voice_kokoro`.
- `metadata.clock: "narration (Kokoro (VOICE-LOCK)) — ... until GATE 0 audio
  lock"` → REMOVED (references GATE 0 which was abolished 2026-08-22).

## Palette hygiene (Claude-wash removed)
- **B03**: `shot.remotion.pattern: FormACard` (Claude palette) → REMOVED.
  A Claude-branded text card in the middle of a medhavy vox reel visually
  breaks the vox-editorial ground. B03 will slate honestly on the vox palette
  (`#F3EBDD` / `#2F2A26`) via `compile.py`'s slate generator. The beat's real
  home is a mechanism illustration (proteins swarming a particle); leaving it
  as a declared slate names exactly what's missing.

## Schema conforms (Remotion prop mismatches)
- **B12 OutroSeries**: props were `{seriesTitle, tagline, githubSlug}` (old
  schema). Current zod schema is `{eyebrow, line}`. Migrated:
  - `eyebrow: "CANCER NANOMEDICINE"`
  - `line: "Part of the Cancer Nanomedicine series on Medhavy AI."`
- **B13 OutroCTA**: props were `{authorName, handle, ctaText}` (old schema).
  Current zod schema is `{line, handle}`. Migrated:
  - `line: "Explore the full course at medhavy.com"`
  - `handle: "@MedhavyAI"`

## Not rebuilt (out of scope for this pass)
- `shot.form` derivation per SHOT-FORM-SYSTEM: the sheet's `shot.type`
  (CARD/GRAPHIC/STILL/COMPOSITE) + `graphic.manim` scene names already carry
  the routing intent for the current `compile.py`. Adding `form` would be
  additive and is not required for the review slate cut.
- Manim scene classes named in `graphic.manim` (B04_CoronaForms,
  B05_LigandMasked, B06_OpsominClearance, B07_TwoEnvironments,
  B09_FolateExample, B10_CoronaSummary) do NOT exist in
  `runtime/manim/animated_graphics.py`. Those six beats will slate honestly
  in the review cut; authoring them is a follow-up.
