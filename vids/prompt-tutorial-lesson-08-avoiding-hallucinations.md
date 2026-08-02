## prompt-tutorial-lesson-08-avoiding-hallucinations

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/08_Avoiding_Hallucinations.ipynb
- **Teachable claim:** You cannot stop Claude from hallucinating by asking nicely — the reliable method is grounding: provide the source documents in the prompt and tell Claude to say "I don't know" if the answer isn't in those documents, then verify citations against the source.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Hallucination in the wild: asking Claude about a specific fact without grounding → confident wrong answer
2. Grounding pattern: add source document + "only answer from this document" + "say 'I don't know' if unsure"
3. Uncertainty signal: the difference between a hedged response and a confident hallucination in Claude's language
4. Verification workflow: how to use citations feature to confirm claimed sources exist

### Score
- Teachability: 5/5 — hallucinations are the #1 user complaint; the grounding fix is concrete
- Visual: 4/5 — wrong answer vs. grounded answer comparison is dramatic
- Pull: 5/5 — every Claude user worries about hallucinations
- Freshness: 3/5 — grounding is established, but the combination with citations API is fresh
- **Total: 17/20**
