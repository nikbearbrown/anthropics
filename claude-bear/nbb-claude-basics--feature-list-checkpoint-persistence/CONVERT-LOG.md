# CONVERT-LOG — nbb cut of claude-basics--feature-list-checkpoint-persistence

Source: `../claude-basics--feature-list-checkpoint-persistence/beat_sheet.json` (Plain register, hai-simple, 8 beats).
Output: `beat_sheet.nbb.json` (Teardown register, 9 beats — added B_LLM as second-to-last).

## What changed

- **Register**: rewrote every beat's `narration_text` in the Teardown register per `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Voice only — every factual claim (feature_list.json, 200 rows, id + status, git commit per row, feature 51 as first-incomplete, session-2 resuming at 51 and running to 100, the "workspace not memory" carry-out) survives unchanged.
- **Design-critic frame**: B02 now names the design choice ("do not hold the state in memory at all"). B04 now names the trade explicitly ("every read is a disk read, and every commit is friction — slower than in-memory context. What that buys is that no session ever burns tokens rebuilding what a prior one already shipped").
- **Forbidden phrases**: none used. Preferred openers ("Here is what is actually happening…", "Here is the trade this design makes…") replace the plain-register statements.
- **BCRY (carry-out)**: `narration_text` and the WantQuote `quote` prop both rewritten to match — same claim, tightened phrasing. `sparkLine` "The file is the memory." kept (already correct in the Teardown register).
- **B_LLM (new, second-to-last)**: inserted per SKILL.md §Step 3. Ready-to-paste prompt for Claude / ChatGPT / Gemini asks the LLM to design the externalized progress ledger + JSON schema + commit protocol + three-step startup — useful on its own without the video. Dig-deeper follow-up pivots to the parallel-agent race for the same first-incomplete row.
- **BOUT (outro)**: kept the "Persisting Progress Across Context Windows. Liam, in for Bear." OutroCTA line unchanged — already in Teardown-compatible cadence, and it carries the IN-FOR-BEAR sign-off.
- **`_variant_todo`**: removed.
- **`estimated_duration_s`**: nudged upward on B00 (14→18), B01 (15→24), B02 (18→24), B03 (15→20), B04 (18→28), BCRY (11→12) to match the longer Teardown rewrites at Kokoro `am_onyx` cadence. Audio-first: these are estimates; the compile pass replaces them with measured durations.

## Judgement calls

1. **Channel handle stayed `@HumanitariansAI`, not `@NikBearBrown`.** The scaffold (`brand_variant.py`) wrote `channel_title: "@HumanitariansAI"`, `folderLabel: "@HumanitariansAI"`, `playlist: "Claude Basics"`; every sibling `nbb-*` reel in this book (`nbb-claude-basics--screenshot-prompt-caching`, `nbb-financial-services--claude-liam-*`, etc.) does the same. In this tree, `nbb` means "Teardown-register cut of a hai-simple reel" — the register moves, the channel does not. `outro_source: "AUTHOR.MD :: NikBearBrown"` is preserved as attribution/register provenance. If the supervisor intended a channel move (per literal SKILL.md wording), rerun with `folderLabel`/`handle`/`channel_title` swapped — that is a search-and-replace on this sheet, not a rewrite.
2. **B_LLM inserted as a new beat rather than converting BHTF.** BHTF is the "Your Turn" handoff and its narration/composer prompt were already coherent in Teardown register; converting it would have dropped the "Liam, in for Bear" sign-off that belongs on the handoff. New B_LLM lives between BHTF and BOUT so the ordering is BHTF → B_LLM → BOUT, and B_LLM sits precisely second-to-last per the supervisor's done check.
3. **B_LLM `shot.type` = "CARD"** per SKILL.md §Step 3 schema, `source: "own"`, `motion: "hold"`. No `remotion` block, no `graphic` block, no `build`, no `audio_file` — this beat is unrendered by design; the render pass will slate it or render a CARD template.
4. **B00 typed-text prop preserved verbatim.** The `BrutalistHesitantWriter.text` prop is a synced typing animation ("An agent with 200 features / just remembers where it left off. / How does it resume at feature 51, / not feature 1?") with `triggerWords: "remembers"` → `replacementWords: "checks"`. Changing that copy would desync the typing. Narration was rewritten around it in the Teardown register instead.
5. **BHTF composer `command` prop unchanged.** It is the paste-target text the viewer sees on screen and reads aloud with the narrator; rewriting it would break lip-sync with the ClaudeComposerAsk scene.

## Done conditions

- [x] `beat_sheet.nbb.json` is valid JSON.
- [x] Every beat's `narration_text` rewritten in the Teardown register.
- [x] LLM exercise beat is second-to-last (`beats[-2].beat_id == "B_LLM"`).
- [x] Outro is last (`beats[-1].beat_id == "BOUT"`).
- [x] `_variant_todo` removed from `metadata`.
- [x] Voice fields untouched: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam, in for Bear.
- [x] No render / no compile / no audio generation performed.
