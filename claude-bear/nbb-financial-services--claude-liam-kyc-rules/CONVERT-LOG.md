# CONVERT-LOG — financial-services--claude-liam-kyc-rules → nbb

Converted `beat_sheet.json` (Plain, hai-simple) → `beat_sheet.nbb.json` (Teardown, NikBearBrown).

## What changed

- **Metadata**: dropped `_variant_todo`. Kept `register: "Teardown"`, `audience: "NikBearBrown"`, `palette: "teardown"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"` as the scaffold set them. Left `style_preset: "humanitarians"` and `ground: "#F3EBDD"` alone — the source-native palette props still feed the visuals; the *register* is what the nbb pass owns, not the surface color of already-rendered media beats.
- **Narrations rewritten in Teardown register**: B00, NB01, NB02, NB03 all re-voiced. Machinery named ("the file is the program"), design choices called out ("optimized for auditability over cleverness", "optimized for defensible reasoning over speed to a verdict"), trade-offs stated in plain terms ("no case closes without a human touching it"). Facts, numbers, file names (SKILL.md, kyc-rules), and the four-step pipeline all survive unchanged.
- **BCRY (carry-out)**: left verbatim. It's the money line and it's on-screen inside the `WantQuote` pattern — narration and the `quote` prop have to match. The sentence already reads clean.
- **BHTF converted to LLM EXERCISE**: `act` changed from `"your turn handoff"` → `"LLM EXERCISE"`. Added `llm_exercise` object with paste-ready `prompt` + `dig_deeper` follow-up. Narration re-cut to (1) read the paste-ready prompt aloud, then (2) name the connection to what kyc-rules does, then (3) issue the "Go deeper" prompt. Kept the `ClaudeComposerAsk` scene and its `command` prop in sync with the exercise prompt.
- **BOUT (outro)**: kept the source `OutroSeries` pattern verbatim — eyebrow `KYC-RULES · @HumanitariansAI`, line `It Scores and Routes. It Doesn't Decide.`, sign-off `Liam, in for Bear.` This is already the NikBearBrown-brand outro form; nothing to replace.

## Judgement calls

- **BHTF prompt tightening**: the source prompt was `"walk me through each rule, whether the record satisfies it, and what's missing"`. I added `"one at a time"` and `"what evidence you used"` in the LLM prompt (and matched the `command` prop). Reason: a Teardown-register exercise names the machinery — walking rules "one at a time" and asking for *evidence* is the difference between a scoring exercise and a vibes exercise, and it reflects what kyc-rules literally does (list every rule outcome tied to the rule that produced it). No claim about the skill itself was changed.
- **BCRY not rewritten**: judged that changing narration to Teardown flourishes here would drift from the `quote` prop that renders on-screen. The carry-out is the video's crown; matching audio to visual matters more than register polish on one sentence.
- **`estimated_duration_s` bumped** on rewritten beats (B00 13→15, NB01 18→22, NB02 18→22, NB03 28→34, BHTF 26→42) to reflect longer narration text. These are hints only; Kokoro measures the truth downstream.
- **`actual_duration_s` dropped** on every rewritten beat — they were the source's measured Kokoro durations and no longer describe the new narration. The next `generate_audio_kokoro.py` pass will write the correct ones. Left the `audio_file` and `build` fields alone so compile still points at the right media until re-render.
- **Palette metadata mismatch left alone**: metadata carries both `palette: "teardown"` (nbb) and `style_preset: "humanitarians"` / `ground: "#F3EBDD"` (source). This is intentional — the register pass is my job; palette swaps + Manim regeneration to true teardown white belong to the render pass, not this conversion.
- **No IN-FOR-BEAR violation**: Liam is named as "in for Bear" only in the outro (source already had it). Cold open leaves the persona implicit, matching sibling nbb reels.

## Not done (deferred to render pass)

- Audio regeneration (`generate_audio_kokoro.py`).
- Manim re-render for NB01/NB02/NB03 if palette conversion from humanitarians cream to teardown white is wanted.
- Compile.
