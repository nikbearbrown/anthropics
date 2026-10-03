# CONVERT-LOG — nbb conversion

Source: `../knowledge-work-plugins--claude-liam-build-zoom-contact-center-app/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Date: 2026-09-03

## What changed

**Narration (all 7 source beats).** Rewrote every `narration_text` in the
Teardown register (Feynman × MKBHD): take the skill apart, name the mechanism,
call out the design choice (depth on a fixed five-item list at the expense of
breadth). Cold open opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW.
Every fact from the source (the eight folder items, the five-item scope, the
Zoom Contact Center platform wrap-around, the carry-out) survives unchanged.

**Beat sequence.** Body ends at BCRY (carry-out). BHTF upgraded from a plain
"your turn handoff" to `act: "LLM EXERCISE"` with an `llm_exercise` block
(paste-ready prompt + `dig_deeper` follow-up). BOUT is the last beat.
Order: `B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT`.
BHTF's `command` prop mirrors the paste-ready prompt.

**Metadata.** `_variant_todo` removed. `style_preset: humanitarians → teardown`,
`ground: #F3EBDD → #FFFFFF`, `folderLabel: @HumanitariansAI → @NikBearBrown`,
`channel_title: @HumanitariansAI → @NikBearBrown`. `audience`, `register`,
`engine`, `voice_kokoro`, and `palette` were already correct from `brand_variant.py`.

**Palette re-skin in shot blocks (judgment call).** The scaffold left
per-beat color hints in humanitarians values even though `palette: "teardown"`.
Kept the shot descriptions, patterns, and structural props intact, but flipped:

- B00 `BrutalistHesitantWriter` props: `ink #2F2A26 → #2A1A0E`,
  `accent #E4572E → #C8102E`, `bg #F3EBDD → #FFFFFF`,
  `seed "hai-zoom-contact-center" → "nbb-zoom-contact-center"`.
- B01 / B02 / B03 `graphic.production_viz.colors`: humanitarians four-color
  array `["#F3EBDD", "#2F2A26", "#E4572E", "#1F4E5F"]` → teardown three-color
  array `["#FFFFFF", "#2A1A0E", "#C8102E"]` (single-accent color law).
- B01 `mechanic` sentence: "opens on cream" → "opens on white" (same visual
  redescribed for the new ground).

**Preserved exactly.** All `beat_id`s, `act` labels (except BHTF's upgrade to
`"LLM EXERCISE"`), `shot.type`, Remotion `pattern` names, non-color Remotion
props, Manim scene names, `graphic.production_viz.label` / `mechanic` /
`new_visual_element` (except the B01 ground-color word), the BCRY `WantQuote`
`quote` + `sparkLine` (it already fits the Teardown register), `note` on B00,
audio filenames, build metadata.

## Judgment calls

1. **Palette re-skin was made across shot blocks, not just metadata.** The
   Manim renderers and the Remotion `BrutalistHesitantWriter` component read
   these local color values directly, so leaving them as humanitarians would
   have produced a rendered reel that visually contradicts its own
   `palette: teardown` metadata. Treated this as a palette re-skin implied by
   the scaffold, not a facts change.

2. **BCRY quote left unchanged.** The `WantQuote` `quote` prop is on-screen
   card copy; the SKILL says preserve on-screen copy that still fits the
   register. Read it — it already takes the skill apart in Teardown voice
   ("makes Claude build the app: integration code for…"). Kept verbatim so
   narration reads the on-screen card.

3. **LLM exercise stayed topic-native (build a Zoom integration) rather than
   going meta (draft a SKILL.md).** Both would be useful, but a viewer who
   watched a video about a Zoom Contact Center skill is most likely to want
   help actually building a Zoom Contact Center integration. The prompt is
   answerable on its own without the video and the `dig_deeper` pushes past
   the reel's frame — asks Claude to name where the skill's five-item scope
   forces you out of skill-land.

4. **BOUT shortened from "Claude Doesn't Answer Your Calls — It Builds the
   Contact Center App. Liam, in for Bear." to "Claude Doesn't Answer Your
   Calls. It builds the app. Liam, in for Bear."** — same NBB outro shape as
   the exemplar (`title. spark. sign-off.`), keeps it under a 7-second beat.

5. **Playlist left as "Extending Claude — Skills, Plugins & Connectors".**
   The exemplar NBB reels use "Claude Basics", but this reel is specifically
   about a Claude skill/plugin, so the current playlist name is thematically
   accurate and channel-agnostic. No reason to overwrite it.

## Deliverable check

- [x] Valid JSON.
- [x] Every beat's `narration_text` rewritten in Teardown register.
- [x] LLM exercise beat second-to-last (BHTF), with `llm_exercise.prompt` +
      `llm_exercise.dig_deeper`.
- [x] NikBearBrown outro last (BOUT), handle `@NikBearBrown`.
- [x] `_variant_todo` removed.
- [x] `engine: kokoro`, `voice_kokoro: am_onyx` untouched (Liam, free, local).

Not rendered, no audio generated, no compile. That's the next pass.
