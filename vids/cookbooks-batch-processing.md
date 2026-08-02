## cookbooks-batch-processing

- **Source path:** claude-cookbooks/misc/batch_processing.ipynb
- **Teachable claim:** The Message Batches API processes large volumes of API requests asynchronously at 50% lower cost — if you're running more than a few hundred Claude calls at once, not using it is leaving money on the table.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Cost comparison bar chart: standard API vs. batch API for 1k, 10k, 100k requests
2. Batch lifecycle: submit → monitor status → retrieve results — three steps shown in terminal
3. Async polling pattern: how to check batch completion without blocking
4. Use case gallery: classification, translation, summarization at scale

### Score
- Teachability: 4/5 — simple mechanic with a hard number (50% off) as the hook
- Visual: 3/5 — mostly terminal output but cost comparison is visual
- Pull: 4/5 — any developer running scale workloads needs to know this
- Freshness: 3/5 — batch APIs are a known pattern but Message Batches is Claude-specific
- **Total: 14/20**
