# CONVERT-LOG — nbb-claude-basics--browser-coordinate-scaling

Converted `beat_sheet.json` → `beat_sheet.nbb.json` in the Teardown register.
Voice: Liam (Kokoro `am_onyx`), in for Bear. Palette: teardown.

## What changed

- **B00 (cold open)** — rewritten. Names the mechanism plainly ("Claude's vision
  encoder resizes every screenshot to a fixed canvas") instead of the softer
  "they're scaled from a resized copy". Ends on the same real question.
- **B01 (stakes)** — rewritten. Explicitly surfaces the design choice ("one input
  pipeline, not one per screen resolution — that's the design choice") and names
  its cost, per Teardown MKBHD lens.
- **B02 (anchor planted)** — rewritten. Adds the arithmetic that makes the miss
  intuitive ("728 out of 2560 is a quarter across, not the middle"). Anchor
  numbers unchanged: 1456×819, (728, 409), 2560×1440.
- **B03 (mechanism)** — rewritten. Explains *why* the multiply undoes the resize
  ("you're just undoing the shrink, one axis at a time") and names why the clamp
  exists ("Claude occasionally reports one pixel outside its own canvas"). File
  name and 20-line count preserved.
- **B04 (anchor payoff)** — rewritten. Explains why the single 1.76 ratio works
  ("width ratio and height ratio have to match" — because 16:9). Preserves the
  non-16:9 caveat and reframes it as the lookup-table branch, not a failure mode.
- **BCRY (carry-out)** — narration + `WantQuote.quote` both updated to say
  "inverse ratio" instead of just "ratio" (precision — Teardown values the
  direction of the multiply). On-screen sparkLine kept ("Resized space vs. real
  pixels.").
- **BHTF** — repurposed as the LLM EXERCISE beat (see judgement call below).
  Narration is a paste-ready prompt for any frontier LLM (Claude / ChatGPT /
  Gemini) + a real "Go deeper:" follow-up about the non-16:9 lookup table.
  Added an `llm_exercise` object per SKILL.md §Step 3 schema. Updated the
  `ClaudeComposerAsk.command` prop so the on-screen ask matches the spoken
  prompt (viewport target changed from 700,410 phrasing to a cleaner
  "Claude reports a click on…" form).
- **BOUT** — unchanged. Title + "Liam, in for Bear." with `@HumanitariansAI`
  handle already reads as a NikBearBrown outro line in this reel's channel
  context; no book AUTHOR.MD exists in `anthropics/claude-bear/` to draw a
  different line from.
- **`_variant_todo`** — removed (checklist satisfied).

## Judgement calls

1. **LLM exercise beat: enrich BHTF vs insert a new B_LLM.** SKILL.md §Step 3
   shows a schema example with `beat_id: B_LLM`. The reference nbb reel in this
   book (`nbb-claude-basics--screenshot-prompt-caching`, same slug family, same
   hai-simple skeleton) keeps 8 beats and enriches BHTF into the LLM exercise
   role rather than adding a 9th beat. BHTF is already a `ClaudeComposerAsk`
   with a paste-ready `command` prop — inserting a new beat would duplicate the
   same visual/role. I followed the shipped precedent: repurposed BHTF, kept
   the count at 8, added the `llm_exercise` object for schema compliance, and
   renamed the `act` to `LLM EXERCISE - your turn handoff` so the role is
   explicit downstream.

2. **BCRY quote text changed to match narration.** The `WantQuote.quote` prop
   is on-screen card copy, which the SKILL.md preserve-rule allows changing
   only when it "still fits the register". Adding "inverse" makes the direction
   of the multiply unambiguous — a Teardown-appropriate tightening, matching
   the reference reel's pattern of syncing quote to narration.

3. **BOUT left as-is.** No `AUTHOR.MD` exists under `anthropics/claude-bear/`
   or `anthropics/` proximate to this reel. The existing OutroCTA line and
   `@HumanitariansAI` handle already read as the NikBearBrown outro in the
   Liam-in-for-Bear frame. Reference reel does the same.

## Facts preserved (spot check)

- 1456 × 819 (Claude's canvas size for 16:9 input) — unchanged.
- (728, 409) → (1280, 720) on 2560 × 1440 — unchanged.
- 2560/1456 ≈ 1.76 and 1440/819 ≈ 1.76 — unchanged.
- `coordinate_scaling.py` in "twenty lines" — unchanged.
- Non-16:9 needs a lookup table, not the one multiply — unchanged.

## Not done (per task scope)

- No render, no audio generation, no compile. Estimated durations left as-is;
  actual durations will be re-measured on the next audio pass.
