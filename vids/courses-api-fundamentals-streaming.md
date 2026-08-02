## courses-api-fundamentals-streaming

- **Source path:** courses/anthropic_api_fundamentals/05_Streaming.ipynb
- **Teachable claim:** Streaming is not a nice-to-have — for responses longer than a few sentences, non-streaming feels broken to users; the Claude SDK's streaming iterator produces tokens as they're generated and you handle them in a simple `for event in stream` loop.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Non-streaming response: blank UI → 3 second pause → full text appears — what it feels like to users
2. Streaming response: same request → tokens appear one by one — perceptibly better
3. Streaming iterator code: `with client.messages.stream() as stream: for text in stream.text_stream` — minimal
4. `stream.get_final_message()`: how to still get the complete response object after streaming

### Score
- Teachability: 4/5 — streaming is the #1 missing piece in beginner Claude apps
- Visual: 5/5 — the before/after UX difference is the most legible possible demo
- Pull: 5/5 — every developer building a chat interface needs this
- Freshness: 2/5 — streaming is established but this is the cleanest tutorial version
- **Total: 16/20**
