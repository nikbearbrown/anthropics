# BUILD-PROMPT — cc-writer-reviewer-pattern

The reel this folder builds is the second in Claude Code 101's tier 02 (plan / rewind / subagents): **Writer / Reviewer, Same Model, Clean Context**. Its argument is that same-context review is narration and clean-context review is review — same model, same weights, different starting context.

## How the film was made (so it can be re-run)

1. **Seed the scratch project** — `scratch/grades.csv` (five rows, three awkward on purpose: a missing quiz, an all-blank row, and a one-very-low-score high average), `scratch/README.md`, `scratch/ask.txt`.
2. **Writer run** — `claude -p "$(cat ask.txt)" --session-id <writer uuid> --output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" < /dev/null > evidence/run-writer.jsonl`.
3. **Same-context review** — same command, replace `--session-id <writer uuid>` with `--resume <writer uuid>`, and swap the prompt for the review prompt (see `PROMPTS.md`). Output: `evidence/run-review-same.jsonl`.
4. **Clean-context review** — copy `pass_fail.py`, `grades.csv`, `README.md`, `ask.txt` to a new folder (nothing else); a fresh `claude -p` there with a brand-new `--session-id`. Output: `evidence/run-review-clean.jsonl`.
5. **Author the sheet** — `python3 author_sheet.py` (12 beats; asserts every text budget). Do not run again in-place after audio: it wipes the mp3 stamps. If props need editing after audio, regenerate to a temp dir and merge, or edit `beat_sheet.json` directly with `art run` NOT alive.
6. **Audio** — `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel-dir>`. Liam (`am_onyx`) on every beat.
7. **Paperwork** — `SESSION.md`, `FACTCHECK.md`, `CHECKS-REPORT.md`, `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`. `python3 brutalist-art/runtime/qc/factcheck_check.py <reel-dir>` must print `clean`.
8. **Compile** — from `books/`: `./brutalist-art/art run anthropics/claude-code-101/02-plan-rewind-subagents/cc-writer-reviewer-pattern`, then `./brutalist-art/art final <same path>`. On any failure, read `_qc/REPORT.md` and `TYPECHECK.md`, fix at source, clear the failing beat's `shot.remotion.rendered` to `{"out":"","at":""}`, delete `media/<id>.mp4`, run again.
9. **Never publish** — master stays here. TOPOST only via `post` on ask.

## Reference spine (see SKILL.md and CHECKS-REPORT.md for the enforced rules)

`B00 (CCSession, writer run) → BIDEA (BrutalistHesitantWriter, one word: reviewer→writer) → BDEFS (CCDefinitions, 4 terms) → B01 (CCSession --resume, same-context review) → B02 (CCPlainShell, cp + new session-id) → B03 (CCSession, clean-context review) → B04 (CCPlainShell, grep receipts) → B05 (CCBoondoggleScore, dangerous middle = step 3) → B06 (CCHumanLedger) → BVDT → BHTF → BOUT.`

Concept film: `metadata.build` unset; BFLOW/BSHOW skipped. Reason logged in `CHECKS-REPORT.md`.
