## cookbooks-building-evals

- **Source path:** claude-cookbooks/misc/building_evals.ipynb
- **Teachable claim:** Good evals use the cheapest possible grader — code match, then model-graded, then human — and you can use Claude itself to generate both the test cases and the grader prompt, turning a week of work into an afternoon.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Eval anatomy: input prompt → golden answer → model output → score — the four parts as a flow diagram
2. Three grading methods side-by-side: exact match (fast/cheap), model-graded (flexible), human (slow/expensive) — with cost curves
3. Grader prompt template: how to write a Claude self-grader for tone or free-form accuracy
4. Live eval run: watching pass/fail scores appear as Claude grades its own outputs

### Score
- Teachability: 5/5 — concrete and actionable; evals are the #1 thing developers skip
- Visual: 4/5 — grading pipeline is easy to diagram and animate
- Pull: 5/5 — anyone deploying Claude in production needs evals
- Freshness: 3/5 — evals are an established concept, but this specific workflow is still underused
- **Total: 17/20**
