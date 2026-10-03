# PROMPTS — show-tell-half-price-if-you-can-wait

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "custom ID" for `custom_id` and "processing status" for `processing_status`):

```
Find the loop in this repo that calls the Claude API once per item. Rewrite it as a Message Batches job: give each request a valid custom_id built from the item's key, submit them as one batch, poll until processing_status is ended, then match each result to its item by custom_id and print any that errored.
```

Checks shown under it (the viewer runs these themselves):
- Check: one result per item, matched by custom_id?
- Check: are errored items printed, not dropped?
