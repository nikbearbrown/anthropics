# CONVERT-LOG — claude-tag-plugins--claude-liam-enterprise-search → nbb

2026-09-03 · Register conversion from Plain (hai-simple) to Teardown (NikBearBrown).

## Changed

- **All 8 body-beat narrations rewritten in the Teardown register.** Machinery
  first ("Here's what's actually happening…"), design intent named ("optimized
  for triage, not for answers"), trade-offs called out (the "not indexed vs no
  permission" ambiguity re-framed as a deliberate security choice: telling you
  'permission denied' also tells you the document exists). Facts unchanged —
  every number (~35-word snippet, 50-doc read cap), API rule (cursor-based
  pagination, index-first), and the contractor-onboarding anchor question all
  survive verbatim.
- **BCRY carry-out**: lightly retuned to match the Teardown cadence
  ("Here's the carry-out…"); on-screen `WantQuote.quote` updated to match the
  narration exactly (both spoken + shown).
- **BHTF converted from `your turn handoff` → `LLM EXERCISE`** (second-to-last):
  narration is now a paste-ready prompt for Claude/ChatGPT/Gemini plus a
  "Go deeper" follow-up. `llm_exercise: { prompt, dig_deeper }` block added.
  `ClaudeComposerAsk` command copy rewritten as a compact 3-part version of the
  prompt; `topic` → `ENTERPRISE SEARCH · YOUR TURN`; `segment` → `Search, Read,
  Report.`; `folderLabel` → `@NikBearBrown`.
- **BOUT outro**: line and handle updated to the NikBearBrown outro pattern —
  `"Search, Read, Report. Liam, in for Bear."` on `@NikBearBrown` (matches the
  precedent in `nbb-claude-basics--screenshot-prompt-caching`, e.g.
  `"Caching Pixels You've Already Seen. Liam, in for Bear." / @NikBearBrown`).
- **Metadata**: `folderLabel` and `channel_title` flipped from
  `@HumanitariansAI` to `@NikBearBrown`. `_variant_todo` removed. `audience`,
  `engine`, `voice_kokoro`, `palette`, `register`, `outro_source` left as the
  scaffold set them.

## Preserved exactly

- Every `beat_id` (B00, B01, B02, B03, B04, B05, B06, BCRY, BHTF, BOUT).
- Every non-BHTF `act` label — the "1 stakes / 4 ANCHOR PLANTED" / "4 ANCHOR
  PAYOFF" / "5 BOTH DIRECTIONS" / "6 CARRY-OUT" spine.
- All `shot`/`graphic` blocks including `production_viz.mechanic` copy,
  `manim` scene names, colors, and `remotion.pattern` names.
- `style_preset: humanitarians` and `ground: #F3EBDD` — kept per the model
  reel `nbb-claude-basics--screenshot-prompt-caching`, which also runs the
  humanitarians preset under the nbb audience. `palette: teardown` on the
  metadata is the switch that governs the render.
- `anchor_pair` string — still accurate (the contractor-onboarding question
  from B01 lands at B05 as snippet → full doc → 'used' feedback).

## Judgement calls

- **BCRY carry-out was already Teardown-shaped.** Left the sentence's spine
  and its `sparkLine` intact; added the "Here's the carry-out." framing and
  the "than this one" tail so it feels judged rather than declared.
- **BHTF `command` (the on-screen composer copy) is a compressed rewrite of
  the paste-ready prompt**, not the old "search internal docs / read /
  report" text. The narration reads the full prompt; the composer shows a
  scannable 3-point version so the frame stays legible. Same pattern as
  `nbb-claude-basics--screenshot-prompt-caching`.
- **`style_preset` / `ground` kept as `humanitarians` / `#F3EBDD`.** The
  scaffold did not switch them, and the model NBB reel didn't either — the
  `palette: teardown` metadata is what the compile step reads. Flipping the
  preset would be a shot-block edit, not a register conversion, and would
  risk desyncing from already-rendered media (`build.status: VIDEO/MANIM`
  on every beat).
