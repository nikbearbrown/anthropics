# PROMPTS — show-tell-security-review-every-pr

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "Anthropic's claude code security review" so Kokoro doesn't spell the slash; "API" is left as written because Kokoro's lexicon says it right, while a spelled "A P I" reduces the A to a schwa):

```
Add anthropics/claude-code-security-review to this repo as a GitHub Action. Trigger it on pull requests only, read the API key from a repository secret, and exclude our vendored and generated folders. It must never run on untrusted pull requests, so tell me how to require approval for outside contributors. I'll treat its comments as leads to check, not verdicts.
```

Checks shown under it:
- Check: the workflow. Pull requests only, key in a secret?
- Check: repo settings. Outside contributors need approval?
