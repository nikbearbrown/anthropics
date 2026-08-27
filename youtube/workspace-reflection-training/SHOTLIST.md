# SHOTLIST — workspace-reflection-training

## Rhythm & Histogram
| Beat | Type | Source | Motion |
|---|---|---|---|
| B00 | REMOTION | own | ClaudeComposerAsk — composer types the ask |
| B01 | REMOTION | own | FormACard — title hold |
| B02 | MANIM | own | B02_ThePrediction — three-step syllogism: might-say → says → thinks |
| B03 | MANIM | own | B03_CRTBefore — J-space before CRT: task tokens, ethics absent |
| B04 | MANIM | own | B04_CRTData — truncate → append reflection Q → gradient on answer |
| B05 | MANIM | own | B05_HonestyNumbers — paired bars: dishonesty 0.25→0.07, deception 0.38→0.05 |
| B06 | MANIM | own | B06_HowItWins — before/after response distributions |
| B07 | MANIM | own | B07_LensReceipts — top ethics/reflection token appearance rate delta |
| B08 | MANIM | own | B08_AblationControl — Fig 50-C: intact vs ablated deception scores |
| B09 | REMOTION | own | ChipGrid — four-chip honest evidence label |
| B10 | REMOTION | own | ClaudeVerdictArtifact — five-line verdict |
| B11 | REMOTION | own | ClaudeComposerAsk — Your Turn prompt |
| B12 | REMOTION | own | ClaudeTitleOutro — title restate outro |

## Act Map
COLD OPEN: B00 | TITLE: B01 | PREDICTION: B02 | BEFORE: B03 | METHOD: B04 | NUMBERS: B05–B06 | MECHANISM: B07 | CONTROL: B08 | EVIDENCE LABEL: B09 | VERDICT: B10 | YOUR TURN: B11 | OUTRO: B12

## Manim scenes — all in scenes.py
B02_ThePrediction · B03_CRTBefore · B04_CRTData · B05_HonestyNumbers
B06_HowItWins · B07_LensReceipts · B08_AblationControl

Render one:
  cd anthropics/youtube/workspace-reflection-training && manim -qh --fps 24 -r 1920,1080 scenes.py <ClassName>

## Open slots
None — no AI-gen video beats. All visuals are Manim or Remotion (own-source).
