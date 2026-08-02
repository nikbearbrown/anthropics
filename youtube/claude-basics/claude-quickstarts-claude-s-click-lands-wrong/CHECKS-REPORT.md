# CHECKS-REPORT.md — claude-quickstarts-claude-s-click-lands-wrong
Generated: 2026-07-28T23:04:24.988629

## GATE BANNED-CARD
[banned-card] PASS — claude-quickstarts-claude-s-click-lands-wrong

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-quickstarts-claude-s-click-lands-wrong:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 2
## checks_green: False