# CHECKS-REPORT — cc-claude-skills--claude-liam-example-skill

cc-explainer, Claude Code 101 tier 03 (hooks / skills / commands), film: example-skill.

## SHOW / HOLD / CARD
| # | ID | Surface | Show / Hold / Card | Notes |
|---|---|---|---|---|
| 1 | B00 | CCSession | SHOW | opening the reference template |
| 2 | BIDEA | BrutalistHesitantWriter | HOLD | 'decoration' → 'the shape' |
| 3 | BDEFS | CCDefinitions | HOLD | 4 terms — skill, frontmatter, description, definition of done |
| 4 | B01 | CCSession | SHOW | Run A — no skill; ad-hoc shape |
| 5 | B02 | CCSession | SHOW | Run A verify — check_peek FAIL |
| 6 | B03 | CCPlainShell | SHOW | csv-peek/SKILL.md (40-line full form) |
| 7 | B04 | CCSession | SHOW | Run B — Skill(csv-peek), Write, PASS |
| 8 | B05 | CCSession | SHOW | csv-peek/SKILL.md (4-line bare frontmatter) |
| 9 | B06 | CCSession | SHOW | Run C — Skill fires, lowercase headings |
| 10 | B07 | CCSession | SHOW | Run C verify — check_peek FAIL |
| 11 | B08 | CCBoondoggleScore | CARD | 6 steps, dangerous middle = step 3 |
| 12 | B09 | CCHumanLedger | CARD | 4 MUST/SHOULD, 4 CAN/SHOULD |
| 13 | BVDT | ClaudeVerdictArtifact | HOLD | 4 lines, last is FALSIFIABLE |
| 14 | BHTF | ClaudeComposerAsk | HOLD | Your turn |
| 15 | BOUT | ClaudeTitleOutro | HOLD | title, @NikBearBrown, no subline |

## BUILD-SHOW
Not armed — concept film. This reel explains the example-skill template (a concept), not build-and-ship X. BFLOW/BSHOW skipped intentionally.

## Terminal-first check
14 of 15 beats terminal-native (CCSession or CCPlainShell). Three non-terminal beats (BIDEA, BDEFS, then the bookend trio BVDT/BHTF/BOUT) each carry a named reason. No two consecutive un-named non-terminal body beats.

## Teaching arc
- BIDEA sets the misconception (the description is all that matters; body is decoration).
- B01 shows what "no skill" produces — the null baseline.
- B03-B04 show the description-as-trigger claim confirmed.
- B05-B07 show the body-as-decoration claim falsified — same folder, description-only, drifted output.
- BVDT names both — verified and falsified, side by side. The FALSIFIABLE line is a claim you could actually run.
- BHTF's YOUR TURN is a scaffolded first attempt: copy the description pattern, then write the definition-of-done SCRIPT for your own skill's shape. Body-first thinking.

## Gates armed
- GATE L: every pattern is a real component. Verified via `./art scenes --check` for each.
- REAL-SESSION LAW: every CCSession block traces to `SESSION.md`.
- LIAM LAW: `am_onyx` on every beat; "in for Bear" in B00 and BOUT.
- OUTRO-LOCK: BOUT props carry `title`, `handle: "@NikBearBrown"`, `subline: ""`.
- CCSession text-block budget: ≤ 44 chars, checked by the author script.
- CCHumanLedger row budget: ≤ 34 chars, checked by the author script.
- CCBoondoggleScore step-text budget: ≤ 46 chars, checked by the author script.
- BVDT: 4 lines (paginates as 2+2), last line is FALSIFIABLE.
