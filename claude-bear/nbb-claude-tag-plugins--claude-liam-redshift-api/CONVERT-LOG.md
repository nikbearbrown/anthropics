# CONVERT-LOG — nbb cut of `claude-tag-plugins--claude-liam-redshift-api`

Converted the Plain-register (hai-simple) beat sheet at
`anthropics/claude-bear/claude-tag-plugins--claude-liam-redshift-api/beat_sheet.json`
into the NikBearBrown Teardown cut at
`nbb-claude-tag-plugins--claude-liam-redshift-api/beat_sheet.nbb.json`.

## What changed

- **`_variant_todo` removed** from metadata (scaffold complete).
- **Every beat's `narration_text` rewritten** in the Teardown register (Feynman ×
  MKBHD). The facts, numbers, API names, and API call sequence are unchanged —
  the voice is different. Additions are all "why this way?" framing, never new
  claims.
  - **B00 (cold open)** — leads with "here's what's actually happening" and
    reframes the 200 as a *receipt for submission*, tightening the pivot the
    hesitant writer already sets up.
  - **B01** — names the split (submit-then-poll) as a **design choice**
    optimized for statements that can run for minutes at the cost of
    request-response ergonomics; keeps the typo/FAILED contrast intact.
  - **B02** — same three connection shapes, same anchor, but named as a
    **deliberate refusal to infer** — you pick one, nothing is guessed.
  - **B03** — adds one line explaining *why* `to_entries[0].value` is
    necessary (Redshift wraps every cell in a typed object; the value is one
    indirection down); mechanism stays literal.
  - **BCRY (carry-out)** — same two habits, tightened cadence, phrasing
    matches the on-screen quote card verbatim (which is preserved).
- **BHTF (second-to-last) upgraded to the SKILL.md LLM-exercise beat.**
  - The `ClaudeComposerAsk` `shot` block is untouched — the on-screen prompt,
    running text, and folder chip render identically.
  - The narration now names the paste target explicitly ("paste directly into
    Claude, ChatGPT, or Gemini") and appends a **Go deeper** follow-up:
    *why did AWS split submission and result into two calls — what did the
    Data API optimize for, and what did that cost the caller?* — a real next
    question in the Teardown register, not a summary.
  - Added an `llm_exercise` object (`prompt` + `dig_deeper`) alongside the shot
    block so the beat satisfies SKILL.md §Step 3's schema without disturbing the
    render (Remotion reads the shot; `llm_exercise` is inert metadata).
- **BOUT (outro)** — left as-is. Line and handle are on-screen card copy in the
  `OutroCTA` props (`"Claude, Redshift API. Liam, in for Bear."` /
  `@HumanitariansAI`), and the task instructions require preserving on-screen
  card copy exactly. Precedent set by the prior nbb conversions in this book
  (e.g. `nbb-cwc-workshops--claude-liam-reorder-policy`) confirms the outro
  handle stays on-channel; `metadata.outro_source = "AUTHOR.MD :: NikBearBrown"`
  remains as scaffolded.
- **`estimated_duration_s` bumped** where the Teardown rewrite carries more
  words than the Plain source. Rough scale (source → nbb): B00 14→16, B01 21→30,
  B02 27→34, B03 33→46, BCRY 18→20, BHTF 27→38. BOUT unchanged. Values are plan
  hints only; the render uses measured audio duration as the master clock.

## Preserved exactly

- Every `beat_id` (B00, B01, B02, B03, BCRY, BHTF, BOUT).
- Every `shot` and `graphic` block, including all Manim scene names, Remotion
  patterns, all on-screen text (`text`, `quote`, `sparkLine`, `command`,
  `runningText`, `line`, `folderLabel`, `handle`), palette hexes, `production_viz`
  `label`/`mechanic`/`colors`, and the B00 `note` and TIMING LAW.
- Ending order: `B00 → B01 → B02 → B03 → BCRY → BHTF (LLM exercise) → BOUT
  (outro)` — second-to-last is the LLM exercise, last is the outro.
- Voice: `engine: kokoro`, `voice_kokoro: am_onyx` (Liam, in for Bear). No paid
  engine touched.
- `audio_file` paths, `build` block, all timestamps.

## Judgement calls

1. **Kept BOUT `@HumanitariansAI` and the existing outro line** rather than
   rewriting to a brutalist.art / `@NikBearBrown` sign-off. Reason: the OutroCTA
   `line` and `handle` are on-screen card copy that the task instructions
   protect. This also matches the precedent set by every prior
   `nbb-…` conversion in `anthropics/claude-bear/`.
2. **Enhanced BHTF in place** rather than inserting a new `B_LLM` beat. Reason:
   the source already places a paste-ready Claude prompt as the second-to-last
   beat, its ClaudeComposerAsk render already carries the on-screen prompt, and
   the "preserve every `beat_id`" rule forbids renaming it. Adding a Go-deeper
   line to the narration and an `llm_exercise` metadata object satisfies the
   SKILL.md Step 3 intent without a structural change.
3. **Added `llm_exercise` metadata** to BHTF. This is not in the source, but
   SKILL.md §Step 3 shows it as the schema and adding it is inert for the
   existing render path (Remotion consumes the `shot`, nothing reads the extra
   field). Downstream tooling can now find the paste-ready prompt without
   re-parsing the narration.
