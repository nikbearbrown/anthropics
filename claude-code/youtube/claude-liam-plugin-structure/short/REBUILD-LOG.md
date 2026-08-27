# REBUILD-LOG.md — claude-liam-plugin-structure-short

Session: 2026-08-20 (film-factory, unattended)

## Pre-rebuild backup

`beat_sheet.pre-rebuild.json` created 2026-08-20 before any edit.

## VOICE-LOCK normalized

No dead ElevenLabs-era fields were present. engine=kokoro, voice=am_onyx already
correct. No changes needed.

## Prop edits (beat content)

| Beat | Field | Old value | New value | Source / reason |
|---|---|---|---|---|
| BHTF | shot.remotion.props.greeting | "Your Turn" | "Your turn." | SPARK-LINE LAW: BHTF greeting must be "Your turn." (lowercase t, period). Visible defect confirmed in Gate V: old render showed "Your Turn" on screen. |

## Narration

No narration text was changed. The narration lock holds.

## Stale renders cleared

All beat mp4s deleted (were 1–94 seconds older than beat_sheet.json from original build).
Re-rendered via remotion_scenes.py --force. All 4 Remotion beats confirmed rendered fresh.

## Rebuild result

New master: claude-liam-plugin-structure-short.mp4 (2026-08-20T09:29:10)
All beats VIDEO (no slates). GATE AUDIO PASS (-24.0 dB).
