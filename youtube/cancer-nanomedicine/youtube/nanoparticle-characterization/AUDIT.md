# AUDIT.md — nanoparticle-characterization

Ran 2026-08-27, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet — DONE.
- Dead ElevenLabs fields (`voice_id` in metadata) — DROPPED.
- Metadata voice envelope normalized: `voice: nbbhuman`, `engine: kokoro`, `voice_kokoro: am_onyx`.
- Non-Claude channel skins retained: `NikBearBrownOpen` (B00) and `NikBearBrownOutro` (B09) — NOT Claude-washed.
- Bookends BVDT / BHTF / BOUT kept as the sheet already had them (ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro).
- Narration is LOCKED. No datable claims found needing rewrite. See REBUILD-LOG.md.

## Phase 1 — checks

1. Stale renders — PASS. No mp4s on disk (never rendered).
2. Bookends — PASS. B00 / BVDT / BHTF / BOUT present with canonical patterns.
3. Spark lines — PASS. B02 / B05 have `greeting: "The ask,"`. BHTF has `greeting: "Your turn."`. B00 is a `NikBearBrownOpen` (nbb channel) — greeting rotation N/A.
4. Verdict — FIXED. Body has 8 beats and >180 words; authored real verdict from body nouns (distribution, seven measurements, artifact, buffer vs plasma, batch variability). BVDT narration rewritten to speak the verdict aloud.
5. Card text — FIXED. B01 items were `Key point one/two/three` with empty subs; rewritten with concrete claims from the narration. All other FormBCards written from scratch (was `shot.source: null`).
5b. Chart text — N/A. No Manim / D3 charts in this reel.
6. Punt sweep — FIXED. Four body beats (B04/B06/B07/B08) had `shot.source: null` (punts). Each routed to a `FormBCard` written from its own narration and `visual_intent`.
7. Card-only reel — PASS. Body has B02 terminal ask, B03 code block, B05 terminal ask — three non-card beats.
8. Lens audit — PASS. The reel runs Popper (state, in advance, the seven measurements and what each fails to catch), Plato (artifact = characterization certificate; world = plasma / patient; relationship = corona shifts everything after injection), and Hume (confidence from buffer measurements is a property of the buffer, not of the patient). Three moves earned.
9. Brand fields — PASS. `folderLabel: "@NikBearBrown"`. `voice: nbbhuman` matches the "Nik Bear Brown" persona in narration.
10. Pacing — PASS. Beat WPS estimates fall inside 2.0–3.4 (checked B01 ≈2.2, B04 ≈2.4, B06 ≈2.9, B07 ≈2.4, B08 ≈2.8). Kokoro measurement will reset the clock.
11. `type_check.py` — PASS. Two advisories: B00 recites its card (LOCKED by rebuild contract — cold-open narration is not editable), BVDT recites its card (verdict card text and verdict narration are meant to converge; advisory does not block).

## Phase 2 — build

Proceeding to Kokoro audio and Remotion renders; slate-review cut planned.
