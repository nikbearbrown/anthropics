# CONVERT-LOG — nbb-claude-for-legal--claude-liam-chronology

Register conversion from `beat_sheet.json` (Plain, HAI Simple) →
`beat_sheet.nbb.json` (Teardown, NikBearBrown). Voice: Liam (Kokoro `am_onyx`),
in for Bear. Facts unchanged; register only. No render, no audio, no compile.

## What changed

- **Removed** `_variant_todo` from `metadata`.
- **Rewrote** `narration_text` on B00, B01, B02, B03 in the Teardown register:
  strip the survey-y "one could argue" tone, name what the plain-sort machinery
  actually does, and name the design trade-off ("optimized for completeness, at
  the cost of any sense of what actually happened"; "the events are shared, the
  weights are not"). Every fact from the source survives — the same three
  documents, the same late-payment anchor, the same high/low tag split on the
  same two matter theories, the same "same day" collapse rule.
- **Kept** BCRY's carry-out sentence intact (the source line was already clean
  Teardown — direct, no filler, judges by naming "weighed"). The WantQuote
  `quote` prop stays in sync with the narration.
- **Converted** BHTF from "your turn handoff" into the **LLM EXERCISE** beat
  (second-to-last): added an `llm_exercise` object with a paste-ready prompt for
  Claude / ChatGPT / Gemini and a "Go deeper" follow-up; rewrote the narration
  to read the prompt aloud and hand off; updated the `ClaudeComposerAsk` `command`
  prop to mirror the LLM prompt and expanded `runningText` to "paste this into
  Claude, ChatGPT, or Gemini…" so the composer chip matches the new all-frontier
  framing. Bumped `estimated_duration_s` from 24 → 30 to fit the longer body.
- **Kept** BOUT as the outro (last beat), same `OutroCTA` pattern, same
  `@HumanitariansAI` handle (matches sibling nbb-* reels in this book — the
  outro `handle` field is the destination channel, not the AUTHOR.MD source).
  Enriched the line to "Claude, Chronology. Every event named once, weighed by
  the case. Liam, in for Bear." so the outro re-lands the carry-out; bumped
  `estimated_duration_s` from 6 → 8. `outro_source: AUTHOR.MD :: NikBearBrown`
  metadata field left as the scaffold wrote it.

## Judgement calls

- **BCRY untouched.** The carry-out sentence is the show's poster; it also
  appears verbatim in the `WantQuote` prop. It was already Teardown-clean, so
  rewriting would have added risk (drifting the two copies apart) with no
  register gain. Left it.
- **B00 word count.** Rewritten to 34 words, inside the note's 20-35-word band
  that keeps the BrutalistHesitantWriter typing window ≥ 9 s. The trigger →
  replacement pair (`sort` → `weigh`) survives on-screen unchanged; the new
  narration explicitly walks the same arc verbally ("sort … weigh on the case").
- **BOUT handle stays `@HumanitariansAI`.** The scaffold set the outro
  `handle` and `channel_title` to `@HumanitariansAI` and every completed sibling
  nbb-* reel in `claude-bear/` uses the same. `outro_source: AUTHOR.MD ::
  NikBearBrown` in metadata is the register/voice attribution, not a channel
  swap. Kept the sibling convention.
- **LLM exercise scope.** The source's BHTF prompt was already frontier-LLM
  shaped (paste in the documents, ask Claude to pull-collapse-flag). Generalised
  it to Claude / ChatGPT / Gemini and added a genuinely explorable "Go deeper"
  question (what would have to change about the matter's theory for a
  low-tagged event to flip to high) — probing the same design choice the video
  just landed, not a summary.
