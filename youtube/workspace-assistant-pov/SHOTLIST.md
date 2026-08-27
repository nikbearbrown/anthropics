# SHOTLIST — workspace-assistant-pov (E05)

Typed work order. Remotion beats render via `remotion_scenes.py`. Manim beats render via `manim -qh scenes.py <ClassName>`. No AI-generated video or still assets in this reel (all evidence is text + data visuals).

| Beat | Act | Visual type | Component / scene | Render status | Notes |
|---|---|---|---|---|---|
| B00 | cold-open | REMOTION | ClaudeComposerAsk | SLATE | greeting="The ask," — composer types the question |
| B01 | title | REMOTION | FormACard | SLATE | Two lines: title + series label |
| B02 | evidence-safety | MANIM | B02_TylenolSplit | SLATE | Split: 1000mg safe / 8000mg unsafe; arrow at "is" token |
| B03 | evidence-base | MANIM | B03_BaseVsPost | SLATE | Base model readout — pain/now/feeling; no TERRA |
| B04 | evidence-generalize | MANIM | B04_ReactionBattery | SLATE | Empathy (n=9) + danger (n=10) battery bar chart |
| B05 | evidence-roleplay | MANIM | B05_RoleplayDisclaimer | SLATE | Roleplay workspace: disclaimer + fictional in top-8 (TERRA); base model panel below shows nothing |
| B06 | pivot | REMOTION | DeckPattern | SLATE | divergence pattern — "What it says" vs "What it holds" |
| B07 | experiment-pref-setup | MANIM | B07_PreferenceSetup | SLATE | ⚠ VERIFY: pull Fig 45 preference-question text before final render |
| B08 | experiment-pref-drama | REMOTION | BrutalistHesitantWriter | SLATE | banner="DRAMATIZATION"; seed="e05-b08-but-v1"; "But" → terracotta → deleted → "And" |
| B09 | experiment-pref-data | MANIM | B09_InternalBUT | SLATE | BUT at rank 1 (TERRA) on dispreferred prefill; correction terms (INK) on factual-error control |
| B10 | experiment-suppress-setup | MANIM | B10_SuppressionDesign | SLATE | 2×2 compliance bars (base/post × think/don't-think); ~.97/.97/.97/.93 |
| B11 | experiment-suppress-drama | REMOTION | BrutalistHesitantWriter | SLATE | banner="DRAMATIZATION"; seed="e05-b11-damn-v1"; "Bears"→"boat" catch; "Damn." types slowly |
| B12 | experiment-suppress-data | MANIM | B12_SuppressionData | SLATE | ⚠ VERIFY: transcribe Fig 46 Panel B fractions before final render; placeholder bars in scene |
| B13 | evidence-label | REMOTION | ChipGrid | SLATE | 4 chips (n=9–10; single-token lens; one model family; control holds); 2-col |
| B14 | verdict | REMOTION | ClaudeVerdictArtifact | SLATE | 5 verdict lines; lines type in during narration |
| B15 | your-turn | REMOTION | ClaudeComposerAsk | SLATE | greeting="Your turn." — don't-think prompt |
| B16 | outro | REMOTION | ClaudeTitleOutro | SLATE | title restate; tail_silence_s 1.0 |

## Open items before final render

1. **B07** — Pull the exact preference-question example from Fig 45 of the source paper (`books/arxiv/transformer-circuits.pub/`). Update `scenes.py:B07_PreferenceSetup` placeholder text and remove the ⚠ VERIFY banner from the scene.
2. **B12** — Transcribe exact bar heights from Fig 46 Panel B (concept/fail/'damn' presence fraction, all four conditions). Update `scenes.py:B12_SuppressionData` fractions (currently placeholder 0.78/0.42/0.74/0.26).

## Asset inventory

All visuals are generated locally — no Higgsfield, no pantry stills, no external media. 

- MANIM scenes (8): B02 B03 B04 B05 B07 B09 B10 B12 — render with `manim -qk scenes.py BearsDoodlesVideo` or individually
- REMOTION scenes (9): B00 B01 B06 B08 B11 B13 B14 B15 B16 — render via `runtime/scripts/remotion_scenes.py`
- Audio: Kokoro `am_onyx` via `generate_audio_kokoro.py` — free, no gate required
