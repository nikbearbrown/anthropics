## prompt-tutorial-appendix-prompt-chaining

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/10.1_Appendix_Chaining Prompts.ipynb
- **Teachable claim:** Prompt chaining — using Claude's output as input to the next Claude call — is more reliable than one giant prompt because each stage has a single, auditable job; the chain's correctness is checkable step by step.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. One-shot complex prompt vs. three-stage chain: the same task broken down — output quality comparison
2. Chain diagram: extract → validate → format — each stage with its own prompt and output
3. Error isolation: which stage failed? Debugging a chain vs. debugging a single long prompt
4. When to chain: tasks with natural checkpoints vs. tasks that genuinely belong in one prompt

### Score
- Teachability: 4/5 — the auditability benefit is the key insight most developers miss
- Visual: 3/5 — pipeline diagram is clear but mostly code-based
- Pull: 4/5 — anyone building multi-step Claude workflows needs this pattern
- Freshness: 2/5 — established pattern
- **Total: 13/20**
