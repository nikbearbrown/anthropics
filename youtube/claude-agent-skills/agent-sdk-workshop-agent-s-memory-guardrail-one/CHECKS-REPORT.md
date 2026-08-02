# CHECKS-REPORT.md — agent-sdk-workshop-agent-s-memory-guardrail-one
Generated: 2026-07-28T22:27:16.610277

## GATE BANNED-CARD
[banned-card] PASS — agent-sdk-workshop-agent-s-memory-guardrail-one

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in agent-sdk-workshop-agent-s-memory-guardrail-one:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 1
## checks_green: False