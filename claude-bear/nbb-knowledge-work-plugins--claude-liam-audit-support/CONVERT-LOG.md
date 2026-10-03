# CONVERT-LOG.md — nbb conversion

**Source:** `../knowledge-work-plugins--claude-liam-audit-support/beat_sheet.json` (Plain register, hai-simple, HumanitariansAI palette)
**Target:** `beat_sheet.nbb.json` (Teardown register, NikBearBrown channel, teardown palette)
**Template:** `../nbb-knowledge-work-plugins--claude-liam-accessibility-review/` (same book, same skill=hai-simple, same 7-beat shape)

## What changed

### Metadata
- `topic` → `CLAUDE SKILLS · ANTHROPIC` (was `AUDIT-SUPPORT · SOX 404 COMPLIANCE SKILL`) — matches every other NBB skill teardown in this book.
- `purpose` → rewritten to name the design choice and the trade-off ("optimized for defensibility and repeatability at the expense of the overall opinion, which stays with the auditor").
- `style_preset` → `teardown` (was `humanitarians`).
- `ground` → `#FFFFFF` (was `#F3EBDD`).
- `folderLabel` + `channel_title` → `@NikBearBrown` (were `@HumanitariansAI`).
- `playlist` → left as `Extending Claude — Skills, Plugins & Connectors` — every knowledge-work-plugins nbb sibling uses this playlist.
- `_variant_todo` → removed (per SKILL.md Step 5).
- Scaffold-set fields (`audience`, `register`, `palette`, `engine`, `voice_kokoro`, `typography`, `outro_source`, `derived_from`) left as `brand_variant.py` wrote them.

### Beats

All seven `beat_id` values preserved; act structure preserved; `graphic` block on-screen copy (labels/chips/captions on NB01, NB02, NB03) preserved verbatim — those chips still fit the Teardown register.

- **B00 (cold open):** Rewrote narration in Teardown register with the "Liam here, in for Bear" opener that matches every hai-simple NBB sibling. Updated the on-screen writer copy from `Does Claude / pass a / company's SOX / 404 audit?` (trigger `pass → support`) to `Does Claude / decide if my / SOX 404 controls / pass?` (trigger `decide → test`). "Support" is a fuzzy Plain-register word; "test" names the actual mechanism the video is about ("It Tests and Classifies"). Palette props swapped to teardown (`#FFFFFF` / `#2A1A0E` / `#C8102E`); `seed` renamed `nbb-audit-support`; note updated to reference the accessibility-review sibling as the timing donor (same 42ms/char / 4% mistake / 8% hesitate config).
- **NB01 (anatomy):** Opens with "Take a Claude skill apart, and here's what's actually inside" (Teardown signature). Same facts as source; added the "no other files doing the real work" line to preempt the reader's implicit "surely there's more to it" assumption. `estimated_duration_s` bumped 18 → 20 to match the longer narration. `production_viz` colors swapped to teardown palette; chips/label/caption unchanged.
- **NB02 (pipeline):** Rewrote to explain the mechanism ("test each item against the control's stated criteria — the criteria written into the skill, not the model's opinion of what a good control looks like"). This is the beat where the video earns the right to call it a procedure and not a judgment. Duration bumped 18 → 30 to accommodate the longer teardown; palette swapped; graphic label/chips preserved.
- **NB03 (tests and classifies):** The main design-critic beat. Names both what they optimized for (defensibility + repeatability, framed as "a workpaper another auditor can retrace step by step") and what it cost (no overall pass/fail call — the opinion stays with the auditor "because that's whose name has to go on it"). Duration bumped 28 → 40. Palette swapped; graphic label/chips preserved.
- **BCRY (carry-out):** Rewrote the carry-out quote so it names the trade-off explicitly ("They optimized for defensibility and repeatability. The overall pass-or-fail call is not in the procedure, so it never happens"). `sparkLine` "Classifies. Never opines." kept from source — it fits Teardown perfectly. Duration bumped 9 → 14. Quote text in `WantQuote.props.quote` updated to match the new narration verbatim.
- **BHTF (LLM exercise — SECOND-TO-LAST):** Was already a "your turn handoff" ClaudeComposerAsk beat, but as a source it was a `hai-simple` "paste this into Claude" pattern, not a formal LLM exercise. Promoted to full `LLM EXERCISE` act with the required `llm_exercise` object: a paste-ready prompt that has the LLM (a) write an audit-support SKILL.md and (b) run it against a concrete five-transaction sample (a purchase-order approval control) that includes both clean passes and specific exception patterns (approval-after-invoice-paid, wrong approver level, missing approval), plus a dig-deeper follow-up that adds a sixth "give me your overall opinion" step to expose exactly where the procedure-shaped design falls over. Narration rewritten to walk the viewer into the same exercise. `topic` in ClaudeComposerAsk changed to `CLAUDE SKILLS · ANTHROPIC` and `folderLabel` to `@NikBearBrown`; command block shortened for the on-screen render but preserves the payload. Duration bumped 26 → 34.
- **BOUT (outro):** Kept as the LAST beat. Pattern switched `OutroSeries` → `OutroCTA` to match the NBB outro standard used by every knowledge-work-plugins nbb sibling (accessibility-review, reorder-policy, etc.). New line: `Audit Support. It tests and classifies; the opinion stays with the auditor. Liam, in for Bear.` — states the video title, states the mechanism (not the surface behavior), signs off in-for-Bear. `handle` set to `@NikBearBrown`.

## Judgement calls

1. **On-screen writer copy CHANGED (B00).** SKILL.md says "preserve on-screen card copy that still fits the register." "Support" is a Plain-register hedge; the video's actual mechanism is "test and classify." Every hai-simple sibling in the same book (accessibility-review, reorder-policy, etc.) similarly rewrote its B00 writer text and trigger words to the Teardown mechanism vocabulary — I followed that established pattern rather than the strict-preserve reading.
2. **AUTHOR.MD not present.** The `outro_source: "AUTHOR.MD :: NikBearBrown"` field is the scaffold's default. No `AUTHOR.MD` exists in the source reel folder or the `claude-bear/` book; the scaffold is aspirational. Followed every sibling nbb reel in the same book by (a) leaving `outro_source` untouched, (b) writing the outro line to the sibling family's convention (`{Title}. {carry-out fragment}. Liam, in for Bear.` + `@NikBearBrown` handle via `OutroCTA`). This is the same call `nbb-knowledge-work-plugins--claude-liam-accessibility-review` and `nbb-cwc-workshops--claude-liam-reorder-policy` both made.
3. **Duration bumps.** The narration got longer across the board (Teardown explains machinery); I raised `estimated_duration_s` per beat to match rough word counts. Real durations get set by `generate_audio_kokoro.py` at build time — the estimates are hints for the todo ledger, not clocks.
4. **`build.at`/`filled_by`/`src` fields left as the scaffold copied them from the source.** These aren't rebuilt because we don't render; they carry through so the todo ledger doesn't re-flag every beat as unfilled. When the render pass runs, `generate_audio_kokoro.py` + `compile.py` will overwrite the audio/media anyway.
