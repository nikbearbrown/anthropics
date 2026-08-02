# SHOW-DON'T-TELL AUDIT — nbb-three-check-deployment

**Run:** 2026-07-25 10:23
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | I keep pushing changes and finding breakage days later, so I | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | The simulator works on your laptop. The three-check protocol | — | EXEMPT | — |
| B01 | Three checks catch three different failure modes. Functional | — | TELLS | Manim: concept_card — Three checks catch three different fai |
| B02 | Ask Claude to generate the three-check deployment verificati | —/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The protocol has three sections. Functional: five console te | —/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Functional check: all five pass. Environment check: one fail | — | TELLS | Manim: layer_stack — Functional check: all five pass. Enviro |
| B05 | Add a fourth accessibility check using axe-core in browser d | —/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Axe-core catches one critical issue: the step button has no  | — | TELLS | Manim: concept_card — Axe-core catches one critical issue: t |
| B07 | The three-check protocol is fifteen minutes that prevents a  | — | TELLS | Manim: concept_card — The three-check protocol is fifteen mi |
| B08 | Next: write the post-build document that makes your workflow | — | TELLS | Manim: pipeline_flow — Next: write the post-build document t |
| B09 | Like and subscribe for more Claude Code for Teachers. | —/NikBearBrownOutro | EXEMPT | — |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Run the Three-Check Deployment Verification Protocol with Cl | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

