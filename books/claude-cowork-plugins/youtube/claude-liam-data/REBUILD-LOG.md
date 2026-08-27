# REBUILD-LOG — claude-liam-data
**Date:** 2026-08-27

## Pre-rebuild backup
`beat_sheet.pre-rebuild.json` created before any edits.

## Narration changes (LOCKED — only permitted edits)
No narration_text edits to body beats. Narration is locked.

**BVDT narration authored (new — was empty):**
- Old: `""` (empty string)
- New: `"The data plugin opened the file you were afraid of. Three clients carry sixty percent of revenue — data, not gut feel. Ten minutes the first of every month keeps you from being surprised by your own numbers. One client at forty percent of income is a concentration risk you can now actually see. And the analysis is only as trustworthy as your data and your assumptions. That part is still yours."`
- Source: Authored from body beats B07 (three clients, 60%), B16 (ten minutes, monthly), B19 (40% concentration), B21/B23 (data+assumptions, judgment is yours). This is the CLOSE narration for the verdict bookend — expected new writing under rebuild contract §4.

## Field edits
| Field | Beat | Old | New |
|-------|------|-----|-----|
| `props.artifactLines` | BVDT | ["Key finding one", "Key finding two", "Key finding three"] | [4 real findings from body] |
| `artifactHeading` | BVDT | "Key findings" | "What we found" |
| `estimated_duration_s` | BVDT | 20 | 28 |
| `narration_text` | BVDT | "" | Authored from body (see above) |
| `props.folderLabel` | BHTF | "@claude-liam" | "@NikBearBrown" |

## Scene edits (scenes_std.py)
**B19 scene**: Replaced narration-fragment bar labels with SHORT CATEGORY NOUNS. Fixed ACT label double-space. Fixed caption to complete sentence. Changed from 2-bar wrong pattern to proper 3-bar threshold visualization (Top Client at 40% terracotta, risk threshold line at 30%).

**B24 scene**: Replaced wrong 2-bar comparison with correct 4-tile accumulate pattern (Ask Specific → Iterate → Compare → Export Regularly). Fixed ACT label double-space. Fixed caption to complete sentence.

## Datable claims
No datable claims found in narration. No model version references, no price claims, no "as of" phrasing.
