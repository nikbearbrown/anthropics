# SHOTLIST — workspace-five-tests

## Rhythm & Histogram
| Beat | Type | Source | Motion |
|---|---|---|---|
| B00 | REMOTION | own | ClaudeComposerAsk — composer types the ask |
| B01 | REMOTION | own | FormACard — title hold |
| B02 | MANIM | own | B02_FiveProperties — hub-and-spoke, five workspace properties |
| B03 | MANIM | own | B03_InjectReport — concept vector injection diagram |
| B04 | MANIM | own | B04_FocusIgnore — three-condition citrus bar chart |
| B05 | MANIM | own | B05_WhiteBear — ignore > 0 bar with polar bear watermark circles |
| B06 | MANIM | own | B06_TwoHop — Eiffel Tower → France (midlayer) → Paris (output) |
| B07 | MANIM | own | B07_ArithmeticOrder — (4+17)*2+7 layer-order lollipop markers |
| B08 | MANIM | own | B08_SwapScore — 76/192 and 101/192 scoreboard panels |
| B09 | MANIM | own | B09_ProbeSplit — probe decomposed into J-space + complement arrows |
| B10 | MANIM | own | B10_Generalization — hub-and-spoke, one swap → 8 template spokes |
| B11 | MANIM | own | B11_AblationBattery — before/after task bars under ablation |
| B12 | MANIM | own | B12_SelectiveCollapse — two-column flexible vs automatic |
| B13 | MANIM | own | B13_CoOccupancy — paired bars 0.46/0.53 vs 0.09/0.29 |
| B14 | REMOTION | own | ChipGrid — five-property scorecard |
| B15 | REMOTION | own | ClaudeVerdictArtifact — verdict |
| BHTF | REMOTION | own | ClaudeComposerAsk — Your Turn prompt |
| BOUT | REMOTION | own | ClaudeTitleOutro — title restate outro |

## Act Map
COLD OPEN: B00 | TITLE: B01 | ACT I (What Is a Workspace?): B02–B03 | ACT II (Test 1 — Verbal Report): B04–B05 | ACT III (Test 2 — Internal Reasoning): B06–B07 | ACT IV (Test 3 — Directed Modulation): B08–B09 | ACT V (Test 4 — Flexible Generalization): B10–B11 | ACT VI (Test 5 — Selectivity): B12–B13 | VERDICT: B14–B15 | YOUR TURN: BHTF | OUTRO: BOUT

## Manim scenes — all in scenes.py
B02_FiveProperties · B03_InjectReport · B04_FocusIgnore · B05_WhiteBear
B06_TwoHop · B07_ArithmeticOrder · B08_SwapScore · B09_ProbeSplit
B10_Generalization · B11_AblationBattery · B12_SelectiveCollapse · B13_CoOccupancy

Render all:
  cd anthropics/youtube/workspace-five-tests && manim -qh --fps 24 -r 1920,1080 scenes.py <ClassName>

## Open slots
None — no AI-gen video beats. All visuals are Manim or Remotion.
