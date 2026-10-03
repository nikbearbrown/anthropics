# PROMPTS — show-tell-claude-asks-your-code-runs

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "get weather", "tool use" and "tool result" so Kokoro doesn't read the underscores):

```
Write a short Python script that gives Claude one tool, get_weather, with a name, a description and an input schema, and asks for the weather in Boston. When the response stops for tool_use, print the request, run a fake weather function, send a tool_result back with the matching ID, and print Claude's answer.
```

Checks shown under it (the viewer runs the script and checks these themselves):
- Check: the first stop_reason is tool_use?
- Check: tool_use_id matches the request's id?
