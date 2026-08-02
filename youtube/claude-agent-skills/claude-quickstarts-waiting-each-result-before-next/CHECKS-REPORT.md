# CHECKS-REPORT.md — claude-quickstarts-waiting-each-result-before-next
Generated: 2026-07-28T22:39:08.538574

## GATE BANNED-CARD
[banned-card] PASS — claude-quickstarts-waiting-each-result-before-next

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-quickstarts-waiting-each-result-before-next:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 0
## checks_green: False