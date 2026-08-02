# SHOW-DON'T-TELL AUDIT — vox-context-priority-weight

**Run:** 2026-07-25 12:04
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| B01 | She pasted six documents — all about the same project. Claud | CARD | EXEMPT | — |
| B02 | Keiko is a marketing manager. She pastes a 15-page brand gui | STILL | EXEMPT | — |
| B03 | The output follows the brand guide. It is predominantly blue | CARD | TELLS | Manim: concept_card — The output follows the brand guide. It |
| B04 | Without source labels, Claude treats all pasted documents as | GRAPHIC | TELLS | Manim: concept_card — Without source labels, Claude treats a |
| B05 | The brand guide is 15 pages — long and formally structured.  | GRAPHIC | TELLS | Manim: concept_card — The brand guide is 15 pages — long and |
| B06 | The brief's constraint — nothing blue — gets proportional we | GRAPHIC | TELLS | Manim: concept_card — The brief's constraint — nothing blue  |
| B07 | Adding more unlabeled documents makes this worse, not better | CARD | TELLS | Manim: concept_card — Adding more unlabeled documents makes  |
| B08 | The fix is label and prune. Label each source before it appe | GRAPHIC | TELLS | Manim: concept_card — The fix is label and prune. Label each |
| B09 | With labels, Keiko assigns the priority order she actually i | GRAPHIC | TELLS | Manim: concept_card — With labels, Keiko assigns the priorit |
| B10 | This applies to any multi-document paste. Meeting notes plus | GRAPHIC | TELLS | Manim: concept_card — This applies to any multi-document pas |
| B11 | A school administrator pastes a 20-page district handbook, a | GRAPHIC | TELLS | Manim: concept_card — A school administrator pastes a 20-pag |
| B12 | She adds two labels: handbook — background. Principal email  | GRAPHIC | TELLS | Manim: concept_card — She adds two labels: handbook — backgr |
| B13 | Before pasting multiple documents: label each one. Use three | GRAPHIC | TELLS | Manim: layer_stack — Before pasting multiple documents: labe |
| B14 | More unlabeled context gives Claude more to weight incorrect | CARD | TELLS | Manim: concept_card — More unlabeled context gives Claude mo |


## Rebuild Results

- TELLS found: 12
- Rebuilt (Manim rendered): 12
- Skipped (render failed): 0
- scenes_std.py written: 12 classes

