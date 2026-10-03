# SHOTLIST — cc-pattern-analysis-subagent

| # | Beat | Surface | What is on screen | Duration (est → measured) |
|---|---|---|---|---|
| 1 | B00 | CCSession — `grading — inline`, `accept-edits` | the ask types; Read rubric; Read 5 submissions; Write feedback_focus.md | 28.1 → 21.1 s |
| 2 | BIDEA | BrutalistHesitantWriter (CC palette) | 4 lines type, `prompt` corrects to `subagent` | 28.5 → 21.9 s |
| 3 | BDEFS | CCDefinitions | 4 terms — subagent · YAML frontmatter · tool whitelist · main context | 31.2 → 26.0 s |
| 4 | B01 | CCSession — `grading — inline`, default mode | `!wc -l feedback_focus.md` → 5; `!grep -c '^Read' history.txt` → 8; `!jq …cache_creation…` → 35572 | 21.6 → 18.7 s |
| 5 | B02 | CCPlainShell — `zsh — ~/grading` | `$ cat .claude/agents/pattern-analyzer.md` — YAML + prompt; `$ wc -l` → 39 | 27.8 → 26.1 s |
| 6 | B03 | CCSession — `grading — subagent`, `accept-edits` | the ask types; Task pattern-analyzer; the three findings land + "I do not have Write access"; Write feedback_focus.md | 30.2 → 26.5 s |
| 7 | B04 | CCSession — `grading — subagent`, default mode | `!wc -l feedback_focus.md` → 3; `!grep -oE 'Task\|Write'` → Task, Write; `!jq …cache_creation…` → 31942 | 27.8 → 20.8 s |
| 8 | BFLOW | FlowDiagram (skin claude) | MAIN → TASK → SUBAGENT (Read/Grep/Glob) with BATCH feeding SUBAGENT → SUMMARY → MAIN → WRITE | 27.1 → 22.1 s |
| 9 | BSHOW | CCPlainShell — `zsh — ~/grading` | `$ cat feedback_focus.md` — the three verbatim findings; `$ wc -l` → 3 | 16.1 → 14.6 s |
| 10 | B05 | CCBoondoggleScore | 6 steps, `dangerousMiddle: 3` (the deployment); tally PF·2 PA·1 IJ·1 TO·0 EI·0 | 38.8 → 32.0 s |
| 11 | B06 | CCHumanLedger | 4 human rows / 4 AI rows / closing "39 lines. Mine." | 39.9 → 28.9 s |
| 12 | BVDT | ClaudeVerdictArtifact | 4 lines; last line `FALSIFIABLE:` | 32.3 → 30.1 s |
| 13 | BHTF | ClaudeComposerAsk | greeting "Your turn."; the triage-subagent prompt reads in full | 26.4 → 21.6 s |
| 14 | BOUT | ClaudeTitleOutro | exact title, `@NikBearBrown`, slug-seeded mascot | 6.1 → 5.9 s |

Master duration (measured, sum of Kokoro mp3s): **316.3 s ≈ 5:16**.

Body beats that leave `CCSession`:

- BIDEA — idea beat, always
- BDEFS — jargon card
- B02 — the deployment file (outside any session; CCPlainShell)
- BFLOW — topology across two windows (not visible in either)
- BSHOW — the built artifact
- B05 / B06 — CONDUCT / HUMAN closing-block beats

No two consecutive terminal-leaving beats without a named reason. BFLOW→BSHOW is BUILD-SHOW LAW.
