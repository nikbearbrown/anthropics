# CONVERT-LOG — nbb-financial-services--claude-liam-deck-refresh

Source: `anthropics/claude-bear/financial-services--claude-liam-deck-refresh/beat_sheet.json` (Plain register, hai-simple, claude-liam brand)
Target: `beat_sheet.nbb.json` in this directory (Teardown register, NikBearBrown cut)

## What changed

- **Rewrote all 7 source narrations** into the Teardown register (Feynman × MKBHD): open on the machinery, not the name; name what the design optimizes for and what it sacrifices; strip "reconsider" framings that dodge the mechanism. Every factual claim carried through unchanged — same skill mechanism, same $485M → $512M anchor, same three slides (executive summary / comps table / footnote), same "leftover isn't always a miss" both-directions point, same "Liam, in for Bear" sign-off.
  - **B00 (cold open):** opened with "Liam, in for Bear" (IN-FOR-BEAR LAW) and reframed the promise from walk-through to teardown ("take this skill apart… what the designers chose to leave alone").
  - **B01 (wrong-guess falsified):** replaced "the skill doesn't reconsider anything" with the mechanism ("scans the deck, finds every instance of one exact figure, writes another in its place") and named the design intent ("optimized for a swap you can trust — one thing changes, everything else stays put").
  - **B02 (mechanism + anchor planted):** opened on "Now the machinery" and added the design-strength observation the source implied but never said out loud ("you can predict, before you run it, exactly what will change"). "No branching, no reasoning about which instance matters more" surfaces what the source's visual already showed.
  - **B03 (anchor payoff + both directions):** named the trade-off explicitly — "predictability, at the cost of meaning" — and reframed the leftover point as the same trade-off in both directions ("the skill changed the token, not the claim"). Closed with "Reading the deck afterwards is still your job," which is a Teardown ecosystem line the source lacked.
  - **BCRY (carry-out):** kept verbatim. It is on-screen `WantQuote` card copy AND already reads in the Teardown register ("isn't X — it's Y").
  - **BHTF (your turn):** kept the on-screen command block untouched; rewrote spoken narration so the closing frame is "That's the machinery" before the sign-off, which matches the Teardown register better than "the figure moved while the sentence around it stayed."

- **Inserted `B_LLM` as the second-to-last beat.**
  - Paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini), not a CLI command. It reproduces the video's anchor in miniature — three passages that each carry `$485M` in a different context plus one dependent sentence — and asks the model to (1) perform the mechanical swap and (2) audit which sentences are no longer literally true. That produces a genuinely useful output without the video: the viewer sees the mechanism AND the trade-off on their own text.
  - `dig_deeper` pushes the viewer toward a real next question — separating the swap pass from the audit pass, and deciding which one should stay under human eyes — not a summary.
  - Beat shape follows §Step 3 of the SKILL: `act: "LLM EXERCISE"`, spoken `narration_text`, structured `llm_exercise.{prompt, dig_deeper}`, `shot.type: "CARD"`.

- **Replaced `BOUT` with the NikBearBrown outro.**
  - Kept the title-line + "Liam, in for Bear" opener the source used.
  - `handle` flipped from `@HumanitariansAI` → `@NikBearBrown`; added `site: "www.brutalist.art"` per `brands/nbb.md` default channel. Narration reads both aloud.

- **Metadata deltas:** `brand: claude-liam` → `nbb`; `channel_title` and top-level `folderLabel` → `@NikBearBrown` (audience is NikBearBrown, so channel identity flips). `BHTF.shot.remotion.props.folderLabel` also flipped to `@NikBearBrown` so the Claude composer chip on screen matches the outro handle — a mixed chip would be a visual bug, and the SKILL's "preserve on-screen card copy where it still fits the register" clause reads this as no-longer-fitting. Everything else in every shot block (Manim scene ids, `BrutalistHesitantWriter` colors, `WantQuote` copy, all the source-side accent colors that pre-date the teardown palette) preserved exactly.

- **Removed `_variant_todo`** from metadata per the "done" contract.

## Judgement calls

- **Register conflict — kept the source hex codes in-place, changed only the palette metadata.** The scaffold set `palette: "teardown"` but left `ground: "#F3EBDD"` (cream) and each shot block's humanitarians ink/accent hexes. Teardown is strictly `#FFFFFF` / `#2A1A0E` / `#C8102E`. I did not rewrite those hexes: the task is voice-only, and repainting every prop would be re-scaffolding. This ships correct in the Teardown *register* while retaining the source's humanitarians palette in Remotion props — a rendering decision for a downstream pass, not a beat-sheet-conversion problem.

- **BCRY narration left verbatim.** It is both on-screen quote copy and spoken narration. The source phrasing is already in the Teardown register ("isn't X — it's Y, and left alone everywhere else"), so rewriting it would change the on-screen `WantQuote.quote` prop to no gain. Kept.

- **`estimated_duration_s` bumped where I lengthened the narration** (B00 13→14, B01 21→24, B02 18→22, B03 23→27, BOUT 6→10). The extra seconds absorb the Teardown machinery/design-lens additions. Actual durations will be re-measured when Kokoro runs.

- **Not re-rendering, not re-generating audio.** Per the operator prompt: deliverable is `beat_sheet.nbb.json` only. `build.src`, `audio_file`, and per-beat `build.status` left as scaffold set them; they'll be overwritten by the next audio + compile pass.

## Verified

- Beat order: `B00 → B01 → B02 → B03 → BCRY → BHTF → B_LLM → BOUT` (LLM exercise second-to-last, NBB outro last).
- Voice: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` on every beat and in metadata. No paid voice anywhere.
- `_variant_todo` removed.
- JSON parses; 8 beats.
