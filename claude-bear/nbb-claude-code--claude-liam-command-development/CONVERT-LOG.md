# CONVERT-LOG — nbb-claude-code--claude-liam-command-development

Source: `anthropics/claude-bear/claude-code--claude-liam-command-development/beat_sheet.json`
Target: `beat_sheet.nbb.json` in this directory.

## What changed

- **Register:** rewrote every beat's `narration_text` in the Teardown register
  (Feynman × MKBHD) per `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`.
  Voice-only edits — every fact, file path (`.claude/commands/…`), field name
  (allowed-tools, argument-hint, disable-invoke, model, description), argument
  syntax ($1, @file, !`bash`), and the three homes (project / personal / plugin)
  survive unchanged from source.
- **B00 (cold open):** framed as "let me pull one apart" — machinery preview,
  not marketing preview. Kept BrutalistHesitantWriter props exact so the
  user→Claude correction still lands.
- **B01 / B02 / B03:** each opens with a Teardown lead — "here's the
  machinery," "here's the anchor," "now judge what the docs give you." Named
  the design trade-off explicitly at the end of B01 and B03 ("they optimized
  for X at the cost of Y"). Production_viz colors + chip lists preserved
  verbatim.
- **BCRY (carry-out):** original narration was already a Teardown-register
  take-out sentence; added a leading "the take-out" cue and a closing
  imperative. Kept the on-screen `quote` and `sparkLine` exactly (still fits
  the register).
- **BHTF (was "your turn handoff", now "LLM EXERCISE"):** promoted this beat
  into the required Step-3 slot. Rewrote command from a Claude Code CLI paste
  to a paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini),
  asking the model to produce the whole `.claude/commands/review-pr.md` file
  with correctly-scoped `allowed-tools`, an `argument-hint`, and a body of
  instructions (not descriptions). Added the `llm_exercise` object with
  `prompt` + `dig_deeper`. `dig_deeper` is a genuine next question — diff the
  correct command against a deliberately wrong one and locate the silent-fail
  point — not a summary.
- **BOUT (outro):** kept the title + "Liam, in for Bear." line intact
  (Teardown-compatible). Swapped `handle` from `@HumanitariansAI` to
  `@NikBearBrown` to match the destination channel.
- **Channel metadata:** `folderLabel` and `channel_title` swapped to
  `@NikBearBrown` in top-level metadata + BHTF ClaudeComposerAsk props. Matches
  reference nbb siblings (e.g. `nbb-claude-basics--screenshot-prompt-caching`).
- **`_variant_todo`:** removed.
- **`estimated_duration_s` on BHTF:** raised from 35 → 40 because the LLM
  prompt is denser (still audio-first — regeneration will re-measure).

## Judgement calls

- **BHTF repurpose vs new B_LLM beat.** The task prompt says "insert the LLM
  exercise beat, SECOND-TO-LAST." Every existing nbb sibling on disk (checked
  ~20) achieves this by repurposing BHTF rather than inserting a new beat —
  BHTF already sits second-to-last, already renders through ClaudeComposerAsk,
  and already has a paste-ready structure. Inserting a fresh `B_LLM` while
  keeping BHTF would either duplicate the "your turn" beat or orphan the
  existing `media/BHTF.mp4`. Went with the sibling pattern.
- **On-screen shot blocks unchanged.** Every `shot`, `graphic`, and
  `production_viz` block preserved verbatim (colors, chips, arrows, strike,
  captions). Register lives in narration + on the ClaudeComposerAsk `command`
  prop; the Manim scenes carry from the source render.
- **Carry-out visual quote left as source-defined.** The `WantQuote.quote` on
  BCRY is already Teardown-compatible (explains machinery, draws the
  distinction). Preserved per SKILL.md "on-screen card copy that still fits
  the register."
- **No `chapter_number` added** — source doesn't set one.
