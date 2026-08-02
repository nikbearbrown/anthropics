# BUILD-PROMPT — claude-liam-vercel-refactor (ai-explainer)

Run from `books/` in Claude Code. Phase-gated; never publish.

1. **GATE (narration):** present `beat_sheet.json` narration to Bear beat by
   beat if he hasn't signed off in-session already. No audio before approval.
2. **Audio (free):** `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py
   claude-cowork/youtube/claude-liam-vercel-refactor --no-gate` — then confirm
   per-beat durations look sane (B00 ~20s, act cards ~8s).
3. **Fill visuals.** Bookends (B00, B20, B21, B22) already carry
   `shot.remotion.pattern` + props — verify against each component's zod
   schema (standing rule #4) before rendering. Inner beats are SLATES with
   `graphic.production_viz` intent: fill each per ILLUSTRATE LAW using the
   C2 pattern library / C3 illustrations (`Illu-LayerStack`, `Illu-SourceFlow`,
   `Illu-ChipGrid`, `Illu-PredictCard`) retinted to the claude stage, and
   ClaudeCodeBeat for B11's four-command gate (REAL commands, exact order).
   Read each component's schema first; props keys must match exactly.
4. **Render:** `python3 brutalist-art/runtime/scripts/remotion_scenes.py
   claude-cowork/youtube/claude-liam-vercel-refactor` (foreground). Slates
   stay slates on the first compile — the previz IS the deliverable of pass 1.
5. **Compile + QC:** `./brutalist-art/art run claude-cowork/youtube/claude-liam-vercel-refactor`,
   then the VISUAL QC LAW pass (sample frames, LOOK, `_qc/REPORT.md`).
   FILL-THE-CANVAS check on every illustration beat.
6. Iterate slate→filled per beat; `./brutalist-art/art final` when Bear
   approves the review cut.

Notes: narration ≈ 6 min — if Bear wants the standard 3–4 min ai-explainer,
the trim candidates are B09 (scoping), B14 (checks), and B19 (bypass), which
compress into neighbors without losing the spine. SOURCES.md logs which
claims were re-verified; do not add numbers to narration that aren't there.
