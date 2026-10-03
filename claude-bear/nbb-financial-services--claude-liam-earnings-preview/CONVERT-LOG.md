# CONVERT-LOG — financial-services--claude-liam-earnings-preview → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-earnings-preview/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman × MKBHD).
  Every fact from the source survives unchanged: the skill is a folder Claude reads
  before it acts, the file is called earnings-preview, SKILL.md holds plain-language
  instructions with no hidden code, Steps run linearly with no branching unless a
  step calls for it, the brief is estimate models + bull/bear scenarios + a handful
  of metrics likely to move the stock, and the skill deliberately does not forecast
  the number itself. Voice-only edit: named the mechanism ("the file is the
  program"), named the design choices ("predictability over cleverness"; "they
  optimized for repeatable scenario prep at the expense of a prediction it couldn't
  be honest about anyway"), and kept the honest limit intact ("still won't tell you
  what the report is going to say").

- **BHTF upgraded to the LLM EXERCISE beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added a
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini, parameterized with `[COMPANY]` so the viewer plugs in whatever
  they're actually watching) and `dig_deeper` follow-up (the bull-vs-bear
  inversion metric — a real next question, not a summary). Narration expanded to
  include the "Go deeper: …" line. `beat_id` preserved per rule.
  `ClaudeComposerAsk` shot preserved; `folderLabel` updated to `@NikBearBrown`
  and `runningText` broadened to `paste this into Claude, ChatGPT, or Gemini…`.
  `command` shortened for on-screen legibility while carrying the same asks.
  `estimated_duration_s` bumped 28 → 38 to accommodate the expanded prompt +
  dig-deeper sentence.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle changed
  `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props. Narration kept
  as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in for Bear").

- **Metadata `_variant_todo` removed** (checklist complete). Sheet-level
  `channel_title` and `folderLabel` flipped `@HumanitariansAI` → `@NikBearBrown`
  to match the outro handle.

- **`purpose` line rewritten** for the Teardown lens (now names the mechanism
  and the design choice — "repeatable scenario prep in place of a prediction it
  could not honestly make" — rather than just "in the Plain register").

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls for
   a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The source
   already had `BHTF` at second-to-last position performing the LLM-handoff
   function. Preserve-beat-ids rule wins: kept `BHTF` as the beat_id, adopted
   the `LLM EXERCISE` act name and the `llm_exercise` structured field. No new
   beat inserted; no reorder. Same call the `books--claude-liam-data`
   conversion made.

2. **BCRY (carry-out) quote-vs-narration.** Kept the on-screen `quote` prop
   nearly verbatim from the source carry-out (only tightened the tail: "what
   the report will say" → "what the report is going to say") and mirrored the
   narration to match. The Teardown lift here is the added coda "Ready, not
   predicted." — which is also the existing `sparkLine`, so the beat carries
   its own callback without a visual change.

3. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown section.
   Went with `@NikBearBrown` on both the outro handle and the sheet-level
   `channel_title`/`folderLabel`. `playlist: Claude Basics` kept — series
   identity travels with the source book, not the audience cut.

4. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per the
   shot-blocks preserve rule. Its `bg: #F3EBDD` and `accent: #E4572E` are
   humanitarians-palette colors, but this is a locked visual element (the
   hesitant-writer typing animation) and the timing law binds it to its own
   props. New narration is 34 words — inside the 20–35-word window the note
   requires — and rides the same `predict → preview` correction the typing
   already lands.

5. **`style_preset: humanitarians` and `ground: #F3EBDD` left as scaffold
   wrote them.** Not re-scaffolding was an explicit instruction; `palette`
   is now `teardown` and downstream compile reads that field. The residual
   humanitarians hints only affect the frozen B00 shot props, which are
   supposed to stay.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
