# REBUILD-LOG.md — claude-code-action-natural-trigger-review-counting-check

## Locked (carried verbatim from pre-rebuild)
- Metadata: slug, title, topic, purpose, category, playlist, channel, folderLabel, source pointer, register.
- Body narration B00, B01, B02, B03, B04, B05 — unchanged.
- Beat order for B00–B05.

## Rebuilt
- **Envelope** — VOICE-LOCK per current doctrine. Kept metadata `voice`, `voice_kokoro`, `engine`, `clock` (Kokoro-tagged, not ElevenLabs). No dead fields to drop.
- **Metadata greeting** — `Konnichiwa, Liam` → `Salaam, Liam`. Rotated because two adjacent unbuilt claude-code reels also carry `Konnichiwa` (the seed used one language for the whole cohort). Kept a real world-language hello per SPARK-LINE LAW.
- **`shot.form`** — added for every beat.
- **B00 shot** — greeting `Liam` → `Salaam, Liam` (was placeholder — lonely-asterisk defect). Segment, topic, command tightened; kept the original ask intent.
- **B01–B05 shots** — authored per nopunt catalog (Structure & relationship → static taxonomy → FormB / FormA). Labels + subs paraphrased from the beat's own locked narration; no narration edited.
- **BVDT** — was three placeholder `artifactLines` (`Key finding one/two/three`) with empty narration. Authored four content-bearing lines from B03/B04 nouns (`pull_request_review` → merge ref, `required_approvals: 0` bypass, safe triggers = `pull_request_target`/`issue_comment`, indirect counting on next safe event) and wrote a 22 s stated verdict.
- **BHTF** — was the template `Take what you learned from [...]` your-turn (placeholder wearing brackets). Authored a concrete exercise: open one repo you protect; ask the three questions (trigger / ref / could author edit); if yes, move to `pull_request_target` or `issue_comment`. Composer output shows a passing check.
- **BOUT** — kept title-outro pattern; added `handle` prop; kept mascotSeed.
- **Dropped beats** — `YOURTURN` and `OUTRO` (design-v1 additions) removed. They duplicate BHTF and BOUT respectively; shipped-neighbor pattern (`claude-liam-slopsquatting-hallucinated-package`, all built claude-liam reels) omits them.

## Datable-claims pass
- None. Reel is about GitHub Actions ref-selection semantics (`pull_request_review` vs `pull_request_target` vs `issue_comment` — stable API contracts as of the source README). No model names, no versions, no prices, no "as of" language.

## Gates
- TYPECHECK: PASS (`--skip-pixels`; pixel checks in Gate V after compile).
- FACTCHECK: sourced from `anthropics/claude-code-action/agent-approval-check/README.md`. Merge-ref vs base-ref semantics confirmed against upstream `agent_approval_check.py` docstring "SECURITY MODEL" and README threat-model section.
