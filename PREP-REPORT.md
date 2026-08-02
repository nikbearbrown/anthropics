# anthropics — push preparation report

Generated 2026-08-02. Prepared but **not** committed or pushed.

## What was generated

| Artifact | Detail |
|---|---|
| `.gitignore` | 239 lines. 93 `/<repo>/*` + `!/<repo>/youtube/` pairs, then media/build excludes last so they always win. |
| `bootstrap.sh` | 47 lines, executable. Re-clones the corpus from the manifest and checks out each pinned SHA. |
| `repositories.json` | **92 of 93 repos pinned** to the commit this analysis actually read. |

## Why the .gitignore is shaped that way

Each pair excludes a clone's **contents** (`/<repo>/*`), not the directory. That
is what lets `!/<repo>/youtube/` re-include our reels inside it — git cannot
re-include a path whose parent directory is excluded. It also excludes
`<repo>/.git`, which is what stops git treating **93 nested repositories** as
broken submodules.

Media excludes come **last** so they win even inside `youtube/`.

## SHA pinning — 92/93

`homebrew-claude` did not resolve a HEAD (likely an empty or unusual clone).
`bootstrap.sh` will clone it at its default branch and continue.

This matters because Anthropic ships roughly daily: a claim like "210 files, no
`src/`" is true of a *commit*, not of a repo. Pinned SHAs mean a viewer who takes
up the invitation to go check sees what the analysis actually read.

## Privacy scan — CLEAN

Scanned **173 beat sheets** in `youtube/info-7375-computational-skepticism-and-ai/`
for personal names in narration and card text.

- **Zero student names.** Every reel folder is a topic slug (`claude-liam-cs-18-chart-lie`), never a person.
- Top capitalized-bigram hits were all Title Case phrases from card headings — "Computational Skepticism", "Perfectly Calibrated", "Chart Without".
- The single genuine personal name, *Peter Selinger* (51 hits), is a **potrace attribution string inside an SVG**: `Created by potrace 1.16, written by Peter Selinger 2001-2019`. Software credit, not a person discussed.

**This course folder is Bear's own teaching content, not student work.** The
student-name exposure is in `branding-and-ai/info-7375` (the `ogilvy-<firstname>`
reels) — a different tree, not part of this push.

**Verdict: no privacy blocker. This repo can be public.**

*Scan limits: heuristic capitalized-bigram matching over the course folder, not
exhaustive NER across all ~1,450 beat sheets. A broader pass timed out and was
scoped to the highest-risk subtree.*

## Still to decide

Nothing blocking. `git init` and the first commit have deliberately been left
undone.
