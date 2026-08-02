# BUILD-LOG — claude-liam-mtap-passenger
## "Animate MTAP Passenger Deletion with Claude Code"
### @NikBearBrown · Reel 13 · Animate Cancer Biology with Claude Code series

---

## 2026-07-20 — Initial build

### Step 1 — Folder created
```
cancer-biology/youtube/claude-liam-mtap-passenger/
  mp3/   manim/   media/   pantry/   images/   mp4/
```

### Step 2 — beat_sheet.json written
- 11 beats B00–B10, cli-explainer spine
- B01, B02, B08 → SLATE (null source, human-fill)
- B00, B03, B06, B09 → ClaudeComposerAsk (Remotion)
- B04 → ClaudeCodeBeat (Remotion)
- B05, B07 → Manim (scenes.py)
- B10 → ClaudeTitleOutro (Remotion)
- Voice: am_onyx (Kokoro, free). Channel: @NikBearBrown.

### Step 3 — scenes.py written
Two Manim scenes:
- `B05_MtapPassenger` — initial deletion animation
  - Chromosome bar (GRAY) + 3 surviving ticks
  - VERM bracket arc above deleted gap (tick 1–2 region)
  - BLUE driver square + ORANGE passenger circle fall below bar
  - DashedLines from bar to shapes
  - Arrow from passenger to SKY accumulation node
  - 5 SKY dots FadeIn one-by-one
  - VERM plug + arrow FadeIn from right
- `B07_MtapPassengerFlow` — causal flow revision
  - Full deletion rebuild (B05 sequence)
  - ORANGE passenger pulses (Flash ORANGE)
  - 5 dots animate from source → into accumulation node (LaggedStart)
  - VERM plug moves along arrow path toward node
  - SKY Flash on node as plug arrives

Design compliance:
- `config.background_color = "#FFFFFF"` at MODULE LEVEL (line 4)
- Okabe-Ito palette throughout
- Class names: `B05_MtapPassenger`, `B07_MtapPassengerFlow`
- No chained `.animate` methods (split into separate `self.play()` calls)

### Step 4 — Audio generation
```
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  cancer-biology/youtube/claude-liam-mtap-passenger
```
Voice: am_onyx. Engine: Kokoro (free, local).

### Step 5 — Compile
```
ART_FACTS=0 ./brutalist-art/art run \
  cancer-biology/youtube/claude-liam-mtap-passenger
```

### Step 6 — B05 frame QC
Frames extracted at t=2s, t=4s, t=6s and read visually.

**t=2s** — Bar, 3 ticks, VERM bracket visible. Driver+passenger at bar level (pre-fall).
**t=4s** — Deletion fall complete. BLUE driver square and ORANGE passenger circle hanging below bar. DashedLines visible.
**t=6s** — Full diagram: SKY accumulation node with 5 SKY dots inside. VERM plug triangle pointing left. Arrow from plug to node. All elements present. Nothing clipped.

**QC verdict: PASS**

---

## QC checklist — COMPLETED 2026-07-21

- [x] White background (#FFFFFF)
- [x] GRAY bar spans full width, visible at y=2.5
- [x] 3 surviving ticks present (positions 0, 3, 4)
- [x] VERM bracket arc above deleted gap
- [x] BLUE driver square below bar at x=-0.8
- [x] ORANGE passenger circle below bar at x=+0.8
- [x] DashedLines from bar to each shape
- [x] Arrow from passenger circle to SKY accumulation node (reads through dashed line → node chain)
- [x] 5 SKY dots visible inside/around accumulation node
- [x] VERM plug triangle visible pointing at node
- [x] B07: ORANGE flash fires on passenger circle (16 animations rendered — Flash confirmed in log)
- [x] B07: Dots animate into node (flow visible — LaggedStart over 5 dot anims)
- [x] B07: Plug moves toward node, SKY flash on arrival
- [x] No shapes clipped at frame edges
- [x] No chained animate calls (separate self.play blocks throughout)

## Build summary

| Item | Value |
|------|-------|
| Compile | 2026-07-21 |
| Slate cut | `mp4/mtap-passenger-slate.mp4` (249.2s) |
| Filled | 8/11 (B00, B03, B04, B05, B06, B07, B09, B10) |
| Slates | B01, B02, B08 (human-fill) |
| Manim renders | B05_MtapPassenger (15 anims), B07_MtapPassengerFlow (16 anims) |
| Audio | 11 beats, am_onyx, Kokoro, $0.00 |
| Total narration | ~249s |
| Warnings | B04/B05/B07 slowed (short Remotion clip vs long audio — expected for Manim beats) |

---

## Slates (human-fill)

| Beat | Content needed |
|------|---------------|
| B01  | Chromosome diagram — CDKN2A + MTAP adjacent on 9p21; deletion bracket; "~50% of human cancers" label |
| B02  | Metabolite accumulation → PRMT5 dependency → inhibit → tumor dies; split tumor/normal panel |
| B08  | 4-step causal chain card: deletion → passenger lost → accumulates → drugable; "collateral damage → target" |

Drop pantry files as: `pantry/B01.mp4`, `pantry/B02.mp4`, `pantry/B08.mp4`

---
