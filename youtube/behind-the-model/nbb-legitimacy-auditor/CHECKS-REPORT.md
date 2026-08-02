# CHECKS-REPORT.md — legitimacy-auditor
Generated: 2026-07-28T21:47:47.983226

## GATE BANNED-CARD
[banned-card] PASS — nbb-legitimacy-auditor

## GATE BOOKEND
[bookend] BLOCKED — 4 failure(s) in legitimacy-auditor:
  ✗ COLD-OPEN: first beat pattern='FormBCard' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO subline 'it is whether anyone would know' is not empty — subline is opt-in per video; remove it or set to ""

## compile: OK
## FormBCard beats: 2  boxes: 2
## checks_green: False