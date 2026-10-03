# CONVERT-LOG — financial-services--claude-liam-3-statement-model

Source register: **Plain** (per source_note; scaffold said Teardown but source narration was Plain).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: 3-statement-model reads a template that lays out IS/BS/CF and links them; net income anchor (IS → retained earnings on BS → top of CF); "ties out ≠ right"; a blank line usually means the step got no input; Claude executes the SKILL.md steps linearly and does not improvise off-list.
- **BCRY**: on-screen `WantQuote.quote` and `sparkLine` re-synced to the new narration ("Wired by procedure, not judgment.") so Liam's voice and the card don't split.
- **BHTF**: converted from "your turn handoff" to a proper LLM EXERCISE beat (per SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }`; narration includes the "Go deeper:" follow-up; ClaudeComposerAsk `command` prop rewritten to mirror the paste-ready prompt with concrete assumptions ($500k revenue, $300k expense, $100k cash) so the on-screen composer shows the same thing the viewer would paste. Second-to-last position preserved.
- **BOUT**: NikBearBrown outro. Narration reads the URL ("Brutalist dot art."), OutroCTA handle → `@NikBearBrown`, `line` → `"How Does Claude Fill In a Financial Model? Liam, in for Bear. www.brutalist.art"`. Bumped `estimated_duration_s` 6 → 7 for the extra clause.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF ClaudeComposerAsk `folderLabel` prop at `@HumanitariansAI`. SKILL.md is explicit only about the *outro* handle → NikBearBrown. The composer chip is on-screen source-context card copy for a body beat; preserving it matches sibling nbb sheets in this book. Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Preserved `estimated_duration_s`** on all body beats even though several Teardown rewrites run slightly longer than the source. The clock is measured audio (`clock: narration`); those estimates get overwritten by real durations when `generate_audio_kokoro.py` runs. Left them as loose planning hints.
- **BHTF `estimated_duration_s` 26 → 34** — the added dig-deeper line materially lengthens the read; wanted the planning estimate to not lie by 10s.
- **BHTF `act`** relabelled `"your turn handoff"` → `"LLM EXERCISE"` per SKILL.md schema.
- **No new beat inserted.** BHTF already occupied the "paste this into Claude" second-to-last slot with the right shot component; adding a second card would be redundant. Converted the existing beat instead.

## Ending order (verified)

```
B00  hesitant writer cold open
B01  wrong guess, falsified
B02  mechanism / anchor planted
B03  anchor payoff / both directions
BCRY carry-out
BHTF LLM EXERCISE            ← second-to-last
BOUT outro (NikBearBrown)    ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run.
