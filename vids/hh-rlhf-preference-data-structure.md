## C16 — The Chosen/Rejected Pair: How RLHF Data Is Actually Structured

- **slug:** hh-rlhf-preference-data-structure
- **source:** ../anthropics/hh-rlhf/README.md + arXiv 2204.05862
- **bucket:** RESEARCH / PAPERS → claude-scout lens → claude-explainer builder
- **premise:** RLHF training data is not "label this response good or bad" — it's pairwise: show a human two responses to the same prompt and ask which is better. The chosen/rejected pair structure is what makes preference learning work, and the HH-RLHF dataset makes this concrete.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** The key insight of RLHF is not that humans grade responses — it's that humans grade pairs. The pairwise comparison removes the need for an absolute quality scale and makes the preference signal more consistent across annotators.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `How do you actually train an AI to be helpful and harmless?`
- topic: `AI TRAINING · RLHF Data Structure`
- segment: `The Chosen-Rejected Pair`
- greeting: `Privet, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the naive picture: rate responses 1–10 (why this doesn't work) → B02 the pairwise insight: show annotators two responses to the same prompt, ask which is better → B03 the HH-RLHF dataset: 160k+ preference pairs, helpfulness and harmlessness separately, with red-teaming data → B04 how the preference model is trained on these pairs → HANDOFF → OUTRO

### Visual beats (3 suggested)
1. **B01 — Remotion concept card:** An annotator with a "Rate 1–10" scale. Problem annotations: the same response gets 6 from one annotator and 8 from another. Inconsistency. Then: the pairwise version — which of these two is better? Much easier to agree on.
2. **B02 — Onda code-block:** Show a single jsonl line from the HH-RLHF dataset. `{"chosen": [...], "rejected": [...]}`. The actual data structure — one conversation thread is "chosen," the slightly worse one is "rejected." Label each field.
3. **B03 — Manim training diagram:** The preference model learns a scalar reward for any response. Two training examples shown: chosen response → reward 0.8; rejected response → reward 0.3. The model learns to push chosen higher and rejected lower. The optimization objective shown as a simple formula.

### Register notes
Teardown: RLHF via pairwise comparison is cleverly sidestepping an unsolved problem (how do you define "quality" absolutely?). The honest limitation: pairwise comparison tells you which of two responses is better, not why — the model learns from the preference signal, not from a human-written explanation of the preference.

### Est length
~110 s (3 main beats, definitional + data content_type)

### Scores
- Teachability: 4/5 — the pairwise insight is clean and concrete
- Visual potential: 3/5 — the JSONL data structure is an Onda beat; the training diagram is Manim
- Audience pull: 4/5 — everyone curious about how Claude was trained
- Freshness: 3/5 — RLHF is widely discussed; the HH data structure detail is less shown
- **Total: 14/20**
