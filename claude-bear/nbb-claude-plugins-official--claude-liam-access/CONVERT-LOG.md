# CONVERT-LOG — claude-plugins-official--claude-liam-access → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: `access.json` under `~/.claude/channels/discord/`; five fields (DM policy, allow list, per-channel groups, pending pairing codes, trigger patterns); safe defaults when the file is missing; pair-with-code approval flow (check-expired → add-to-allow-list → delete-pending → write marker file into approved folder); two write-time guards (read fresh before write; never auto-pick a pending code, even when there's only one); the two-message attack (DM seeds a pending code; a second message impersonates you to type "approve"); the terminal-only refusal.

- **B00** — Cold open rewritten to Teardown: names the design premise ("a Discord message could approve itself — that the channel it arrived on was proof enough") and refuses it, then hands off to the mechanism question. On-screen `BrutalistHesitantWriter` props (text, triggerWords → "Discord" → "the terminal", timings, seed) preserved verbatim.
- **NB01** — Mechanism beat now names the machinery (one file, five fields, missing-file fallback), the ordering ("before any of those five fields get touched, one gate runs first"), the honest reason ("a Discord message is text from an untrusted transport"), and the trade — "they optimized for a single source of authority, at the expense of ever letting the chat channel grant power over itself."
- **NB02** — Approval flow now written as an in-order walk with the honest guard reasoning: fresh-read closes an interleaving window; never-auto-pick lands as "the moment convenience picks for you, an attacker gets to pick for you too." Names the marker file as "the whole handoff" between the skill and the Discord side.
- **NB03** — Threat-model beat now names the attack shape out loud ("two-message attack is the specific threat model this design was built against") and the property that stops it ("the one property that keeps step one from ever becoming step two").
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call 1). `WantQuote` on-screen quote + sparkLine untouched.
- **BHTF** — Converted from generic "your turn handoff" into the **LLM EXERCISE** beat. `act` → `LLM EXERCISE`. Added `llm_exercise` block (paste-ready prompt covering state-file shape, pair-with-code flow, the terminal-only rule, and the two-message attack; plus a go-deeper follow-up on the stale-read race between reading and writing `access.json` and designing a lock or atomic-swap primitive that closes the window without breaking the terminal-only rule). Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.command` shortened to numbered (1)(2)(3) form for the on-screen composer while preserving every constraint from the spoken prompt. `ClaudeComposerAsk.props.folderLabel` retargeted to `@NikBearBrown`; `segment` set to "Only the Terminal Says Yes." to match the title.
- **BOUT** — Converted from `OutroSeries` (eyebrow / line) to `OutroCTA` (line / handle) to match settled nbb convention. Narration line unchanged ("Only the Terminal Says Yes. Liam, in for Bear."); `handle` set to `@NikBearBrown`.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so the composer chip, outro handle, and playlist ordering match the nbb channel. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name-what-it-refuses). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography`, and the `build` block left exactly as the scaffold set them. `estimated_duration_s` bumped where the rewrite lengthened the narration (NB01 22→32, NB02 20→30, NB03 20→27, BHTF 22→62 with the full prompt + go-deeper read aloud). Left `actual_duration_s` off — the scaffold didn't set it, and no audio has been regenerated.

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence is already a Teardown-native form — mechanism named ("typed into your own terminal"), scope named ("no matter how convincing it looks"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both. The sparkLine "Typed by you. Never just arrived." already sings and pairs with the sentence. Left as-is.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown`, but reference nbb reels in `claude-bear/` (e.g. `nbb-claude-basics--screenshot-prompt-caching`) leave shot/graphic colors as the humanitarians tokens under nbb metadata. Retinting is a downstream render concern; the shot/graphic contract stays identical so the same scenes can render against the teardown palette without a code change here.
3. **Manim scene names kept (`BDNB01Scene`, `BDNB02Scene`, `BDNB03Scene`).** Same reason — retinting is downstream; the beat sheet does not touch scene identity.
4. **`@NikBearBrown` folder chip + outro handle.** Applied at both the shot level (composer `folderLabel`, outro `handle`) and the metadata level (`folderLabel`, `channel_title`). No reference nbb reel bookends with `@HumanitariansAI`; playlist ordering (`Extending Claude — Skills, Plugins & Connectors`) preserved.
5. **BHTF became the LLM exercise beat (no new beat_id).** Reference nbb reels in this book convert BHTF in place — same slot, same shot component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 7-beat `filled/of` count in `metadata.build`.
6. **BOUT converted to `OutroCTA`.** SKILL.md accepts either `OutroSeries` or `OutroCTA`, but the settled nbb pattern in this book uses `OutroCTA` with `line` + `handle`. Converted; narration line and `tail_silence_s` preserved.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-plugins-official--claude-liam-access/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
