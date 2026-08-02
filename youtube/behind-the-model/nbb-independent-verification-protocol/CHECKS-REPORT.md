# CHECKS-REPORT.md — independent-verification-protocol
Generated: 2026-07-28T21:46:04.317858

## GATE BANNED-CARD
[banned-card] PASS — nbb-independent-verification-protocol

## GATE BOOKEND
[bookend] BLOCKED — 4 failure(s) in independent-verification-protocol:
  ✗ COLD-OPEN: first beat pattern='FormBCard' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO subline 'then verify the artifact exists independently -- without asking the agent to con' is not empty — subline is opt-in per video; remove it or set to ""

## compile: OK
## FormBCard beats: 2  boxes: 2
## checks_green: False