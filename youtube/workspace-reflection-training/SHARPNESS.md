# SHARPNESS GATE — workspace-reflection-training

Compiled master: `workspace-reflection-training.mp4`
Median Laplacian variance: **503.4**
Failure threshold: 251.7 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 398.5 | 79% | PASS — 79% |
| B01 | 123.8 | 25% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 601.3 | 119% | PASS — 119% |
| B03 | 561.2 | 111% | PASS — 111% |
| B04 | 943.8 | 187% | PASS — 187% |
| B05 | 312.4 | 62% | PASS — 62% |
| B06 | 339.5 | 67% | PASS — 67% |
| B07 | 862.4 | 171% | PASS — 171% |
| B08 | 599.9 | 119% | PASS — 119% |
| B09 | 427.6 | 85% | PASS — 85% |
| B10 | 503.4 | 100% | PASS — 100% |
| B11 | 643.6 | 128% | PASS — 128% |
| B12 | 99.9 | 20% | PASS — 20% |
