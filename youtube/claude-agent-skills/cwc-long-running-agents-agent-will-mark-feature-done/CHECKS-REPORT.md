# CHECKS-REPORT.md — cwc-long-running-agents-agent-will-mark-feature-done
Generated: 2026-07-28T22:41:03.693135

## GATE BANNED-CARD
[banned-card] PASS — cwc-long-running-agents-agent-will-mark-feature-done

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in cwc-long-running-agents-agent-will-mark-feature-done:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False