# SHOW-DON'T-TELL AUDIT — nbb-pretooluse-grade-blocker

**Run:** 2026-07-25 10:20
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | I want to actually build the PreToolUse hook that stops Clau | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | NEVER generate a final grade in CLAUDE.md lasts two sessions | — | EXEMPT | — |
| B01 | A CLAUDE.md instruction is probabilistic — Claude weights it | — | TELLS | Manim: concept_card — A CLAUDE.md instruction is probabilist |
| B02 | Ask Claude to write the PreToolUse hook script and the setti | —/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The hook reads the Write tool input from stdin as JSON, extr | —/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Hook test: ask Claude to summarize student performance. Clau | — | TELLS | Manim: bar_chart — Hook test: ask Claude to summarize studen |
| B05 | Extend the hook to distinguish grade percentages from quanti | —/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Extended hook: the student scored in the top 15% of the clas | — | TELLS | Manim: bar_chart — Extended hook: the student scored in the  |
| B07 | The PreToolUse hook is the enforcement layer below the instr | — | TELLS | Manim: two_column — The PreToolUse hook is the enforcement l |
| B08 | Next: deploy a pattern-analysis subagent that keeps the main | — | TELLS | Manim: concept_card — Next: deploy a pattern-analysis subage |
| B09 | Like and subscribe for more Claude Code for Teachers. | —/NikBearBrownOutro | EXEMPT | — |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Build a PreToolUse Hook That Blocks Grade Generation with Cl | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

