## C17 — Build an Attention Head Visualizer With Claude Code

- **slug:** headvis-attention-head-explorer
- **source:** ../anthropics/headvis/README.md
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code)
- **premise:** The headvis repo ships a frontend that visualizes attention head patterns — but the backend data pipeline and server are intentionally stubbed out as `NotImplementedError`. The repo instructs you to hand the stubs to Claude Code with your model choice, and Claude implements them. It's a designed human-AI build partnership.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** The headvis pattern — spec-in-docstrings, implement-with-Claude — is a template for any interpretability tool: write the data contract precisely in docstrings, hand it to Claude Code, let it implement the model-specific bits.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Build me an attention head visualizer for GPT-2`
- topic: `CLAUDE CODE · Interpretability Tools`
- segment: `Spec to Implementation`
- greeting: `Sawadee, Liam` (Wagwan check: not 0)

### CLI spine
INTRO → PROBLEM (interpretability tools require model-specific forward-pass code that's painful to write by hand) → CLI LOOP: ASK (paste the README's own prompt: "Here is data_pipeline.py from the headvis repo. Implement the NotImplementedError functions for gpt2 from HuggingFace using openwebtext.") → CODE (show Claude reading the docstrings = the spec, then implementing the forward pass) → OUTPUT (screen recording: run the data pipeline, serve the frontend, click on an attention head — see its top-activating sequences) → CHANGE (add UMAP projection: ask Claude to implement the `project_to_umap` endpoint in server.py) → SUMMARY → NEXT STEPS → OUTRO

### Hook
The headvis README contains a prompt you paste into Claude Code verbatim. That's intentional — the docstrings ARE the spec, and Claude reading specs is more reliable than Claude guessing intent.

### The artifact
Screen recording: a working headvis frontend with populated data — click a head at layer 5, see its top-activating sequences from openwebtext, its PCA projection, its induction score. The interpretability UI is live, built by Claude from the spec in the docstrings.

### Prompt seed (from the repo's own README)
```
Here's data_pipeline.py from the headvis repo. I want to run it against gpt2
from HuggingFace using the openwebtext dataset, studying layers 5 and 8
across all heads. Implement the NotImplementedError functions and run the pipeline.
```

### Read / check
Verify: (1) the data pipeline produces JSON files in the expected format (the contract is in the docstrings); (2) the frontend can read those JSON files and display head data; (3) clicking a head shows real sequences, not placeholder data.

### Human supplies
A GPU is helpful for running the data pipeline at scale; on CPU with gpt2-small and a small sample (1000 sequences) it's feasible. The screen recording requires running the pipeline — that's the human's compute contribution.

### Output medium
Screen recording mp4 (the working frontend) + Onda code-block for the prompt that Claude implements

### The change
Add SAE (sparse autoencoder) attribution: implement one of the stubbed attribution endpoints to decompose an attention edge into contributing sparse-dictionary feature pairs. Shows the extensibility of the pattern.

### Teardown angle
The design judgment: why are the docstrings detailed enough to be a spec? Because interpretability tools need exact data-format contracts — the frontend can't debug a wrong JSON shape at render time. The lesson: good stubs with precise docstrings are the real artifact; the implementation is almost mechanical.

### Exclusions
No training the SAE from scratch. No comparison to other interpretability tools. No cost/compute analysis.

### Score: 7/10

### Scores (rubric dimensions)
- Teachability: 4/5 — the "docstrings as spec" pattern is broadly applicable
- Visual potential: 4/5 — the attention head UI is genuinely visually interesting
- Audience pull: 3/5 — ML practitioners specifically; narrower than general Claude audience
- Freshness: 4/5 — the specific headvis + Claude Code workflow is new
- **Total: 15/20**
