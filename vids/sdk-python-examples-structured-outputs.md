## sdk-python-examples-structured-outputs

- **Source path:** anthropic-sdk-python/examples/structured_outputs.py
- **Teachable claim:** Structured outputs in the Anthropic SDK guarantee that Claude's response parses to your Pydantic model — `client.messages.parse(response_format=MyModel)` returns a `.parsed` attribute of type `MyModel`, not a string you have to parse yourself.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Without structured outputs: `json.loads(response.content[0].text)` — manual parsing with error risk
2. With `.parse()`: the Pydantic model populated directly — `.parsed.field` accessed immediately
3. Streaming structured outputs: tokens appear AND the parsed model is valid at the end of the stream
4. Validation on model: Pydantic validation catching an out-of-range value Claude tried to output

### Score
- Teachability: 4/5 — the `.parsed` attribute vs. manual JSON parse is the clean lesson
- Visual: 3/5 — code comparison is functional
- Pull: 4/5 — structured outputs are the standard pattern for any Claude integration that consumes data
- Freshness: 4/5 — `.parse()` method is a new SDK convenience
- **Total: 15/20**
