# SHARPNESS GATE — claude-liam-synthesis-vs-deciding

Compiled master: `synthesis-vs-deciding.mp4`
Median Laplacian variance: **406.9**
Failure threshold: 203.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 353.0 | 87% | PASS — 87% |
| B01 | 881.6 | 217% | PASS — 217% |
| B02 | 460.8 | 113% | PASS — 113% |
| B03 | 471.1 | 116% | PASS — 116% |
| B04 | 523.7 | 129% | PASS — 129% |
| B05 | 295.7 | 73% | PASS — 73% |
| B06 | 313.9 | 77% | PASS — 77% |
| BVDT | 262.3 | 64% | PASS — 64% |
| BHTF | 1010.5 | 248% | PASS — 248% |
| BOUT | 215.7 | 53% | PASS — 53% |
