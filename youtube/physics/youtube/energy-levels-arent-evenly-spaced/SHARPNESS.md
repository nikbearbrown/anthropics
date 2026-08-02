# SHARPNESS GATE — energy-levels-arent-evenly-spaced

Compiled master: `energy-levels-arent-evenly-spaced-slate.mp4`
Median Laplacian variance: **133.0**
Failure threshold: 66.5 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 402.8 | 303% | PASS — 303% |
| H01 | 426.9 | 321% | PASS — 321% |
| H02 | 433.1 | 326% | PASS — 326% |
| A01 | 433.1 | 326% | PASS — 326% |
| A02 | 139.9 | 105% | PASS — 105% |
| A03 | 191.3 | 144% | PASS — 144% |
| A04 | 38.3 | 29% | **FAIL** — 29% (below 50% floor and below abs floor 40) |
| A05 | 85.0 | 64% | PASS — 64% |
| A06 | 93.8 | 71% | PASS — 71% |
| A07 | 106.2 | 80% | PASS — 80% |
| A08 | 95.6 | 72% | PASS — 72% |
| BVDT | 126.0 | 95% | PASS — 95% |
| BHTF | 236.3 | 178% | PASS — 178% |
| BOUT | 117.8 | 89% | PASS — 89% |
