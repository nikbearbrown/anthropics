# CHECKS-REPORT.md — launch-your-agent-autonomous-agent-freeze-mid-run
Generated: 2026-07-28T22:52:10.872806

## GATE BANNED-CARD
[banned-card] PASS — launch-your-agent-autonomous-agent-freeze-mid-run

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in launch-your-agent-autonomous-agent-freeze-mid-run:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False