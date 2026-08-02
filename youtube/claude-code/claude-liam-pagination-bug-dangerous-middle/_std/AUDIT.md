# SHOW-DON'T-TELL AUDIT — claude-liam-pagination-bug-dangerous-middle

**Run:** 2026-07-25 10:03
**Brand:** claude-liam  **Palette:** #F2F0E9/#3D3929/#D97757

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| B01 | This is Liam, in for Bear. Seth writes a pagination function | — | EXEMPT | — |
| B02 | Every test Seth wrote passed. The function compiled. The cod | — | TELLS | Manim: concept_card — Every test Seth wrote passed. The func |
| B03 | The function itself is fine. The calling loop used a termina | — | TELLS | Manim: cycle_diagram — The function itself is fine. The call |
| B04 | The bug lives in exactly one place on the number line: any i | — | TELLS | Manim: concept_card — The bug lives in exactly one place on  |
| B05 | The failure was not in the function. The function was fine.  | — | TELLS | Manim: pipeline_flow — The failure was not in the function.  |
| B06 | A handoff condition is a falsifiable claim, written before t | — | TELLS | Manim: pipeline_flow — A handoff condition is a falsifiable  |
| B07 | The handoff condition lives in the prompt, before Claude run | — | TELLS | Manim: bar_chart — The handoff condition lives in the prompt |
| B08 | Priya builds a paginated leaderboard for her school's quiz a | — | TELLS | Manim: pipeline_flow — Priya builds a paginated leaderboard  |
| B09 | Before you ship any paginated output — or any function with  | — | TELLS | Manim: pipeline_flow — Before you ship any paginated output  |
| B10 | The dangerous middle is not the easy bug that fails on first | — | TELLS | Manim: pipeline_flow — The dangerous middle is not the easy  |


## Rebuild Results

- TELLS found: 9
- Rebuilt (Manim rendered): 9
- Skipped (render failed): 0
- scenes_std.py written: 9 classes

