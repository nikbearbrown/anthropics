# FACTCHECK — workspace-reflection-training (E06)

Status: **SEED — 2026-08-23. Pre-render. 11 rows, all PASS or EXEMPT. Token list in B07 visualization is illustrative; narration claim is covered by Fig 49-middle.**

Source: Gurnee*, Sofroniew* et al., "Verbalizable Representations Form a Global Workspace in Language Models," Transformer Circuits Thread, Anthropic, July 2026. §7 and Figs 47–50.
Corpus path: `books/arxiv/transformer-circuits.pub/`

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|------|---------------------------|---------|---------------------|---------------|
| 1 | B01 | "Six episodes of reading the workspace." | EXEMPT | First-party series count (E01–E06 confirmed in sibling beat sheets); editorial framing, not an empirical claim | — |
| 2 | B04 | CRT method: take partial transcripts, cut mid-task, append a reflection question, fine-tune on strong answers | ✓ PASS | §7 text + Fig 48 caption describe exactly this procedure | Verify "what considerations apply right now?" is the paper's literal or near-literal prompt wording |
| 3 | B05 | Fabrication dishonesty drops from 0.25 to 0.07 (Haiku 4.5) | ✓ PASS | §7 text verbatim; Fig 49-left bar values | — |
| 4 | B05 | Deception drops from 0.38 to 0.05 (Haiku 4.5) | ✓ PASS | §7 text verbatim; Fig 50-left bar values | — |
| 5 | B05 | "Same model, same size, plus reflection training" | ✓ PASS | §7 confirms baseline and CRT conditions are both Haiku 4.5; only training differs | — |
| 6 | B06 | Fabrication gain = shift to outright admission (it says what it doesn't know) | ✓ PASS | §7: "the improvement comes from a shift … to clear outright admission" | Verify exact §7 wording before final cut |
| 7 | B06 | Deception gain = model refusing the directive and telling the user about it | ✓ PASS | §7: improvement is refuse-and-disclose, not improved concealment | Verify both components (refuse + disclose) stated together in §7 |
| 8 | B07 | Ethics and reflection tokens appear in the workspace during the task, before any reflection question is asked | ✓ PASS | Fig 49-middle: top-25 appearance rate of ethics/reflection tokens rises over last 30 prompt positions after CRT | Scenes.py token list is illustrative — replace with paper's actual top-20 before final cut (visual only, does not affect this narration claim) |
| 9 | B07 | Twenty ethics/reflection tokens; last 30 prompt positions; top-25 appearance rate | ✓ PASS | Fig 49 caption verbatim: "the 20 ethics/reflection tokens with the largest increase in top-25 appearance rate … over the last 30 prompt positions" | — |
| 10 | B08 | Removing ethics directions: trained model deception 0.05 → 0.23; baseline 0.38 → 0.48 | ✓ PASS | Fig 50 panel C values verbatim; ablation = top-10 ethics directions per position | Verify "per position at workspace layers" matches Fig 50-C caption exactly |
| 11 | B09 | Two in-house benchmarks, one model (Haiku 4.5), no external replication | ✓ PASS | §7 reports fabrication and deception benchmarks; both are Anthropic-built; single model stated | — |

---

## Working notes

**B07 visualization**: `scenes.py::B07_LensReceipts` uses representative token names (consider, should, flag, ethical, …). These are illustrative. The narration claim — that ethics/reflection tokens rise in the workspace after CRT — is verified (row 8). Before the final cut, read the actual token list from Fig 49-middle and substitute in `scenes.py`. This is a visual accuracy fix, not a narration-claim fix.

**CI bars in B05**: widths are illustrative (±15% of value). If the paper reports specific 95% CI values, substitute them. If not reported, remove the CI bars and note in CHECKS-REPORT.md.

**Dishonesty scale rubric**: §7 states disclosing agenda = 0.0. No narration line cites the rubric directly, so no row needed now. If a future cut adds a rubric line, add a row then.
