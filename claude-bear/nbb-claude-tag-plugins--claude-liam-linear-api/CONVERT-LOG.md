# CONVERT-LOG — claude-tag-plugins--claude-liam-linear-api → nbb

## What changed

Every beat rewritten in the Teardown register (Feynman × MKBHD): explain the
machinery, reveal the design philosophy, name the trade-offs. Facts unchanged —
every endpoint, ID system, status code, header quirk, and reset-time unit
survives from the source verbatim.

- **B00 (cold open)** — sharpened to "expected REST, got one GraphQL endpoint";
  kept ~34 words per BrutalistHesitantWriter TIMING LAW window.
- **NB01 (mechanism)** — opened with "Here's what's actually happening"; framed
  the one-endpoint design as an explicit trade with REST's status-code intuition.
- **NB02 (mechanism)** — reframed the viewer / UUID / success / totalCount
  patterns as the price of trading REST's fixed shape for GraphQL's flexible
  one. Kept the four facts intact.
- **NB03 (mechanism)** — kept the 400-not-429 mechanism and the epoch-ms fact;
  added the design-critic reading ("can't tell 'throttled' from 'query is
  wrong'"). Estimated duration nudged 29 → 33s to fit the sharpened phrasing.
- **BCRY (carry-out)** — same two-sided observation, with one added Teardown
  clause ("the status code isn't the answer here; the body is"). WantQuote prop
  quote updated to match narration; sparkLine also updated.
- **BHTF** — repurposed from "your turn handoff" to `act: "LLM EXERCISE"`.
  Added `llm_exercise` block (paste-ready prompt + `dig_deeper` follow-up).
  The `dig_deeper` extends the video: it asks the model to write the retry loop
  that would use NB03's 400/RATELIMITED + epoch-ms facts. Narration updated to
  "Paste this into Claude, ChatGPT, or Gemini" + `Go deeper: …`. Duration bumped
  27 → 44s to fit the added dig-deeper line.
- **BOUT (outro)** — switched Remotion pattern from `OutroSeries` → `OutroCTA`
  (matches reference nbb sibling reels' NikBearBrown outro shape) and folded
  the subtitle into the sign-off line: "There's No REST API Here — the Linear
  API Skill. Liam, in for Bear."

## Judgement calls

- **Handle kept as `@HumanitariansAI`**, not `@NikBearBrown`. Scaffold left
  `folderLabel` and `channel_title` as `@HumanitariansAI`; every sibling nbb
  reel in `anthropics/claude-bear/nbb-*` does the same in its `OutroCTA` handle
  and `ClaudeComposerAsk` folderLabel. Followed reference practice rather than
  the literal AUTHOR.MD `@NikBearBrown` pointer — the supervisor can retarget
  if that call is wrong.
- **`in_for_bear: true` metadata is already set and the outro carries "Liam,
  in for Bear"** — did not force an extra "Liam, in for Bear" sentence into
  the B00 cold-open narration, matching every other reference nbb reel.
  The BrutalistHesitantWriter visual carries the setup; the outro carries the
  sign-off.
- **BCRY's WantQuote `quote` prop was updated to match the new narration** —
  on-screen card copy is the narration's carry-out sentence, so the two need
  to agree letter-for-letter.
- **Estimated durations updated** where narration length changed materially
  (NB03, BCRY, BHTF, BOUT). Real durations are a render-pass concern; not my
  step. `actual_duration_s` stayed removed (scaffold had already stripped it).
- **`build` blocks left untouched.** The MP3s and MP4s referenced will be
  stale after this rewrite; regenerating audio (Kokoro `am_onyx`) and
  recompiling is the next pass's job, not this one.

## What was not touched

Every `beat_id`, act label (except BHTF, promoted to LLM EXERCISE per SKILL.md
§Step 3), `shot` block, Remotion `props` other than the two quote/sparkLine
updates in BCRY, Manim scene names, graphic chip lists, palette hexes,
`engine`, `voice_kokoro`, `palette`, `audience`, `outro_source`. `_variant_todo`
removed per SKILL.md Step 5 verification.
