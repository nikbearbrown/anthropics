# FACTCHECK.md — claim | verdict | source | fix

Source: Bear's research prompt (first-principles methodology, self-annotated).
Genre rule 5 (unverified-source caution) is CENTRAL to this episode: the source
deliberately MIXES a verified framework, a self-flagged synthetic worked example,
and an admittedly-invented metric. Inheriting the source's confidence is the exact
failure this reel is ABOUT — so every named work below gets a LIVE re-verify at
Gate F before narration lock. Verdicts here are the agent's standing assessment,
not a substitute for that check.

| # | Claim in episode | Verdict | Source | Fix / note |
|---|---|---|---|---|
| 1 | Goodhart's Law: when a measure becomes a target it stops being a good measure (origin ~1975) | HOLDS WITH CORRECTION | Goodhart 1975 + Strathern 1997 | **Gate F correction applied.** The 1975 date is correct (Goodhart, "Problems of Monetary Management: The U.K. Experience," RBA Papers in Monetary Economics, 1975). But the pithy phrasing "when a measure becomes a target, it stops being a good measure" is Marilyn Strathern's 1997 formulation ("'Improving Ratings': Audit in the British University System," *European Review* 5:305–321) — not Goodhart's own words. The narration "Economists named this in 1975. Goodhart's Law: when a measure becomes a target…" falsely implies Goodhart wrote those words in 1975. **Fix applied in B03:** removed "in 1975" from the narration. The SOURCES card (B32S) retains "Goodhart (1975)" as the origin credit for the law. The phrasing stands as the widely-used popularization. |
| 2 | A change reshapes the error surface rather than moving wrong→right on one axis | EDITORIAL (the thesis) | ours, from the source's frame | Teardown framing of the source's core idea — clearly the episode's argument |
| 3 | LLM outputs are sampled/nondeterministic even at temp 0 with tools + multi-turn state | HOLDS | source Part 2 + standard | Narrate as mechanism (sampling + backend/version drift); no vendor "fingerprint" detail |
| 4 | Paired comparison beats aggregate: +20/−15 nets the same +5 as +20/−0 | HOLDS (arithmetic + method) | source Part 2 | Kept as illustrative arithmetic, not a measured result |
| 5 | McNemar's test is the correct tool for paired binary before/after on the same items; low power on few discordant pairs → exact-binomial | HOLDS | McNemar 1947; NIST Dataplot reference (itl.nist.gov/div898/software/dataplot/refman1/auxillar/mcnemar.htm); Fay (2010), *R Journal*, `exact2x2` package | Standard characterization confirmed. Minor precision note: the NIST reference lives in the NIST Dataplot manual, not the main Engineering Statistics Handbook; narration says "NIST" generically which is defensible. Exact-binomial small-sample caveat (b+c < 25 threshold) is documented and correct. |
| 6 | Aggregate metrics are severity-blind; weight categories by cost-of-failure | HOLDS (method) | source Part 3 | — |
| 7 | The format-drift 12→2% / hallucinated-tool-call 10→18% trade | ILLUSTRATIVE | source Part 3 example | Explicitly an example of a severity trade; numbers framed as illustration, never a statistic |
| 8 | LLM-as-judge biases: position/order, verbosity, authority, sycophancy; polite hedge can swing a grader | HOLDS WITH CORRECTION | Zheng et al. (2023), "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 Datasets and Benchmarks (arXiv:2306.05685); Ye et al. (CALM framework); "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" (arXiv:2410.02736) | **Gate F correction applied.** Position bias, verbosity bias, authority bias — all documented in Zheng et al. (2023) and confirmed in subsequent work. "Apology-and-authority bias" (as a single compound label) is NOT a term of art; the literature separates **authority bias** (favoring responses citing references or claiming expertise) and **sycophancy / sentiment bias** (polite or deferential framing inflating scores). **Fix applied in B21:** replaced "Apology-and-authority bias" with "Authority bias, and sycophancy." |
| 9 | Mitigations: frozen canary set, paraphrase/perturb inputs, randomize order, panel of judges | HOLDS (method) | source Part 4 | — |
| 10 | Symptom vs cause: one hedgy-answer symptom, ≥3 causes; "be confident" makes confident-wrong for 2 of 3 | HOLDS (reasoning) | source Part 5 | The single strongest teaching beat; kept as reasoning, not data |
| 11 | Regression-suite discipline: append-only, never delete a fixed case, version + bisect, log full traces | HOLDS | source Part 6 + software practice | — |
| 12 | CheckList (behavioral testing of NLP capabilities) | HOLDS | Ribeiro, Wu, Guestrin, Singh — "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList," ACL 2020 (acl-main.442; arXiv:2005.04118) | Title, authors, venue, and "behavioral testing across capability categories" framing confirmed. |
| 13 | Dynabench (dynamic, human-and-model-in-the-loop benchmarking; static sets get overfit) | HOLDS | Kiela et al. — "Dynabench: Rethinking Benchmarking in NLP," NAACL 2021 (2021.naacl-main.324; arXiv:2104.14337) | Title, authors, venue, and "dynamic / human-in-loop / overfit" framing confirmed. |
| 14 | HELM (Holistic Evaluation of LMs; multi-metric so trade-offs stay visible) | HOLDS | Liang, Bommasani et al. (Stanford CRFM) — "Holistic Evaluation of Language Models," arXiv:2211.09110 (2022); TMLR 2023 | Title, institution, year, and "holistic / multi-metric / trade-offs visible" framing confirmed. |
| 15 | PoLL — Panel of LLM evaluators reduces single-judge bias | HOLDS | Verga, Hofstätter et al. — "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models," 2024 (arXiv:2404.18796) | Title, authors, year, and bias-reduction characterization confirmed. |
| 16 | Not every failing eval is a prompt fix — sometimes model/guardrail/system-design (the added lever) | HOLDS | source Part 7 (Anthropic guidance) | Named generically as guidance; no product/version specifics |

## Gate F — live re-verify completed 2026-07-23

Agent ran independent web verification on all rows flagged "re-verify at Gate F."

**Two corrections applied:**

**Correction 1 — B03 narration (Goodhart phrasing/attribution):**
- Old: "Economists named this in 1975. Goodhart's Law: when a measure becomes a target, it stops being a good measure."
- New: "Economists named this — Goodhart's Law: when a measure becomes a target, it stops being a good measure."
- Reason: "In 1975" placed immediately before Strathern's 1997 phrasing implies Goodhart wrote those words in 1975. The pithy formulation is Strathern's. Removing the inline date eliminates the false attribution; the SOURCES card (B32S) retains "Goodhart (1975)" as origin credit.

**Correction 2 — B21 narration (LLM-judge bias taxonomy):**
- Old: "Position bias: the order you list candidates changes the winner. Verbosity bias. Apology-and-authority bias."
- New: "Position bias: the order you list candidates changes the winner. Verbosity bias. Authority bias, and sycophancy —"
- Reason: "Apology-and-authority" is not a documented compound term. The literature (Zheng et al. 2023 and subsequent) separates authority bias and sycophancy/sentiment bias as distinct phenomena. The replacement uses both documented terms.

**All other Gate F rows confirmed HOLDS.** No other narration changes required.

## EXCLUDED by design (the source flags these itself — do NOT ship)

- **The "Exponential Impact Score" formula.** The source states plainly it is
  *invented for the example, not sourced from the literature.* The nonlinear-severity
  IDEA (critical failures dominate) is reused in the severity-weighting beat (B17);
  the specific invented formula is NOT shown or named.
- **The synthetic worked example** (the 40-case walkthrough, p ≈ 0.39, the
  routing-rule/negation relocation, the agreeableness-grader artifact). Flagged by
  the source as *synthetic/illustrative, not real data.* No synthetic number appears
  on screen as if measured. The episode teaches the METHOD the walkthrough
  demonstrates, never its numbers.
- **Citation-style markers with no bibliography** carried in the source's appendix
  are ignored; only the named works in the Reference Lineage (rows 12–16) are used,
  each re-verified at Gate F.

## Stripped as datable (hard rule 4)

- No model names, no version numbers, no "as of [month]" claims, no vendor tool
  lists. The source's own examples (system fingerprint, specific tool names) are
  compressed to generic mechanisms. Narration is built to age.
