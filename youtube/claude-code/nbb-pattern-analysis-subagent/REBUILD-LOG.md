# REBUILD-LOG — nbb-pattern-analysis-subagent (2026-08-31)

Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of `beat_sheet.json` before this pass).

## Locked (verbatim)

- All 10 body-beat narration blocks (B00–B09) — the script and shot ideas per the rebuild contract.
- Beat order, act labels, metadata identity (title, slug, topic, register, channel).
- Kokoro `am_onyx` on all 17 beats.

## Rebuilt

- **Narration edits (non-datable — cross-reel contamination fixes):**
  - `NBB02.narration_text`: `"Take this prompt, run it on your own — pick any cancer type or clinical scenario you know about and ask how this mechanism applies there."` → `"Your turn. Pick one task in your workflow that fills your session window with reads — grading, PR triage, log review — and write a subagent for it. Frontmatter, three structured fields, read-only tools. Then run it on three real inputs and check the summary."`. Reason: not a datable claim — a template-boilerplate leak from a cancer-biology reel that made no sense for a Claude-Code-for-teachers reel.
  - `NBB01.narration_text`: `"Let's recap with Claude. Here's what the body just demonstrated."` → real verdict recap sentence stating the finding. Reason: `verdict_audit` classifies "Here is what the evidence shows"-style narration as empty (announces a finding without stating one).
- **Bookend / composer machinery:**
  - `NBB00.props.greeting`: `"Your turn."` → `"Namaste, Liam"` (world-hello, adjacent Hola/Kia ora avoided).
  - `B00.props.greeting`: `"Liam"` → `"Policy fills the session."` (four-word spark from that beat's narration).
  - `NBB00.props.segment` + `NBB02.props.segment`: `"Deploy a Pattern-Analysis Subagent for a"` → `"Deploy a Pattern-Analysis Subagent for a Grading…"` (fix §8.9 truncation-without-ellipsis).
  - `NBB02.props.command`: cancer-biology template → real "write a Claude Code subagent" prompt.
  - `BHTF.props.command`: template `"Take what you learned from [Title] and apply..."` → same real subagent prompt.
  - `NBB03.props.subline`: `"cancer biology, one mechanism at a time"` → `"Claude Code for teachers, one pattern at a time"`.
- **Verdict:** `NBB01` + `BVDT` `artifactLines` — placeholder trios (`"Key mechanism established."` / `"Key finding one|two|three"`) → three lines drawn from body content.
- **FormBCard:** `B01.props.items` — `"Key point one/two/three"` with empty `sub` → 3 authored items (Delegate context / Return a summary / Stay isolated).
- **Chart text:** `scenes_std.py` — B04/B06/B07/B08 previously fed narration fragments (mid-word truncated) as figure text. Rewrote every scene with short category nouns and one full-sentence caption where present.
- **Envelope:** VOICE-LOCK already normalized (kokoro / am_onyx everywhere; no dead ElevenLabs fields present in the pre-rebuild sheet).
- **Audio:** Kokoro fresh, 12 mp3s written, `actual_duration_s` measured per beat.
- **Renders:** 13 Remotion patterns + 4 Manim scenes → 17/17 slots filled.

## Datable claims

No datable-claim edits required — the narration named no specific model versions, prices, or "as of" dates.

## Dropped

- No dead fields to drop (sheet had already been through a VOICE-LOCK pass; no `voice_id`, `voice_env`, or ElevenLabs `clock` prose to remove).

## Not modified

- Body B00–B09 narration blocks (all 10 locked).
- Duplicate bookend structure (NBB00–03 + BVDT/BHTF/BOUT). This is corpus-wide across nbb-* reels — kept as-is per rebuild rule 5 (non-claude channels keep their own skins; don't restructure).
