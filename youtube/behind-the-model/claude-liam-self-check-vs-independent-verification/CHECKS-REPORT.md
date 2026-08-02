# CHECKS-REPORT.md — self-check-vs-independent-verification
Generated: 2026-07-28T21:23:25.856717

## GATE BANNED-CARD
[banned-card] PASS — claude-liam-self-check-vs-independent-verification

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in self-check-vs-independent-verification:
  ✗ COLD-OPEN: first beat pattern='NikBearBrownOpen' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False