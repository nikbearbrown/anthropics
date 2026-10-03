# CONVERT-LOG — nbb-claude-for-legal--claude-liam-cold-start-interview

Register conversion: **Plain (hai-simple) → Teardown (NikBearBrown)**.
Source: `claude-for-legal--claude-liam-cold-start-interview/beat_sheet.json`.
Output: `beat_sheet.nbb.json` (this dir).

## What changed

**Register rewrite (every body beat).** Every `narration_text` now takes the machinery
apart, names what the design was optimized for, and calls the trade-off. Facts,
`beat_id`s, `act` labels, `shot` blocks, graphic mechanics, and Manim scene bindings
are unchanged.

- **B00 (cold open)** — reframed as brief-as-data-dump vs interview-as-protocol; the
  hesitation on "brief → interview" now lands on that distinction. Trimmed to
  35 words to hold under the BrutalistHesitantWriter TIMING LAW (20–35).
- **B01 (stakes / wrong guess)** — names the design flaw of briefing directly:
  "works if you value coverage of what you remembered; fails on what you assume
  goes without saying." Retains the three original gap examples verbatim
  (jurisdiction, conflicts, retainer scope).
- **B02 (mechanism / ANCHOR PLANTED)** — explicitly names the trade-off ("traded
  your judgment about what's unusual for uniform coverage on every matter") and
  keeps the jurisdiction anchor intact for the B03 payoff.
- **B03 (anchor payoff / both directions)** — restructured as an honest-limit
  passage: per-matter guarantee only, then the thorough≠complete distinction
  stated as machine properties, not vibes.
- **BCRY (carry-out)** — tightened ("one thing an interview does that a memory
  can't"). `WantQuote.quote` prop updated in lockstep so on-screen card and
  narration remain identical.

**LLM exercise inserted second-to-last (BHTF).** Repurposes the original "your
turn handoff" beat (same beat_id, same `ClaudeComposerAsk` visual) as the
LLM-EXERCISE beat per SKILL Step 3:

- `llm_exercise.prompt` — paste-ready intake request that works standalone in any
  frontier LLM; derived from the video's subject (cold-start intake, fixed script,
  one-at-a-time answers).
- `llm_exercise.dig_deeper` — "which questions still matter on your tenth matter,
  which only matter on the first" — a genuine next question about the design of
  the intake, not a summary of what the video said.
- `ClaudeComposerAsk.command` prop updated to match `llm_exercise.prompt` verbatim
  so the on-screen composer text and the narration line up.
- `act` on BHTF changed from `your turn handoff` → `LLM EXERCISE` to match the
  reference NBB pattern (e.g. `nbb-books--claude-liam-building-plugins`).

**Outro (BOUT) as last beat.** Kept the source `OutroCTA` with handle
`@HumanitariansAI` and the "Liam, in for Bear" sign-off — same pattern the
sibling nbb-legal reels use. Not switched to `OutroSeries` because the source
already used `OutroCTA` and both are documented as valid teardown outro
components; least visual change, same NBB register.

## Judgement calls

- **Graphic `production_viz.colors` and Manim scene ids left untouched.** The
  scaffold flipped `metadata.palette` to `teardown`, but the per-beat graphic
  color arrays (`#F3EBDD / #2F2A26 / #E4572E / #1F4E5F`) and the `CSIB0[123]Scene`
  Manim references belong to already-rendered `manim/*.mp4` assets and to the
  in-place source `production_viz` payload — edits there would be a re-skin,
  which is outside the register-conversion scope ("change the voice, not the
  facts"). The reference nbb sibling reels also leave these alone.
- **`estimated_duration_s` bumped** on B01–B03 (20→26, 18→24, 21→26) and
  BHTF (24→40) to reflect the longer Teardown prose and the two-part LLM
  exercise (prompt + dig-deeper). Real values will be measured after
  `generate_audio_kokoro.py`; these are planning hints only.
- **B00 was capped at 35 words** to hold the BrutalistHesitantWriter TIMING LAW
  in the note field, even though a fuller Teardown intro was possible. The
  visual is a fixed 9-second typing window; longer narration would desync the
  correction.
- **`_variant_todo` removed** — scaffold checklist obsolete once conversion is
  applied.

## Not done

- Not rendered. Not compiled. No audio generated. Deliverable is
  `beat_sheet.nbb.json` only, per the invocation contract.
