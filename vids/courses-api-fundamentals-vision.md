## courses-api-fundamentals-vision

- **Source path:** courses/anthropic_api_fundamentals/06_vision.ipynb
- **Teachable claim:** Sending an image to Claude requires wrapping it as a `base64` content block with the media type — three lines of code — and Claude can then describe, analyze, extract text from, or answer questions about any image you provide.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The content block structure: `{"type": "image", "source": {"type": "base64", "media_type": "...", "data": "..."}}` shown in code
2. URL image: passing a URL directly vs. encoding locally — when each works
3. Mixed content: text question + image in the same message — the multimodal prompt structure
4. Use case gallery: OCR, chart reading, UI description, document analysis — each in one line

### Score
- Teachability: 4/5 — the base64 content block is the one technical barrier to vision
- Visual: 4/5 — image input + Claude output is inherently visual
- Pull: 4/5 — vision unlocks a huge set of use cases; many developers skip it because of the encoding step
- Freshness: 2/5 — established feature
- **Total: 14/20**
