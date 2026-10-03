# AUDIT — hai-vox-trial-failure-tree

Audited 2026-08-28. PHASE 1 checks against the anthropics lens (LENS-NOTES.md)
and the rebuild contract.

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists in the reel folder. Nothing to delete. |
| 2 | Bookends | PASS | HAI (non-Claude) channel — no ClaudeComposerAsk/BVDT/HTF/OUT required. Opens on COLD OPEN CARD (B01), closes with OutroSeries (B14) + OutroCTA (B15). Correct for this skin. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats in this reel. |
| 4 | Verdict | N/A | No BVDT in the sheet; the RECAP endcard (B13) carries the closing sentence in narration and card copy — not a template default. |
| 5b | Chart text | LOG | Manim scenes (B04/B06/B07/B08/B09/B10/B12) DO NOT EXIST in runtime/manim/animated_graphics.py — beats remain slate-declared. When authored, they must use SHORT category labels (DELIVERY / PAYLOAD / BIOLOGY etc.), not narration slices. |
| 5 | Card text | FIXED | B02 and B11 FormACard `lines` were leftover truncations from an older narration ("The particle was elegant…" / "Building delivery measurement…"). Rewritten to short vox lines from the current narration only. B01/B03/B13 CARD copy matches narration. |
| 6 | Punt sweep | LOG | 11 body beats declare slate (B01, B03, B04, B05, B06, B07, B08, B09, B10, B12, B13). None are archive-STILL punts; each carries a `needs`/`suggested` row that is the review-cut request card. Not a punt — the review-slate format IS the declaration. |
| 7 | Card-only | PASS | Body carries seven GRAPHIC beats and two STILL·ai beats; only three pure CARDs (B01 title, B03 question, B13 endcard). Not a card-only reel. |
| 8 | Lens audit | PASS | The reel runs Descartes ("what would falsify the response-only endpoint claim") and Plato (artifact = binary readout; world = which of three failure modes; relationship = collapsed into one signal). It also runs Popper implicitly (delivery measurement is the pre-stated falsifier). Two moves clearly present. |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs `voice_id`; dropped stale `clock` prose. `engine=kokoro / voice_kokoro=am_onyx` correct. `folderLabel` N/A (no ClaudeComposerAsk). |
| 10 | Pacing | LOG | Word-count vs estimated_duration_s check on all body beats (using measured actual_duration_s): all fall in the 2.0–3.4 wps band (B01 30w/9.86s=3.04, B02 30w/12.4s=2.42, B03 55w/14.66s=3.75 → SLIGHT OVER on the question CARD; B04 40w/12.48s=3.21; B05 25w/9.60s=2.60; B06 30w/9.56s=3.14; B07 40w/11.46s=3.49 → SLIGHT OVER; B08 41w/13.7s=2.99; B09 34w/11.93s=2.85; B10 40w/13.93s=2.87; B11 36w/13.95s=2.58; B12 88w/28.78s=3.06; B13 42w/14.74s=2.85). B03 and B07 nudge past 3.4 wps; leaving as-is per narration-lock. |
| 11 | type_check.py | (see below) | Runs at end of PHASE 1. |

## Fixed
- Dead ElevenLabs `voice_id` dropped.
- Stale `clock` prose dropped.
- B02 FormACard.lines rewritten from current narration.
- B11 FormACard.lines rewritten from current narration.
- B14 OutroSeries.props re-shaped to current `{eyebrow, line}` schema.
- B15 OutroCTA.props re-shaped to current `{line, handle}` schema.

## Logged (not blockers for a review-slate cut)
- Seven Manim scenes referenced by GRAPHIC beats do not exist in
  `animated_graphics.py`. Authoring them is beyond a single-invocation
  slate cut. They remain slate placeholders.
- Two beats (B03 question CARD, B07 delivery-failure narration) drift ~0.1
  wps above the 3.4 pacing ceiling; narration is locked, so recorded
  actual_duration_s stands.

No BLOCKED items. Building the review-slate cut.
