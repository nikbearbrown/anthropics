# SHOW-DON'T-TELL AUDIT — claude-liam-map-the-agentic-loop

**Run:** 2026-07-25 10:39
**Brand:** claude-liam  **Palette:** #F2F0E9/#3D3929/#D97757

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| B00 | This is Liam, in for Bear. Nik Bear Brown. Build it with a C | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | Ask Claude to narrate its own loop on a real task. The loop  | GRAPHIC | TELLS | Manim: bar_chart — Ask Claude to narrate its own loop on a r |
| B02 | Ask Claude to label each stage before doing it -- and at Che | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The loop trace parser reads Claude's labeled output and flag | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | The labeled loop prints. Five stages visible. One Check stag | GRAPHIC | TELLS | Manim: pipeline_flow — The labeled loop prints. Five stages  |
| B05 | Now remove the loop-narration instruction and run the same t | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Default output: no stage labels. The Check stage is gone. Th | GRAPHIC | TELLS | Manim: pipeline_flow — Default output: no stage labels. The  |
| B07 | The loop happens whether you ask for it or not. Naming the s | GRAPHIC | TELLS | Manim: pipeline_flow — The loop happens whether you ask for  |
| B08 | On your next agentic task, require explicit stage labels at  | GRAPHIC | TELLS | Manim: pipeline_flow — On your next agentic task, require ex |
| B09 | Nik Bear Brown. Build it with a CLI. Then take it apart. At  | GRAPHIC/NikBearBrownOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

