# CONVERT-LOG — financial-services--claude-liam-fsi-strip-profile → nbb

Source: `anthropics/claude-bear/financial-services--claude-liam-fsi-strip-profile/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Every number, name, file path, and claim in the source survives
  unchanged: the skill is `fsi-strip-profile`; a folder holding one
  `SKILL.md`; three ordered moves — ask scope first (one slide or several,
  what to focus on), then research (filings / market data / news), then
  build one slide at a time with a picture-check between each (render to
  image → inspect for overflow / cut-off labels / chart bleed → fix → show →
  stop). Voice-only edit throughout: explained the mechanism (skills live as
  text on disk, not in weights — "same file, same routine, every run"),
  named the design choices ("they optimized for you owning the scope, at
  the expense of the model just running ahead"; "the loop runs one increment
  at a time on purpose"), and drew the trade-off line into the carry-out
  ("'the picture came out fine' and 'the numbers are actually right' are two
  different claims, and the skill guarantees the first, not the second" —
  seeded in `metadata.purpose` and paid off in the LLM exercise dig-deeper).

- **BHTF upgraded to the LLM exercise beat** (already second-to-last, so no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added
  the structured `llm_exercise` object with `prompt` (paste-ready for Claude /
  ChatGPT / Gemini, generalized past finance so it works without the skill
  installed — any single-artifact task where the model can render its own
  output and self-inspect: one-slide investment profile, one-page product
  brief, one-page résumé) and `dig_deeper` follow-up (what visual inspection
  can't catch — the class of errors that render out clean and are still
  wrong; the seam between rendering-looks-good and being-actually-right).
  Narration expanded to include the "Go deeper: …" line. `beat_id`
  preserved per rule. Shot (`ClaudeComposerAsk`) preserved; `folderLabel`
  updated to `@NikBearBrown`, `runningText` broadened to
  `paste this into Claude, ChatGPT, or Gemini…`, and `command` rewritten to
  a shorter version of the paste-ready `llm_exercise.prompt` that fits the
  composer UI. `estimated_duration_s` bumped 24 → 48 for the fuller prompt +
  dig-deeper appendage.

- **BOUT (outro) retargeted to the NikBearBrown channel.** Pattern swapped
  `OutroSeries` → `OutroCTA` (matches the sibling `nbb-…-deal-sourcing`
  precedent). Props reshaped: `line` now carries the full
  "Checks the Picture, Then Stops. Liam, in for Bear." string, and
  `handle: "@NikBearBrown"` added. Narration kept verbatim — already
  IN-FOR-BEAR-LAW compliant.

- **BCRY (carry-out) narration preserved verbatim.** The on-screen
  `WantQuote` props render this exact sentence, and it already reads clean
  in the Teardown register (names the mechanism — "checks its own picture
  before it ever shows you one — then it stops" — and the design outcome
  — "something you actually approved, not just something the model
  produced"). Rewriting the narration would have desynced it from the
  rendered quote for zero register gain.

- **Metadata `_variant_todo` removed** (checklist complete).
  `channel_title` and `folderLabel` at the sheet level flipped
  `@HumanitariansAI` → `@NikBearBrown` for consistency with the outro
  handle. `playlist: Claude Basics` kept — series identity travels with the
  topic ("does the skill actually check?"), not the audience cut.

- **`purpose` line rewritten** to the Teardown lens (register now reads
  "take apart Anthropic's fsi-strip-profile skill" and names the design
  choice — you signing off each slide, at the expense of throughput; the
  render vs. correctness split — rather than the Plain-register framing of
  the source).

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a new beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The
   source already had `BHTF` at second-to-last position doing the
   LLM-handoff. The preserve-beat-ids rule wins: kept `BHTF` as the
   beat_id, adopted the `LLM EXERCISE` act name and the structured
   `llm_exercise` field. No new beat inserted; no reorder. Matches the
   sibling `nbb-…-deal-sourcing` precedent.

2. **Handle on BOUT.** Source used `@HumanitariansAI`. NBB brand spec
   (`brands/nbb.md`, SKILL Step 4) says the outro is the NikBearBrown
   section — default channel is the NikBearBrown identity. Went with
   `@NikBearBrown` on the outro handle and on the sheet-level
   `channel_title`/`folderLabel`. `AUTHOR.MD` for this book isn't in the
   book root (only found `books/anthropics/youtube/ai-1/AUTHOR.MD`); the
   sibling precedent's outro pattern gave enough — `OutroCTA` with
   `handle: "@NikBearBrown"` — without needing the full AUTHOR.MD.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per
   the shot-blocks preserve rule. `bg: #F3EBDD` and `accent: #E4572E` are
   humanitarians-palette colors, but this is a locked visual element (the
   hesitant-writer typing animation, correction 'trust' → 'check') and the
   note explicitly ties timing to those props. New narration is 32 words —
   sits inside the 20–35 window the note requires, and keeps the trust →
   check hesitation legible.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata left
   as scaffold wrote them.** Not re-scaffolding was an explicit
   instruction; `palette: teardown` is the field the downstream compile
   reads. The residual humanitarians hints only affect the frozen B00 shot
   props, which are supposed to stay.

5. **LLM exercise generalized past the NKE example.** The source's
   handoff prompt requires the fsi-strip-profile skill installed in
   Claude to work end-to-end, and won't run at all in ChatGPT or Gemini
   (no skill system, no filings-fetch tool). The paste-ready prompt was
   generalized so it borrows the *mechanic* — build → render → inspect
   your own picture → fix → stop — and applies it to any single-artifact
   task the model can render on its own (one-slide investment profile,
   one-page product brief, one-page résumé). The NKE case is offered as
   the first option, preserving the source's example without demanding
   it. The dig-deeper prompt makes the video's own carry-out actionable:
   ask what visual self-inspection can't catch — the seam is what
   remains yours.

## Not done (out of scope)

- No audio generated. No compile. No render. No `art` invocation.
  Deliverable is `beat_sheet.nbb.json` alone, per the invocation contract.
