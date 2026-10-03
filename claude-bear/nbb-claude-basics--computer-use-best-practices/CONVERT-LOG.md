# CONVERT-LOG — nbb-claude-basics--computer-use-best-practices

Converted `beat_sheet.nbb.json` from the hai-simple Plain-register source into the
NikBearBrown Teardown register. Facts unchanged (1200 tok/screenshot, 10-step =
12k, 20-step = 40k, resize+prune = 70–80% cut, ~1568px width, the seven changes,
the recording distinction). Voice = Kokoro `am_onyx` (Liam, in for Bear).

## What changed

- **Every `narration_text` rewritten in Teardown** (Feynman × MKBHD) — machinery
  named, design decision surfaced ("optimized for demo simplicity, not for how
  the bill compounds"; "the seventh change is different — it doesn't lower cost,
  it makes the run inspectable"). All `beat_id`s, `shot` blocks, `graphic`
  blocks, and on-screen card copy preserved.
- **BHTF became the LLM EXERCISE beat (second-to-last).** `act` → `LLM
  EXERCISE`; added the required `llm_exercise` object (`prompt` + `dig_deeper`);
  updated `ClaudeComposerAsk.command` to the paste-ready prompt with a
  Teardown-shaped "judge your own schema" turn and a real dig-deeper question
  ("which fields catch a wrong-task success, and which let one hide?").
  `segment` → `LLM Exercise`; `runningText` → "paste this into Claude, ChatGPT,
  or Gemini…" to reflect the LLM-agnostic contract.
- **BOUT became the NBB outro.** `handle` → `@NikBearBrown`, `line` and
  `narration_text` updated to name the channel per the brand spec's default
  (`www.brutalist.art`, read as "brutalist dot art"). Liam sign-off preserved
  (IN-FOR-BEAR LAW).
- **Metadata:** `folderLabel` and `channel_title` → `@NikBearBrown` so the NBB
  variant renders with the correct channel chip on `ClaudeComposerAsk` and the
  correct outro handle. `_variant_todo` removed.

## Judgement calls

1. **BCRY (carry-out) narration was left verbatim.** The same string is also the
   on-screen `WantQuote.quote`; rewriting the narration without rewriting the
   quote would desync audio and image, and the existing sentence is already
   Teardown-compatible ("Production isn't the demo running longer — it's every
   screenshot made leaner and every action logged"). Changing the wording only
   for register cosmetics would violate "change the voice, not the facts" for a
   thesis sentence.
2. **No `AUTHOR.MD` exists for the `anthropics/claude-bear/` book,** so the NBB
   outro uses the brand-spec default channel (`www.brutalist.art`) with
   `@NikBearBrown` as the handle chip. If an AUTHOR.MD :: NikBearBrown block
   later gets written, the outro line should be re-derived from it.
3. **Metadata `folderLabel`/`channel_title` changed from `@HumanitariansAI` to
   `@NikBearBrown`.** The scaffold left them inherited from the hai-simple
   source, but this reel is now the NBB cut and both fields drive on-screen
   render text (composer chip + outro handle). Leaving them as HAI would render
   the NBB reel under the wrong channel identity.
4. **B02 `estimated_duration_s` kept at 16s** even though the Teardown rewrite
   is 42 words (~11s at Kokoro's ~4 wps). Kokoro will overwrite `actual_duration_s`
   on generation — the estimate is a coarse budget for `duration-planner`, not a
   render constraint.

## Ending order verified

```
… B04 (anchor payoff) → BCRY (carry-out) → BHTF (LLM EXERCISE) → BOUT (NBB outro)
```

## Not done here (next passes)

- Kokoro audio generation (`generate_audio_kokoro.py`) — no audio was
  regenerated; `mp3/beat-*.mp3` and `actual_duration_s` from the source scaffold
  are stale and will get overwritten by the next audio pass.
- Render / compile.
