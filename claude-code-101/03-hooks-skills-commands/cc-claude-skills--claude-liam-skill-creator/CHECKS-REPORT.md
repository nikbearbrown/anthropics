# CHECKS-REPORT — cc-claude-skills--claude-liam-skill-creator

Pre-compile pass, 2026-09-10.

## Spine (SHOW/HOLD/CARD)

| Beat | Surface | Class | Note |
|---|---|---|---|
| B00 | CCSession | SHOW | Cold open: the vague-A1 run; Skill() fires from a nine-word description |
| BIDEA | BrutalistHesitantWriter | HOLD | "crafted" → "measured" is the film's misconception |
| BDEFS | CCDefinitions | CARD | 5 terms: skill, description, trigger, router, eval |
| B01 | CCSession | SHOW | Liam's VERIFY on the vague-A1 run (grep, wc, checker) |
| B02 | CCPlainShell | CARD | The two SKILL.md descriptions compared (9 vs 63 words) |
| B03 | CCSession | SHOW | The pushy-A1 run — same ask, same Skill() fire, same shape |
| B04 | CCSession | SHOW | The negative ask (a3) — no Skill(), prose reply |
| B05 | CCPlainShell | SHOW | Six-cell tally grepped out of every run; trigger-tally.txt |
| B06 | CCBoondoggleScore | CARD | 5 steps, dangerous middle at step 4 (reading a null result honestly) |
| B07 | CCHumanLedger | CARD | AI CAN / SHOULD × HUMAN MUST / SHOULD, filled from this session |
| BVDT | ClaudeVerdictArtifact | HOLD | 6 verdict lines including FALSIFIABLE |
| BHTF | ClaudeComposerAsk | CARD | Your-turn prompt: run your own six-cell tally |
| BOUT | ClaudeTitleOutro | HOLD | Locked outro; slug-seeded mascot |

## Terminal-first check

Body beats: 13. Non-terminal beats (BIDEA, BDEFS, B02, B05, B06, B07 all leave the terminal). No two consecutive card beats without a named reason:

- BIDEA / BDEFS — the two "before the loop" beats, both named as such (SKILL.md).
- B02 (CCPlainShell) is between two CCSession beats.
- B05 is the tally-across-sessions beat; B06/B07 are the closing block. Each carries `leaves_terminal_because` or is a beat the SKILL.md exempts (closing block, IDEA, DEFINITIONS).

## Teaching arc

- **Misconception (BIDEA):** the description is *crafted*.
- **Correction (BIDEA):** the description is *measured*.
- **Show (B00 + B01):** the vague description fires; the checker passes.
- **Contrast (B02 + B03):** the pushy version, same ask, same fire.
- **Falsification test (B04):** the near-miss ask; neither fires.
- **Verify (B05):** the six-cell tally — 4/4 both descriptions.
- **Conduct (B06):** who did what; dangerous middle = reading a null result honestly.
- **Human (B07):** what only the human can do — pick the ask, read the tally as it stands.
- **Recap (BVDT):** falsifiable line — "an ask on which one description fires and the other doesn't."
- **Handoff (BHTF):** scaffolded task — run the same six-cell tally on your own skill.

## BUILD-SHOW

**BUILD-SHOW: not armed — concept film.** This reel explains a Claude Code feature (the description-optimizer's inner loop, done by hand at n=6) rather than building something with Claude Code. `metadata.build` is unset; BFLOW / BSHOW are skipped per SKILL.md §BUILD-SHOW LAW.

## GATE T — text budgets pre-check

- Text blocks all ≤ 44 chars (author_sheet.py assertion, warnings addressed).
- Ledger rows all ≤ 34 chars (author_sheet.py assertion; longest = 34).
- Boondoggle step text all ≤ 46 chars (author_sheet.py assertion; longest = 39).
- Verdict = 6 lines (allowed: 4 or 6 — never 5).
- CCPlainShell lines all ≤ 60 chars; ≤ 14 lines per beat.

## Voice and outro

- Every beat: Liam (`am_onyx`), Kokoro, first person, present tense, Teardown register.
- Cold open opens with "This is Liam, in for Bear." (IN-FOR-BEAR LAW § cold open).
- BVDT starts "Let's recap with Claude." (per SKILL.md handoff line).
- BOUT is exact title then "Liam, in for Bear." (IN-FOR-BEAR LAW § outro).

## Audio

- All 13 beats measured by `generate_audio_kokoro.py` (2026-09-10).
- Total measured runtime: 243.2 s (~4:03) before compile padding / holds.
