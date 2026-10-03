# CONVERT-LOG — financial-services--claude-liam-deal-sourcing → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-deal-sourcing/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Every number, name, file path, and claim from the source survives
  unchanged: deal-sourcing is a folder holding one SKILL.md; three steps in
  order — search sector / check CRM / draft founder outreach; the anchor pair
  (B03 plants the single-file checklist, B06 pays it off); B07's twin
  demonstrations (twenty candidates surfaced ≠ good investments; clean email
  drafted ≠ founder reply). Voice-only edit throughout: revealed the mechanism
  (skills live in a document, not in the weights; the same routine every run
  because it's the same document every run), named the design choice ("they
  optimized for guaranteed consistency at the expense of guaranteed judgment"),
  and drew the trade-off line ("ran-the-step and worked are two different
  claims"; "the mechanism is the checklist; the mechanism is not the taste
  that would rank the results").

- **BHTF upgraded to the LLM exercise beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added a
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini, generalized to any repeatable search-and-outreach routine)
  and `dig_deeper` follow-up (which step actually requires judgment that isn't
  on the page — the seam between the checklist and you). Narration expanded
  to include the "Go deeper: …" line. `beat_id` preserved per rule. Shot
  (`ClaudeComposerAsk`) preserved; `folderLabel` updated to `@NikBearBrown`,
  `runningText` broadened to `paste this into Claude, ChatGPT, or Gemini…`,
  and `command` rewritten to match the paste-ready `llm_exercise.prompt`.
  `estimated_duration_s` bumped 21 → 36 to accommodate the fuller prompt +
  dig-deeper appendage.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle changed
  `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props. Narration
  kept as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in for Bear").

- **BCRY (carry-out) narration preserved verbatim.** The on-screen `WantQuote`
  props render that exact sentence, and it already reads clean in the Teardown
  register (mechanism + judgment split, plain enough for a card). Rewriting
  the narration would have desynced it from the rendered quote for no
  register gain.

- **Metadata `_variant_todo` removed** (checklist complete).
  `channel_title` and `folderLabel` at the sheet level also flipped to
  `@NikBearBrown` for consistency with the outro handle.

- **`purpose` line rewritten** to reflect the Teardown lens (register now
  reads "what does the word 'skill' actually add to Claude" and names the
  design choice — guaranteed checklist execution at the expense of any
  investment judgment about the results — rather than the Plain-register
  framing of the source).

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source sheet already had `BHTF` at second-to-last position doing the
   LLM-handoff. The preserve-beat-ids rule wins: kept `BHTF` as the
   beat_id, adopted the `LLM EXERCISE` act name and the structured
   `llm_exercise` field. No new beat inserted; no reorder. Matches the
   sibling `nbb-books--claude-liam-data` precedent.

2. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown
   section — default channel is the NikBearBrown identity. Went with
   `@NikBearBrown` on both the outro handle and the sheet-level
   `channel_title`/`folderLabel`. `playlist: Claude Basics` kept because
   the series identity travels with the topic ("what is a skill?"), not
   the audience cut.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per
   the shot-blocks preserve rule. Its `bg: #F3EBDD` and `accent: #E4572E`
   are humanitarians-palette colors, but this is a locked visual element
   (the hesitant-writer typing animation, correction 'decides' → 'finds')
   and the timing law binds it to its own props. New narration is 33 words
   — inside the 20–35 window the note requires.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata
   left as scaffold wrote them.** Not re-scaffolding was an explicit
   instruction; `palette: teardown` is the field the downstream compile
   reads. The residual humanitarians hints only affect the frozen B00 shot
   props, which are supposed to stay.

5. **LLM exercise generalized past finance.** The source's handoff already
   used "sourcing candidates for anything, not just deals" — kept that
   generalization and made it the spine of both the paste-ready prompt and
   the ClaudeComposerAsk `command`. The dig-deeper question ("which step
   actually requires judgment that isn't on the page") is the video's
   central claim turned into a self-audit — genuinely explorable, not a
   summary of what was said.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
