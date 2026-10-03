# SHOTLIST — cc-claude-skills--what-is-claude-skills

| Beat | Surface | What moves |
|---|---|---|
| B00 | `CCSession` (naive) | the ask; ls; three Reads capped at frontmatter; three summaries |
| BIDEA | `BrutalistHesitantWriter` | 'match' → 'may not' |
| BDEFS | `CCDefinitions` | four terms (SKILL.md, frontmatter, body, install) |
| B01 | `CCPlainShell` | `sed -n '1,4p'` on each SKILL.md; three descriptions land |
| B02 | `CCSession` (full body) | prompt; Read summarizer; rule 5 (rm) quoted; Claude's flag |
| B03 | `CCPlainShell` | `grep -n delete` → line 14; awk → 23 body lines |
| B04 | `CCSession` (full body) | Read tone-warmer; rule 9 quoted; "sticky override" flag |
| B05 | `CCSession` (full body) | Read format-strict; three rules; "no surprise" |
| B06 | `CCBoondoggleScore` | six steps; step 3 rings; tally PF 2 · PA 1 · IJ 1 |
| B07 | `CCHumanLedger` | AI column then HUMAN column; closing "The audit is a prompt. It's yours." |
| BVDT/BHTF/BOUT | bookends | verdict → your turn → OUTRO-LOCK |

Non-terminal body beats: BIDEA (writer types the misconception), BDEFS (definitions card), B01 (shell side-by-side comparison — the naive run only saw one description at a time), B03 (the arithmetic of the mismatch). Each carries `shot.leaves_terminal_because`.
