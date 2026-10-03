# CONVERT-LOG — nbb cut

Slug: `claude-plugins-official--claude-liam-hook-development`
Converted: 2026-09-03 (register-conversion factory)
Source register: Plain (hai-simple)
Target register: Teardown (Feynman × MKBHD)

## What changed

- **All 7 beats' `narration_text` rewritten in Teardown register.** Voice
  changed; facts unchanged. Every number, event name, timeout, API surface,
  environment variable, and config-format detail from the source survives
  verbatim.
  - B00 cold-open sharpened to "Obvious guess … wrong branch"; kept the
    hesitant-writer trigger/replacement copy exactly (`any` → `only four`) so
    the BrutalistHesitantWriter clip re-renders identically.
  - NB01 recast as machinery + trade-off ("flexibility at the cost of
    determinism" for Prompt-Based; "auditability at the cost of writing bash"
    for Command; who each config format is *for*).
  - NB02 recast as "each rule is a design choice with a cost" —
    parallel/no-hot-swap/case-sensitive/security defaults each named with what
    they buy and what they sacrifice.
  - NB03 names the design cost of the silent failure explicitly ("the loader
    doesn't cross-check event against hook type, so a mismatched pair fails
    silently instead of loudly").
  - BCRY carry-out tightened; the WantQuote `quote` prop updated to match.
  - BOUT rewritten as the NikBearBrown outro line ("Only Four of the Nine —
    Prompt-Based isn't everywhere. Liam, in for Bear.") and the OutroCTA
    `line` prop kept in sync.

- **BHTF converted into the LLM EXERCISE beat (second-to-last).**
  - `act` changed from `"your turn handoff"` → `"LLM EXERCISE"`.
  - Added `llm_exercise` block with `prompt` (paste-ready for
    Claude/ChatGPT/Gemini) and `dig_deeper` follow-up.
  - The prompt reuses the source's four watch-points as numbered checks —
    Prompt-Based vs Command routing (with PostToolUse vs PreToolUse named),
    `CLAUDE_PLUGIN_ROOT` vs hardcoded, plugin hooks.json wrapper vs flat
    settings format, and the post-edit restart. All facts intact.
  - Dig-deeper is a real next question, not a summary: build a Prompt-Based
    hook on PostToolUse, then have the model explain in its own words why it
    won't fire and what one change fixes it.
  - Updated the ClaudeComposerAsk `command` prop to render the paste-ready
    prompt (matching sibling nbb reels).

- **BOUT is the NikBearBrown outro (last).**
  - Kept the Remotion `OutroCTA` pattern used by sibling nbb reels; changed
    `handle` from `@HumanitariansAI` → `@NikBearBrown` per `AUTHOR.MD ::
    NikBearBrown` (default channel).

- **Removed `_variant_todo`** — Steps 2–5 complete.

## Ending order

```
B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (NikBearBrown outro)
```

## Judgement calls

- **`folderLabel` on BHTF (ClaudeComposerAsk):** changed to `@NikBearBrown`
  because it renders on-screen inside the composer chrome and this reel is
  the NBB cut. Metadata `folderLabel` / `channel_title` left at
  `@HumanitariansAI` (source-inherited); those are metadata, not on-screen
  copy. If the intent is that even the metadata should re-brand for the NBB
  channel, that's a scaffolder change, not a conversion change.
- **Duration bumps:** Teardown adds ~20% word count for the design-cost
  clauses. Bumped `estimated_duration_s` on NB01 (30→55), NB02 (30→55),
  NB03 (20→26), BHTF (27→55), B00 (13→15), BOUT (6→7). These are pre-audio
  estimates; `actual_duration_s` will be written back by Kokoro on the next
  render pass and become the master clock.
- **`quote` prop on BCRY kept in sync with the rewritten narration** so
  WantQuote displays the same sentence Liam reads.
- **BOUT `line` prop kept in sync with the rewritten narration** for the
  same reason.
- **BrutalistHesitantWriter typed text (`text`, `triggerWords`,
  `replacementWords`) preserved verbatim** — the on-screen correction is
  the whole point of the cold open and it still fits the Teardown register.
- **Facts:** every technical claim from the source is preserved. No new
  claims were invented; no source claims were dropped.

## Not touched

- Source `beat_sheet.json` (untouched — nbb never modifies source).
- Any media files, audio, or build outputs.
- No render, compile, or audio generation performed.
