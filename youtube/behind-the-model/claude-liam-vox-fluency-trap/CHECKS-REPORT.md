# CHECKS-REPORT.md — vox-fluency-trap
Generated: 2026-07-28T21:32:25.695075

## GATE BANNED-CARD
[banned-card] PASS — claude-liam-vox-fluency-trap

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in vox-fluency-trap:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False