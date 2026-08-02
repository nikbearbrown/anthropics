## courses-prompt-evals-model-graded

- **Source path:** courses/prompt_evaluations/
- **Teachable claim:** Model-graded evals — using Claude to score Claude's outputs — work for tasks where human grading would take weeks; the key is writing a grader prompt that scores with a rubric, then calibrating the grader against human labels to confirm it's reliable.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. The grader prompt structure: rubric criteria → Claude assigns 1-5 score → score distribution shown
2. Grader calibration: grader scores vs. human scores on 50 examples — correlation visible
3. Code-graded vs. model-graded: showing where each is appropriate — decision flowchart
4. Custom grader (PromptFoo integration): how to plug a Claude grader into an eval framework

### Score
- Teachability: 5/5 — model-graded evals are the unlock for fast, scalable quality measurement
- Visual: 4/5 — grader calibration scatter plot + rubric table are both visual
- Pull: 4/5 — everyone building a production AI system needs evals; model grading is the scalable path
- Freshness: 3/5 — model grading is established; PromptFoo integration is fresher
- **Total: 16/20**
