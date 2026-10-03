# AUDIT — hai-vox-fdg-proxy

Reel: HAI (humanitarians) channel, vox-editorial skin, Kokoro `am_onyx`.
Not a claude reel → no `B00 / BVDT / BHTF / BOUT` bookends; opens with title
card (B01), closes with `OutroSeries` (B13) + `OutroCTA` (B14).

## Phase 0
1. `beat_sheet.pre-rebuild.json` — copied byte-exact before edits.

## Phase 1 checks

| # | Check | Result |
|---|---|---|
| 1 | Stale renders | PASS — no mp4s in `media/`, `manim/`, or `clips/*.mp4` older than sheet |
| 2 | Bookends | N/A — non-claude reel; own skin retained (OutroSeries/OutroCTA) |
| 3 | Spark lines | N/A — no `ClaudeComposerAsk` beats |
| 4 | Verdict | PASS — B12 recap authored from body ("PET measures metabolism, not malignancy — imaging suggests, biopsy confirms"); not a template default |
| 5b | Chart text | ADVISORY — Manim scenes (B04/B05/B08/B10) declare production_viz labels; not rendered in this slate cut, so no chart-text render defect this pass |
| 5 | Card text | FIXED — B02/B06/B09 FormACard lines had ellipsis-truncated placeholder text; rewrote as short editorial hooks (paraphrase, not narration recital) |
| 6 | Punt sweep | LOGGED — B02, B09 remain `STILL src="ai"` (gen-AI ask by design); B01/B03/B07/B11/B12 are scripting-gap CARD/DOCUMENT with no Remotion pattern → will slate. See §Punt-log below. |
| 7 | Card-only reel | PASS — has 4 declared Manim beats (B04, B05, B08, B10) plus Remotion patterns |
| 8 | Lens audit | PASS — Popper (B06/B07 declare false-positive causes and dark-scan falsification in advance) + Plato (B05/B08 name artifact/world/relationship: PET signal → metabolism proxy → biology) |
| 9 | Brand fields | FIXED — dropped dead ElevenLabs `voice_id` + `clock` prose; `engine=kokoro`, `voice_kokoro=am_onyx` match the audio; palette=humanitarians is coherent with HAI outro |
| 10 | Pacing | LOGGED — B03 estimate 35 words / 18s = 1.94 wps (below 2.0); measured audio is 9.81s (fast). All other beats within 2.0–3.4 wps window against estimate. |
| 11 | type_check.py | PASS — GATE T green |

## Punt-log

Pipeline-owned beats with no rendered file yet (will slate this pass, listed
so the eventual full-render invocation knows what to fill):

- **B04** — Manim `B04_FDGUptake` — SCRIPTING-GAP (no scene file on disk)
- **B05** — Manim `B05_WhatPETSees` — SCRIPTING-GAP
- **B08** — Manim `B08_ImagingSuggests` — SCRIPTING-GAP
- **B10** — Manim `B10_ExampleResult` — SCRIPTING-GAP
- **B13** — Remotion `OutroSeries` — renderable via `remotion_scenes.py`
- **B14** — Remotion `OutroCTA` — renderable via `remotion_scenes.py`
- **B02, B06, B09** — Remotion `FormACard` — renderable via `remotion_scenes.py`

Human-owned (gen-AI ask by sheet design):
- **B02, B09** — STILL src="ai"; kept as gen-AI ask per sheet intent

Scripting-gap (no remotion pattern, no manim scene — will slate as request cards):
- **B01** (title CARD), **B03** (section CARD), **B07** (DOCUMENT quote),
  **B11** (DOCUMENT quote), **B12** (endcard CARD)

## Changes made to beat_sheet.json (pre-compile)

1. Dropped `metadata.voice_id` (ElevenLabs-era dead field)
2. Dropped `metadata.clock` (ElevenLabs GATE-0-era prose)
3. Rewrote `B02.shot.remotion.props.lines[0]` — was truncated ellipsis; now paraphrase
4. Rewrote `B06.shot.remotion.props.lines[0]` — was truncated ellipsis; now paraphrase
5. Rewrote `B09.shot.remotion.props.lines[0]` — was truncated ellipsis; now paraphrase

All narration text: LOCKED. No changes.
