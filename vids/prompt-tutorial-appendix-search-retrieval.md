## prompt-tutorial-appendix-search-retrieval

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/10.3_Appendix_Search & Retrieval.ipynb
- **Teachable claim:** RAG (Retrieval-Augmented Generation) with Claude is a search problem first and an LLM problem second — the bottleneck is usually the retrieval quality, not Claude's ability to synthesize what it retrieves.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. RAG pipeline: embed query → vector search → retrieve top-k → inject into prompt → Claude answers
2. Retrieval quality test: same Claude prompt, different retrieval results — output quality tracks the retrieval
3. Chunking strategy: how chunk size and overlap affect what gets retrieved and what gets lost
4. Failure mode: relevant content present in corpus but not retrieved — the retrieval failure vs. hallucination distinction

### Score
- Teachability: 4/5 — the "retrieval first" framing is a useful mental model correction
- Visual: 4/5 — the pipeline diagram and retrieval quality comparison are both clear
- Pull: 4/5 — RAG is the most common production Claude pattern
- Freshness: 2/5 — RAG is well-established
- **Total: 14/20**
