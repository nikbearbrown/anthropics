# CONVERT-LOG — hai-simple-what-is-claude-actually → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: the search-engine wrong-guess, the "capital of France → Paris" anchor and its return at B09, the neural-net + next-token-prediction mechanism, the second training step reshaping the same weights toward helpful/honest/harmless, the training cutoff + no-live-web flag, the B10/B11 pay-off vs cost mirror, and the WantQuote carry-out at BCRY.

- **B00** — Cold open rewritten to Teardown: names the design read behind the correction ("‘search' names the wrong machinery"). BrutalistHesitantWriter on-screen text, triggerWords/replacementWords, seed, and all typography props preserved verbatim.
- **B01** — Stakes beat now points at the gap the take-apart is *for* ("the machinery, not the marketing"), instead of only naming the feeling.
- **B02** — Wrong-guess beat sells the retrieval read with a design reason ("retrieval is how almost everything else on the web works, so retrieval is the frame you bring in"). No crimson, per beat mechanic.
- **B03** — Anchor planted; adds the take-apart cue ("keep this beat in mind; we return to it once the machinery is out on the bench"). Composition contract with B09 preserved.
- **B04** — Break-it beat now explains *why* the index model fails ("change the query wording, you can miss the entry"), then lands "there is no index to miss, because there is no index."
- **B05** — Mechanism beat 1: names the machinery ("a big stack of matrix operations"), names the single training objective, and reads the design ("everything else Claude appears to do is a downstream effect of getting very good at that one task").
- **B06** — Mechanism beat 2: names the design choice explicitly — "they didn't bolt a rulebook on top of the base model; they edited the same continuous function. Nothing external checks the output at run time."
- **B07** — Mechanism beat 3: "generation, not retrieval," landed as a mechanism read on "written fresh, from the weights, right now."
- **B08** — One-flag beat re-voiced to Teardown honesty: cutoff + no live web named as a design consequence, and the caller's job spelled out ("if you need current facts, you supply them").
- **B09** — Anchor payoff rewritten to explain what "in the weights" actually means — "compressed into the network's continuous parameter surface … not stored as a fact string anywhere you could point at." Composition contract with B03 preserved.
- **B10** — Direction A (payoff): reframes the range as a *design consequence*, not a bonus ("the generality isn't a bonus feature; it's what next-token prediction gives you once the corpus is broad enough").
- **B11** — Direction B (cost): closes with the explicit design trade — "this works if you value one general machine; it fails if you need a source you can cite." Mirrors B10 as required.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). WantQuote quote/attribution/sparkLine preserved verbatim.
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.topic` set to `CLAUDE BASICS · WHAT IS CLAUDE` to match metadata; `segment` set to `Generates, Not Finds.` (from the BCRY sparkLine); `folderLabel` updated to `@NikBearBrown` to match the nbb channel. `command` prop rewritten to numbered (1)/(2)/(3) form and shortened for the on-screen composer while preserving every constraint from the spoken prompt.
- **BOUT** — Outro left mechanically identical (OutroCTA). Narration ("What is Claude, actually? Liam, in for Bear.") already matches the NBB shape. `line` retargeted from "More Claude Basics from @HumanitariansAI." to "What is Claude, actually? Liam, in for Bear." to match nbb-reel convention; `handle` retargeted to `@NikBearBrown`. `title`/`subline` preserved.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so the composer/outro chip matches the nbb channel. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope) without changing what the reel actually claims. `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence is already a Teardown-native form — mechanism named ("generating the next most useful thing to say"), design source named ("shaped by everything Anthropic taught it to care about"). WantQuote's on-screen text IS the quote, so touching either forces touching both. Kept verbatim, matching CARRY-OUT.md.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` (e.g. `nbb-claude-basics--screenshot-prompt-caching`) leave the underlying shot/graphic colors as the humanitarians tokens even under nbb metadata. Matches convention; nothing was retinted.
3. **Manim scene names kept (`B01Scene` … `B11Scene`).** Retinting is a downstream render concern; the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
4. **`@NikBearBrown` folder chip + outro handle applied.** Reference convention: no nbb reel bookends with `@HumanitariansAI` on the composer chip or outro handle. Retargeted at both the metadata level and the shot props level, since the source metadata did not carry a distinct playlist identity worth preserving.
5. **BHTF became the LLM exercise beat in place (no new beat_id).** Reference nbb reels in this book convert BHTF in place — same slot, same shot component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 15-beat `filled/of` count in `metadata.build`.
6. **`estimated_duration_s` bumped, not recomputed.** Teardown rewrites run longer than Plain-register originals; bumped each beat's estimate roughly to match word count at ~2.7 words/sec Kokoro read rate. Kokoro re-measures on the audio pass, so these are guides, not clocks.
7. **BHTF `runningText` kept ("paste this into Claude…").** Reference nbb reel used the same string; the Claude+ChatGPT+Gemini scope is carried by the spoken narration, not by the composer chip.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim / Remotion render.
- No compile / no final master.
- No touch to source files in `hai-simple-what-is-claude-actually/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
