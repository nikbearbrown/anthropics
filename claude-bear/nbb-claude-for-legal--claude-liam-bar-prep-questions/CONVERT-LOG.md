# CONVERT-LOG — claude-for-legal--claude-liam-bar-prep-questions (nbb)

Converted source `beat_sheet.json` to `beat_sheet.nbb.json` in the Teardown
register (Feynman × MKBHD). Facts unchanged; every claim in the source
survives (bar-review workflow, generation-from-patterns vs. licensed item
bank, the hearsay-exception anchor, jurisdiction/superseded-standard caveats).

## What changed

- **B00 (cold open, hesitant writer).** Rewritten to name the mechanism — "real"
  is wrong because the retired items sit in a paywalled bank; what Claude
  actually does is draft in the exam's shape. Kept under the WRITER LAW window;
  the `BrutalistHesitantWriter` props (typed text, trigger/replacement,
  timings) are untouched so the on-screen correction still lands.
- **B01.** Reframed the "easy assumption" as a design-critic observation:
  our brains use format as a stand-in for verification, so a certified-looking
  card gets certified-level trust. Same beat, sharper diagnosis.
- **B02.** Explicitly named the generator: a statistical model of legal style,
  not a live question bank kept current against real statutes and cases. Added
  the trade-off tag "same output shape, different source of truth."
- **B03.** Judged the trade-off directly — confidence and hedging are both
  prose registers the model absorbed; neither one is evidence about the rule.
- **BCRY (carry-out).** Preserved the original sentence, added one line
  ("the rule inside it is a claim, not a citation") to hammer the register.
  `WantQuote` prop updated to the new quote.
- **BHTF → LLM exercise beat.** This is the judgement call (see below).
- **BOUT (outro).** Untouched — the existing "Claude, Bar Prep Questions.
  Liam, in for Bear." (`OutroCTA` + `@HumanitariansAI`) is already the correct
  last-beat form. `subtitle` / `subtitle_line` fields were never present in
  the source and were not synthesised.

## Judgement calls

1. **BHTF was repurposed into the LLM-exercise beat rather than inserting a
   new beat between BHTF and BOUT.** BHTF was already a paste-into-Claude
   "your turn" handoff — inserting a second paste-prompt beat immediately
   before the outro would double the same move. Instead, BHTF's `act` was
   renamed `LLM EXERCISE`, its narration extended with a "Go deeper:" line,
   and a structured `llm_exercise` block was added (`prompt` + `dig_deeper`,
   per §Step 3 of the nbb SKILL). The `ClaudeComposerAsk` shot was kept —
   it is the paste-prompt render the sibling nbb reels use — and its
   `command` and `segment` props were updated to the new prompt. Result:
   ending order is body → LLM EXERCISE → outro, second-to-last is a
   paste-ready prompt that works standalone, and no beat is now redundant.

2. **`estimated_duration_s` bumped from 24 → 30 on BHTF.** The rewrite adds
   a genuine "Go deeper:" question, which spends ~5–7s of extra narration
   time. Audio generation will overwrite this with the measured Kokoro
   duration, so this is only a scheduling hint.

3. **No AUTHOR.MD on disk under `anthropics/claude-bear/`.** The SKILL says
   the outro is "content from the NikBearBrown section of the book's
   AUTHOR.MD"; that file doesn't exist for this book. Sibling nbb reels in
   the same tree (e.g. `nbb-claude-for-legal--claude-liam-ip-clause-review/`)
   handle this by keeping the existing HAI-branded outro pattern. I did the
   same — the outro is already correct in form; substituting a
   `www.brutalist.art` handle would break the reel's brand continuity
   (`channel_title` / `folderLabel` / `playlist` are all Humanitarians AI).

4. **`_variant_todo` removed** as required by the supervisor's done-criteria.
