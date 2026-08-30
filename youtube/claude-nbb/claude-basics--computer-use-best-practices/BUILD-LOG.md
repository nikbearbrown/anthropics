# BUILD-LOG — claude-basics--computer-use-best-practices (nbb-rebrand, assemble_nbb.py)

**DONE** — 2026-08-30T02:03:36

Built via assemble_nbb.py, golden.json frozen 2026-08-29.

## Lint results
- [PASS] scene_registry (ids + roles): scene_registry_lint.py
- [PASS] props deep-equal golden (except text fields): []
- [PASS] ask-beat final frame contains full question: 7/7 key words found, "?" present=True
- [PASS] OCR chip check (old chip absent, new chip present): []
- [PASS] 16:9 outro carries its mascot (OUTRO-LOCK.md): 2/3 sampled frames (within BOUT's own window) show the mascot body color
- [PASS] body beats byte-identical to source: []
- [PASS] duration = source - cut outro/writer + new beats, within 0.5s: expected~122.32s actual=122.33s (source 114.60s)
- [PASS] source reel SHA-256 unchanged: 8642773b30e21c49f9ecd985945bb5352fabbfb5fb5ecdaa3d03cc4a0dd51398
- [PASS] audio presence (mean_volume > -40dB): mean_volume: -24.0
