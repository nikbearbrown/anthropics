# CONVERT-LOG — nbb-claude-for-legal--claude-liam-dsar-response

Register conversion of `beat_sheet.json` (Plain, claude-liam / HAI) → `beat_sheet.nbb.json` (Teardown, NikBearBrown / Liam-in-for-Bear). Scaffold from `brand_variant.py` was already in place; this pass did Steps 2–4 (rewrite, LLM exercise, verify order).

## What changed

- **B00–BCRY narration** — every beat rewritten in the Teardown register (Feynman × MKBHD). Facts unchanged: same three-identifier example (current email / name-only / closed-out email), same two-consequences payoff (zero-hit ≠ no-data; a hit is not automatically shippable), same carry-out (every system, every identifier, only their data). Voice moves from HAI-Plain narration to Teardown mechanism-and-design-critique: names what each system was optimized for (customer database = one row per customer for marketing, not every trace for legal), why each identifier landed where it did (signup form asked for current email; support queue keys on whoever the agent typed; mailing list still carries a legacy address). Aimed word counts within ~15 % of source per beat to keep visual/audio windows close.
- **BCRY WantQuote `quote` prop** — resynced with the rewritten carry-out sentence so the on-screen line matches the narration.
- **BHTF → LLM EXERCISE beat (second-to-last).** Repurposed the existing `your turn handoff` slot rather than inserting a new beat_id, matching the pattern used in the sibling reels under `nbb-claude-for-legal--*` and `nbb-books--*`. The `ClaudeComposerAsk` scene is preserved; the beat now carries an `llm_exercise` block with a paste-ready prompt (build a defensible DSAR search plan — enumerate systems, enumerate identifiers, produce a search matrix, flag records that need redacting) plus a `dig_deeper` follow-up (where DSAR search plans usually break in practice, and what one process change would catch each failure earlier). Composer `command` is the compact on-screen version of the prompt; `segment` was flipped from `Your Turn` to `Claude, DSAR Response.` to match how the working sibling sheets label the LLM-exercise composer.
- **BOUT** — kept as `OutroCTA` with `@HumanitariansAI`. Narration and `line` prop preserved as the standard "Claude, [Title]. Liam, in for Bear." (see judgement call below).
- **`_variant_todo` metadata block** — removed, per the scaffold contract.

## Judgement calls

- **"Dsar" → "DSAR"** in the BOUT `line`, the BOUT narration, and the BHTF composer `segment`. DSAR is a real legal acronym (Data Subject Access Request); the lowercased form in the source was a title-case artifact from the automated slug-to-title step. Fixing capitalization is a fact-preserving polish; more importantly, Kokoro pronounces an all-caps acronym as letters ("D-S-A-R") but reads "Dsar" as a nonsense word — leaving it broken would ship a mispronounced brand line. Applied only where the string is spoken or shown; `metadata.title` and `metadata.source_sheet` were left as-is to avoid collateral changes to downstream indexers.
- **BHTF beat_id kept as `BHTF`** instead of the `B_LLM` id shown in `skills/make/nbb/SKILL.md` §Step 3. Every already-converted sibling in this tree (`nbb-books--*`, `nbb-claude-for-legal--claude-liam-ip-clause-review`) keeps `BHTF`; the SKILL.md schema example is a template, not a hard contract, and preserving the id avoids re-wiring downstream references to a beat slot that already has a Remotion scene wired to it.
- **Visual/graphic blocks left untouched.** The Manim `production_viz.colors` still carry the humanitarians four-color set (`#F3EBDD / #2F2A26 / #E4572E / #1F4E5F`) instead of the teardown white/ink/one-red. `brand_variant.py` did not repaint them and SKILL.md §Step 2 says preserve visuals — so I did. If the teardown palette must actually apply to the Manim renders, that is a re-render decision, not a beat-sheet edit.
- **`estimated_duration_s` on BHTF** bumped from 25 → 45 to reflect the longer LLM-exercise narration (paste-ready prompt + dig-deeper follow-up + sign-off). Every other beat's estimate left untouched; audio-first pass will re-measure regardless.

## Ending order (verified)

```
B00  hesitant writer cold open
B01  1 stakes / 2 wrong guess, falsified
B02  3 mechanism / 4 ANCHOR PLANTED
B03  4 ANCHOR PAYOFF / 5 both directions
BCRY 6 CARRY-OUT
BHTF LLM EXERCISE        ← second-to-last
BOUT outro               ← last
```

No render, no audio, no compile performed. Deliverable is the sheet.
