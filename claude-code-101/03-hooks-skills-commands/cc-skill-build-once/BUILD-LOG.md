# BUILD-LOG — cc-skill-build-once

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

**The experiment.** Same one-sentence teacher's ask — `Grade student-submission.md — feedback and a final grade please.` — under four conditions, each a fresh headless `claude -p` run against Claude Code 2.1.150 in a scratch folder: bare (README + two submissions only), with the skill (a 54-line `.claude/skills/grading-workflow/SKILL.md` + a 34-line `check_grade.py`), durability (a second student, same skill), and pressure (user demands a percent). Bare: 32.3 s, an invented rubric, `# Grade: A- (92/100)`. Skill: 35.9 s, `Skill(grading-workflow)` fires as a tool call in the stream-json, `Read → Write feedback/mira.md → Bash check_grade.py → PASS`, refuses a final grade. Durability: 62.2 s, same shape on a different student. Pressure: 58.1 s, refuses again after reading `check_grade.py` itself.

**Session evidence** in `evidence/`: raw `--output-format stream-json` for all four runs, the two submissions, the SKILL.md and checker Liam wrote once, and both feedback files the skill produced.

**Compile.** One pass. `art run` filled every slot (15 of 15 VIDEO); `art final` re-mapped, ran GATE T (PASS — three §8.10 SKIPs on component-native beats, four measured hits ≤ 0.68), content-check PASS, frame-check PASS (canvas 3840×2160), lane-check PASS, GATE AUDIO PASS (mean_volume −23.7 dB). Master `cc-skill-build-once.mp4` — 281.3 s (4:41), 3840×2160 h264 + AAC.

**Non-blocking warnings.**
- SKIN LINT: `B00: cold open is 'CCSession', COLD OPEN LAW wants ClaudeComposerAsk`. False positive — `cc-explainer`'s GATE BOOKEND override arms via `metadata.skill: "cc-explainer"` and permits a CC surface cold open (TERMINAL-FIRST LAW).
- Motion histogram: `type: 9/15 (60%)` over the pantry's 40 % cap. Expected for a Session/Shell reel — CCSession, CCPlainShell, and BrutalistHesitantWriter all animate by typing; `drawon` covers CCDefinitions, CCHarnessMap, CCBoondoggleScore, CCHumanLedger; `hold` covers BVDT and BOUT. The alternative would be to convert one shell to `hold` (a still frame of the final state), which would break the "the shell keeps typing" reading the beat is built on. Left as-is.

**GATE T detail.** All §8-family subgates PASS; the four measured §8.10 (edge-density) hits: B01 = 0.44, B02 = 0.56, B04 = 0.33, BSHOW = 0.10, BVDT = 0.68 — all well below the failure threshold. Component-native beats (BIDEA, BDEFS, BFLOW, BCOND, BHUM, BHTF, BOUT) SKIP §8.10 as designed.

**Not published.** TOPOST only via `post`, only on ask. Master stays in the reel folder per cc-explainer Hard Rule #9.

**What the receipts prove.**

1. Claude Code 2.1.150 auto-launches a skill by matching the natural-language ask against the `description:` frontmatter — visible as a `Skill()` tool call in the stream-json, exactly the way `Read()` and `Write()` are.
2. The workflow shape holds across two different students (Runs B and C).
3. The `Never` rule was respected in three of three skill runs, including one under direct pressure — but that is an outcome, not a guarantee. The verdict's FALSIFIABLE line names the disproof condition.
