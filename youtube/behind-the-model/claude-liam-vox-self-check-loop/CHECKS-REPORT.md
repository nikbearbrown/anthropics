# CHECKS-REPORT.md — vox-self-check-loop
Generated: 2026-07-28T21:33:22.929498

## GATE BANNED-CARD
[banned-card] PASS — claude-liam-vox-self-check-loop

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in vox-self-check-loop:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 2
## checks_green: False