# CONVERT-LOG — nbb-claude-for-legal--claude-liam-matter-briefing

**Converted:** 2026-09-03 · Plain → Teardown (nbb) register-conversion pass.

## What changed

- **Every beat's `narration_text` rewritten in the Teardown register** (Feynman × MKBHD): take-it-apart openings ("Here's what's actually inside…", "Here's the test that gives it away…"), one explicit design trade-off named at B05 ("optimizes for consistency at the cost of anything not already on the record; nothing new gets discovered by the read"), and one intellectually-honest reframe at B07 ("Neither read is proof of anything about Claude; both are readings of the record you gave it").
- **B00 narration re-voiced within TIMING LAW** — 30 words (in the 20–35 range) so the BrutalistHesitantWriter still has its ≥9-second typing window; the `tracking` → `handed a file on` correction pair is unchanged.
- **BCRY carry-out sentence rewritten in both places** — `narration_text` **and** the `WantQuote.props.quote` are updated together so the on-screen quote continues to match the spoken carry-out. `sparkLine` ("Same file, same five parts.") preserved.
- **BHTF converted from `your turn handoff` → `LLM EXERCISE` (SECOND-TO-LAST beat).** Added the `llm_exercise` block with a paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini) and a "Go deeper" follow-up. The `ClaudeComposerAsk.props.command` was rewritten to display the same paste-ready prompt on-screen; the shot pattern is unchanged.
- **BOUT (outro) rewritten to fold the subtitle into the sign-off** — "Claude, Matter Briefing — what a skill actually is. Liam, in for Bear." — matching the pattern used in already-converted nbb siblings (e.g. `nbb-books--claude-liam-building-plugins`).
- **`metadata._variant_todo` removed.** `metadata.purpose` also refreshed to reflect the Teardown framing (mechanism + design trade-off) rather than the Plain-register carry-out; `metadata.register` was already set to Teardown by `brand_variant.py`.

## Facts preserved (voice change, not fact change)

- Skill = folder holding one `SKILL.md`, read top to bottom, no branching unless the file says branch.
- Five-part read verbatim: **posture, changes, deadline, questions, risk**.
- Delete-the-folder test: no memory to lose because none was ever stored — one routine stops running.
- Both-directions failure mode (B07): a clean-looking briefing does not prove nothing was missed; a briefing that misses something obvious does not prove the skill is broken — both are readings of the record.
- Anchor pair (`B03 → B06`) intact: single SKILL.md planted at B03, returned to at B06.

## Judgement calls

- **Kept humanitarian ground (`#F3EBDD`) and `folderLabel: @HumanitariansAI`** untouched — the scaffold left them as HAI attribution, and the reference sibling (`nbb-books--claude-liam-building-plugins`) does the same. `palette` reads `teardown` in metadata, but the on-screen manim graphic colors (`#F3EBDD` / `#2F2A26` / `#E4572E`) are the colors those `.mp4` files were already rendered with — changing them here would put the JSON out of sync with the frames. Any re-render into the strict teardown palette (`#FFFFFF` / `#2A1A0E` / `#C8102E`) is a separate render pass, not this conversion.
- **Refreshed `metadata.purpose`** because the old copy still described the Plain-register carry-out ("a file of steps Claude reads before it starts, run once on whatever's on record right now, not new model memory"). The new purpose keeps the same claims but frames them as Teardown does: mechanism + the trade-off (consistency purchased at the cost of coverage of anything not on the record).
- **LLM exercise prompt chose the direct application** — write a SKILL.md for one thing you brief someone on regularly, using the same five parts — because it mirrors the video's central artifact (the one-file skill) and produces a useful output on its own without the video. Dig-deeper is genuinely open-ended: what parts of your briefings depend on judgment you never wrote down, and how would the file have to change to catch them.
- **BHTF `narration_text` runs ~90 words** to accommodate the paste-ready prompt + dig-deeper; `estimated_duration_s=42` is unchanged from the reference sibling's LLM-exercise beat, which uses the same shot pattern. Real duration will be re-measured by `generate_audio_kokoro.py` in the render pass.

## Not done (out of scope)

No audio, no compile, no render. Deliverable is `beat_sheet.nbb.json` only.
