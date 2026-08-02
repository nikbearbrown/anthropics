# SHARPNESS GATE — one-atom-farther-cuts-current-tenfold

Compiled master: `one-atom-farther-cuts-current-tenfold-slate.mp4`
Median Laplacian variance: **101.0**
Failure threshold: 50.5 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 386.4 | 382% | PASS — 382% |
| H01 | 410.4 | 406% | PASS — 406% |
| H02 | 416.8 | 412% | PASS — 412% |
| A01 | 416.8 | 412% | PASS — 412% |
| A02 | 38.0 | 38% | **FAIL** — 38% (below 50% floor and below abs floor 40) |
| A03 | 103.8 | 103% | PASS — 103% |
| A04 | 57.6 | 57% | PASS — 57% |
| A05 | 84.1 | 83% | PASS — 83% |
| A06 | 72.1 | 71% | PASS — 71% |
| A07 | 98.3 | 97% | PASS — 97% |
| A08 | 98.7 | 98% | PASS — 98% |
| BVDT | 91.9 | 91% | PASS — 91% |
| BHTF | 124.8 | 124% | PASS — 124% |
| BOUT | 103.4 | 102% | PASS — 102% |
