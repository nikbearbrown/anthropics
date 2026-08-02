# SHOW-DON'T-TELL AUDIT — nbb-agentic-handoff-auditor

**Run:** 2026-07-25 11:48
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | I'm chaining prompts where one step's output feeds the next, | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | — | — | EXEMPT | — |
| B01 | Multi-step agentic prompts fail at handoffs — the boundary b | — | TELLS | Manim: pipeline_flow — Multi-step agentic prompts fail at ha |
| B02 | The audit command reads a multi-step agentic chain and class | — | TELLS | Manim: pipeline_flow — The audit command reads a multi-step  |
| B03 | The script reads the prompt chain, runs the handoff audit th | — | TELLS | Manim: pipeline_flow — The script reads the prompt chain, ru |
| B04 | The audit shows three handoffs: Step 1 to 2 is compatible. S | — | TELLS | Manim: pipeline_flow — The audit shows three handoffs: Step  |
| B05 | Fix the incompatible handoff by adding an explicit output fo | — | TELLS | Manim: pipeline_flow — Fix the incompatible handoff by addin |
| B06 | Handoff 2 to 3: incompatible turns compatible. The arrow tur | — | TELLS | Manim: pipeline_flow — Handoff 2 to 3: incompatible turns co |
| B07 | Agentic chains are only as reliable as their weakest handoff | — | TELLS | Manim: pipeline_flow — Agentic chains are only as reliable a |
| B08 | Next: a GIGO detector for data prompts — make the invisible  | — | TELLS | Manim: concept_card — Next: a GIGO detector for data prompts |
| B09 | — | — | EXEMPT | — |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Build an Agentic Prompt Handoff Auditor with Claude | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 8
- Rebuilt (Manim rendered): 8
- Skipped (render failed): 0
- scenes_std.py written: 8 classes

