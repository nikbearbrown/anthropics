# CONVERT-LOG — financial-services--claude-liam-financial-plan

Source register: **Plain** (per source_note; scaffold said Teardown but source narration was Plain — hai-simple).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: the financial-plan skill only recognizes the cases the file names (new client onboarding, annual plan review, scenario request) and only builds the four artifacts the file names (retirement projections, education funding, estate planning, cash flow analysis); anchor is the retirement-age dial → monthly savings-target readout; both-directions honest limit (big jump ≠ improvising, tiny change ≠ judged fine).
- **B00**: 34-word rewrite, still inside the 20–35 word TIMING LAW window and preserves the "judgment → a skill" pivot the BrutalistHesitantWriter typing performs.
- **B01**: added the explicit design-critic frame — "They optimized for reproducibility at the expense of judgment. Same inputs, same procedure, same four artifacts." Kept the "TAX FILING?" style off-list example (a tax filing / an insurance shop) so the graphic and narration still line up.
- **B02 / B03**: narration re-voiced to describe the anchor as machinery ("It's being computed" / "It never means the skill formed an opinion about the number"). Concrete dial numbers (65 → 60) pulled up from the graphic mechanic so the on-screen action and the words are in sync.
- **BCRY**: on-screen `WantQuote.quote` and `sparkLine` re-synced to the new narration ("Fixed steps, not judgment.") so Liam's voice and the card don't split.
- **BHTF**: converted from "your turn handoff" to a proper LLM EXERCISE beat (per SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }`; narration ends with the "Go deeper:" follow-up. ClaudeComposerAsk `command` prop rewritten to mirror the paste-ready prompt with concrete inputs (current age 40, target retirement 65, target retirement income $80k, $120k college fund in 15 years, $150k assets, $20k/yr savings; then change retirement age to 60 and rerun) so the on-screen composer shows the same thing the viewer would paste. Second-to-last position preserved.
- **BOUT**: NikBearBrown outro. Narration reads the URL ("Brutalist dot art."), OutroCTA `handle` → `@NikBearBrown`, `line` → `"Is Claude's Financial Plan Its Own Judgment? Liam, in for Bear. www.brutalist.art"`. Bumped `estimated_duration_s` 6 → 7 for the extra clause.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF ClaudeComposerAsk `folderLabel` prop at `@HumanitariansAI`. SKILL.md is explicit only about the *outro* handle → NikBearBrown; the composer chip is on-screen source-context copy for a body beat. Matches sibling `nbb-financial-services--claude-liam-3-statement-model`. Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Preserved `estimated_duration_s`** on all body beats even though several Teardown rewrites run slightly longer than source. The clock is measured audio (`clock: narration`); those estimates get overwritten by real durations when `generate_audio_kokoro.py` runs. Left them as loose planning hints, exactly like sibling.
- **BHTF `estimated_duration_s` 26 → 40** — the LLM prompt paraphrase + full dig-deeper line materially lengthens the read; wanted the planning estimate to not lie by ~15s.
- **BHTF `act`** relabelled `"your turn handoff"` → `"LLM EXERCISE"` per SKILL.md schema.
- **No new beat inserted.** BHTF already occupied the "paste this into Claude" second-to-last slot with the right shot component (ClaudeComposerAsk). Adding a second card would be redundant. Converted the existing beat, same as sibling.
- **Concrete numbers in the LLM prompt** — SKILL.md §Step 3 says the prompt must produce a useful output on its own, without the video. A prompt that only asks the viewer to "give Claude a retirement age" does not; one with real inputs the viewer can paste unmodified does. Numbers chosen to make the anchor visible (retirement-age shift is what moves the plan) and to keep the four artifacts non-trivial.
- **Cream ground preserved** (`ground: #F3EBDD`, `style_preset: humanitarians`) even though `palette: teardown`. The scaffold set it and sibling kept it; the humanitarians cream is the paper for these Claude Basics reels, and Teardown palette rules apply to marks/accents on top.

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
