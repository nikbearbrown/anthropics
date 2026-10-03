# PROMPTS — show-tell-inside-a-plugin-folder

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "plugin dot json" so Kokoro doesn't read the dot as a full stop):

```
Before I install the Claude Code plugin [name], read its folder. List every part it ships: plugin.json, commands, sub-agents, skills, hooks, and MCP servers. For each hook, give the event and the exact command it runs. For each MCP server, say where it connects and what keys it needs. Then list what it could read, change, or send off my machine. Don't install or run anything.
```

Checks shown under it:
- Check: open hooks/hooks.json and read every command it runs.
- Check: open .mcp.json. Does every server match what the plugin says it does?
