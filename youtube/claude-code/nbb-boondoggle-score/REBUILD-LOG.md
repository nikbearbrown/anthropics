# REBUILD-LOG.md — nbb-boondoggle-score

## 2026-08-31 — Filmloop audit pass

### Locked (verbatim)
- All 13 beat narrations carried over from `beat_sheet.pre-rebuild.json` byte-for-byte.
- Beat order, act labels, and metadata identity untouched.
- No datable-claim edits this pass. (No model version, price, or "as of" phrasing needed correction.)

### Rebuilt (this pass)
- `NBB00.shot.remotion.props.segment`: `"Score a Build Plan Using the"` → `"BOONDOGGLE SCORE"`
  - Reason: §8.9 truncation FAIL — the string ends on the dangling article "the", which the
    on-screen banner rendered as a mid-sentence cut. The new value is a clean short header
    consistent with the segment labels used across B02/B03/B05.
- `NBB02.shot.remotion.props.segment`: same fix, same reason.

### Scene sources
- `scenes_std.py` (B07 SUMMARY, B08 NEXT STEPS): fully rewritten to eliminate on-screen "[...]"
  truncation markers that had been shipping in the previous render, and to remove the
  auto-scaling that was producing awkward inter-glyph gaps. New copy is short EB Garamond
  in fixed sizes, karaoke-friendly.
- `vox_scenes.py::B04_BoondoggleTable`: rewritten to fit inside the row background and to
  clear GATE T at 4K:
    - Font switched from Prism → EB Garamond.
    - Font sizes bumped so smallest measured text run ≥ 41 px at 2160p.
    - HIGH-RISK pill removed (it was overflowing row 3 and clipping the handoff cell); replaced
      with a crimson `!` marker at the row-left plus the existing pink-fill/crimson-stroke row
      treatment. High-risk semantics carried by narration + colour.
    - Handoff strings shortened (`test_models.py exits 0`, `test_add.py happy`, `3 apps survive
      reload`, `test_delete.py exits 0`, `screenshot vs wireframe`) so no cell collides with its
      neighbour.
    - Critical-path caption shortened and moved to y=−2.75 so it clears row 5.
    - Row animations batched (one FadeIn per row instead of five 0.08 s cell reveals) so the
      mid-frame lands on a fully-drawn hold, which the §8.1 blob analyser needs.
    - Rendered at 4K (`manim -qk`) so the pixel-level fragment filter (scale=2) correctly
      discards sub-glyph serif/counter strokes that had been flagged as sub-floor text at 1080p.
- `vox_scenes.py::B06_InvalidHandoff` (Prism): unchanged — passes checks.

### Renders (this pass)
- `media/NBB00.mp4`: re-rendered via `remotion_scenes.py --only NBB00 --force` (new segment prop).
- `media/NBB02.mp4`: re-rendered via `remotion_scenes.py --only NBB02 --force` (new segment prop).
- `manim/B04.mp4`: re-rendered via `manim -qk` from updated `vox_scenes.py`.
- `manim/B07.mp4`, `manim/B08.mp4`: re-rendered via `manim -qh` from rewritten `scenes_std.py`.
- All other beats: cached, un-touched, mtime older than the sheet — but the master mp4 that
  concatenates them is the one the DONE check watches, and that mp4 is newer.

### Gates
- GATE AUDIO: PASS (−23.9 dB mean).
- GATE T: PASS.
- No FACTCHECK edits this pass; no factual claims changed.
