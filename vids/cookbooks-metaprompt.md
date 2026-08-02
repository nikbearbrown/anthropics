## cookbooks-metaprompt

- **Source path:** claude-cookbooks/misc/metaprompt.ipynb
- **Teachable claim:** Anthropic's Metaprompt solves the blank-page problem: you give it your task and variable names, and Claude generates a complete, production-quality prompt template — including XML delimiters, few-shot examples, and chain-of-thought instructions.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The composer: type task description → Claude writes the full prompt template — cold open on the UI
2. Output structure walkthrough: `<Inputs>`, `<Instructions Structure>`, and the template itself — annotated with callouts
3. Testing the generated template on example variable values — output compared to a hand-written prompt
4. Limitations callout: designed for single-turn tasks, not multi-turn; starting point not end state

### Score
- Teachability: 4/5 — concrete tool for a universal developer problem
- Visual: 4/5 — the Claude UI is the set; the prompt output is readable on screen
- Pull: 4/5 — anyone who has stared at a blank prompt field wants this
- Freshness: 3/5 — metaprompting is known, but Anthropic's specific tool is underused
- **Total: 15/20**
