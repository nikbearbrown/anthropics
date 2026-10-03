# SOURCES — cc-writer-reviewer-pattern

**Primary source (REAL-SESSION LAW).** The three real Claude Code sessions run on 2026-09-09, saved as stream-json in this reel:

- `evidence/run-writer.jsonl` — writer session `4837f38e-…`
- `evidence/run-review-same.jsonl` — same-context review via `--resume 4837f38e-…`
- `evidence/run-review-clean.jsonl` — clean-context review, fresh `--session-id 72948a3b-…`, in `/private/tmp/clean-review/` with copies of the four files only

Every `CCSession` block in the sheet traces to one of these three files; every `CCPlainShell` line is a real shell action either around the sessions (setup, verify) or an actual grep on the transcripts.

**Concept scaffolding** (framing only, no factual claim borrowed):

- `books/anthropics/claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-writer-reviewer-pattern/beat_sheet.json` — the concept card this film is derived from. Title's claim ("Writer/Reviewer: Same Model, Clean Context") and Your-Turn intent kept; its "off-by-one in the rubric parser that would misgrade any submission over twenty items" was never checked against a session and is NOT used.

**Closing-block doctrine** (CONDUCT and HUMAN beats):

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score idea and the five capacities (PF, TO, PA, IJ, EI).
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the human ledger (MUST / SHOULD / CAN / SHOULD) and Tier 4 framing (the machine cannot reliably report its own uncertainty).

**Kit and skill**:

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — LIAM LAW, TERMINAL-FIRST, REAL-SESSION, spine, kit gotchas.
- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` — the CC kit contract (verbatim product strings only).

**Not used** (deliberate exclusions):

- Any auto-transcription, generation-service claim, or benchmark number.
- Any name other than Liam and Bear in narration or on-screen prop text.
- Any version number, model name, or price (recorded in the JSONL metadata only, never shown or spoken).
