# SHOTLIST — cc-claude-agent-skills--claude-skills-progressive-disclosure

| Beat | Pattern | Content |
|---|---|---|
| B00 | CCSession | Run B — the ask types, `Skill(exec-summary)` fires, Read article.md, three text blocks (four-section shape), Write summary.md. `mascot: off`. |
| BIDEA | BrutalistHesitantWriter | Four lines. Trigger word "resident" reconsidered into "described". CC palette (ink `#F2F0E9`, accent `#D97757`, bg `#1F1E1B`). |
| BDEFS | CCDefinitions | Five terms: skill, description, body, reference, progressive disclosure. |
| B01 | CCPlainShell | `wc -l` on SKILL.md and refs; `head -3` on frontmatter; `wc -w` on the same files. All lines ≤60 chars. |
| B02 | CCSession | Run A — Read article.md, Write summary.md. `mascot: off`. |
| B03 | CCSession | Run A verify — three `grep`/`python3` bang commands, three outputs (`0`, `0`, `FAIL: headings — got []`). |
| B04 | CCSession | Run B — the ask, `Skill(exec-summary)`, Read article.md, three text blocks (four sections + refs skip), Write summary.md. `mascot: off`. |
| B05 | CCSession | Run B verify — four bang commands, `1`, `0`, four `##` heads, `PASS`. |
| B06 | CCSession | Run C — the ask with "house style", `Skill(exec-summary)`, Read references/house-style.md, Read article.md, three text blocks (rules cited), Write summary.md. `mascot: off`. |
| B07 | CCSession | Run C verify — four bang commands, `1`, `1`, `0`, `PASS`. |
| B08 | CCBoondoggleScore | 7 steps. Dangerous middle: step 3 (references + conditionals). Distribution shown: PF 2 · IJ 1 · PA 1 · TO 0 · EI 0. |
| B09 | CCHumanLedger | 4 CAN/SHOULD rows (AI) + 4 MUST/SHOULD rows (HUMAN) + closing. All rows ≤34 chars. |
| BVDT | ClaudeVerdictArtifact | 4 lines, last is `FALSIFIABLE:`. |
| BHTF | ClaudeComposerAsk | Greeting `Your turn.`, topic `YOUR TURN · CLAUDE CODE 101`, prompt read aloud. |
| BOUT | ClaudeTitleOutro | Title, `@NikBearBrown`, no subline. Mascot seeded from slug. |
