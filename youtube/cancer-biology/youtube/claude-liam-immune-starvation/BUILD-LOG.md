# BUILD-LOG — immune-starvation
## Animate Immune Starvation with Claude Code
### @NikBearBrown · cancer-biology · cli-explainer · 2026-07-20

---

## Source
- Plate: `cancer-biology/illustrae/plates/14-immune-starvation.svg`
- Plate function: `plates_gen.py :: p14()`
- Series: Animate Cancer Biology with Claude Code — Reel 14

## Geometry notes
- Reservoir: Rectangle, ORANGE outline, 5 dots near bottom (nearly empty)
- Thick left pipe: stroke_width=22, GRAY → tumor cluster (7 BLUE circles)
- Thin right pipe: stroke_width=5, GRAY → lone immune cell (SKY/VERM dashed)
- 3 ORANGE dots along left pipe (starvation asymmetry visible)
- Manim frame: ~14 wide × 8 tall; all elements within safe margins

## Build steps

### Step 1 — directories
- [x] mkdir cancer-biology/youtube/claude-liam-immune-starvation/{mp3,manim,media,pantry,images,mp4}

### Step 2 — beat_sheet.json
- [x] Written — 11 beats B00–B10

### Step 3 — scenes.py
- [x] Written — B05_ImmuneStarvation + B07_ImmuneStarvationContrast

### Step 4 — audio generation
- [x] 11 beats generated · am_onyx · $0.00 · ~194s total

### Step 5 — compile
- [x] ART_FACTS=0 bash brutalist-art/art run ... → 8/11 filled
- [x] B05:MANIM B07:MANIM rendered; B01,B02,B08 SLATE (expected)

### Step 6 — QC
- [x] Frame extracted: /tmp/immune-starvation_b05.png
- [x] PASS — white bg, ORANGE reservoir + 5 dots, thick GRAY pipe, 7 BLUE tumor circles, all in frame

---

## Issues
_none yet_
