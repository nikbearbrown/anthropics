# SHOW-DON'T-TELL AUDIT — nbb-boondoggle-score

**Run:** 2026-07-25 09:40
**Brand:** claude-liam  **Palette:** #F2F0E9/#3D3929/#D97757

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | You made the highest-risk row the one every other step inher | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | Before Claude sees a single prompt, you know which step is h | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | A handoff condition must be machine-checkable — it names a t | GRAPHIC | TELLS | Manim: pipeline_flow — A handoff condition must be machine-c |
| B02 | We ask Claude to generate a Boondoggle Score table for Phase | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | Claude returns five steps. Every handoff condition names a p | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | The Boondoggle Score table — five steps, critical path highl | GRAPHIC/B04_BoondoggleTable | SHOWS | — |
| B05 | We deliberately set row 1's handoff condition to 'Claude com | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | The validator flags it: not machine-checkable. Then shows th | GRAPHIC/B06_InvalidHandoff | SHOWS | — |
| B07 | The Boondoggle Score is a diagnostic before a single line of | GRAPHIC | TELLS | Manim: concept_card — The Boondoggle Score is a diagnostic b |
| B08 | Next: run the three-pass verification protocol. | GRAPHIC | TELLS | Manim: concept_card — Next: run the three-pass verification  |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Score a Build Plan Using the Boondoggle Score with Claude Co | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 3
- Rebuilt (Manim rendered): 3
- Skipped (render failed): 0
- scenes_std.py written: 3 classes

