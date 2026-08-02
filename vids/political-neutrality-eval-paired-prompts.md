## C18 — How Anthropic Tests Whether Claude Is Politically Biased

- **slug:** political-neutrality-eval-paired-prompts
- **source:** ../anthropics/political-neutrality-eval/README.md
- **bucket:** RESEARCH / PAPERS → claude-scout lens → claude-explainer builder
- **premise:** The paired-prompts methodology for political bias eval: for every political topic, write two prompts that argue opposite positions, run both through Claude, and measure whether the responses are equally good — not equally long, but equally persuasive, evidence-based, and complete.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** You can't test political bias by looking at what a model says — you have to compare how well it argues opposite sides of the same issue. A model that refuses both sides equally is as "fair" as one that argues both equally well; the eval must distinguish those cases.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Is Claude politically biased? Here's how Anthropic actually tests it.`
- topic: `AI EVALS · Political Neutrality`
- segment: `The Paired-Prompts Method`
- greeting: `Hei, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 why naive testing fails: you can't just ask "is Claude biased?" or count how many times it mentions each party → B02 the paired-prompts design: same topic, opposite stance, same task framing → B03 the three dimensions graded by a judge model: even-handedness, refusal rate, acknowledgment of opposing perspectives → B04 the result: the methodology revealed specific task categories (humor, opinion) where consistency was harder to achieve → HANDOFF → OUTRO

### Visual beats (3 suggested)
1. **B01 — Remotion concept card:** Naive method vs paired-prompts method. Left: "count mentions of Party A vs Party B" (broken — topic frequency isn't bias). Right: "write two prompts, measure response quality parity" (correct — measures helpfulness symmetry).
2. **B02 — Onda code-block:** Show two example paired prompts from the repo's actual topics.txt: one prompt arguing for a policy, one arguing against it. Show the grading dimensions: Evidence | Persuasiveness | Engagement.
3. **B03 — Manim animated result table:** Task categories (reasoning, formal writing, narrative, analysis, opinion, humor) × consistency score. Opinion and humor categories shown with lower initial consistency. The animation builds the table row by row.

### Register notes
Teardown: the even-handedness metric is the insight — it's asking "does Claude work equally hard for both sides?" not "does Claude agree with neither?" A model that writes mediocre arguments for both conservative and liberal positions scores the same as one that writes nothing — but those are very different behaviors. The methodology distinguishes them via a refusal score.

### Est length
~115 s (3 beats, mixed definitional and data content_type)

### Scores
- Teachability: 4/5 — the paired-prompt design is immediately clear and reproducible
- Visual potential: 3/5 — the table and code block work; the split-card comparison is the strong visual
- Audience pull: 4/5 — AI safety and bias is high-interest; the methodology angle is less expected
- Freshness: 4/5 — the blog post exists; the methodology explanation as a video is new
- **Total: 15/20**
