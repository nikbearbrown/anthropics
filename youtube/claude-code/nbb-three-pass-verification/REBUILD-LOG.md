# REBUILD-LOG — nbb-three-pass-verification

Filmloop 2026-08-31. Byte-exact snapshot at `beat_sheet.pre-rebuild.json` was
taken first (per rebuild contract).

## Envelope normalization

- Dropped `source_clip` / `source_audio` on every beat — the parent
  `../three-pass-verification/{clips,mp3}/` never existed on disk. Pointers to
  non-existent files silently fail the pipeline; better to route the beat
  through fresh render+audio.
- Dropped stale `actual_duration_s` fields — every audio will be re-measured by
  Kokoro on this run, and a wrong clock stamped in the sheet would mislead the
  compiler.
- No ElevenLabs-era fields present (`voice_id`, `voice_env`, `clock` prose).

## Structural fix — stripped duplicate empty bookend stubs

The pre-rebuild sheet carried TWO overlapping bookend sets: `NBB00..NBB03`
(filled Liam/Claude bookends) followed by `BVDT / BHTF / BOUT` (empty
placeholder stubs from a later scaffolder pass — `narration_text: ""`,
`build.status: SLATE`, verdict lines `Key finding one/two/three`).

Per PHASE 1 check 2 amendment ("BVDT may be legitimately ABSENT if a previous
pass stripped a placeholder verdict — absent is legal, present-and-empty is
not") and per `verdict_audit.py` boilerplate rule, the empty duplicates were
stripped. `NBB01 / NBB02 / NBB03` remain and match the canonical
`ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro` patterns.

## Narration edits (authorized under Phase 1 checks — logged old → new)

**NBB00 cold-open greeting (check 3 — spark line):** props.greeting was
`"Your turn."` — that spark line belongs on BHTF, not on a cold open. Cold-open
greeting rule: `<world-language hello>, Liam`. Also swapped model chrome:

- old: `"greeting": "Your turn."`  →  new: `"greeting": "Bonjour, Liam"`
- old: `"modelLabel": "Fable 5"`   →  new: `"modelLabel": "Claude Sonnet 4.5"`

Source: `skills/make/ai-explainer/SKILL.md` §"The greeting"; the "Fable 5"
label was a fabricated model name (rebuild rule: props that render on screen as
factual chrome may be updated to current real values).

**NBB02 Your-Turn (check 5c — placeholder your-turn):** the pre-rebuild
narration and command were about "any cancer type or clinical scenario" — a
template contamination from an unrelated reel (this reel is about SDD
verification, not oncology). Rewritten from the video's own content:

- old narration: "Take this prompt, run it on your own — pick any cancer type
  or clinical scenario you know about and ask how this mechanism applies
  there."
- new narration: "Your turn. Run all three passes on your own build. List your
  Pass 2 edge cases, read your SDD user needs aloud, and for any failing need
  decide whether to build it or amend the spec — and say why."
- old command: "Explain how [Run the Three-Pass Verification Protocol with
  Claude Code] applies to a specific cancer type or clinical case you're
  studying. What proteins are involved…"
- new command: a real three-pass prompt scaffold naming Pass 1/2/3 checks and
  the build-or-amend decision (see beat_sheet.json).

Source: LENS-NOTES.md and the reel's own body (B02–B06 walk exactly this
protocol on an app-tracker build).

**B01 FormBCard items (check 5 — card text placeholders):** labels/subs were
"Key point one/two/three" with empty subs. Rewritten from B01's own narration:

- item 1: `Tests / verify code against tests / check`
- item 2: `The gap / built vs. needed / list-checks`
- item 3: `Pass 3 / the pass tests can't run / user`

**All other narration LOCKED.** B00, B01–B08 body prose, NBB01 verdict
narration and artifactLines, NBB03 outro title — all carried over verbatim.

## scenes_std.py rewritten (check 5b — chart-text defects)

The prior file used `Text(narration[:20])` and `Text(narration[:30])` for
labels — the exact defect check 5b calls out (colliding, mid-word-truncated
labels shipped in enterprise-search B02/B09). Replaced with:

- B01 — three-stack card (act, three narration lines with proper wrap widths).
- B04 — PASS/FAIL panel with three rows (Pass 1 / Pass 2 / Pass 3), badges,
  terracotta on the two failing rows.
- B06 — outcome card with four wrapped lines.
- B07 — protocol summary rows (Pass 1/2/3 × kind × who does it).
- B08 — Next-Steps bridge card (was a meaningless two-bar chart with one blank
  label; NEXT STEPS beats have no quantities to chart — a title bridge is the
  honest form).

All widths pass through `_fit()` to keep lines inside the 11.0-unit safe box.

## audio_file paths

All beats rewritten from `../three-pass-verification/mp3/beat-*.mp3` (dead) to
local `mp3/beat-*.mp3` — Kokoro will populate them on this run.
