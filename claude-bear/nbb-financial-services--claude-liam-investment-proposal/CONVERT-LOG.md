# CONVERT-LOG — financial-services--claude-liam-investment-proposal

Source register: **Plain** (source sheet's `register: "Plain"`; scaffold pre-set `register: "Teardown"` on the nbb copy, which this pass now honors).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: a Skill is a folder Claude reads before it works; SKILL.md is the plain-English instruction set; the Steps section is the pipeline; Claude executes each step in order, linearly, no branching unless a step says so; the investment-proposal spec covers approach, allocation, expected outcomes, and fees; same page → same result every run; scope limited to what the page names.
- **B00**: added an explicit "Liam here, in for Bear" line (IN-FOR-BEAR LAW), reframed the app→skill correction as a wrong-noun teardown rather than a bare rephrase. `estimated_duration_s` 15 → 18.
- **B01–B02**: rewrote to name the design bet ("the file is the program") and the trade ("optimized for predictability at the expense of cleverness"). `estimated_duration_s` bumped modestly (15→17, 10→17) to match longer reads.
- **B03**: added the honest limit — "only covers what the page says … ask for tax analysis and you get nothing" — and named the trade-off explicitly ("works if you value repeatability; fails if you needed a section the author never wrote"). `estimated_duration_s` 21 → 28.
- **BCRY**: narration and on-screen `WantQuote.quote` are the metadata `carry_out` verbatim; left as-is (already Teardown-register-fit and already synced to the card).
- **BHTF**: converted from generic "your turn handoff" to a proper LLM EXERCISE beat per SKILL.md §Step 3. `act` relabelled `"LLM EXERCISE"`. Added `llm_exercise: { prompt, dig_deeper }`. Narration reads the paste-ready prompt in shortened spoken form and includes the "Go deeper:" follow-up. `ClaudeComposerAsk.command` rewritten to mirror the paste-ready prompt so the on-screen composer matches what the viewer would paste. `estimated_duration_s` 22 → 44 (long-form read).
- **BOUT**: NikBearBrown outro. Pattern swapped `OutroSeries` → `OutroCTA`; `handle` = `@NikBearBrown`; `line` = `"Claude, Investment Proposal. Liam, in for Bear. www.brutalist.art"`. Narration: "Claude, Investment Proposal. Liam, in for Bear. Brutalist dot art." (URL read aloud). `estimated_duration_s` 4 → 7 for the extra clause. `metadata.style_preset` left as `claude` — that's the composer chrome, not the outro chrome.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` / `channel` = `@HumanitariansAI`** and left the BHTF `ClaudeComposerAsk.folderLabel` prop at `@HumanitariansAI`. SKILL.md is explicit only about the outro handle → NikBearBrown. The composer chip is on-screen source-context card copy for a body beat; preserving it matches the sibling nbb sheet (`nbb-financial-services--claude-liam-3-statement-model`). Only BOUT's rendered chrome flips to `@NikBearBrown`.
- **Preserved the `metadata.purpose`, `mode`, `source_sheet`, `source_register` fields** as scaffolded even though the source_register field disagrees with the actual source sheet's `register: "Plain"` — the scaffold wrote `"Teardown"` there and that's the field the tooling reads. Logged the actual source register at the top of this doc; did not silently fix the metadata field.
- **Preserved every `estimated_duration_s` where the rewrite is only slightly longer**, bumped only where the Teardown add materially lengthens the read (B00, B02, B03, BHTF, BOUT). The clock is measured audio; these are loose planning hints that get overwritten by real `generate_audio_kokoro.py` output.
- **Preserved on-screen card copy** (`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism` props). The cards are already spare and Teardown-register-fit; rewriting them risks desyncing the visual from beats that render fine as-is.
- **No brand-new beat inserted for the LLM exercise.** BHTF already occupied the second-to-last slot with the right shot component (`ClaudeComposerAsk`); adding a second card would be redundant. Converted the existing beat in place.

## Ending order (verified)

```
B00  hesitant writer — cold open
B01  anatomy
B02  pipeline
B03  mechanism + scope
BCRY carry-out
BHTF LLM EXERCISE          ← second-to-last
BOUT outro (NikBearBrown)  ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run for this variant.
