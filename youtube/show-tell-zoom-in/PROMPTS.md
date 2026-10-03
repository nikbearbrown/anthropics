# PROMPTS — show-tell-zoom-in

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "x one, y one, x two, y two" and "crop tool"):

```
Add a zoom tool to my image-question script, the way Anthropic's crop_tool cookbook does it: inputs x1, y1, x2, y2 in pixels; crop from the full-resolution original, scale the crop up, and print every region Claude asks for.
```

Checks shown under it (the viewer runs these themselves):
- Check: does each region cover the detail?
- Check: does the answer change with the tool off?
