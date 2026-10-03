# CONVERT-LOG — claude-for-legal--claude-liam-handbook-updates → nbb

## What changed

- Rewrote all seven `narration_text` values in the Teardown register (Feynman × MKBHD): name the design choice, name what it optimizes for, name the trade-off. Facts, beat ids, act labels, shot blocks, and Manim/Remotion scene ids preserved unchanged.
- Repurposed `BHTF` as the LLM exercise beat (act now `LLM EXERCISE`). Added the `llm_exercise` object per `skills/make/nbb/SKILL.md §Step 3`:
  - `prompt` — a paste-ready, four-part audit prompt for one handbook policy, useful on its own without the video.
  - `dig_deeper` — a "Go deeper" follow-up about which policy is highest-risk if silently stale and how to migrate it off calendar-based review first.
- Updated the `ClaudeComposerAsk` `command`/`segment`/`runningText` props on `BHTF` so the on-screen composer matches the paste-ready prompt viewers hear.
- Bumped `BHTF.estimated_duration_s` from 26 → 30 to fit the added "Go deeper" line (source's `actual_duration_s` of 17.64 is stale relative to the new narration; audio regen will set the true clock).
- Swapped `BOUT` Remotion pattern `OutroCTA` → `OutroSeries` (`eyebrow` + `line`) to match the NikBearBrown outro convention already in use on the sibling reel `nbb-claude-for-legal--claude-liam-ip-clause-review`.
- On the carry-out `BCRY.WantQuote`, normalized the em-dash so the quoted card copy uses a real `—` instead of the source's `--` (register + typography consistency; the sentence itself is unchanged).
- Removed `_variant_todo` from metadata (task complete).
- Left the CarryOut sentence itself verbatim — it is already Teardown-shaped and appears on the WantQuote card, so the on-screen copy stays exactly aligned with what Liam reads.

## Judgement calls

- **BHTF = the LLM exercise beat, not a new inserted beat.** The source already had a `your turn handoff` beat second-to-last whose whole job was to voice a paste-ready Claude prompt. Inserting a second, structurally-identical beat would double the outro ramp and confuse the composition slot. The sibling `nbb-claude-for-legal--claude-liam-ip-clause-review` reel takes the same approach (BHTF as the exercise slot, no separate `B_LLM`), so this matches established nbb convention in this book. The `llm_exercise` object was still added inline so the SKILL.md schema is honored.
- **Channel handle kept `@HumanitariansAI`.** `outro_source: AUTHOR.MD :: NikBearBrown` refers to the NBB *outro format* (title recap + eyebrow, OutroSeries) rather than a channel-swap; the sibling nbb reel keeps `folderLabel/channel_title/eyebrow` on the source channel and this one follows suit.
- **Facts unchanged, voice only.** The reconstructed spring paid-leave anchor, the December review straw-man, the two failure modes (flagged ≠ finished, quiet ≠ complete), and the carry-out remain exactly as the source reported them.
