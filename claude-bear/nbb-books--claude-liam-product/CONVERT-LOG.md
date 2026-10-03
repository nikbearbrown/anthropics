# CONVERT-LOG — nbb conversion of `books--claude-liam-product`

Source : `anthropics/claude-bear/books--claude-liam-product/beat_sheet.json` (Plain register)
Output : `anthropics/claude-bear/nbb-books--claude-liam-product/beat_sheet.nbb.json` (Teardown register)
Date   : 2026-09-03
Voice  : Kokoro `am_onyx` — Liam, in for Bear (unchanged; IN-FOR-BEAR LAW).

## What changed

- **All 21 body narrations rewritten** in Teardown register (B00, NB01–NB19, BCRY).
  Feynman × MKBHD: explain the machinery, name the design choice, name the
  trade-off. No facts moved. Beat IDs, act labels, `shot` blocks, `graphic`
  blocks, and on-screen card copy preserved verbatim.
- **B00 cold open** gets the Liam self-ID up front ("Liam here, in for Bear.")
  per IN-FOR-BEAR LAW and per the reference nbb-marketing sheet's pattern. The
  BrutalistHesitantWriter on-screen text ("decides → narrows") is unchanged.
- **BCRY carry-out narration + WantQuote `quote` prop tightened together** so
  card and voice-over stay in sync: "The product plugin ranks — it doesn't
  decide. It turns scattered ideas and feedback into a shortlist of what to
  build next, and leaves the call at the desk to you." The `sparkLine`
  ("You keep the call.") is unchanged.
- **BHTF removed.** The old "your turn handoff" beat is replaced by the LLM
  exercise (see next). This is the pattern in the completed nbb-marketing sheet;
  the alternative pattern (rename BHTF → LLM EXERCISE, kept in
  nbb-building-plugins) also exists in the corpus. Choice: follow the SKILL.md
  schema exactly, which specifies a `B_LLM` beat_id — see JUDGMENT below.
- **B_LLM inserted second-to-last** — the SKILL.md §Step 3 beat: paste-ready
  prompt for Claude/ChatGPT/Gemini that runs the four-question product-manager
  pass on the viewer's own list (rank by impact-per-hour, flag distractions
  dressed up as good ideas, surface the one hard unanswered question), plus a
  `dig_deeper` follow-up that argues the flagged distraction from the other
  side. Prompt is derived directly from the video's subject (§NB04 "four
  questions", §NB11 "ten ideas / few hours", §NB18 "ranks, doesn't decide").
- **BOUT rewritten as the NikBearBrown outro.** `handle` flipped from
  `@HumanitariansAI` → `@NikBearBrown`; `line` now
  `"Claude, Shipping — the product plugin, taken apart. Liam, in for Bear.
  brutalist.art"`; narration matches. Build status flipped from `VIDEO` to
  `PENDING` since the outro must re-render.
- **B_LLM build status** = `PENDING` (new beat, no media yet).
- **`_variant_todo` scaffold checklist removed** from metadata.
- **`purpose` string** in metadata updated to the Teardown framing so it
  matches the register the sheet is now in (parallel to what the nbb-marketing
  sheet did).

## What was NOT changed

- Beat IDs, act labels, `shot` blocks, `graphic.production_viz` blocks, chip
  arrays, colors arrays, `manim` scene names.
- BrutalistHesitantWriter props on B00 (on-screen text, trigger/replacement,
  seed, timings).
- Metadata `style_preset`, `ground`, `folderLabel`, `channel_title`, `playlist`,
  `in_for_bear`, `clock`, `gate_c`, `gate_h`, `anchor_pair`, `one_flag`,
  `build.*`. These were all left as scaffold set them / source had them.
- Palette hex codes inside graphic blocks (`#F3EBDD` cream / `#2F2A26` ink /
  `#E4572E` terracotta). Consistent with every other completed nbb- sheet in the
  corpus: the teardown palette override happens at render time via metadata
  `palette: "teardown"`, not by rewriting per-beat color arrays.
- All `estimated_duration_s` values updated only to reflect the rewritten
  narration length (small adjustments); no re-measurement — audio has not been
  regenerated. Compile will replace with `actual_duration_s` when audio runs.

## Judgment calls

1. **BHTF → B_LLM as insertion, not rename.** Corpus has both patterns:
   nbb-marketing removes BHTF and inserts a new `B_LLM`; nbb-building-plugins
   keeps `BHTF` and just re-labels its `act`. The SKILL.md §Step 3 schema
   specifies `"beat_id": "B_LLM"` verbatim, so I went with insertion (matching
   nbb-marketing). This changes the beat count from 23 (with BHTF) to still 23
   (with B_LLM), so the `metadata.build.filled/of` counts stay valid.
2. **Outro channel flip to `@NikBearBrown`.** Corpus is split here too:
   nbb-building-plugins kept `@HumanitariansAI`; nbb-marketing flipped to
   `@NikBearBrown` with `brutalist.art` appended. SKILL.md §Step 4 says the
   default channel is `www.brutalist.art` and pulls from
   `AUTHOR.MD :: NikBearBrown` — this book has no `AUTHOR.MD`, so I followed
   the more spec-aligned nbb-marketing pattern.
3. **BCRY tightened.** The source carry-out sentence works in Plain register
   ("but ranking isn't deciding, and the call at the desk stays yours") but is
   comma-spliced and passive. Teardown wants the mechanism named first, so I
   flipped the front to "ranks — doesn't decide." The claim is unchanged.
