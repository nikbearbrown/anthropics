# CONVERT-LOG — Plain → Teardown (nbb) for `claude-plugins-official--claude-liam-claude-md-improver`

Converted `beat_sheet.json` (Plain, hai-simple) into `beat_sheet.nbb.json`
(Teardown, NBB). Voice only — facts, beat IDs, shot blocks, and on-screen
card copy preserved one-for-one. `_variant_todo` removed.

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD): each beat now names the mechanism, names what the design was
  optimized for, and where useful names the trade-off — "Here's what's
  actually happening…", "They optimized for measurement before mutation",
  "They optimized for consent over speed", "This works if you value X; it
  fails if you need Y." Every fact from the source survives — the five
  discovery locations, the six scoring criteria, the A–F grade, the
  phase order, the fifty-file cap, the silent skip. Nothing invented.
- **BHTF converted to the LLM EXERCISE beat** (already the second-to-last
  beat and already a paste-ready ask). Changed `act` from "your turn
  handoff" → "LLM EXERCISE"; added the structured `llm_exercise` field
  (`prompt` + `dig_deeper`); rewrote the paste-ready prompt so it produces
  a useful output on its own without the video (a five-question CLAUDE.md
  drafting + six-criteria self-grade); added a real "Go deeper: …"
  follow-up. Broadened the ask surface from "Paste this into Claude" to
  "Claude, ChatGPT, or Gemini" per SKILL.md §Step 3 (paste-into-any-
  frontier-LLM prompt, not a CLI command). Updated `runningText`
  accordingly. Kept the `ClaudeComposerAsk` shot block, kept the beat_id,
  kept `folderLabel: @HumanitariansAI`. Bumped `estimated_duration_s`
  from 22 → 45 to cover the longer prompt + dig-deeper line.
- **BCRY narration kept verbatim.** The source carry-out is the exact
  line signed off in `CARRY-OUT.md` — and it already reads in the
  Teardown register (names the design decision — "before it touches a
  single line", "diff with a reason, never a silent rewrite"). Rewriting
  it would fabricate variance without changing meaning.
- **BOUT kept verbatim** (`"It Scores Before It Edits. Liam, in for
  Bear."`) — already the standard NBB signoff line, in for Bear per
  IN-FOR-BEAR LAW. `OutroSeries` shot block preserved from source per
  the "preserve shot blocks" rule.
- **B00 cold-open** rewritten around the `rewrite → score` correction
  that is hard-wired into `BrutalistHesitantWriter` (`triggerWords:
  "rewrite"` / `replacementWords: "score"`) — the pivot words stay
  intact so the audio-visual sync survives, only the surrounding
  framing shifts to Teardown ("Here's what's actually happening…").
  Kept within the 20-35-word timing window per the note.
- **Metadata `purpose`** updated "Plain register" → "Teardown register"
  to reflect what the beat sheet now is.
- **`estimated_duration_s` bumps** for the three mechanism beats
  (NB01 26→34, NB02 24→30, NB03 16→22) to reflect longer Teardown
  narrations at the source's word-rate. These are just estimates; the
  real clock is `actual_duration_s` after Kokoro measures the audio.

## Judgement calls

1. **Kept BHTF instead of inserting a separate `B_LLM` beat.** SKILL.md
   §Step 3 shows an idealised `beat_id: "B_LLM"` schema, but the
   invocation also demands "preserve every `beat_id`" and the source
   already has a second-to-last "paste this into Claude" beat.
   Every sibling `nbb-*` sheet in `claude-bear/` follows the same
   pattern (see `nbb-books--claude-liam-what-plugins-are`,
   `nbb-financial-services--*`, etc.) — BHTF *is* the LLM exercise beat.
   Kept the beat_id, attached the `llm_exercise` structured field.

2. **Kept `OutroSeries` (source pattern) instead of switching to
   `OutroCTA` (sibling pattern).** Several sibling `nbb-*` sheets
   switched their outros to `OutroCTA` with `line` + `handle`, but the
   SKILL.md explicitly names both `OutroSeries` / `OutroCTA` as valid
   NBB outro renderers and the invocation says preserve shot blocks
   where they still fit the register. `OutroSeries` with
   `eyebrow: "CLAUDE MD IMPROVER · @HumanitariansAI"` + `line: "It
   Scores Before It Edits."` fits. Not switching unilaterally.

3. **Kept `folderLabel` / `channel_title` / `handle` at
   `@HumanitariansAI` even though `audience: NikBearBrown`.** The
   scaffold set them that way (inherited from source), and every
   sibling `nbb-*` in this `claude-bear/` tree follows the same
   convention: NBB register, HAI channel. Not touching the
   book-series convention on a single reel.

4. **Reused the six-criteria rubric as the spine of the LLM exercise
   prompt.** The prompt has the viewer draft a CLAUDE.md, then grade
   it A–F against the exact same six criteria the source names
   (commands documented, architecture clarity, non-obvious patterns,
   conciseness, currency, actionability). That way the exercise
   teaches the rubric itself — not just the plugin's existence — and
   still produces a useful output on its own without the video.

## Order verified

```
B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (NBB outro)
```

7 beats, matches source beat_ids one-for-one.

## Not done here

Not rendered. No audio regenerated, no compile, no publish. Deliverable
is `beat_sheet.nbb.json` only, per the register-conversion factory
contract.
