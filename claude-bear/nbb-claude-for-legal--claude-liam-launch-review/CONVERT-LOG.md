# CONVERT-LOG — claude-for-legal--claude-liam-launch-review

Converted the scaffold at `beat_sheet.nbb.json` from the Plain / hai-simple
source into the NikBearBrown / Teardown cut. Voice: Liam (Kokoro `am_onyx`), in
for Bear. No render, no audio, no compile — sheet only.

## What changed

- Removed `_variant_todo` from metadata. Every beat now carries the finished
  narration, and the LLM exercise + outro are in place.
- Rewrote all eleven `narration_text` fields in the Teardown register (Feynman ×
  MKBHD): take the "skill" word apart, explain the actual machinery (folder +
  one SKILL.md, read top-to-bottom before Claude starts), and name the design
  trade-off — Anthropic optimized for repeatability at the cost of any judgment
  outside the file. Facts unchanged: still one folder, one SKILL.md, still
  step-by-step in written order, still no branching unless the file says
  branch, still same behavior every run, still "off the map = no special
  opinion."
- **B00** cold open now opens with "Liam here, in for Bear." — matches the
  IN-FOR-BEAR LAW and every completed nbb reel's cold open. The
  BrutalistHesitantWriter visual (text, triggerWords `approves` →
  `replacementWords` `checks`, seed `hai-launch-review`) is untouched —
  narration and visual are independent.
- **BCRY** carry-out narration rewritten in Teardown cadence. Also updated the
  `WantQuote.quote` prop to a shorter Teardown line ("A skill isn't sign-off —
  it's the same checklist, walked in the same order, every time. Everything
  outside the file is still on you."). Kept the `sparkLine` ("Checklist, not
  authority.") — it already fits Teardown perfectly and matches the anchor
  language of B01/B06.
- **BHTF** promoted from "your turn handoff" to the LLM EXERCISE beat per
  nbb SKILL.md §Step 3:
  - `act` changed from "your turn handoff" to "LLM EXERCISE".
  - Added `llm_exercise: { prompt, dig_deeper }`. The prompt is a paste-ready
    block that asks the model to interview the viewer for one decision they
    already check the same way, then draft an ordered-step SKILL.md, then read
    the file back and walk through what the model will actually check — so the
    viewer can catch the drift between the checklist and the real check. The
    dig-deeper prompt names the exact limit the video's B05/B07 beats set up:
    which step is really a judgment call the checklist can't hold.
  - Updated the ClaudeComposerAsk `command` prop to a trimmed version of the
    same prompt (fits the composer card), and the `segment` label to "Write me
    a SKILL.md — run it yourself" (the previous "Claude, Launch Review." was
    just the video title, not what the beat does).
  - Kept `folderLabel: @HumanitariansAI` and `channel_title: @HumanitariansAI`
    — the completed 8-beat nbb reference reel
    (nbb-claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes)
    kept the source handle on the composer card. Matching that precedent
    rather than re-tagging to @NikBearBrown.
- **BOUT** narration tightened to the reference nbb cadence: "What a skill
  actually is. Liam, in for Bear." (was: "Claude, Launch Review. Liam, in for
  Bear.") — matches the "one carry-out phrase + Liam sign-off" shape in the
  reference. `OutroCTA.line` prop updated to match.
- Bumped `estimated_duration_s` on every rewritten beat to reflect new word
  counts. Estimates only — audio generation will measure actuals. Removed all
  `actual_duration_s` fields (the scaffold had already stripped them; leaving
  them out is correct — they belong to the old Plain audio).

## Judgement calls

- **Promoted BHTF in place; did not insert a new B_LLM beat.** nbb SKILL.md
  allows either shape. This reel already had BHTF sitting second-to-last with
  a ClaudeComposerAsk paste-ready prompt — same shape as the enterprise-search
  and anthropic-retrieval-demo references. Promoting BHTF preserved its
  Remotion shot props and kept the beat count at 11. Ending order is body →
  [BCRY carry-out] → [BHTF LLM exercise] → [BOUT outro]; BCRY is not the LLM
  exercise, but it sits before the second-to-last per the same reference
  precedent.
- **Kept every Manim `production_viz` block untouched** (labels, chips,
  accents, strikes, captions, colors — including the humanitarians `#F3EBDD`
  ground and `#E4572E` accent in each beat's `colors` array). They describe
  the rendered scene, not the narration, and the source visuals still land
  the Teardown beats' mechanism. Re-tinting to pure teardown white/ink/red
  here would drift the render from the existing manim/*.mp4 files that the
  scaffold's `build.status: MANIM` still points at. If a re-skin is wanted,
  it's a render pass, not a narration rewrite.
- **B03 lengthened from ~13s → ~22s.** Teardown demands the "not a plug-in,
  not a permission — a document" line that stripes the "skill" jargon and
  names what the file actually is. That's where a Teardown mechanism beat
  earns its keep, so I let it run.
- **B05 keeps the explicit "they optimized for X at the expense of Y"
  formulation** ("They optimized for the same steps running twice; they gave
  up any adapting mid-run.") — this is exactly the Teardown / MKBHD sentence
  shape PROSE.md calls for, and it seats the payoff/limit pair the anchor
  needs to pay off at B06.
- **Left `topic: "CLAUDE · SKILLS"` and `subtitle: "What a Skill Actually Is"`
  intact.** They already carry the Teardown framing (what is it *actually*),
  and they thread the outro line.

## Not done here

- No `python3 runtime/scripts/generate_audio_kokoro.py [dir]`.
- No `python3 runtime/scripts/compile.py [dir] --height 1080`.
- No render, no publish. Supervisor's next pass handles those.
