# SHARPNESS GATE — claude-liam-simple-delve

Compiled master: `claude-liam-simple-delve.mp4`
Median Laplacian variance: **308.3**
Failure threshold: 154.1 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 32.7 | 11% | **FAIL** — 11% (below 50% floor and below abs floor 40) |
| S01 | 250.0 | 81% | PASS — 81% |
| S02 | 272.2 | 88% | PASS — 88% |
| S03 | 155.9 | 51% | PASS — 51% |
| S04 | 246.5 | 80% | PASS — 80% |
| S05 | 242.9 | 79% | PASS — 79% |
| S06 | 319.9 | 104% | PASS — 104% |
| S07 | 105.1 | 34% | PASS — 34% |
| S08 | 433.7 | 141% | PASS — 141% |
| S09 | 460.4 | 149% | PASS — 149% |
| S10 | 340.0 | 110% | PASS — 110% |
| S11 | 290.4 | 94% | PASS — 94% |
| S12 | 438.1 | 142% | PASS — 142% |
| S13 | 323.6 | 105% | PASS — 105% |
| S14 | 309.9 | 101% | PASS — 101% |
| S15 | 359.6 | 117% | PASS — 117% |
| S16 | 354.5 | 115% | PASS — 115% |
| BCRY | 306.6 | 99% | PASS — 99% |
| BHTF | 530.8 | 172% | PASS — 172% |
| BOUT | 132.2 | 43% | PASS — 43% |
