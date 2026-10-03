# CONVERT-LOG — nbb-claude-for-legal--claude-liam-escalation-flagger

## What changed

- **All seven narrations rewritten in Teardown register.** Facts, numbers,
  beat_ids, act structure, shot blocks and Manim scene names preserved. Every
  beat now takes the thing apart, names the design choice, and judges the
  trade-off — no "innovative", no boosterism.
- **BCRY quote prop synced** to the rewritten carry-out narration so the
  spoken line and the on-screen sentence remain identical.
- **BHTF converted into the proper NBB LLM exercise beat** (SKILL.md Step 3):
  added `llm_exercise.prompt` (paste-ready for Claude/ChatGPT/Gemini, produces
  a useful SKILL.md draft + two test inputs on its own) and
  `llm_exercise.dig_deeper`. `act` renamed to `LLM EXERCISE`, `segment` in
  the composer card renamed to `LLM Exercise`, `runningText` updated to name
  all three frontier LLMs. `beat_id` preserved.
- **BOUT rewritten as the NikBearBrown outro** (SKILL.md Step 4). Kept the
  "Liam, in for Bear" signoff (IN-FOR-BEAR LAW). Added "More at brutalist
  dot art" per `brands/nbb.md` default channel (`www.brutalist.art`).
- **Palette hex values swapped** in every visual (B00 props, B01/B02/B03
  graphic.production_viz.colors, BHTF folderLabel) from the source
  humanitarians palette (ink `#2F2A26`, terracotta `#E4572E`, cream `#F3EBDD`,
  slate `#1F4E5F`) to the teardown palette (ink `#2A1A0E`, crimson `#C8102E`,
  white `#FFFFFF`, slate `#545454`) per `brands/nbb.md`.
- **`_variant_todo` removed** — all four items complete.
- **`metadata.brand` set to `nbb`**, `style_preset` to `teardown`, `ground`
  to `#FFFFFF` (flat white — the teardown palette is never cream), `playlist`
  changed to `Claude, Taken Apart`, `folderLabel` and `channel_title` set to
  `@NikBearBrown`.

## Judgement calls

- **BHTF used as the LLM exercise beat, not a new B_LLM inserted.** The source
  BHTF was already the "Your turn — paste this into Claude" beat sitting
  second-to-last; adding a separate B_LLM would have duplicated the function
  and pushed BHTF into a role it wasn't written for. Preserving `beat_id`
  (the SKILL calls it out explicitly) and honouring "second-to-last LLM
  exercise" both survive by upgrading BHTF in place with the required
  `llm_exercise` field and paste-ready prompt.
- **Brand-scoped card copy updated** (folderLabel `@HumanitariansAI` →
  `@NikBearBrown`, palette hexes, outro handle `@HumanitariansAI` →
  `brutalist.art`). The SKILL rule "preserve shot blocks" is preserved in
  structure; brand identifiers count as card copy that "no longer fits the
  register" and were updated. Source `beat_sheet.json` untouched.
- **Kept `note` on B00 verbatim** — its TIMING LAW guidance still applies;
  my 32-word rewrite is inside the 20–35 window and preserves the `thinks`→
  `matches` trigger/replacement pair the hesitant-writer scene needs.

## Not done here

- No audio generated, no compile, no render — per orders.
- Word counts checked against Kokoro's ~3 wps for the source
  `estimated_duration_s` values; no changes to those.
