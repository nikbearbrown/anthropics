# CONVERT-LOG — books--claude-liam-productivity (NBB cut)

Converted `beat_sheet.json` (Plain / hai-simple, Liam for @HumanitariansAI) into
`beat_sheet.nbb.json` (Teardown / NikBearBrown, Liam for @NikBearBrown).
Narration rewritten, LLM exercise inserted second-to-last, NikBearBrown outro
placed last. No render, no compile, no audio.

## What changed

- **All 21 body/act narrations rewritten** in Teardown register (Feynman × MKBHD):
  mechanism-first ("Here's what's actually happening…", "Here's the mechanism…"),
  design-choice framing ("The trade-off is real…", "The optimization is…", "The
  design choice: bend to the user's system…"). Facts, numbers, and named
  workflows (five moves, three streams, urgency-versus-importance, global
  instructions) preserved verbatim. No fabrication.
- **BCRY (carry-out)** re-voiced into a Teardown verdict; the on-screen
  `WantQuote` prop was updated to match the new spoken line so the reel stays
  coherent (screen and voice can't disagree on a quote beat).
- **B_LLM inserted as second-to-last beat** with schema per SKILL.md §Step 3:
  `narration_text` names the exercise and reads the "Go deeper" follow-up
  aloud; `llm_exercise.prompt` is a paste-ready, model-agnostic
  chief-of-staff prompt (works in Claude, ChatGPT, Gemini) that produces a
  useful morning-briefing / weekly-review routine on its own without the
  video; `llm_exercise.dig_deeper` asks a real next question about the
  privacy trade-off of full calendar access, not a summary. Visual reuses the
  existing `ClaudeComposerAsk` scene (per SKILL Ask/intro rule); the composer's
  `command` prop mirrors the paste-ready prompt so viewers can lift it off
  screen.
- **BOUT replaced with NikBearBrown outro** — `OutroCTA` with
  `handle: "@NikBearBrown"` and `subline: "www.brutalist.art"` (default channel
  per SKILL §Step 4, since claude-bear has no book-level AUTHOR.MD with a
  NikBearBrown section). Narration adds "More at brutalist dot art."
- **`_variant_todo` removed** from metadata.

## Judgment calls

1. **Kept BCRY and BHTF's original slots.** BHTF was already a "your turn" LLM
   handoff at the second-to-last position, so I converted it in place (renamed
   `BHTF → B_LLM`, promoted to the `LLM EXERCISE` act, added the required
   `llm_exercise` block) rather than inserting a new beat and shuffling
   anything. Result: order is `…NB19 → BCRY (verdict) → B_LLM (exercise) → BOUT
   (outro)` — matches SKILL §Step 5 (body → LLM exercise → outro) exactly.
2. **Changed `folderLabel`/`channel_title`/composer `folderLabel` from
   `@HumanitariansAI` to `@NikBearBrown`.** The scaffold left these alone, but
   the whole point of an NBB cut is that it *is* the NikBearBrown channel
   version. Leaving `@HumanitariansAI` on the outro card and the composer chip
   would visibly contradict the audience shift. Ground (`#F3EBDD`) and
   `style_preset: "humanitarians"` left untouched — those are visual scaffolding
   the compile pipeline uses; the palette metadata (`teardown`) is what actually
   selects the accent system.
3. **Updated the on-screen quote on BCRY.** Normally card copy is preserved, but
   `WantQuote` renders the exact narration as the on-screen quote — leaving the
   old Plain-register quote while Liam speaks a new one would break the beat.
   Both updated together.
4. **`estimated_duration_s` left approximate.** Kokoro will re-measure on the
   next audio pass; the compile pipeline treats measured duration as the master
   clock, so stale estimates don't leak into the cut.
