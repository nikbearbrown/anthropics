# CHECKS-REPORT.md — irreversible-action-gate
Generated: 2026-07-28T21:46:48.400466

## GATE BANNED-CARD
[banned-card] PASS — nbb-irreversible-action-gate

## GATE BOOKEND
[bookend] BLOCKED — 4 failure(s) in irreversible-action-gate:
  ✗ COLD-OPEN: first beat pattern='FormBCard' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO subline 'paste this' is not empty — subline is opt-in per video; remove it or set to ""

## compile: OK
## FormBCard beats: 2  boxes: 1
## checks_green: False