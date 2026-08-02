# BUILD-LOG — claude-liam-differentiation-block
## Animate Differentiation Block with Claude Code
### @NikBearBrown · Teardown register · Kokoro am_onyx

---

## 2026-07-20 — Initial build

**Plate source:** `cancer-biology/illustrae/plates_gen.py p09()`
**Template:** `claude-liam-p53-circuit/`

### Files written
- `beat_sheet.json` — 11 beats B00–B10
- `scenes.py` — B05_DifferentiationBlock + B07_DifferentiationBlockRelease
- `BUILD-LOG.md` — this file

### Audio generation
(pending)

### Compile
(pending)

### Manim scenes
- `B05_DifferentiationBlock` → `manim/B05.mp4`
  Two-panel staircase: left blocked (5 SKY step-nodes, GRAY arrows, VERM bar, 8 SKY pile-up circles, dim BLUE star), right released (5 steps, GREEN flow arrow, bright BLUE star)
- `B07_DifferentiationBlockRelease` → `manim/B07.mp4`
  Animated release: blocked state built → VERM bar FadeOut → pile circles migrate to top (LaggedStart) → GREEN flow arrow grows → star brightens to full opacity

### Slates (human fill)
- B01 — AML maturation staircase mechanism slate
- B02 — ATRA/APL statistics and "release not kill" slate
- B08 — summary card

### QC
- B05 frame at 3s: PASS — white background, left panel blocked staircase: SKY nodes on diagonal, GRAY arrows, VERM bar diagonal cut between steps 1-2, 8 SKY pile-up circles, dim BLUE star at top, all correct
- B07 rendered: 20.2s, animated release (bar FadeOut → pile migrates to top → GREEN arrow grows → star brightens), PASS
- Static check fix: `.set_stroke()` chained on `.animate` not valid in Manim — replaced with single `.set_fill()` call
- Slate cut: `differentiation-block-slate.mp4` (223.1s) — 8/11 filled (B01, B02, B08 are human slates)
