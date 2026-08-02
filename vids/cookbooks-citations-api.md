## cookbooks-citations-api

- **Source path:** claude-cookbooks/misc/using_citations.ipynb
- **Teachable claim:** Claude's native citations feature returns structured citation objects with exact locations (character offsets for text, page numbers for PDFs) — unlike prompt-based citations, these are guaranteed to point to real locations in the documents you provided.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. API response anatomy: text block + citations array, each citation showing `document_id` and `char_location`
2. Three document types compared: plain text (char offset), PDF (page number), custom content (block index)
3. Live demo: feed a customer FAQ → ask a question → citations appear pointing to the exact policy line
4. Precision/recall comparison: citations feature vs. prompt-based citation techniques

### Score
- Teachability: 5/5 — clear API mechanic with a concrete verification benefit
- Visual: 4/5 — citation objects in JSON are readable and the pointer-to-source is visually compelling
- Pull: 4/5 — anyone building a RAG or document QA system needs this
- Freshness: 5/5 — native citations feature is recent and still underused
- **Total: 18/20**
