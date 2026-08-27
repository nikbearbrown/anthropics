# SHARPNESS GATE — claude-liam-hook-development

Compiled master: `claude-liam-hook-development.mp4`
Median Laplacian variance: **581.2**
Failure threshold: 290.6 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 513.5 | 88% | PASS — 88% |
| B01 | 581.2 | 100% | PASS — 100% |
| B02 | 817.0 | 141% | PASS — 141% |
| B05 | 535.5 | 92% | PASS — 92% |
| BVDT | 994.7 | 171% | PASS — 171% |
| BHTF | 846.1 | 146% | PASS — 146% |
| BOUT | 92.8 | 16% | PASS — 16% |
