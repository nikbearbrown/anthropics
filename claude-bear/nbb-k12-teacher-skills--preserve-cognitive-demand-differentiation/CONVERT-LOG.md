# CONVERT-LOG — k12-teacher-skills--preserve-cognitive-demand-differentiation → nbb

Source: `anthropics/claude-bear/k12-teacher-skills--preserve-cognitive-demand-differentiation/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Facts preserved verbatim: 17 ÷ 5 across three tiers (dots grouped by
  5, basket-analogy 3 R2, proof of remainder < divisor); the simpler-book vs
  same-book-plus-scaffold counterexample; the differentiation-vs-tracking test
  (three doors into one room vs one entry forking into three separate
  ceilings); cognitive load theory's split into extraneous (scaffold absorbs)
  and germane (learner keeps) load; the remainder = 2 anchor returning at B04
  as germane load; and the carry-out sentence. Voice-only edits: named the
  design move explicitly ("the representation flexes, the entry point flexes,
  but the hard case sits inside every tier"), surfaced the trade-off ("what
  this optimizes for is who gets in; what it refuses to sacrifice is what
  happens once they are there"), and made the intellectual-honesty test
  concrete ("the tell is the exit, not the entrance"). Every rewrite ends on
  a "worth keeping" or "trade-off" beat so the Feynman × MKBHD lens is
  visible, not just implied.

- **BHTF upgraded to the LLM EXERCISE beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added the
  structured `llm_exercise` object with `prompt` (paste-ready template for
  Claude / ChatGPT / Gemini, using `[X]` / `[Y]` placeholders for the viewer's
  own concept + hard case) and `dig_deeper` follow-up (asks the model to draft
  a *tracked* version that quietly removes the hard case and to name what got
  deleted — that is the germane load the differentiated version was
  protecting). Narration rewritten to read out the prompt and end with the
  "Go deeper: …" line. `beat_id` preserved per the preserve-IDs rule.
  Shot (`ClaudeComposerAsk`) preserved; `topic` broadened from
  "DIFFERENTIATION · K-12 PEDAGOGY" to "DIFFERENTIATION · YOUR LESSON" so the
  composer chip names the viewer's task, `segment` simplified to "The Hard
  Case", `folderLabel` flipped `@HumanitariansAI` → `@NikBearBrown`, and
  `runningText` broadened to `paste this into Claude, ChatGPT, or Gemini…`.
  `command` prop rewritten to match the new template prompt.
  `estimated_duration_s` bumped 24 → 42.

- **BOUT retargeted to the NikBearBrown channel.** Remotion pattern kept
  (`OutroCTA` — same as sibling `nbb-k12-teacher-skills--cra-progression-scaffold`).
  `handle` flipped `@HumanitariansAI` → `@NikBearBrown`. Narration line
  lengthened from "The Hard Case. Liam, in for Bear." to include the carry-out
  compressed to one clause ("The Hard Case — differentiation changes the door
  in, not the room behind it. Liam, in for Bear.") so the outro line carries
  the whole argument on its own. `estimated_duration_s` bumped 5 → 8.

- **Metadata `_variant_todo` removed** (checklist complete). `folderLabel` and
  `channel_title` at the sheet level flipped `@HumanitariansAI` → `@NikBearBrown`
  for consistency with the outro handle. `register` set to "Teardown" (scaffold
  already wrote this — kept).

- **`purpose` rewritten** in the Teardown register. Was a plain description of
  what the reel does; now names the trade-off explicitly ("tiering optimizes
  for who gets to the concept; what it refuses to sacrifice is the concept
  itself") and calls out cognitive load theory as the reason the rule
  survives — germane load *is* the curriculum.

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL example
   uses `beat_id: "B_LLM"` and says "insert one beat before the outro". The
   source already has `BHTF` at second-to-last position performing a paste-ready
   handoff — adding a *second* paste-ready prompt beat right after it would
   force viewers through two "paste this into Claude" moments back-to-back for
   no gain. Followed the sibling nbb reels' precedent (see
   `nbb-k12-teacher-skills--cra-progression-scaffold`): kept `BHTF` as the
   beat_id, renamed the act to `LLM EXERCISE`, added the `llm_exercise`
   structured field and the "Go deeper: …" follow-up. No new beat inserted; no
   reorder. This preserves *every* source beat_id, which the invocation lists
   as an exact-preserve requirement.

2. **BCRY narration + WantQuote card copy left unchanged.** The carry-out
   sentence ("Differentiation changes the door in — never the hard case waiting
   behind it.") already reads as Teardown — it names the design contrast and
   the trade-off in one clause, and it is the on-screen `quote` prop that pairs
   with `sparkLine`. Rewriting the voice-over here would either drift out of
   sync with the card or force a re-write of the card copy for no register
   gain. Applied the "on-screen card copy that still fits the register" rule.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim.** The typing
   text ("My strugglers cannot do this. So I will make their task easier?") is
   the locked visual — the correction from "easier" to "different" is what the
   whole cold open turns on, and the trigger/replacement pair is a single
   whitespace token each (a multi-word trigger silently never fires — the
   lesson the sibling reels carried over from the k12-lesson-differentiation
   Gate V finding). Only the narration was re-voiced. New narration is 33
   words — inside the 20–35 window the note requires.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` left as scaffold
   wrote them.** Re-scaffolding was explicitly out of scope; `palette` is now
   `teardown` and downstream compile reads that field. The residual
   humanitarians hints only affect the frozen B00 shot props, which stay.

5. **`playlist: Claude Basics` preserved from source.** The series identity
   travels with the K-12 teacher-skills book, not with the audience cut — same
   call the sibling nbb reels made.

6. **BHTF `topic` widened.** Source topic on the composer was
   "DIFFERENTIATION · K-12 PEDAGOGY" (echoing the reel-level topic). Changed
   to "DIFFERENTIATION · YOUR LESSON" so the chip on-screen matches what the
   viewer is being asked to paste — the template is for their lesson, not the
   reel's example. Sibling reel made the same move
   ("CRA PROGRESSION · YOUR LESSON").

7. **BOUT pattern kept as `OutroCTA`.** Source was already `OutroCTA` — no
   swap needed. Only the `handle` and the `line` changed.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.
