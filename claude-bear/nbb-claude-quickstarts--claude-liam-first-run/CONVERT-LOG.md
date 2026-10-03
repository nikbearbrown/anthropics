# CONVERT-LOG — claude-quickstarts--claude-liam-first-run → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: the skill is called first-run, its whole instruction set lives in a single SKILL.md file in plain language, Claude reads the Steps section top-to-bottom and executes linearly (no branching unless a step says so), the specified scope is exactly (a) check the environment, (b) run one safe browser-only task, (c) open the trajectory viewer, Claude runs that exact sequence every time and has nothing to say about anything the file never described, and the carry-out that a skill is a folder of plain-language instructions Claude reads before it acts, not a built-in capability.

- **B00** — Cold-open narration rewritten to Teardown: names the design choice as a design choice ("skills are text, not code") and preserves the `built`→`written` pivot demanded by the on-screen `BrutalistHesitantWriter` (triggerWords/replacementWords/text kept verbatim). `estimated_duration_s` raised 14→16s for the added design-read sentence; still short enough to respect the ≥8s writer window.
- **B01** — Anatomy beat now names the machinery ("one folder, one file inside it — SKILL.md") and the design choice ("legibility over cleverness"). Folder/file/instruction-set visual unchanged; the on-screen "The file is the program." footer is echoed by the closing narration beat.
- **B02** — Pipeline beat rewritten to state the design choice explicitly: "linear by design; no branching unless a step explicitly says branch. They chose predictability over expressiveness." Straight-arrow visual unchanged.
- **B03** — Mechanism/scope beat sharpens the take-apart: names the exact three specified steps in the file's own words, then names the wall around the skill as a feature and the cost ("at the cost of any improvisation"). Bounded-box + dashed-boundary visual unchanged.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). WantQuote sparkLine "Written down, not built in." kept.
- **BHTF** — Converted in place from generic "your turn handoff" into the **LLM EXERCISE** beat. Added `llm_exercise` block (paste-ready three-part prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration now reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.segment` set to "Written Down, Not Built In." (mirrors BCRY sparkLine); `topic` kept as "CLAUDE BASICS · SKILLS" (on-topic); `folderLabel` updated to `@NikBearBrown` to match the nbb channel; `command` prop rewritten as numbered (1)/(2)/(3) form for the on-screen composer, shortened while preserving every constraint from the spoken prompt. `output: []` added to match sibling nbb reels. `estimated_duration_s` raised 27→62s to cover the full read (in line with `nbb-claude-basics--what-is-claude-basics` BHTF at 60s).
- **BOUT** — Retargeted to the NikBearBrown outro: `handle: @HumanitariansAI` → `@NikBearBrown`. `OutroCTA.props.line` kept as-is ("Claude, First Run. Liam, in for Bear.") — the source line was already in NBB shape.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown`. `purpose` rewritten in the Teardown lens (take-apart the SKILL.md pipeline / evaluate the design choice / name what it costs, then land the same carry-out). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY narration unchanged.** The source carry-out sentence is already a Teardown-native form — names the negation ("isn't a built-in capability"), the mechanism ("plain-language instructions Claude reads before it acts"), and the scope ("only as far as the file goes"). `WantQuote`'s on-screen text IS the quote, so touching either forces touching both. Kept as-is; the sparkLine "Written down, not built in." already sings and pairs with the B00 built→written pivot.
2. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props (BHTF composer, BOUT outro) even though the source shots carried `@HumanitariansAI`. `metadata.outro_source: "AUTHOR.MD :: NikBearBrown"` and `metadata.audience: NikBearBrown` explicitly declare the identity; sibling `nbb-claude-basics--what-is-claude-basics` set the same precedent. Fixed at the shot level and mirrored in metadata `folderLabel` / `channel_title`; underlying playlist ordering (`Claude Basics`) preserved via `metadata.playlist`.
3. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E` / `#1F4E5F`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` leave the underlying shot/graphic colors as the humanitarians tokens even under the nbb metadata. Matches convention; nothing was retinted. Retinting is a downstream render concern.
4. **Manim scene names kept (`B01Scene` / `B02Scene` / `B03Scene`).** Same reasoning as (3): the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
5. **BHTF `estimated_duration_s` raised 27→62s.** The narration now reads the full three-part paste-ready prompt plus the go-deeper follow-up aloud. Matches the pattern in `nbb-claude-basics--what-is-claude-basics` (BHTF at 60s for a similarly sized prompt). Every other narration duration adjusted only where the Teardown rewrite genuinely added or removed words; original beat structure and pacing preserved.
6. **B00 `estimated_duration_s` raised 14→16s.** The added design-read sentence ("That's the design choice: skills are text, not code.") pushes the read a touch longer. Still short enough to respect the WRITER LAW ≥8s window; original `lead_silence_s: 0.8` preserved so the correction ('built' → 'written') stays visible on a late frame.
7. **BOUT `line` unchanged.** Source already reads "Claude, First Run. Liam, in for Bear." — the exact NBB outro shape ("[Title]. Liam, in for Bear."). Only the handle needed retargeting.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-quickstarts--claude-liam-first-run/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
