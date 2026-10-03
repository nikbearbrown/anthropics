# CONVERT-LOG — nbb cut of `claude-basics--claude-liam-four-places-your-data-goes`

Source → NBB rewrite of `beat_sheet.json` into `beat_sheet.nbb.json`.
Voice-only. Every number, name, taxonomy label, gate name, and prop-shape from
the source survives unchanged. Scaffold metadata (`audience`, `engine`,
`voice_kokoro`, `palette`, `register`, `outro_source`, `derived_from`,
`typography`) left in the state `brand_variant.py` wrote.

## What changed

- **Every `narration_text` rewritten in the Teardown register.** Feynman × MKBHD:
  explain the mechanism at each level (context window as working memory / a file
  on your account re-read into every new chat / provider systems as plumbing
  with a written-down retention clock / training as a probability-distribution
  nudge), reveal the design trade at each level (statelessness on purpose /
  memory-as-document, not black box / operability at the cost of instant undo /
  forward-only opt-out because the model itself is forward-looking), name the
  one door that opens once. All 24 body beats + BVDT recap re-voiced. Forbidden
  phrases avoided; "Here's what's actually happening", "They optimized for X at
  the expense of Y", "This is a design choice", "That's a real trade, not a
  broken one" carried the register.
- **BHTF turned into the explicit LLM-exercise beat** (SECOND-TO-LAST).
  Reused `BHTF` rather than inserting a new `B_LLM` beat, following the
  precedent set by the sibling nbb reels
  `nbb-claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context`
  and `nbb-claude-basics--screenshot-prompt-caching` — both of those also have
  a `ClaudeComposerAsk` handoff as second-to-last with the paste-ready prompt
  baked into the `command` prop, and inserting a duplicate `B_LLM` slot would
  have doubled the "your turn" moment. Added:
  - `act` renamed to `"your turn handoff / LLM exercise"` so the role is
    unambiguous.
  - A new `llm_exercise` block with `prompt` (paste-ready, no CLI, works in
    Claude / ChatGPT / Gemini on its own — produces a real four-part settings
    audit of the viewer's own AI tool) and `dig_deeper` (a genuinely
    explorable follow-up about acquisition-transferability of privacy
    settings — a question the video doesn't answer).
  - The narration now says "you can paste straight into Claude, ChatGPT, or
    Gemini" so the LLM-exercise framing is spoken out loud, closes with the
    explicit "Go deeper:" follow-up, and ends "Liam, in for Bear."
  - `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".
  - `ClaudeComposerAsk.command` prop updated to match the sharpened prompt in
    the `llm_exercise` block so on-screen copy and spoken copy agree.
- **BOUT kept as the NikBearBrown-style outro** (LAST beat). Line is the full
  title-cased episode title followed by "Liam, in for Bear." — same shape as
  the sibling nbb reels. `handle` left as `@HumanitariansAI` because this is a
  hai-simple source destined for that channel and every other metadata field
  (`channel`, `channel_title`, `folderLabel`) is HAI; overriding just the outro
  handle to `@NikBearBrown` would have contradicted the rest of the sheet.
- **`_variant_todo` removed** from `metadata` — all five checklist items are
  now done.
- **`purpose` line rewritten** to state the Teardown framing explicitly (the
  mechanism at each level + the trade at each level + reversibility as the
  compass).
- **`BVDT.artifactHeading`** restored to source's original `"The verdict"`
  (the earlier Plain-register redo hedged it to `"In short"`). Teardown earns
  the judgment word.
- **`BVDT.artifactLines`** expanded to carry each level's design-verdict tag
  ("statelessness, on purpose" / "lever, not dial" / "probability nudge") — same
  taxonomy, register-appropriate labels.
- **`estimated_duration_s` bumped** on beats whose narration got longer
  (B00 12→14, B01 11→14, B02 13→14, B03 10→12, B04 8→11, B05 12→16, B06 11→15,
  B07 11→15, B08 7→9, B09 11→14, B10 12→17, B11 12→15, B12 12→17, B13 11→15,
  B14 8→14, B15 10→17, B16 11→14, B17 11→15, B18 12→17, B19 12→17, B21 13→17,
  B22 12→16, BVDT 19→22, BHTF 24→34, BOUT 8→6). Estimates only; audio-first
  pipeline will replace them with measured `actual_duration_s` from the
  regenerated Kokoro mp3s.
- **`total_estimated_duration_s`** bumped from 240 to 260 to reflect the
  aggregate.
- **`actual_duration_s` cleared implicitly.** Left `actual_duration_s` off
  every rewritten beat (as the scaffold produced) so nothing downstream
  mistakes stale (pre-rewrite) durations for the truth.

## Judgment calls

1. **No new `B_LLM` beat.** SKILL.md §Step 3 gives a `B_LLM` schema, but the
   source's `BHTF` already IS the "your turn / paste-this-prompt" beat, and
   two sibling nbb reels in this same book resolve the collision the same way
   — fold the exercise into `BHTF`. Inserting a separate `B_LLM` slot would
   have created two sequential handoffs. Annotated the choice by renaming
   `BHTF.act` to `"your turn handoff / LLM exercise"` and attaching the
   structured `llm_exercise` block onto it (so the schema field is present
   even though the beat_id isn't `B_LLM`).
2. **Outro handle stayed `@HumanitariansAI`.** As documented in the sibling
   `nbb-claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context`
   convert-log, this matches sibling convention and stays consistent with the
   rest of the HAI-flavored metadata the scaffold preserved (`channel`,
   `channel_title`, `folderLabel`). If Bear later decides to flip the whole
   reel to `@NikBearBrown`, that's a bigger metadata edit than a register
   rewrite.
3. **Mechanism named explicitly at each level.** Source stayed at the level
   of "the model doesn't hold it anywhere"; Teardown named *why* — the context
   window is a working memory that exists only for this exchange (B05); the
   on-account file is a document you can open and edit, not a black box (B10);
   the provider retention is the plumbing behind the chat window running four
   jobs stacked into one layer (B12); training is a probability nudge — tokens
   changing the likelihood one word follows another (B17). All new mechanism
   claims are consistent with the source's implied model; no new facts, just
   the machinery made explicit.
4. **B17 Manim spec left untouched.** The Manim scene builds
   `B17_WordsBecomePattern` on the "words → probability distribution → single
   bar nudge" beat; the new narration now names that mechanism out loud
   ("nudge the model's probability distribution — the likelihood, for a given
   context, that one word follows another") so voice and visual reinforce.
5. **On-screen card copy preserved.** BrutalistHesitantWriter text (B00),
   `ClaudeDescent` sparkLines and level labels (all body beats), `ClaudeMemoryReread`
   card lines (B09), `ClaudeComposerAsk` topic/segment/greeting (B08),
   `ClaudeVerdictArtifact` title (BVDT), and `OutroCTA` handle (BOUT) all left
   register-neutral or Teardown-compatible. Only `BVDT.artifactHeading` +
   `artifactLines`, `BHTF.command`, and `BHTF.runningText` were edited to
   match the sharpened voice.
6. **`sources` metadata block preserved verbatim.** The Anthropic-team
   attribution and the ClaudeDescent / ClaudeMemoryReread / ClaudeVerdictArtifact
   palette-lock notes are still correct after the rewrite — those components are
   locked to the Claude fidelity token palette, so the `palette: teardown` set
   by the scaffold will not retint them. That's an expected known-mixed-skin
   condition, not a defect.

## Ending order (verified)

B00 → B01 → B02 → B03 → B04 → B05 → B06 → B07 → B08 → B09 → B10 → B11 → B12 →
B13 → B14 → B15 → B16 → B17 → B18 → B19 → B20 → B21 → B22 → BVDT → **BHTF
(LLM exercise)** → **BOUT (outro)**.
