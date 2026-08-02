# BUILD-LOG — claude-liam-clonal-evolution
## Animate Clonal Evolution with Claude Code · @NikBearBrown

**Date:** 2026-07-20  
**Plate source:** `cancer-biology/illustrae/plates_gen.py` p10()  
**Voice:** am_onyx (Kokoro, free)  
**Channel:** @NikBearBrown  

---

## Build steps

### Step 1 — Folder created
`cancer-biology/youtube/claude-liam-clonal-evolution/` with subdirs: mp3/ manim/ media/ pantry/ images/ mp4/

### Step 2 — beat_sheet.json written
11 beats B00–B10. Slates: B01, B02, B08. Remotion: B00, B03, B06, B09, B10. Manim: B05, B07. Code: B04.

### Step 3 — scenes.py written
- `B05_ClonalEvolution`: founder → tree branches (LaggedStart) → node circles → X-marks → selection arrow (GrowArrow) → sweep cluster (LaggedStart 8 BLUE circles)
- `B07_ClonalEvolutionSweep`: same tree, X-marks with Flash each, sweep flows one-at-a-time, cluster repacks, Flash on cluster

### Step 4 — Audio generation
11 beats generated, am_onyx, $0.00, total ~188s

### Step 5 — Art build
- B05_ClonalEvolution: MANIM OK (7.2s rendered, slowed 2.21x to 16.0s)
- B07_ClonalEvolutionSweep: MANIM OK (8.4s rendered, slowed 2.33x to 19.5s)
- Remotion beats: B00, B03, B04, B06, B09, B10 — all rendered
- Slates: B01, B02, B08
- Total filled: 8/11. Slate cut: clonal-evolution-slate.mp4 (187.8s)
- Gate A: B05 CLEAN, B07 WARN (coord at x=6.3 near safe boundary — acceptable)
- Gate W: both scenes CLEAN

### Step 6 — Frame QC
Frame at t=5s of B05.mp4 VERIFIED:
- White background: PASS
- Founder (GRAY circle) at left: PASS
- Tree branches: PASS
- 3 subclone types (hollow ORANGE, hatched GREEN, solid SKY): PASS
- VERM X-marks on dead ends: PASS
- VERM selection arrow: PASS
- Winning BLUE lineage forming: PASS
- QC: PASS
