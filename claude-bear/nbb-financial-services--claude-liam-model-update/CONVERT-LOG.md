# CONVERT-LOG — financial-services--claude-liam-model-update

Source register: **Plain** (per source metadata `"register": "Plain"`, though the scaffold pre-set Teardown).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Updated `metadata.purpose` to say "in the Teardown register" (was "Plain register").
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: model-update is a Claude Skill; the skill is a folder Claude reads before it acts; the folder contains one file, SKILL.md, in plain language; Claude runs the numbered steps top to bottom (take new data → adjust estimates + recalculate valuation → flag what changed materially); no branching unless a step tells it to; inputs are the earnings print, revised guidance, a changed assumption; the update touches the model, not Claude; data is per-run and doesn't persist into Claude; the investment call still belongs to a person; the skill flags what changed, doesn't decide.
- **B00**: added the in-for-Bear self-introduction ("Liam here, in for Bear") to satisfy IN-FOR-BEAR LAW at the cold open. Kept the visual card, hesitant-writer props, and TIMING LAW note exactly. Bumped `estimated_duration_s` 13 → 14 for the added clause.
- **NB01–NB03**: re-registered Plain → Teardown ("Here's what's actually happening…", "That's the trade they picked — reproducibility over cleverness", "They optimized for a repeatable refresh at the expense of an automated call — the human is doing the judgment on purpose"). Bumped estimated durations to reflect the slightly longer reads (planning hints only; actual clock comes from measured audio when `generate_audio_kokoro.py` runs).
- **BCRY**: narration + `WantQuote.quote` + `sparkLine` left exactly as-is. The carry-out sentence is what CARRY-OUT.md is signed on and it already reads as pure Teardown (mechanism claim + trade-off named). Rewriting would break the signed gate; the sparkLine "Current. Never decided." already lands the trade in one breath.
- **BHTF**: converted from "your turn handoff" → LLM EXERCISE beat per SKILL.md §Step 3. Added `llm_exercise: { prompt, dig_deeper }` with a paste-ready prompt anchored to concrete numbers (8% growth, 22% margin, existing DCF, earnings beat with a 200 bps margin miss, guidance cut 8%→6%, capex +15%) so the LLM can produce a useful walk-through without the video. Narration re-worked to speak the paste prompt and end on the "Go deeper:" follow-up; `act` relabelled "LLM EXERCISE"; the `ClaudeComposerAsk.command` prop rewritten to mirror the paste prompt so the on-screen composer shows what the viewer would actually paste. Second-to-last position preserved.
- **BOUT**: NikBearBrown outro. Remotion pattern flipped `OutroSeries` → `OutroCTA`; props `{ eyebrow, line }` replaced with `{ line, handle }`; `line` now reads "It Updates the Model. Not Itself. Liam, in for Bear. www.brutalist.art" and `handle` is `@NikBearBrown`. Narration reads "Brutalist dot art." at the end. Bumped `estimated_duration_s` 6 → 7 for the extra clause. `tail_silence_s: 1.0` kept.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF `ClaudeComposerAsk.folderLabel` chip at `@HumanitariansAI`. SKILL.md only requires that the *outro* handle be `@NikBearBrown` (per `outro_source: AUTHOR.MD :: NikBearBrown`). The composer chip is on-screen context for a body beat; preserving it matches how sibling nbb sheets in this book render (see `nbb-financial-services--claude-liam-3-statement-model/beat_sheet.nbb.json` BHTF). Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Kept `metadata.palette: "teardown"`** as the scaffold set it, but left `style_preset: "humanitarians"` and `ground: "#F3EBDD"` alone. Those are visual overrides used by downstream compile — this pass rewrites the voice, not the skin. If the render turns out to want the flat-white teardown ground (`#FFFFFF`) instead of `#F3EBDD`, that is a compile-time flip, not a beat-sheet edit for this stage.
- **Did not touch `metadata.gate_c: "SIGNED - CARRY-OUT.md"`** or the carry-out narration itself. The carry-out sentence is the signed hinge and rewriting it would invalidate the signature; the Teardown register is honored by the surrounding beats and by keeping the sentence exact.
- **No new beat inserted for the LLM exercise.** BHTF already sat in the second-to-last "paste this into Claude" slot with the correct `ClaudeComposerAsk` component. Adding a second card would be redundant; the sibling `3-statement-model` conversion made the same call. Converted the existing beat instead.
- **`estimated_duration_s` bumps** on B00/NB01–NB03/BHTF/BOUT are planning hints; the clock is `narration` (measured audio) and the real durations overwrite these when audio is regenerated.

## Ending order (verified)

```
B00  hesitant writer cold open
NB01 3 mechanism (skill is a folder)
NB02 3 mechanism (linear pipeline)
NB03 3 mechanism (updates the model, not Claude)
BCRY 6 CARRY-OUT
BHTF LLM EXERCISE            ← second-to-last
BOUT outro (NikBearBrown)    ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run to pick up the new B00/NB01–NB03/BHTF/BOUT narration and re-measure the clock.
