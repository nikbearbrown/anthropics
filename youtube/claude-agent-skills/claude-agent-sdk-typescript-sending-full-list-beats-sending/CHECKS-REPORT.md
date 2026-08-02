# CHECKS-REPORT.md — claude-agent-sdk-typescript-sending-full-list-beats-sending
Generated: 2026-07-28T22:32:50.384520

## GATE BANNED-CARD
[banned-card] PASS — claude-agent-sdk-typescript-sending-full-list-beats-sending

## GATE BOOKEND
[bookend] BLOCKED — 3 failure(s) in claude-agent-sdk-typescript-sending-full-list-beats-sending:
  ✗ COLD-OPEN: first beat pattern='' — expected one of ['ClaudeCodeBeat', 'ClaudeComposerAsk']
  ✗ RECAP (BVDT): no ClaudeVerdictArtifact beat found — add beat_id=BVDT
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat

## compile: OK
## FormBCard beats: 1  boxes: 2
## checks_green: False