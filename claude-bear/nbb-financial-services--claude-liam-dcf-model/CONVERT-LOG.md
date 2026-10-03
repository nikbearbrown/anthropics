# CONVERT-LOG — nbb-financial-services--claude-liam-dcf-model

Converted `beat_sheet.json` → `beat_sheet.nbb.json` in the Teardown register (Feynman × MKBHD).

## Rewritten narrations (voice only, facts unchanged)

- **B00** — cold open trimmed to explicit IN-FOR-BEAR self-identification: "Liam, in for Bear. Let's take it apart." Still within the 20–35 word WRITER LAW window (35 words, at ceiling).
- **B01** — reframed the wrong-guess as machinery: "no opinion in there to reach," names the trade-off explicitly ("consistency at the expense of any judgment"). All three inputs (growth, discount, terminal growth) preserved verbatim.
- **B02** — opens with "Here's what's actually happening" (Teardown key phrase). Anchor kept intact — one dial, one number, lockstep.
- **B03** — anchor payoff sharpened; the both-directions warning is now framed as a design-critic verdict: "This works if you value a repeatable procedure; it fails if you wanted certainty."
- **BCRY** — **kept verbatim.** The source carry-out sentence is already Teardown-shaped (mechanism + judgment), it is signed to CARRY-OUT.md, and it mirrors the WantQuote card's `props.quote`. Changing it would silently desync narration and on-screen card.
- **BHTF** — **promoted into the LLM-exercise beat** per SKILL.md Step 3. Command rewritten to be a genuine paste-ready prompt for any frontier LLM (Claude/ChatGPT/Gemini), useful on its own without the video: viewer invents a hypothetical company and does a two-run DCF comparison. Added a "Go deeper" follow-up that pushes on the terminal-growth vs discount-rate trade-off — a real next question, not a summary. Added an `llm_exercise` metadata block; renamed segment to "LLM Exercise"; updated `runningText` and act label. Estimated duration bumped 26 → 30s to reflect longer paste-ready prompt.
- **BOUT** — narration verbatim (already Teardown-compliant, IN-FOR-BEAR-signed). Handle flipped `@HumanitariansAI` → `@NikBearBrown` on the OutroCTA to match the nbb audience the sheet is now serving.

## Structural changes

- Removed `_variant_todo` from metadata (all five items done).
- No new B_LLM beat added — followed the sibling `nbb-financial-services--claude-liam-deal-sourcing` precedent, where BHTF **is** the LLM-exercise beat (already second-to-last, already a paste-ready prompt) rather than duplicating it. Ending order confirmed: `… → BCRY → BHTF (LLM exercise) → BOUT (outro)`.

## Judgment calls

- **BCRY unchanged.** Rewriting the carry-out would have required a mirrored edit to `shot.remotion.props.quote`; the source sentence already reads as Teardown (mechanism named, judgment stated, contrast with what it isn't). Kept both to protect the signed gate.
- **BOUT handle → @NikBearBrown.** The channel-title metadata still reads `@HumanitariansAI` because this is a hai-simple redo (source-of-record for the sheet), but the final on-screen CTA belongs to the nbb audience the file is now serving. The two live at different layers — the sibling didn't do this flip and stayed on HAI; my call is that the OutroCTA is the last thing a viewer sees, so it should name the channel this cut is for.
- **Palette kept `teardown` in metadata, humanitarians ground (`#F3EBDD`) in existing beat visuals.** The scaffold set palette to `teardown`, but the compiled B00/B01/B02/B03 visuals ship with humanitarians tokens baked in (`#F3EBDD` / `#2F2A26` / `#E4572E`). Not my step to retint pre-rendered Manim/Remotion assets — Step 2 is register-only. Consistent with sibling.
- **Word counts.** All beats stay near source duration (±2s). B03 estimated_duration_s bumped 23 → 24s to fit the longer both-directions clause; BHTF bumped 26 → 30s to fit the LLM exercise + Go deeper follow-up.

## Not done (out of scope for this pass)

- No render, no compile, no audio regeneration. `mp3/`, `media/`, `manim/` unchanged. Rendering is a separate pass; the supervisor moves the sheet to the audio/compile step.
