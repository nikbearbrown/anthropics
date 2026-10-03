# psma-theranostic-loop · GATE V (post-compile QC)

## Master file

- `psma-theranostic-loop.mp4` — 3840×2160 4K, 24 fps, 204.7 s (3:24.70), stereo aac 48 kHz.
- `beat_sheet.json` mtime: 12:30. Master mtime: 12:31. **Cut is NEWER than the sheet.** ✓

## Gate AUDIO (compile.py built-in)

- master mean_volume = **-24.0 dB** (spec floor = -40 dB) — PASS
- master max_volume = -2.9 dB (no clipping)
- master audio duration = 3:24.72 — matches video within tail_silence

## Gate V — frames read

Extracted at 0.5 fps (every 2 s) into `_qc/frames/`. Spot-read:

| Frame | Beat  | What's on it                                           | Verdict |
|-------|-------|--------------------------------------------------------|---------|
| f001  | B00   | NBB terminal with `nikbearbrown` prompt + name         | CLEAN   |
| f005  | B01   | PSMA-617 · image it, treat it — three-item FormBCard   | CLEAN   |
| f020  | B03   | psma_theranostics.py NikBearBrownCodeBlock             | CLEAN   |
| f050  | B06   | Two pairs, one rule — PSMA / DOTATATE / Same loop      | CLEAN   |
| f070  | B08   | Is your tumor a theranostic candidate? — three checks  | CLEAN   |
| f080  | BVDT  | ClaudeVerdictArtifact page 1/2 — lines 1 & 2           | CLEAN   |
| f090  | BVDT  | ClaudeVerdictArtifact page 2/2 — lines 3 & 4           | CLEAN   |
| f100  | BOUT  | ClaudeTitleOutro w/ @NikBearBrown + mascot             | CLEAN   |

All read frames pass: no text overflow, no text/figure collision, exactly one terracotta accent
per frame (title heading star or accent stroke), safe inset respected, labels are short category
nouns (§5b Chart-text rule holds for the Manim B04 boxes: Ga-68 PSMA / SELECT / Lu-177 / ASSESS).

## Compile.py gates recorded

- `content-check` PASS — 13 beats, no violations
- `frame-check` PASS — 13 beats, canvas 3840×2160
- `lane-check` PASS — 13 beats, no lane violations
- `motion-check` INFO — remotion carries 7/13 beats (53%, over ~40% pantry cap). Advisory only,
  not a blocker: 7 of those 7 Remotion beats are canonical brand skins (NBB open/outro + 3 Claude
  bookends + 3 FormB/FormA cards for the body); trading them for another language would break
  the reel's own skin contract.

## Downgrades

None. Strict mode ran end-to-end; no gates were disabled.

## One recorded warning

- **B04 clip slowed 4.0×.** The Manim source (`B04_TheranosticLoop`) plays in 7.0 s and is
  stretched to fill the 27.7 s audio bed. On a review-slate cut this is acceptable; for a
  final-render pass the Manim scene needs `run_time=` per animation or a `self.wait(...)` chain
  matched to the beat's `actual_duration_s`. Logged to `replace_log.md` by compile.py.

## Verdict

Master mp4 built, audible (-24 dB), every slot filled by a real render (13/13 VIDEO/MANIM, zero
slate placeholders), sheet older than cut. GATE V passes.
