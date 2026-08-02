## prompt-tutorial-lesson-06-precognition

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/06_Precognition_Thinking_Step_by_Step.ipynb
- **Teachable claim:** "Think step by step" is not a magic spell — it works because it forces Claude to produce intermediate reasoning in the output before the final answer, and you can make it even more reliable by giving Claude a structured scratchpad between XML tags.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Logic puzzle attempted directly: wrong answer → same puzzle with "think step by step" → correct answer — the effect demonstrated
2. XML scratchpad structure: `<thinking>` block before the `<answer>` — forcing visible reasoning
3. Why it works: token-by-token generation means intermediate steps feed forward into the final answer
4. The precognition principle: make Claude "think before it speaks" just like you'd prompt a human consultant

### Score
- Teachability: 5/5 — the mechanistic explanation (tokens feed forward) is the key insight
- Visual: 4/5 — right/wrong answer comparison is punchy; the XML scratchpad diagram is clean
- Pull: 4/5 — chain-of-thought is the single most important prompt technique
- Freshness: 3/5 — well-known concept, but the XML scratchpad structure is underused
- **Total: 16/20**
