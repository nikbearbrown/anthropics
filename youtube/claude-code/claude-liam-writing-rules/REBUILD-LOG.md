# REBUILD-LOG — claude-liam-writing-rules

Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy of `beat_sheet.json` before edits).

## Locked
- Every beat's `narration_text` — unchanged.
- Beat order, act labels, sparkLines (except B01 — see below).
- Metadata identity (title, slug, topic, brand, greeting, folderLabel).

## Rebuilt / edits made BEFORE the final compile

### Sheet edits
| beat | field | old | new | reason |
|---|---|---|---|---|
| B00 | `shot.remotion.props.modelLabel` | `Opus 4.8` | `Opus 4.7` | DATABLE CLAIM — `Opus 4.8` does not exist. Current top-tier is Claude Opus 4.7 (model ID `claude-opus-4-7`). |
| B01 | `shot.remotion.props.sparkLine` | `Name it. Event it. Pattern it. Message it. One markdown file, immediate effect.` (13 words) | `Name. Event. Pattern. Message. One markdown file — immediate effect.` (9 words) | GATE T §8.5 no-wordy-card: 12-word limit for pull-quote elements. Compressed to 9 while keeping the "name+event+pattern+message" structural cue. |

### Scene edits (per-reel content fix; only this reel uses HookifyTell)
- `runtime/remotion/src/scenes/HookifyTell.tsx`: sparkLine wrapper
  `bottom: H * 0.04` → `bottom: H * 0.06`. GATE T §8.2 overflow — the italic
  sparkLine at bottom 4% sat below the 5% title-safe bottom boundary at 3840×2160.
  Moved 2% up to sit inside the safe box. No other reel uses this scene (grep
  across all `beat_sheet.json` under `anthropics/youtube/`).

## Kept (no datable claims found)
- B00–B05, BVDT, BHTF, BOUT narration: no model names, versions, prices, or
  "as of" phrasing that has rotted.

## Bookends / structure
- B00 `ClaudeComposerAsk`, BVDT `ClaudeVerdictArtifact`, BHTF `ClaudeComposerAsk`
  (Your-turn), BOUT `ClaudeTitleOutro` — canonical bookend chain, all four present.
- Verdict is a real verdict (rule format, 5 events, action, body, four gaps) —
  authored from the body's own nouns. Not stripped.
- BHTF is a real exercise ("write Hookify rules that Claude Code can enforce
  deterministically — pattern, vague-vs-precise, false-positive test"). Not the
  "[Take what you learned…]" template.

## Post-compile edits
None. Compile runs after this log; no sheet edits after the master mp4.
