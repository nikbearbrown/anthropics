# BUILD-LOG — protein-level-loss
## Animate Protein-Level Loss with Claude Code
### @NikBearBrown · Reel 18 of 20

**Date:** 2026-07-20  
**Slug:** `protein-level-loss`  
**Folder:** `cancer-biology/youtube/claude-liam-protein-level-loss/`  
**Source plate:** `cancer-biology/illustrae/plates/18-protein-level-loss.svg` (p18())  

---

## Build steps

### 1. Directories created
```
mp3/ manim/ media/ pantry/ images/ mp4/
```

### 2. beat_sheet.json written
11 beats B00–B10. Slates: B01, B02, B08. Remotion beats: B00, B03, B06, B09, B10.

### 3. scenes.py written
- `B05_ProteinLevelLoss` — left-to-right production line: gene → mRNA (wavy arcs) → SKY protein circle → 3 VERM tag-dots snap on → VERM downward arrow → VERM funnel/shredder → dashed GRAY arrow → empty dashed slot.
- `B07_ProteinLevelLossFocus` — revised: tags Flash VERM after snapping on, protein animates toward funnel and FadeOut, empty slot pulses with Indicate ×3. Gene and mRNA stay bright throughout.
- `config.background_color = "#FFFFFF"` set at MODULE LEVEL.

### 4. Audio generation
`generate_audio_kokoro.py --no-gate` → 11 beats, am_onyx, $0.00, total ~242s

### 5. Art run
`ART_FACTS=0 bash brutalist-art/art run ...` → B05_ProteinLevelLoss + B07_ProteinLevelLossFocus rendered; Remotion B00/B03/B04/B06/B09/B10 rendered; compile complete.
- B01, B02, B08 → SLATE (needs human fill)
- Slow-mo warnings on B04 (4.8×) and B05 (3.5×) — Manim clips are short; logged in replace_log.md

### 6. Frame QC — B05 at t=2s
PASS — white background, GRAY gene rect with INK tick centre, BLUE wavy mRNA arcs (four half-circles), SKY protein circle. Production line reads left-to-right. Tag-dots and funnel appear later in animation as expected.

### Status: REVIEW CUT READY
- 8/11 filled (B01, B02, B08 → slate)
- No publish, no commit, no push
