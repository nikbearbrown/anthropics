# Chapter 24 — Case: Supply Chain Risk Monitor


## TL;DR

- Multi-agent risk scoring with bear / bull / geopolitical analysts and a citation-grounded guardrail.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Multi-agent risk scoring with bear / bull / geopolitical analysts and a citation-grounded guardrail.*

**Author:** [TBD — pending attribution] [verify]
**Editor:** Nik Bear Brown

*This case documents a proposal-stage system. The architecture is built; the load-bearing measurements (precision, recall, end-to-end accuracy on real filings) are the next step. Outcomes below report targets, not measured results.*

---

## 1. Question

Is a given firm at elevated short-term supply-chain risk, given the public evidence available today? The Supply Chain Risk Monitor frames this as a multi-agent reasoning problem: each analyst agent is a noisy judgment process, and the system asks whether the combination of those processes can estimate a latent risk state the individual agents cannot.

The inputs are three document streams. SEC EDGAR 10-K filings supply the firm's own disclosures — Apple's 2025 10-K is the sample document the project is wired against. A curated set of five RSS feeds supplies ongoing trade and logistics coverage. NewsAPI supplies broader headline flow. All three are embedded with `text-embedding-3-small` and stored in Pinecone for retrieval.

What is being claimed is structural. The architecture says that stance-prompted agents reading shared evidence, aggregated by a JSON-scoring judge and filtered by a citation guardrail, can produce a calibrated 0–100 risk score. Whether that claim survives contact with held-out shocks is the next experiment, not this chapter.

## 2. Causal diagram

The system is a directed graph. Let R be the latent short-term supply-chain risk state of the firm. R is unobserved. The three analyst agents — bear, bull, geopolitical — each produce a noisy stance-conditioned estimate: Ê_bear, Ê_bull, Ê_geo. The judge node J reads all three and outputs a structured JSON score on a 0–100 scale. The guardrail G reads J's output plus the retrieved Pinecone documents and emits a trust score and hallucination flags. The final reported value Y is G's filtered version of J.

In arrow form:

```
R --> Ê_bear --> J --> G --> Y
R --> Ê_bull -----^
R --> Ê_geo  -----^
```

But this diagram is incomplete. The three analysts do not read R directly. They read a shared retrieval D, drawn from EDGAR + RSS + NewsAPI through Pinecone:

```
D --> Ê_bear, Ê_bull, Ê_geo
```

D sits upstream as a confounder of analyst errors. When D is missing a signal, all three analysts are missing the same signal. When D contains a misleading article, all three read it. The errors in Ê_bear, Ê_bull, Ê_geo are therefore not independent given R — they are correlated through D. This is the central structural feature the rest of the chapter explains.

## 3. Identification strategy

The strategy is multi-perspective ensembling with a falsifiability layer. Each GPT-4o analyst is prompted with a different stance: the bear looks for downside signals, the bull looks for resilience, the geopolitical agent looks for state-actor and trade-policy exposure. The same retrieved evidence is read three ways. The judge node aggregates the three readings into a single JSON object containing an integer `risk_score` between 0 and 100, weighted by the judge's own assessment of which analyst's reading the evidence supports.

The guardrail layers a separate check. It compares each claim in the judge's output against the retrieved Pinecone documents, scores citation grounding, and emits hallucination flags when a central claim has no document support. The guardrail's report is a structured dict, not free text, so downstream code can act on it.

The identifying assumption is conditional independence: given R, the three analysts produce errors that are at least partially independent. Stance prompting is supposed to manufacture that independence — a bear and a bull reading the same paragraph should disagree where the evidence is genuinely ambiguous. The assumption breaks when the evidence is unambiguous in a misleading direction. If D contains a confidently stated claim that is wrong, all three stance-prompted agents will read it, all three will incorporate it, and the judge will see three-way agreement that looks like signal but is shared misreading. The guardrail's citation check is the single remaining safeguard. The choice of `text-embedding-3-small` over a heavier model is a cost decision — RAG-grounded citation is the falsifiability lever, not embedding fidelity.

## 4. Results

The Day 1 scaffold is wired end-to-end. Every named file in the project log was built and is importable. The Postgres DDL applies cleanly. The GitHub Actions deploy pipeline targets Cloud Run. The judge returns a typed JSON object with an integer risk score; the guardrail returns a typed dict with trust and hallucination fields. Seven pre-review bugs were caught and fixed.

What is not yet measured: precision and recall against historical disruption events; rate at which the guardrail catches hallucinated citations; analyst-disagreement variance and whether it correlates with subsequent disruption. To ship as a published case, the project would need three target metrics:

- Per-firm precision and recall on a labelled set of 50 historical supply-chain disruption events, with the labels assigned before the system sees the firm.
- Hallucination-flag rate from the guardrail, validated by hand on a sample of 100 judge outputs.
- Analyst-disagreement variance — the spread among Ê_bear, Ê_bull, Ê_geo — checked for correlation with disruption events that occurred in the 30 days following each run.

None of these numbers exist yet. They are the next experiment.

## 5. Sensitivity and limitations

The named failure mode is **shared-mode confabulation**. When all three stance-prompted agents converge on a reading the underlying documents do not support, the ensemble produces a high-confidence wrong answer, the judge sees consensus, and only the guardrail's citation check stands between the system and a false report. The guardrail can detect the failure when the unsupported claim is specific enough to fail a citation lookup. It cannot detect the failure when the shared misreading is interpretive — when all three agents read a real document the same wrong way.

Three structural pressures push toward this mode. NewsAPI returns headlines and snippets, not full articles, so citation grounding can succeed against a headline that does not contain the claim. RSS feed quality varies — five curated feeds is a small sample with uneven editorial standards. The Pinecone index has no automatic staleness eviction, so a document indexed weeks ago can dominate retrieval after its content has been overtaken. CrewAI patterns evolve quickly; the AGENTS.md file warns that today's patterns may not hold in six months.

## 6. Theory connection

This case pairs with **Chapter 14 — Causal Agents**. The Supply Chain Risk Monitor is the agent-graph that chapter develops: stance-prompted reasoners as parallel noisy estimators of a latent state, a judge node as aggregator, a guardrail as falsifier. The shared retrieval D is the confounder Chapter 14 names as the dominant threat to ensemble validity.

## 7. Transfer prompt

If you build a multi-agent system for a judgment task, what evidence would distinguish your agents producing independent errors from your agents sharing a confabulation? What document would your guardrail need access to in order to detect the shared error? At what point does the answer to that question force you to re-architect rather than re-prompt?

---

## A note about AI

Supply-chain risk agents reason about cascading failures across networks. The cascade is the place the model's pattern recognition both helps and misleads.

Where the model genuinely helps: surfacing the canonical cascading-failure modes from documented historical cases.

Where the model does damage: predicting which cascades will occur in your specific supply chain. Predictions depend on relationships among your suppliers, your inventory positions, and your alternatives — none of which the model has.

The rule: historical cascade patterns from the model; the specific risk assessment from someone with your supplier list.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Hal Varian** built much of modern applied economic analysis at Google as Chief Economist — including the use of causal reasoning in product, pricing, and supply-chain decisions. His 2014 paper "Big Data: New Tricks for Econometrics" bridged classical causal inference and ML.

**Run this:**

```
Who is Hal Varian, and how does his work bringing causal analysis into industrial supply chains connect to the case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hal Varian"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Varian's framework to one specific supply-chain risk decision — what causal estimates would inform it?
- Ask it about Varian's earlier textbook *Intermediate Microeconomics* and what it teaches that more advanced texts skip.

What changes? What gets better? What gets worse?
