# SHOW-DON'T-TELL AUDIT — nbb-spec-prompt-audit

**Run:** 2026-07-25 10:22
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | The pandas-import-that-breaks-the-lab-machine versus stdlib  | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | Two prompts, one minute apart, same model. The specification | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | A specification prompt is not a longer prompt — it is a diff | GRAPHIC | TELLS | Manim: concept_card — A specification prompt is not a longer |
| B02 | We run two prompts side by side: a weak vague request, and a | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The specification output uses csv.reader with encoding utf-8 | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Two outputs, side by side. The specification version: 42 lin | GRAPHIC | TELLS | Manim: concept_card — Two outputs, side by side. The specifi |
| B05 | We run the weak prompt twice and show the two outputs differ | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Weak prompt run 1: pandas. Weak prompt run 2: openpyxl. Both | GRAPHIC | TELLS | Manim: two_column — Weak prompt run 1: pandas. Weak prompt r |
| B07 | A specification is not a longer prompt. It is a set of invar | GRAPHIC | TELLS | Manim: concept_card — A specification is not a longer prompt |
| B08 | Next: catch a package hallucination before it becomes a slop | GRAPHIC | TELLS | Manim: concept_card — Next: catch a package hallucination be |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Build and Audit a Specification Prompt with Claude Code | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

