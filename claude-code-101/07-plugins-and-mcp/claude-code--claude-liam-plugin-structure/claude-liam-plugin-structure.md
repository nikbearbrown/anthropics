Plugin Structure — Claude Code Skills Teardown

Claude Code plugins follow a standardized directory layout: a manifest in .claude-plugin/, and component directories — commands/, agents/, skills/, hooks/ — at the plugin root. Auto-discovery means you add a file to the right directory and it loads; no registration step needed. But the manifest-in-.claude-plugin vs components-at-root placement rule is the most common silent failure. This teardown walks through the full directory anatomy, the five component types, the ${CLAUDE_PLUGIN_ROOT} portable-path law, and where the skill gets it right — and where it bites.

0:00 Intro
0:40 Directory Layout + Manifest
1:41 Component Types + Paths
2:44 Teardown: Gets Right / Where It Bites
3:59 Verdict
4:42 Your Turn
5:30 Outro

YOUR TURN: Open a Claude Code session. Paste this prompt: "Create a plugin called code-review-assistant that has a review command, a code-reviewer agent, and an api-testing skill." Watch four things: (1) Does Claude place the manifest at .claude-plugin/plugin.json, not at the plugin root? (2) Does Claude place commands/, agents/, and skills/ at the plugin root, not inside .claude-plugin/? (3) Does the skill directory contain a file named exactly SKILL.md? (4) Does any hook configuration use ${CLAUDE_PLUGIN_ROOT} for its command path?

Source: anthropics/claude-code plugins/plugin-dev/skills/plugin-structure/SKILL.md

Liam, in for Bear · @NikBearBrown

Every claim in this video was fact-checked against the source material before rendering.

#claudecode #aitools #claudeai
