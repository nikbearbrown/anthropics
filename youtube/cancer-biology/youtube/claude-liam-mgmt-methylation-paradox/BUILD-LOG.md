# BUILD-LOG — mgmt-methylation-paradox
## Animate the MGMT Methylation Paradox with Claude Code
### @NikBearBrown · Reel 19 of 20

**Date:** 2026-07-20  
**Slug:** `mgmt-methylation-paradox`  
**Folder:** `cancer-biology/youtube/claude-liam-mgmt-methylation-paradox/`  
**Source plate:** `cancer-biology/illustrae/plates/19-mgmt-methylation-paradox.svg` (p19())  

---

## Build steps

### 1. Directories created
```
mp3/ manim/ media/ pantry/ images/ mp4/
```

### 2. beat_sheet.json written
11 beats B00–B10. Slates: B01, B02, B08. Remotion beats: B00, B03, B06, B09, B10.

### 3. scenes.py written
- `B05_MgmtMethylation` — lesion strand + VERM diamond → fork (two thin lines) → upper track: GRAY strands + GREEN enzyme arc moves, diamond FadeOut (repaired) → SKY intact cell. Lower track simultaneously: BLUE promoter rect + 4 lollipop methylation marks → GRAY strand with VERM diamond persisting → VERM break mark → ORANGE dead cell polygon.
- `B07_MgmtMethylationFork` — revised: lesion Flash VERM at open; enzyme animates position sweep along upper strand; lollipop stems grow from dots upward (LaggedStart GrowFromPoint); lower diamond pulses (Indicate ×2); dead cell assembles from 3 triangle fragments (LaggedStart FadeIn).
- `config.background_color = "#FFFFFF"` set at MODULE LEVEL.

### 4. Audio generation
`generate_audio_kokoro.py --no-gate` → 11 beats, am_onyx, $0.00, total ~254s

### 5. Art run
`ART_FACTS=0 bash brutalist-art/art run ...` → B05_MgmtMethylation + B07_MgmtMethylationFork rendered; Remotion B00/B03/B04/B06/B09/B10 rendered; compile complete.
- B01, B02, B08 → SLATE (needs human fill)
- Slow-mo warning on B04 (4.6×) — logged in replace_log.md
- Gate A warnings on both scenes (not errors) — pipeline continued

### 6. Frame QC — B05 at t=3s
PASS — white background, GRAY strand left with fork diverging up/down. Upper track: GREEN enzyme arc (pac-arc C-shape). Lower track: BLUE promoter rect + 4 BLUE lollipop dots + ORANGE/VERM diamond lesion. Fork structure reads cleanly. Upper and lower tracks both visible at mid-animation.

### Status: REVIEW CUT READY
- 8/11 filled (B01, B02, B08 → slate)
- No publish, no commit, no push
