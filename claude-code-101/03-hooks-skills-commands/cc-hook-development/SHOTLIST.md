# SHOTLIST — cc-hook-development

14 beats, 277.58 s master, 3840×2160 @ 24 fps. Order below is master timeline order. Every source file cited is under this reel's folder.

| # | beat | act | surface | source of every visible string | media |
|---|---|---|---|---|---|
| 1 | B00 | COLD OPEN — BARE | `CCSession` "scratch — bare", accept-edits | `evidence/ask.txt`; `evidence/run-bare.jsonl` (Bash `ls`, Read, Edit, Claude's "Added the bullet…") | `media/B00.mp4` |
| 2 | BIDEA | THE IDEA | `BrutalistHesitantWriter`, CC palette | authored copy; one word `magic → wired` — the misconception this film fixes | `media/BIDEA.mp4` |
| 3 | BDEFS | DEFINITIONS | `CCDefinitions`, 5 terms | authored copy; each term used by the film | `media/BDEFS.mp4` |
| 4 | B01 | DRAFT — SCRIPT | `CCSession` "scratch — draft", accept-edits | `evidence/run-draft.jsonl`: two-line prompt, `pwd && ls -la`, `ls -la .claude/ hooks/`, `Write hooks/log-write.sh`, `chmod +x`; script body `evidence/log-write.sh.CLAUDE_DRAFT` | `media/B01.mp4` |
| 5 | B02 | DRAFT — THE WALL | `CCSession` "scratch — draft" (cont.) | `evidence/run-draft.jsonl`: four blocked attempts on `.claude/settings.local.json` (Write × 2, `cat > … <<'EOF'`, `printf`); Claude's "I've stopped retrying. Paste this in." verbatim | `media/B02.mp4` |
| 6 | B03 | THE HUMAN WIRING | `CCPlainShell` "zsh — scratch/.claude" | `evidence/settings.local.json.MINE` (15 lines, cat'd verbatim: `hooks` wrapper, `PostToolUse`, matcher `"Write\|Edit\|MultiEdit"`, command `"bash hooks/log-write.sh"`) | `media/B03.mp4` |
| 7 | B04 | SMOKE — VERIFY | `CCSession` "scratch — smoke test", default mode | Liam's three `echo … \| bash log-write.sh` runs from `evidence/writes.log.smoke`; three `exit=0`; the three log lines (Write /tmp/foo.md, Edit target.md, Bash empty-column) | `media/B04.mp4` |
| 8 | B05 | FIRES — REAL RUN | `CCSession` "scratch — fires", accept-edits | `evidence/run-fires.jsonl`: prompt, Read target.md, Edit target.md, Claude's "Added the bullet at end of Notes.", `target.md:10`; `evidence/writes.log.fires` single line | `media/B05.mp4` |
| 9 | B06 | HONEST LIMIT | `CCSession` "scratch — two events", default | five authored text blocks reprising the API doc: PostToolUse fires AFTER; PreToolUse fires BEFORE; exit 0 → nothing; exit 2 → reject; same script shape, different event | `media/B06.mp4` |
| 10 | B07 | CONDUCT — Boondoggle Score | `CCBoondoggleScore` | 7 steps mapped to the three runs; dangerous middle = step 3 (harness wall); PF/PA/EI capacities from what Liam actually did | `media/B07.mp4` |
| 11 | B08 | HUMAN — Ledger | `CCHumanLedger` | 4 MUST/SHOULD rows for the human; 4 CAN/SHOULD rows for Claude; closing line "The two lines only you can sign." | `media/B08.mp4` |
| 12 | BVDT | VERDICT | `ClaudeVerdictArtifact`, 6 lines | recap of the three runs; last line FALSIFIABLE | `media/BVDT.mp4` |
| 13 | BHTF | YOUR TURN | `ClaudeComposerAsk`, "Your turn." | the paste-into-Claude-Code prompt, same shape as B01 ask, plus "Do not run the hook." | `media/BHTF.mp4` |
| 14 | BOUT | OUTRO | `ClaudeTitleOutro`, `@NikBearBrown`, subline `""` | title verbatim; "Liam, in for Bear." | `media/BOUT.mp4` |

Two consecutive off-terminal body beats: none (BIDEA + BDEFS are the two required openers; every subsequent body beat except B03 lives in `CCSession`, and B03 names its `leaves_terminal_because`). Every `CCSession` text block ≤ 44 characters. Every `CCHumanLedger` row ≤ 30. Every `CCBoondoggleScore` step text/handoff ≤ 44. Verdict lines = 6.

Voice on every beat: Kokoro `am_onyx` (Liam). All narration is first person, present tense, Teardown register. No datable numbers spoken (no model version, no price).
