# SHARPNESS GATE — why-schrodingers-cat-is-not-about-cats

Compiled master: `why-schrodingers-cat-is-not-about-cats-slate.mp4`
Median Laplacian variance: **92.9**
Failure threshold: 46.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 402.3 | 433% | PASS — 433% |
| A00 | 426.4 | 459% | PASS — 459% |
| A01 | 431.8 | 465% | PASS — 465% |
| A02 | 431.8 | 465% | PASS — 465% |
| A03 | 102.3 | 110% | PASS — 110% |
| A04 | 73.4 | 79% | PASS — 79% |
| A05 | 39.6 | 43% | **FAIL** — 43% (below 50% floor and below abs floor 40) |
| A06 | 121.7 | 131% | PASS — 131% |
| A07 | 67.8 | 73% | PASS — 73% |
| A08 | 92.9 | 100% | PASS — 100% |
| A09 | 37.6 | 41% | **FAIL** — 41% (below 50% floor and below abs floor 40) |
| A10 | 90.3 | 97% | PASS — 97% |
| A11 | 55.5 | 60% | PASS — 60% |
| A12 | 80.3 | 86% | PASS — 86% |
| A13 | 143.3 | 154% | PASS — 154% |
| A14 | 127.3 | 137% | PASS — 137% |
| A15 | 78.0 | 84% | PASS — 84% |
| A16 | 82.9 | 89% | PASS — 89% |
| A17 | 117.7 | 127% | PASS — 127% |
| A18 | 71.5 | 77% | PASS — 77% |
| A19 | 63.4 | 68% | PASS — 68% |
| A20 | 137.4 | 148% | PASS — 148% |
| BVDT | 81.7 | 88% | PASS — 88% |
| BHTF | 98.2 | 106% | PASS — 106% |
| BOUT | 242.8 | 261% | PASS — 261% |
