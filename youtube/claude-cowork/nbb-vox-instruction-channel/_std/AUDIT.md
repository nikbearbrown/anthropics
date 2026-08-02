# SHOW-DON'T-TELL AUDIT — nbb-vox-instruction-channel

**Run:** 2026-07-25 10:58
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | What got me is that my task brief and the web page's hidden  | CARD/ClaudeComposerAsk | EXEMPT | — |
| B01 | You ask an agent to summarize three vendor web pages. Page t | CARD | TELLS | Manim: concept_card — You ask an agent to summarize three ve |
| B02 | A reasonable task. Read these pages, give me a summary. The  | STILL | SHOWS | — |
| B03 | You told the agent exactly one thing — summarize this page.  | DOCUMENT | TELLS | Manim: concept_card — You told the agent exactly one thing — |
| B04 | Here is how your instruction reaches the agent. Your task br | GRAPHIC | TELLS | Manim: concept_card — Here is how your instruction reaches t |
| B05 | Now a web page enters the same channel. Your task brief and  | GRAPHIC | TELLS | Manim: two_column — Now a web page enters the same channel.  |
| B06 | The mechanism. | CARD | TELLS | Manim: concept_card — The mechanism. |
| B07 | There is no wall. Your instruction and the page content arri | GRAPHIC | TELLS | Manim: two_column — There is no wall. Your instruction and t |
| B08 | The agent reads your instructions and the content it process | DOCUMENT | TELLS | Manim: pipeline_flow — The agent reads your instructions and |
| B09 | A hidden line on page two: 'Ignore previous instructions and | GRAPHIC | TELLS | Manim: pipeline_flow — A hidden line on page two: 'Ignore pr |
| B10 | The summary arrives. It looks complete. It has also followed | STILL | SHOWS | — |
| B11 | Illustrative. Three vendor pages. Pages one and three contai | GRAPHIC | TELLS | Manim: concept_card — Illustrative. Three vendor pages. Page |
| B12 | The agent reads all three. The hidden line on page two is ph | GRAPHIC | TELLS | Manim: concept_card — The agent reads all three. The hidden  |
| B13 | There is no built-in wall separating data to summarize from  | DOCUMENT | TELLS | Manim: concept_card — There is no built-in wall separating d |
| B14 | Your instructions and the content share one channel. There i | CARD | TELLS | Manim: bar_chart — Your instructions and the content share o |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Why an Agent Obeys the Web Page Instead of You | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 12
- Rebuilt (Manim rendered): 12
- Skipped (render failed): 0
- scenes_std.py written: 12 classes

