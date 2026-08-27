Fix three narration/screen mismatches in `anthropics/youtube/mas-epistemics`. Run from `books/`.

This SUPERSEDES the earlier `FIX-PROMPT.md` in that folder. Defects 1 and 2 are unchanged; defect 3 is new and is the serious one.

The charts are CORRECT. Do not touch `manim/`, do not regenerate the Figure 4 or Figure 5 masters, do not change any number in a chart. The script drifted from the chart; the script is what gets fixed.

## Ground truth — Figure 4, gap recovered at a 50% lie rate

Read off the rendered frame of `manim/B09.mp4`, in the order the on-screen table ranks them:

| rank | model | gap recovered @ 50% |
|---|---|---|
| 1 | Mythos 5 | 91.5% |
| 2 | Opus 4.8 | 62.5% |
| 3 | Opus 4.6 | 59.3% |
| 4 | Sonnet 5 | 37.8% |
| 5 | **Sonnet 4.6** | **34.4%** |

At the 0.25 lie rate the line chart reverses: Sonnet 5 is the lowest line of all five. The on-screen footer already states this correctly — "last of five at 0.25".

## Ground truth — Figure 5, hidden profile

Read off the rendered frame of `manim/B21.mp4`. Bar order left to right is Sonnet 4.6, Sonnet 5, Opus 4.6, Opus 4.8, Mythos 5.

| model | group accuracy | solo ceiling | deliberation cost |
|---|---|---|---|
| Sonnet 4.6 | 17.5 | ~96.2 | -78.7 pp |
| Sonnet 5 | 35.5 | ~97.3 | -61.8 pp |
| Opus 4.6 | 18.5 | ~98.6 | -80.1 pp |
| Opus 4.8 | 18.2 | ~98.7 | -80.5 pp |
| Mythos 5 | 85.2 | ~100 | -14.8 pp |

---

## Defect 3 (NEW, most serious) — B09 stops one row early, and B10 then contradicts the table on screen

B09 reads Mythos 5, Opus 4.8, Opus 4.6, Sonnet 5 — and stops. The fifth row, Sonnet 4.6 at 34.4%, is visible on screen directly beneath Sonnet 5 and is never spoken. B10 then says "Sonnet 5 is last of all five" while the table showing Sonnet 4.6 last is still on screen.

The 0.25 claim is true. The problem is that it is spoken over the 0.50 table without naming the switch, and the row that complicates the story is the one row left unread. In a film whose entire thesis is "the post's sentence does not match its own chart," omitting the inconvenient row is the exact failure being criticised.

In `beat_sheet.json`, beat **B09**, replace `narration_text` exactly:

FROM
```
Mythos 5 recovers ninety-one and a half percent. Opus 4.8, sixty-two. Opus 4.6, fifty-nine. Sonnet 5 — which the post calls, quote, our most recent model — recovers thirty-seven point eight.
```

TO
```
Mythos 5 recovers ninety-one and a half percent. Opus 4.8, sixty-two and a half. Opus 4.6, fifty-nine point three. Sonnet 5 — which the post calls, quote, our most recent model — recovers thirty-seven point eight. And the older Sonnet 4.6, thirty-four point four.
```

In beat **B10**, replace `narration_text` exactly:

FROM
```
That is below a model two generations older. And at a twenty-five percent lie rate, Sonnet 5 is last of all five.
```

TO
```
Both Opus models are older, and both beat it. Only the previous Sonnet lands lower. Drop the lie rate to twenty-five percent, and Sonnet 5 is last of all five.
```

This keeps the argument and removes the contradiction: it now says out loud that Sonnet 4.6 is below Sonnet 5 at the 50% rate, and it marks the lie-rate switch before making the "last of five" claim. B11's conclusion — the ordering is capability tier, not recency — is strengthened, not weakened, because both older Opus models beating the newer Sonnet is now stated explicitly.

## Defect 1 — B17 points at the wrong bars

B17 says "the middle three bars," then B18 reads 17.5 / 18.5 / 18.2 — bars 1, 3 and 4. The middle three are 35.5, 18.5, 18.2.

In beat **B17**, replace `narration_text` exactly:

FROM
```
The caption talks about scaling: performance scales with model intelligence but does not saturate. Look at the middle three bars.
```

TO
```
The caption talks about scaling: performance scales with model intelligence but does not saturate. Look at the three short bars.
```

**B18 needs no change.** Its numbers are right and "a flat floor with two outliers" is correct — the outliers are Sonnet 5 at 35.5 and Mythos 5 at 85.2.

## Defect 2 — B22 says "eighty points in four cases," but only three are ~80

-78.7, -80.1 and -80.5 are ~80. Sonnet 5 is -61.8 and Mythos 5 is -14.8. The wrong sentence is in BOTH the narration and the `ClaudeVerdictArtifact` props, so fixing the voiceover alone leaves it on screen. Change both.

In beat **B22**, replace `narration_text` exactly:

FROM
```
For every single model tested, group discussion made the group worse than one agent with the same information. Eighty percentage points worse, in four cases out of five.
```

TO
```
For every single model tested, group discussion made the group worse than one agent with the same information. Sixty to eighty percentage points worse, in four cases out of five.
```

In the same beat, `shot.remotion.props.artifactLines`, replace the third entry exactly:

FROM
```
Eighty percentage points worse, in four cases out of five.
```

TO
```
Sixty to eighty percentage points worse, in four cases out of five.
```

That range is exact: the four collapsed models are -61.8, -78.7, -80.1, -80.5. "Every single model tested" stays — all five are negative.

---

## Then rebuild, in this order

1. Regenerate audio for **B09, B10, B17 and B22 only** with `runtime/scripts/generate_audio_kokoro.py`, voice `am_onyx`. Audio is free and local — generate it, do not stop to ask. Leave the other 25 mp3s alone.
2. Let the new measured durations write back to `timings.json`. Never hand-edit a timing.
3. Re-render **B22** only, via `runtime/scripts/remotion_scenes.py <reel>`, foreground, `--concurrency=1`. Never hand-roll `npx remotion render`. B09, B10 and B17 are external Manim masters and do not re-render.
4. B09 gets noticeably longer and B10 slightly shorter. If the new audio no longer fits those Manim clips, fix it at the compile step — never by trimming narration back to something inaccurate, and never by editing the chart.
5. Recompile the reel.

## Verify before calling it done

Extract a late frame from `manim/B09.mp4` and from the newly rendered `media/B22.mp4`, open both, and read them. Confirm with your own eyes that all five rows in the Figure 4 table are now spoken, and that the B22 card says "Sixty to eighty percentage points worse, in four cases out of five." An ffprobe pass is not verification.

Then re-check the whole reel for this class of defect, applying all three tests:

- every number spoken matches the number rendered in that beat's clip
- every model name spoken matches the labels on screen
- **no ranked list is read partially** — if a chart shows five rows and the narration reads four, that is a defect even when every number spoken is correct

Report anything else you find. Do not fix beyond the three defects above without telling me first.

## Housekeeping

- Delete the `_numcheck/` folder in the reel directory — leftover frame extractions from the audit.
- Append to `BUILD-LOG.md`: all three defects, what the chart actually showed, what the narration said, the exact edits, and that the charts were confirmed correct and left untouched. Note explicitly that defect 3 was a partial read of a ranked table, so future checks look for it.
- Do not publish. Do not stage to TOPOST. Do not upscale.
