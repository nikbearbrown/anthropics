# CHECKS-REPORT.md — claudeforfoundationmodels-same-api-key-shipped-prototype
Generated: 2026-07-28T23:05:24.887196

## GATE BANNED-CARD
[banned-card] PASS — claudeforfoundationmodels-same-api-key-shipped-prototype

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claudeforfoundationmodels-same-api-key-shipped-prototype:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 2
## checks_green: False