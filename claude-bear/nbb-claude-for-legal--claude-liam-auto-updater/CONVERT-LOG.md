# CONVERT-LOG — claude-for-legal--claude-liam-auto-updater → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: Skill = folder Claude reads before acting, Skill named `auto-updater`, SKILL.md holds the whole program in plain sentences (not code), roughly five numbered steps top to bottom, Claude reads then follows, strict-linear Steps section (branches only where a step says to), delete-step-3 falsification with no hidden fallback, same-input-twice determinism as long as the input stays inside what the file describes, edge-case blindness outside it.

- **B00** — Cold open rewritten to Teardown: opens with "Here's the assumption most people start with…" and names the design read (logic in a file, not the model) before landing the same question. On-screen `BrutalistHesitantWriter` props (`text`, `triggerWords`, `replacementWords`, `seed`, timing) preserved verbatim. `estimated_duration_s` bumped 13 → 15 to match the slightly longer narration; still inside the WRITER LAW window.
- **B01** — Anchor-plant beat rewritten. Names the design choice explicitly ("They optimized for something you can audit by reading: no compiler, no hidden source") and closes with the trade ("the file is the whole program"). Facts unchanged: folder / one SKILL.md / plain sentences / five numbered steps / read-then-follow.
- **B02** — Wrong-guess/mechanism beat rewritten in the take-apart/falsify pattern. Ends on the explicit design read: "They optimized for predictability at the expense of anything the file forgot to say." Delete-step-3 falsification preserved.
- **B03** — Anchor-payoff/both-directions beat rewritten with the paired verdict: "This works if you value replayability you can audit by reading; it fails if you need graceful degradation on the edges the author didn't foresee." Same-input-twice determinism + outside-case blindness preserved.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call 1). `WantQuote` props (`quote`, `sparkLine`) untouched.
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration now reads the full prompt + go-deeper aloud (bumped 27 → 55 s). `ClaudeComposerAsk.props.segment` set to "The File Is The Program." (matches BCRY's `sparkLine`); `folderLabel` retargeted `@HumanitariansAI` → `@NikBearBrown`; `command` prop rewritten to numbered (1)/(2)/(3) form for the on-screen composer while preserving every constraint from the spoken prompt; `output: []` added to match the nbb `ClaudeComposerAsk` schema used by other converted reels in this book.
- **BOUT** — Outro left unchanged. Already the NikBearBrown-shaped `OutroCTA` with "Liam, in for Bear." Handle updated `@HumanitariansAI` → `@NikBearBrown` to match the nbb channel.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted `@HumanitariansAI` → `@NikBearBrown` so the composer chip and outro CTA match the nbb channel (`playlist: Extending Claude — Skills, Plugins & Connectors` preserved for ordering). `purpose` rewritten in the Teardown lens (take-apart / evaluate / name the trade). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence — "A Skill's SKILL.md is the whole program. Claude follows it exactly — reliable inside what's written, blind past its edge." — is already a Teardown-native form: mechanism named ("follows it exactly"), trade named ("reliable inside… blind past its edge"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both. Kept as-is; matches the convention set by `nbb-claude-basics--screenshot-prompt-caching`.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E` / `#1F4E5F`).** Metadata says `palette: teardown` but every reference nbb reel in `claude-bear/` (e.g. `nbb-claude-basics--screenshot-prompt-caching`, `nbb-books--claude-liam-*`) leaves the underlying shot/graphic colors as the humanitarians tokens under the nbb metadata. Retinting is a downstream render concern; the graphic/shot contract stays identical so the same Manim scenes can be re-rendered against the teardown palette without a code change.
3. **Manim scene names kept (`AUB01Scene`, `AUB02Scene`, `AUB03Scene`).** Same reason as (2) — retint at render time, don't rename the scenes.
4. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props even though the underlying metadata `playlist` stayed at "Extending Claude — Skills, Plugins & Connectors" for ordering — no reference nbb reel bookends with `@HumanitariansAI` on the composer chip or the outro CTA. Fixed at the shot level, not the playlist level, so ordering is preserved.
5. **BHTF became the LLM exercise beat (no new `B_LLM` beat_id).** Reference nbb reels in this book convert BHTF in place — same slot, same `ClaudeComposerAsk` shot component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 7-beat `filled/of` count in `metadata.build`.
6. **`estimated_duration_s` on rewritten beats bumped modestly (B00 13→15, B01 22→26, B02 22→24, B03 25→28, BHTF 27→55).** Teardown narrations run a touch longer, and BHTF now reads the full paste-ready prompt aloud. `actual_duration_s` fields removed by the scaffold — will re-populate on audio regen.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-for-legal--claude-liam-auto-updater/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
