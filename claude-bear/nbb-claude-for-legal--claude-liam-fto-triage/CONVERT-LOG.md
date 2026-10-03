# CONVERT-LOG — nbb-claude-for-legal--claude-liam-fto-triage

Register conversion from `../claude-for-legal--claude-liam-fto-triage/beat_sheet.json`.
Voice-only rewrite: no fact changed, no beat added or dropped without a reason logged below.

## What changed

- **Register rewritten (all 6 body beats).** Every `narration_text` re-voiced from
  Plain into Teardown (Feynman × MKBHD): take the skill apart, name the design
  choice (screen, not clearance), state the trade-off (repeatability at the cost
  of creative reasoning). Facts, beat IDs, act names, on-screen card copy, and
  `shot.remotion.props` are preserved verbatim except where explicitly noted below.
- **BCRY quote card tightened.** The `WantQuote` `quote` and `sparkLine` were
  updated to match the new Teardown carry-out phrasing (screening vs clearance).
  On-screen quote now reads: "Same checklist in, same triage report out, every
  time. The clearance call is still yours." — same meaning as the source, in
  Teardown-register wording, kept short enough to sit on one card.
- **BHTF promoted to the LLM-exercise beat.** Act renamed
  `your turn handoff / LLM exercise`; added the structured `llm_exercise` block
  (paste-ready `prompt` + `dig_deeper` follow-up per SKILL.md §Step 3). The
  narration reads the prompt with the viewer, lands the "a flag is a question
  you still have to answer with a person" beat, then delivers the dig-deeper
  question. `ClaudeComposerAsk` props updated: `topic` →
  `YOUR TURN · FTO-TRIAGE`, `segment` → `Screening, not clearance.`, `command`
  → the paste-ready prompt, `runningText` → `paste this into Claude, ChatGPT,
  or Gemini…`. `folderLabel` kept as `@HumanitariansAI`.
- **Outro consolidated to a single OutroCTA (LAST beat).** Source had two
  outro beats — `BOUT` (`OutroSeries`, "Claude, Fto Triage.") and `BCTA`
  (`OutroCTA`, "…Liam, in for Bear."). Every fully-converted nbb sibling on
  disk (e.g. `nbb-claude-basics--claude-liam-four-places-your-data-goes`,
  `nbb-books--claude-liam-legal-finance`, `nbb-claude-quickstarts--claude-liam-first-run`)
  collapses these into a single `OutroCTA` reading `"Title. Liam, in for Bear."`.
  This sheet follows that precedent — `BOUT` is now the single OutroCTA
  ("Claude, Fto Triage. Liam, in for Bear.") and `BCTA` is dropped.
- **`_variant_todo` removed** from `metadata` (the four register/exercise/outro/order
  items are done; the fifth was a build step, which is a separate pass).

## Judgement calls

1. **B00 cold-open card copy kept as-is.** The `BrutalistHesitantWriter`
   trigger word "CLEAR" → replacement "triage" is exactly the wrong-guess the
   new Teardown narration disassembles ("clearing is a legal opinion; this
   skill won't produce one"). Card copy still fits the register — preserved
   per SKILL.md §Step 2.
2. **Outro consolidated (see above).** Sibling-precedent > source structure
   because the source's split OutroSeries + OutroCTA pattern is a hai-simple
   convention, not the NikBearBrown outro convention. The nbb outro per the
   converted-sibling corpus is a single OutroCTA sign-off. Chose the sibling
   precedent to keep this sheet consistent with the rest of the nbb channel.
3. **BOUT act name kept as `"outro"`** (not renamed to something like
   "NikBearBrown outro") — matches every converted sibling's act naming.
4. **LLM-prompt design.** The prompt is deliberately generic ("[paste your
   feature description]") so it produces a useful first-pass FTO screen on any
   feature the viewer brings, without needing the video. The dig-deeper
   question (smallest description change that flips a flag) is a genuinely
   open question the reel itself does not answer — pushes past summary into
   exploration.
5. **`build.filled` left at `8`** to match the scaffold's snapshot. The beat
   count is now `7` (BCTA dropped, no other beats added). Compile is a
   separate pass and will overwrite this counter; leaving the scaffold value
   in place avoids inventing build metadata this pass didn't produce.

## Not done (out of scope for this pass)

- Audio generation (`generate_audio_kokoro.py`).
- Compile / render.
- Any modification of the source `beat_sheet.json` or its media.
