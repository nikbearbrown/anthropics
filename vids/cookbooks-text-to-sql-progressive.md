## cookbooks-text-to-sql-progressive

- **Source path:** claude-cookbooks/capabilities/text_to_sql/guide.ipynb
- **Teachable claim:** Natural-language SQL generation improves in four measurable steps — baseline prompt, few-shot examples, chain-of-thought XML scratchpad, RAG over schema — and each step's accuracy gain is measured against a held-out test set so you know when to stop.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Baseline: plain prompt → SQL against a SQLite employees/departments DB; run the generated query; show a wrong result from an ambiguous natural-language question
2. Few-shot: add 3 examples of hard questions with correct SQL → accuracy jumps; show the same ambiguous question now resolved correctly
3. Chain-of-thought scratchpad: add `<reasoning>` XML tag in the system prompt → the model writes its interpretation before generating SQL → catches a different class of errors
4. RAG schema lookup: when the DB schema is too large for the prompt, embed schema descriptions; retrieve the relevant tables for each question; show token count before/after

### Score
- Teachability: 5/5 — the four-step accuracy ladder with a live measurement at each step is a perfect pedagogical structure
- Visual: 4/5 — wrong query → right query before/after at each step is concrete and checkable
- Pull: 4/5 — text-to-SQL is the most common "Claude on my data" use case
- Freshness: 3/5 — text-to-SQL is well-covered; the progressive accuracy measurement framing is the differentiator
- **Total: 16/20**
