# BUILD-LOG — claude-liam-p53-circuit
## "Animate the p53 Relay with Claude Code"
### Series: Animate Cancer Biology with Claude Code · Reel 01 of 20

---

## 2026-07-20 — Initial build

### Files created
- `beat_sheet.json` — 11-beat spine (B00–B10), Kokoro am_onyx, palette claude
- `scenes.py` — two Manim scenes: B05_P53Circuit, B07_P53CircuitBroken
- `BUILD-LOG.md` — this file
- Subdirectories: mp3/, manim/, media/, pantry/, images/, mp4/, clips/

### Beat spine
| Beat | Act | Source |
|------|-----|--------|
| B00  | INTRO (cold open) | ClaudeComposerAsk |
| B01  | PROBLEM 1 — what is being animated | slate |
| B02  | PROBLEM 2 — why it matters (~50% cancers) | slate |
| B03  | ASK (the real prompt) | ClaudeComposerAsk |
| B04  | CODE (B05_P53Circuit class) | ClaudeCodeBeat |
| B05  | OUTPUT — initial animation | Manim (B05_P53Circuit) |
| B06  | CHANGE — revision prompt | ClaudeComposerAsk |
| B07  | OUTPUT — stagger + collapse | Manim (B07_P53CircuitBroken) |
| B08  | SUMMARY | slate |
| B09  | NEXT STEPS | ClaudeComposerAsk ("Your turn.") |
| B10  | OUTRO | ClaudeTitleOutro @NikBearBrown |

### Steps to run
```bash
# From books/
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  cancer-biology/youtube/claude-liam-p53-circuit --no-gate

ART_FACTS=0 ART_QC=0 bash brutalist-art/art run cancer-biology/youtube/claude-liam-p53-circuit
```

### Geometry notes
- SVG canvas 1300×430, cx=[110,320,545,770,980,1175]
- Edge-gap-based placement: NODE_W=1.85, HUB_SCALE=1.25, _GAP=0.40
- Final XS (computed): centred ≈ [-6.3, -3.88, -1.21, 1.46, 3.88, 6.3] adjusted
- All edges within ±6.78 (frame half-width 7.11) — no clipping
- Hub node index 2 (BLUE=#0072B2), 25% larger, stroke_width=4.2

---

## 2026-07-20 — Build complete

### Rendered successfully
| Beat | Type | Duration | Status |
|------|------|----------|--------|
| B00 | Remotion ClaudeComposerAsk | 7.7s | VIDEO |
| B01 | Slate | 21.7s | SLATE (human fill) |
| B02 | Slate | 20.3s | SLATE (human fill) |
| B03 | Remotion ClaudeComposerAsk | 27.8s | VIDEO |
| B04 | Remotion ClaudeCodeBeat | 21.9s | VIDEO |
| B05 | Manim B05_P53Circuit | 17.5s | MANIM |
| B06 | Remotion ClaudeComposerAsk | 18.0s | VIDEO |
| B07 | Manim B07_P53CircuitBroken | 19.8s | MANIM |
| B08 | Slate | 23.1s | SLATE (human fill) |
| B09 | Remotion ClaudeComposerAsk | 29.5s | VIDEO |
| B10 | Remotion ClaudeTitleOutro | 5.0s | VIDEO |

### Slate cut
- `p53-circuit-slate.mp4` — 212.3s total
- 8/11 beats filled; 3 slates remain: B01, B02, B08

### QC frame results (verified by reading PNG)
- B05 final state: WHITE background, 6 nodes all in frame, hub (BLUE index 2)
  visibly larger with thicker stroke, Okabe-Ito colors correct, uniform gaps,
  no overlap, no clipping. PASS.
- B07 collapse state: WHITE background, VERM X-mark visible at hub centre,
  hub dimmed, downstream nodes at reduced opacity. Collapse signal readable. PASS.

### Issues fixed during build
1. `config.background_color` must be set at MODULE LEVEL not inside construct()
2. Hub overlap with neighbour nodes: switched from uniform-centre to edge-gap
   placement; NODE_W reduced 2.1→1.85 to fit all 6 nodes in frame
3. Rightmost node cropping: edge-gap formula ensures outer edges at ±6.78

### MISSING (human fill slots)
- B01: stat card — six node labels + relay arrow, p53 circled as hub
- B02: stat card — "TP53 mutated in ~50% of cancers" + broken chain visual
- B08: summary card — relay clock metaphor, four code blocks listed

### Kokoro audio
- 11 beats generated, voice am_onyx, cost $0.00 (free/local)
- Total actual duration: ~212s (~3m 32s)

---
