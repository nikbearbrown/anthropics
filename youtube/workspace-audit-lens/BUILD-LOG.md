# BUILD-LOG — workspace-audit-lens

## 2026-08-24 — HUMAN FEEDBACK (Bear, is-done review): "formatting and text issues"

Bear reviewed the slate cut (item 32/35 in the is-done pass) and flagged formatting
and text defects. Three frames identified, all Manim beats. Fixed this session:

### B09_ModelOrganisms — labels erased + circle overflow
- The token-highlight ring (`hl = node[0].copy()`) inherited the circle's OPAQUE
  GROUND fill and was drawn on top of the label → "Reward hacker", "Reward hacker +",
  "Hidden objective" had their middles painted out. Fix: `hl.set_fill(opacity=0)`.
- Labels were wider than the r=0.55 circles. Fix: labels moved BELOW their circles;
  arrows re-anchored to circle edges (`nodes[i][0]`), not node bounding boxes.

### B10_ProbeAUC — dial collided with note text and formula box
- The AUC dial arc was corner-positioned into the same region as "94,000 positions
  scored" and the formula box's right edge (box is ~5.4 units wide — nothing fits
  beside it). Fix: AUC title + note + dial stacked BELOW the formula box in the
  empty bottom half.

### B11_Validations — panel collision
- The right-aligned 11-column realism row (0.44 w / 0.22 buff) started at x≈-0.85
  and collided with suite 6 of the steering panel (ends x≈-1.0). Fix: 0.36 w /
  0.18 buff → row starts at x≈+0.45, clean gutter between panels.

### Pango space-collapse (systemic, this machine, Manim v0.20.1)
Single spaces at certain word boundaries rasterize at ZERO width, in BOTH EB
Garamond and Montserrat ("fingerprints in" → "fingerprintsin", "statistically
significant", "away from", "monotonic on", "tracks the / thing it / claims to").
Verified by controlled render test: NBSP also collapses; en-space and DOUBLE SPACE
render correctly (a double space rasterizes at normal single-space width).
Fix applied: doubled spaces at the verified-fused boundaries in B09/B10/B11
strings. NOTE for GATE T and other reels: this failure mode is invisible in
source and layout audits — it only shows in rendered frames.

### State after fixes
- B09/B10/B11 re-rendered (4K/24fps), installed to `manim/`, review cut recompiled
  via `art run`. Fixed frames verified by eye in the compiled cut.
- GATE V still FAILING on the PRE-EXISTING underfill defects (B02_85 3%, B04_85 17%,
  B05_85 40%, B10_85 43%, B11_50 6% + low-contrast, B11_85 28%) — the slow-fit
  sampling-artifact thread documented in SAVE-STATE.md, unchanged by this session.
  That investigation continues separately; per standing order, stopped at slate cut.
