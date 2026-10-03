# CONVERT-LOG — nbb cut

Converted `beat_sheet.json` → `beat_sheet.nbb.json` for
`claude-for-legal--claude-liam-international-expansion`.

## What changed

- **All 7 narrations rewritten in the Teardown register.** Machinery first
  (why does a court re-classify — because the law was designed so the label
  can't decide it); design choices named and judged (EOR = speed at the cost
  of a monthly per-head cut; carry-out framed "works if you value X, fails if
  you value Y"). No facts added, none dropped — every number, entity, and
  legal concept in the source (three checks, Berlin developer, EOR, notice
  periods, statutory benefits) survives unchanged.
- **BHTF transformed into the LLM-exercise beat.** `act` changed from
  "your turn handoff" → `LLM EXERCISE`. Added the `llm_exercise` object
  (paste-ready prompt for Claude / ChatGPT / Gemini + a real "Go deeper"
  follow-up about mid-employment country moves). Narration re-cast as
  paste-and-go instructions, ending with the Go-deeper line per SKILL §Step 3.
  Composer `command` shortened to the on-screen version; full prompt lives in
  `llm_exercise.prompt`. `segment` changed from "Your Turn" → "LLM Exercise".
- **BOUT rewritten as the NBB outro.** Narration + `OutroCTA.line` now sign
  off with "Take it apart, judge the choices — that's the work. Liam, in for
  Bear. More at brutalist.art." `handle` flipped @HumanitariansAI → @NikBearBrown.
  `estimated_duration_s` bumped 6 → 8 to fit the longer sign-off.
- **`_variant_todo` removed** from metadata.
- **Metadata `folderLabel` / `channel_title`** flipped @HumanitariansAI →
  @NikBearBrown so the NBB reel's branding is consistent with the outro
  handle and the composer folder chip.

## Judgment calls

- **Kept BHTF as the beat_id** (preserving IDs per SKILL) instead of renaming
  to the schema example `B_LLM`. The beat already sat in the second-to-last
  slot and already used `ClaudeComposerAsk`, so the transformation is voice +
  role, not structure.
- **Kept `ClaudeComposerAsk` shot instead of the schema-example `CARD` shot.**
  The Ask/intro scene rule (2026-07) makes the composer the NBB idiom for
  showing a prompt; the composer is the right visual for "paste this."
- **Left B00's `BrutalistHesitantWriter` colors and B01/B02/B03's Manim
  humanitarians palette in place.** Shot blocks preserved exactly per SKILL;
  teardown palette applies at the metadata level. If the runtime doesn't
  re-skin those props from `metadata.palette`, that's a separate build fix,
  not a narration-conversion problem.
- **Metadata `ground` (`#F3EBDD`) and `style_preset` (`humanitarians`) left
  as scaffolded.** Instructions said audience / register / palette / engine
  / voice_kokoro are the scaffold's job — didn't touch the rest.

## Ending order (verified)

```
B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)
```

Second-to-last = LLM EXERCISE with `llm_exercise` object present. Last = outro.
Valid JSON, `_variant_todo` gone.
