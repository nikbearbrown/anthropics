## C07 — @claude Tags Your PR and Fixes the Bug

- **slug:** claude-code-github-action
- **source:** ../anthropics/claude-code-action/README.md
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code / GitHub Actions)
- **premise:** You can add Claude to your GitHub workflow in 12 lines of YAML — after that, any PR comment mentioning @claude triggers Claude Code to read the diff, respond in the thread, and optionally push a fix commit.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** Claude Code in CI is not a chatbot bolted onto GitHub — it has full repo access, reads the diff, understands the PR context, and can push commits back; the 12-line YAML is all the configuration needed.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Add @claude to my GitHub PR workflow`
- topic: `CLAUDE CODE · GitHub Action`
- segment: `@claude in Your PR`
- greeting: `Merhaba, Liam` (Wagwan check: not 0)

### CLI spine
INTRO → PROBLEM (code review is slow; context-switching to ask a question breaks flow) → CLI LOOP: ASK (type the YAML snippet into the terminal) → CODE (show the 12-line workflow file, annotated) → OUTPUT (screen recording: a PR comment mentioning @claude → Claude responds in the thread with a diff → the fix commit appears) → CHANGE (add `allowed_tools: ["Bash"]` to let Claude run tests before suggesting a fix) → SUMMARY → NEXT STEPS → OUTRO

### Hook
You tag @claude in a PR comment the same way you tag a teammate. Claude reads the full diff, understands what changed, answers in the thread — and if you give it write access, pushes the fix.

### The artifact
Screen recording of the GitHub PR lifecycle: open PR → write comment "@claude this function has an off-by-one error" → wait ~15 seconds → Claude's response appears as a thread comment with the corrected code → optional commit pushed to the branch.

### Prompt seed
```
claude "Generate the GitHub Actions workflow file to add Claude Code Action
to my repo. The workflow should:
- trigger on PR comments mentioning @claude
- have Claude read the diff and respond in the PR thread
- NOT automatically push commits (require human confirmation)
Show me the exact YAML and explain each field."
```

### Read / check
Verify: (1) the workflow uses `pull_request` and `issue_comment` triggers correctly; (2) the `ANTHROPIC_API_KEY` secret is referenced but not hardcoded; (3) the `permissions` block includes `pull-requests: write`.

### Human supplies
A GitHub repo with at least one open PR is ideal for the screen recording. A synthetic example (show the YAML + a simulated PR comment thread) is acceptable for the video if a real repo recording is not available.

### Output medium
Screen recording mp4 (the GitHub PR thread is the live artifact) + Onda code-block for the YAML

### The change
Add a structured output schema: instead of a free-form PR comment, Claude returns a JSON object (file, line, severity, suggestion) that the workflow uses to post a formatted review table.

### Teardown angle
The design judgment: "write access" is the meaningful threshold — the action without write access is a smart search; with write access it's a pull-request author. The trust model question (should CI have push rights?) is the one sentence the Teardown register needs to name.

### Exclusions
No Bedrock/Vertex routing. No custom tool configuration. No security hardening beyond the README warning. No cost analysis.

### Score: 8/10

### Scores (rubric dimensions)
- Teachability: 4/5 — the pattern is immediately actionable
- Visual potential: 4/5 — the PR thread appearing in real time is compelling motion
- Audience pull: 5/5 — every developer with a GitHub repo is the audience
- Freshness: 3/5 — GitHub Actions + AI is becoming common; the specific Claude Code pattern is less shown
- **Total: 16/20**
