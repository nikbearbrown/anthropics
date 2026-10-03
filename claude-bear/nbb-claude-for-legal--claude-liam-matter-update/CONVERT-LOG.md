# CONVERT-LOG — nbb-claude-for-legal--claude-liam-matter-update

Source: `anthropics/claude-bear/claude-for-legal--claude-liam-matter-update/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)

## What changed

- Removed `_variant_todo` from metadata (scaffold checklist consumed).
- Rewrote `narration_text` for every body beat (B00–B11) in the Teardown register:
  take-it-apart phrasing, "here's what's actually happening", named trade-offs
  ("scope is what the file says, no more"; "judgment isn't in the file, so
  judgment isn't on the menu"). Facts unchanged: five-trigger list, Case 4471
  anchor, matter-update SKILL.md as the mechanism, linear no-branching runtime.
- **BCRY (carry-out) narration left verbatim.** It already reads as Teardown
  design-judgment ("a file, not a memory"), and it is the exact string sitting
  in the `WantQuote.quote` prop — rewriting the narration would desync the
  on-screen card. Kept them locked together.
- **BHTF converted from "your turn handoff" → "LLM EXERCISE"** (§Step 3):
  - `act` renamed `"LLM EXERCISE"`.
  - Old prompt (a CLI-style "before you make any change, read your
    instructions…" directed at Claude Code) replaced with a paste-into-any-LLM
    prompt derived from the video's subject: *write me a SKILL.md for a repeated
    task I do, with triggers / steps / do-not-touch / return, then tell me what
    you left out.* Produces a genuinely useful artifact on its own without the
    video.
  - Added `llm_exercise` object with `prompt` + `dig_deeper` per SKILL.md schema.
  - Updated `ClaudeComposerAsk.command` prop to match (short-form, no
    `[describe it in one sentence]` line since the composer card is a still).
  - Bumped `estimated_duration_s` 30 → 55 to match the longer read (reference:
    ip-clause-review LLM beat, 55s).
- **BOUT (outro) narration updated** to add the punch tag before "Liam, in for
  Bear": `"Claude, Matter Update — a file, not a memory. Liam, in for Bear."`
  Same edit propagated to `OutroCTA.line` prop so the on-screen card matches.
  Same construction as the ip-clause-review reference outro
  (`"…assignment, not license. Liam, in for Bear."`).

## Judgement calls

- **B00 word count.** SKILL.md WRITER LAW note requires 20–35 words + 0.8s
  lead-silence for the typing window. Teardown rewrite lands at ~34 words —
  inside the ceiling, no note edit needed.
- **BCRY untouched.** As above — narration is the visible quote card, and the
  sentence is already Teardown. Preserved rather than paraphrased.
- **B11 trade-off phrasing.** Added the explicit trade-off sentence
  ("Judgment isn't in the file, so judgment isn't on the menu") because the
  Teardown register requires naming what the design costs, not just what it
  buys. Facts unchanged — the source already said "it only does what's
  written"; the rewrite frames that as the cost side of the reliability trade.
- **LLM exercise subject.** Chose "write me a SKILL.md for one of your own
  repeated tasks" over a matter-update-specific prompt. Rationale: the reel's
  general lesson is *what a Skill is and how it works*, not the specific
  legal-ops workflow. The dig-deeper (run the SKILL.md against three variants,
  including one where it clearly fails) reinforces the B10/B11 direction-A vs
  direction-B split from the reel.

No files besides `beat_sheet.nbb.json` and this log were touched. No renders,
no audio, no compile.
