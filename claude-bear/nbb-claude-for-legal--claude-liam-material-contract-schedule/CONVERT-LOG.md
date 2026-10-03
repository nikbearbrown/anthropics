# CONVERT-LOG — claude-for-legal--claude-liam-material-contract-schedule (nbb)

Register: Plain → Teardown (Feynman × MKBHD). 11/11 beats rewritten; facts, beat IDs, acts, shot blocks, and graphic card copy preserved.

## Per-beat rewrites (voice only)

- **B00 (hesitant writer cold open)** — reframed as "the obvious read / wrong branch" to sharpen the misconception. Kept the 20–35 word TIMING LAW window (~30 words). `BrutalistHesitantWriter` props left as-is: the on-screen typed text ("Claude learned contract law…") and the `learned → was given` correction still frame the same misdirection, and the writer text is doctrine per the WRITER LAW note.
- **B01 (1 stakes)** — added "on some training pass" to name the imagined mechanism that isn't happening.
- **B02 (2 wrong guess, broken)** — swapped "nothing in the model changes" for "nothing in the model's weights moved" — names the actual mechanism (no gradient update) instead of hand-waving.
- **B03 (4 ANCHOR PLANTED)** — opened with "Here's what's actually happening" (preferred Teardown phrase), added "Text you can open, read, and audit" — same file, but now named as an auditable specification.
- **B04 (3 mechanism)** — added the design read: "Linear on purpose, so the same input goes through the same steps every run." Names WHY the linear runtime is a choice, not just what it is.
- **B05 (3 mechanism)** — added the explicit trade-off line: "They optimized for repeatability at the expense of judgment." This is the MKBHD design-critic beat of the reel.
- **B06 (4 ANCHOR PAYOFF)** — reworked as "smaller and more valuable" to preserve the anchor return while sharpening the value claim; added "Same file, same routine, same shape" as a tri-tap.
- **B07 (5 both directions)** — added "The failure modes cut both ways" opening and "a confident-looking string with no fact behind it" — makes the epistemic critique concrete.
- **BCRY (6 CARRY-OUT)** — tightened carry-out. Updated BOTH `narration_text` AND `remotion.props.quote` (WantQuote) so on-screen matches the voice; updated `sparkLine` to "Same file. Same shape. Every run." to echo the tri-tap.
- **BHTF (LLM EXERCISE, second-to-last)** — repurposed the source's "your turn handoff" into the mandated LLM exercise beat: `act` = "LLM EXERCISE", added `llm_exercise.prompt` + `llm_exercise.dig_deeper` block, kept `ClaudeComposerAsk` (per the 2026-07 ASK-scene rule) with `command` prop trimmed to a paste-fit version of the prompt. The prompt generalizes off the reel's subject — "pick one document you produce the same way every time and have the model draft a SKILL.md for it" — and produces a usable artifact even for a viewer who missed the video. Dig-deeper is a real next question about failure-mode cells that fill themselves in, not a summary.
- **BOUT (outro)** — kept `OutroCTA` + `@HumanitariansAI` handle (matches the sister nbb reels in `claude-bear/`). Added a Teardown spark to the sign-off: "Claude, Material Contract Schedule — same file, same shape, every run. Liam, in for Bear." Updated both `narration_text` and `remotion.props.line`.

## Metadata

- `_variant_todo` removed.
- `register` stays "Teardown" (scaffold-set).
- `purpose` rewritten to name the Teardown angle and the trade-off (repeatability vs judgment); no longer says "Plain register".
- `topic` promoted from "CLAUDE · SKILLS" to "MATERIAL-CONTRACT-SCHEDULE · ANTHROPIC SKILL" to match the sister nbb reel convention (`ip-clause-review` uses the same shape) and to name the specific skill.
- `audience` / `engine` / `voice_kokoro` / `palette` / `outro_source` / `typography` / `derived_from` left exactly as `brand_variant.py` set them.
- `style_preset` and `ground` (humanitarians cream `#F3EBDD`) kept as-is — the pre-rendered manim graphics use those colors and were not re-rendered. This matches the pattern in the sister `nbb-claude-for-legal--claude-liam-ip-clause-review` sheet.
- Preserved the original `build` block (11 filled / 11 of) unchanged. Convention across other nbb sheets is to keep the source's last-successful-build metadata pending a real nbb build; not this task's job to invalidate.

## Judgement calls

1. **BHTF: repurpose vs insert.** The scaffold contained a "your turn handoff" beat as the second-to-last position. SKILL.md §Step 3 says "insert one beat before the outro". The sister nbb reel (`ip-clause-review`) repurposed BHTF into `act: "LLM EXERCISE"` rather than inserting a 12th beat. Followed that pattern — one LLM exercise beat, no duplicate, keeps ClaudeComposerAsk which already targets the paste-ready ASK format.
2. **Outro handle.** `AUTHOR.MD :: NikBearBrown` was called for in the scaffold's `outro_source`, but the anthropics tree has no NikBearBrown-section AUTHOR.MD (the only AUTHOR.MD is `anthropics/youtube/ai-1/AUTHOR.MD` and it has no per-channel section). The sister `nbb-claude-for-legal--*` sheets all keep `@HumanitariansAI` as the outro handle. Held to that convention — flipping to `@NikBearBrown` would break the cohort's visual continuity and there's no source-of-truth NikBearBrown section here.
3. **B00 writer prop text unchanged.** The BrutalistHesitantWriter's typed text and its `learned → was given` correction still frame the same misconception the Teardown narration now sharpens. Rewriting the on-screen typed text would force a re-render of B00 (which the task explicitly forbids) and would drift the visible correction away from the audio. Kept the typed text; only the narration voice changed.
4. **Graphic card copy left in Plain-register form.** Card labels and captions ("SOUNDS LIKE A DEAL-REVIEW UPGRADE", "there's nothing to learn", etc.) still fit the Teardown register — they name mechanisms, not vibes — and rewriting them would invalidate the pre-rendered Manim scenes (BGB01Scene…BGB07Scene). SKILL.md §Step 2 explicitly allows preserving card copy that still fits.

## Not done (out of scope per invocation)

- No audio regenerated (`generate_audio_kokoro.py` not invoked).
- No compile / render.
- No re-render of B00/BCRY/BHTF/BOUT Remotion assets, even though the on-screen `quote` / `line` / `command` / `topic` props changed. The existing `media/*.mp4` files still on disk are stale relative to the new nbb voice; a subsequent render pass owns that.
