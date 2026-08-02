# SHOW-DON'T-TELL AUDIT — nbb-engineering-partner-loop

**Run:** 2026-07-25 10:16
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | I want to run the engineering partner loop on a real failing | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | Nik Bear Brown. Build it with a CLI, then take it apart. | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | The verification oracle runs first — then Claude fixes the c | GRAPHIC | TELLS | Manim: pipeline_flow — The verification oracle runs first —  |
| B02 | In the terminal: ask Claude Code to follow the engineering p | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | Read the diff before running. The change is minimal — one fu | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Run the oracle. The test suite reports exit code zero. test_ | GRAPHIC | TELLS | Manim: cycle_diagram — Run the oracle. The test suite report |
| B05 | Introduce a second failing test requiring a different fix. A | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Both tests pass. Two distinct fixes — one for empty string,  | GRAPHIC | TELLS | Manim: two_column — Both tests pass. Two distinct fixes — on |
| B07 | The oracle is the control system. Without it, 'Claude fixed  | GRAPHIC | TELLS | Manim: concept_card — The oracle is the control system. With |
| B08 | Your move: take one known failing test from your own codebas | GRAPHIC | TELLS | Manim: cycle_diagram — Your move: take one known failing tes |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Run the Engineering Partner Loop with Claude Code | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

