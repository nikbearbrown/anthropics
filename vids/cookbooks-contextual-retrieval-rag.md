## cookbooks-contextual-retrieval-rag

- **Source path:** claude-cookbooks/capabilities/contextual-embeddings/guide.ipynb
- **Teachable claim:** Adding a 100-token context prefix to each chunk before embedding — "chunk X appears in a document about Y, in a section about Z" — cuts retrieval failure rate by 49% because the embedding carries enough context to match queries that the raw chunk text would miss.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The failure mode: show a raw chunk that looks like "The company reported $4.2B in revenue" — no context; the embedding correctly places it near finance queries but the question "what did Acme report?" retrieves the wrong company's chunk
2. Contextual prefix generation: `claude.messages.create` with the chunk + full document → 100-token context sentence; show the prefix making the chunk unambiguous
3. Embedding comparison: Voyage AI embeddings on raw vs. contextualized chunks; cosine similarity scores on matching vs. non-matching queries — the gap widens on ambiguous queries
4. BM25 hybrid search: combine dense contextual embeddings with BM25 keyword search; the `recall@10` improvement table shows each technique's contribution

### Score
- Teachability: 5/5 — the "49% retrieval failure reduction from a 100-token prefix" is a specific, checkable claim
- Visual: 4/5 — chunk-with-and-without-prefix + retrieval scoring table is concrete
- Pull: 5/5 — RAG retrieval quality is the #1 problem every Claude-on-docs builder hits
- Freshness: 4/5 — contextual retrieval was the original blog post; the guide notebook is the buildable version
- **Total: 18/20**
