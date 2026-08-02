## cookbooks-extended-thinking

- **Source path:** claude-cookbooks/extended_thinking/extended_thinking.ipynb
- **Teachable claim:** Extended thinking makes Claude's step-by-step reasoning visible in the response — you get a `thinking` block before the final answer, and the model uses those thoughts to produce measurably better results on hard problems.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. API response split: thinking block (raw scratchpad) vs. final answer — showing the raw chain of thought
2. Redacted thinking blocks explained: what "redacted" means and when it appears
3. Streaming extended thinking — token-by-token output with thinking vs. text phases labeled
4. Token count comparison: simple prompt vs. extended thinking on a hard logic puzzle

### Score
- Teachability: 5/5 — visible chain of thought is a clear, testable mechanic
- Visual: 4/5 — the thinking block output is inherently dramatic to watch appear
- Pull: 4/5 — developers want to know when to use it and what they're paying for
- Freshness: 5/5 — extended thinking is a flagship Claude 3.7+ feature
- **Total: 18/20**
