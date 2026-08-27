# BUILD-LOG — mas-turf-war

## 2026-08-16 — Built from scratch (audio + Remotion + compile)

### Starting state
- 26 beats in `beat_sheet.json`
- Flat `remotion` field at beat root (e.g. `"remotion": "ClaudePatternBeat"`)
- Missing patterns referenced: `ClaudePatternBeat`, `ClaudePullQuote`
- No `voice_kokoro` in metadata
- No `channel_title` in metadata
- Nothing in `mp3/`, no `actual_duration_s`, no Remotion renders
- `manim/` already had B10..B14 + B16..B18 (external chart animations)
- `media/` already had B06, B09, B15, B19 (STILLs)
- `pantry/clips/` had fig6, fig7 chart mp4s (silent 3840x2160 masters)

### Autonomous decisions (with reasoning)
1. **Missing patterns → ClaudeVerdictArtifact.** Per the task spec, and
   confirmed by inspecting `runtime/remotion/src/scenes/`, no
   ClaudePatternBeat / ClaudeChecklistBeat / ClaudePullQuote component
   exists. Substituted all with `ClaudeVerdictArtifact`. Props derived
   from `narration_text` (first sentence -> heading, splits into
   `artifactLines`) and `new_visual_element` (-> `artifactTitle`).
2. **Voice metadata.** Added `voice_kokoro: am_onyx` (script reads this
   field, not `voice`), preserving existing `voice: am_onyx`.
3. **Aspect ratio.** Set `aspect_ratio: 16:9` in metadata (was None).
4. **GRAPHIC beats.** External pre-rendered chart mp4s (fig6, fig7) live in
   `manim/BXX.mp4` — compile.py resolves them directly via that path.
   Added `graphic.manim` class name derived from the media_file basename
   (`fig6_turf_war_outcomes`, `fig7_time_to_resolution`) so
   `type_check.py` can find them in `HAND_DRAWN_PATTERNS` /
   `OVERFLOW_EXEMPT_PATTERNS`. Also added those entries to `type_check.py`
   with the same rationale as fig1..fig3 in mas-coordination
   (render_lib.py origin, sub-floor axis labels are structural).
5. **STILL beats already have media** — no need to re-link external webp.
6. **Compile ran in review mode.** Per standing order, do not `art final`
   or stage to TOPOST. STOP at slate cut for Bear's review.
7. **STILL fit law was applied** — this reel benefits from the same
   compile.py fix used on mas-coordination (whole image at frame 1,
   gentle 1.15x ken-burns).

### Kokoro audio result
26 beats generated, all in `am_onyx`. Durations captured in beat sheet's
`actual_duration_s` (Kokoro is the master clock).

### Remotion render
Foreground via `remotion_scenes.py`. Patterns rendered: ClaudeComposerAsk
(B01, B25), ClaudeVerdictArtifact (many), ClaudeCodeBeat (B04, B07, B22),
ClaudeTitleOutro (B26).

### Compile / gates
(Filled in after compile completes — see CHECKS-REPORT.md.)

### Files touched
- `beat_sheet.json` normalized (previous saved as `beat_sheet.pre-normalize.json`)
- `mp3/beat-B01.mp3` .. `mp3/beat-B26.mp3` (Kokoro)
- `media/B01.mp4` .. `media/B26.mp4` (Remotion)
- `brutalist-art/runtime/scripts/type_check.py` — added
  `fig6_turf_war_outcomes` and `fig7_time_to_resolution` to
  HAND_DRAWN_PATTERNS + OVERFLOW_EXEMPT_PATTERNS
- `/tmp/normalize_mas_reel.py` — one-off normalizer (kept for mas-epistemics)

## 2026-08-18 — Composer swap fix (B25)

### Defect — B25 `greeting`/`command` swapped

`ClaudeComposerAsk` in `your-turn` beats: `greeting` renders **above** the composer box; `command` renders **inside** it. B25 had these backwards:

| prop | was | now |
|---|---|---|
| `greeting` | `"The ask,"` | `"Your turn."` |
| `command` | `"Your turn."` | *(full runnable prompt — see below)* |

**What was on screen:** composer body read "Your turn." with no prompt inside; "The ask," appeared above the box. Viewer could not see or copy the prompt the narration was reading aloud.

**New `command` value:**
> "Give two agent sessions genuinely incompatible instructions on one shared folder — not hostile, just contradictory — then read both reasoning traces. Does either one ever consider that the other might be following orders too?"

Narration text **unchanged** — audio not regenerated.

### GATE T note

mas-turf-war has pre-existing GATE T failures in B04, B07, B22 (ClaudeCodeBeat with prose content, no file extension in title). These are unrelated to this fix. `art final` is blocked until those are resolved; this pass compiled via `compile.py` directly for the review cut.

### Verification

Frame extracted from `media/B25.mp4` at t=8s: "Your turn." confirmed above the composer, full two-sentence prompt confirmed inside the composer box.

### Files touched

- `beat_sheet.json` — B25 `shot.remotion.props.greeting` + `command` swapped and expanded
- `media/B25.mp4` — Remotion re-render (ClaudeComposerAsk, 15.5s, via remotion_scenes.py --force)
- `mas-turf-war.mp4` — recompiled via compile.py (278.1s)
