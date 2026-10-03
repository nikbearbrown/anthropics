# SHOTLIST — cc-skill-build-once

Fifteen beats. Every shot is a Remotion library component; no Manim, no slates, no external footage. Cold open on `CCSession`, per `cc-explainer`'s TERMINAL-FIRST law and the `metadata.skill: "cc-explainer"` bookend override.

| # | Beat | Pattern | What lands | Provenance |
|---|---|---|---|---|
| 1 | B00 · COLD OPEN — BARE | `CCSession` (accept-edits) | The ask · Read · Claude improvises rubric · `# Grade: A- (92/100)` | `evidence/run-bare.jsonl` |
| 2 | BIDEA · THE IDEA | `BrutalistHesitantWriter` | 4-line thesis; "Typed" → "Written once" | pedagogy — the film's own claim |
| 3 | BDEFS · DEFINITIONS | `CCDefinitions` | SKILL.md · frontmatter · trigger sentence · Never section · definition of done | jargon the chat-window audience will hear |
| 4 | B01 · BARE — VERIFY | `CCPlainShell` | `head`, `grep -cE 'A-\|/100'` → 2; `grep -c 'rubric I asked for'` → 0 | `evidence/run-bare.jsonl` (final `result.result`) |
| 5 | B02 · THE SKILL FILE | `CCPlainShell` | `wc` → 54 SKILL.md · 34 check_grade.py; frontmatter; three `## ` sections | `evidence/SKILL.md`, `evidence/check_grade.py` |
| 6 | B03 · SKILL — THE RUN | `CCSession` (accept-edits) | Same ask · `Skill(grading-workflow)` · Read · Write feedback · Bash check_grade → PASS | `evidence/run-skill.jsonl` |
| 7 | B04 · SKILL — VERIFY | `CCPlainShell` | `wc feedback/mira.md` → 16; 4 verdicts; 0 grades; `check_grade.py` → PASS | `evidence/feedback-mira.md` |
| 8 | B05 · THE PRESSURE TEST | `CCSession` (accept-edits) | Pressure ask · Skill · Reads checker · refuses percent · PASS | `evidence/run-skill-pressure.jsonl` |
| 9 | BFLOW · THE FLOW | `CCHarnessMap` | Core MODEL; rings PROMPT / DESCRIPTION MATCH / SKILL LOAD / YOUR LOOP | strings drawn from evidence |
| 10 | BSHOW · THE BUILT FILE | `CCPlainShell` | `cat feedback/mira.md` — 4 rubric headings, Growth line, arithmetic verified | `evidence/feedback-mira.md` |
| 11 | BCOND · CONDUCT | `CCBoondoggleScore` | 6 steps; dangerous middle at #3 (reading bare) | `SESSION.md` |
| 12 | BHUM · HUMAN | `CCHumanLedger` | 4 MUST/SHOULD human rows · 4 CAN/SHOULD AI rows · closing | `SESSION.md` |
| 13 | BVDT · VERDICT | `ClaudeVerdictArtifact` | 4 lines; last line `FALSIFIABLE: …` | this reel's own thesis |
| 14 | BHTF · YOUR TURN | `ClaudeComposerAsk` | Greeting `Your turn.`; topic `YOUR TURN · CLAUDE CODE 101`; full paste prompt | authored |
| 15 | BOUT · OUTRO | `ClaudeTitleOutro` | Title · `@NikBearBrown` · slug-seeded mascot | OUTRO-LOCK |
