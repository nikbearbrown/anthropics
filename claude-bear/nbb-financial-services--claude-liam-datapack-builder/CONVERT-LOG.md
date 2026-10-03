# CONVERT-LOG — financial-services--claude-liam-datapack-builder → nbb

Converted the Plain-register hai-simple sheet into the NBB (Teardown) cut.
Facts unchanged; every number, source name (CIMs, offering memos, SEC filings,
MCP servers), and pipeline claim survives from source.

## What changed

- **`register`** metadata: `Plain` → `Teardown`.
- **`palette`** metadata: `humanitarians` → `teardown` (nbb spec).
- **`_variant_todo`** removed (checklist complete).
- **`purpose`** — re-worded from "Plain register" to "Teardown register"; content unchanged.
- **B00 (cold open)** — re-voiced. Kept ≤35 words for BrutalistHesitantWriter TIMING LAW. On-screen `text`, `triggerWords`, `replacementWords`, `seed` unchanged (the visual is the writer typing/correcting; that stays fixed).
- **NB01 (mechanism — a skill is a folder)** — re-voiced: named the design choice explicitly ("the file is the program", "no opaque model layer to decode"). Facts identical.
- **NB02 (mechanism — linear steps)** — re-voiced: named the trade-off ("predictability at the cost of clever routing"). Facts identical.
- **NB03 (mechanism — narrow scope)** — re-voiced: named the design philosophy ("They optimized for repeatability at the expense of scope"). Every source (CIMs, offering memos, SEC filings, web search, MCP servers) preserved verbatim.
- **BCRY (carry-out)** — tightened to "doesn't do the math" phrasing; matched `WantQuote.quote` prop to the new narration. Kept the sparkLine as-is ("Standardizes the data. Doesn't do the math.") — already Teardown-crisp.
- **BHTF (LLM exercise, second-to-last)** — re-voiced in Teardown; kept the paste-ready prompt EXACTLY as source (that string appears on-screen in `ClaudeComposerAsk.command` for the viewer to copy). Added a "Go deeper:" clause to the narration and an `llm_exercise` sidecar block (`prompt` + `dig_deeper`) per SKILL.md §Step 3. Bumped `estimated_duration_s` 26 → 30 to reflect the added Go-deeper clause; audio-first will re-measure on regen.
- **BOUT (outro)** — untouched. Source already ships NBB-shape ("Liam, in for Bear." sign-off, OutroSeries in teardown palette). Nothing to swap.

## Judgement calls

1. **BHTF as the LLM-exercise slot, not a new `B_LLM` beat.** SKILL.md Step 3 describes inserting a beat with `beat_id: B_LLM`, but every prior shipped nbb sibling in this book (deal-sourcing, gl-recon, model-update, deal-screening) satisfies the requirement by re-voicing the existing BHTF handoff and skipping a separate B_LLM. Followed shipped precedent — one paste-ready prompt second-to-last, no duplication. Added the `llm_exercise` sidecar block + "Go deeper:" clause so the beat still satisfies the invocation's explicit LLM-exercise contract without breaking the pattern.
2. **Outro kept as OutroSeries, not swapped to OutroCTA.** Some sibling nbb sheets use OutroCTA. The source here already renders in teardown palette with a Liam sign-off; SKILL.md permits either component. Leaving the source's OutroSeries choice intact avoids a gratuitous swap.
3. **`topic` metadata left as "DATAPACK-BUILDER · FINANCIAL SERVICES SKILL"** (not generalized to "CLAUDE · SKILLS" the way deal-sourcing did). This reel is specifically about one named skill; the topic string is on-screen text and stays specific.
