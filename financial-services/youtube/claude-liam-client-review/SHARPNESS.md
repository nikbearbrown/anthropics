# SHARPNESS GATE — claude-liam-client-review

Compiled master: `claude-liam-client-review.mp4`
Median Laplacian variance: **200.1**
Failure threshold: 100.0 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 340.8 | 170% | PASS — 170% |
| B01 | 130.4 | 65% | PASS — 65% |
| B02 | 187.9 | 94% | PASS — 94% |
| B03 | 200.1 | 100% | PASS — 100% |
| BVDT | 487.4 | 244% | PASS — 244% |
| BHTF | 458.6 | 229% | PASS — 229% |
| BOUT | 103.6 | 52% | PASS — 52% |
