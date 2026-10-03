# BUILD-PROMPT — cc-agentic-loop

The prompt this session ran on. Kept for provenance so a later session can
resume the same task with the same brief.

## The concept, in one sentence

Same one-sentence ask, two `--permission-mode` values; the loop's shape changes
with the flag. `acceptEdits` closes the loop autonomously (7 tools, 2 files, one
turn, no pause). `plan` stops the loop at Gather (3 Reads, 1 plan file, 0 writes
in the repo, ExitPlanMode waits for a human's "yes"). Same design, both surfaces.

## The task

Author one `cc-explainer` reel that shows the mechanism from a real session —
never from imagination. The reel folder is
`anthropics/claude-code-101/00-what-it-is/cc-agentic-loop`; the source concept is
`anthropics/claude-code-101/00-what-it-is/claude-code--claude-liam-vox-agentic-loop/beat_sheet.json`
(concept only — do not reuse its beats or statistics).

## The film

- **Skill:** `cc-explainer` (Liam, in for Bear · Kokoro `am_onyx` · Teardown register · CC palette · 16:9 · 30 fps).
- **Spine (12 beats):** B00 COLD-OPEN loop / BIDEA / BDEFS / B01 loop-VERIFY / B02 correction (reset + one-flag change) / B03 plan-mode SAME-ASK / B04 plan-VERIFY / B05 CONDUCT (Boondoggle Score) / B06 HUMAN (Ledger) / BVDT / BHTF / BOUT.
- **Concept film** — BFLOW/BSHOW skipped (nothing built).
- **Every block traces to `SESSION.md`.** Every CCSession block is a real prompt / tool / text span from `evidence/run-{loop,plan}.jsonl`. Every CCPlainShell line is a real command executed against `evidence/` or `scratch/`.
- **Falsifiability:** BVDT's last line names the observation that would refute the film.

## Rules I followed

1. Never publish — the master stays here.
2. Never spend money beyond the two `claude -p` calls (Kokoro is free/local; Higgsfield and paid voice not used).
3. Never edit the skill, the kit components, `Root.tsx`, or another reel.
4. Never name Bear's unpublished books or courses in narration.
5. Never re-run `author_sheet.py` in place after audio — the audio stamps are the clock.
