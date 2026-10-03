# CONVERT-LOG — claude-basics--what-is-claude-basics → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: same-model / different-context divergence over one week, the naive "smarter model" wrong-guess, the stateless-by-default chat surface (no files / no history / no memory across chats), the project as a persistent context envelope with attached documents and a threaded history, the anchor of "the three documents you keep re-explaining at work," the mirrored empty-project failure (label changed / context didn't; uploaded-but-never-referenced files don't help), and the carry-out that a blank chat and an empty project behave the same.

- **B00** — Cold-open narration rewritten to Teardown: names the actual mechanism (statelessness) behind the naive "not smart enough" framing, then explicitly reframes not-smart-enough as the wrong diagnosis and not-fed-enough as the mechanism. On-screen `BrutalistHesitantWriter` text / `triggerWords` / `replacementWords` preserved verbatim.
- **S01** — Stakes beat now names the machinery: same tokenized weights, different context window. Diverging-output visual unchanged.
- **S02** — Wrong-guess beat sharpens the take-apart: names why the interface invites the "smarter model" read (a chat box looks like a search bar) and locates the true bottleneck (what the model can see, not capability).
- **S03** — Break-it beat rewritten to state the design choice as a design choice: "They optimized for a simple, session-free server; you pay for that choice by re-explaining yourself every Monday." Filmstrip/blank-chat visual unchanged.
- **S04** — Mechanism/anchor beat opens with the definition ("a persistent context envelope"), explains the container mechanic ("Instead of retyping the setup every chat, the setup lives with the project"), and lands on the anchor phrase verbatim.
- **S05** — Anchor-payoff beat foregrounds the mechanism over the tip: "You're not tuning prompts; you're loading the context container so the model finally has what you've been keeping in your head." Slide-into-frame visual unchanged.
- **S06** — Direction A rewritten to name the causal chain in Teardown terms: "Not because the model got smarter between Monday and Wednesday. Because the context window got denser. Same weights, more to reason over." Loaded-project visual unchanged.
- **S07** — Direction B rewritten to make the failure mode mechanical: an empty project is "a labelled folder with nothing in it — same statelessness as a blank chat, just with a nicer breadcrumb." Names the in-context-vs-on-disk distinction explicitly. Mirror visual unchanged.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). WantQuote sparkLine "Feed it, don't just ask it." kept.
- **BHTF** — Converted in place from generic "your turn handoff" into the **LLM EXERCISE** beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.segment` set to "Feed It, Don't Just Ask It."; `topic` retargeted to "CLAUDE BASICS · WEEK ONE"; `folderLabel` updated to `@NikBearBrown` to match the nbb channel. `command` prop rewritten as numbered (1)/(2)/(3) form for the on-screen composer, shortened while preserving every constraint from the spoken prompt. `output: []` added to match sibling nbb reels.
- **BOUT** — Rewritten to the NikBearBrown outro shape: single `OutroCTA` reading "What Is the Claude Basics Playlist. Liam, in for Bear.", `handle: @NikBearBrown`. Absorbs the CTA beat.
- **BCTA** — **Dropped** (see judgment call).
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown`. `purpose` rewritten in the Teardown lens (take-apart / evaluate the project container / name what it doesn't cover). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY narration unchanged.** The source carry-out sentence is already a Teardown-native form — mechanism named ("feed it the documents") and scope named ("otherwise keep re-explaining"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both. Kept as-is; the sparkLine "Feed it, don't just ask it." already sings.
2. **Collapsed BOUT + BCTA into a single BOUT.** The source had two consecutive outro beats: `BOUT` (`OutroSeries`) and `BCTA` (`OutroCTA`). The nbb convention across sibling reels (`nbb-claude-basics--screenshot-prompt-caching`, `nbb-cwc-workshops--claude-liam-reorder-policy`, `nbb-books--claude-liam-*`) is a single closing outro beat, and Step 3 requires the LLM EXERCISE to be second-to-last — that only works if there is one outro beat, not two. Merged into the reference-nbb form: one `OutroCTA` beat, `handle: @NikBearBrown`, line "[Title]. Liam, in for Bear.". The CTA line "More Claude Basics, every week." was dropped as redundant with the playlist context implicit in the title read; playlist-ordering metadata is preserved via `metadata.playlist: "Claude Basics"`.
3. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props (BHTF composer, BOUT outro) even though the source shots carried `@HumanitariansAI`. `metadata.outro_source: "AUTHOR.MD :: NikBearBrown"` and `metadata.audience: NikBearBrown` explicitly declare the identity; sibling `nbb-claude-basics--screenshot-prompt-caching` set the same precedent ("no reference reel bookends a NikBearBrown reel with `@HumanitariansAI` on the composer chip"). Fixed at the shot level and mirrored in metadata `folderLabel` / `channel_title`; underlying playlist ordering (`Claude Basics`) preserved via `metadata.playlist`.
4. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` (e.g. `nbb-books--claude-liam-*`, `nbb-claude-basics--screenshot-prompt-caching`) leave the underlying shot/graphic colors as the humanitarians tokens even under the nbb metadata. Matches convention; nothing was retinted. Retinting is a downstream render concern.
5. **Manim scene names kept (`S01Scene` … `S07Scene`).** Same reasoning as (4): the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
6. **BHTF's `estimated_duration_s` raised from 29s → 60s.** The narration now reads the full three-part paste-ready prompt plus the go-deeper follow-up aloud, matching the pattern in `nbb-claude-basics--screenshot-prompt-caching` (BHTF at 46s for a shorter prompt). Every other narration duration adjusted only where the Teardown rewrite genuinely added or removed words; original beat structure and pacing preserved.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-basics--what-is-claude-basics/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
