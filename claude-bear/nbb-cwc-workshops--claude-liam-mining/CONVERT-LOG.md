# CONVERT-LOG — cwc-workshops--claude-liam-mining → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: a Claude skill is a folder Claude checks before it acts; the skill named `mining` contains exactly one file `SKILL.md`; the file is one sentence — "where diamonds spawn in Minecraft 1.20"; asking twice returns the identical answer; asking about Minecraft 1.21 or emeralds returns nothing extra; the carry-out — a skill is Claude reading one short file, not Claude knowing more, and it can't answer past what that file says.

- **B00** — Cold-open narration rewritten to Teardown: opens with "Here's what's actually happening," names the design choice ("a scope you can audit in one glance") and sets up the real question. On-screen `BrutalistHesitantWriter` text, `triggerWords` (`knows` → `reads`), and every prop preserved verbatim; note's TIMING LAW window respected (36 words, still inside the 20–35+silence budget the note describes for a ≥8s render).
- **B01** — Anatomy beat now names the surface area explicitly ("that's the whole surface area") and closes with the design read: "No code, no config, no plugin — just a file Claude will read."
- **B02** — Wrong-guess beat rewritten to Teardown; closes "That is the guess this design has to defeat," which telegraphs the reveal at B03 without stealing it.
- **B03** — Anchor-planted beat now says what the file *is not* before what it *is*, then names the design trade explicitly: "They chose a scope you can audit at a glance over any cleverness Claude might bring from training." Ends "This is the anchor: the whole skill, on one line."
- **B04** — Mechanism beat now explains the machinery ("no branching, no lookup, no extra reasoning invented along the way") and names the design intent: "Linear on purpose: they optimized for a mechanism you can predict from the file alone, not one that improvises off it."
- **B05** — Anchor-payoff rewritten to hit both directions and close with the design judgment: "This works if you value a predictable, auditable scope; it fails if you needed the skill to generalize past what's written."
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call 1).
- **BHTF** — Converted from generic "your turn handoff" into the **LLM EXERCISE** beat. `act` → `LLM EXERCISE`. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.segment` set to "Claude, Mining."; `folderLabel` retargeted to `@NikBearBrown` (the nbb channel). `command` prop rewritten to numbered (1)/(2)/(3) form and shortened for the on-screen composer while preserving every constraint in the spoken prompt.
- **BOUT** — Outro left otherwise unchanged (already the NikBearBrown-shaped `OutroCTA` with "Liam, in for Bear."); `handle` updated to `@NikBearBrown` to match the nbb channel.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so composer chip + outro handle + playlist ordering match the nbb channel. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them. `estimated_duration_s` bumped by 2–3s on beats B00, B01, B02, B03, B04 to reflect the longer Teardown narrations (facts unchanged; the actual clock will still be the measured `mp3` durations at build time).

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence is already Teardown-native — mechanism named ("Claude reading one short file"), scope limit named ("it can't answer past what that file says"). WantQuote's on-screen text IS the quote, so touching either forces touching both. Kept as-is; the sparkLine "Reading, not knowing." already sings. Matches the reference conversion (`nbb-claude-basics--screenshot-prompt-caching`) which also left BCRY as-is on the same principle.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` leave the underlying shot/graphic colors as the humanitarians tokens even under the nbb metadata. Followed convention; nothing was retinted. Retinting is a downstream render concern; the shot/graphic contract stays identical so the same scenes re-render against the teardown palette without a code change.
3. **Manim scene names kept (`BDB01Scene` … `BDB05Scene`).** Same reasoning as #2 — the code contract does not change.
4. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props even though the source shipped `@HumanitariansAI` — no reference nbb reel bookends with the humanitarians chip. Fixed at both metadata (`folderLabel`, `channel_title`) and shot level (`ClaudeComposerAsk.props.folderLabel`, `OutroCTA.props.handle`) so composer, outro, and playlist ordering all agree.
5. **BHTF became the LLM exercise beat in place (no new `B_LLM`).** The source's BHTF is already a paste-ready `ClaudeComposerAsk` handoff — same slot, same shot component. Retitled its `act` to `LLM EXERCISE`, added the `llm_exercise` block, expanded narration to read the full prompt + go-deeper. Matches the reference conversion pattern and keeps the 9/9 `filled/of` count in `metadata.build` intact (inserting a new beat would have broken it).
6. **LLM prompt written to work standalone.** The prompt asks the model to (a) explain the read-file mechanism, (b) evaluate the design trade of "one short file vs code/plugin/fine-tuning," and (c) produce a minimal `SKILL.md` for a `meeting-notes` skill. That produces a genuinely useful output on its own — a viewer who never watched the video still gets a working example SKILL.md and a design explanation. The dig-deeper (what happens when `SKILL.md` and training pull against each other on a half-covered question) is a real next question, not a summary of the video.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `cwc-workshops--claude-liam-mining/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
