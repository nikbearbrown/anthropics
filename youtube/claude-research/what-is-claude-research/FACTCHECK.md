# FACTCHECK — what-is-claude-research

## Beat-by-beat verification

**B01** — "Model output flows straight to document. No detour. No stop."
- VERIFIED. This describes the wrong model: treating Claude's citations as verified primary sources without checking. LLMs are documented to hallucinate citations. Source: Maynez et al. (2020) "Faithfulness and Factuality in Abstractive Summarization"; multiple Anthropic model-card disclaimers.

**B02** — "Citation routed through primary source check. Bad citation? Dissolved. Verify before you cite."
- VERIFIED. The correct research workflow requires verifying model-generated citations against primary sources before use. This is established academic practice and explicitly recommended in Anthropic guidance on using Claude for research. Source: Anthropic usage guidelines; standard academic citation practice.

**B04** — "Source laundering: a real number attaches to the wrong banner. Real number. Wrong banner."
- VERIFIED. Source laundering — where a real statistic is correctly stated but misattributed — is a documented failure mode in LLM-assisted research. The example (73% moving from Source A to Source B) accurately illustrates the mechanism. Source: computational-skepticism-for-ai curriculum; Anthropic model-card disclaimers on hallucination.

## Exclusions confirmed
- No specific academic papers cited by title/DOI in the video — correct for an intro playlist video
- Hallucination claim is well-established across the literature

## VERDICT: PASS
