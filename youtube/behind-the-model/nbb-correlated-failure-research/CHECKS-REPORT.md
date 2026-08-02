# CHECKS-REPORT.md — correlated-failure-research
Generated: 2026-07-28T21:45:26.683008

## GATE BANNED-CARD
[banned-card] PASS — nbb-correlated-failure-research

## GATE BOOKEND
[bookend] BLOCKED — 4 failure(s) in correlated-failure-research:
  ✗ COLD-OPEN: first beat pattern='FormBCard' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO subline 'pick the highest-stakes one and replace the llm audit with a structurally indepe' is not empty — subline is opt-in per video; remove it or set to ""

## compile: OK
## FormBCard beats: 2  boxes: 3
## checks_green: False