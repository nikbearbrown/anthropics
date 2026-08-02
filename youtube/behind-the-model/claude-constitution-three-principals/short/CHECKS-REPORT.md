# CHECKS-REPORT.md — claude-constitution-three-principals-short
Generated: 2026-07-28T21:16:56.297870

## GATE BANNED-CARD
[banned-card] PASS — short

## GATE BOOKEND
[bookend] BLOCKED — 4 failure(s) in claude-constitution-three-principals-short:
  ✗ COLD-OPEN: first beat pattern='ClaudeComposerAsk916' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO handle is empty — must be '@NikBearBrown'

## compile: OK
## FormBCard beats: 1  boxes: 3
## checks_green: False