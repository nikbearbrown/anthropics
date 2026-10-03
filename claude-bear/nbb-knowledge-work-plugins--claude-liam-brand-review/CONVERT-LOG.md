# CONVERT-LOG.md — nbb cut of `knowledge-work-plugins--claude-liam-brand-review`

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown register, Liam in for Bear, NBB channel).

## What changed

- **Every beat's `narration_text` rewritten** in the Teardown register (Feynman × MKBHD): take-it-apart, name-the-machinery, judge-the-design-choice. Facts, numbers, and structure preserved.
  - B00: cold open — Liam-in-for-Bear intro added ("Liam here, in for Bear."); rewritten to ~34 words to stay in the 20–35-word BrutalistHesitantWriter TIMING LAW window; still lands the corrected question ("review my content for brand voice") on-screen sync.
  - NB01: reframed as machinery ("A skill isn't a program — it's a folder Claude reads before it starts") + design-choice line ("optimized for readability over enforcement").
  - NB02: reframed trigger as semantic dispatch + named the trade-off ("optimized for natural phrasing at the expense of predictability").
  - NB03: kept the report-not-rewrite carry line, added the honest cost ("optimized for auditability at the expense of coverage") and the "works if / fails if" close.
  - BCRY: narration and on-screen `WantQuote` quote preserved verbatim — this beat IS the branded carry-out sentence ("Flagged, Not Fixed."); rewriting it would break the title/quote/narration lock.
- **BHTF converted into the LLM exercise beat (second-to-last).** BHTF was already the paste-ready `ClaudeComposerAsk` handoff, so I promoted it in place rather than inserting a redundant second Ask beat — that preserves the existing `beat_id` while satisfying the "LLM exercise second-to-last" requirement:
  - Added `llm_exercise` block (`prompt` + `dig_deeper`) per SKILL.md §Step 3.
  - Broadened `runningText` to "paste this into Claude, ChatGPT, or Gemini…" (any frontier LLM, not just Claude).
  - Narration folds in the dig-deeper: "Go deeper: ask it what your style guide would have to say for the flags to change."
  - `act` renamed from "your turn handoff" → "LLM EXERCISE" to match the schema in SKILL.md.
- **BOUT reworked as the NikBearBrown outro (last).** Narration signs off with `brutalist.art`; `eyebrow` prop swapped from `@HumanitariansAI` → `@NikBearBrown` to match the NBB channel.
- **Metadata:** `folderLabel` and `channel_title` switched to `@NikBearBrown`; `purpose` rewritten as a Teardown-flavored purpose; `_variant_todo` removed.

## Judgement calls

- **BHTF promoted in place instead of inserting a new B_LLM beat.** SKILL.md §Step 3 shows an example beat with `beat_id: B_LLM`, but the instructions require preserving every existing `beat_id`. BHTF already served the paste-ready-LLM-handoff role, and inserting a second Ask-your-turn beat before it would be redundant / off-rhythm. Promoting BHTF (add `llm_exercise` block, fold dig-deeper into narration, rename `act`) satisfies both constraints.
- **`shot`/`graphic`/`build` blocks preserved verbatim, including humanitarians-palette hexes and rendered media paths.** Per instructions ("preserve `shot` blocks"). `metadata.palette` is set to `teardown`; if the supervisor's downstream render pass reskins from metadata, it'll do so; if not, that's a separate pass, not a beat-sheet concern. Rendered `media/*.mp4` and `manim/*.mp4` paths preserved so this file can be re-audio'd and re-compiled without triggering an unnecessary re-render.
- **BCRY quote left unchanged.** The `WantQuote` prop, the narration, and the reel's `metadata.title` are all locked to "Flagged, Not Fixed." Changing the carry-out sentence would change the deliverable. It reads fine in Teardown context (it's a design-judgement observation already).
- **B00 note preserved verbatim.** It's engineering guidance about the BrutalistHesitantWriter TIMING LAW and stays valid — my rewrite is 34 words, inside the 20–35 window it demands.

## Not changed / not done here

- No render, no audio generation, no compile. Deliverable is the beat sheet.
- `NikBearBrown` outro content pulled from the anthropics-repo `AUTHOR.MD` at `books/anthropics/youtube/ai-1/AUTHOR.MD` (there is no `AUTHOR.MD` in `books/anthropics/claude-bear/`); default channel `brutalist.art` per `brands/nbb.md`.
