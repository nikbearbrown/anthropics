# PROMPTS — show-tell-pay-once-for-the-long-part

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with the underscores as spaces: "cache control", "cache creation input tokens", "cache read input tokens"):

```
Find every place this project calls the Claude API with the same long context each time, like a big system prompt or a document. Turn on prompt caching with a top-level cache_control, keep that long part first and unchanged, and move anything that changes, like a timestamp, after it. Then log cache_creation_input_tokens and cache_read_input_tokens for each call.
```

Checks shown under it:
- Check: run it twice. Does call two show cache reads?
- Check: does anything that changes sit before the long part?
