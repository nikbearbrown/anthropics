## cookbooks-programmatic-tool-calling

- **Source path:** claude-cookbooks/tool_use/programmatic_tool_calling_ptc.ipynb
- **Teachable claim:** Programmatic Tool Calling (PTC) lets Claude write Python that calls tools inside a Code Execution sandbox instead of round-tripping through the model for each call — slashing end-to-end latency on multi-tool tasks and letting the code filter noise before it hits the context window.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The contrast: standard tool calling = one model turn per tool call; PTC = one model turn generates a Python script that calls N tools in a loop inside the sandbox
2. Latency demo: run the same 10-API-call task both ways; show the wall-clock comparison — the loop inside the sandbox has no per-call round-trip cost
3. Context filtering: the Python script runs `grep` over a large file and returns only the relevant lines — show the before (whole file in context) vs. after (only signal in context)
4. When NOT to use PTC: deterministic scripts vs. judgment calls; the PTC code runs in a sandboxed environment the model trusts, so tool validation logic belongs in the host layer

### Score
- Teachability: 5/5 — "write code that calls tools, not tools that call Claude" inverts the mental model productively
- Visual: 4/5 — wall-clock timer + context size comparison is measurable and concrete
- Pull: 5/5 — anyone with multi-step tool workflows wants to cut latency
- Freshness: 5/5 — PTC is new API surface with almost no public coverage
- **Total: 19/20**
