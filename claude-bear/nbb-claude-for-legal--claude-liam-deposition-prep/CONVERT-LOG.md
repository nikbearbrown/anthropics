# CONVERT-LOG — nbb-claude-for-legal--claude-liam-deposition-prep

Converted from source `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown register, Liam / Kokoro am_onyx).

## What changed

- **Register rewritten.** Every `narration_text` (B00–BOUT) rewritten in Teardown voice (Feynman × MKBHD): "Here's what's actually happening…", "They optimized for X at the expense of Y", "repeatability, not judgment". No new facts introduced; every claim in the source survives (deposition-prep = one folder + one SKILL.md; pull docs → sort by case theory → flag impeachment; linear execution; specification not instinct).
- **BCRY WantQuote `quote` prop** updated to match the rewritten carry-out narration verbatim.
- **BHTF elevated to the LLM-exercise beat** (second-to-last). Added `llm_exercise: {prompt, dig_deeper}` block per SKILL.md §Step 3 schema; narration now names the three frontier LLMs and ends with a "Go deeper:" follow-up. Kept the existing `ClaudeComposerAsk` visual (updated `command` and `runningText` to match). Act label changed from "your turn handoff" → "LLM EXERCISE". Estimated duration bumped 19→24s to fit the longer paste-ready + dig-deeper narration.
- **BOUT (outro) narration preserved verbatim** — "Claude, Deposition Prep. Liam, in for Bear." IS the NikBearBrown outro form (IN-FOR-BEAR LAW). Changed `handle` prop from `@HumanitariansAI` → `@NikBearBrown` since this is the NBB cut destined for the NikBearBrown channel; visual pattern (`OutroCTA`) left as scaffold set it.
- **Metadata.** Removed `_variant_todo` (Done criterion). Rewrote `purpose` to describe the Teardown pass rather than the Plain-register source. Left `register: Teardown`, `palette: teardown`, `engine: kokoro`, `voice_kokoro: am_onyx`, `outro_source: AUTHOR.MD :: NikBearBrown` exactly as the scaffold set them. `channel_title` / `folderLabel` / `ground` / per-beat visual color hexes left untouched — that palette reconciliation belongs to the render pass, not to a register conversion.

## Judgement calls

- **No separate `B_LLM` beat inserted.** The source's `BHTF` was already a paste-ready-prompt "Your Turn" beat with `ClaudeComposerAsk`; the sibling `nbb-claude-for-legal--claude-liam-ip-clause-review` treats `BHTF` as the LLM-exercise slot. Inserting a separate `B_LLM` would have stacked two paste-ready prompts back-to-back before the outro. Chose to satisfy §Step 3 by upgrading `BHTF` in place — schema (`llm_exercise` block) and content (frontier-LLM framing + `dig_deeper`) both present, second-to-last position preserved.
- **Outro pattern kept as `OutroCTA` (source pattern)**, not switched to `OutroSeries` (sibling pattern). Both are valid per SKILL.md; keeping the source pattern minimizes render-time risk given the narration is unchanged.
- **B00 typing hesitation intact.** Rewrite kept "knows" in the narration so the on-screen correction (`triggerWords: knows` → `replacementWords: was given steps for`) still lands. Word count 37, inside the 20–35-ish TIMING-LAW window noted in the beat.
