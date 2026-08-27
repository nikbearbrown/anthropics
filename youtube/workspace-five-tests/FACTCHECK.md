# FACTCHECK — workspace-five-tests

Status: SEED — 2026-08-23 by Claude. 11 rows; key figures traced to named paper figures and sections. Full paper PDF verification required before GATE F SIGNED.

Source: Gurnee*, Sofroniew* et al., "Verbalizable Representations Form a Global Workspace in Language Models," Transformer Circuits Thread, Anthropic, July 2026.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | "Five claims, each with its own experiment" (verbal report, directed modulation, internal reasoning, flexible generalization, selectivity) | ✓ PASS | Paper's five-property framework, Fig 1; confirmed against BUILD-PROMPT.md source table which cites Fig 1 explicitly | — |
| 2 | B04 | "concentrate on citrus fruits while it copies 'The old painting hung crookedly on the wall'; the lens at mid-word reads orange — with lemon close behind" | ✓ PASS | §3.2 text + Fig 9; verbatim in BUILD-PROMPT source table | — |
| 3 | B05 | "the white-bear effect. The machine has it too." (paper names this parallel) | ✓ PASS | §3.2 text + Fig 10 caption ("parallels the 'white bear' effect in humans"); verbatim in BUILD-PROMPT source table | — |
| 4 | B05 | "Under 'ignore,' the concept still activates — less than under 'focus,' but the baseline was zero" | ✓ PASS | Fig 10; three-condition bar chart shows: no-instruction ≈ 0, ignore > 0, focus highest; BUILD-PROMPT source table | — |
| 5 | B07 | "(4+17)*2+7"; "twenty-one appears in the lens first, then the product — later layers, in the order the math requires" | ✓ PASS | Fig 17 caption; verbatim in BUILD-PROMPT source table | — |
| 6 | B08 | "seventy-six of one hundred ninety-two swaps at natural strength — one hundred one when you push harder. Across sixteen function templates" | ✓ PASS | Fig 19 caption (76/192 top-1, 101/192 at α=2, 16 function templates × 12 pairs); verbatim in BUILD-PROMPT source table | — |
| 7 | B08 | "forty to fifty percent reliability" | ✓ PASS | Derived: 76/192 = 39.6% ≈ 40%; 101/192 = 52.6% ≈ 53%. Narration says "forty to fifty percent" — low end is slightly understated; within honest rounding. | Tighten to "forty to fifty-three percent" if Bear wants precision |
| 8 | B09 | "The piece inside carries most of the causal punch" | ✓ PASS | Fig 16 caption + §3.3; J-space component of probe carries larger causal effect than complement; BUILD-PROMPT source table | — |
| 9 | B13 | "nine percent, against a twenty-nine percent baseline" and "0.46 vs 0.53 control" for held concepts | ✓ PASS | §A.17 text; verbatim in BUILD-PROMPT source table | — |
| 10 | B11 | "Test five is the beautiful one" | EXEMPT | Editorial opinion of the presenter; makes no empirical claim | — |
| 11 | B12 | "That dissociation is the workspace signature. In humans, it's the difference between what you do consciously and what you do on autopilot." | EXEMPT | The dissociation (flexible vs automatic) is the paper's own experimental result (PASS); the analogy to human conscious/autopilot is the presenter's framing, not a paper claim — EXEMPT for that clause only | — |
