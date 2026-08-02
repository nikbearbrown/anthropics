## C13 — The Unreasonable Effectiveness of HTML as Claude's Output Format

- **slug:** html-as-claude-output-format
- **source:** ../anthropics/html-effectiveness/README.md + index.html
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code / Claude API)
- **premise:** A single Claude prompt can produce a complete interactive HTML app — no build step, no framework, no dependencies — and "HTML as output format" unlocks a whole class of Claude use cases that Markdown cannot handle.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** When you ask Claude for Markdown, you get a document. When you ask for HTML, you get an app — and the 20 examples in the html-effectiveness gallery prove that one prompt is enough for a slide deck, a triage board, an interactive flowchart, and a prompt tuner.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Build me a status report dashboard as a single HTML file`
- topic: `CLAUDE OUTPUT · HTML Format`
- segment: `One Prompt, One App`
- greeting: `Aloha, Liam` (Wagwan check: not 0)

### CLI spine
INTRO → PROBLEM (Markdown caps out at text + tables; interactive outputs require a framework or a build step — or do they?) → CLI LOOP: ASK (type the prompt: "Generate a self-contained HTML status report with sortable columns and a RAG status indicator") → CODE (show the prompt in the composer; show the output HTML in a code block) → OUTPUT (screen recording: open the .html file in a browser — it works, no install) → CHANGE (add a constraint: "no external CDN links, all CSS/JS inline") → SUMMARY → NEXT STEPS → OUTRO

### Hook
Claude producing Markdown is like asking a carpenter to sketch on napkins. The 20 examples in Anthropic's html-effectiveness gallery — from a triage board to an interactive prompt tuner — all run in a browser with no setup.

### The artifact
Screen recording: a terminal `claude "..."` call outputs an HTML file → `open output.html` → a functional interactive dashboard opens in Safari. The "no install" payoff is visible in real time.

### Prompt seed
```
claude "Generate a self-contained single-file HTML status report for a software project.
Requirements:
- Sortable columns (priority, status, owner)
- RAG status indicator (red/amber/green dot per row)
- All CSS and JavaScript inline (no external dependencies)
- Fictional sample data for 8 items
Output the HTML only, no explanation."
```

### Read / check
Verify: (1) the output opens in a browser without loading external resources; (2) sorting actually works; (3) the file is under 200 lines (the key constraint — Claude should not generate bloated code).

### Human supplies
Nothing — fully synthetic. The prompt produces the artifact; the screen recording of opening it is the output beat.

### Output medium
Screen recording mp4 (browser opening the generated HTML) + Onda code-block for the prompt

### The change
Add persistence: prompt Claude to add `localStorage` save/restore so the user's edits survive a page refresh. Show that Claude adds this correctly without breaking the existing functionality.

### Teardown angle
The design judgment: when is HTML the right output format vs JSON, Markdown, or a Python script? Rule of thumb: if the consumer is a human in a browser, HTML; if the consumer is another program, JSON. Claude producing HTML skips the "build a frontend" step entirely for prototypes and internal tools.

### Exclusions
No React/framework comparison. No security/XSS discussion (important but a second video). No cost analysis of long HTML generation. No CDN-linked vs inline debate.

### Score: 7/10

### Scores (rubric dimensions)
- Teachability: 4/5 — the "HTML as output format" framing is immediately actionable
- Visual potential: 4/5 — the screen recording of a working app appearing is satisfying motion
- Audience pull: 4/5 — practitioners who use Claude for work artifacts
- Freshness: 3/5 — HTML output is used but the "20-example gallery" framing is new
- **Total: 15/20**
