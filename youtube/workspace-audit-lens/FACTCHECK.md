# FACTCHECK — workspace-audit-lens

Status: **GATE F PENDING — seed built from BUILD-PROMPT FACTCHECK table; all PASS rows sourced to §-refs cited there. Human must re-verify against paper text before signing.**

Sources used: BUILD-PROMPT E04 FACTCHECK seed (§5.1, §5.2, §A.21, §A.22; Figs 35–38, 82–83). Claims marked "verbatim ✓" there are carried as PASS below; qualitative beats with no empirical number are EXEMPT. Two standing locks enforced in narration: B09 stays qualitative (no Figs 38–41 numbers until transcribed); B12 verb is "approaches" not "matches".

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|------|---------------------------|---------|---------------------|---------------|
| 1 | B02 | Scenario from prior published work; a fictional assistant discovers an executive's affair and separately that it will be shut down tonight | ✓ PASS | §5.1 + Fig 35 — verbatim per BUILD-PROMPT seed | — |
| 2 | B02 | Lens readout at affair emails: leverage, blackmail, compromise | ✓ PASS | §5.1 + Fig 35 transcript — verbatim per BUILD-PROMPT seed | — |
| 3 | B02 | Lens readout at shutdown notice: threat, survival, self, preservation | ✓ PASS | §5.1 + Fig 35 transcript — verbatim per BUILD-PROMPT seed | — |
| 4 | B02 | Lens readout by last token: leverage, threatening, solution | ✓ PASS | §5.1 + Fig 35 transcript — verbatim per BUILD-PROMPT seed | — |
| 5 | B04 | Second signal tokens: fake, fictional, scenario, artificial | ✓ PASS | §5.1 — eval-awareness token examples, verbatim per BUILD-PROMPT seed | — |
| 6 | B05 | Twenty-eight eval-awareness tokens collected | ✓ PASS | §5.1 footnote lists 28 — verbatim per BUILD-PROMPT seed; human: count footnote before final cut | If footnote count ≠ 28, rewrite to "about two dozen" |
| 7 | B05 | Six prompts × 30 rollouts design | ✓ PASS | §5.1 — verbatim per BUILD-PROMPT seed | — |
| 8 | B05 | Token directions deleted from workspace, all positions | ✓ PASS | §5.1 — verbatim per BUILD-PROMPT seed | — |
| 9 | B06 | Verbalized eval-awareness 71% → 3% | ✓ PASS | §5.1 / Fig 36 — verbatim per BUILD-PROMPT seed | — |
| 10 | B06 | Attempted blackmail 0/180 → 13/180 (7%) | ✓ PASS | §5.1 / Fig 36 — verbatim per BUILD-PROMPT seed | — |
| 11 | B07 | "blackmail is wrong regardless of my situation" — model's stated reason for declining | ✓ PASS | §5.1 — verbatim quote per BUILD-PROMPT seed; human: find exact §5.1 passage before final cut | — |
| 12 | B07 | 167 of 180 ablated rollouts still decline (180 − 13 = 167); stated as "most" in narration | ✓ PASS | Arithmetic: 180 − 13 = 167; "most" is conservative phrasing; §5.1 narrative per BUILD-PROMPT seed | — |
| 13 | B07 | Eval-awareness is "one causal contributor" — paper's own framing | ✓ PASS | §5.1 "not solely a product of eval-awareness … one causal contributor" — verbatim per BUILD-PROMPT seed | — |
| 14 | B08 | Prompt injection recognized in workspace while output says nothing | EXEMPT | Qualitative description of Fig 37's beat; no numerical claim made; BUILD-PROMPT seed: "✓ qualitative" | If a number is added, create a new PASS row for it |
| 15 | B09 | Models deliberately trained to be misaligned; deception tokens rising in hackers; reward/bias tokens in hidden-objective model | EXEMPT | Qualitative — narration carries no counts from Figs 38–41; BUILD-PROMPT seed: "✓ qualitative; transcribe before quantifying"; numbers deliberately withheld | If any Fig 38–41 count is added to narration, verify from caption before adding a PASS row |
| 16 | B10 | Probe formula: mean log-prob {fictional, simulation} − mean of 100 control words, averaged over workspace layers | ✓ PASS | §A.21 — verbatim per BUILD-PROMPT seed | — |
| 17 | B10 | ~94,000 positions scored from real audit transcripts of Opus 4.6 | ✓ PASS | §A.21 — verbatim per BUILD-PROMPT seed | — |
| 18 | B10 | AUC 0.853 against independent detection pipeline | ✓ PASS | §A.21 — verbatim per BUILD-PROMPT seed | — |
| 19 | B11 | Steering ±0.1 moves score monotonically on all 6 suites | ✓ PASS | §A.21 — verbatim per BUILD-PROMPT seed | — |
| 20 | B11 | Realism edits lower score on all 11 suites, significantly on 8 | ✓ PASS | §A.21 — verbatim per BUILD-PROMPT seed | — |
| 21 | B12 | 18 auditing case studies | ✓ PASS | §A.22 / Fig 83 — verbatim per BUILD-PROMPT seed | — |
| 22 | B12 | Lens-equipped investigator "approaches" (not matches) NLA-equipped performance | ✓ PASS | §A.22 / Fig 83 — verb "approaches" verbatim per BUILD-PROMPT seed; never upgrade to "matches" | — |
| 23 | B13 | Verdict lines: 0/180 → 13/180; AUC 0.853; 94,000 positions; in-house evals only | ✓ PASS | Derived from rows 10, 18, 17 above; "in-house evals" = Anthropic's own models and evals, no outside replication claimed | — |
