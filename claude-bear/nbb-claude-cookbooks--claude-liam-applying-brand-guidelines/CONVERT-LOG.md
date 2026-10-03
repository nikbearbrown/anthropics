# nbb convert log — claude-cookbooks--claude-liam-applying-brand-guidelines

Converted 2026-09-03 by the register-conversion factory.

## What changed

- Rewrote `narration_text` on every beat (B00, B01, B02, B03, BCRY, BHTF, BOUT)
  in the Teardown register (Feynman × MKBHD): explain the machinery, name the
  design choice ("the file is the program", "linear by design", "optimized for
  repeatability at the expense of range"), judge the trade-off. Voice only,
  facts unchanged.
- Facts preserved verbatim: every filename (`apply_brand.py`, `validate_brand.py`,
  `REFERENCE.md`, `SKILL.md`), the four-kilobyte SKILL.md size, the three-step
  Steps section, the stated scope ("external communications only"), the
  in-scope-vs-out-of-scope anchor pair, and validate_brand.py as the check on
  wrong colors / wrong fonts / wrong scope.
- B00 kept inside the WRITER LAW TIMING envelope: rewrite is 31 words with
  `lead_silence_s: 0.8` untouched, so the BrutalistHesitantWriter still has its
  ≥9s window to land the `match` → `apply` correction.
- BCRY's on-screen `WantQuote.props.quote` updated to match the new narration
  so the card and the read still agree (same claim, tighter voice; `sparkLine`
  left as-is — "Applies it. Then checks it." still fits).
- BHTF promoted to the **LLM EXERCISE** beat (act renamed): added the structured
  `llm_exercise` object with a paste-ready `prompt` naming SKILL.md, both scripts,
  and the stated scope; plus a real `dig_deeper` follow-up ("hand it a document
  outside the stated scope — internal doc instead of external communications —
  which steps change and which don't?"). Narration now ends "Go deeper: …" so
  Liam speaks the extension out loud.
- BOUT (outro) left as-is — matches the standing NikBearBrown/Liam sign-off.
- Removed `_variant_todo` (all four items done).
- Metadata `audience`, `register`, `palette`, `engine`, `voice_kokoro` left as
  the scaffold set them.

## Ending order (verified)

`… body → BCRY (carry-out) → BHTF (LLM exercise) → BOUT (outro)` ✓

## Judgement calls

1. **BHTF already stood in the LLM-exercise slot** (paste-ready prompt via
   `ClaudeComposerAsk`, second-to-last). Rather than insert a new `B_LLM` beat
   and either duplicate the paste-in prompt or push BHTF out of position, I
   upgraded BHTF in place: renamed its `act` to `LLM EXERCISE`, added the
   schema's structured `llm_exercise` object, and worked the `dig_deeper` line
   into the spoken narration. Matches the sibling nbb conversion pattern
   (`nbb-claude-cookbooks--claude-liam-analyzing-financial-statements`).
2. **Kept the `ClaudeComposerAsk` visual for BHTF** instead of the SKILL.md
   schema's plain `CARD` type. `ClaudeComposerAsk` renders the paste-in prompt
   inside the actual Claude composer chrome — the same "hold on a card" motion,
   but the card is the exact thing the viewer will paste. Losing it would make
   the exercise abstract; keeping it makes it copyable.
3. **Did not re-scaffold.** The existing `beat_sheet.nbb.json` already had
   `audience: NikBearBrown`, `palette: teardown`, `engine: kokoro`,
   `voice_kokoro: am_onyx`. Left every one of those as-is per the standing
   rule ("Do not re-scaffold").
4. **No audio, no compile.** Deliverable is the beat sheet only; rendering is a
   separate pass.
