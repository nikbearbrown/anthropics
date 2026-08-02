# BUILD-LOG — claude-liam-mir-deletion
## "Animate MicroRNA Deletion with Claude Code" · Reel 17 · @NikBearBrown

---

## 2026-07-20 — Initial build

**Reel:** 17 in the "Animate Cancer Biology with Claude Code" series  
**Slug:** `mir-deletion`  
**Folder:** `cancer-biology/youtube/claude-liam-mir-deletion/`  
**Voice:** `am_onyx` (Kokoro, free)  
**Palette:** claude  
**Register:** Teardown  

### Files written
- `beat_sheet.json` — 11 beats (B00–B10), spec-compliant
- `scenes.py` — `B05_MirDeletion` and `B07_MirDeletionSurge`

### Beat spine
| Beat | Type | Status |
|------|------|--------|
| B00 | ClaudeComposerAsk | greeting: "Zdravo, Liam" |
| B01 | null/SLATE | PROBLEM 1 — mechanism |
| B02 | null/SLATE | PROBLEM 2 — stakes (13q14 deletion, BCL-2 surge) |
| B03 | ClaudeComposerAsk | greeting: "The ask," |
| B04 | ClaudeCodeBeat | sparkLine: "Remove the clamp, nine times the output." |
| B05 | manim | B05_MirDeletion |
| B06 | ClaudeComposerAsk | greeting: "The change," |
| B07 | manim | B07_MirDeletionSurge |
| B08 | null/SLATE | SUMMARY |
| B09 | ClaudeComposerAsk | greeting: "Your turn." — BCL-2/apoptosis-momp handoff |
| B10 | ClaudeTitleOutro | handle: "@NikBearBrown" |

### Manim scenes
- `B05_MirDeletion`: Two-state stacked layout. Top state (y=+1.5): BLUE mRNA strand, GREEN hairpin arc, blocked arrow, 1 ORANGE dot. Dashed separator at y=0. Bottom state (y=-1.5): BLUE mRNA strand, VERM X-mark, full arrow, 9 ORANGE dots (3×3 grid). Sequential animation (Create→FadeIn→GrowArrow→LaggedStart).
- `B07_MirDeletionSurge`: Transition-based. Builds top state, then: hairpin FadeOut → VERM X-mark Flash → block FadeOut → free arrow → rapid LaggedStart dot surge (lag=0.06) → Wiggle cluster.

### Design notes
- `config.background_color = "#FFFFFF"` set at MODULE LEVEL (line 3)
- Both scenes use consistent Okabe-Ito colors: BLUE mRNA, GREEN hairpin, VERM X-mark, ORANGE dots, GRAY arrow/separator
- `class B05_MirDeletion` → renders to `manim/B05.mp4`
- `class B07_MirDeletionSurge` → renders to `manim/B07.mp4`
- Arc uses `radius=0.7, start_angle=0, angle=PI` centred at `[0.0, 1.5, 0]`
- 9 dots: 3×3 grid formula `[2.5 - 0.38 + (i%3)*0.38, y_base + (i//3)*0.38]`

---

## Audio generation log — 2026-07-21

`python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py cancer-biology/youtube/claude-liam-mir-deletion --no-gate`

| Beat | File | Duration |
|------|------|----------|
| B00 | beat-B00.mp3 | 7.55s |
| B01 | beat-B01.mp3 | 17.09s |
| B02 | beat-B02.mp3 | 21.76s |
| B03 | beat-B03.mp3 | 22.17s |
| B04 | beat-B04.mp3 | 37.03s |
| B05 | beat-B05.mp3 | 23.36s |
| B06 | beat-B06.mp3 | 19.37s |
| B07 | beat-B07.mp3 | 21.21s |
| B08 | beat-B08.mp3 | 11.29s |
| B09 | beat-B09.mp3 | 34.11s |
| B10 | beat-B10.mp3 | 5.16s |

Voice: am_onyx (Kokoro). Cost: $0.00.

---

## Compile log — 2026-07-21

`ART_FACTS=0 bash brutalist-art/art run cancer-biology/youtube/claude-liam-mir-deletion`

| Beat | Result | Duration |
|------|--------|----------|
| B00 | VIDEO (ClaudeComposerAsk) | 7.6s |
| B01 | SLATE | 17.1s |
| B02 | SLATE | 21.8s |
| B03 | VIDEO (ClaudeComposerAsk) | 22.2s |
| B04 | VIDEO (ClaudeCodeBeat) | 37.0s |
| B05 | MANIM (B05_MirDeletion) | 23.4s |
| B06 | VIDEO (ClaudeComposerAsk) | 19.4s |
| B07 | MANIM (B07_MirDeletionSurge) | 21.2s |
| B08 | SLATE | 11.3s |
| B09 | VIDEO (ClaudeComposerAsk) | 34.1s |
| B10 | VIDEO (ClaudeTitleOutro) | 5.2s |

8/11 filled. Slate cut: `mir-deletion-slate.mp4` (220.1s total).
Slates remaining: B01, B02, B08 (human fill slots — gen-AI clip → pantry).

---

## QC — 2026-07-21

Frame probe: `ffmpeg -ss 00:00:02 -vframes 1 -update 1 manim/B05.mp4 → /tmp/mir_b05.png`

**B05 at t=2s — PASS**
- White background: confirmed
- BLUE mRNA strand: present, thick, left-to-right
- GREEN hairpin arc: present, above midpoint of strand, arc open upward
- Gray downward arrow: present, right side
- Gray block bar: present, below arrow
- 1 ORANGE dot: present, below block bar
- Dashed separator: visible at bottom edge (drawing in progress at t=2s)
- Bottom state: not yet drawn (correct — animation sequential)

**B07 at t=3s — PASS**
- White background: confirmed
- BLUE mRNA strand: present
- VERM X-mark: present above mRNA strand (deletion event rendered, hairpin gone)
- Block bar + 1 dot still visible (surge fires after t=3s — correct sequencing)
- No artifacts, no clipping

**QC verdict: PASS**
