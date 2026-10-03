# REBUILD-LOG — nbb-writer-reviewer-pattern (2026-08-31)

Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of `beat_sheet.json` before this pass).

## Locked (verbatim)

- All 6 body-beat narration blocks (B00–B05) — the script per rebuild contract.
- Beat order, act labels, metadata identity (title, slug, topic, register, channel).
- Kokoro `am_onyx` on every beat (no ElevenLabs-era fields present pre-rebuild).

## Rebuilt

- **Narration edits (non-datable — cross-reel contamination + verdict/your-turn fixes):**
  - `NBB02.narration_text`: `"Take this prompt, run it on your own — pick any cancer type or clinical scenario you know about and ask how this mechanism applies there."` → real "run a reviewer subagent on your last shipped code" exercise. Reason: template-boilerplate leak from a cancer-biology reel that made no sense for a writer/reviewer subagent reel.
  - `NBB01.narration_text`: `"Let's recap with Claude. Here's what the body just demonstrated."` lead-in → `"The verdict:"` — verdict_audit classifies the "here's what the evidence shows"-style lead-in as an empty announcement of a finding.
  - `BVDT.narration_text`: `""` → real recap sentence stating the finding.
  - `BHTF.narration_text`: `""` → real your-turn exercise.

- **Bookend / composer machinery:**
  - `NBB00.props.greeting`: `"Your turn."` → `"Aloha, Liam"` (world-hello; sibling reels used Namaste, Salaam — Aloha is distinct).
  - `B00.shot.remotion.props.greeting`: `"Liam"` (placeholder) → `"Same session, same context."` (4-word spark line drawn from the beat's own narration). Also folded top-level `remotion` block down into `shot.remotion.props` and dropped the duplicate (compile.py reads `shot.remotion` only).
  - `B00.shot.remotion.props.segment`: `"Writer/Reviewer: Same Model, Clean Context"` (was already), `command` kept as `"review the grading tool for correctness"`.
  - `B05.shot.remotion`: promoted from top-level `remotion` sibling into `shot.remotion` so remotion_scenes.py can render it. Cleaned the "[Open a new Claude Code session]" bracket prefix in the command narration; the prompt itself is intact.
  - `BOUT`: marked `silent: true` + `silence_s: 6.0` (was untagged — NBB03 already carries the audible outro line; BOUT is the second title-restate card with no voice). Dropped placeholder `build.status: SLATE` on every bookend so compile fills them from the freshly-rendered media.
  - `NBB02.props.command`: cancer-biology template → real "code reviewer with no context" prompt matching the narration and the B05/BHTF prompts.

- **Verdict lines authored:**
  - `NBB01.props.artifactLines` — trio containing a `"…"` mid-sentence truncation → three clean lines drawn from body content:
    1. "Same-context review inherits every assumption the writer made."
    2. "Same model, same weights — an empty starting context is the whole tool."
    3. "The reviewer subagent reads the code cold and flags what the writer normalized."
  - `BVDT.props.artifactLines` — placeholder trio `"Key finding one/two/three"` → same three authored lines.
  - Added `B04.shot.remotion` as `ClaudeVerdictArtifact` with its own three lines from B04's narration (was pattern-less → would have slated).

- **FormBCard fix:**
  - `B01.shot.remotion.props.items` — `"Key point one/two/three"` with empty `sub` → three authored items with real labels and full-sentence subs drawn from the narration (Inherits every decision / Normalizes the obvious / Validates what it wrote). Also rewrote the placeholder title.

- **Chart text (scenes_std.py):**
  - Old scenes fed `narration[:60]` fragments to Manim as chart text — the exact defect from enterprise-search B02/B09 (fixed 2026-08-26). Rewritten with short category labels and one full-sentence caption per scene:
    - `Scene_B02_NbbWriterReviewer`: `Main session → Subagent (own context) → Summary` pipeline with a caption sentence about intermediate work.
    - `Scene_B03_NbbWriterReviewer`: three-panel `Implicit assumptions / Untested edge cases / Off-by-one errors` (terracotta on the third), single caption sentence.
    - Dropped stale `Scene_B01_NbbWriterReviewer` — B01 is a Remotion FormBCard, no Manim needed.

- **Locked / source-clip cleanup:**
  - Removed `locked: true`, `source_clip`, `source_audio`, and pre-existing `actual_duration_s` from every body beat. The referenced source paths (`../writer-reviewer-pattern/clips/*.mp4` and `../writer-reviewer-pattern/mp3/beat-*.mp3`) do not exist — this reel has to render + generate its own audio locally. `audio_file` reset to `mp3/beat-<id>.mp3` on every beat.

## Datable claims

No datable-claim edits required — no specific model versions, prices, or "as of" dates named in the narration.

## Dropped

- Top-level `remotion` block on B00 (dead — compile.py reads `shot.remotion` only).
- Top-level `remotion` block on B05 (promoted into `shot.remotion` before deletion).
- Placeholder `build.status: SLATE` records on B00, B01, BVDT, BHTF, BOUT.
- Stale `actual_duration_s` values carried over from the source reel (Kokoro will re-measure).
- Stale `../writer-reviewer-pattern/…` source references (source folder has no clips or mp3s).

## Not modified

- Body B00–B05 narration blocks (all 6 locked).
- Duplicate bookend structure (NBB00–03 + BVDT/BHTF/BOUT). Corpus-wide across nbb-* reels — kept per rebuild rule 5 (non-claude channels keep their own skins; don't restructure).
- Metadata identity: slug, title, topic, variant, palette, register.
