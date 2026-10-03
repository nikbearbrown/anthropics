# PROMPTS — show-tell-four-reviewers-and-a-sieve

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "Claude dot M D", "from zero to a hundred" and "eighty"), pasted into Claude Code on a branch with changes:

```
Review my branch's changes against main the way the code-review plugin does. Run five separate passes: CLAUDE.md rules, obvious bugs in the changed lines, git blame and history, comments on earlier pull requests that touched these files, and code comments in the changed files. Score each issue 0-100 for confidence that it is real. List every issue with its score, mark which ones survive a cut at 80, and post nothing.
```

Checks shown under it (the viewer runs these themselves):
- Check: is each survivor on a line you changed?
- Check: read one dropped issue. Was it noise?

The prompt says "post nothing" on purpose: the plugin's own command posts a comment on the pull request, and a first try should not.
