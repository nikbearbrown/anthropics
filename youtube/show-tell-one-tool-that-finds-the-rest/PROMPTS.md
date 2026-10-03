# PROMPTS — show-tell-one-tool-that-finds-the-rest

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "get weather" for `get_weather` and "tool search" for `tool_search`):

```
Read the live docs for the tool search tool. Then write a Python script with twenty mock tools, including get_weather, all set to defer loading, plus a custom tool_search that ranks them by embeddings. Ask about the weather in Tokyo and print each tool Claude calls, in order, with each call's input tokens. Then rerun it with all twenty loaded.
```

Checks shown under it (the viewer runs these themselves):
- Check: tool_search called before get_weather?
- Check: fewer input tokens on the first call?
