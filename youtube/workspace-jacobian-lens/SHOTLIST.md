# SHOTLIST — workspace-jacobian-lens

## Rhythm & Histogram
| Beat | Type | Source | Motion |
|---|---|---|---|
| B00 | REMOTION | own | ClaudeComposerAsk — composer types the ask |
| B01 | REMOTION | own | FormACard — title hold |
| B02 | MANIM | own | B02_ResidualStack — token column rising through layer stack |
| B03 | MANIM | own | B03_JLensGradient — gradient arrows; one vector per token |
| B04 | MANIM | own | B04_ReadoutRanking — activation projection → top-K word list |
| B05 | REMOTION | own | DeckPattern (divergence) — three lenses, one activation |
| B06 | MANIM | own | B06_SixPrompts — six prompt types × midlayer readout words |
| B07 | MANIM | own | B07_LensBakeoff — Fig 52 animated bar comparison, six families |
| B08 | MANIM | own | B08_SwapSurgery — spider→ant swap; answer follows |
| B09 | STILL | archive | img_1b62b10ab235e6e7.png — §2.1 methods figure, kenburns |
| B10 | REMOTION | own | StepStream — pivot card, third step active |
| B11 | MANIM | own | B11_SingleTokenBlindSpot — blackmail splits; lens sees only 'black' |
| B12 | MANIM | own | B12_TemplateOracle — two patch-lenses appear |
| B13 | REMOTION | own | ChipGrid — four-chip honest label |
| B14 | REMOTION | own | ClaudeVerdictArtifact — five-line verdict |
| BHTF | REMOTION | own | ClaudeComposerAsk — Your Turn prompt |
| BOUT | REMOTION | own | ClaudeTitleOutro — title restate outro |

## Act Map
COLD OPEN: B00 | TITLE: B01 | ACT I (The Instrument): B02–B05 | ACT II (Evidence): B06–B09 | PIVOT: B10 | ACT III (Blind Spot): B11–B12 | VERDICT: B13–B14 | YOUR TURN: BHTF | OUTRO: BOUT

## Manim scenes — all in scenes.py
B02_ResidualStack · B03_JLensGradient · B04_ReadoutRanking · B06_SixPrompts
B07_LensBakeoff · B08_SwapSurgery · B11_SingleTokenBlindSpot · B12_TemplateOracle

Render all:
  cd anthropics/youtube/workspace-jacobian-lens && manim -qh --fps 24 -r 1920,1080 scenes.py <ClassName>

## Archive still
B09: pantry/stills/img_1b62b10ab235e6e7.png (§2.1 methods figure; kenburns)
Credit: Gurnee*, Sofroniew* et al., 'Verbalizable Representations Form a Global Workspace in Language Models', Transformer Circuits Thread, Anthropic, July 2026 — §2.1 methods figure, reproduced for educational criticism.

## Open slots
None — no AI-gen video beats. All visuals are Manim, Remotion, or pantry archive.
