# FACTCHECK — what-is-claude-youtube

## Beat-by-beat verification

**B01** — "Prompt in, finished film out, one arrow. That is not the pipeline."
- VERIFIED. Text-to-video models exist but do not produce finished educational explainer films from a single prompt. The brutalist-art pipeline (script → beats → audio → visuals → compile) is the actual production pipeline used in this codebase. Source: CLAUDE.md pipeline documentation; real-world AI video limitations.

**B02** — "Full pipeline with audio-master clock and two human gates. Human owns the argument."
- VERIFIED. The brutalist-art pipeline is audio-first (narration is the master clock) and has explicit human gate requirements before spending (Gate P) and at Manim approval. The five stages (Script, Beats, Audio, Visuals, QC) are accurate. Source: brutalist-art/AGENTS.md; run.sh QC gate implementation.

**B04** — "Two passes over one artifact: Build and Audit. Two exercises. Same artifact."
- VERIFIED. The build-then-audit pattern is the standard QC workflow: first compile (build), then QC gate (audit). This two-pass structure is implemented in run.sh and enforced by Gate V (final_frame_check). Source: brutalist-art/runtime/scripts/run.sh.

## Exclusions confirmed
- No claims about commercial AI video generation tools or their limitations by name
- Pipeline description matches actual codebase implementation

## VERDICT: PASS
