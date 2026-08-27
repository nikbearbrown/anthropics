# SHARPNESS GATE — nbb-vox-agentic-loop

Compiled master: `vox-agentic-loop.mp4`
Median Laplacian variance: **244.4**
Failure threshold: 122.2 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 325.8 | 133% | PASS — 133% |
| NBB00 | 913.2 | 374% | PASS — 374% |
| B01 | 197.5 | 81% | PASS — 81% |
| B02 | 202.3 | 83% | PASS — 83% |
| B03 | 416.6 | 170% | PASS — 170% |
| B04 | 483.2 | 198% | PASS — 198% |
| B05 | 162.6 | 67% | PASS — 67% |
| B06 | 218.4 | 89% | PASS — 89% |
| B07 | 166.3 | 68% | PASS — 68% |
| B08 | 596.5 | 244% | PASS — 244% |
| B09 | 161.5 | 66% | PASS — 66% |
| B10 | 308.9 | 126% | PASS — 126% |
| B11 | 166.1 | 68% | PASS — 68% |
| B12 | 165.5 | 68% | PASS — 68% |
| NBB01 | 602.2 | 246% | PASS — 246% |
| NBB02 | 681.6 | 279% | PASS — 279% |
| NBB03 | 216.8 | 89% | PASS — 89% |
| BVDT | 0.0 | 0% | **FAIL** — 0% (below 50% floor and below abs floor 40) |
| BHTF | 540.3 | 221% | PASS — 221% |
| BOUT | 270.3 | 111% | PASS — 111% |
