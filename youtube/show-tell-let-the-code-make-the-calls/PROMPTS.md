# PROMPTS — show-tell-let-the-code-make-the-calls

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "get orders" for `get_orders` and "Jason" for JSON):

```
Read the live docs for programmatic tool calling, then write a Python script with a mock get_orders tool that returns long JSON orders. Let code execution call it for ten customers, find who spent over a thousand dollars, and print each call's caller and the input tokens. Then rerun it with direct calls only.
```

Checks shown under it (the viewer runs these themselves):
- Check: every get_orders call from code execution?
- Check: far fewer input tokens than direct?
