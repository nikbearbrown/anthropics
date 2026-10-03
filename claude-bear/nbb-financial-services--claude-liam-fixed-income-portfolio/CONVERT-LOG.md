# CONVERT-LOG — financial-services--claude-liam-fixed-income-portfolio → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-fixed-income-portfolio/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Voice-only edit — every number, name, and mechanism claim from the
  source is preserved verbatim: DV01 is the dollar change per one basis point
  move; the skill sums DV01 across each bond; a hundred-basis-point shock as
  the worked example; scenario analysis resizes the shock; the two limits (a
  large DV01 can be an intentional hedge, a small one doesn't mean rate-safe
  under a bigger move or a non-parallel curve shift); inputs are coupon,
  maturity, current price. The register work: reveal the mechanism ("it reads
  three numbers, then runs the math"), name the design choice ("they built a
  calculator, not a critic"; "arithmetic on inputs you control, at the expense
  of any view on whether the shock you picked is the one that matters"), name
  the limit ("which scenarios matter is judgment it doesn't have"). No new
  factual claim was introduced.

- **BHTF upgraded to the LLM exercise beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added a
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini — a specific, self-contained brief that asks the LLM to
  compute duration and DV01 on a three-bond book, stress-test a 100 bp shift
  both directions, then double the shock; opens with the model stating in one
  sentence what DV01 does and does not tell you about risk) and `dig_deeper`
  follow-up (which of the two inputs — the bonds you picked, or the shock you
  specified — you trust the least, and why that judgment matters more than
  the number the arithmetic spits back). Narration expanded to include the
  "Go deeper: …" line and retains the closing "Liam, in for Bear."
  `beat_id` preserved per rule. Shot (`ClaudeComposerAsk`) preserved;
  `folderLabel` updated to `@NikBearBrown`, `runningText` broadened to
  `paste this into Claude, ChatGPT, or Gemini…`, and `command` rewritten to
  match the paste-ready `llm_exercise.prompt`. `estimated_duration_s` bumped
  24 → 40 to accommodate the fuller prompt + dig-deeper appendage.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle changed
  `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props. Narration
  kept as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in for Bear").

- **BCRY (carry-out) narration preserved verbatim.** The on-screen `WantQuote`
  props render that exact sentence, and it already reads clean in the Teardown
  register (mechanism + judgment split, plain enough for a card). Rewriting
  the narration would have desynced it from the rendered quote for no
  register gain.

- **B00 (hesitant writer cold open) narration rewritten inside the TIMING
  LAW window** (20–35 words — landed at 34). Preserves the locked
  `BrutalistHesitantWriter` shot props exactly (typing "What decides / a
  portfolio's risk — / judgment?" and correcting `judgment` → `the numbers`).
  Adds Liam's cold-open identifier ("Liam here, in for Bear — let's take the
  skill apart") to signal both IN-FOR-BEAR LAW and the Teardown lens up front.

- **Metadata `_variant_todo` removed** (checklist complete).
  `channel_title` and `folderLabel` at the sheet level also flipped to
  `@NikBearBrown` for consistency with the outro handle.

- **`purpose` line rewritten** to reflect the Teardown lens. Reads as
  mechanism + design choice + trade-off now ("built a calculator that runs
  the arithmetic the same way every time, at the expense of any opinion
  about whether the shock you picked or the holdings you handed it are the
  right ones") rather than the Plain-register framing of the source.

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source sheet already had `BHTF` at second-to-last position doing the
   your-turn handoff. The preserve-beat-ids rule wins: kept `BHTF` as the
   beat_id, adopted the `LLM EXERCISE` act name and the structured
   `llm_exercise` field. No new beat inserted; no reorder. Matches the
   sibling `nbb-financial-services--claude-liam-deal-sourcing` precedent.

2. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown
   section — default channel is the NikBearBrown identity. Went with
   `@NikBearBrown` on both the outro handle and the sheet-level
   `channel_title` / `folderLabel`. `playlist: Claude Basics` kept because
   the series identity travels with the topic ("what is Claude actually
   computing when you install this skill?"), not the audience cut.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per
   the shot-blocks preserve rule. Its `bg: #F3EBDD` and `accent: #E4572E`
   are humanitarians-palette colors, but this is a locked visual element
   (the hesitant-writer typing animation, correction `judgment` → `the
   numbers`) and the timing law binds it to its own props. New narration
   is 34 words — inside the 20–35 window the note requires.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata
   left as scaffold wrote them.** Not re-scaffolding was an explicit
   instruction; `palette: teardown` is the field the downstream compile
   reads. The residual humanitarians hints only affect the frozen B00 shot
   props, which are supposed to stay.

5. **LLM exercise built to run without the video.** The paste-ready
   `prompt` opens by asking the model to say in one sentence what DV01
   does and does not tell you about risk before it computes — that framing
   forces the mechanism-vs-judgment split that is the video's carry-out to
   surface in the model's own answer, so the exercise stands on its own
   for a viewer who never watched the reel. The `dig_deeper` question is
   genuinely explorable: it asks the viewer to interrogate which of their
   two inputs (holdings vs shock) they least trust — the seam the arithmetic
   cannot cross.

6. **Kept BCRY narration verbatim over Teardown rewrite.** BCRY's
   `WantQuote` renders the narration string as the on-screen card. A
   Teardown-register rewrite of the narration would have desynced audio
   from the card. The source's carry-out sentence already lands the
   mechanism-vs-judgment split cleanly — no rewrite earned its keep.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
