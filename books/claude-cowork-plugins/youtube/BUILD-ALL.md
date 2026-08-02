# BUILD-ALL — render the whole *Claude Cowork Plugins* deep-explainer series

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives),
typically under `claude --dangerously-skip-permissions`. It renders all 14 reels in
chapter order, honoring every gate. Each reel also has its own `BUILD-PROMPT.md` if
you'd rather do them one at a time.

---

```
Build the deep-explainer series in
books/anthropics/books/claude-cowork-plugins/youtube/, in chapter order.

The batch order (chapter order) is:
  1 claude-liam-what-plugins-are
  2 claude-liam-installing-plugins
  3 claude-liam-productivity
  4 claude-liam-marketing
  5 claude-liam-sales
  6 claude-liam-research
  7 claude-liam-data
  8 claude-liam-enterprise-search
  9 claude-liam-product
  10 claude-liam-support
  11 claude-liam-legal-finance
  12 claude-liam-building-plugins
  13 claude-liam-combining-plugins
  14 claude-liam-troubleshooting

Read the series README.md and the book-level FACTCHECK.md first. Then, for EACH reel:

1. SCHEMA RECONCILE. Conform beat_sheet.json to runtime/schema/beat_sheet.schema.json
   exactly (field names, scene keys, shot/vox_run/handoff). Do not change content,
   lanes, narration, or act order.
2. LANE-MIX LINT. Confirm the histogram (VOX 20–25 / MANIM 25–40 / REMOTION 30–45 /
   CARD remainder). The authored sheets already land in band; if reconcile shifts a
   beat, re-balance rather than pad.
3. GATE P — present the full narration on an animated slate for sign-off before ANY
   audio. Channel claude-liam: Kokoro am_onyx, free. No ElevenLabs anywhere in the batch.
4. AUDIO LOCK — generate_audio.py (Kokoro/am_onyx); per-beat mp3 durations become the
   clock; align writes the word clock; faster-whisper captions.
5. SHOPPING LIST (Gate D2, after audio lock) — pantry_search.py per vox beat against
   svg/svg/images/; copy real matches pre-checked; write each reel's SHOPPING.md from
   the LOCKED durations. Every vox still in this series is Tier 1 illustrative (no real
   people, no rights escalation).
6. GATE D1 PREVIZ — ./brutalist-art/art run <reel> (slates in vox slots, Manim/Remotion
   real, --review burn-in). Review pacing; source the stills.
7. PANTRY FILL → REVIEW CUT — drop stills into pantry/, re-run (only changed slots
   recompile); set shot.focus per still.
8. VISUAL QC LAW — frame-level pass per CLAUDE-CODE-VISUAL-QC-CHECK.md; read the PNGs;
   fix root causes in scene source; re-render to zero BLOCKER/MAJOR; log _qc/REPORT.md.
9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH.

Honor every parent law throughout: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE,
ASK→RESULT, REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed),
OUTRO, VISUAL QC, IN-FOR-BEAR, GATE P. Retint deck patterns to the claude stage
(cream #F2F0E9, ink #3D3929, accent #D97757) and log retints. Never hardcode plugin
counts, prices, or platform lists on screen or in narration.

Batch discipline: rotate the B00 world-language hello (already set per reel — don't
repeat within the batch), and don't re-render a reel that already passed final unless
its beat sheet changed.
```

---

**Reminder:** the render toolkit (`brutalist-art/`, Remotion, Manim, Kokoro) is not in
the authoring sandbox where these packages were written — run this on your toolkit machine.
