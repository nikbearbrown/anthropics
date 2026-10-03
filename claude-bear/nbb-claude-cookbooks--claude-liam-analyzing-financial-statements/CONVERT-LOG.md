# nbb convert log — claude-cookbooks--claude-liam-analyzing-financial-statements

Converted 2026-09-03 by the register-conversion factory.

## What changed

- Rewrote `narration_text` on every beat (B00, B01, B02, B03, BCRY, BHTF, BOUT)
  in the Teardown register (Feynman × MKBHD): explain the machinery, name the
  design choice ("the file is the program", "linear by design", "optimized for
  repeatability at the expense of range"), judge the trade-off.
- Facts unchanged: every filename (`calculate_ratios.py`, `interpret_ratios.py`,
  `SKILL.md`), the two-kilobyte size, the three-step Steps section, the
  in-spec-vs-out-of-spec anchor pair — all preserved verbatim.
- BCRY's on-screen `WantQuote.props.quote` was updated to match the new
  narration so the card and the read still agree (same claim, tighter voice).
- BHTF promoted to the **LLM EXERCISE** beat (act renamed): added a structured
  `llm_exercise` object with a paste-ready `prompt` and a real `dig_deeper`
  follow-up ("hand it a cash-flow statement… which steps change and which don't?").
  The narration now ends "Go deeper: …" so Liam speaks the extension out loud.
  Kept the existing `ClaudeComposerAsk` visual — its `command` prop is the exact
  paste-in prompt, which is the whole point of the card.
- BOUT (outro) left as-is — matches the standing NikBearBrown/Liam sign-off.
- Removed `_variant_todo` (all four items done).
- Metadata `audience`, `register`, `palette`, `engine`, `voice_kokoro` left as
  the scaffold set them.

## Ending order (verified)

`… body → BCRY (carry-out) → BHTF (LLM exercise) → BOUT (outro)` ✓

## Judgement calls

1. **BHTF already stood in the LLM-exercise slot** (paste-ready prompt via
   `ClaudeComposerAsk`, second-to-last). Rather than insert a new
   `B_LLM` beat and either duplicate the paste-in prompt or push BHTF out of
   position, I upgraded BHTF in place: renamed its `act` to `LLM EXERCISE`,
   added the schema's structured `llm_exercise` object, and worked the
   `dig_deeper` line into the spoken narration. Matches the prior nbb
   conversion pattern (nbb-financial-services--claude-liam-deal-sourcing).
2. **Kept the `ClaudeComposerAsk` visual for BHTF** instead of the SKILL.md
   schema's plain `CARD` type. `ClaudeComposerAsk` renders the paste-in prompt
   inside the actual Claude composer chrome — the same "hold on a card" motion,
   but the card is the exact thing the viewer will paste. Losing it would make
   the exercise abstract; keeping it makes it copyable.
3. **Did not re-scaffold.** The existing `beat_sheet.nbb.json` already had
   `audience: NikBearBrown`, `palette: teardown`, `engine: kokoro`,
   `voice_kokoro: am_onyx`. Left every one of those as-is per the standing
   rule ("Do not re-scaffold").
4. **No audio, no compile.** Deliverable is the beat sheet only.
