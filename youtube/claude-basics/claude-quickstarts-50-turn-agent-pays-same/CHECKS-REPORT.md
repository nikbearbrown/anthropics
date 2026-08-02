# CHECKS-REPORT.md — claude-quickstarts-50-turn-agent-pays-same
Generated: 2026-07-28T23:02:49.279609

## GATE BANNED-CARD
[banned-card] PASS — claude-quickstarts-50-turn-agent-pays-same

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-quickstarts-50-turn-agent-pays-same:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 2
## checks_green: False