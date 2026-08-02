## C04 — Constitutional AI: Teaching an AI to Grade Its Own Homework

- **slug:** constitutional-ai-self-critique
- **source:** ../anthropics/ConstitutionalHarmlessnessPaper/README.md (arXiv 2212.08073)
- **bucket:** RESEARCH / PAPERS → claude-scout lens → claude-explainer builder
- **premise:** Instead of having human annotators label thousands of harmful outputs, Anthropic wrote 16 principles and had Claude critique and revise its own answers against them — then used those self-revisions as the training data. The result beat human-feedback-only training on harmlessness without sacrificing helpfulness.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register)
- **teachable claim:** You can replace most human harmlessness labeling with AI self-critique against a written constitution — and the resulting model follows the spirit of the rules rather than pattern-matching to what annotators disliked.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Can an AI learn to be safe by grading its own answers?`
- topic: `AI SAFETY · Constitutional AI`
- segment: `The Self-Critique Loop`
- greeting: `Jambo, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the problem with human labeling (expensive, inconsistent, doesn't generalize) → B02 constitutional AI: write rules, run the critique loop → B03 MECHANISM: Critique → Revision → better response, iterated → B04 RLHF from AI feedback (RLAIF): use those revised responses to train a preference model → B05 result — as harmless as human-feedback model, more transparent about its reasoning → HANDOFF → OUTRO

### Visual beats (4 suggested)
1. **B01 — Remotion concept card:** Two boxes: "human labeling" (annotator icon, dollar signs, slow) vs "constitutional AI" (document icon, fast feedback loop). Split-screen contrast.
2. **B02 — ClaudeComposerAsk micro-beat (ASK→RESULT):** Show the actual constitution principle ("Identify the most harmful response..."). Then show the Claude prompt that implements the critique step. Then show an example harmful response → the critique → the revised response.
3. **B03 — Manim loop diagram:** Critique → Revision → Repeat. Three cycles shown as an animated loop. Each cycle the response quality improves (color shifts from red toward green). Simple feedback loop with arrow labels.
4. **B04 — Remotion animated chart:** Side-by-side harmlessness vs helpfulness scores: RLHF (human labels) vs CAI. The two bars are comparable on harmlessness; the CAI bar is slightly better on helpfulness. Bars animate in. Spark line: "Less human labor. Same result."

### Register notes
Teardown: CAI is genuinely clever — it turns the AI into its own safety labeler. The honest caveat: the constitution is still written by humans; you haven't removed human values from the loop, you've made them more explicit and scalable. That's the Teardown line to land.

### Est length
~130 s (5 beats, mechanism content_type)

### Scores
- Teachability: 5/5 — clean loop, concrete mechanism, publishable result
- Visual potential: 4/5 — the critique-revision loop is a strong diagram; the constitution document is a visual anchor
- Audience pull: 4/5 — "AI grades its own safety homework" is relatable
- Freshness: 4/5 — many have heard of RLHF; CAI's self-critique loop is less known
- **Total: 17/20**
