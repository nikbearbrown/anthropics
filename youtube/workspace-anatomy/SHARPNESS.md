# SHARPNESS GATE — workspace-anatomy

Compiled master: `workspace-anatomy.mp4`
Median Laplacian variance: **334.5**
Failure threshold: 167.3 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 621.8 | 186% | PASS — 186% |
| B01 | 101.9 | 30% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 629.5 | 188% | PASS — 188% |
| B03 | 219.8 | 66% | PASS — 66% |
| B04 | 212.8 | 64% | PASS — 64% |
| B05 | 417.0 | 125% | PASS — 125% |
| B06 | 224.7 | 67% | PASS — 67% |
| B07 | 342.3 | 102% | PASS — 102% |
| B08 | 473.9 | 142% | PASS — 142% |
| B09 | 334.5 | 100% | PASS — 100% |
| B10 | 274.0 | 82% | PASS — 82% |
| B11 | 264.4 | 79% | PASS — 79% |
| B12 | 493.7 | 148% | PASS — 148% |
| B13 | 622.9 | 186% | PASS — 186% |
| B14 | 79.7 | 24% | PASS — 24% |
