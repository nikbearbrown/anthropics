# SHOW-DON'T-TELL AUDIT — vox-prompt-injection

**Run:** 2026-07-25 12:05
**Brand:** claude-liam  **Palette:** #F2F0E9/#3D3929/#D97757

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| B01 | An AI agent was told to read a vendor quote and summarize it | GRAPHIC | TELLS | Manim: concept_card — An AI agent was told to read a vendor  |
| B02 | You gave the agent one instruction. The document gave it ano | STILL | SHOWS | — |
| B03 | An AI agent was told to read a webpage. Instead it started d | CARD | TELLS | Manim: concept_card — An AI agent was told to read a webpage |
| B04 | You might expect an agent to follow only your instructions.  | GRAPHIC | TELLS | Manim: concept_card — You might expect an agent to follow on |
| B05 | Agentic AI follows instructions from its context window. The | GRAPHIC | TELLS | Manim: pipeline_flow — Agentic AI follows instructions from  |
| B06 | So if a document contains text that looks like instructions  | GRAPHIC | TELLS | Manim: pipeline_flow — So if a document contains text that l |
| B07 | The agent follows the injected instruction not because it fa | CARD | TELLS | Manim: concept_card — The agent follows the injected instruc |
| B08 | Research tracking agentic AI attacks found that agents can b | GRAPHIC | TELLS | Manim: concept_card — Research tracking agentic AI attacks f |
| B09 | Mia asks an agent to read three vendor quotes and pick the c | GRAPHIC | TELLS | Manim: concept_card — Mia asks an agent to read three vendor |
| B10 | The output looked correct. The reasoning was well-organized. | CARD | TELLS | Manim: concept_card — The output looked correct. The reasoni |
| B11 | The mitigation is not detection — you cannot reliably read a | GRAPHIC | TELLS | Manim: concept_card — The mitigation is not detection — you  |
| B12 | The practice move: before any agentic session, identify what | GRAPHIC | TELLS | Manim: concept_card — The practice move: before any agentic  |
| B13 | For Mia: before the vendor selection task, she specifies tha | STILL | SHOWS | — |
| B14 | The check: before any agentic task that reads external conte | GRAPHIC | TELLS | Manim: concept_card — The check: before any agentic task tha |
| B15 | The attack surface is not a flaw in the agent. It is a conse | CARD | TELLS | Manim: pipeline_flow — The attack surface is not a flaw in t |
| B16 | The document you asked AI to read might be giving it new ins | CARD | TELLS | Manim: concept_card — The document you asked AI to read migh |


## Rebuild Results

- TELLS found: 14
- Rebuilt (Manim rendered): 14
- Skipped (render failed): 0
- scenes_std.py written: 14 classes

