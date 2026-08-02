# CHECKS-REPORT.md — vox-silent-omission
Generated: 2026-07-28T21:34:27.118317

## GATE BANNED-CARD
[banned-card] PASS — claude-liam-vox-silent-omission

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in vox-silent-omission:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 3
## checks_green: False