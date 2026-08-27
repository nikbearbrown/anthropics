# BUILD-LOG — mas-coordination

## 2026-08-16 — STILL scaling defect fixed (in compile.py, shared codepath)

### Symptom
Bear's screenshot showed B10 STILL at t=1:17 in `mas-coordination-slate.mp4`
displaying only a fragment of the source text (a few words filled the entire
3840x2160 frame). Same defect on B05, B06, B10, B16, B17, B21, B30.
Slate label also read `B10 STILL STILL` (duplicate word).

### Diagnosis (verified before fixing)
Read `brutalist-art/runtime/scripts/compile.py` at the STILL branch (was lines
272-300 pre-fix). The bug had two mechanical parts:

1. `vf = [vf_fit(w*2, h*2, fit)]` used the default `fit="crop"` from
   `metadata.fit`. `vf_fit` in `crop` mode returns
   `scale=W:H:force_original_aspect_ratio=increase,crop=W:H` — i.e. it
   scales the source until it FILLS the frame in the larger dimension and
   crops the excess in the other. For a widescreen 16:9 output and an image
   with a very different aspect ratio, this cropped huge portions BEFORE
   any zoompan even ran.

2. The `zoompan=z='1.10'` (or 1.08 kenburns cap) then zoomed further INTO
   that already-cropped surface, compounding the loss.

Confirmed with source image dimensions:
```
B05: 2000x1200   (5:3, matches 16:9 more closely) - light crop
B06: 2000x1200   (5:3)                            - light crop
B10: 3629x826    (4.39:1 wide banner!)            - severe H-crop (~40% visible)
B16: 1999x707    (2.83:1)                         - severe H-crop
B17: 1999x707    (2.83:1)                         - severe H-crop
B21: 2000x1120   (1.79:1, ~16:9)                  - minimal crop
B30: 3487x341    (10.2:1 ultra-wide banner!)      - catastrophic crop
```

Bear's hypothesis ("stills placed at native pixel scale, only ~20% shows")
was **directionally right, mechanism-wrong**: the compositor DID scale-to-fit,
but with `crop` fill mode, which cropped away the parts of the image that
didn't fit the output aspect. Native placement would have shown even less.

Label bug: at line 833 the review overlay wrote
`f"{bid} {stype} {status}"` where `stype` is `shot.type` (e.g. `"STILL"`) and
`status` is `resolve_slot`'s verdict (also `"STILL"` when a .png resolves).
Same word, twice.

### Fix (applied ONCE in compile.py shared code path)

**STILL FIT LAW** — the whole image must be visible at frame 1.

`brutalist-art/runtime/scripts/compile.py` STILL branch:
- Frame-1 canvas: `scale=W:H:force_original_aspect_ratio=decrease,pad=W:H:...:color=0xF3EBDD`
  (letterbox on the newsprint cream — same color used elsewhere in the tree).
- `hold` motion: fits whole image, holds.
- `pan` motion: modest 1.05x pan, no zoom, so pan motion has room.
- `kenburns` motion (default for STILL): gentle push capped at `Z_MAX = 1.15`
  toward `shot.focus` (defaults to center). Linear zoom over frames; visual
  ease-out is achieved by keeping delta small (0.15 total).

Label fix at review overlay: de-dupe when `stype` and `status` match; emit
`"STILL"` once. Now reads e.g. `B10 STILL 76.1s +4.7s`.

Change is in the SHARED code path — one edit affects every reel, not per-beat.

### Verification (frame-level)

Extracted frame 0 of each STILL beat and READ each PNG:

| Beat | Src dims | Frame 0 result |
|---|---|---|
| B05 | 2000x1200 | Whole cumulative-vulnerabilities chart visible, all 7 legend entries readable, axes labeled |
| B06 | 2000x1200 | Same chart with title "Vulnerabilities found vs. sampled tokens" fully visible |
| B10 | 3629x826  | Full text paragraph readable, all sentences visible |
| B16 | 1999x707  | Both side-by-side charts (Merged PR fraction + Code sharing) fully visible with all axis labels |
| B17 | 1999x707  | Both charts visible with Y-axis labels ("Fraction of PRs merged" / "Median agent code sharing") |
| B21 | 2000x1120 | 5-panel grid (Sonnet 4.6 / Opus 4.6 / Sonnet 5 / Opus 4.8 / Mythos Preview) all visible |
| B30 | 3487x341  | Full pull-quote visible with attribution "— agent 1, round 1" and surrounding narration |

Extracted last frame of B10 and B30: gentle 1.15x push, focal text still fully
readable, no crop of critical information.

Slate label verified at t=1:17: reads `B10 STILL 76.1s +4.7s` (correct).

### Autonomous decisions logged
- Chose `pad` (letterbox) over shrinking to a "safe zone" — pad honors the
  BRUTALIST cream ground (color 0xF3EBDD, same as `vf_fit`'s pad path) and
  preserves the whole image at frame 1 which is the primary requirement.
- Kept `hash-based direction randomness` (zin/ltr) so beats don't all move
  the same way.
- Cap of 1.15x picked as "gentle documentary push" per task spec.
- Did not touch `manim/media/video` code paths — they don't have this bug
  (their sources are already in output ratio).

### mas-coordination compile result (post-fix)
```
compile: 34/34 filled  323.0s runtime
STILL beats compiled: B05, B06, B10, B16, B17, B21, B30 (all with new fit law)
MOTION.md warning: static:20 kenburns:7 drawon:7 — static at 58% (>40% cap)
  This is because 20 beats are Remotion (static motion) — expected for a
  claude-audience explainer, not a media problem.
FRAME/CONTENT/LANE/AUDIO gates: all PASS
```
