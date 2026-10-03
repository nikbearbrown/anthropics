# FACTCHECK — cc-hook-development

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json (`evidence/run-{bare,draft,fires}.jsonl`), the two files on disk (`evidence/log-write.sh.CLAUDE_DRAFT`, `evidence/settings.local.json`), the two log files the reel shows (`evidence/writes.log.smoke`, `evidence/writes.log.fires`), and the target's before/after (`evidence/target.md.{before,final}`). Liam's checks were run in a plain shell against the scratch folder. Claude's sentences are verbatim spans; the block error message is verbatim from the `tool_result` `is_error: true` payloads.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Bare run: ls, Read, Edit, "Added the bullet under `## Notes`."; three turns, ~15 s | PASS | `run-bare.jsonl`: 4 turns, 15.6 s, cost $0.247; last Claude text is verbatim | — |
| 3 | B00 | "no receipt" | PASS | `hooks-log/` did not exist after Run 1; snapshot in SESSION.md; grep of `evidence/` shows no bare-run log | — |
| 4 | BIDEA | Framing lines ("shell command at a moment", "which two lines only you can sign") | PASS | characterisation of the draft-vs-wire asymmetry established in Runs 2 and 3; not a datable claim | — |
| 5 | BDEFS | The five terms and their meanings | PASS | `hook` / `matcher` / `PostToolUse` / `PreToolUse` — behaviour observed in Runs 2/3 and archived hook script; `settings.local.json` — blocked in Run 2, permitted only by hand | — |
| 6 | B01 | The draft ask ("PostToolUse hook that logs every Write, Edit, MultiEdit"); Claude wrote `hooks/log-write.sh` (20 lines) on the first try; "twenty lines" | PASS | `run-draft.jsonl` prompt; `wc -l evidence/log-write.sh.CLAUDE_DRAFT` → 20; script archived verbatim | — |
| 7 | B01 | "Read stdin, extract tool name and file path, append UTC and tool and path" | PASS | `evidence/log-write.sh.CLAUDE_DRAFT` body — literal lines | — |
| 8 | B02 | "Then Claude tries to write the second file … blocked" (4 attempts, one heredoc, one printf fallback) | PASS | `run-draft.jsonl`: four `tool_result` `is_error: true` events on `.claude/settings.local.json`; heredoc rejected as `Contains brace with quote character (expansion obfuscation)`; `printf` fallback blocked with the same permission message | — |
| 9 | B02 | "Claude gave up and printed the JSON in the chat for me to paste" | PASS | `run-draft.jsonl` final assistant text (verbatim in SESSION.md): "The write to `.claude/settings.local.json` keeps getting blocked …" | — |
| 10 | B03 | `settings.local.json`, 15 lines, matcher `Write\|Edit\|MultiEdit`, command `bash hooks/log-write.sh` | PASS | `wc -l evidence/settings.local.json` → 15; JSON content verbatim | — |
| 11 | B03 | "Claude Code won't let anyone else sign it" | PASS | Run 2 (draft) — blocked 4× at the same target path; the neighbour reel `cc-hook-enforcement` reports the same wall for `settings.local.json` writes | — |
| 12 | B04 | Three payloads piped to the script; three `exit 0`; log has three lines (Write, Edit, Bash with empty third column) | PASS | `evidence/writes.log.smoke` — three lines, exactly as shown; matches SESSION.md's "Direct hook smoke test" block | — |
| 13 | B05 | Fires run: Read, Edit, "Added the bullet at the end of the Notes list"; three turns; one line in `hooks-log/writes.log` — timestamp, tool, path | PASS | `run-fires.jsonl` (3 turns, 14.7 s, $0.221; assistant text `Added the bullet at the end of the Notes list in \`target.md:10\``); `evidence/writes.log.fires` — one line | — |
| 14 | B06 | "PostToolUse fires after the write" and "PreToolUse and exit two" as the wall event | PASS | Claude Code's documented hook contract; observed in this reel (Post) and the neighbour reel `cc-hook-enforcement` (Pre + exit 2) | — |
| 15 | B07 | 7 conducting steps; dangerous middle at step 3; capacity tally PF 1, PA 2, EI 1, TO 0 | PASS | maps to SESSION.md (Runs 1–3 + smoke); step 3 is the harness block on `.claude/settings.local.json`; step-7 EI is B06's honest limit | — |
| 16 | B08 | Ledger rows: AI CAN "draft the hook script" / "extract JSON from stdin" (Run 2); AI SHOULD "refuse to wire itself in" — it did (Run 2); AI SHOULD "test its own script" — it did not (the ask said "Do NOT run or test") | PASS | `run-draft.jsonl`; MUST rows are the reel's argument, not a datable claim | — |
| 17 | BVDT | Verdict lines quoting counts (20, 15, 4×, one line) | PASS | rows 6, 10, 8, 13 above | — |
| 18 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 19 | all | Model / version / date strings (Claude Code 2.1.150, `Opus 5`) | EXEMPT | version numbers in SESSION.md are for the record; not shown or spoken in the reel; `Opus 5` is a UI prop, not a claim | — |
| 20 | metadata | Per-run costs ($0.247 / $0.509 / $0.221) | EXEMPT | recorded in SESSION.md, not shown or spoken | — |
