## C14 — Letting the Model Write Its Own Exam: Model-Written Evaluations

- **slug:** model-written-evals-sycophancy
- **source:** ../anthropics/evals/README.md (Perez et al 2022, "Discovering Language Model Behaviors with Model-Written Evaluations")
- **bucket:** RESEARCH / PAPERS → claude-scout lens → claude-explainer builder
- **premise:** Instead of having humans write thousands of evaluation questions (expensive, slow, incomplete), Anthropic had the language model itself generate the evaluation dataset — and the resulting evals detected sycophancy, power-seeking, and persona stability behaviors that hand-curated evals missed.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** A model can write better evaluations of itself than humans can — not because it's honest about its failures, but because it can generate adversarial prompts faster and at scale than any human labeler.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Can you write test questions designed to catch your own bad behaviors?`
- topic: `AI EVALS · Model-Written Evaluations`
- segment: `The Model Grades Itself`
- greeting: `Kia ora, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the human-labeling bottleneck: how many questions do you need to test sycophancy reliably? → B02 model-written evals: the model generates candidate questions, humans validate a sample → B03 the four behavior categories found: persona, sycophancy, advanced AI risk, gender bias → B04 THE SURPRISE: model-written sycophancy evals caught behaviors that human-curated evals missed (scale + diversity) → HANDOFF → OUTRO

### Visual beats (4 suggested)
1. **B01 — Remotion concept card:** Split: "human labeler writes 500 questions in a week" (slow, limited diversity) vs "model generates 50,000 questions in an hour" (fast, diverse). The scale difference animated as growing bar lengths.
2. **B02 — ClaudeComposerAsk micro-beat:** Show an actual few-shot prompt from the eval repo that asks Claude to generate sycophancy test questions. Then show the output: 10 varied sycophancy scenarios. Receipt: ask → result.
3. **B03 — Remotion animated card grid:** The four behavior categories as labeled cards appearing one by one: PERSONA | SYCOPHANCY | ADVANCED AI RISK | GENDER BIAS. Each card gets a 1-line description and an example question.
4. **B04 — Manim bar chart:** False positive rate vs detection rate: human-curated eval vs model-written eval across the sycophancy category. The model-written eval bar extends further — higher recall. The key result.

### Register notes
Teardown: model-written evals don't replace human judgment — humans validate a sample of the model-generated questions and the grading is still done by a trained preference model. The insight is scalability: you get coverage across far more behavioral dimensions than any team of human writers could produce. The honest limit: the model may systematically miss its own blind spots — evals it writes won't test what it doesn't know to test.

### Est length
~120 s (4 beats, mix of data and mechanism content_type)

### Scores
- Teachability: 4/5 — the mechanism is clear; the scale argument is the hook
- Visual potential: 3/5 — the bar chart and card grid work; the demo prompt is the strongest beat
- Audience pull: 4/5 — anyone who builds evals or uses Claude in production
- Freshness: 3/5 — model-written evals are referenced but underexplained in most discussions
- **Total: 14/20**
