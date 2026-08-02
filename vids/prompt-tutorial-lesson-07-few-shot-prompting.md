## prompt-tutorial-lesson-07-few-shot-prompting

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/07_Using_Examples_Few-Shot_Prompting.ipynb
- **Teachable claim:** Examples in a prompt do more than demonstrate format — they encode implicit style rules, tone calibration, and domain vocabulary that are nearly impossible to specify explicitly, making few-shot prompting the right tool whenever your output has a subjective "feel" requirement.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Tone transfer: three examples of a brand's customer service voice → Claude matches it without explicit description
2. Format replication: structured examples encode a response template Claude extracts and follows
3. Zero-shot vs. one-shot vs. three-shot on the same task — output quality progression
4. When NOT to use few-shot: when examples are hard to source or the task is fully specifiable in instructions

### Score
- Teachability: 4/5 — the "implicit style encoding" framing is genuinely novel to most developers
- Visual: 3/5 — output comparison is clear; tone matching is harder to show visually
- Pull: 4/5 — anyone building a branded AI product needs few-shot techniques
- Freshness: 2/5 — established technique
- **Total: 13/20**
