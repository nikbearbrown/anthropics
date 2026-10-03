# CONVERT-LOG — claude-tag-plugins--claude-liam-grafana-api → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: three time formats (Unix milliseconds for datasource-query + annotations, Unix seconds for state-history, RFC-3339 for silences), GNU-vs-BSD `date` gap on macOS, per-request Viewer/Editor/Admin role → 403 on mismatch, Grafana frame-format response with `results.<refId>.error` at HTTP 200, session-only bearer-token helper, two alert surfaces (Prometheus API read-only for live state; provisioning API for full CRUD with UI-lock header), dashboards full-replace + 412 on missing version, datasource fan-out → batch design, annotations endpoint with no page parameter.

- **B00** — Cold open rewritten to Teardown. Names the wrong guess explicitly (training data ≠ knowing this API's traps) and lands the same question the source lands. Hesitant-writer visual props (`text`, `triggerWords`, `replacementWords`, `seed`) preserved verbatim.
- **B01** — Anatomy rewritten in the machinery-then-design pattern. Each fact from the source is preserved; the added layer is the design read: "they optimized each subsystem for its own convenience, and pushed the cost of remembering which is which onto the caller"; "one response shape for every backend at the expense of a failure that can look like a success"; "nothing on disk. The cost is you re-do it every shell." No new facts.
- **B02** — Design beat rewritten to name each design choice explicitly (source-of-truth-by-default for provisioning, optimistic concurrency for dashboards, batched queries for the fan-out, caller-shapes-the-window for annotations) and its cost. All endpoint behavior, verbs, and status codes carried through unchanged.
- **B03** — Both-directions rewritten with the design-critic close: "This works if you value a short, scannable skill file that names the sharpest traps up front; it fails if you needed exhaustive coverage of every corner." Two-column card copy untouched (it already carries per-item facts).
- **BCRY** — Carry-out sentence left **unchanged**. Already Teardown-native (mechanism named — "map of where the traps are" — scope limit named — "only the ones the map actually marks"). Judgment call: `WantQuote.quote` must match narration, so touching either forces both; the source form already sings.
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. `act` → `LLM EXERCISE`, `llm_exercise` block added (paste-ready prompt for Claude/ChatGPT/Gemini + `dig_deeper` follow-up). The narration now reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.topic` retargeted to the reel's `CLAUDE BASICS · GRAFANA API SKILL`; `segment` set to "A Map, Not Knowledge." (echoes BCRY's sparkLine); `command` prop rewritten to numbered (1)–(4) form and tightened for the on-screen composer while preserving every constraint from the spoken prompt. `folderLabel` → `@NikBearBrown`.
- **BOUT + BCTA → BOUT** — Collapsed the source's two-beat outro (`OutroSeries` "Claude, Grafana API." then `OutroCTA` "…Liam, in for Bear.") into a single `OutroCTA` beat matching the nbb-in-`claude-bear/` convention (see judgment call below). Line: "Claude, Grafana API. Liam, in for Bear." — handle: `@NikBearBrown`. IN-FOR-BEAR LAW preserved.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown`. `register` was already `Teardown` in the scaffold. `playlist: "Claude Basics"` added to match sibling nbb reels' playlist-ordering convention. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope). `build.filled` and `build.of` dropped from 8 → 7 to reflect the outro collapse. `audience`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** Same reasoning as `nbb-claude-basics--screenshot-prompt-caching`: `WantQuote` renders the quote as its own on-screen text, so the sentence and the render are the same string. The source carry-out is already a Teardown-native shape (mechanism + scope limit). Kept as-is.
2. **Outro collapsed BOUT + BCTA → single OutroCTA.** Every sibling nbb reel in `claude-bear/` (checked: `nbb-claude-basics--screenshot-prompt-caching`, `nbb-claude-basics--stable-element-refs`, `nbb-claude-quickstarts--claude-liam-first-run`, `nbb-financial-services--claude-liam-deal-screening`) ships one outro beat, `OutroCTA` pattern, `"<title>. Liam, in for Bear."` line, `@NikBearBrown` handle. Following that convention. Also puts the LLM exercise (BHTF) genuinely second-to-last per SKILL Step 3, which a keep-both-outros structure would have violated (BHTF would land third-to-last).
3. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`) in the shot props.** Metadata says `palette: teardown` but the reference `nbb-*` reels in `claude-bear/` leave the underlying shot/graphic tokens as the humanitarians values under nbb metadata. Retinting is a downstream render concern; not touching the shot contract.
4. **Playlist added, not present in source.** Source metadata had no `playlist` field. Added `"Claude Basics"` per the topic prefix and per sibling convention (`nbb-claude-basics--screenshot-prompt-caching` has this exact playlist).
5. **B01 duration bumped 55 → 70s, B02 bumped 55 → 65s, B03 bumped 26 → 30s, BHTF 27 → 52s.** `estimated_duration_s` is a hint; the audio-first pipeline re-measures real duration after Kokoro synth. Numbers are updated to reflect the longer Teardown-rewritten narration so pantry/beat_plan doesn't nag; the real clock is whatever `generate_audio_kokoro.py` measures downstream.
6. **`redo_of` metadata preserved verbatim.** The source's `redo_of` string names the upstream Teardown source sheet; that lineage is still accurate for the nbb variant and stays useful for auditing.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-tag-plugins--claude-liam-grafana-api/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.
