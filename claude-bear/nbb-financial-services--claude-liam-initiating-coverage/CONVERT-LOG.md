# CONVERT-LOG — financial-services--claude-liam-initiating-coverage → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-initiating-coverage/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD), except `BCRY` (see judgement call 1). Every fact from the source
  survives unchanged: the workflow is five fixed tasks in order (company
  research → financial model → valuation analysis → chart generation → final
  report assembly); deliverables are markdown / Excel / valuation from that
  Excel / charts / DOCX; each task refuses to start until the deliverable
  before it exists on disk and has been verified; tasks 3–5 depend on the
  outputs of earlier tasks. Voice-only edit throughout — revealed the
  mechanism ("task three's input isn't optional — it's task two's output"),
  named the design choice ("they optimized for guaranteed order at the expense
  of guaranteed judgment"), and drew the trade-off line ("verification checks
  that the file exists and has the right shape, not that the numbers are
  wise"; "blocked is a sequencing gap, not evidence the earlier research was
  wrong"). Anchor B02 → B03 (one ticker's coverage package through the five
  tasks, then resting at REPORT) preserved by the on-screen graphics; the new
  narration explicitly names it going in and pays it off coming out.

- **BHTF upgraded to the LLM EXERCISE beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added a
  structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini — three ordered tasks: research, project, value; then a
  second run that skips step two, so the viewer sees the dependency break)
  and `dig_deeper` follow-up (which of the three steps was analytical work
  worth trusting with real money, and which was paperwork any ordered chain
  could have produced — the seam between running the tasks and being right).
  Narration expanded to include the "Go deeper: …" line at the end. `beat_id`
  preserved per rule. Shot (`ClaudeComposerAsk`) preserved; `folderLabel`
  changed `@HumanitariansAI` → `@NikBearBrown`, `runningText` broadened to
  `paste this into Claude, ChatGPT, or Gemini…`, and `command` rewritten as a
  compressed version of the paste-ready `llm_exercise.prompt`.
  `estimated_duration_s` bumped 26 → 42 to accommodate the fuller prompt +
  dig-deeper appendage.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Handle changed
  `@HumanitariansAI` → `@NikBearBrown` on the `OutroCTA` props. Narration
  kept as-is — already IN-FOR-BEAR-LAW compliant ("Liam, in for Bear") and
  reads the title cleanly.

- **BCRY (carry-out) narration preserved verbatim.** The on-screen
  `WantQuote` props render that exact sentence, and it already reads clean in
  the Teardown register (mechanism + judgment split, plain enough for a
  card). Rewriting the narration would have desynced it from the rendered
  quote for no register gain.

- **Metadata `_variant_todo` removed** (checklist complete). Sheet-level
  `channel_title` and `folderLabel` also flipped to `@NikBearBrown` for
  consistency with the outro handle.

- **`purpose` line rewritten** for the Teardown lens — now names the
  design choice ("guaranteed order at the expense of guaranteed judgment")
  and the both-directions payoff ("a finished report proves the chain ran,
  not that the assumptions inside it are sound") rather than the Plain-
  register framing of the source.

- **`estimated_duration_s` bumped on beats whose narration lengthened**:
  B01 25 → 27, B02 24 → 28, B03 27 → 33, BHTF 26 → 42. B00 kept at 13
  (word count 33, inside the 20–35 window the WRITER LAW note pins).
  BCRY and BOUT untouched (narration preserved verbatim).

## Judgement calls

1. **BCRY preserved verbatim.** The `WantQuote` prop's `quote` field is the
   on-screen text and the narration is the read of that text; they must
   match. The source sentence is already Teardown-clean — mechanism first,
   trade-off named — so no rewrite. Same call as the sibling
   `nbb-financial-services--claude-liam-deal-sourcing`.

2. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source sheet already had `BHTF` at second-to-last position doing the
   handoff. The preserve-beat-ids rule wins: kept `BHTF` as the beat_id,
   adopted the `LLM EXERCISE` act name and the structured `llm_exercise`
   field. No new beat inserted; no reorder. Matches the
   `nbb-financial-services--claude-liam-deal-sourcing` precedent.

3. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown
   section — default channel is the NikBearBrown identity. Went with
   `@NikBearBrown` on both the outro handle and the sheet-level
   `channel_title`/`folderLabel`. `playlist: Claude Basics` kept because the
   series identity travels with the topic ("what does 'initiating coverage'
   actually run?"), not the audience cut.

4. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per the
   shot-blocks preserve rule. Its `bg: #F3EBDD`, `accent: #E4572E`, and the
   trigger/replacement pair (`instantly` → `five ordered tasks`) are the
   locked visual gag; the new narration re-lands that same reveal in words
   ("It isn't — it's a five-task chain, dependency-gated"). Word count 33 —
   inside the 20–35 window the note pins.

5. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata left
   as scaffold wrote them.** Not re-scaffolding was an explicit instruction;
   `palette: teardown` is the field the downstream compile reads. The
   residual humanitarians hints only affect the frozen B00 shot props,
   which are supposed to stay.

6. **LLM exercise generalized past the source's specific ask.** Source
   BHTF asked the viewer to pick one company and run three ordered tasks
   plus a break-it second run. Kept that spine but tightened the paste-ready
   `prompt` — specifies two valuation methods (DCF and comparable-multiple)
   and asks the model to reconcile them, so the third step is doing real
   analytical work and the "skip step two" break is more concrete. The
   dig-deeper question ("which step was analytical work you'd trust with
   real money, which was paperwork any ordered chain could have produced")
   is the video's central claim — order guaranteed, judgment not —
   turned into a self-audit. Genuinely explorable; not a summary.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
