# Chapter 21 — Case: Aegis


## TL;DR

- Cost-aware LLM routing with a Pearl Rung-2 hallucination test — do(phrasing) as a runtime reliability signal.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Cost-aware LLM routing with a Pearl Rung-2 hallucination test — do(phrasing) as a runtime reliability signal.*

**Author:** Nilay Raut
**Editor:** Nik Bear Brown

---

## 1. Question

Production LLM systems face a quiet failure: the model returns a confident, fluent answer that is wrong, and there is no ground-truth knowledge base to check it against. The standard responses are a curated fact store (expensive, domain-specific) or self-consistency sampling (slow, costs more tokens). Both treat hallucination as something to look up.

Raut reframes the problem as causal. A grounded answer should be anchored to what the user means, not to the literal characters of what the user typed. So the question becomes: *under intervention on the surface form of the prompt — paraphrase the question while preserving the intent — does the model's response remain invariant?* If yes, the response is being driven by something beyond the wording; if no, the response is being driven by the wording itself, which is the signature of a model pattern-matching its way to a confident sentence.

This is a Pearl Rung-2 question. Rung 1 would ask whether hedging language correlates with hallucinations. Rung 2 sets the surface form by intervention — *do(phrasing = q′)* — and looks at how the response moves.

## 2. Causal diagram

Four nodes. *Latent intent* `I` is what the user actually wants to know. *Surface form* `S` is the literal string they typed (or its paraphrase). *Model knowledge* `K` is whatever the trained weights have stored about the intent. *Response* `R` is what comes out.

In arrow form:

`I → S` (the user's intent generates a surface form)
`I → R` (intent should drive the response when the model is grounded)
`K → R` (model knowledge feeds the response)
`S → R` (surface form *should not* drive the response when the model is grounded — if this edge is strong, the model is doing surface pattern-matching)

The intervention `do(S = q′)` cuts the incoming arrow to `S` from `I` and sets `S` by hand. `I` is held fixed by the construction of `q′` — the paraphrase preserves intent. `K` is held fixed by holding the model fixed. So a change in `R` under `do(S)` can only travel along `S → R`. If `R` is invariant across paraphrases, the path `I → R` and `K → R` are doing the work — the response is grounded. If `R` swings, the path `S → R` is doing the work — the model is keying on phrasing, which is what hallucination looks like in this DAG.

The hedging-phrase scan that runs in parallel is a Rung-1 quantity: a correlation between linguistic uncertainty markers and hallucination labels. It is fast and useful, but it cannot separate `S → R` from `I → R`.

## 3. Identification strategy

The intervention is implemented by paraphrase. For an incoming prompt `p`, Aegis generates two paraphrases `q₁, q₂` with `gpt-4o-mini` at temperature 0.7, with a system prompt instructing the model to preserve semantic content while varying sentence structure. The routing model then answers `q₁` and `q₂` at temperature 0 — temperature is dropped to zero on the response side specifically to remove sampling variance from the response and isolate the prompt-surface effect. The two responses are embedded with `all-MiniLM-L6-v2`, and the variance signal is `ν = 1 − s̄`, where `s̄` is the mean pairwise cosine similarity of the response embeddings. A response inconsistent with the model's own answer to a paraphrased prompt — `ν > θ` — is flagged.

The deployed threshold is `θ = 0.35`. The PDF reports that factual-grounded queries cluster below variance 0.20 and hallucination-prone queries above 0.40; θ is placed in the upper half of that gap to bias toward precision over recall.

The load-bearing assumption is that the paraphrase preserves `I`. Everything in the identification rests on this. If the paraphrase model swaps a real entity for a near-synonym, or rewrites a precise factual question into a slightly different one, then `do(S = q′)` has not held `I` fixed — and the variance the test sees is no longer cleanly attributable to `S → R`. This is where sensitivity analysis should focus, not on the threshold.

The Tier-1 hedging-phrase scan runs in parallel as a Rung-1 baseline. It counts hedging tokens against a fixed list of 25 markers and assigns a confidence based on the count. It is essentially free, runs in under a millisecond, and catches the loudest cases. It is also weaker: it cannot detect a confident hallucination and cannot separate model uncertainty from polite hedging.

## 4. Results

On a 50-record synthetic workload, Aegis estimates a 40–60% cost reduction relative to a GPT-4o-only baseline. On a 30-sample labeled evaluation set — 15 factual queries, 15 hallucination-prone — the combined detector achieves precision 0.82, recall 0.60, F1 0.69 at θ = 0.35. The test suite reports 57 of 57 unit and integration tests passing. The system is deployed with the FastAPI backend on Render and the React dashboard on Vercel.

Two things to name. The 30-sample evaluation set is small — Wilson-score 95% confidence intervals on F1 at n = 30 span roughly ±0.18, which the PDF itself acknowledges, and this is not enough to make a confident claim about general LLM hallucination detection. Recall is 0.60: the detector misses two of every five hallucination-prone prompts in the labeled set, mostly cases where the model refused to confabulate and answered consistently across paraphrases. The cost-reduction figure is computed against a synthetic 50-record workload, not deployed production traffic.

## 5. Sensitivity and limitations

The named failure mode is paraphrase-LLM intent leakage. The paraphrase step is itself an LLM operation, and a paraphrase model that fails to preserve `I` injects intent variation into the test. Whatever variance shows up downstream is then ambiguous: it might be `S → R` (the signal we want), or it might be the paraphrase model having quietly changed the question. The identifying assumption fails silently, and the detector's specificity degrades.

The 30-sample labeled set is too small to support general claims about hallucination detection in LLMs. The cost figure is computed on a 50-record synthetic seed workload; production traffic mixes vary, and the savings on a real workload could be higher or lower. The Tier-1 hedging-phrase scan is a heuristic — it will systematically penalize careful, correct responses that hedge for legitimate reasons (a doctor's "this is uncertain" gets flagged the same as a confabulator's "I think"). The semantic cache is in-memory and resets on server restart. The PDF reports two false positives on stable factual answers ("Newton's first law", `E = mc²`) where paraphrase variants produced non-identical but semantically equivalent phrasings; a semantic entailment check would resolve those.

## 6. Theory connection

This case pairs with Chapter 10, *LLMs and Causal Reasoning*. The paraphrase intervention is a Pearl Rung-2 operation — `do(surface form)` — applied to the LLM's input to test whether the response is causally grounded in user intent or is being driven by phrasing. The same chapter's specification move applies here: "hallucination" is replaced with the precise quantity Aegis actually measures, which is *response inconsistency under semantic-preserving paraphrase intervention*.

## 7. Transfer prompt

If you wanted to test whether your own LLM-driven product is hallucinating, what intervention on the input could you run that holds the user's intent fixed? What signal would tell you the response is invariant under that intervention — and how confident are you that your intent-preserving check actually preserves intent? If the answer is "we trust the paraphrase model," what would change your mind?

---

*Still puzzling:* whether the paraphrase model's intent-preservation can itself be audited at runtime, or whether it has to be taken on faith every request.

---

## A note about AI

LLM-Aegis routing is a case where the model is both the subject and the analyst. The conflict of interest is structural.

Where the model genuinely helps: laying out the routing decision problem in causal language — treatments (route choices), outcomes (downstream quality), confounders (query difficulty, user characteristics).

Where the model does damage: evaluating its own routing performance. The model has a stake in being used in the configuration that performs well, which biases the evaluation it produces.

The rule: causal framework from the model; the evaluation from an independent test harness that the model did not design.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Cynthia Dwork** built the mathematical foundation of differential privacy — a framework that lets you reason rigorously about what an algorithm reveals about its inputs. Modern LLM routing and access-control systems use her formalism for guaranteeing data protection.

**Run this:**

```
Who is Cynthia Dwork, and how does her work on differential privacy connect to the LLM routing case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Cynthia Dwork"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain how the epsilon parameter in differential privacy quantifies the privacy-utility tradeoff.
- Ask it about Dwork's later work on fairness in machine learning algorithms.

What changes? What gets better? What gets worse?
