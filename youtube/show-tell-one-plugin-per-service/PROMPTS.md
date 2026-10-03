# PROMPTS — show-tell-one-plugin-per-service

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "Anthropic's claude tag plugins repo" so Kokoro doesn't spell the slash; the bracketed slot is read as "list them"):

```
Here are the tools my team uses each week: [list them]. From the plugin list in anthropics/claude-tag-plugins, pick the ones our Claude Tag needs. For each, say whether it should only read or also write, and in which channels. Then list what to leave unplugged, and why.
```

Checks shown under it:
- Check: every plugin. Who used that tool this week?
- Check: every write. Which channel and task need it?
