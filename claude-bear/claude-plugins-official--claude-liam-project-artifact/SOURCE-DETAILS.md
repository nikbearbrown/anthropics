# Source Details — claude-plugins-official--claude-liam-project-artifact

Generated: 2026-09-05T11:09:00

## Reel
- Question: project-artifact
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-project-artifact/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/project-artifact/skills/project-artifact/SKILL.md
- Name: project-artifact
- Description: Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a piece of work spans several workstreams and you want a shareable overview kept current. Each artifact is backed by a small per-project config in the plugin data dir, so refreshing it re-gathers live state, redeploys the same URL, and reports only the delta. For software projects whose workstreams are PRs, also read swe.md (the X.Y PR-numbering convention; pulling PR state with gh/git; a per-PR detail block). Needs the built-in Artifact tool (claude.ai login). Not for single-PR changes or public docs.

## Capabilities To Name On Screen
- Generate and publish a project status artifact — an opinionated
- tabbed status page for a project too big for one update (overview & success criteria
- the workstream sequence
- plus background
- risks & open questions

## Constraints / Failure Modes
- description: Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the…
- so everything is inlined; the only <script> is the tab switcher) and publishes it with
- Pull whatever the domain gives you cheaply — always live, never from memory or earlier
- Pick the tabs from the catalog below — only the ones with real content
- Decisions/FAQ each earn a tab only when there's something substantive to put in it
- (a simple, self-explanatory project may have just Overview + Workstreams; a big one ~6–8). Never
- must scroll inside its own overflow-x:auto container, never the page body. After
- updates and is only removed on uninstall). It is machine-local: a user who wants a config

## Procedure / Sequence
- Resolve the artifact config, then locate the project.: Each project gets a directory at ${CLAUDE_PLUGIN_DATA}/artifacts/<slug>/ holding config.md (see **"The artifact…
- Pick the tabs: from the catalog below — only the ones with real content. Overview and the Workstreams sequence are the spine and are…
- Generate the HTML: from template.html in this skill directory (same folder as this SKILL.md): it already has the house style (light/dark…
- Review the output for cut-off text and overflow.: Before publishing, re-read the file and check that nothing gets clipped or truncated: fixed-width table columns…
- Publish with the Artifact tool.: Call Artifact with file_path = the HTML, favicon = one or two emoji that fit the project (keep the same emoji on every…
- Share it.: First publish is private to the user — teammates can't open it (they get a 404) until the user shares it. Tell the user…
- (Optional) Register on a hub.: If the user keeps a project hub or index page, append the artifact URL there per that hub's instructions. The slug is…
- Write the config and report.: On a first publish, write ${CLAUDE_PLUGIN_DATA}/artifacts/<slug>/config.md now — recording the minted URL, favicon…

## Supporting Files And Signals
- Referenced: https://claude.ai/code/artifact/<uuid>
- Referenced: swe.md
- Referenced: ${CLAUDE_PLUGIN_DATA}/artifacts/<slug>/
- Referenced: config.md
- Referenced: page.html
- Referenced: artifacts/
- Referenced: claude.ai/code/artifact/...
- Referenced: template.html
- Referenced: prefers-color-scheme
- Referenced: ${CLAUDE_PLUGIN_DATA}/artifacts/<slug>/page.html

## Source Sections
- Workflow
- The artifact config (one per project)
- Refreshing an artifact (deltas, not re-narratives)
- Freshness and trust
- Reading an existing artifact page
- Tab catalog (domain-neutral)
- Conventions (all domains)
- Specializations
- Files

## Batch Log Match
- Row: 61
- Canonical path: anthropics/claude-plugins-official/plugins/project-artifact/skills/project-artifact/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-project-artifact/claude-liam-project-artifact.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
