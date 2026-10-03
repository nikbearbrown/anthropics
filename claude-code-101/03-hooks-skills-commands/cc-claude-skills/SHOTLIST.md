# SHOTLIST — cc-claude-skills

15 beats · Kokoro `am_onyx` throughout · 4:30 measured.

| # | Beat | Pattern | Duration | What is on screen |
|---|---|---|---|---|
| 1 | B00 | CCSession | 14.7 s | Bare cold open: the ask types, `Read article.md`, five ad-hoc summary text blocks, `**Two takeaways:**` bolded list. Mode `accept-edits`. Mascot off. |
| 2 | BIDEA | BrutalistHesitantWriter | 17.8 s | CC palette (bg #1F1E1B, ink #F2F0E9, accent #D97757). Writer types four lines; `slash command` reconsidered into `description`. |
| 3 | BDEFS | CCDefinitions | 22.7 s | Five terms: SKILL.md · frontmatter · description · auto-launch · semantic match. |
| 4 | B01 | CCPlainShell | 11.0 s | zsh — ~/scratch. `ls scratch/` → README.md article.md. `grep -c '"name":"Skill"' run-bare.jsonl` → 0. Comment closes. |
| 5 | B02 | CCPlainShell | 17.3 s | zsh — ~/scratch. `ls .claude/skills/exec-summary/`, `wc -l`, `head -3 SKILL.md` (frontmatter), `grep '^## '` shows Format · Rules · Done. |
| 6 | B03 | CCSession | 15.7 s | scratch — with skill. The same ask, then `Skill(exec-summary)`, then `Read article.md`, two-line plan text, `Write summary.md`, `Bash python3 check_summary.py summary.md`, `PASS. Four sections written.` |
| 7 | B04 | CCPlainShell | 14.0 s | zsh — ~/scratch. `grep -c '"name":"Skill"' run-skill.jsonl` → 1. `grep '^## ' summary.md` → four headings. `CHK=…`, `python3 $CHK summary.md`, `PASS`. |
| 8 | B05 | CCSession | 20.1 s | scratch — the other ask. Prompt: "Wrap article.md for a leadership audience…". `Skill(exec-summary)` fires anyway. Read×2, two-line plan, Write, Bash, `PASS. Same four sections.` |
| 9 | BFLOW | CCHarnessMap | 19.1 s | MODEL core with subline "can only talk". Four rings, inside out: YOUR ASK → DESCRIPTION MATCH → SKILL LOAD → YOUR LOOP. Each ring's item is a string from the transcript. Caption last. |
| 10 | BSHOW | CCPlainShell | 19.4 s | zsh — ~/scratch — summary.md. `cat summary.md` reveals the four sections and their opening lines (paraphrase-shortened to fit width). |
| 11 | BCOND | CCBoondoggleScore | 26.2 s | System "exec-summary · fresh sessions". Six steps, PF/PF/C/H/C/C. Dangerous middle: step 4 (`Read bare: nothing was pinned`). Tally at the end. |
| 12 | BHUM | CCHumanLedger | 23.6 s | Two columns. AI: CAN/CAN/SHOULD/SHOULD. HUMAN: MUST/MUST/MUST/SHOULD. Closing: "58 lines, written once. Same shape every ask." |
| 13 | BVDT | ClaudeVerdictArtifact | 26.3 s | artifactTitle `verdict.md`, heading `One Prompt. Every Time.`, four lines — last one starts `FALSIFIABLE:`. |
| 14 | BHTF | ClaudeComposerAsk | 19.8 s | Greeting `Your turn.`; topic `YOUR TURN · CLAUDE CODE 101`; segment title = film title; command = the four-question prompt. |
| 15 | BOUT | ClaudeTitleOutro | 3.2 s | Title `One Prompt. Every Time.`, handle `@NikBearBrown`, subline `""`. Slug-seeded mascot. |
