# SHOW-DON'T-TELL AUDIT — nbb-vox-handoff-conditions

**Run:** 2026-07-25 10:25
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | The syllabus link that passed 'looks good' and still broke i | CARD/ClaudeComposerAsk | EXEMPT | — |
| B01 | The teacher reviewed the new About page. It rendered. The na | CARD | TELLS | Manim: concept_card — The teacher reviewed the new About pag |
| B02 | The page existed. The link existed. It pointed to syllabus.h | GRAPHIC | TELLS | Manim: concept_card — The page existed. The link existed. It |
| B03 | Here is the question. Reviewing the output visually and veri | CARD | TELLS | Manim: two_column — Here is the question. Reviewing the outp |
| B04 | Looks good is a feeling, not a condition. A feeling can appr | GRAPHIC | TELLS | Manim: pipeline_flow — Looks good is a feeling, not a condit |
| B05 | The weak condition: looks good. It does not name the artifac | GRAPHIC | TELLS | Manim: concept_card — The weak condition: looks good. It doe |
| B06 | The condition that would have caught the syllabus-link bug:  | STILL | SHOWS | — |
| B07 | Here is where this compounds. The instinct when a handoff co | GRAPHIC | TELLS | Manim: pipeline_flow — Here is where this compounds. The ins |
| B08 | The structural fix is revert and respecify. When the handoff | GRAPHIC | TELLS | Manim: pipeline_flow — The structural fix is revert and resp |
| B09 | The practical move: before approving any Claude Code build s | GRAPHIC | TELLS | Manim: pipeline_flow — The practical move: before approving  |
| B10 | Exit zero is not a handoff condition. Looks good is not a ha | CARD | TELLS | Manim: pipeline_flow — Exit zero is not a handoff condition. |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Why 'Looks Good' Fails as a Gate and What to Write Instead | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 9
- Rebuilt (Manim rendered): 9
- Skipped (render failed): 0
- scenes_std.py written: 9 classes

