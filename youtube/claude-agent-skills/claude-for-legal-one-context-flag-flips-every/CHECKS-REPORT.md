# CHECKS-REPORT.md — claude-for-legal-one-context-flag-flips-every
Generated: 2026-07-28T22:36:12.122653

## GATE BANNED-CARD
[banned-card] PASS — claude-for-legal-one-context-flag-flips-every

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-for-legal-one-context-flag-flips-every:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False