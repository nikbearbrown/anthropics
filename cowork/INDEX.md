# Cowork — Why This One, and When Not

*Folder created 2026-09-12. Sibling to `claude-code-101/`, which covers the terminal side.*

---

## The short answer

**Claude Code and Cowork are the same agent wearing different clothes.** Same model, same agentic loop, same skills-and-plugins substrate. What differs is *where the work happens* and *what the work is made of*.

- **Claude Code** — terminal and IDE. The material is a repository: source files, git history, a test suite, a build. It runs on your machine with your toolchain.
- **Cowork** — the desktop app. The material is a folder of documents: manuscripts, spreadsheets, decks, PDFs, research notes. It runs in an isolated cloud environment that reaches into folders you grant it.
- **Claude.ai chat** — neither. One turn, one answer, no persistent file tree, no multi-hour job.

So the honest form of "why Cowork rather than Claude Code" is **not** "Cowork is better." It is:

> Choose by the *shape of the artifact*, not by how technical you feel.

If the deliverable is a commit, use Code. If the deliverable is a document, use Cowork. If you are asking a question rather than producing an artifact, use chat and stop overthinking it.

---

## Read in this order

| File | What it settles |
|---|---|
| [`00-what-cowork-is.md`](00-what-cowork-is.md) | What Cowork actually is, mechanically — where it runs, how it touches files, what the permission model is. Sourced. |
| [`01-why-cowork-over-claude-code.md`](01-why-cowork-over-claude-code.md) | The five real arguments for Cowork, each with its limit stated. |
| [`02-when-claude-code-wins.md`](02-when-claude-code-wins.md) | The honest counter-case. Longer than file 01 on purpose. |
| [`03-decision-guide.md`](03-decision-guide.md) | The picker. A table, a flowchart, and the four cases people get wrong. |
| [`04-case-study-factcheck.md`](04-case-study-factcheck.md) | A real Cowork job from this tree: the two-book fact-check, cross-validated against Codex. |
| [`05-sources.md`](05-sources.md) | Every external claim in this folder, with its URL and date. |

---

## The one-paragraph version, for a slide

Anthropic built Claude Code for people whose work product is a repository. Then it turned out that the *agentic* part — decompose a goal into subtasks, run them in parallel, check your own output, hand back something finished — was never actually about code. It was about any long-horizon task with files in it. Cowork is that same loop pointed at documents instead of source, in a window instead of a terminal. The reason to use it is not that it is easier. It is that a fifty-chapter manuscript is a codebase that happens to be in prose, and Cowork is the surface that treats it that way without asking you to `cd` anywhere.

---

## Caveat on sourcing

Product facts here were verified on **2026-09-12** against Anthropic's own documentation and the `knowledge-work-plugins` repo mirrored in this tree. This is a fast-moving product — it launched January 2026 and changed materially twice by February. **Re-verify before teaching from it.** Claims that come from my own use rather than from documentation are marked *(experience, not doc)*.
