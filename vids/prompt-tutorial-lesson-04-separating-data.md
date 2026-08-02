## prompt-tutorial-lesson-04-separating-data

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/04_Separating_Data_and_Instructions.ipynb
- **Teachable claim:** XML tags like `<document>` and `<instructions>` are the right way to separate your instructions from the data Claude should process — they prevent instruction-injection attacks and let Claude reliably distinguish "what to do" from "what to do it to."
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The injection risk: user data containing "ignore previous instructions" — what breaks without XML separation
2. XML-wrapped prompt: `<instructions>` wrapping the task, `<document>` wrapping the data — Claude treats them correctly
3. Multiple documents: `<document index="1">`, `<document index="2">` pattern for multi-source tasks
4. Claude's native preference: why Claude handles XML well (trained on XML-rich web data)

### Score
- Teachability: 5/5 — injection prevention is a safety-critical technique with a clear mechanical explanation
- Visual: 4/5 — the injection attack example is dramatic and the XML fix is clean
- Pull: 4/5 — anyone building production prompts that accept user data needs this
- Freshness: 3/5 — XML separation is documented but still widely ignored
- **Total: 16/20**
