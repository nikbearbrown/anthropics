# CONVERT-LOG — nbb-financial-services--claude-liam-accrual-schedule

Source: `../financial-services--claude-liam-accrual-schedule/beat_sheet.json`
Output: `beat_sheet.nbb.json`

## What changed

- **Register rewritten to Teardown (Feynman × MKBHD)** on every beat's
  `narration_text`. All facts preserved verbatim — same skill mechanism
  (compute → cite → draft), same anchor (December utility bill), same
  carry-out. Voice change only.
- **Named the design choice on B01/B02/B03.** "Optimized for auditability at
  the cost of coverage" (B01). "The stopping point is a design decision, not a
  limit — controller's desk next, not ledger next" (B02). "Works if you value
  defensible entries you'll re-check; fails if you wanted the machine to catch
  bad source documents on its own" (B03). Standard Teardown "they optimized for
  X at the expense of Y" moves — no new facts.
- **B00 cold open** re-voiced within the 20–35 word / ≥9s typing-window
  constraint noted in the source's `note`. Kept "Liam here, standing in for
  Bear" (IN-FOR-BEAR LAW).
- **BHTF re-voiced** with a Teardown framing at the end ("You're not testing
  Claude's judgment — you're testing whether the skill stops when there's
  nothing left to cite"). "Liam, in for Bear" sign-off preserved.
- **BCRY narration held nearly verbatim** to match the `WantQuote.props.quote`
  card copy on screen — the whole beat is that sentence, so narration ≡ card.
- **BOUT held verbatim** — narration line ≡ `OutroCTA.props.line` on screen.
- **Inserted B_LLM as the second-to-last beat** — a paste-ready LLM prompt
  (explain accruals + walk through an unbilled year-end utility expense: draft
  JE, cited support, why the citation matters before posting) + a dig-deeper
  follow-up (which accruals are hardest to build this way — where the number
  is real but no single document supports it — and how a controller handles
  those). Prompt is model-agnostic (Claude / ChatGPT / Gemini), no CLI, no
  skill install, useful without the video. Shot: `CARD / own / hold` per
  SKILL.md §Step 3. Narration reads the prompt's shape aloud, not the prompt
  verbatim.
- **`_variant_todo` removed** — every item ticked.
- **Ending order verified**: B00 → B01 → B02 → B03 → BCRY → BHTF → **B_LLM**
  (second-to-last) → **BOUT** (last).

## Judgement calls

1. **BHTF kept, not consumed by B_LLM.** BHTF was already a "your turn" beat
   in the source (CLI-shaped: "run the accrual-schedule skill"). B_LLM is a
   different beast — a paste-ready LLM prompt that produces useful output on
   its own without the skill or any Anthropic tooling. Kept both because
   SKILL.md §Step 3 says *insert* the LLM exercise beat, and preserving every
   `beat_id` was a hard rule. Result: BHTF stays as the skill-oriented handoff,
   B_LLM is the standalone LLM exercise.
2. **BOUT `handle` left as `@HumanitariansAI`.** The scaffold set the audience
   to NikBearBrown but left `channel_title` / `folderLabel` / OutroCTA.handle
   pointing at @HumanitariansAI. Since the instructions say "preserve exactly:
   … shot blocks", I did not change the on-screen handle. If this reel is
   supposed to re-address the NikBearBrown channel (@NikBearBrown /
   brutalist.art) instead of remaining a NBB-register cut for @HumanitariansAI,
   that's a channel-repoint decision the supervisor should make, not this
   conversion pass.
3. **BOUT narration held verbatim.** The nbb SKILL.md says the outro should
   come from `AUTHOR.MD :: NikBearBrown`. That file was not provided and the
   current line — "How Does Claude Build an Accrual Schedule? Liam, in for
   Bear." — is a legitimate Liam sign-off already on the OutroCTA card. Kept
   narration ≡ card copy rather than desynchronize them by guessing at
   AUTHOR.MD content.
4. **All GRAPHIC blocks' Manim colors preserved** (humanitarians palette
   quartet on B01/B02/B03), even though the metadata palette is now
   `teardown`. Rationale: `graphic.production_viz.colors` lives inside the
   shot block; the "preserve shot blocks exactly" rule wins. Downstream Manim
   scenes will render as-is; retinting is a separate pass if the supervisor
   wants it.

## Not done (out of scope for this pass)

- No audio generated. No render. No compile. The beat sheet is the deliverable.
- `mp3/beat-B_LLM.mp3` referenced but does not exist yet — the audio pass will
  create it.
