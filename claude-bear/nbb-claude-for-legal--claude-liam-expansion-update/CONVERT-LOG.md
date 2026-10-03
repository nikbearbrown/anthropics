# CONVERT-LOG — nbb-claude-for-legal--claude-liam-expansion-update

Register-conversion pass (source → NikBearBrown/Teardown). No render, no audio,
no compile. Deliverable is `beat_sheet.nbb.json`.

## What changed

- **Metadata**
  - `brand`: `hai-fellows` → `claude-liam` (matches sibling `nbb-...-ai-inventory`
    which is the closest working precedent; audience is `NikBearBrown` per the
    scaffold, brand carries the channel identity — `hai-fellows` describes the
    source lane, not the NBB cut).
  - `purpose` opening clause: `Plain register` → `Teardown register`.
  - Removed `_variant_todo` (checklist satisfied).
  - Everything else (title, slug, palette=teardown, engine=kokoro,
    voice_kokoro=am_onyx, folderLabel, in_for_bear, gate signs) kept as the
    scaffold set it.

- **Narrations rewritten in Teardown register** (voice only; every fact from the
  source survives unchanged — the skill is still expansion-update, still reads
  SKILL.md, still runs Steps linearly, still compares handbook vs new-state
  requirements and flags sections):
  - B00 cold open — kept the ~9s typing window (44 words + lead_silence 0.8);
    still lands on "flag, not rewrite"; adds the "Liam, take it from here"
    handoff (matching the sibling pattern for IN-FOR-BEAR on the cold open).
  - B01 anatomy — added "reader over compiler" trade-off; on-screen sparkLine
    updated to "The file you can read is the program that runs."
  - B02 pipeline — added "predictable route over a clever one" trade-off;
    sparkLine updated to "Same input, same route, same output shape."
  - B03 mechanism — reframed as "Here's what's actually happening… They
    optimized for repeatable flagging over judgment"; on-screen body + sparkLine
    updated to match.
  - BCRY carry-out — carries the same claim as the source (same-in / same-out /
    the deciding is still yours); WantQuote quote synced to the new narration;
    sparkLine tightened to "The skill flags. You decide."

- **BHTF → LLM EXERCISE (second-to-last)**
  - `act` renamed `your turn handoff` → `LLM EXERCISE`.
  - Added `llm_exercise` object with `prompt` + `dig_deeper`.
  - Rewrote the `command` from the CLI-shaped "Read the expansion-update skill
    …" prompt (only works if the skill is installed on the machine running the
    LLM) into a **frontier-LLM-pasteable** prompt: it teaches the checklist
    behavior inline, pins a concrete jurisdiction (Colorado), enumerates six
    real Colorado employer-rule categories that commonly force handbook edits
    (sick leave / HFWA, meal + rest periods, next-business-day final paycheck,
    non-compete under CRS §8-2-113, wage-transparency posting under the Equal
    Pay for Equal Work Act, workers'-comp posting), and forbids the LLM from
    rewriting language itself — mirroring the carry-out.
  - `runningText`: "paste this into Claude…" → "paste this into Claude, ChatGPT,
    or Gemini…" (matches sibling and SKILL.md §Step 3).
  - `topic` / `segment` retitled to fit the LLM-exercise card.

- **BOUT + BCTA collapsed → single BOUT with OutroCTA (last beat)**
  - Source had two outro beats (OutroSeries + OutroCTA); the NBB brief and
    SKILL.md §Step 4 both say the outro is *the* last beat. Merged the series
    line + the IN-FOR-BEAR signoff into one OutroCTA: "Claude, Expansion
    Update. Liam, in for Bear." Handle stays `@HumanitariansAI`. Matches the
    sibling's `BOUT`.

## Judgement calls

1. **No AUTHOR.MD exists at `anthropics/claude-bear/`.** The scaffold's
   `outro_source: "AUTHOR.MD :: NikBearBrown"` metadata is preserved as
   intent, but the outro copy is reconstructed from the existing OutroCTA
   pattern in the sibling NBB reels (`.../nbb-…-ai-inventory` uses "…Liam, in
   for Bear" with the reel title). The channel is `@HumanitariansAI`, not the
   default-channel `www.brutalist.art` — because every other NBB reel in this
   folder is `@HumanitariansAI`, and the source sheet is a HAI-fellows reel.
   No handle was fabricated.

2. **Colorado as the pinned jurisdiction.** SKILL.md requires the LLM prompt
   to produce a useful output on its own without the video, so the prompt
   needs a concrete state instead of `[state]`. Colorado is a defensible pick
   because all six enumerated rule areas are real, documented Colorado
   employer obligations that meaningfully diverge from a generic single-state
   handbook. Any other state with a comparable divergence profile would work;
   Colorado just gave the tightest, most-verifiable set.

3. **Kept `ground: "#F3EBDD"` and `style_preset: "humanitarians"`.** The
   scaffold left both HAI-cream values in metadata even though `palette` is
   now `teardown`. The sibling NBB reels do the same — the ClaudeComposerAsk
   and BrutalistHesitantWriter compositions still read the HAI cream, and
   changing the ground would fork the visual system. Palette-vs-ground
   mismatch is a known scaffold behavior, not a bug I should fix here.

4. **`brand: claude-liam` (not `nbb`).** The sibling working precedent uses
   `claude-liam` on NBB cuts of `claude-liam` source reels — the identity
   stays with the Liam-in-for-Bear voice, the audience/register flag rides on
   `audience: NikBearBrown` + `register: Teardown`. I followed that rather
   than inventing a `nbb` brand string.

## Verified

- JSON parses, 7 beats.
- `_variant_todo` removed.
- Beat order: B00 → B01 → B02 → B03 → BCRY → **BHTF (LLM EXERCISE, second-to-last)** → **BOUT (outro, last)**.
- Every `beat_id` preserved; no facts fabricated.
- `engine: kokoro`, `voice_kokoro: am_onyx` untouched. Liam, in for Bear.
