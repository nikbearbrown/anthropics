# CONVERT-LOG — nbb-claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before

Converted `beat_sheet.json` (Plain register, hai-simple) → `beat_sheet.nbb.json`
(Teardown register, NikBearBrown audience). Facts unchanged. `_variant_todo` removed.

## What changed

- `metadata.register`: `Plain` → `Teardown` (already set by scaffold; preserved).
- `metadata.purpose`: rewritten to name the machinery (stack + zero-value default)
  and the design trade (usable-and-provisional over correct-and-late), consistent
  with the new narration. Facts identical.
- **Every `narration_text` rewritten** in the Teardown register:
  - Strip "the natural guess" → name the priority the design was built for.
  - B03: added the design judgement line — "They optimized for feedback speed
    at the cost of ever handing you a value you can trust as final."
  - B04: named the trade explicitly — "Shape-safe and value-final are two
    different guarantees, and the parser only gives you the first."
  - BCRY: tightened the carry-out to the same trade (shape-safe vs value-done).
- **WantQuote prop `quote`** (BCRY) updated to match the new carry-out sentence.
  `sparkLine`: "Shape-safe vs. value-finished." → "Shape-safe, not value-final."
  to compress the trade into three words on-screen.
- Every `beat_id`, `act`, `shot`, `graphic`, Manim scene name, and on-screen
  card mechanic preserved verbatim.

## LLM exercise placement — judgement call

SKILL.md §Step 3 says "insert one beat before the outro" with `beat_id: B_LLM`.
The source already had a second-to-last **your-turn handoff** beat (`BHTF`)
whose whole point is a paste-ready ClaudeComposerAsk prompt. Inserting a new
`B_LLM` beat would leave two adjacent "here's a prompt, paste it" beats —
redundant and it violates the invocation's own preservation rule ("Preserve
exactly: every `beat_id`"), which would forbid re-numbering BHTF away.

Call: keep `BHTF` as the LLM-exercise beat. Rewrote its narration in the
Teardown register, added the required "Go deeper: …" follow-up spoken at the
tail, and attached the `llm_exercise` object (`prompt` + `dig_deeper`) that
SKILL.md's schema requires. The `act` field is now
`"LLM EXERCISE - your turn handoff"` so the role is visible. `estimated_duration_s`
raised 24 → 32 to cover the added dig-deeper sentence (narration is the clock).

The on-screen `ClaudeComposerAsk.command` stays the paste-ready prompt only
(no dig-deeper) — the dig-deeper is a spoken follow-up, not composer text.
`runningText` updated: "paste your streaming tool-call handler…" → "paste this
into Claude, ChatGPT, or Gemini…" so the on-screen affordance names the frontier
LLMs the exercise is written for.

## Outro

`BOUT` preserved as the last beat: title re-read + "Liam, in for Bear." sign-off,
`OutroCTA` pattern, `handle: "@HumanitariansAI"`. This matches the sibling nbb
sheets under this book (e.g. `nbb-claude-basics--screenshot-prompt-caching`) —
the reel lives on the HumanitariansAI channel; nbb is the register/palette
overlay, not a channel move.

## Not changed

- No render, no compile, no audio generation. The sheet is the deliverable.
- `voice: "am_onyx"`, `engine: "kokoro"` left exactly as the scaffold set them
  (IN-FOR-BEAR LAW; Liam, in for Bear).
