# SHARPNESS GATE — workspace-jacobian-lens

Compiled master: `workspace-jacobian-lens-slate.mp4`
Median Laplacian variance: **485.5**
Failure threshold: 242.7 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 682.9 | 141% | PASS — 141% |
| B01 | 166.9 | 34% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 365.2 | 75% | PASS — 75% |
| B03 | 508.4 | 105% | PASS — 105% |
| B04 | 552.8 | 114% | PASS — 114% |
| B05 | 485.5 | 100% | PASS — 100% |
| B06 | 987.3 | 203% | PASS — 203% |
| B07 | 216.6 | 45% | PASS — 45% |
| B08 | 340.8 | 70% | PASS — 70% |
| B09 | 320.3 | 66% | PASS — 66% |
| B10 | 142.1 | 29% | PASS — 29% |
| B11 | 345.1 | 71% | PASS — 71% |
| B12 | 654.3 | 135% | PASS — 135% |
| B13 | 565.0 | 116% | PASS — 116% |
| B14 | 559.7 | 115% | PASS — 115% |
| BHTF | 679.9 | 140% | PASS — 140% |
| BOUT | 149.9 | 31% | PASS — 31% |
