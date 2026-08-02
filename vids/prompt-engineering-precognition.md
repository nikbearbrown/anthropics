## C08 — Precognition: Why Telling Claude to Think First Doubles Accuracy

- **slug:** prompt-engineering-precognition
- **source:** ../anthropics/prompt-eng-interactive-tutorial/Anthropic 1P/06_Precognition_Thinking_Step_by_Step.ipynb
- **bucket:** BUILD-WITH-CLAUDE / SDK → claude-scout lens → claude-explainer builder
- **premise:** Chain-of-thought prompting is not about making the model "think longer" — it forces the probability distribution over tokens to commit to a reasoning path before committing to the answer, and that sequential commitment is why it works.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** When you ask Claude to reason step-by-step before answering, you are exploiting the autoregressive structure of transformers — the token that says "therefore X" raises the probability of the correct next token because it has already narrowed the distribution.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Why does "think step by step" make Claude more accurate?`
- topic: `PROMPT ENGINEERING · Precognition`
- segment: `Chain-of-Thought Explained`
- greeting: `Namaste, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the baseline failure: one-shot math question, wrong answer → B02 MECHANISM: autoregressive prediction means every output token conditions on all prior tokens — so a wrong intermediate answer cascades → B03 chain-of-thought demo: same question, step-by-step prompt → correct answer → B04 when it helps vs when it hurts (simple lookups don't benefit; adding extra tokens for a one-word answer is noise) → HANDOFF → OUTRO

### Visual beats (4 suggested)
1. **B01 — Onda code-block + ClaudeComposerAsk:** Show the one-shot prompt: "If a bat and a ball cost $1.10 total and the bat costs $1 more than the ball, how much is the ball?" → output: "$0.10" (wrong). Then the step-by-step version → "$0.05" (correct).
2. **B02 — Manim diagram:** Autoregressive sequence: boxes for tokens, each box labeled with a probability distribution that narrows as more tokens appear. A wrong intermediate token (highlighted in terracotta) causes the distribution to drift toward wrong answers. Animation: the probability mass concentrating in the wrong direction.
3. **B03 — ClaudeComposerAsk micro-beat:** Show the actual Claude prompt that adds "Think through this step by step before answering." Then show Claude's full chain-of-thought output with the correct answer. The typed ask → the result receipt.
4. **B04 — Remotion concept card:** Two-column table: tasks where CoT helps (multi-step math, logic puzzles, complex code) vs tasks where it doesn't (simple lookup, single-fact retrieval, yes/no classification). Visual: left column grows bars, right column stays flat.

### Register notes
Teardown judgment: chain-of-thought is not a hack — it's exploiting a structural property of how transformers generate text. The Teardown line: "You're not asking Claude to be smarter; you're asking it to put its work on paper before committing." Caveat: extended thinking (the model token budget) is a different mechanism — don't conflate them.

### Est length
~120 s (4 beats, mix of definitional and mechanism content_type)

### Scores
- Teachability: 5/5 — the mechanism is clear, the demo is immediate, the result is reproducible by any viewer
- Visual potential: 4/5 — the autoregressive distribution diagram is a strong Manim beat
- Audience pull: 5/5 — everyone who uses Claude wants to know this
- Freshness: 3/5 — chain-of-thought is widely discussed; the autoregressive mechanism explanation is less common
- **Total: 17/20**
