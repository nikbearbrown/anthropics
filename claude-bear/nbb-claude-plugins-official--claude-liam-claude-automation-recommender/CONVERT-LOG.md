# CONVERT-LOG — claude-plugins-official--claude-liam-claude-automation-recommender

nbb conversion of source `beat_sheet.json` → `beat_sheet.nbb.json`.
Voice-only rewrite in Teardown register (Feynman × MKBHD). Facts unchanged;
every beat_id, act, shot, and on-screen card copy preserved. `_variant_todo`
removed.

## Rewrites (narration only)

- **B00 (cold open).** Trimmed original narration and added the IN-FOR-BEAR
  sign-in ("Liam here, in for Bear.") at the front. Final word count: 26,
  inside the 20–35-word BrutalistHesitantWriter budget the note guards. The
  typed-text prop (`text`, `triggerWords: build → recommend`) is untouched.
- **NB01 (five automation types).** Opened with "Here's what's actually
  happening." Reframed the closing summary as "Five slots, five triggers,
  five scopes. The design forces you to pick the right shape…" — a
  design-critic beat that lands where the original just listed. All five
  types, triggers, and worked examples preserved verbatim.
- **NB02 (three phases + cap).** Renamed "The skill works in three phases"
  as "The mechanism is three phases" and added a Teardown coda naming the
  trade-off ("optimized for signal density over completeness — the cap is
  the design's honest answer to the fact that you don't need every possible
  automation, you need the two that actually pay off"). Phase list, config
  signals, and the three worked signal→pick examples all preserved.
- **NB03 (the catch).** Opened with "Here's the catch, and it's a design
  decision, not a bug." Added the "This works if you value X; it fails if
  you need Y" pair explicitly, and closed with "…yours to close, on
  purpose." Every technical claim (subagent template, plugin install
  lookup, read-only end to end) preserved.
- **BCRY (carry-out).** Narration kept identical to the source, because it
  IS the on-screen `WantQuote` quote prop — the visual and audio have to
  match, and the source line already reads in Teardown-clean prose.
- **BHTF (your turn handoff).** Teardown pass; command
  (`Analyze this codebase and recommend Claude Code automations.`) and the
  two follow-up checks (subagent template? plugin install command?) all
  preserved verbatim. Reworked the closing sentence to
  "The gap between the recommendation and the runnable step is where the
  design lives."
- **BOUT (outro).** Kept as-is. It already reads
  "Recommend, Not Install. Liam, in for Bear." — the IN-FOR-BEAR sign-off
  the SKILL requires; `OutroSeries` pattern in the teardown palette matches
  the brand spec.

## New beat (second-to-last)

- **B_LLM (LLM EXERCISE).** Inserted between BHTF and BOUT per SKILL.md
  §Step 3. Shot is a `CARD` (source: own, motion: hold) that will render
  in the teardown palette. Voice is Kokoro `am_onyx` (Liam, in for Bear).
  - `llm_exercise.prompt` — a paste-ready block asking any frontier LLM
    (Claude / ChatGPT / Gemini) to take Claude Code's five extension types
    apart on their own terms: trigger, scope, right-choice case,
    better-fit case, trade-off. Produces a useful output without needing
    the video.
  - `llm_exercise.dig_deeper` — a genuine follow-up: design a sixth
    automation type that fills a gap the current five don't cover, and
    name what you'd have to sacrifice to fit it in.

## Judgement calls

- **BHTF vs B_LLM (do we need both?).** BHTF already reads as a paste-into-
  Claude call-to-action tied to *your own* codebase. B_LLM is a distinctly
  broader prompt tied to *the topic itself* (understanding the five
  extension types), with a "Go deeper" follow-up. Kept both because SKILL
  §Step 3 is explicit about the second-to-last slot and the two prompts
  do different work: BHTF is "test this in your project," B_LLM is
  "understand the design space." Facts unchanged in either.
- **AUTHOR.MD :: NikBearBrown not present in this book.** Outro pattern
  (`OutroSeries`) and copy (`Recommend, Not Install.` /
  `Liam, in for Bear.`) match the sibling nbb reels in this book already
  and satisfy the IN-FOR-BEAR sign-off. `outro_source` in metadata still
  reads `AUTHOR.MD :: NikBearBrown` — that's the scaffold's declared
  provenance, and it stays so a later AUTHOR.MD pass can re-derive the
  copy without a schema change.
- **`palette` set to `teardown`; `style_preset`/`ground`/`folderLabel`/
  `channel_title` left on their HAI values.** Same pattern the other
  converted nbb reels in this directory use — the register/palette flip
  is the nbb-cut; the channel-level metadata stays with the source
  channel until an explicit re-channel pass says otherwise.

## Not touched

- No rendering, no audio generation, no compile. This pass writes one
  file: `beat_sheet.nbb.json`.
- Source `beat_sheet.json` untouched.
- Every `beat_id`, `act`, `shot`, `graphic`, and Remotion prop preserved
  exactly for the six carried-over beats.
