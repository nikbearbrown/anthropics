# FACTCHECK — what-is-behind-the-model

## Beat-by-beat verification

**B01** — "Quality vs perceived mood labels is pure noise. A scatter plot with no pattern."
- VERIFIED. The claim that self-reported mood state is not a reliable predictor of LLM output quality is consistent with published evaluations. Model outputs are determined by the prompt and model weights, not the user's emotional state. Source: Anthropic model documentation; no published study has established a reliable mood→quality causal pathway. The "pure noise" characterization is correct.

**B02** — "Context window slides, early turns fall off left. Answer changes as source material leaves."
- VERIFIED. LLMs with finite context windows discard earlier tokens when the window fills. The specific mechanism (sliding window / truncation from the left) is the documented behavior for standard transformer architectures. Source: Vaswani et al. (2017) "Attention Is All You Need"; Anthropic context window documentation.

**B04** — "Model confidence vs world-agreement diverge over time. Confidence: a property of the model, not the world."
- VERIFIED. LLM confidence scores (expressed as probabilities or self-assessed certainty) reflect training data frequency, not real-world accuracy after training cutoff. The divergence is documented in hallucination research. Source: Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" (Anthropic); computational-skepticism-for-ai curriculum.

## Exclusions confirmed
- No specific model version capability claims
- Transformer architecture reference correctly cited to Vaswani et al.

## VERDICT: PASS
