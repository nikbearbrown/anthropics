# PROMPTS — workspace-assistant-pov (E05)

No open AI-generation slots. Every beat in this reel is built from local sources:
- **Manim** (8 beats: B02 B03 B04 B05 B07 B09 B10 B12) — data diagrams from paper figures
- **Remotion** (9 beats: B00 B01 B06 B08 B11 B13 B14 B15 B16) — reel-local components

No pantry stills, no Higgsfield images or video, no external media required.

## Pre-render verification items (not prompts — data lookups)

**B07 — Fig 45 example question**
Action: Read the source paper (`books/arxiv/transformer-circuits.pub/`) and copy the exact preference question shown in Fig 45. Update `scenes.py:B07_PreferenceSetup` — replace placeholder text, remove ⚠ VERIFY banner.

**B12 — Fig 46 Panel B bar fractions**
Action: Transcribe the exact bar heights (fraction of trials) from Fig 46 Panel B for all four conditions (base-think / base-don't-think / post-think / post-don't-think). Update `scenes.py:B12_SuppressionData` placeholder values (0.78 / 0.42 / 0.74 / 0.26).
