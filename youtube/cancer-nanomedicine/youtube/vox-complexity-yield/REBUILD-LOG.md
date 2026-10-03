# REBUILD-LOG — vox-complexity-yield
_Rebuild: 2026-08-28_

## Phase 0 — pre-rebuild snapshot + envelope

- `beat_sheet.pre-rebuild.json` created (byte-exact copy of pre-edit `beat_sheet.json`).
- Envelope cleanup (VOICE-LOCK.md):
  - **Dropped** `voice_id` (ElevenLabs-era dead field).
  - **Dropped** `clock` prose (ElevenLabs-era hand-off note).
  - **Added** `engine: kokoro`, `voice_kokoro: am_onyx` (matches audio actually on disk and the invocation-declared voice).
  - **Added** `folderLabel: @NikBearBrown` (channel handle).

## Narration edits — LOCKED

All 13 narrations preserved **verbatim** from the pre-rebuild sheet. No datable-claim fixes were required (no model names, versions, prices, or "as of" phrases). No spark-line or verdict edits apply — this is a vox-editorial reel with title/question/section/endcard beats, not a Claude bookend reel.

## Shot-form rebuild (SHOT-FORM-SYSTEM)

Six body beats and both outros were rebuilt to real, renderable Remotion patterns. The pre-rebuild sheet referenced Manim scenes (`B04_GateMultiply`, `B05_YieldCollapse`, `B06_MathCard`, `B07_OneVsSix`, `B09_ProgramAB`, `B10_DesignChoice`) that do not exist on disk in any scene library — leaving them would silently slate the whole body. Text substitutes follow the same accepted tradeoff recorded in `hai-vox-complexity-yield` and `medhavy-vox-complexity-yield` (FILMLOOP-LOG 2026-08-28 / 2026-08-27).

| Beat | Pre-rebuild shot | Rebuilt shot | Why |
|------|-----------------|-------------|-----|
| B01 | CARD (title) | CARD (title) — unchanged | Falls through to slate; narration is a cold-open frame, no drawable spec. |
| B02 | STILL src=ai (gen-AI prompt) | REMOTION FormACard | `STILL src=ai` for a conceptual figure is a nopunt-catalog punt costume. FormACard itemises the six functions honestly. |
| B03 | CARD (question) | CARD (question) — unchanged | Falls through to slate; the question IS the frame. |
| B04 | GRAPHIC → `B04_GateMultiply` (Manim class not on disk) | REMOTION FormACard | Text substitute — every gate must open. |
| B05 | GRAPHIC → `B05_YieldCollapse` (Manim class not on disk) | REMOTION FormACard | Text substitute — the 1→90, 2→81 … 6→53 ladder. |
| B06 | GRAPHIC → `B06_MathCard` (Manim class not on disk) | REMOTION FormACard | Text substitute — 0.9^6 = 53% / 0.95^6 = 74%. |
| B07 | GRAPHIC → `B07_OneVsSix` (Manim class not on disk) | REMOTION FormBCard | Two-item contrast fits FormBCard cleanly. |
| B08 | CARD (section) | CARD (section) — unchanged | Falls through to slate; section aphorism. |
| B09 | GRAPHIC → `B09_ProgramAB` (Manim class not on disk) | REMOTION FormBCard | Two-program contrast fits FormBCard. |
| B10 | COMPOSITE → `B10_DesignChoice` (Manim class not on disk) | REMOTION FormACard | Text substitute — same quality, different economics. |
| B11 | CARD (endcard) | CARD (endcard) — unchanged | Falls through to slate. |
| B12 | OutroSeries with phantom props (`seriesTitle`/`tagline`/`githubSlug`) | OutroSeries with correct schema (`eyebrow`/`line`) | The phantom schema would silently default and misrender. Confirmed against `runtime/remotion/src/scenes/OutroSeries.tsx`. |
| B13 | OutroCTA with phantom props (`authorName`/`handle`/`ctaText`) | OutroCTA with correct schema (`line`/`handle`) | Same reason. Confirmed against `runtime/remotion/src/scenes/OutroCTA.tsx`. |

## Honest note

Six body beats (B04–B07, B09, B10) are FormACard/FormBCard text substitutes for the drawn diagrams the sheet originally intended. Same accepted tradeoff as sibling variants `hai-vox-complexity-yield` (2026-08-28) and `medhavy-vox-complexity-yield` (2026-08-27) — no `vox_graphics.py` or `scenes_std.py` module exists in this reel folder, and authoring one is out of scope for a single-invocation build. The substitute text preserves each beat's key nouns and numbers; a future Manim pass can slot the drawn figures in without touching narration.

## Bookends amendment

This is a vox-editorial reel. It has never had the Claude cold-open / verdict / your-turn / title-outro bookends (B00/BVDT/BHTF/BOUT). Its structural bookends are the B01 title CARD, B11 endcard CARD, B12 OutroSeries, and B13 OutroCTA. Absence of Claude bookends is legal under the rebuild contract's "non-claude channels keep their own skins" clause.
