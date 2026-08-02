# SHOW-DON'T-TELL AUDIT — nbb-receipt-extraction-pipeline

**Run:** 2026-07-25 10:54
**Brand:** claude-liam  **Palette:** #FFFFFF/#2A1A0E/#C8102E

| Beat | Narration (gist) | Visual now | Classification | Planned fix |
|---|---|---|---|---|
| NBB00 | The side-by-side sold me: the no-schema pass raised zero exc | CARD/ClaudeComposerAsk | EXEMPT | — |
| B00 | Without a schema, you're not extracting data — you're hoping | SLATE | EXEMPT | — |
| B01 | Receipt extraction without a schema produces output — but fi | SLATE | TELLS | Manim: concept_card — Receipt extraction without a schema pr |
| B02 | Extract from this receipt: vendor as string, date in ISO 860 | SLATE/NikBearBrownTerminalAsk | SHOWS | — |
| B03 | The extraction script runs two passes: no-schema then schema | SLATE/NikBearBrownCodeBlock | SHOWS | — |
| B04 | 5 receipts processed. No-schema: 3 date format inconsistenci | SLATE | TELLS | Manim: bar_chart — 5 receipts processed. No-schema: 3 date f |
| B05 | Add exception rule: if total is over 500 dollars, flag for h | SLATE/NikBearBrownTerminalAsk | SHOWS | — |
| B06 | Two receipts above the 500-dollar threshold: both get high_v | SLATE | TELLS | Manim: two_column — Two receipts above the 500-dollar thresh |
| B07 | The schema is an interface contract for extraction. Without  | SLATE | TELLS | Manim: concept_card — The schema is an interface contract fo |
| B08 | Next: audit your workspace permissions — which access does e | SLATE | TELLS | Manim: concept_card — Next: audit your workspace permissions |
| B09 | Nik Bear Brown. Brutalist and Educational AI. nikbearbrown.c | SLATE/NikBearBrownOutro | EXEMPT | — |
| NBB01 | Let's recap with Claude. Here's what the body just demonstra | CARD/ClaudeVerdictArtifact | EXEMPT | — |
| NBB02 | Take this prompt, run it on your own — pick any cancer type  | CARD/ClaudeComposerAsk | EXEMPT | — |
| NBB03 | Receipt Extraction Pipeline: Schema-First vs. No-Schema | CARD/ClaudeTitleOutro | EXEMPT | — |


## Rebuild Results

- TELLS found: 5
- Rebuilt (Manim rendered): 5
- Skipped (render failed): 0
- scenes_std.py written: 5 classes

