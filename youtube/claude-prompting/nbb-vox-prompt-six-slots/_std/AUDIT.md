# SHOW-DON'T-TELL AUDIT — nbb-vox-prompt-six-slots

**Run:** 2026-07-25 11:59
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | Dr. Osei's problem was that 'improve this' left all six slot | CARD/ClaudeComposerAsk | EXEMPT | — |
| B01 | She asked for an improved introduction. Claude improved it.  | CARD | EXEMPT | — |
| B02 | Dr. Osei is writing for a specialist review committee — expe | STILL | EXEMPT | — |
| B03 | She asked for an improved introduction. She got a polished r | CARD | TELLS | Manim: concept_card — She asked for an improved introduction |
| B04 | A prompt is a specification. It covers six slots: task, cont | GRAPHIC | TELLS | Manim: concept_card — A prompt is a specification. It covers |
| B05 | The guesses are plausible. Task: make it clearer. Context: g | GRAPHIC | TELLS | Manim: concept_card — The guesses are plausible. Task: make  |
| B06 | The slot that matters most: context. Dr. Osei's actual conte | GRAPHIC | TELLS | Manim: concept_card — The slot that matters most: context. D |
| B07 | The same input — the same raw text — produces two different  | GRAPHIC | TELLS | Manim: concept_card — The same input — the same raw text — p |
| B08 | Each slot you fill removes a generic guess. Fill all six and | CARD | TELLS | Manim: bar_chart — Each slot you fill removes a generic gues |
| B09 | Dr. Osei fills the slots: task — tighten the gap statement.  | GRAPHIC | TELLS | Manim: concept_card — Dr. Osei fills the slots: task — tight |
| B10 | The six slots apply to every request. Not just editing. Summ | GRAPHIC | TELLS | Manim: concept_card — The six slots apply to every request.  |
| B11 | Jamie asks Claude to analyze this dataset. No context, no co | GRAPHIC | TELLS | Manim: concept_card — Jamie asks Claude to analyze this data |
| B12 | Jamie fills the task slot: identify outliers, flag any value | GRAPHIC | TELLS | Manim: concept_card — Jamie fills the task slot: identify ou |
| B13 | Before you submit a vague request, spend thirty seconds on e | GRAPHIC | TELLS | Manim: concept_card — Before you submit a vague request, spe |
| B14 | A prompt is a specification covering six slots. Leave them e | CARD | TELLS | Manim: concept_card — A prompt is a specification covering s |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Why 'Improve This' Is a Wish, Not an Instruction | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 12
- Rebuilt (Manim rendered): 12
- Skipped (render failed): 0
- scenes_std.py written: 12 classes

