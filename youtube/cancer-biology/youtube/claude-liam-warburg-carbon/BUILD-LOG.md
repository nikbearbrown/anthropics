# BUILD-LOG — claude-liam-warburg-carbon

## 2026-07-20 — Initial build

**Reel:** Animate the Warburg Effect with Claude Code  
**Series:** Animate Cancer Biology with Claude Code — @NikBearBrown  
**Slug:** `warburg-carbon` (plate 03)  
**Scenes:** B05_WarburgCarbon, B07_WarburgCarbonFlow  

### Geometry source
`cancer-biology/illustrae/plates_gen.py` → `p03()`  
Hexagon (BLUE fill, ORANGE stroke) → two tracks: upper (VERM nodes → large ATP square), lower (GREEN nodes → building blocks + small ATP square + excreted circle)

### Build steps
- [x] Kokoro audio generated — 11 beats, $0.00, voice=af_heart
- [x] art run pipeline complete — B05+B07 Manim rendered, Remotion B00/B03/B04/B06/B09/B10 ok
- [x] B05 QC frame — PASS: white bg, BLUE hexagon left, VERM/ORANGE upper nodes+arrows, GREEN lower nodes. Geometry correct mid-animation.
- [x] B07 QC frame — PASS: white bg, same mid-animation state, geometry consistent. Flow particles and scale animation appear later in clip.
