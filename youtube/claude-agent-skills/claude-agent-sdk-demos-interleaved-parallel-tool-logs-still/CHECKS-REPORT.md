# CHECKS-REPORT.md — claude-agent-sdk-demos-interleaved-parallel-tool-logs-still
Generated: 2026-07-28T22:31:45.902716

## GATE BANNED-CARD
[banned-card] PASS — claude-agent-sdk-demos-interleaved-parallel-tool-logs-still

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-agent-sdk-demos-interleaved-parallel-tool-logs-still:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 4
## checks_green: False