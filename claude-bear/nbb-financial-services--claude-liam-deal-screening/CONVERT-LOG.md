# CONVERT-LOG — financial-services--claude-liam-deal-screening

Source register: **Plain** (the source sheet's `register` was `Plain`, the hai-simple audience; the scaffold flipped `register` to `Teardown` but the narration itself was still Plain).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts preserved unchanged:
  - a skill is a folder Claude reads before it works; SKILL.md holds plain-language instructions; the file is the program;
  - the instructions live in a Steps section; Claude runs them top-to-bottom, linear, no branching unless a step says so;
  - deal-screening's three-step job = pull deal metrics, run pass/fail against the fund's investment criteria, output a one-page screening memo;
  - what isn't in the SKILL.md's steps isn't part of the job;
  - the carry-out: deal-screening doesn't decide whether the fund should pursue the deal — it runs the pass/fail checks against your criteria and hands you a memo, the same way every time.
- **BCRY**: on-screen `WantQuote.quote` re-synced to the new narration so Liam's voice and the card don't split. `sparkLine` kept at the original title-echoing `"Screens the deal. Doesn't decide it."` — brand cohesion with `metadata.title`.
- **BHTF**: converted from "your turn handoff" to a proper **LLM EXERCISE** beat (per SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }`; narration includes the `"Go deeper: …"` follow-up; `ClaudeComposerAsk.command` rewritten to mirror the paste-ready prompt with concrete assumptions (Coastal Freight Co., $60M revenue, $9M EBITDA, $12M net debt, $75M asking EV, ~18% top-customer concentration; criteria: NA industrials, $5–15M EBITDA, EV/EBITDA <8x, ≤25% concentration) so the composer chip on screen shows the same thing the viewer would paste. Second-to-last position preserved. `act` relabelled `"your turn handoff"` → `"LLM EXERCISE"`.
- **BOUT**: NikBearBrown outro. Narration reads the URL ("Brutalist dot art."), `remotion.pattern` moved `OutroSeries` → `OutroCTA`, `handle` → `"@NikBearBrown"`, `line` → `"Screens the Deal. Doesn't Decide It. Liam, in for Bear. www.brutalist.art"`. Bumped `estimated_duration_s` 6 → 7 for the extra clause.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF `ClaudeComposerAsk.folderLabel` prop at `@HumanitariansAI`. SKILL.md is explicit only about the *outro* handle → NikBearBrown. The composer chip is on-screen source-context for a body beat, and preserving it matches the sibling `nbb-financial-services--claude-liam-3-statement-model` sheet in this book. Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Preserved `sparkLine` on BCRY** even though the quote was rewritten. The spark echoes `metadata.title` and is the title beat of the reel — swapping it would fracture the brand hit. The narration/quote pair still ends on "The judgment is still yours.", which lands the same claim in a Teardown voice.
- **`estimated_duration_s` bumps.** Left NB01/NB02/NB03/BCRY estimates loose (they get overwritten by real durations when `generate_audio_kokoro.py` runs; `clock: narration`), but bumped where the Teardown rewrite materially lengthened the read so the planning estimate doesn't lie by >5s: NB01 16→22, NB02 11→17, NB03 19→28, BCRY 10→13, BHTF 24→42 (added the dig-deeper line), BOUT 6→7.
- **No new beat inserted.** BHTF already occupied the "paste this into Claude" second-to-last slot with the right shot component — converting it in place was cleaner than adding a redundant card.

## Ending order (verified)

```
B00   hesitant writer cold open
NB01  mechanism  (skill = folder)
NB02  mechanism  (steps run linear)
NB03  mechanism  (three-step job, off-list = not part of job)
BCRY  carry-out
BHTF  LLM EXERCISE                ← second-to-last
BOUT  outro (NikBearBrown)        ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run.
