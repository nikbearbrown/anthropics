# CONVERT-LOG — nbb cut of `financial-services--claude-liam-equity-research`

Source → NBB rewrite of `beat_sheet.json` into `beat_sheet.nbb.json`.
Voice-only. Every fact, count, source name (analyst consensus estimates,
fundamentals, historical prices, macro context), gate name, prop shape, and
scene id from the source survives unchanged. Scaffold metadata (`audience`,
`engine`, `voice_kokoro`, `palette`, `register`, `outro_source`, `derived_from`,
`typography`) left in the state `brand_variant.py` wrote.

## What changed

- **Every `narration_text` rewritten in the Teardown register.** Feynman × MKBHD:
  - **B00** — cold-open reframed as a takedown. "Trained analyst inside the
    model" → "written file, plain language, on disk." Word count kept inside
    the 20-35 WRITER LAW window; trigger/replacement pair unchanged.
  - **B01** — explains the machinery of a Claude Skill (a folder Claude reads
    before it works — not a specialized model, not extra training) and names
    the four inputs verbatim from the source.
  - **B02** — the four-step run explained as a **deterministic pipeline**, and
    the design trade named out loud: "they optimized for a legible, repeatable
    pipeline over adaptive judgment."
  - **B03** — the anchor payoff carries the sharper judgment. The "no step lights
    up" moment reframed as "the design being honest about its edges." The
    reverse case ("clean snapshot ≠ checked/judged") capped with "Assembly is
    not validation" and a Teardown value trade: "This works if you value an
    auditable pipeline; it fails if you needed judgment the file never wrote
    down."
  - **BCRY** — left verbatim. The source's carry-out sentence is already the
    Teardown thesis and is duplicated into the `WantQuote.quote` prop; rewriting
    it would have desynced spoken and on-screen copy.
  - **BOUT** — left verbatim. Standard nbb outro shape (episode title + "Liam,
    in for Bear.") already matches every sibling nbb reel.
- **BHTF turned into the explicit LLM-exercise beat** (SECOND-TO-LAST). Followed
  the sibling nbb precedent (`nbb-claude-basics--claude-liam-four-places-your-data-goes`,
  `nbb-claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context`)
  which folds the exercise into the existing `your turn handoff` rather than
  inserting a duplicate `B_LLM` slot. Changes:
  - `act` renamed to `"your turn handoff / LLM exercise"` so the role is
    unambiguous.
  - New `llm_exercise` block per SKILL.md schema:
    - `prompt` — paste-ready for Claude / ChatGPT / Gemini. Asks the model to
      draft a plain-language SKILL.md for equity research on a company the
      viewer cares about, combining the same four sources, **and** explicitly
      list three questions the file will NOT answer (including "should I buy
      the stock") with a reason each is out of scope. No CLI, no local files —
      works on its own, produces a useful audit + a scoped-out list.
    - `dig_deeper` — a genuinely explorable follow-up the video doesn't answer:
      *if you added a fifth source of your own choosing, which would move the
      file closest to actually judging whether to buy, and which would just add
      noise?* Real design-critic question, not a summary.
  - Narration reads the prompt out loud, closes with the explicit "Go deeper:"
    follow-up, and ends "Liam, in for Bear."
  - `ClaudeComposerAsk.command` prop rewritten to match the new prompt so
    on-screen copy and spoken copy agree.
  - `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".
- **`_variant_todo` removed** — all five checklist items are now done.
- **`purpose` line rewritten** to state the Teardown framing explicitly:
  mechanism (plain-language SKILL.md, four written steps into one snapshot),
  design trade (legible/repeatable at the cost of adaptive judgment), carry-out
  (Claude only runs steps that are written down).
- **`estimated_duration_s` bumped** on beats whose narration got longer
  (B01 20→22, B02 22→25, B03 22→28, BHTF 32→46). Estimates only; the
  audio-first pipeline will replace them with measured `actual_duration_s` from
  regenerated Kokoro mp3s. B00, BCRY, BOUT unchanged. `actual_duration_s` cleared
  by the scaffold on every rewritten beat — left off so nothing downstream
  mistakes stale pre-rewrite durations for the truth.

## Judgment calls

1. **No new `B_LLM` beat.** SKILL.md §Step 3 gives a `B_LLM` schema, but this
   source's `BHTF` already IS the "your turn / paste-this-prompt" beat, and the
   two sibling nbb reels cited above resolve the same collision the same way —
   fold the exercise into `BHTF`. Inserting a separate `B_LLM` slot would have
   created two sequential handoffs and doubled the "your turn" moment.
2. **Outro handle stayed `@HumanitariansAI`.** Matches sibling convention and
   the rest of the metadata the scaffold preserved (`channel_title`,
   `folderLabel`, `playlist: "Claude Basics"`). This is a hai-simple source
   destined for that channel; overriding only the outro handle to
   `@NikBearBrown` would contradict the rest of the sheet. A whole-reel flip is
   a bigger metadata edit than a register rewrite and belongs elsewhere.
3. **BCRY narration + `WantQuote.quote` prop preserved verbatim.** The source
   sentence is already Teardown-clean ("written file of steps, and Claude only
   runs the steps that are written down") and it's the on-screen quote the
   viewer reads along with. Rewriting narration without matching the quote —
   or rewriting both without a reason — would break the beat's whole design.
4. **On-screen card copy preserved.** BrutalistHesitantWriter text and
   trigger/replacement pair (B00), production_viz `label` and `mechanic`
   (B01/B02/B03), `WantQuote.quote` + `sparkLine` (BCRY), `ClaudeComposerAsk`
   `greeting` / `topic` / `segment` (BHTF), `OutroCTA.line` + `handle` (BOUT)
   all Teardown-compatible or already-Teardown. Only `BHTF.command` and
   `BHTF.runningText` edited to match the sharpened prompt.
5. **Manim scene ids left untouched.** `EQRB01Scene`, `EQRB02Scene`,
   `EQRB03Scene` build the four-step ANCHOR sequence the new narration names
   out loud ("pull the analyst consensus estimates, pull the fundamentals, pull
   the historical prices, pull the macro context") — voice and visual reinforce.
6. **Design trade named at exactly two beats.** B02 names *what they optimized
   for* (legible repeatable pipeline over adaptive judgment); B03 names *what
   that trade costs* (no adaptive judgment on questions the file doesn't cover;
   no validation past assembly). Kept the naming to those two beats rather than
   scattering it across the whole reel — B01 stays mechanism-only, BCRY stays
   the crisp carry-out, and BHTF turns the trade into an exercise the viewer
   runs themselves.
7. **`anchor_pair` and `build` metadata preserved verbatim.** The B02→B03
   anchor logic and the 7/7 filled build status describe the visual/audio state
   the source shipped in; a register rewrite doesn't change either.

## Ending order (verified)

B00 → B01 → B02 → B03 → BCRY → **BHTF (LLM exercise)** → **BOUT (outro)**.
