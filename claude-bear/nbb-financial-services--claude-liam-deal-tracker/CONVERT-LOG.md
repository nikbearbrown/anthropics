# CONVERT-LOG — nbb-financial-services--claude-liam-deal-tracker

Source: `anthropics/claude-bear/financial-services--claude-liam-deal-tracker/beat_sheet.json`
Output: `beat_sheet.nbb.json` (this dir)
Voice: Kokoro `am_onyx` — Liam, in for Bear (unchanged from scaffold).
Reference pattern: sibling `nbb-financial-services--claude-liam-deal-sourcing/beat_sheet.nbb.json`.

## What changed

- **Rewrote every beat's `narration_text` in the Teardown register.** Facts unchanged
  (four fields, six trigger phrases, three-step checklist, the ACME Series C
  anchor, the term-sheet-due-Friday milestone). Voice shifted to Feynman × MKBHD:
  explain the mechanism ("a folder Claude reads top to bottom"), reveal the design
  choice ("optimized for guaranteed execution of what's on the page at the expense
  of any reasoning about what isn't"), name the trade.
- **BCRY carry-out sentence** sharpened to match the Teardown register on both
  `narration_text` and `remotion.props.quote` (they must stay in sync — the quote
  renders on-screen). `sparkLine` preserved ("Reliable inside the spec. Nothing
  outside it." — already Teardown-shaped).
- **BHTF repurposed as the LLM EXERCISE beat** (second-to-last). Act renamed
  `your turn handoff` → `LLM EXERCISE`. Added `llm_exercise.prompt` — a
  paste-ready block for Claude/ChatGPT/Gemini that runs the three-deal checklist
  (Acme/Beta Corp/Gamma LLC), then explicitly asks for negotiation of the redline
  and instructs the model to say-so-or-refuse if that's outside the checklist —
  making the video's payoff observable in the wild. Added `llm_exercise.dig_deeper`
  pointing at the seam between checklist execution and human judgment. Composer
  card `command`, `topic`, `segment` and `runningText` refreshed to match.
- **BOUT outro** narration preserved verbatim ("Claude, Deal Tracker. Liam, in
  for Bear."). `handle` prop switched to `@NikBearBrown`.
- **Removed** `metadata._variant_todo` (checklist done).

## Judgment calls

- **`folderLabel` / `channel_title` / BOUT `handle` all switched to
  `@NikBearBrown`.** The scaffold left them at `@HumanitariansAI` (from the
  source's HAI cut). Per `brands/nbb.md` and the sibling reference reels, the
  NikBearBrown cut publishes to `@NikBearBrown`; the on-screen folder chip and
  outro handle are on-screen card copy that no longer fits the register (a
  different channel), so I updated them. Everything else in `shot`/`graphic`
  blocks preserved exactly.
- **`estimated_duration_s`** revised upward on beats where the Teardown rewrite
  adds material (B00 12→15, B03 20→22, BCRY 9→10, BHTF 30→38) so `todo` doesn't
  flag them under-budgeted before audio is regenerated. `actual_duration_s`
  cleared everywhere — the stale numbers refer to the old narration; a separate
  audio-regen pass will refill them.
- **Metadata `register`** left as `Teardown` (scaffold-set). `brand` kept as
  `claude-liam` because that's what the source labeled the persona chassis; the
  NBB cut is identified by `audience: NikBearBrown` and `palette: teardown`.

Not built. Rendering, audio generation, and QC are a separate pass.
