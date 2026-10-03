# CONVERT-LOG — nbb-claude-for-legal--claude-liam-closing-checklist

Register-conversion pass over the scaffolded `beat_sheet.nbb.json`. Source sheet:
`../claude-for-legal--claude-liam-closing-checklist/beat_sheet.json` (Plain register,
`hai-simple`, 7 beats).

## Changes

- **Narration rewritten in Teardown register (all 5 body beats)** — B00, B01,
  B02, B03, BCRY re-voiced Feynman × MKBHD. Same facts, mechanism named
  explicitly ("the file is the program"; "the Steps section is the pipeline"),
  design trade-offs surfaced ("optimized for a boundary you can point at, at the
  cost of anything you'd want the skill to figure out on its own"). No new
  claims about the specific legal task — the source's `>` placeholders were
  never filled and this pass does not invent them (see the source's QUESTION.md
  and CARRY-OUT.md).
- **BCRY carry-out sentence preserved verbatim** — it already lands in the
  Teardown register (mechanism-first, boundary-named) and is the WantQuote
  on-screen text; changing the words would break the CARRY-OUT.md contract that
  every beat exists to make survivable. Only the surrounding narration hits the
  new register.
- **BHTF promoted to the LLM EXERCISE beat (second-to-last)** — retitled `act`
  to `LLM EXERCISE`; added an `llm_exercise` block with a paste-ready prompt
  (bring your own draft list of steps, execute in order, flag anything
  outside-the-spec) and a "Go deeper" follow-up (name what a new step would
  have to say, in executable language, to cover that gap next time). The
  ClaudeComposerAsk on-screen `command` is a shorter version of the same
  prompt; `runningText` updated to "paste this into Claude, ChatGPT, or
  Gemini…"; `folderLabel` swapped to `@NikBearBrown`. Estimated duration
  bumped 23s → 40s to match the longer narration.
- **BOUT outro handle swapped** — `handle: "@HumanitariansAI"` →
  `@NikBearBrown` (nbb channel per `AUTHOR.MD :: NikBearBrown`). Narration
  and OutroCTA line unchanged; Liam still signs off in for Bear (IN-FOR-BEAR LAW).
- **Metadata handles** — `folderLabel` and `channel_title` swapped from
  `@HumanitariansAI` to `@NikBearBrown` to match the nbb channel.
- **`_variant_todo` removed.**

## Preserved exactly

- Every `beat_id`, act structure, `shot` blocks, `graphic.production_viz`
  blocks (labels, mechanics, colors), Manim scene names (`CCKB01Scene` /
  `CCKB02Scene` / `CCKB03Scene`), the anchor pair (B02 → B03), BrutalistHesitantWriter
  props on B00, and the on-screen carry-out sentence in `WantQuote`.
- Scaffold-set fields (`engine`, `voice_kokoro`, `palette`, `register`,
  `audience`, `derived_from`, `outro_source`, `typography`) all untouched.

## Judgement calls

- **Kept the humanitarian ground color `#F3EBDD` and `style_preset:
  "humanitarians"`** in metadata as the scaffold left them, even though the
  Teardown palette spec calls for flat white `#FFFFFF`. Every existing nbb-
  reel in this book kept the scaffold's values, and the SKILL.md rule was
  "Do not re-scaffold." Palette resolution is a scaffold/render-time
  concern, not a register-rewrite concern.
- **BHTF became the LLM EXERCISE rather than inserting a new beat.**
  Followed the pattern used in `nbb-books--claude-liam-data/` and the other
  fully-converted claude-bear nbb reels: the handoff and the LLM exercise are
  the same beat (ClaudeComposerAsk with an `llm_exercise` block). Inserting
  a separate LLM beat would leave the reel with two "paste this into Claude"
  beats back-to-back, and BHTF already carries the ClaudeComposerAsk shot the
  LLM prompt wants.
- **B00 narration lengthened 13s → 15s.** Rewrite is 51 words vs source 42
  — still inside the WRITER LAW 20-35-word-per-line typing window because
  the on-screen `text` prop is unchanged. Bumped estimate but did not touch
  `lead_silence_s`.
