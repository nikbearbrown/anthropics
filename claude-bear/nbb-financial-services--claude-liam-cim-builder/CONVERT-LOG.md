# CONVERT-LOG — financial-services--claude-liam-cim-builder → nbb

Register: Plain → Teardown (Feynman × MKBHD). Voice: Kokoro `am_onyx` (Liam, in
for Bear). All facts preserved; wording only.

## Beat-by-beat changes

- **B00** (hesitant writer cold open) — narration rewritten. Opened with a
  design observation ("Assume cim-builder writes your CIM and you'll be
  disappointed"), named the mechanism directly ("a fixed set of steps that
  structure one, run the same way each time"), landed the same real question
  ("does cim-builder structure my CIM?"). Remotion `text`/`triggerWords`/
  `replacementWords`/`seed` untouched — those are the typed on-screen artifact.
- **NB01** — added mechanism framing ("that's the whole mechanism") and the
  design judgment sentence Teardown wants ("They optimized for readability over
  cleverness"). Every claim survives: skill = folder, one file = SKILL.md,
  plain English, no hidden logic, file is the program.
- **NB02** — tightened rhythm; added "Linearity is the whole point" to name
  the design choice. Steps section + in-order execution + branching-only-if-a-
  step-says-so all preserved.
- **NB03** — reframed as a deliberately-narrow design decision and named the
  tradeoff explicitly ("consistency for range: same output shape every time,
  at the cost of anything novel"). CIM definition, sell-side M&A, formatting
  consistency, and "not in SKILL.md's steps → off the map" preserved verbatim
  in substance.
- **BCRY** — micro-refined for cadence and updated the `WantQuote` `quote`
  prop in sync so the on-screen quote matches the spoken line. `sparkLine`
  ("Runs the steps. Doesn't write the deal.") kept — already Teardown.
- **BHTF** — this is the LLM-exercise beat (matches the pattern in
  `nbb-financial-services--claude-liam-deal-sourcing` and
  `nbb-financial-services--claude-liam-gl-recon`: the source's own
  "your turn handoff" IS the paste-into-Claude prompt, so a separate `B_LLM`
  is not inserted — this beat sits second-to-last as required). Changes:
  - `act` relabeled `"your turn handoff"` → `"LLM EXERCISE"` per SKILL.md
    §Step 3.
  - Added `llm_exercise` object with `prompt` (the exact string in the
    `ClaudeComposerAsk` `command` prop) and `dig_deeper` (a real follow-up
    question, not a summary: which sections did Claude invent from thin
    material — that's where judgment has to land).
  - Narration extended to read the dig-deeper line aloud. `estimated_duration_s`
    bumped 24 → 34 to cover the added ~10s of copy at Kokoro's ~3.5 wps.
  - `ClaudeComposerAsk` props untouched (the `command` prop is the paste-ready
    artifact and stays verbatim).
- **BOUT** (outro) — narration kept ("Runs the Steps. Doesn't Write the CIM.
  Liam, in for Bear."). It already satisfies both the Teardown carry-out
  cadence and the IN-FOR-BEAR LAW; rewriting for its own sake would drift
  from the title-echo pattern reference nbb reels use. `OutroSeries` props
  untouched.

## Metadata changes

- `_variant_todo` removed (all items addressed).
- `audience`, `register`, `palette`, `engine`, `voice_kokoro`, `typography`,
  `outro_source`, `derived_from` — untouched from scaffold.

## Judgment calls

- **No separate `B_LLM` beat inserted.** The source's `BHTF` beat is already a
  paste-into-Claude prompt in the exact position SKILL.md §Step 3 asks for
  (second-to-last). Following the pattern established by the two closest
  reference reels in this same tree (deal-sourcing, gl-recon), I relabeled
  BHTF's `act` to `"LLM EXERCISE"`, attached the `llm_exercise` object, and
  extended the narration to speak the dig-deeper follow-up. Inserting a new
  `B_LLM` beat would have produced two consecutive "paste this" beats and
  broken the reference pattern.
- **Outro pattern kept as `OutroSeries`** (from scaffold). Reference reels
  use `OutroCTA`; scaffold used `OutroSeries`. SKILL.md line 154 allows either
  ("Renders via Remotion `OutroSeries` / `OutroCTA`"), and rewriting the
  Remotion pattern is outside the register-conversion scope.
- **BCRY `quote` updated to match narration.** The `WantQuote` scene displays
  the quote as it's spoken; letting them drift would produce a caption/audio
  mismatch on render.
