# SOURCES — cc-plan-mode-interruption

## Primary — the real session

- `SESSION.md` — the reconstructed transcript.
- `evidence/run-a-accept.jsonl` — Run A stream-json (acceptEdits).
- `evidence/run-b-plan.jsonl` — Run B stream-json (plan).
- `evidence/run-c-plan-fixed.jsonl` — Run C stream-json (plan, resumed).
- `evidence/plan-b.md` — the plan Claude wrote in Run B (extracted from the `ExitPlanMode` input).
- `evidence/plan-c.md` — the revised plan from Run C.
- `evidence/run-a-diff.txt`, `evidence/run-a-full.diff`, `evidence/run-a-deleted.txt` — receipts of what Run A changed on disk.
- `evidence/index.baseline.html`, `schedule.baseline.html`, `README.baseline.md`, `notes.baseline.md`, `ask.txt` — the site files as they stood before the runs.
- `evidence/index.after-a.html`, `README.after-a.md` — the two files that Run A rewrote before `schedule.html` was deleted.
- `evidence/uuid-a.txt`, `evidence/uuid-b.txt` — session UUIDs used with `--session-id` / `--resume`.

## Doctrine

- `books/info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score (CONDUCT); "dangerous middle" framing.
- `books/info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger (HUMAN); MUST/SHOULD × human/AI.

## Framing borrowed from the concept card

- `books/anthropics/claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-plan-mode-interruption/beat_sheet.json` — its title, its subject (Shift+Tab twice as the plan-mode trigger), and its Your-Turn intent. Its card-body claims are replaced here by the three real headless runs.
