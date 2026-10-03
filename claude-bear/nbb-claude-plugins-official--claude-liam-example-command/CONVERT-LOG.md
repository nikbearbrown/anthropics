# CONVERT-LOG.md — nbb conversion

Source: `../claude-plugins-official--claude-liam-example-command/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Date: 2026-09-03

## What changed

- **Register rewrite (17 beats).** Every `narration_text` rewritten in the Teardown register (Feynman × MKBHD): the design lens throughout is *interface vs function* — the frontmatter + ARGUMENTS slot are the interface; the behavior is the empty slot you write. Design-critic frames pulled through: "string substitution, verbatim" (B05), "friction cut here, permission expansion nowhere else" (B07), "per-invocation override, not a session change" (B08), "shape right, behavior slot empty" (B12), "menu hint, not schema" (B06), "the parser tolerates its absence, not that dropping it kills the command" (B13). Facts unchanged — every field name, count, syntax mention, and mechanism claim survives.
- **Cold-open note (B00).** Updated the note's parenthetical correction example from `('just work' -> 'run a template')` to `('works' -> 'runs a template')` to match the new narration's trigger word — the BrutalistHesitantWriter props already point at `triggerWords: "works"` and `replacementWords: "runs a template"`, so the note now matches props + narration.
- **BCRY (WantQuote).** Rewrote both the narration and the on-screen `quote` prop to match, sharpening to name the interface/function split explicitly. Kept the original `sparkLine` unchanged — it already reads Teardown-clean.
- **BHTF is the LLM exercise beat.** The source's "your turn handoff" was already a paste-ready LLM prompt (ClaudeComposerAsk with a well-formed ask). Rather than insert a new second-to-last beat that would displace this into third-to-last and duplicate its function, I promoted BHTF in place — added the `llm_exercise: { prompt, dig_deeper }` block per SKILL.md §Step 3, added a "Go deeper:" follow-up covering the prose-instructions-vs-script trade-off, updated the ClaudeComposerAsk `runningText` from "paste this into Claude…" to "paste this into Claude, ChatGPT, or Gemini…" so the on-screen composer matches the frontier-LLM framing, and set `act` to `"LLM EXERCISE"`. `estimated_duration_s` bumped 24 → 42 to reflect the longer narration; audio regen on next build will overwrite the actual timing. This mirrors the pattern in the reference nbb sheet `nbb-cwc-workshops--claude-liam-reorder-policy/beat_sheet.nbb.json`, which also treats the existing BHTF as the exercise beat.
- **BOUT outro.** Kept the source's minimalist "Title. Liam, in for Bear." shape (this is the NikBearBrown outro form per the reference nbb sheet), extended with one CTA line ("Find the rest of this series on the channel.") to give the OutroCTA slot content beyond the title-and-attribution. Kept `handle: "@HumanitariansAI"` because this reel's whole scaffold is HumanitariansAI-hosted; no book AUTHOR.MD exists to override.
- **Metadata.** Set `register: "Teardown"`, kept scaffold-set `audience/engine/voice_kokoro/palette` untouched, rewrote `purpose` to describe the Teardown reading. Removed `_variant_todo` per the finish criterion. Kept `style_preset/ground/folderLabel` at their humanitarians values — palette metadata swap is out of scope for a register conversion, and the reference nbb sheet also left those alone.
- **Preserved exactly.** Every `beat_id`, all `shot`/`graphic`/`remotion.props` blocks (except the two intentional updates called out above), all card labels/chips/captions, `build.status`/`src`/`filled_by`/`at`, `audio_file` paths, `lead_silence_s`/`tail_silence_s` values, and beat order (B00, B01–B13, BCRY, BHTF, BOUT).

## Ending order verified

body → BCRY (carry-out) → BHTF (LLM exercise, second-to-last) → BOUT (outro, last). ✓

## Judgement calls (flagging for the supervisor)

1. **Promoted BHTF instead of inserting a new beat.** SKILL.md §Step 3 gives a `beat_id: "B_LLM"` schema for the exercise beat — I did not add a new beat with that id. Rationale above.
2. **Kept `folderLabel: "@HumanitariansAI"` and the source handle in the outro.** Brand default is `www.brutalist.art` per `brands/nbb.md`, but the source reel is a HumanitariansAI production and the reference nbb sheet preserved the source handle; overriding it would visibly rebrand a HAI reel mid-metadata without other palette work.
3. **Left `style_preset`, `ground`, and other humanitarians-flavored metadata untouched.** `palette: "teardown"` is the register-facing switch; the other keys are visual defaults that a downstream palette swap would handle. Same choice as the reference nbb sheet.
