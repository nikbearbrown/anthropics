# CONVERT-LOG — books--claude-liam-data → nbb

Source: `anthropics/claude-bear/books--claude-liam-data/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman × MKBHD).
  Every number, name, and claim from the source survives unchanged: the folder
  called Finances, the four kinds of work (explore/clean/visualize/compare),
  the anchor pair (60% : 3 clients, one sliding since September), the monthly
  ritual's six-part checklist, the 40%-of-income concentration example, the
  data + assumptions trustworthiness rule, and the four habits. Voice-only edit
  throughout: revealed the mechanism (formula = encode-question-in-spreadsheet-
  grammar; NLQ = read-columns / infer-intent / run / translate-back), named
  design choices ("hide the machinery, keep the input in English — buys speed,
  costs sight of the exact query"), and judged trade-offs ("confident nonsense
  is worse than no answer, because it looks like a decision").

- **BHTF upgraded to the LLM exercise beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added a
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini) and `dig_deeper` follow-up. Narration expanded to include
  the "Go deeper: …" line. `beat_id` preserved per rule. Shot
  (`ClaudeComposerAsk`) preserved; `folderLabel` updated to `@NikBearBrown`
  and `runningText` broadened to `paste this into Claude, ChatGPT, or
  Gemini…`. `estimated_duration_s` bumped 30 → 34 to accommodate the appended
  dig-deeper sentence.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle changed
  `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props. Narration
  kept as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in for Bear").

- **Metadata `_variant_todo` removed** (checklist complete).
  `channel_title` and `folderLabel` at the sheet level also flipped to
  `@NikBearBrown` for consistency with the outro handle.

- **`purpose` line rewritten** to reflect the Teardown lens (register now
  reads "what does routing the question through a language model actually
  change" rather than "in the Plain register").

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source sheet already had `BHTF` at second-to-last position performing
   the LLM-handoff function. The preserve-beat-ids rule wins: kept `BHTF`
   as the beat_id, adopted the `LLM EXERCISE` act name and the
   `llm_exercise` structured field. No new beat inserted; no reorder.

2. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown
   section — default channel `www.brutalist.art`. Went with
   `@NikBearBrown` on both the outro handle and the sheet-level
   `channel_title`/`folderLabel`. `playlist: Claude Cowork` kept because
   the series identity travels with the plugin book, not the audience cut.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per
   the shot-blocks preserve rule. Its `bg: #F3EBDD` and `accent: #E4572E`
   are humanitarians-palette colors, but this is a locked visual element
   (the hesitant-writer typing animation) and the timing law binds it to
   its own props. New narration is 35 words — inside the 20–35 window
   the note requires.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata
   left as scaffold wrote them.** Not re-scaffolding was an explicit
   instruction; palette is now `teardown` and downstream compile reads
   that field. The residual humanitarians hints only affect the frozen
   B00 shot props, which are supposed to stay.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
