# CONVERT-LOG — nbb-claude-for-legal--claude-liam-irac-practice

Converted 2026-09-03. Source `beat_sheet.json` unchanged.

## What changed

- Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
  Facts unchanged: A Skill is a folder; `irac-practice/SKILL.md` in plain English;
  Steps run top to bottom, Issue → Rule → Application before Conclusion, linear
  unless a step says otherwise; the Application is where the Rule meets the facts
  one at a time; a Conclusion without Application is a guess wearing the right
  answer.
- B00 cold open re-voiced into the "obvious guess is X — wrong branch, it's Y"
  frame the sibling `nbb-…-ip-clause-review` uses. On-screen writer text +
  trigger/replacement (`answer` → `steps`) preserved verbatim.
- NB01/NB02/NB03 mechanism beats deepened: named the design choice
  (plain-text so it's auditable), the trade-off (linearity buys the whole point
  of IRAC), and the philosophy (optimizing for the reasoning habit that survives
  after the video). All chip labels, captions, and Manim scene IDs preserved.
- BCRY carry-out kept verbatim — it was already in the "isn't X — it's Y" form
  the register demands. `WantQuote` sparkLine unchanged.
- BHTF: was `your turn handoff` referencing the Skill; converted to `LLM EXERCISE`
  with a `llm_exercise.{prompt, dig_deeper}` block that runs in any frontier LLM
  without the Skill installed. The prompt asks the model to drill the viewer
  through I → R → A → C and refuse jumps. `dig_deeper` asks for three hypos
  where one fact flips the Rule. `ClaudeComposerAsk` props kept; `command` shortened
  to the paste-form.
- BOUT: pattern switched from `OutroSeries` → `OutroCTA` and the `handle` prop
  added (`@HumanitariansAI`), matching the sibling nbb-ip-clause-review outro.
  Line reworked to include a pithy tag: "Application, not Conclusion."
- Metadata `_variant_todo` removed. `purpose` retagged Plain → Teardown.

## Judgement calls

- **Channel on outro.** `brands/nbb.md` names `www.brutalist.art` /
  `@NikBearBrown` as the NBB default, but the scaffold set
  `folderLabel`/`channel_title` to `@HumanitariansAI` and the sibling
  `nbb-…-ip-clause-review` conversion kept `@HumanitariansAI` on the outro handle.
  Followed the sibling — this reel is part of the same batch and consistency
  wins over the brand default. One line to flip if Bear disagrees.
- **B00 background stays `#F3EBDD` (cream), not teardown white.** The scaffold
  and the sibling nbb-ip-clause-review both left B00's `bg` prop at the source
  cream so the hesitant-writer visual stays cohesive with the compiled reel.
  Palette metadata still declares `teardown` — the compiler owns the reconciliation.
- **Duration estimates re-set from narration length**, following the ip-clause-review
  precedent (audio gets regenerated on build, so these are just planning hints).
- **BCRY narration unchanged.** Rewriting a sentence already in perfect Teardown
  form would only weaken it. `estimated_duration_s` kept at 9.

## Not done (per supervisor spec)

No audio generated, no compile, no render. Deliverable is
`beat_sheet.nbb.json` only.
