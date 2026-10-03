# BUILD-PROMPT.md — claude-liam-the-missing-feedback-loop

Paste-ready. Run from `books/` in a local Claude Code session. The reel was
authored + fact-checked + audio-locked on 2026-08-30/31; this prompt rebuilds
or continues it.

---

```
Build the deep-explainer reel at
anthropics/youtube/claude-liam-the-missing-feedback-loop/.

READ FIRST:
  brutalist-art/skills/make/deep-explainer/SKILL.md
  brutalist-art/skills/make/ai-explainer/SKILL.md
  the reel's SOURCES.md, FACTCHECK.md, BUILD-LOG.md, SHOPPING.md

LOCKED: beat_sheet.json (29 beats: B00, B01–B25, BVDT, BHTF, BOUT),
narration, act structure, lane mix, FACTCHECK verdicts. mp3/ holds all 29
measured Kokoro am_onyx files — REUSE them; mp3/words.json is the word clock.

CHANNEL claude-liam. FREE build — no ElevenLabs, no Higgsfield, no paid calls.
The reel NEVER requests generated media: the five vox beats (B04 B09 B13 B18
B23) take human pantry stills per SHOPPING.md, render as slates until then,
and each carries a GRAPHIC/own fallback — convert, never slate, if a still
can't be cleared.

STEP 1 — Manim (9): render manim/scenes.py classes B02 B03 B08 B10 B14 B15
  B17 B21 B25 at 1080p24 into manim/<BID>.mp4. LAYOUT LAW binds (no hardcoded
  move_to; check_overlaps at end of every construct, including every label).
  PANGO CHECK: read rendered frames for fused words (this Mac drops some
  single spaces); fix by doubling the space at the fused boundary.

STEP 2 — Remotion (15): ONLY via
    python3 brutalist-art/runtime/scripts/remotion_scenes.py \
        anthropics/youtube/claude-liam-the-missing-feedback-loop
  Foreground, --concurrency=1. Patterns: ClaudeComposerAsk (B00 BHTF) ·
  ClaudeSegmentCard (B01 B06 B12 B20) · DeckPattern (B05 threshold, B16
  divergence) · ClaudeCodeBeat (B07) · ChipGrid (B11 B19 B22) ·
  ClaudeC2FullStatement (B24) · ClaudeVerdictArtifact (BVDT, FIVE lines —
  verify no overflow in the frame) · ClaudeTitleOutro (BOUT). Props already
  match each component's zod schema — do not freehand new fields.

STEP 3 — Gate D1 previz:
  ./brutalist-art/art run anthropics/youtube/claude-liam-the-missing-feedback-loop
  Vox slots render as slates; everything else real; audio real. Verify with
  ffprobe: 48000 Hz AAC (96 kHz = the old loudnorm bug — stop). ~6:45.

STEP 4 — gates, with eyes: GATE T type_check → TYPECHECK.md zero FAIL.
  VISUAL QC: every beat at 15/50/85%, READ the PNGs — hunting text-on-text
  and fused words specifically. Audio tail check: BVDT/BHTF/BOUT all narrated.

STEP 5 — STOP. Hand the previz + SHOPPING.md to Bear. Pantry fill and
  `art final` happen after his review. DO NOT PUBLISH; do not touch
  books/youtube/TOPOST/.

Log in BUILD-LOG.md, human feedback first. REPORT: runtime, lane histogram
as built, TYPECHECK status, QC summary, SHOPPING items outstanding.
```
