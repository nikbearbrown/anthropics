# BUILD-PROMPT — claude-liam-vercel-mcp (ai-explainer)

Run from `books/` in Claude Code. Phase-gated; never publish.

1. **GATE (narration):** present beat_sheet.json to Bear + FACTCHECK.md.
   Note the deliberate strips (dates, CVE, spec version) — if Bear wants a
   dated "as of" cut for a short-shelf-life audience, that's a separate
   variant, not this evergreen one.
2. **Audio (free):** generate_audio_kokoro.py claude-cowork/youtube/claude-liam-vercel-mcp --no-gate
3. **Fill visuals.** Bookends (B00, B18, B19, B20) carry patterns+props —
   verify against each component's zod schema (standing rule #4). Inner beats
   are SLATES with graphic.production_viz intent; fill per ILLUSTRATE LAW:
   C2 patterns (divergence B04, scale B07, threshold B10), C3 illustrations
   (SourceFlow B02/B03 mirror pair, LayerStack B15), PredictCard (B08), and
   ClaudeCodeBeat for B15B's PreToolUse hook (real hook shape, exact).
4. **Render:** remotion_scenes.py (foreground). Slates stay slates on pass 1.
5. **Compile + QC:** art run → VISUAL QC LAW pass (frames READ, _qc/REPORT.md)
   → FILL-THE-CANVAS on every illustration beat. Iterate slate→filled →
   art final when Bear approves.

Length ≈ 5.8 min — upper edge for an ai-explainer, lower edge for a
deep-explainer; it earns it (single thesis, four facets). If Bear wants it
tighter to ~4 min, the merge candidates are B15/B15B/B16 (the hardening
layers compress into two beats) and B17 (the self-hoster aside, cuttable
whole for an account-access-only audience).
