# CONVERT-LOG — claude-for-legal--claude-liam-cocounsel-legal:deep-research → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: cocounsel-legal deep-research is a folder holding a single SKILL.md, plain-language instructions turning a research question into a synthesized, cited answer using Westlaw Deep Research; Claude reads it before it starts, works through it top-to-bottom in order, no branching unless the file itself branches; delete the folder and no legal reasoning is lost because none was ever added; two failure modes (well-cited memo doesn't prove judgment; missed case doesn't prove the skill is broken).

- **B00** — Cold open rewritten to Teardown: "Here's what's actually happening." Names the mechanism directly (Claude followed a written file, didn't reason). On-screen hesitant-writer text (`text`, `triggerWords`, `replacementWords`, `seed`) preserved verbatim; TIMING LAW word window respected (~33 words).
- **B01** — Wrong-guess beat rewritten to name the linguistic trap: the word "skill" carries the misread, and the misread is wrong. "That's the natural read. It's the wrong read."
- **B02** — Wrong-guess-broken beat rewritten as a mechanical test — deletion — and lands the design read: "no legal reasoning is missing — because none was added."
- **B03** — Anchor planted; keeps the source facts verbatim (folder, SKILL.md, Westlaw Deep Research, plain language, read-before-start) and adds one Teardown line naming the design choice: "capability routed through documentation, not through weights."
- **B04** — Mechanism beat rewritten to name the machinery and the control-flow read: "The control flow lives in the document, not in the model."
- **B05** — Spec-not-judgment beat given explicit optimize-for / trade-off form: "They optimized for consistency … The trade is scope."
- **B06** — Anchor payoff rewritten with the design judgment: "repeatability, not reasoning. Works if you value a stable output shape; fails if you needed a lawyer's call on which case actually matters."
- **B07** — Both-directions beat named as "Two failure modes here, both mistaking output for judgment." Same rule stated at the close: "read the file, not the memo."
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). `WantQuote` on-screen quote and `sparkLine` preserved.
- **BHTF** — Converted from generic "your turn handoff" into the **LLM EXERCISE** beat. Added `llm_exercise` block (paste-ready prompt for Claude/ChatGPT/Gemini + `dig_deeper` follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud (SKILL.md and .M-D spelled out for TTS). `ClaudeComposerAsk.props.segment` set to "A Skill, Not a New Judgment."; `folderLabel` → `@NikBearBrown` to match the nbb channel. `command` prop rewritten to numbered (1)/(2) form and shortened for the on-screen composer while preserving every constraint from the spoken prompt (recurring legal-research question, plain-language ordered steps, top-to-bottom, no branching, sources / output format / citation style, plus the file-vs-prompt contrast). `estimated_duration_s` bumped to 50s to match the longer exercise text.
- **BOUT** — Outro left unchanged as `OutroCTA`. `handle` retargeted `@HumanitariansAI` → `@NikBearBrown` to match the nbb channel.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` (playlist "Claude Basics" preserved for ordering). `purpose` rewritten in the Teardown lens (take-apart / evaluate design choice / name what it does not do), keeping the carry-out clause verbatim. `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography`, `anchor_pair`, `one_flag`, `gate_c`, `gate_h`, and `build` block left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence — "A skill doesn't hand Claude legal judgment — it's a file of steps that turns a research question into the same searched-and-cited answer, the same way, every time." — is already Teardown-native: mechanism named ("file of steps"), scope-shape named ("same … same way, every time"), and Feynman-honest about what it isn't ("doesn't hand Claude legal judgment"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both. Kept as-is; the `sparkLine` "Same file, same structure." already sings.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` (e.g. `nbb-claude-basics--screenshot-prompt-caching`) leave the underlying shot/graphic colors as the humanitarians tokens even under the nbb metadata. Followed convention; nothing retinted here. Retinting is a downstream render concern.
3. **Manim scene names kept (`BGB01Scene` … `BGB07Scene`).** Same reasoning — retinting to the teardown palette is a downstream render concern; the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
4. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props (BHTF `folderLabel`, BOUT `handle`) so the composer chip and end-card handle match the nbb channel — no reference reel bookends an nbb reel with `@HumanitariansAI`. Also retargeted at the metadata level (`folderLabel`, `channel_title`) to be internally consistent; `playlist: "Claude Basics"` preserved for ordering across the Claude Basics channel.
5. **BHTF became the LLM exercise beat (no new beat_id).** Reference nbb reels in this book convert BHTF in place — same slot, same `ClaudeComposerAsk` component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 11-beat `filled/of` count in `metadata.build`. Anchor pair `B03 -> B06` is undisturbed and remains the anchor-planted/anchor-payoff structure.
6. **LLM exercise question chosen inside the same legal-research subject.** The recurring question example ("every court that's addressed personal jurisdiction over a Delaware LLC formed for a single deal") is a real, narrow, answerable legal-research task — the kind a lawyer actually runs repeatedly and the exact kind cocounsel-legal deep-research is designed to serve. Keeps the exercise inside the video's subject, produces a useful `SKILL.md` on its own, and the `dig_deeper` question (hand the same model a question outside the SKILL.md's steps; how would you notice you'd wandered off the map?) is a real next probe of the video's B05/B07 point about scope — not a summary.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-for-legal--claude-liam-cocounsel-legal:deep-research/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
