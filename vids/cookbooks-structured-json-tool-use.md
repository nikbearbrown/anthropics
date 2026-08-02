## cookbooks-structured-json-tool-use

- **Source path:** claude-cookbooks/tool_use/extracting_structured_json.ipynb
- **Teachable claim:** Tool use is the right way to get structured JSON from Claude — not prompting for JSON — because it uses the schema as a guarantee rather than a suggestion, with higher precision and lower output tokens.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Live demo: ask Claude for a summary as plain text vs. via a tool with JSON schema — raw output comparison
2. Five structured extraction tasks side-by-side: summarization, NER, sentiment, classification, open-ended schema
3. Schema design: input_schema with required fields vs. open-ended to handle unknown keys
4. Token count comparison: prompt-based JSON vs. tool-use JSON

### Score
- Teachability: 5/5 — concrete technique with measurable output quality improvement
- Visual: 4/5 — JSON output comparison is clean and readable on screen
- Pull: 5/5 — structured extraction is one of the top Claude use cases
- Freshness: 3/5 — tool use for structured output is established but still underused
- **Total: 17/20**
