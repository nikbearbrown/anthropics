# SHOW-DON'T-TELL AUDIT — nbb-package-hallucination-scanner

**Run:** 2026-07-25 10:19
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | I like that the scanner checks each import against the PyPI  | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | Claude imports requests_oauth_helper — a name that doesn't e | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | Hallucinated package names appear across thousands of model  | GRAPHIC | TELLS | Manim: concept_card — Hallucinated package names appear acro |
| B02 | We ask Claude to write a package auditor that reads import s | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | Claude writes the auditor using requests and the PyPI API. I | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Scanner run: requests — EXISTS. numpy — EXISTS. requests_oau | GRAPHIC | TELLS | Manim: concept_card — Scanner run: requests — EXISTS. numpy  |
| B05 | We extend the scanner with a --npm flag for JavaScript impor | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | npm scan: react — EXISTS. lodash — EXISTS. react-query-optim | GRAPHIC | TELLS | Manim: concept_card — npm scan: react — EXISTS. lodash — EXI |
| B07 | The hallucination rate is low but the recurrence rate is hig | GRAPHIC | TELLS | Manim: bar_chart — The hallucination rate is low but the rec |
| B08 | Next: write a five-artifact Software Design Document with Cl | GRAPHIC | TELLS | Manim: concept_card — Next: write a five-artifact Software D |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Catch a Package Hallucination Before It Becomes a Slopsquatt | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

