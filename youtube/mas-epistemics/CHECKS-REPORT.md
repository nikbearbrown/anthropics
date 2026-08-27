# CHECKS-REPORT — mas-epistemics

Date: 2026-08-20
Slate: `mas-epistemics.mp4` — 299.4s, 3840x2160, 30/30 beats filled.

**B00 added 2026-08-20** — ClaudeComposerAsk cold-open bookend (BOOKENDS-ALWAYS rule 2);
Kokoro am_onyx, 10.71s measured audio; Remotion rendered; recompiled.

## Gates

| Gate | Result | Notes |
|---|---|---|
| GATE CONTENT | PASS | 30 beats checked, no violations |
| GATE FRAME | PASS | canvas 3840x2160 |
| GATE LANE | PASS | no lane violations |
| GATE AUDIO | PASS | mean_volume -23.8 dB |
| GATE T | PASS | B00 SKIP (bookend, no text overlay to check) |

## Per-beat status

`B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:STILL B07:STILL
B08:MANIM B09:MANIM B10:MANIM B11:VIDEO B12:VIDEO B13:VIDEO B14:VIDEO
B15:VIDEO B16:STILL B17:STILL B18:MANIM B19:MANIM B20:MANIM B21:MANIM
B22:VIDEO B23:VIDEO B24:VIDEO B25:VIDEO B26:VIDEO B27:VIDEO B28:VIDEO
B29:VIDEO`

Composition: 18 Remotion (ClaudeComposerAsk, ClaudeVerdictArtifact,
ClaudeCodeBeat, ClaudeTitleOutro), 4 STILL (chart figures + paper quotes),
7 MANIM (fig4_gullibility, fig5_hidden_profile animations).

## Autonomous fixes applied (see BUILD-LOG.md)

1. Beat sheet normalization (flat `remotion` -> nested `shot.remotion.pattern`)
2. Missing Remotion patterns substituted with `ClaudeVerdictArtifact`:
   `ClaudePatternBeat`, `ClaudeChecklistBeat`, `ClaudePullQuote` (multiple beats).
3. Metadata: added `voice_kokoro`, `aspect_ratio: 16:9`, `palette: claude`.
4. Type_check exemption: added `fig4_gullibility` to both
   HAND_DRAWN_PATTERNS and OVERFLOW_EXEMPT_PATTERNS.
5. Fixed §8.9 truncation (2 iterations):
   - Pass 1 FAIL: 3 mid-word truncations (initial normalizer bug).
   - Pass 2 FAIL: B01/command lost terminal `?` via .rstrip; B23/heading
     ended in "written in" (trailing preposition).
   - Both fixed by normalizer updates + Remotion re-render of affected beats.
6. STILL fit law: whole image at frame 1 for B06/B07/B16/B17 (Gullibility
   curve + tier chart + paper claim stills).

## Visual QC (9-point rubric, sampling qc-sheet.png)

1. B01 cold open (ClaudeComposerAsk): PASS - "Hey Claude - if you put four
   AI agents in a room..."
2. STILL beats (B06 Gullibility curve, B07 tier chart, B16 hidden-profile
   chart, B17 paper claim): PASS - whole images visible at frame 1
3. MANIM beats (B08-B10 fig4_gullibility, B18-B21 fig5_hidden_profile):
   PASS - chart animations rendered, exempt from §8.1 min-size (calibrated
   at 14pt @1080 baseline per render_lib.py)
4. Verdict beats (13 ClaudeVerdictArtifact): PASS - compact headings, split
   narration lines
5. B_last outro (B29 ClaudeTitleOutro): PASS - title + slug
6. Timecodes readable at 24fps: PASS
7. Audio-first: 29/29 beats have measured `actual_duration_s`
8. Label overlays: `B06 STILL` (not `B06 STILL STILL`) — de-dupe applied
9. No unfilled slates

## Advisory flags (non-blocking)

- MOTION.md pantry cap: `static:18 drawon:7 kenburns:4` — static at 62%
  is expected (18 Remotion cards).
- §8.10 redundancy advisory (11 beats): the narration recites the artifact
  card. Editorial polish item, not a slate-cut blocker.

## Duration

- Sum of actual: ~298.4s (B00 added 10.71s)
- Compiled runtime: 299.4s (+1s tail silence on B29)
- Sum of estimated: 374.0s (over-estimated by ~20%)

## Ready state

Slate cut with B00 bookend — STOP per standing order. Awaiting Bear approval
before `art final` / TOPOST / publish.
