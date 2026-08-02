## quickstarts-financial-data-analyst

- **Source path:** claude-quickstarts/financial-data-analyst/
- **Teachable claim:** Claude can drive interactive data visualization — ask a question in natural language, Claude writes the chart code, the chart renders in the browser, you refine in the next message — turning a data analyst workflow into a conversation.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. Upload CSV → ask "show me revenue trends by quarter" → chart appears — the full loop in real-time
2. Refinement: "make it a bar chart and highlight Q4" → Claude rewrites the plotting code → updated chart
3. Code shown: Claude's generated matplotlib/plotly code visible in a side panel — transparency about what ran
4. Architecture: Claude generates code → sandbox executes → result returned to UI — the data analyst pattern

### Score
- Teachability: 4/5 — code-generating-then-executing for data analysis is a compelling workflow
- Visual: 5/5 — chart appearing from a natural language question is visually satisfying
- Pull: 4/5 — data analyst workflows are high-value for business users
- Freshness: 3/5 — data analysis with LLMs is established but this quickstart is clean
- **Total: 16/20**
