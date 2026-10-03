# PROMPTS — show-tell-loop-that-wont-let-go

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown in full and read in full (spoken as "Slash ralph loop, and in quotes: … Output COMPLETE in promise tags … Then: completion promise, COMPLETE. Max iterations, ten."). Needs the Ralph Loop plugin from the official directory (`/plugin install ralph-loop@claude-plugins-official`), in a repo you own with failing tests:

```
/ralph-loop "Make every test in this repo pass. Do not delete or skip any test. Run the full suite each lap. Output <promise>COMPLETE</promise> only when every test passes." --completion-promise "COMPLETE" --max-iterations 10
```

Checks shown under it (the viewer runs these themselves):
- Check: run the tests yourself. All pass?
- Check: the git diff. Any test deleted or skipped?
