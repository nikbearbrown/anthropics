# Chapter 25 — Case: BrandArchetype


## TL;DR

- Soft-label expert annotation of Jungian brand archetypes — testing whether supervised classification beats zero-shot LLM extraction.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Soft-label expert annotation of Jungian brand archetypes — testing whether supervised classification beats zero-shot LLM extraction.*

**Authors:** Abisha Vadukoot, Nina Harris, Nik Bear Brown
**Editor:** Nik Bear Brown

*This case documents a proposal-stage system. Annotation by Nina Harris is in progress; preliminary classifier benchmarks are reported below as an early read, not a finished result. Outcomes report targets where measurements are not yet available.*

---

## 1. Question

A Jungian brand archetype is a contested construct. Mark and Pearson's twelve categories — Sage, Hero, Lover, Outlaw, Magician, Innocent, Explorer, Caregiver, Ruler, Creator, Jester, Everyman — are working vocabulary in brand strategy practice, but practitioners routinely describe brands as blends ("70% Creator, 30% Magician"), and trained experts disagree at the edges. Treating archetype as a single categorical label discards information experts actually have.

BrandArchetype operationalizes the construct as a *soft probability distribution over the twelve archetypes, with say/do divergence stratification* — companies whose stated narrative diverges from their behavioral record are tagged in a separate evidence tier so the disagreement is preserved rather than smoothed away. The inferential question: does a classifier supervised on expert narrative labels recover archetype distributions from behavioral text more stably than a zero-shot LLM does?

This is a variable-identification problem (Chapter 13), not a confounding-adjustment problem (Chapter 3). The question is whether the expert label carries information beyond what an unsupervised reader of behavioral text can extract on its own.

## 2. Causal diagram

The latent-variable structure is:

```
        A  (latent archetype distribution, soft over 12 classes)
       / \
      /   \
     v     v
     N     T
     |     |
     |     v
     |     Ŷ  (classifier prediction)
     v
   (used as supervision)
```

Read the arrows. *A* is the unobserved archetype distribution for a company. *N* is Nina Harris's expert annotation — a noisy reading of *A* through the lens of corporate narrative material (annual reports, CEO letters, brand guidelines). *T* is behavioral text — the company's marketing and communication corpus, drawn here from SEC filings, earnings calls, regulatory filings, and verified news archives. *T* is a separate noisy reading of the same latent *A*. *Ŷ* is the classifier output, produced from *T*.

The supervised classifiers learn the mapping (T, N) → Ŷ: they see behavioral text paired with expert narrative labels during training and learn to predict *A*'s distribution from *T* alone at test time. The zero-shot model receives only *T* and the twelve archetype definitions; it never sees *N*. Whatever it knows about archetypes comes from its pretraining corpus, which plausibly already contains marketing-textbook analyses of well-known brands.

That last point is central to the design. If a zero-shot LLM and a supervised classifier produce similar outputs, we cannot tell whether the LLM has independently identified *A* or whether it has memorized published consensus about the same companies.

## 3. Identification strategy

Three classifiers are evaluated on the same held-out companies:

- **TF-IDF + SVM.** Bag-of-words features, linear classifier. Cheap, interpretable, fixed vocabulary. Establishes whether surface lexical signal is enough.
- **Zero-shot Claude Haiku.** Prompted with the twelve archetype definitions and the behavioral text. No training examples. Reads *T*, returns a soft distribution.
- **Fine-tuned DeBERTa.** Trained on (T, N) pairs to predict the soft expert distribution by minimizing cross-entropy against Harris's labels.

The identification claim has a clean shape. If the supervised models beat zero-shot on out-of-sample companies, the expert label *N* carries information the LLM does not extract from *T* alone — meaning the human annotation is not redundant with what pretraining already knows. If zero-shot wins, either *N* is redundant or the supervised models are starved.

Here is the limit, stated plainly. At the current dataset size — 100 companies, expert annotation in progress — DeBERTa fine-tuning collapses to zero accuracy. A 100-million-parameter model cannot be meaningfully trained on 100 examples without catastrophic overfitting. This is a sample-size constraint, not a methodological failure of the design. The V1 PDF reports it as expected and uses it to motivate a frozen-encoder + lightweight head architecture for the final run.

The say/do divergence stratification matters here. Tier 3 companies are pre-selected for documented gaps between narrative identity and behavioral record — regulatory actions, greenwashing determinations, investigative journalism. The classifier is shown these disagreements as labeled examples rather than asked to discover them. Whether the supervised model captures the divergence pattern (narrative archetype paired with the corresponding *shadow* archetype in behavior — Caregiver/Enabler, Ruler/Tyrant, Magician/Manipulator) is the central downstream test.

## 4. Results

Preliminary numbers, from the V1 manuscript:

- **Zero-shot Claude Haiku:** 77.8% top-1 accuracy, Macro F1 0.75 — the strongest preliminary classifier on the partial annotation set.
- **DeBERTa fine-tuned:** 0.0% accuracy, Macro F1 0.00. McNemar's test against zero-shot Haiku returned p = 0.023; the gap is statistically significant at this preliminary stage.
- **TF-IDF logistic regression:** intermediate accuracy. Surface lexical features carry some archetype signal but cannot capture rhetorical pattern.

Targets the project would need to publish as a finished case:

- Per-archetype precision and recall on the full-annotation held-out test set, after Harris's labels are complete.
- Calibration of the soft probability distributions — Brier score and expected calibration error against the expert distributions.
- Stability under perturbation of the behavioral-text input (paraphrase invariance test): does the classifier's distribution shift when *T* is rewritten without changing meaning?

The headline question — does supervised soft-label classification beat zero-shot prompting on behavioral text? — is *not* answered by the preliminary numbers. Zero-shot wins early, on narrative text the LLM has plausibly seen analyses of in pretraining. Whether it still wins on behavioral text, against a properly architected supervised model with full expert annotation, is the open question this case is designed to resolve.

## 5. Sensitivity and limitations

The named failure mode is **expert-annotation noise**. With a single senior annotator, inter-rater reliability has no floor measurement at all; any classifier trained on Harris's labels learns Harris's house style alongside the construct. The V1 paper names a second senior strategist from a different agency lineage as the highest-priority extension, with Krippendorff's alpha as the planned reliability metric.

Three additional limits:

- **Sample size.** N = 100 cannot support a 100M-parameter fine-tune. The frozen-encoder design is the response, but subgroup analysis by industry, confidence tier, or archetype is not yet supported.
- **Selection bias.** Interbrand Best Global Brands 2025 selects for large, mature, market-leading firms with consistent brand voice. Findings will not transfer cleanly to startups, B2B firms, or non-Western brands without re-annotation.
- **Construct contestability.** The Mark-and-Pearson framework is itself disputed in marketing scholarship. The case takes it as a working construct and does not defend it against alternatives.

## 6. Theory connection

Pairs with **Chapter 13, *LLM Causal Variable Identification***. The expert label is the variable-identification step: a credentialed human pins down what the latent construct means in this corpus. The classifier benchmark is the test of whether that identification carries information beyond what an unsupervised LLM extracts on its own.

## 7. Transfer prompt

If you wanted to test whether expert labels in your domain add value over zero-shot LLM extraction, what dataset size would you need to support a real fine-tune, and what cheaper architecture would you fall back to if you cannot reach it? What disagreement-among-experts structure would you preserve in your labels rather than smoothing away? How would you tell whether your fine-tuned model is learning the construct or learning the labelers?

---

**Tags:** brand-archetype, soft-labels, latent-variable-identification, zero-shot-comparison, expert-annotation, Jungian-archetypes, narrative-vs-behavioral-text, INFO-7390-spring-2026

---

## A note about AI

The brand-archetype case treats brand effects as a causal question. Brand effects are particularly hard to identify because the treatment (brand exposure) is hard to randomize and the outcome (consumer behavior) is hard to attribute.

Where the model genuinely helps: producing candidate operationalizations of brand archetype and naming the measurement challenges for each.

Where the model does damage: declaring that a specific archetype causes a specific consumer response. The causal claim requires evidence the marketing literature is still working out.

The rule: operationalization from the model; the causal claim from the experimental record.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Carolyn Heinrich** has spent her career on causal evaluation of social programs — including welfare-to-work and education interventions — using observational data when randomization isn't feasible. Her work models how to identify variables that genuinely drive outcomes in messy programs.

**Run this:**

```
Who is Carolyn Heinrich, and how does her work on causal program evaluation connect to the variable-identification case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Carolyn Heinrich"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one specific welfare-to-work evaluation Heinrich led — what variables mattered, what didn't.
- Ask it to compare Heinrich's observational methods with the RCT-based evaluation Esther Duflo would run.

What changes? What gets better? What gets worse?
