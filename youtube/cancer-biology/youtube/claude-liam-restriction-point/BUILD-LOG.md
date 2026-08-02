# BUILD-LOG — claude-liam-restriction-point

## 2026-07-20 — Initial build

**Reel:** Animate the Restriction Point with Claude Code  
**Series:** Animate Cancer Biology with Claude Code — @NikBearBrown  
**Slug:** `restriction-point` (plate 04)  
**Scenes:** B05_RestrictionPoint, B07_RestrictionPointFate  

### Geometry source
`cancer-biology/illustrae/plates_gen.py` → `p04()`  
Circle loop (GRAY, radius 2.8), VERM gate square at 210°, two BLUE cells at 234°/186° with radial outward arrows (GRAY).

### Static check
- B05_RestrictionPoint: PASS (4 distinct states / 11 beats)
- B07_RestrictionPointFate: PASS (5 distinct states / 11 beats)  
  Note: initial version used unsupported chained .animate methods; fixed to use FadeOut + separate plays.

### Build steps
- [x] Kokoro audio generated — 11 beats, $0.00, voice=af_heart
- [x] art run pipeline complete — B05+B07 Manim rendered, Remotion B00/B03/B04/B06/B09/B10 ok
- [x] B05 QC frame — PASS: white bg, GRAY loop circle, VERM gate square at ~210°, two BLUE cells on loop. Geometry correct. Radial arrows appear after second 2.
- [x] B07 QC frame — PASS: white bg, same layout confirmed. Fate animation (pre-gate exits, post-gate arrow fades) appears after second 2.
