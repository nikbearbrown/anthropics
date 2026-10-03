# CONVERT-LOG — nbb cut of `claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context`

Source → NBB rewrite of `beat_sheet.json` into `beat_sheet.nbb.json`.
Voice-only. Every number, name, API surface, and file-level fact from the source
survives unchanged. Scaffold metadata (`audience`, `engine`, `voice_kokoro`,
`palette`, `register`, `outro_source`, `derived_from`, `typography`) left in the
state `brand_variant.py` wrote.

## What changed

- **Every `narration_text` rewritten in the Teardown register.** Feynman × MKBHD:
  explain the machinery ("a server-verifiable token, signed by the API so it
  knows it produced it"), reveal the design choice ("they split the work into a
  memory object the server owns and a display object you own"), name the
  trade-off ("Two jobs, two payloads. Send the wrong one to the next call and
  only one of those jobs fails."). Forbidden phrases avoided; concrete
  "here's what's actually happening" framing kept throughout. All eight
  `beat_id`s, all `shot` blocks, all `production_viz` mechanics, all
  BrutalistHesitantWriter / WantQuote / ClaudeComposerAsk / OutroCTA prop shapes
  preserved verbatim.
- **BHTF turned into the explicit LLM-exercise beat** (SECOND-TO-LAST).
  Reused `BHTF` rather than inserting a new `B_LLM` beat, following the
  precedent set by the sibling nbb reel
  `nbb-claude-basics--screenshot-prompt-caching/beat_sheet.nbb.json` — that reel
  also has a `ClaudeComposerAsk` handoff as second-to-last with the paste-ready
  prompt baked into the `command` prop, and inserting a duplicate `B_LLM` beat
  would have doubled the "your turn" moment. Added:
  - `act` renamed to `"your turn handoff / LLM exercise"` so the role is
    unambiguous.
  - A new `llm_exercise` block with `prompt` (paste-ready, no CLI, works in
    Claude/ChatGPT/Gemini on its own) and `dig_deeper` (a real next question
    about API-key rotation mid-session and compaction-mid-stream — a genuinely
    explorable follow-up, not a summary).
  - The narration now says "you can paste into Claude, ChatGPT, or Gemini" so
    the LLM-exercise framing is spoken out loud, and closes with the explicit
    "Go deeper:" follow-up.
  - `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".
- **BOUT kept as the NikBearBrown-style outro** (LAST beat). Uses the full
  metadata title in title-case followed by "Liam, in for Bear." — same shape as
  the sibling nbb reel's outro. `handle` left as `@HumanitariansAI` because
  this is a hai-simple source destined for that channel, and the sibling nbb
  reel follows the same convention (the scaffold also preserved the HAI
  `channel_title` and `folderLabel`, so overriding the outro handle to
  `@NikBearBrown` would have contradicted the rest of the sheet).
- **`_variant_todo` removed** from `metadata` — all four checklist items are
  now done.
- **Purpose line rewritten** to state the Teardown framing ("two payloads,
  two jobs") explicitly, matching the new register.

## Judgment calls

1. **No new `B_LLM` beat.** SKILL.md §Step 3 gives a `B_LLM` schema, but the
   source's `BHTF` already IS the "your turn / paste-this-prompt" beat. Adding
   a separate `B_LLM` before it would have created two sequential handoffs. The
   sibling nbb reel resolves this the same way. I annotated the choice by
   renaming the `act` and attaching the `llm_exercise` block onto `BHTF`.
2. **Outro handle stayed `@HumanitariansAI`.** As documented above, this
   matches the sibling nbb reel and stays consistent with the rest of the
   HAI-flavored metadata the scaffold preserved. If the intent is to flip the
   whole reel to `@NikBearBrown` (channel, folder, outro), that's a bigger
   metadata edit than a register rewrite.
3. **Estimated durations bumped** on beats whose narration got longer (B00 14→15,
   B01 16→22, B02 17→20, B03 14→18, B04 17→22, BHTF 24→26). These are
   estimates only; audio-first pipeline will replace them with measured
   `actual_duration_s` from the regenerated Kokoro mp3s.
4. **`estimated_duration_s` bumped, `actual_duration_s` cleared implicitly.**
   Left `actual_duration_s` off entirely on rewritten beats so nothing
   downstream mistakes stale (pre-rewrite) durations for the truth. The
   regenerate-audio step will write fresh ones.
5. **On-screen card copy preserved.** BrutalistHesitantWriter text, WantQuote
   quote + sparkLine, ClaudeComposerAsk topic/segment/greeting, and OutroCTA
   handle all left in the Teardown register or already register-neutral. Only
   the `ClaudeComposerAsk.command` was updated to match the sharpened prompt
   in the `llm_exercise` block.

## Ending order (verified)

B00 → B01 → B02 → B03 → B04 → BCRY → **BHTF (LLM exercise)** → **BOUT (outro)**.
