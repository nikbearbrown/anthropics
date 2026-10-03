# SHOTLIST — cc-buildlog-assessment

TERMINAL-FIRST: every body beat is a Claude Code surface (`CCSession` or `CCPlainShell`); the one non-terminal beat, BIDEA, names its reason. `leaves_terminal_because` is set on BIDEA (the writer typing what the film is about — not in any session), BDEFS (a chat-window definitions card), and B02 (dated file content read outside a session).

| Beat | Surface | Motion | Blocks / props |
|---|---|---|---|
| B00 | `CCSession` (default mode, mascot off) | type | `ls`, `wc -l` on signup.htmls, `diff -q`, `wc -l` on CLAUDE.mds — 11 blocks |
| BIDEA | `BrutalistHesitantWriter` | type | 4 lines, one-word correction: "code" → "file", CC palette |
| BDEFS | `CCDefinitions` | drawon | 5 terms, 1 line each, ≤70 chars |
| B01 | `CCSession` (accept-edits, mascot off) | type | prompt (ask verbatim) + 10 text blocks — refusal, dated citation, 3 alternatives |
| B02 | `CCPlainShell` | type | `grep '^### '` + `sed` block — the three dated headers and the Aug-14 body |
| B03 | `CCSession` (accept-edits, mascot off) | type | prompt + Read tool + 6 text blocks + AskUserQuestion tool + 3 option texts |
| B04 | `CCSession` (default, mascot off) | type | 4 bang commands: `diff`, `grep -c` ×3 — 11 blocks |
| B05 | `CCSession` (accept-edits, mascot off) | drawon | 2 Reads + 12 text blocks — the grader's per-row scores and totals |
| B06 | `CCBoondoggleScore` | drawon | 6 steps; dangerousMiddle=2; distribution shown |
| B07 | `CCHumanLedger` | drawon | 4 AI rows + 4 human rows + closing |
| BVDT | `ClaudeVerdictArtifact` | hold | 4 lines; last line FALSIFIABLE |
| BHTF | `ClaudeComposerAsk` | type | greeting "Your turn.", full command; topic "YOUR TURN · CLAUDE CODE 101" |
| BOUT | `ClaudeTitleOutro` | hold | exact title, `@NikBearBrown`, no subline |

Kit gotchas respected: every CCSession text block ≤44 chars; every ledger row ≤30; every score step ≤44; verdict is exactly 4 lines; every CCSession full stack sets `mascot: "off"`; no status blocks use `↓ …` — tokens strings are absent.
