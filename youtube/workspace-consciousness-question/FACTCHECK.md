# FACTCHECK — workspace-consciousness-question (E07)

Status: **SEED — GATE F NOT YET SIGNED. Audio lock requires human sign-off on this file.**

Sources: `books/arxiv/transformer-circuits.pub/workspace-paper.html` (primary);
`books/arxiv/transformer-circuits.pub/workspace-skeptical-read.md` (Bear's skeptical read);
`books/arxiv/transformer-circuits.pub/workspace-dive-manifest.json` (paper metadata).
Economist claims: ⛔ ECON-VERIFY — Bear's saved article copy required; no guesses ship.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | GWT core: "broadcast to a shared stage… brain's specialists can all read. Limited capacity. Competitive entry. Sharp ignition." | PASS | §9.4 opening paragraph lists these as the GWT properties motivating the five tests; confirmed in workspace-skeptical-read.md. Paraphrase; not a verbatim quote. | — |
| 2 | B04 | §9.4: "restrict our focus to theories that tie consciousness to functional or computational properties" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against corpus §9.4. Re-verify character-for-character at audio lock. | — |
| 3 | B04 | §9.4: "our results are not relevant to assessing consciousness according to such theories" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against corpus §9.4 (IIT/substrate bracket). Re-verify at audio lock. | — |
| 4 | B04 | §9.1: "unclear whether this mirrors the sharp, competitive 'ignition'" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against corpus §9.1 ignition hedge. Re-verify at audio lock. | — |
| 5 | B05 | §9.4: "neither of which has a direct analog in a transformer's forward pass" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against corpus §9.4 recurrence discussion. Re-verify at audio lock. | — |
| 6 | B05 | §9.4: "We do not know whether this difference matters" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against corpus §9.4. Re-verify at audio lock. | — |
| 7 | B06 | Fig 25A ablated transcript verbatim (five lines) | EXEMPT | Must be verified line-for-line against Fig 25A in corpus before audio lock — marked RE-VERIFY in build prompt. Exempt from GATE F sign-off until Bear reads Fig 25A and signs. No audio may generate before that sign-off. | Verify Fig 25A in corpus; if lines differ, update beat_sheet.json B06 props.text and narration. |
| 8 | B06 | Baseline: "Am I performing introspection or actually doing it?" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against Fig 25/87 baseline text. Re-verify at audio lock. | — |
| 9 | B07 | Experiential score: 3 binary LLM judgments; collapse on Sonnet 4.5/Opus 4.5/Opus 4.6; matched-norm controls near baseline | PASS | §6.2/A.23 confirmed in build prompt FACTCHECK seed. Score methodology: three binary judgments, mean = score. Re-verify model identities at audio lock. | — |
| 10 | B08 | §6.2: "someone who has just opened a letter from someone they have not heard from in years, or someone waiting by the phone for news they are dreading" | PASS | Verbatim confirmed in build prompt FACTCHECK seed against §6.2 other-minds probe examples. Re-verify at audio lock. | — |
| 11 | B08 | Ablation flattens third-person experience descriptions (Fig 26/84) | PASS | §6.2 / Fig 26 / Fig 84 confirmed in build prompt FACTCHECK seed. Effect is quantified, not anecdotal. Re-verify figure numbers at audio lock. | — |
| 12 | B10 | Coverage framing claims (Economist article) | EXEMPT | ⛔ ECON-VERIFY — no Economist claim ships until Bear reads saved article copy. B10 left panel is paraphrase-mode only; no masthead, no direct quote. Exempt from GATE F until ECON-VERIFY checklist below is completed. | Complete ECON-VERIFY checklist; upgrade B10 narration and B10_CoverageGap scene when verified. |
| 13 | B11 | Butlin et al. 2023 indicator-property framework; "one such empirical investigation" | PASS | §9.4 reference confirmed in build prompt FACTCHECK seed. Year, authors, and "one such empirical investigation" verbatim confirmed. Re-verify at audio lock. | — |
| 14 | B13 | Five verdict lines (all) | PASS | Each line traceable: lines 1–3 → §9.4 brackets; line 4 → §6.2/Fig 26 other-minds collapse; line 5 → §4/§3 (workspace not explicitly designed for; emerged from training). Editorial characterization in Teardown register — not paper quotes. | — |

## ECON-VERIFY checklist (required before B10 can name the Economist)

Before row 12 can move from EXEMPT to PASS and B10 can use named quotes:
1. Open Bear's saved Economist article copy.
2. Confirm the article names this paper as a source (check sources/references).
3. Note whether the §9.4 hedges appear in a subordinate clause.
4. Check for internal inconsistencies in indicator/theory/test counts (flagged in workspace-skeptical-read.md).
5. If verified: update B10 narration + B10_CoverageGap left panel to use named quotes; optionally add B10b for itemized inconsistencies; update row 12 verdict to PASS.

Until complete: **no Economist masthead, no direct quotes, paraphrase markers in B10_CoverageGap**.

## Audio-lock sign-off requirements

Before any beat's audio may be generated:
- Rows 2–6, 8–11, 13: re-verify verbatim quotes against corpus at audio lock.
- Row 7 (Fig 25A): Bear reads Fig 25A and signs off; B06 props.text updated if needed.
- Row 12: ECON-VERIFY checklist completed or B10 ships in paraphrase-mode permanently.
- Human signs GATE F: replace "SEED" with "GATE F SIGNED — [date] by [name]" above.
