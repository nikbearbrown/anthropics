# CONVERT-LOG — nbb cut

Source: `cwc-workshops--agent-decomposition-skills-vs-tools/beat_sheet.json` (hai-simple, Plain register)
Target: `beat_sheet.nbb.json` (Teardown register, NikBearBrown audience)

## What changed

- **Every narration rewritten in Teardown register** (Feynman × MKBHD): took the
  slow-agent problem apart, explained the actual machinery (what "carrying all of
  it, always" means at the model-call level, what a skill boundary actually is,
  what a subagent's own context window buys), and named the design trade-off
  ("this works if the task has seams; it fails if it doesn't"). Facts unchanged
  — 402 lines, 12 tools, 102 calls, 488s, 5x, ~100s, 3 scripts, 15-line core,
  five skill modules (reorder policy, forecasting, notifications, vendor lookup,
  audit logging), 200-line forecasting sub-prompt — every number and label
  survives verbatim.
- **BHTF elevated to formal LLM EXERCISE beat.** Beat already carried a
  paste-ready prompt in ClaudeComposerAsk; formalised it with the
  `llm_exercise` object (`prompt` + `dig_deeper`) per SKILL.md §Step 3. Kept the
  ClaudeComposerAsk shot — it's the paste-into-Claude-composer visualisation and
  a better renderer than a generic CARD for an LLM exercise. Updated
  `folderLabel` to `@NikBearBrown` and the composer topic/segment to reflect
  the LLM-exercise role.
- **BOUT stays as outro (LAST).** Kept `OutroSeries` shot; swapped the eyebrow
  handle from `@HumanitariansAI` to `@NikBearBrown` to match the nbb channel
  identity. Line stays as title + "Liam, in for Bear." — no AUTHOR.MD in
  `claude-bear/` with a NikBearBrown section, so followed the pattern the
  neighbouring `nbb-cwc-workshops--claude-liam-reorder-policy` reel used.
- **`_variant_todo` removed** from metadata.
- **`purpose` field updated** to reflect the Teardown cut (was still describing
  the Plain-register redo).

## Judgement calls

- **BCRY carry-out left verbatim.** "Faster agents don't know less — they load
  only the knowledge each task actually needs, exactly when it needs it." is
  already Teardown-shaped (design philosophy, takes the wrong guess apart, no
  forbidden phrases) and the `WantQuote` prop renders it on-screen. Rewriting
  it would force the prop to change too and would weaken a sentence that is
  already the reel's thesis. Same treatment the neighbouring reference reel
  gave its BCRY.
- **B00 narration lengthened by 3 words** (27 → 30). The BrutalistHesitantWriter
  cold open needs ≥9s of typing window (TIMING LAW in the note); the extra
  words keep the audio comfortably in that band. `note` field updated
  accordingly.
- **BHTF `act` renamed** from `"your turn handoff"` to `"LLM EXERCISE"` to
  match the beat's new formal role. `beat_id` preserved.
- **No new beat inserted.** SKILL.md §Step 3 says "insert an LLM exercise
  beat as SECOND-TO-LAST." BHTF was already SECOND-TO-LAST and already
  functionally an LLM exercise beat (paste-ready prompt rendered in a Claude
  composer). Elevated it in place rather than inserting a duplicate. Ending
  order verified: `… B11 → BCRY → BHTF (LLM exercise) → BOUT (outro)`.
