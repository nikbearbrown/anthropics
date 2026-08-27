# SHOTLIST — workspace-audit-lens

## Rhythm & Histogram
| Beat | Type | Source | Motion |
|---|---|---|---|
| B00 | REMOTION | own | ClaudeComposerAsk — composer types the ask |
| B01 | REMOTION | own | FormACard — title hold |
| B02 | MANIM | own | B02_HoneypotTimeline — annotated transcript timeline, lens readouts per stage |
| B03 | REMOTION | own | FormACard — Fig 35 readout table (3 lines); corpus PNG not found, fallback applied |
| B04 | MANIM | own | B04_EvalAwareness — dual-signal timeline: plot (terracotta) + eval-awareness (blue) |
| B05 | MANIM | own | B05_AblationDesign — 28 tokens deleted + 6×30 rollout grid |
| B06 | MANIM | own | B06_BlackmailNumbers — paired bars: verbalized eval-awareness + blackmail rate |
| B07 | MANIM | own | B07_EvidenceCard — SUPPORTED WITH CAVEATS tier badge + claim + caveat |
| B08 | MANIM | own | B08_PromptInjection — two-column: silent output vs workspace recognition |
| B09 | MANIM | own | B09_ModelOrganisms — four organism nodes, fingerprint tokens per type |
| B10 | MANIM | own | B10_ProbeAUC — score distributions + probe formula + AUC 0.853 dial |
| B11 | MANIM | own | B11_Validations — steering ±0.1 on 6 suites; realism edits on 11 suites |
| B12 | REMOTION | own | StepStream — output evals → workspace audits (active) → pre-deployment |
| B13 | REMOTION | own | ClaudeVerdictArtifact — five-line verdict |
| B14 | REMOTION | own | ClaudeComposerAsk — Your Turn prompt |
| B15 | REMOTION | own | ClaudeTitleOutro — title restate outro |

## Act Map
COLD OPEN: B00 | TITLE: B01 | ACT I (The Scenario): B02–B03 | ACT II (The Experiment): B04–B07 | ACT III (More Cases): B08–B09 | ACT IV (The Scale): B10–B12 | VERDICT: B13 | YOUR TURN: B14 | OUTRO: B15

## Manim scenes — all in scenes.py
B02_HoneypotTimeline · B04_EvalAwareness · B05_AblationDesign · B06_BlackmailNumbers
B07_EvidenceCard · B08_PromptInjection · B09_ModelOrganisms · B10_ProbeAUC · B11_Validations

Render one:
  cd anthropics/youtube/workspace-audit-lens && manim -qh --fps 24 -r 1920,1080 scenes.py B02_HoneypotTimeline

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py anthropics/youtube/workspace-audit-lens

## Archive still
B03: pantry-needed — extract transcript panel from corpus PNG for Fig 35
     Search: books/arxiv/transformer-circuits.pub/ for fig35 / honeypot / blackmail transcript table
     If not found: apply FormACard fallback (defined in beat_sheet.json B03.pantry_fallback)
     Credit when found: Anthropic Workspace Paper §5.1 / Fig 35 — reproduced for educational criticism.

## Open slots
B03 (SLATE) — human to supply Fig 35 pantry still OR approve FormACard fallback.
All other visuals are Manim or Remotion (no AI-gen video beats in this reel).
