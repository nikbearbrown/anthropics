# CHECKS-REPORT.md — sleeper-agents-safety-training-fails-short
Generated: 2026-07-28T22:13:12.163495

## GATE BANNED-CARD
[banned-card] PASS — short

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in sleeper-agents-safety-training-fails-short:
  ✗ COLD-OPEN: first beat pattern='ClaudeComposerAsk916' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO subline 'Hubinger et al. (2024) · arXiv:2401.05566' is not empty — subline is opt-in per video; remove it or set to ""

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False