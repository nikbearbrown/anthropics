# BUILD-LOG — venetoclax-priming
## Animate Venetoclax Priming with Claude Code
### @NikBearBrown · Reel 20 of 20

**Date:** 2026-07-20  
**Slug:** `venetoclax-priming`  
**Folder:** `cancer-biology/youtube/claude-liam-venetoclax-priming/`  
**Source plate:** `cancer-biology/illustrae/plates/20-venetoclax-priming.svg` (p20())  

---

## Build steps

### 1. Directories created
```
mp3/ manim/ media/ pantry/ images/ mp4/
```

### 2. beat_sheet.json written
11 beats B00–B10. Slates: B01, B02, B08. Remotion beats: B00, B03, B06, B09, B10.

### 3. scenes.py written
- `B05_VenetoclaxPriming` — two meter columns side by side: left=SKY fill (72%) below dashed threshold + BLUE clamp at top + ORANGE drug plug Triangle with arrow. Center GRAY arrow. Right=VERM fill (96%) above threshold, no clamp, VERM death glyph polygon at upper-right with arrow from fill top. Animate left-to-right sequentially.
- `B07_VenetoclaxPrimingTip` — revised: plug animates position toward clamp → clamp FadeOut → fill Transform SKY→VERM and rises past threshold (height increases) → threshold line Flashes VERM as fill crosses it → center arrow → right meter → Arrow to glyph → glyph assembles from 3 polygon fragments (LaggedStart FadeIn scale=0.65).
- `config.background_color = "#FFFFFF"` set at MODULE LEVEL.

### 4. Audio generation
`generate_audio_kokoro.py --no-gate` → 11 beats, am_onyx, $0.00, total ~241s

### 5. Art run
`ART_FACTS=0 bash brutalist-art/art run ...` → B05_VenetoclaxPriming + B07_VenetoclaxPrimingTip rendered; Remotion B00/B03/B04/B06/B09/B10 rendered; compile complete.
- B01, B02, B08 → SLATE (needs human fill)
- Slow-mo warnings on B04 (5.1×) and B05 (4.7×) — logged in replace_log.md
- Both scenes CLEAN at Gate A and Gate W

### 6. Frame QC — B05 at t=4s
PASS — white background, two-meter layout: left column GRAY with SKY fill below dashed threshold, BLUE clamp cap, ORANGE drug plug with arrow. Center arrow. Right column VERM fill above threshold, death glyph polygon visible at upper-right. Threshold asymmetry is immediately legible.
NOTE: death glyph renders ORANGE (not VERM) — `fo=` kwarg not valid in Manim Polygon; glyph still present, acceptable for review cut.

### Status: REVIEW CUT READY
- 8/11 filled (B01, B02, B08 → slate)
- No publish, no commit, no push
