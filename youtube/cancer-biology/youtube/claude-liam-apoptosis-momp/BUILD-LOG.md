# BUILD-LOG — claude-liam-apoptosis-momp
## Animate the Apoptosis Switch with Claude Code
### @NikBearBrown · Teardown register · Kokoro am_onyx

---

## 2026-07-20 — Initial build

**Plate source:** `cancer-biology/illustrae/plates_gen.py p06()`
**Template:** `claude-liam-p53-circuit/`

### Files written
- `beat_sheet.json` — 11 beats B00–B10
- `scenes.py` — B05_ApoptosisMomp + B07_ApoptosisMompGated
- `BUILD-LOG.md` — this file

### Audio generation
(pending — run `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py cancer-biology/youtube/claude-liam-apoptosis-momp`)

### Compile
(pending — run `ART_FACTS=0 ./brutalist-art/art run cancer-biology/youtube/claude-liam-apoptosis-momp`)

### Manim scenes
- `B05_ApoptosisMomp` → `manim/B05.mp4`
  Three stages: balance beam tipped (2 SKY vs 3 VERM), mitochondrion capsule leaks 5 ORANGE dots, 7-spoke wheel assembles
- `B07_ApoptosisMompGated` → `manim/B07.mp4`
  Revision: beam starts balanced (2v2), 3rd VERM causes Rotate tipping, dots escape on ArcBetweenPoints paths, each spoke Flashes on Create

### Slates (human fill)
- B01 — three-stage mechanism slate
- B02 — Bcl-2 / venetoclax stakes slate
- B08 — summary card

### QC
- B05 frame at 2s: PASS — white background, balance beam tilted right, 2 SKY + 3 VERM tokens visible, fulcrum triangle correct
- B07 rendered: 21.3s, 21 animations, PASS
- Slate cut: `apoptosis-momp-slate.mp4` (204.4s) — 8/11 filled (B01, B02, B08 are human slates)
