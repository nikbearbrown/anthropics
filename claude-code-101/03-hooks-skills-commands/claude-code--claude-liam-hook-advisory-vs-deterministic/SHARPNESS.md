# SHARPNESS GATE — claude-liam-hook-advisory-vs-deterministic

Compiled master: `hook-advisory-vs-deterministic.mp4`
Median Laplacian variance: **333.6**
Failure threshold: 166.8 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 291.5 | 87% | PASS — 87% |
| B01 | 224.5 | 67% | PASS — 67% |
| B02 | 424.9 | 127% | PASS — 127% |
| B03 | 375.7 | 113% | PASS — 113% |
| B04 | 461.7 | 138% | PASS — 138% |
| B05 | 840.0 | 252% | PASS — 252% |
| B06 | 203.5 | 61% | PASS — 61% |
| BVDT | 223.4 | 67% | PASS — 67% |
| BHTF | 473.3 | 142% | PASS — 142% |
| BOUT | 158.3 | 47% | PASS — 47% |
