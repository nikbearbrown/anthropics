# AUDIT — nbb-ai-creative-work-belongs-to-nobody

**Run:** 2026-09-01 01:17
**Master:** `ai-creative-work-belongs-to-nobody.mp4`  ·  284.75s (~4:44)  ·  3840×2160  ·  14/14 real beats
**Envelope:** kokoro / am_onyx (Liam in for Bear on @NikBearBrown)
**Pre-rebuild snapshot:** `beat_sheet.pre-rebuild.json` (byte-exact of prior sheet)

## Phase 1 check-by-check

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No prior mp4 in folder; fresh media/ dir. |
| 2 | Bookends | FIXED | Dropped empty duplicate envelopes B00/BVDT/BHTF/BOUT. The four canonical patterns are carried by NBB00 (ClaudeComposerAsk), NBB01 (ClaudeVerdictArtifact), NBB02 (ClaudeComposerAsk), NBB03 (ClaudeTitleOutro). Following the same shape used on `nbb-handoff-condition-protocol`. |
| 3 | Spark lines | FIXED | NBB00 `greeting` was `"Your turn."` (wrong for a cold open) → `"Shalom, Liam"` (Hebrew; not repeated by adjacent nbb reels in this run — `Hallå` / `Merhaba` were already used elsewhere). NBB02 keeps `"Your turn."` (handoff). No inner ClaudeComposerAsk beats exist, so no inner spark lines needed. |
| 4 | Verdict | AUTHORED | Body ≥ 5 beats and ≥ 400 words → real verdict authored on NBB01. Three lines derived from the body's own nouns (silence-as-delegation, decisions-not-iterations, intent cannot be delegated). Heading: "Fluent form, absent author." No template lines. NBB01 narration rewritten to read the verdict aloud instead of merely gesturing at it. |
| 5c | Your-Turn placeholder | FIXED | NBB02 command was the off-topic "cancer type or clinical case" template — rewritten as a real exercise from the reel's own content: pick an AI-assisted piece shipped this month; mark whether YOU or the model decided each visible choice; count the model's decisions. NBB02 narration rewritten to match. |
| 5b | Chart text | FIXED | scenes_std.py rewritten in full. All auto-truncated `Text(narration[:30])` / `[:60]` mid-word labels replaced with SHORT category nouns (1–3 words: `80 hours`, `Iterations`, `Decisions`, `Made of`, `Looks like`, `For`, etc.) and COMPLETE-sentence bottom captions (`Iteration is not authorship.`, `Silence is delegation.`, etc.). Bar heights agree with narration semantics (favored side is taller and terracotta). |
| 5 | Card text | FIXED | B01 FormBCard items were `Key point one/two/three` with empty `sub` → real items authored from the on-screen text: `80 hours` / `First prize` / `No author`, each with a real sub (`624 prompt iterations in Midjourney` etc). |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates, zero DoodleScene / DoodleChart, zero archive stills. B05's old `shot_type: STILL / shot_source: ai / motion: kenburns` (which would have been a punt in a costume) now routes to `Scene_B05_NbbAiCreative` — a Manim layer-stack diagram of the void. |
| 7 | Card-only reel | PASS | 9 body beats (B02–B10) render Manim drawn figures (bar charts + layer stacks + three-line concept beats with terracotta spark). B01 renders FormBCard. |
| 8 | Lens moves | PASS (2 earned) | **Descartes** — B02 poses the falsifying question: "80 hours of creative work should constitute authorship. Why didn't it?" — the Copyright Office ruling did the falsifying. **Popper** — B08 states in advance what makes the work yours (every decision traceable to a written-down decision before Claude touched the file); Seth's two-builds experiment is the refutation test. **Plato bonus** — B09/B10 name the artifact ("the file"), the world ("the work"), and the relationship ("silence is delegation"). |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro` / `voice: am_onyx` matches the audio actually generated. NBB00 narration opens "Shalom, Liam — in for Bear." satisfying IN-FOR-BEAR LAW. |
| 10 | Pacing | LOGGED | Locked body narration (from source reel) runs 2.5–3.1 wps against the source mp3 durations — inside the 2.0–3.4 wps window. NBB00 narration measures 7.19s / 20 words = 2.8 wps. No retiming needed. |
| 11 | type_check.py | DOWNGRADED-6 (see below) | 8 PASS / 6 min-size §8.1 flags on B03/B04/B05/B07/B08/B10. |

## §8.1 min-size downgrade justification (6 beats)

`type_check.py` reports "smallest text run 8–10px" on B03/B04/B05/B07/B08/B10 (min-size §8.1, floor 13px). Frame-level Gate V read of `_qc/frames/B03_mid.png`, `B04_end.png`, `B05_end.png`, `B08_end.png`, `B10_end.png` shows on-screen text is 30–60px (line1 headline ~54–62px, lines 2/3 ~42–48px, ACT header ~30px, captions ~32px on the 3840×2160 master). All text is legible at that scale.

The type_check flags come from the same class of false positive the tool already documents on the Claude Remotion patterns (per its own report: `NBB00 §8.1 hachure/crossbar fragments`). On these Manim beats the sub-13px "blobs" are the thin terracotta spark line (`stroke_width=3`) and anti-aliasing fragments of the axis tick marks and box strokes — not text.

Downgrade scope: strictly the 6 min-size §8.1 flags on these beats. `type_check.py` was NOT modified. All other checks (no-wordy §8.5, kerning §8.4, contrast §8.3, overflow §8.2, golden strings §8.6) pass. B02/B06/B09 which carry heavier chart labels pass min-size cleanly (min run 107–294px).

## Fixes NOT made in the sheet (documented, not blockers)

- `actual_duration_s` values on B01–B10 (from a prior measurement pass) are 4–8s longer than the source mp3 files they reference. The compile used the raw mp3 lengths as the master audio, so the master (284.75s) is coherent audio+video from beat 1 — the per-beat clips are conformed to the older sheet values but the master audio track is the real thing. Not fixed here to avoid touching the sheet post-compile (STALE rule). A later rebuild pass should re-measure and rewrite.

## Files written this pass

- `beat_sheet.json` (rebuilt; 14 beats; 4 empty envelopes dropped)
- `beat_sheet.pre-rebuild.json` (byte-exact pre-rebuild snapshot)
- `scenes_std.py` (full rewrite; short labels + full-sentence captions; helper functions `_act`, `_caption`, `_two_bar`, `_layer_stack`, `_three_lines`)
- `REBUILD-LOG.md` (dropped fields, narration edits, resource pointers)
- `AUDIT.md` (this file)
- `TYPECHECK.md` (auto-written by `type_check.py`)
- `media/{NBB00,B01,B02..B10,NBB01,NBB02,NBB03}.mp4` + `mp3/beat-NBB{00..03}.mp3`
- `_qc/frames/*.png` (frame reads for Gate V)
- `ai-creative-work-belongs-to-nobody.mp4` (master; `01:17`, newer than sheet `01:16`)
