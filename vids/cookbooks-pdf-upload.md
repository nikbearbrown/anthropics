## cookbooks-pdf-upload

- **Source path:** claude-cookbooks/misc/pdf_upload_summarization.ipynb
- **Teachable claim:** Claude can read a full PDF natively — no parsing, no text extraction, no chunking — by encoding it as a base64 document block; the model sees the actual document structure, not just extracted text.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–3 min)

### Visual beats
1. The document block: `{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": "..."}}` — the one code addition
2. Long PDF summarized: a multi-page research paper → Claude returns a structured summary in seconds
3. Page-level citation: Claude citing "on page 4, the paper states..." — the native document structure preserved
4. Comparison: text extraction + summary vs. native PDF block — token cost and quality side-by-side

### Score
- Teachability: 4/5 — native PDF without parsing is the practical unlock for document workflows
- Visual: 3/5 — code + text output, but the "no parsing" revelation is the story
- Pull: 5/5 — PDF processing is one of the most common Claude use cases
- Freshness: 3/5 — native PDF support is established but still underused
- **Total: 15/20**
