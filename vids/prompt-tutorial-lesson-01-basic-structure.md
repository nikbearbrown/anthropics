## prompt-tutorial-lesson-01-basic-structure

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/01_Basic_Prompt_Structure.ipynb
- **Teachable claim:** A Claude API call is three things: a model name, a max_tokens limit, and a messages array — understanding the messages array structure (role + content pairs) is the single prerequisite for everything else in prompt engineering.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–3 min)

### Visual beats
1. The minimal API call: three fields, nothing else — shown as code then as a diagram
2. Messages array anatomy: role=user / role=assistant alternation rule — the constraint explained
3. First response object: showing where the text lives in the response (`content[0].text`)
4. Common mistake: sending two consecutive user messages — the error and the fix

### Score
- Teachability: 4/5 — foundational but a real barrier for beginners
- Visual: 3/5 — code-heavy but the messages array diagram is clear
- Pull: 3/5 — beginner-focused; high volume audience
- Freshness: 2/5 — Messages API is established
- **Total: 12/20**
