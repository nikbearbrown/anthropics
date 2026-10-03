# CONVERT-LOG — claude-code--claude-liam-hook-development → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: reminder vs hook, config-file vs conversation-scope, nine fixed hook events, from before-a-tool-runs to session-starts/ends, command hooks (bash script, deterministic) vs prompt-based hooks (Claude's judgment), PreToolUse checks file path and returns allow / deny / ask, plugin `hooks.json` wraps events in a `hooks` key, project `settings.json` puts events at the top level, swap silently never fires, `$CLAUDE_PLUGIN_ROOT`, 60-second default timeout.

- **B00** — Cold open rewritten to Teardown: opens with "Here's what's actually happening", names the design opposition (conversation-scoped reminder vs runner-read script). 31 words, within the 20–35 TIMING LAW window; `lead_silence_s: 0.8` preserved. On-screen hesitant-writer text (`text`, `triggerWords`, `replacementWords`) preserved verbatim.
- **B01** — Wrong-guess beat now closes with the explicit design read: "Determinism over convenience — you pick which of the nine you actually want." Names why the reminder fails (finite conversation window) and what the hook trades to survive it.
- **B02** — Anchor beat rewritten; opens "the choice is a philosophy", explains the machinery of a command hook (shells out, reads the exit code) vs a prompt-based hook (Claude's judgment, "flexible until the day you needed it not to be"), lands the anchor as short, hard clauses: "Deny fires. The write never happens. Not undone. Never happened." Manim scene (`HDVB02Scene`) and colors unchanged.
- **B03** — Anchor payoff rewritten; ends with the design judgment: "Permissive parser is the design choice; the caller pays with a hook that looks configured and does nothing." Names the exact machinery of the silent-never-fires failure (runner reads it, doesn't find what it expects where it expects it).
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). `WantQuote.props.sparkLine` "Configured, or silent." kept.
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud (dot-env, dollar CLAUDE_PLUGIN_ROOT, sixty-second, spelled out for TTS). `ClaudeComposerAsk.props.segment` set to "Configured, Or Silent." (matches the carry-out sparkline); `folderLabel` retargeted to `@NikBearBrown` to match the nbb channel; `command` prop rewritten to numbered (1)/(2)/(3) form. `output: []` added to match reference nbb-composer shape.
- **BOUT** — Outro left unchanged: already the NikBearBrown-shaped `OutroCTA` with "Liam, in for Bear." `handle` updated to `@NikBearBrown`.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so the composer chip and playlist ordering match the nbb channel. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name the scope). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out is already Teardown-native — mechanism named ("script wired to one exact moment"), scope limit named ("or not at all"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both, and the sparkLine "Configured, or silent." already sings. Matches the reference nbb pattern (BCRY left unchanged in `nbb-claude-basics--screenshot-prompt-caching`).
2. **BHTF converted in place (no new `B_LLM` beat).** The reference nbb reels in this book convert BHTF in place — same slot, same `ClaudeComposerAsk` shot, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 7-beat `filled/of` count in `metadata.build`.
3. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E` / `#1F4E5F`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` leave the underlying shot/graphic colors as the humanitarians tokens under nbb metadata. Retinting is a downstream render concern; nothing was retinted here.
4. **Manim scene names kept (`HDVB01Scene` … `HDVB03Scene`).** Same reason — the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
5. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props even though the `playlist` field stayed `Claude Code` — no reference nbb reel bookends with `@HumanitariansAI` on the composer chip. Fixed at the shot level, not by touching the playlist identity used for ordering.
6. **B00 word count.** Rewrite is 31 words with `lead_silence_s: 0.8` — inside the 20–35 window the TIMING LAW note calls for. Source was 34 words, 10.11s actual; rewrite trends slightly shorter, still gives the typing its >=9s window.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-code--claude-liam-hook-development/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
