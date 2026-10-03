# SHOTLIST — cc-skill-development

Every beat renders on a CC-kit component or a Claude-brand bookend. All frames come from the reel itself (Remotion). No external footage, no captured recordings.

| # | Beat | Component | What is on screen |
|---|---|---|---|
| 1 | B00 | CCSession | The bare run's terminal: prompt block with the one-line ask; four tool calls (Read × 3, Bash mkdir, Write SKILL.md, Bash validate\_skill.py); three text blocks with Claude's PASS summary. |
| 2 | BIDEA | BrutalistHesitantWriter | Dark CC palette. Four lines of serif type land line-by-line; "prompt" gets typed, held, and rewritten as "folder". |
| 3 | BDEFS | CCDefinitions | Five terms in a column: SKILL.md, frontmatter, trigger phrase, prog. disclosure, imperative form. |
| 4 | B01 | CCSession | Bang commands against the bare skill's folder: `wc`, `ls`, `head -3`, `grep -Ec 'you should\|you need'`. One-file result, third-person description, zero second-person forms. |
| 5 | B02 | CCSession | The checker-only run's terminal: shorter ask, one Read (validate\_skill.py), one Write, one PASS line at 635 words, then `ls` → SKILL.md. Same shape as bare. |
| 6 | B03 | CCSession | The rules run's terminal: rules-added ask, three Reads, mkdir references/, two Writes, PASS at 367 words. |
| 7 | B04 | CCSession | Verify the rules run: `wc -w SKILL.md references/*.md` → 367 + 552; `ls` → two entries; `grep -n references SKILL.md` → line 46 points at troubleshooting. |
| 8 | BFLOW1 | CoworkFolderTree | Root labelled `skills/csv-shape`. Four children land in sequence: **SKILL.md** (accent), references/, scripts/, assets/. Caption: "SKILL.md required · everything else optional". Spark: "The folder is the skill." |
| 9 | BSHOW1 | CCPlainShell | Plain terminal, no Claude chrome. Three commands land in order: `head -3 SKILL.md`, `grep -o '"…"' SKILL.md \| head -3`, `grep -n references SKILL.md` — each followed by its actual output from `evidence/SKILL.rules.md`. |
| 10 | BCOND | CCBoondoggleScore | Two-column score, six rows, dangerous middle rings step 3 in terracotta. Distribution tally at the bottom: PF 2 · PA 1 · IJ 1 · TO 0 · EI 0. |
| 11 | BHUM | CCHumanLedger | THE AI (CAN × 2, SHOULD × 2) fills first; THE HUMAN (MUST × 3, SHOULD × 1) follows at cue 70. Closing sentence lands last. |
| 12 | BVDT | ClaudeVerdictArtifact | verdict.md style card; four lines; final line "FALSIFIABLE: a bare run that writes a references/ folder on its own." |
| 13 | BHTF | ClaudeComposerAsk | Composer with greeting "Your turn.", eyebrow "YOUR TURN · CLAUDE CODE 101", the paste prompt in the input, send arms. |
| 14 | BOUT | ClaudeTitleOutro | Title restate; @NikBearBrown handle; mascot seeded by slug. |

Aspect: 16:9. FPS: 30. Native 4K (3840×2160) via runtime defaults. Master file: `cc-skill-development.mp4` at reel root after `art final`.
