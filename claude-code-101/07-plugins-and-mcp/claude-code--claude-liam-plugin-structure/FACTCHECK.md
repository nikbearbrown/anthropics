# FACTCHECK — claude-liam-plugin-structure

Status: **GATE F SIGNED — 2026-08-19 by Claude (rebuild pass). 10 rows, all PASS.**
Primary source: `anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/SKILL.md`. Cross-skill source: `anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|------|--------------------------|---------|---------------------|---------------|
| 1 | B00 | Claude Code plugins follow a standardized layout: manifest in the dot-claude-plugin directory, component directories at the plugin root | ✓ PASS | plugin-structure SKILL.md §Directory Structure, Critical rules 1+2 | — |
| 2 | B00 | Auto-discovery: add a file to the right directory and it loads; no registration step | ✓ PASS | §Auto-Discovery Mechanism: "Plugin installation: Components register with Claude Code" | — |
| 3 | B01 | The manifest, plugin.json, has one required field: name, in kebab-case | ✓ PASS | §Required Fields: `{"name": "plugin-name"}` only; §Name requirements: "Use kebab-case format" | — |
| 4 | B01 | Custom paths in the manifest supplement auto-discovery — they don't replace it. If you set a custom agents path, the default agents directory is still scanned | ✓ PASS | §Component Path Configuration: "Custom paths supplement defaults—they don't replace them. Components in both default directories and custom paths will load." | — |
| 5 | B02 | Five component types: commands, agents, skills, hooks, MCP servers | ✓ PASS | §Component Organization: Commands, Agents, Skills, Hooks, MCP Servers — five sections | — |
| 6 | B02 | Skills must have a file named exactly SKILL.md — not README.md, not skill.md | ✓ PASS | §Skills: "each skill in its own directory with SKILL.md file"; §Troubleshooting: "Ensure skill has SKILL.md (not README.md or other name)" | — |
| 7 | B05 | Three layout patterns — minimal, full-featured, skill-focused — cover the practical range | ✓ PASS | §Common Patterns: three named subsections "Minimal Plugin", "Full-Featured Plugin", "Skill-Focused Plugin" | — |
| 8 | B05 | The placement rule (manifest in .claude-plugin vs components at root) gets one mention in Critical Rules but is never reinforced in the component sections | ✓ PASS | Critical rules block states both rules; §Commands, §Agents, §Skills, §Hooks, §MCP Servers sections contain no restatement of placement rules | — |
| 9 | B05 | The skill states no restart required for changes | ✓ PASS | §Auto-Discovery Mechanism: "No restart required: Changes take effect on next Claude Code session" | — |
| 10 | B05 | The hook-development skill says restart is required — inconsistent guidance for the same lifecycle event | ✓ PASS | hook-development SKILL.md: "Hooks are loaded when Claude Code session starts. Changes to hook configuration require restarting Claude Code." — confirms the inconsistency | — |
