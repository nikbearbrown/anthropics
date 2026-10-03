# CHECKS-REPORT — cc-skill-build-once

## SHOW / HOLD / CARD

- **SHOW (11 of 15 beats).** B00, B03, B05 are `CCSession` transcripts of real fresh headless runs; B01, B02, B04, BSHOW are `CCPlainShell` verifications of the files those runs wrote or read; BCOND, BHUM, BVDT are the score/ledger/verdict of *this* session, not exposition.
- **HOLD (2 beats).** BIDEA (`BrutalistHesitantWriter`, the film's thesis with one corrected word) and BDEFS (`CCDefinitions`, five terms the chat-window audience would trip on).
- **CARD (2 beats).** BHTF (`ClaudeComposerAsk`, the viewer's paste-ready prompt) and BOUT (`ClaudeTitleOutro`).
- **DIAGRAM (1 beat).** BFLOW (`CCHarnessMap`) — the concentric rings the transcript already showed, drawn.

## Teaching arc

- **Predict-before-reveal.** B00 sets the surprise up: same ask, empty folder, letter grade and percent nobody asked for. B01 reveals it as a verifiable count (`grep -cE 'A-|/100' bare.md` → 2). BIDEA states the misconception in one word: `Typed` → `Written once`.
- **Concrete-before-abstract.** B02 shows the SKILL.md as a file — `wc`, `grep` on the sections — before B03 shows what happens when Claude sees it (`Skill(grading-workflow)` auto-fires). BFLOW comes only after the viewer has watched the rings behave.
- **Useful friction.** B05 (the pressure test) is the honest correction cycle: the `Never` rule is advisory; it held here, but "it held" is not "it is a law". The verdict's FALSIFIABLE line names the disproof condition explicitly ("a skill run that emits a percent grade with no user pressure").
- **Scaffolded handoff.** BHTF's prompt asks Claude to interview the viewer through the four decisions (trigger, workflow, Never, definition-of-done script) and then write the SKILL.md and checker — the same order this film demonstrated.

## BUILD-SHOW

- **Armed.** `metadata.build: true` — the ask verb is *build* (build a SKILL.md and a checker); the loop ends with a thing that runs (the skill invokes on any subsequent matching ask).
- **BFLOW.** `CCHarnessMap` — MODEL core; rings PROMPT · DESCRIPTION MATCH · SKILL LOAD · YOUR LOOP. Every ring's items are strings the transcript already carried (the ask, the skill's `name:` field, the skill file path, the tool sequence).
- **BSHOW.** `CCPlainShell` scrolls `cat feedback/mira.md` — the actual file the skill wrote, with the arithmetic verified in line. Provenance: `evidence/feedback-mira.md`.

## Gate status

- **GATE BOOKEND** — cold open is `CCSession` (the skill override arms via `metadata.skill = "cc-explainer"`); recap is `ClaudeVerdictArtifact` (`BVDT`); your-turn is `ClaudeComposerAsk` (`BHTF`); outro is `ClaudeTitleOutro` (`BOUT`).
- **GATE T (kerning)** — no `CCSession` text block > 44 chars; no `CCHumanLedger` row > 34 chars; no `CCBoondoggleScore` step > 46 chars; no `CCDefinitions` meaning > 70 chars (checked in `author_sheet.py`).
- **GATE L (library-first)** — every pattern used exists in `runtime/remotion/src/scenes/` (`BrutalistHesitantWriter`, `CCDefinitions`, `CCSession`, `CCPlainShell`, `CCHarnessMap`, `CCBoondoggleScore`, `CCHumanLedger`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro`). No slates; no PUNTs.

## Deviations from the concept

- Concept framed invocation as `/grading-workflow` (slash-command). This reel films the actual Claude Code 2.1.150 behavior: the skill is auto-launched by description-trigger match, visible as a `Skill()` tool call in the stream-json. The pedagogy (build once, invoke every semester) is unchanged.
- Concept's timing claim ("18 min → 90 sec") is generic — I did not stage a stopwatch. What the receipts do show: the bare run was 32.3 s and the skill run was 35.9 s (both wall-clock of a headless call); the skill's *savings* live in Liam not re-typing the workflow, not in a Claude wall-clock delta. Narration mirrors this ("ninety seconds of Claude's time; nineteen minutes of Liam's teacher-time replaced by fifty-four lines of a file he can read") — the "nineteen minutes" is the teacher's cost, not a benchmark.

## What Bear should watch for on review

1. B03 timing — nine blocks including a `Skill` tool call not present in earlier CC-explainer reels; watch for Clawd bleed under the last text (`mascot: 'off'` already set).
2. BFLOW ring items — verify every string appears in `evidence/` before this reel is retitled or re-cut.
3. B05's fourth text ("the Never held, but it is not a law") is the load-bearing epistemic claim; the verdict's FALSIFIABLE line is its receipt.
