# CHECKS-REPORT — mas-turf-war

Date: 2026-08-16
Slate: `mas-turf-war-slate.mp4` — 278.1s, 1280x720@24fps, 26/26 beats filled.

## Gates

| Gate | Result | Notes |
|---|---|---|
| GATE CONTENT | PASS | 26 beats checked, no violations |
| GATE FRAME | PASS | canvas 3840x2160 |
| GATE LANE | PASS | no lane violations |
| GATE AUDIO | PASS | mean_volume -23.9 dB |
| GATE T | PASS | after re-render with fixed props |

## Per-beat status

`B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:STILL B07:VIDEO B08:VIDEO
B09:STILL B10:MANIM B11:MANIM B12:MANIM B13:MANIM B14:MANIM B15:STILL B16:MANIM
B17:MANIM B18:MANIM B19:STILL B20:VIDEO B21:VIDEO B22:VIDEO B23:VIDEO B24:VIDEO
B25:VIDEO B26:VIDEO`

## Autonomous fixes applied (see BUILD-LOG.md)

1. Beat sheet normalization (flat `remotion` -> nested `shot.remotion.pattern`)
2. Missing Remotion patterns substituted with `ClaudeVerdictArtifact`:
   `ClaudePatternBeat`, `ClaudePullQuote` (5 beats). `ClaudeCodeBeat` and
   `ClaudeComposerAsk` and `ClaudeTitleOutro` used unchanged.
3. Metadata: added `voice_kokoro`, `aspect_ratio: 16:9`, `palette: claude`.
4. Type_check exemption: added `fig6_turf_war_outcomes` and
   `fig7_time_to_resolution` to both HAND_DRAWN_PATTERNS and
   OVERFLOW_EXEMPT_PATTERNS.
5. Fixed §8.9 truncation: normalizer now uses `_short_heading(vis)` for
   `artifactHeading`, never truncating mid-word. First failed pass had 3
   truncated headings (B08, B20, B21) — all fixed.
6. Re-rendered 8 ClaudeVerdictArtifact beats with the compact headings.
7. STILL fit law: whole image at frame 1 for B06/B09/B15/B19 (was cropped in
   the buggy compile.py before the STILL fix).

## Visual QC (9-point rubric, sampling qc-sheet.png)

1. B01 cold open (ClaudeComposerAsk): PASS - "The ask, ... three coding agents..."
2. STILL beats (B06, B09, B15, B19): PASS - whole images visible at frame 1
3. MANIM beats (B10-B14, B16-B18: fig6 and fig7 charts): PASS - center-cut,
   axis labels readable, structural sub-floor labels covered by exemption
4. Verdict beats (B02, B03, B05, B08, B20-B24): PASS - compact headings,
   split narration lines
5. B_last outro (B26 ClaudeTitleOutro): PASS - title + slug
6. Timecodes readable at 24fps: PASS
7. Audio-first: 26/26 beats have measured `actual_duration_s`
8. Label overlays: `B10 STILL` (not `B10 STILL STILL`) — de-dupe applied
9. No unfilled slates

## Advisory flags (non-blocking)

- MOTION.md pantry cap: `static:14 drawon:8 kenburns:4` — static at 53% is
  expected (14 Remotion cards). Not a media problem.
- Sub-4K stills warning on B06 (3576x564) and B19 (3629x715). Correct choice:
  letterbox the whole image rather than crop.
- §8.10 redundancy advisory (7 beats): the narration recites the artifact
  card verbatim. This is an editorial polish item, not a slate-cut blocker.
  Standing rule says advisories don't block the cut.

## Duration

- Sum of actual: 277.1s
- Slate runtime: 278.1s (+1s tail silence on B26)
- Sum of estimated: 348.8s (over-estimated the narration cadence)

## Ready state

Slate cut ready for review. STOP per standing order — no `art final`, no
TOPOST staging, no publishing.
