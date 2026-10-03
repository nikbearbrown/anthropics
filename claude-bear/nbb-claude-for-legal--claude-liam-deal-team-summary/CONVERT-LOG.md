# CONVERT-LOG — claude-for-legal--claude-liam-deal-team-summary → nbb

Register conversion only. No audio, no render, no compile.

## What changed

- **Register — every `narration_text` rewritten in Teardown (Feynman × MKBHD).** Each beat now takes the mechanism apart, names what the design was optimized for, and names the trade. The spine is: *they optimized for repeatable structure at the expense of judgment*.
- **Facts preserved verbatim.** The five-field shape (parties, key terms, status, open issues, next steps), the Aster Corp / Vale Robotics illustrative deal, the SKILL.md-is-plain-markdown claim, and the "structure isn't a fact-check" line all survive unchanged. No new deal details, no invented clauses.
- **LLM exercise inserted as second-to-last beat (`BHTF`).** Reused the existing `BHTF` slot and its `ClaudeComposerAsk` shot (already a paste-ready-prompt beat in the source). Added the required `llm_exercise` block with `prompt` + `dig_deeper`. Renamed the act from `your turn handoff` to `LLM EXERCISE` per SKILL §Step 3. The dig-deeper follow-up ("is the second answer more thoughtful, or is the shape not yet stable enough to trust — and what would you change to lock it?") is a real next question, not a summary.
- **Outro reduced to a single last beat (`BOUT`).** Source had two outros (`BOUT` OutroSeries + `BOUTCTA` OutroCTA); SKILL §Step 5 requires exactly one outro *after* the LLM exercise. Collapsed to one `OutroSeries` beat with narration `Claude, Deal Team Summary. Liam, in for Bear.` — matching the reference `nbb-claude-for-legal--claude-liam-ip-clause-review` conversion.
- **`_variant_todo` removed** (all four steps done).
- **Metadata:** flipped `register` → `Teardown`, `palette` → `teardown`. Left `engine`/`voice_kokoro` as the scaffold set them (`kokoro` / `am_onyx`). Added `subtitle: "The Deal-Team-Summary Skill"` for the Teardown title-card convention. Updated `metadata.purpose` to describe the new register + carry-out, not the source's Plain-register purpose.
- **`estimated_duration_s`** raised on every rewritten beat to reflect longer Teardown narrations. The audio pass will overwrite these; they're just planning hints.
- **Card copy left as-is.** Every `title` / `label` / `sub` on the `FormBCard` shots reads fine in Teardown register — no structural edit warranted. SKILL §Step 2 says preserve where it fits.

## Judgement calls

- **Channel stayed `@HumanitariansAI`.** SKILL §Step 4 and `brands/nbb.md` say the outro sources from `AUTHOR.MD :: NikBearBrown` (default channel `www.brutalist.art`). No such `AUTHOR.MD` exists for this book (`anthropics/claude-bear/`); the only `AUTHOR.MD` in the tree lives at `anthropics/youtube/ai-1/AUTHOR.MD`. The reference nbb conversion (`nbb-claude-for-legal--claude-liam-ip-clause-review`) also kept `@HumanitariansAI` on the outro. Followed that precedent — the reel was authored for HAI, and re-badging it to a channel Bear hasn't asked for on this reel is a bigger call than a register conversion should make.
- **`BOUT` + `BOUTCTA` collapsed rather than kept.** SKILL §Step 5 requires *outro is LAST beat*, i.e. exactly one outro after the LLM exercise. Keeping both would push the LLM exercise to third-from-last. Collapse matches the reference nbb pattern.
- **BHTF reused for the LLM exercise instead of inserting a new beat.** The source `BHTF` was already a paste-ready-prompt beat with `ClaudeComposerAsk` shot — exactly the shape §Step 3 specifies. Reusing it (with rewritten narration + new `llm_exercise` block) is the minimum change that meets the spec; inserting a duplicate beat would render two composer cards back-to-back.
- **`build.status: VIDEO` / `build.src: media/*.mp4` left untouched.** Those paths point to media rendered from the *old* narrations and no longer match. The compile pass will regenerate against the new audio; leaving the fields as scaffold-set follows the reference conversion. The audio+render pass owns cache invalidation, not this pass.
