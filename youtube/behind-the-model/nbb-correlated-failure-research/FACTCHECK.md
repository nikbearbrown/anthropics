# FACTCHECK — nbb-correlated-failure-research

Status: **GATE F SIGNED — 2026-07-31 by Codex. 4 rows, all PASS.**

The NBB wrapper reuses the locked body. Claims were checked against the ensemble
derivation in Bishop and the primary LLM-as-judge evaluation paper.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | NBB00–B04 | Cross-checking reduces error when checker errors are independent; shared failure modes create correlated error. | ✓ PASS | Christopher M. Bishop, *Pattern Recognition and Machine Learning*, §14.2 “Committees”; for two independent checkers with marginal error \(p\), the joint-error term is \(p^2\), whereas perfectly correlated errors retain joint error \(p\). | — |
| 2 | B01–B03 | LLM judges exhibit position bias, verbosity bias, and self-enhancement bias. | ✓ PASS | Zheng et al., “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” NeurIPS 2023, arXiv:2306.05685, §§4.2–4.4. | — |
| 3 | B05–B06 | Reversing answer order is a valid reproducibility test for position bias. | ✓ PASS | Zheng et al., arXiv:2306.05685, position-consistency protocol compares judgments after swapping answer order. | — |
| 4 | B07–NBB01 | Retrieval, executable math, schema validation, and domain review provide structurally different checks from another unconstrained LLM judgment. | ✓ PASS | Engineering derivation: each named checker evaluates a different artifact contract—source match, executable result, schema conformance, or expert-domain acceptance—rather than sampling another free-form model verdict. | — |
