# CONVERT-LOG — nbb rewrite

Slug: `claude-for-legal--claude-liam-ai-tool-handoff`
Source: `../claude-for-legal--claude-liam-ai-tool-handoff/beat_sheet.json`
Output: `beat_sheet.nbb.json`

## What changed

- **Register**: every `beat.narration_text` rewritten in Teardown (Feynman × MKBHD).
  Facts, numbers, scenarios, IDs, act names, shot/graphic mechanics preserved.
- **B00**: cold-open narration kept in the 20-35 word window that
  `BrutalistHesitantWriter` needs to reach the ≥9s render floor. "Liam, take
  them through it" → "Liam, in for Bear" so Liam names himself in the register
  the outro repeats (IN-FOR-BEAR LAW).
- **BCRY**: rewrote both the narration AND the on-screen `WantQuote.quote` so
  the voice and the card stay in sync. Old quote read "The handoff isn't done
  when Claude finishes — it's done when a person signs off on what comes back";
  new quote reads "The handoff finishes with a signature — not a delivery."
  Sparkline unchanged.
- **B_LLM** (new, second-to-last): paste-ready prompt asking any frontier LLM
  to build the viewer a scope / boundary / record checklist for a task they're
  about to hand off — the same three parts B02 introduces. Dig-deeper follow-up
  asks which failure mode has NO catch in their current workflow.
- **BOUT**: replaced the HAI signoff with the NikBearBrown outro. Line reads
  the title + "A Nik Bear Brown teardown — more at brutalist.art." Handle
  swapped from `@HumanitariansAI` to `@NikBearBrown`.

## Judgement calls

- **Palette colors in graphic beats**: the scaffold set `palette: teardown` in
  metadata but the per-beat `graphic.production_viz.colors` arrays and the B00
  `BrutalistHesitantWriter` props still carried the humanitarians palette
  (`#F3EBDD` / `#2F2A26` / `#E4572E` / `#1F4E5F`). I updated those arrays and
  props to the teardown palette (`#FFFFFF` / `#2A1A0E` / `#C8102E` / `#545454`)
  so the manim scenes render consistent with the declared palette. The scene
  structure and mechanic text is untouched.
- **Brand-visible labels**: `metadata.folderLabel`, `metadata.channel_title`,
  `BHTF` `ClaudeComposerAsk.folderLabel`, and `BOUT` `OutroCTA.handle` all
  moved from `@HumanitariansAI` → `@NikBearBrown`. `style_preset` moved from
  `humanitarians` → `teardown`. `ground` moved from `#F3EBDD` → `#FFFFFF`.
  `brand` moved from `claude-liam` → `nbb`. B00 seed prefix moved from
  `hai-` → `nbb-` so the render is a distinct file, not a re-use of the HAI cut.
- **BHTF kept as body beat**: the source reel already has a "your turn"
  ClaudeComposerAsk. The nbb SKILL asks for a separate LLM-exercise beat before
  the outro, so I preserved BHTF (voice rewrite only) and inserted B_LLM after
  it. Two closely related closing beats, but each does a different job: BHTF
  is the small, do-it-in-your-workflow paste; B_LLM is the derived-from-topic
  paste-ready prompt the nbb spec wants.
- **AUTHOR.MD**: no per-book AUTHOR.MD exists under `claude-bear/`; used the
  standard NikBearBrown outro (default channel `www.brutalist.art`, handle
  `@NikBearBrown`) per `brands/nbb.md`.

## Preserved exactly

Every `beat_id`, every `act` label, every `shot.type`, every remotion pattern
name (`BrutalistHesitantWriter`, `WantQuote`, `ClaudeComposerAsk`, `OutroCTA`),
every `graphic.manim` scene name (`AITHB01Scene`, `AITHB02Scene`,
`AITHB03Scene`), the anchor-pair (B02 → B03), and the entire body of
`graphic.production_viz.mechanic` text. `_variant_todo` removed.

## Not done

No audio generation, no compile, no render. That is the next pass.
