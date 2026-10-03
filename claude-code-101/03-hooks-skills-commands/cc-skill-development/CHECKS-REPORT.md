# CHECKS-REPORT — cc-skill-development

## Spine

| Beat | Kind | Element | leaves_terminal_because |
|---|---|---|---|
| B00 | COLD OPEN | CCSession | — |
| BIDEA | IDEA | BrutalistHesitantWriter | the idea is not in any session; the writer types it and corrects "prompt" → "folder" |
| BDEFS | DEFINITIONS | CCDefinitions | definitions for a chat-window audience |
| B01 | LOOP · VERIFY (bare) | CCSession | — |
| B02 | LOOP · MIDDLE CASE (checker-only) | CCSession | — |
| B03 | LOOP · PROMPT+CHANGE (rules) | CCSession | — |
| B04 | LOOP · VERIFY (rules) | CCSession | — |
| BFLOW1 | BUILD-SHOW · flow | CoworkFolderTree | BFLOW: the folder anatomy the terminal only implied across two sessions |
| BSHOW1 | BUILD-SHOW · output | CCPlainShell | BSHOW: the finished skill's frontmatter and reference pointer, plain-shell read |
| BCOND | CONDUCT | CCBoondoggleScore | — |
| BHUM | HUMAN | CCHumanLedger | — |
| BVDT | VERDICT | ClaudeVerdictArtifact | — |
| BHTF | YOUR TURN | ClaudeComposerAsk | — |
| BOUT | OUTRO | ClaudeTitleOutro | — |

## Gates satisfied at authoring time

- **TERMINAL-FIRST (SKILL §85–102).** Body defaults to `CCSession` (B00, B01, B02, B03, B04). BIDEA / BDEFS / BFLOW1 / BSHOW1 leave the terminal with a named reason (above). Two consecutive non-terminal beats: BIDEA → BDEFS (both reasoned, part of the fixed spine), BFLOW1 → BSHOW1 (both reasoned as build-show slots). No unreasoned pair.
- **REAL-SESSION.** Every `CCSession` block traces to `SESSION.md` — tool sequences from the three real headless runs, PASS lines from the actual `validate_skill.py` output, prompt blocks from the argv `claude -p` received (or its faithful summary where the prompt would overflow the block; the full text is in `SESSION.md`).
- **TYPES-NOT-NARRATES.** Every `prompt` block contains what Liam typed (the ask; the bang-commands in the plain shells). No block contains narration.
- **VERBATIM PRODUCT STRINGS.** Session modes are `accept-edits` and `default` — the two the ask uses. No hand-styled status strings.
- **VERIFY IS A COMMAND.** B01 and B04 run bang-commands (`wc`, `ls`, `head`, `grep`) against the skill files. B00, B02, B03 include `python3 validate_skill.py` as the VERIFY step.
- **BUILD-SHOW LAW (SKILL §202–265).** `metadata.build: true` — the ask is "build a skill". BFLOW1 (CoworkFolderTree, real names on the folders — SKILL.md, references/, scripts/, assets/) and BSHOW1 (CCPlainShell reading the finished SKILL.md frontmatter and the reference pointer) sit immediately before CONDUCT. Node labels on BFLOW1 come from the source SKILL.md's Anatomy section (REAL-SESSION applies to the anatomy, not to invented children).
- **CONDUCT + HUMAN.** BCOND is a real-session score: PF 2, PA 1, IJ 1, TO 0, EI 0 — the film says so and rings the dangerous middle (step 3: reading the folder after the bare run and noticing there was no references/). BHUM is grounded in the runs, not principle.
- **OUTRO-LOCK.** `ClaudeTitleOutro`, `handle: "@NikBearBrown"`, `subline: ""`, title verbatim, Liam says "in for Bear".
- **IN-FOR-BEAR LAW.** Satisfied twice — B00 cold open ("This is Liam, in for Bear") and BOUT ("Liam, in for Bear").
- **VERDICT.** 4 lines (not 5), FALSIFIABLE line last, handoff "Let's recap with Claude." opens the narration.
- **YOUR-TURN.** Greeting `"Your turn."`, topic carries "YOUR TURN".
- **Budget.** author_sheet.py asserts CCSession text blocks ≤ 44 chars, ledger rows ≤ 30, boondoggle steps ≤ 44, handoffs ≤ 50, plain-shell lines ≤ 62, verdict lines ∈ {4, 6}, CCDefinitions terms ≤ 18 chars, meanings ≤ 72. All pass at generation.

## Teaching arc

- **Prediction before reveal.** BIDEA plants the misconception ("A skill is a prompt Claude reads") and its correction ("folder"). B00 shows the bare run silently making the mistake the film exists to fix — a monolithic file — and the checker missing it.
- **Concrete before abstract.** Three real headless sessions before the anatomy diagram (BFLOW1). Only after the viewer has SEEN two files vs one file does the folder-shape become the argument.
- **Useful friction.** B02 (the checker-only run) is the friction: the viewer has to hold two things at once — the checker passing, and the folder shape failing progressive disclosure. That is the pedagogy.
- **Falsifiability.** BVDT's last line names the specific bare-run behaviour that would refute the film.
- **Handoff to practice.** BHUM closes with what to keep in the human's lane. BHTF hands the viewer a prompt they can paste that reproduces the human moves in miniature — name the triggers, decide what belongs where, don't write the skill yet.

## Not applicable / not armed

- **Bookend gate override.** `metadata.skill: "cc-explainer"` set — bookend_check accepts a CC cold open. BOUT props carry the redundant-but-required `handle` and `subline` even though ClaudeTitleOutro hardcodes them.
- **Diagrams beyond BFLOW1.** One BFLOW beat covers the whole build (folder anatomy). No secondary diagram (state machine / sequence / file-tree) needed — the folder tree IS the file tree.
- **Photorealism / paid generation.** None. Kokoro `am_onyx` only. No Higgsfield. No paid audio. Cost: three Claude API sessions and $0 for everything else.
