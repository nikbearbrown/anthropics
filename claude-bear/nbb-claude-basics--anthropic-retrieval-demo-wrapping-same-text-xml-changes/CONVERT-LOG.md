# CONVERT-LOG — claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes

Converted the scaffold at `beat_sheet.nbb.json` from the Plain / hai-simple
source into the NikBearBrown / Teardown cut. Voice: Liam (Kokoro `am_onyx`), in
for Bear. No render, no audio, no compile — sheet only.

## What changed

- Removed `_variant_todo` from metadata. Every beat now carries the finished
  narration, and the LLM exercise + outro are in place.
- Rewrote all eight `narration_text` fields in the Teardown register (Feynman ×
  MKBHD): take it apart, explain how the training distribution actually shapes
  the answer, name the design trade-off (Anthropic optimized for legible
  structure at the cost of asking you to provide it). Facts held constant — no
  numbers or examples changed; the product-description case and the Robot
  Building Kit / title-content-category example survive intact.
- **B00** cold open now opens with "Liam here, in for Bear." — matches the
  IN-FOR-BEAR LAW and every other completed nbb reel's cold open. The
  BrutalistHesitantWriter visual (text, triggerWords, replacementWords) is
  untouched — narration and visual are independent.
- **BCRY** carry-out narration rewritten; also updated the `WantQuote.quote`
  prop to the shorter, tighter Teardown carry-out line ("XML tags aren't
  decoration — they're the training distribution talking back."). Kept the
  original `sparkLine` ("Structure is a constraint, not decoration.") — it
  already fits the register perfectly.
- **BHTF** promoted to the LLM EXERCISE beat per the nbb SKILL.md §Step 3:
  - `act` changed from "your turn handoff" to "LLM EXERCISE".
  - Added `llm_exercise: { prompt, dig_deeper }` — a paste-ready prompt that
    tells the viewer to run the plain-versus-tagged test on their own text
    (Version A / Version B, three requirements each: summary, key-fact quote,
    confidence rating) + a "Go deeper" follow-up that asks whether tag
    *semantics* (`<title>` vs generic `<a>`) actually matter and how you'd
    design the experiment.
  - Updated the ClaudeComposerAsk `command` prop to the same prompt (trimmed
    for readability on the composer card) and the `segment` label to "Plain vs.
    XML — run it yourself" (the previous "Your Turn" placeholder no longer named
    what the beat is).
  - Kept `folderLabel: @HumanitariansAI` — matches the closest completed
    reference (nbb-books--claude-liam-enterprise-search), which kept the source
    handle on the composer card. Not re-tagging to @NikBearBrown without a
    clearer signal.
- **BOUT** narration tightened from "Why wrapping the same text in XML changes
  the answer Claude gives. Liam, in for Bear." → "Why wrapping the same text in
  XML changes Claude's answer. Liam, in for Bear." Matches the shorter outro
  cadence in the reference nbb sheets. `OutroCTA.line` updated to match.
- Bumped `estimated_duration_s` on B00/B01/B02/B03/B04/BCRY/BHTF/BOUT to
  reflect the new narration word counts. These are estimates only — audio
  generation will measure the actual durations.

## Judgement calls

- **Where to put the LLM exercise.** The nbb SKILL.md allows either inserting a
  new `B_LLM` beat second-to-last (see the research reel with 25 beats) or
  promoting an existing "your turn" handoff beat into the LLM EXERCISE role
  (see the completed 8-beat enterprise-search reel). This reel already had a
  BHTF beat with a ClaudeComposerAsk paste-ready prompt sitting second-to-last —
  the same shape as the enterprise-search template — so I promoted BHTF in
  place rather than inserting a new beat and losing the existing shot props.
  Ending order is body → [BCRY carry-out] → [BHTF LLM exercise] → [BOUT
  outro]; BCRY is not itself the LLM exercise, but it sits before the
  second-to-last per the same enterprise-search precedent.
- **Kept `channel_title` / `folderLabel` = `@HumanitariansAI`.** The completed
  8-beat nbb reels I checked keep the source channel handle even in nbb cuts;
  I matched that rather than re-tagging to `@NikBearBrown`.
- **Kept the visual `mechanic` prose (production_viz labels and mechanics)
  unchanged.** They already fit the Teardown register and they describe the
  Manim scene, not the narration — rewriting them would drift the render.
- **B03 is the longest beat (~32s estimated).** The Teardown rewrite deepens
  the mechanism description (adds the "billions of examples", the "processed
  coherently vs. has to guess" reframing, and the explicit design trade-off).
  Longer than the source's 19s, but the design analysis is the point of a
  Teardown mechanism beat — the trade-off is where the beat earns its keep.

## Not done here

- No `python3 runtime/scripts/generate_audio_kokoro.py [dir]`.
- No `python3 runtime/scripts/compile.py [dir] --height 1080`.
- No render, no publish. Supervisor's next pass handles those.
