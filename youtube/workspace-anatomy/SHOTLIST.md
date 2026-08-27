# SHOTLIST — workspace-anatomy

## Rhythm & Histogram
| Beat | Type | Source | Motion |
|---|---|---|---|
| B00 | REMOTION | own | ClaudeComposerAsk — composer types the ask |
| B01 | REMOTION | own | FormACard — title hold |
| B02 | MANIM | own | B02_ThreeRegions — layer stack: sensory / workspace / motor + CKA strip |
| B03 | MANIM | own | B03_BandSignatures — band boundary curve with elbows at L38 and L92 |
| B04 | MANIM | own | B04_Ignition — ambiguous-input bimodal snap at workspace entry |
| B05 | REMOTION | own | ChipGrid — NOT DETERMINABLE tier; ignition hedge four-chip label |
| B06 | MANIM | own | B06_Occupancy — two-panel: occupancy plateau ~25 + variance < 10% |
| B07 | MANIM | own | B07_ListOverflow — 80-word animal list; dashed unread animals in readout |
| B08 | MANIM | own | B08_Displacement — 25-slot grid: unrelated words displace each other |
| B09 | MANIM | own | B09_BroadcastHubs — MLP bars + broadcast heads + ablation comparison |
| B10 | MANIM | own | B10_Multitask — two concepts time-sharing across tokens |
| B11 | REMOTION | own | DeckPattern (threshold) — three anatomy claims vs GWT prediction |
| B12 | REMOTION | own | ClaudeVerdictArtifact — five-line verdict |
| B13 | REMOTION | own | ClaudeComposerAsk — Your Turn prompt |
| B14 | REMOTION | own | ClaudeTitleOutro — title restate outro |

## Act Map
COLD OPEN: B00 | TITLE: B01 | ACT I (Location): B02–B04 | HEDGE: B05 | ACT II (Capacity): B06–B08 | ACT III (Wiring): B09–B10 | VERDICT: B11–B12 | YOUR TURN: B13 | OUTRO: B14

## Manim scenes — all in scenes.py
B02_ThreeRegions · B03_BandSignatures · B04_Ignition · B06_Occupancy
B07_ListOverflow · B08_Displacement · B09_BroadcastHubs · B10_Multitask

Render one:
  cd anthropics/youtube/workspace-anatomy && manim -qh --fps 24 -r 1920,1080 scenes.py B02_ThreeRegions

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py anthropics/youtube/workspace-anatomy

## Open slots
None — no AI-gen video beats. All visuals are Manim or Remotion (own-source).
