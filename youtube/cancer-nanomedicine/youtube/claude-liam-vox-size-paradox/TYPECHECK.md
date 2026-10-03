# TYPECHECK — claude-liam-vox-size-paradox

Date: 2026-08-28
Cut: vox-size-paradox-slate.mp4 (review, 225.9s @ 1280×720p24)

## Gates that fired at compile time

| Gate | Result |
|------|--------|
| CARD LINT (compile.py lint_card_fields) | PASS — 0 placeholder subs / 0 overlong labels across 13 FormBCard beats. |
| GATE CONTENT (runtime/qc/content_check.py) | PASS — 19 beats checked, no violations. |
| GATE FRAME (runtime/qc/frame_check.py) | PASS — canvas 3840×2160, 19 beats checked, no layout/contrast violations. |
| GATE LANE (runtime/qc/lane_check.py) | PASS — 0 lane violations, known_slates=[]. |
| PIPELINE-CARD RULE | PASS — 0 pipeline-owned slates (no INCOMPLETE flag). |
| GATE AUDIO | PASS — mean_volume −27.1 dB (≥ −40 dB gate). max_volume −5.9 dB. |
| SKIN LINT (lint_skin) | PASS — palette=claude · B00 = ClaudeComposerAsk · last beat BOUT = ClaudeTitleOutro. |
| MOTION HISTOGRAM | WARN — remotion carries 19/19 (100%) beats, over the ~40% pantry cap. Expected for a card-only slate cut; not a defect. |
| STALE-RENDER PURGE | Nothing to purge — root had no prior mp4s. |

## Build stamp (verbatim)

```
build.status Counter: {'VIDEO': 19}
metadata.build: {'at': '2026-08-28T02:19:39', 'cut': 'review',
                 'filled': 19, 'of': 19, 'slates': [],
                 'skin_warnings': []}
```

19/19 beats VIDEO. 0 slates. 0 skin warnings.

## Files

- `vox-size-paradox-slate.mp4` (6.5 MB · 225.9s · h264 · aac 48 kHz · 1280×720p24)
- `beat_sheet.json` mtime 02:19:39 · master mp4 mtime 02:19:54 · **freshness ✓** (cut newer than sheet by 15 s)
- Per-beat renders in `media/B00.mp4` … `media/BOUT.mp4` (19 files)
- Per-beat conformed clips in `clips/B00.mp4` … `clips/BOUT.mp4`
- Kokoro audio in `mp3/beat-B01.mp3` … `mp3/beat-BHTF.mp3` (17 files)
- QC contact sheet: `qc-sheet.png`
- Gate V frames: `_qc/frames/tick-001.png` … `tick-023.png` (every 10s)

## type_check.py note

`runtime/scripts/type_check.py` is the older gate the supervisor references.
On this workspace the equivalent hard gates run **inside `compile.py`** —
`lint_card_fields` (before ffmpeg), `content_check` (GATE CONTENT),
`frame_check` (GATE FRAME), `lane_check` (GATE LANE), `lint_skin`
(post-compile), plus PIPELINE-CARD RULE and GATE AUDIO. All ran green on
this reel (table above). No validator was loosened for this build.
