# AUDIT — nbb-clear-vs-compact (FILMLOOP 2026-08-31)

Sheet was rebuilt under the LOCKED SCRIPT + SHOT LIST contract (see `REBUILD-LOG.md`).
Snapshot preserved at `beat_sheet.pre-rebuild.json`. All audit fixes were applied to
`beat_sheet.json` BEFORE audio/compile.

## 1. Stale renders — PASS
No `*.mp4` in reel folder. Nothing to purge. `media/`, `manim/`, `clips/` do not exist yet.

## 2. Bookends — FIXED
Rebuild introduced the four canonical bookends:
- `B00` — ClaudeComposerAsk (cold open, ask answered)
- `BVDT` — ClaudeVerdictArtifact (verdict, real content authored — see check 4)
- `BHTF` — ClaudeComposerAsk (your-turn, real exercise authored — see check 5c)
- `BOUT` — ClaudeTitleOutro (title re-read + subline)

Four legacy pre-canonical duplicates (NBB00–NBB03) were removed — see REBUILD-LOG.md.

## 3. Spark lines — FIXED
- `B00.props.greeting = "Cześć, Liam"` (Polish "Hi" + name; rotates language)
- `BHTF.props.greeting = "Your turn."`
- Inner ClaudeComposerAsk `B05.props.greeting = "Paste after /clear."` (3 words, from narration)
- Beat-level `spark_line` on B01–B04 (drawn beats) all ≤5 words, compressed from beat narration:
  - B01: "Stale context biases output."
  - B02: "Chat gone. Code stays."
  - B03: "Load-bearing: compact. Done: clear."
  - B04: "Progress is on disk."

## 4. Verdict — AUTHORED
Body = 5 beats (B00 setup + B01–B04) × 80±10 words each = ≥400 words → **AUTHOR**, not strip.
Placeholder BVDT (Key finding one/two/three, empty narration) replaced with three lines
derived from body verbs/nouns; narration authored to speak them. See REBUILD-LOG.md.
`verdict_audit.py` run against `books/anthropics/` — this reel is NOT in the violations list.

## 5. Card text — FIXED
- `B01.FormBCard.items` (was three "Key point one/two/three" with empty `sub`) → three real
  items with labels and complete `sub` lines derived from beat narration.
- `B04.FormBCard.items` — newly authored (beat previously had no template).
- All FormB `label` values ≤ ~25 chars, no mid-word clip risk.

## 5b. Chart text — N/A
No Manim BarChart / axes beats in this reel. B02/B03 Manim scenes are layer stack + text
concept cards, not data charts. (Their captions in `scenes_std.py` are already whole
sentences and short category labels, not narration slices.)

## 5c. Your-Turn — AUTHORED
`BHTF.command` was the templated "Take what you learned from [X] and apply it…"
placeholder. Replaced with a real, scaffolded exercise built from the reel's own rule
(audit the transcript, apply the compact/clear/rewrite decision, report back).
No square brackets, no title restated.

## 6. Punt sweep — PASS
Zero gen-AI asks. Zero unfilled `fill_slates` / `remotion_scenes` slates in the rebuilt
sheet. Zero DoodleScene / DoodleChart. Zero STILL archive slots. Every beat maps to a
concrete template: 4 × ClaudeComposerAsk, 2 × FormBCard, 2 × Manim scene,
1 × ClaudeVerdictArtifact, 1 × ClaudeTitleOutro.

## 7. Card-only — PASS
B02 and B03 route to Manim scenes (`Scene_B02_NbbClearVs`, `Scene_B03_NbbClearVs`) — two
drawn beats in the body.

## 8. Lens audit — PASS (≥3 moves)
Against `youtube/LENS-NOTES.md`:
- **Hume** — B01: "Quality degrades because the context contains the problem, not because
  the model changed." The observation is a property of the transcript, not the model.
- **Popper** — B03: "The test: is the conversation still doing work? Yes: compact. No:
  clear." A rule stated in advance for what counts as which command.
- **Descartes** — B04: "If Claude has corrected the same issue more than twice, the
  context is polluted." A checklist item — a triggering condition that falsifies "the
  context is still fine".
- **Plato** — B04: "The progress is not in the chat — it is in the code on disk and the
  instructions in CLAUDE.md." Artifact (chat) vs world (code + CLAUDE.md); the reel is
  built on that distinction.

## 9. Brand fields — FIXED
- `folderLabel: "@NikBearBrown"` (channel handle) on every composer.
- `engine: kokoro` / `voice: am_onyx` on every beat (VOICE-LOCK).
- Persona coherence: narration says "This is Cześć, Liam — in for Bear." Voice `am_onyx`
  IS the Liam voice. Consistent.

## 10. Pacing — LOG
Estimated durations are pre-measurement; Kokoro will overwrite `actual_duration_s`.
Against the loose `estimated_duration_s`:
- B04: 89 words / 22 s ≈ 4.05 wps — over 3.4; likely renders closer to ~30 s once Kokoro
  measures it (comparable to the old NBB01 recap at ~2.9 wps).
- B00/B01/B03: ~3.5 wps against 22 s — marginally over; likely resolves at measurement.
Nothing retimed silently; the master clock will come from the mp3s.

## 11. type_check.py — PASS
`GATE T: PASS`. §8.10 chart-text audit: B01=0.46, B04=0.52, BVDT=0.79 — all under the
FAIL threshold. TYPECHECK.md written.

## Blockers
None. Proceeding to Phase 2 build.
