# CONVERT-LOG — books--claude-liam-research → nbb

Register: Plain → Teardown. Facts unchanged; voice, LLM exercise, and outro replaced.

## What changed

- **Rewrote `narration_text` on 23 beats** (B00, NB01–NB21, BCRY) in the Teardown register. Every fact, number, mechanism, and claim from the source survives; only the voice is different. Added mechanism + trade-off framing to each beat ("here's what's actually happening", "they optimized for X at the expense of Y", "the design being honest about what a fast reader can and can't be"). Stripped the forbidden phrases; none were in the source but none were added either.
- **B00**: prepended "Liam here, in for Bear." per IN-FOR-BEAR LAW. Held under the note's 20–35 word window (~40 words including the intro — one over the ceiling but the trigger→replacement typing has ≥9s regardless).
- **Dropped BHTF (`your turn handoff`) and replaced it with `B_LLM` (LLM EXERCISE) as second-to-last.** Matches the marketing/support/sales pattern: BHTF and B_LLM occupy the same "your turn, paste this into Claude" slot; keeping both would be redundant. B_LLM carries a paste-ready prompt for Claude/ChatGPT/Gemini (four-part market scout — size / map / complaints / confidence flags), plus a `dig_deeper` follow-up about *why* a quadrant is empty (nobody tried vs. someone tried and failed). Uses the same `ClaudeComposerAsk` scene as BHTF did.
- **Rewrote BOUT** as the NikBearBrown sign-off: "This was the NikBearBrown cut of Claude, Scouting — the research plugin, taken apart. Liam, in for Bear. Full toolkit at brutalist.art." OutroCTA `line` matches; `handle` flipped from `@HumanitariansAI` → `@NikBearBrown`.
- **Removed `_variant_todo`** from `metadata` (all four items done).
- Cleared `build.at` / `actual_duration_s` on `B_LLM` and `BOUT` because these are new/rewritten beats; a re-render pass will refill them.

## Preserved as-is

- Every `beat_id`, act label, `graphic` / `shot` block, on-screen card copy (BrutalistHesitantWriter text, chip labels, captions, WantQuote line, Manim scene names).
- Scaffold-set metadata: `audience`, `engine`, `voice_kokoro`, `palette`, `register`, `outro_source`, `typography`, `derived_from`.
- `folderLabel: "@HumanitariansAI"` on B00's card (it is not a NBB-specific asset; it was already inside the pre-rendered `media/B00.mp4`). B_LLM's new card uses `folderLabel: "@NikBearBrown"`.

## Judgement calls

- **Kept the source B00 on-screen text unchanged.** SKILL.md says preserve shot blocks; the source's "full day / an hour" typing gag already lands the video's core setup (mechanism: reading doesn't parallelize; hour vs. day). Rewriting the card would force a re-render of `media/B00.mp4`, which is outside this conversion pass's remit.
- **Did not touch BCRY's `WantQuote.props.quote` or `sparkLine`.** Same reason — `media/BCRY.mp4` is already rendered. Narration is a Teardown riff on the quote; the on-screen quote stands as-is. (Marketing's converter did rewrite the quote, but it appears BCRY was re-rendered there. Conservative choice here.)
- **Dropped BHTF entirely instead of stacking B_LLM after it.** Both beats are "paste this into Claude" prompts; back-to-back they would double the CTA. Matches the marketing template.
- **Word count on B00** is ~40 (ceiling is 35). Added the IN-FOR-BEAR intro, which is non-optional. The BrutalistHesitantWriter typing window is unrelated to narration length, and the note's ≥9s screen-time requirement is a floor, not a ceiling.
- **B_LLM prompt uses the ideas from the source BHTF prompt** (scout / size / map / verify) but reframed for any frontier LLM, not for the research plugin specifically — since the LLM exercise must produce useful output without the plugin.
