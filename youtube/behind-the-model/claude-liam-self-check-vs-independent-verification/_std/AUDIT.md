# SHOW-DON'T-TELL AUDIT — claude-liam-self-check-vs-independent-verification

**Run:** 2026-07-25 09:49
**Brand:** claude-liam  **Palette:** #F2F0E9/#3D3929/#D97757

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| B00 | This is Liam, in for Bear. Nik Bear Brown. Build it with a C | GRAPHIC/NikBearBrownOpen | EXEMPT | — |
| B01 | Ask Claude to check its own answer: it finds two of six erro | GRAPHIC | TELLS | Manim: bar_chart — Ask Claude to check its own answer: it fi |
| B02 | Ask Claude to produce a five-claim research summary with one | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The error comparison table builder outputs each claim with t | GRAPHIC/NikBearBrownCodeBlock | SHOWS | — |
| B04 | Self-check rates all five claims verified. The table shows n | GRAPHIC | TELLS | Manim: bar_chart — Self-check rates all five claims verified |
| B05 | Replace claim three's citation with a paper that does not su | GRAPHIC/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Self-check rates claim three verified with the wrong citatio | GRAPHIC | TELLS | Manim: bar_chart — Self-check rates claim three verified wit |
| B07 | Self-check improves output at the margins but cannot catch s | GRAPHIC | TELLS | Manim: bar_chart — Self-check improves output at the margins |
| B08 | For any consequential research output, open the cited source | GRAPHIC | TELLS | Manim: concept_card — For any consequential research output, |
| B09 | Nik Bear Brown. Build it with a CLI. Then take it apart. At  | GRAPHIC/NikBearBrownOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

