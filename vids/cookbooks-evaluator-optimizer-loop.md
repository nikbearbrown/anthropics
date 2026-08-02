## cookbooks-evaluator-optimizer-loop

- **Source path:** claude-cookbooks/patterns/agents/evaluator_optimizer.ipynb
- **Teachable claim:** Two Claude calls in a loop — one generates, one evaluates with `PASS / NEEDS_IMPROVEMENT / FAIL` — produce iteratively refined code without any framework, because the evaluator's `<feedback>` block becomes the next generator's starting prompt.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The two-call loop: generator prompt → code output; evaluator prompt checks correctness + time complexity + style → verdict + feedback; if NEEDS_IMPROVEMENT, feedback becomes the next generator input
2. Iteration demo: the starter code has an O(n²) sort; evaluator flags it; generator replaces with O(n log n); evaluator passes; show the diff at each iteration
3. When to use this pattern: two signs — LLM responses demonstrably improve on feedback AND the LLM can provide meaningful feedback itself; contrast with single-shot where feedback doesn't help
4. Cost control: set `max_iterations=3`; the loop exits on PASS or when the limit hits; show total token cost for the 3-iteration code improvement

### Score
- Teachability: 5/5 — the evaluator prompt contract (PASS/NEEDS_IMPROVEMENT/FAIL + structured feedback) is immediately reusable
- Visual: 4/5 — code diff across iterations is concrete and satisfying
- Pull: 4/5 — code quality improvement loop is universally useful
- Freshness: 4/5 — evaluator-optimizer pattern is established but the pure-SDK implementation without a framework is the fresh angle
- **Total: 17/20**
