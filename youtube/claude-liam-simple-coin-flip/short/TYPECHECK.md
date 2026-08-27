# TYPECHECK.md — GATE T

Reel: `claude-liam-simple-coin-flip-short`  |  Checked: 2026-08-16T02:00  |  Overall: **FAIL**  |  Beats checked: 21  |  FAILs: 9

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| S01 | ? | light | min-size §8.1: min text-run height 230px >= floor 31px | PASS | — |
| S02 | ? | light | min-size §8.1: min text-run height 149px >= floor 31px | PASS | — |
| S03 | ? | light | overflow §8.2: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S04 | ? | light | min-size §8.1: min text-run height 72px >= floor 31px | PASS | — |
| S05 | ? | light | overflow §8.2: 4 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S06 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S07 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S08 | ? | light | overflow §8.2: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S09 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S10 | ? | light | overflow §8.2: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S11 | ? | light | overflow §8.2: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S12 | ? | light | overflow §8.2: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S13 | ? | light | overflow §8.2: 4 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S14 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S15 | ? | light | overflow §8.2: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| S16 | ? | light | overflow §8.2: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920 | **FAIL** | Move text inside title-safe 90% box |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 94px >= floor 31px | PASS | — |
| END | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

### S03 (?)
- **overflow §8.2**: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S05 (?)
- **overflow §8.2**: 4 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S08 (?)
- **overflow §8.2**: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S10 (?)
- **overflow §8.2**: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S11 (?)
- **overflow §8.2**: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S12 (?)
- **overflow §8.2**: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S13 (?)
- **overflow §8.2**: 4 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S15 (?)
- **overflow §8.2**: 1 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

### S16 (?)
- **overflow §8.2**: 3 text run(s) outside title-safe box (54,96)→(1026,1652) at 1080×1920
- **Fix:** Move text inside title-safe 90% box

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 19 | 0 |
| overflow §8.2 | 19 | 9 |
| contrast §8.3 | 19 | 0 |
| contrast-local §8.3b | 19 | 0 |
| bbox-overlap §8.6b | 19 | 0 |
| kerning §8.4 | 16 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
