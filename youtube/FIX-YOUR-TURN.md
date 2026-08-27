Fix the empty YOUR TURN composer in two Anthropic reels. Run from `books/`.

## The bug

In `ClaudeComposerAsk`, `greeting` renders ABOVE the composer and `command` renders INSIDE it. The YOUR TURN beats in two reels have these swapped: `command` was set to the literal string "Your turn." and `greeting` to "The ask,". The result on screen is a composer whose body reads "Your turn" with no prompt in it — while `runningText` underneath still says "runnable prompt, read in full" and the narration reads a prompt aloud that the viewer can't see or copy.

The cold opens (B01) are correct in every reel. This is only the your-turn beats. `mas-coordination` B33 has it right and is the reference shape.

Affected:

- `anthropics/youtube/mas-epistemics` beat **B28**
- `anthropics/youtube/mas-turf-war` beat **B25**

## Fix 1 — mas-epistemics B28

In `anthropics/youtube/mas-epistemics/beat_sheet.json`, beat **B28**, `shot.remotion.props`:

Set `greeting` to exactly:
```
Your turn.
```

Set `command` to exactly:
```
Split one decision's evidence across four separate chats — each sees the shared facts plus one unique decisive fact. Let them exchange summaries. Do the unique facts ever reach the final answer? Then give a single chat everything and compare.
```

Leave `topic`, `segment`, `runningText`, `folderLabel`, `modelLabel` and `effortLabel` as they are.

The narration already reads this prompt in full and does not change. Check the wording matches what B28's `narration_text` describes — same four chats, same unique-fact-per-chat setup, same solo comparison at the end — so the spoken words and the on-screen prompt agree.

## Fix 2 — mas-turf-war B25

In `anthropics/youtube/mas-turf-war/beat_sheet.json`, beat **B25**, `shot.remotion.props`:

Set `greeting` to exactly:
```
Your turn.
```

Set `command` to exactly:
```
Give two agent sessions genuinely incompatible instructions on one shared folder — not hostile, just contradictory — then read both reasoning traces. Does either one ever consider that the other might be following orders too?
```

Leave the other props alone. Narration does not change.

## Rebuild

1. No audio regeneration. The narration text is unchanged in both reels — do not touch `mp3/`.
2. Re-render **B28** in mas-epistemics and **B25** in mas-turf-war, via `runtime/scripts/remotion_scenes.py <reel>`, foreground, `--concurrency=1`. Never hand-roll `npx remotion render`.
3. Recompile both reels.

If mas-epistemics also has the pending narration fixes from `mas-epistemics/FIX-PROMPT.md` (B09, B10, B17, B22) not yet applied, apply those in the same pass and regenerate only those four mp3s — but this composer fix is independent of them and needs no audio.

## Verify

Extract a frame from each newly rendered beat, open it, and read it. Confirm the composer body now contains the full runnable prompt and that "Your turn." sits above the composer, not inside it. An ffprobe pass is not verification.

## Then sweep for the same bug everywhere else

This is a beat-sheet authoring error, not a component bug, so it can be anywhere `ClaudeComposerAsk` is used. Across ALL reels under `computational-skepticism-for-ai/youtube/`, `skepticism-ai/youtube/`, `brutalist-art/youtube/` and `anthropics/youtube/`, find every beat whose `shot.remotion.pattern` is `ClaudeComposerAsk` and flag any where:

- `command` is shorter than ~25 characters, or
- `command` is one of "Your turn.", "The ask,", "Try this," or any other greeting-shaped string, or
- `command` is empty or missing, or
- `greeting` is longer than `command`

Write the results to `books/COMPOSER-AUDIT.md` as a table: reel, beat, act, current `greeting`, current `command`. Do not fix anything beyond the two beats named above — report the rest and I will decide.

## Housekeeping

- Append to each reel's `BUILD-LOG.md`: the swapped props, what was on screen, the exact new values, and that no audio was regenerated.
- Do not publish. Do not stage to TOPOST. Do not upscale.
