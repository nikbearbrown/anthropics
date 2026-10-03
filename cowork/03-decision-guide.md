# The Decision Guide

*Three tools, one question, four cases people get wrong.*

---

## The one question

> **How will you know it is done?**

| Your answer | Use |
|---|---|
| "A test, a build, or a diff will tell me." | **Claude Code** |
| "I will read it and judge it." | **Cowork** |
| "I just need to know a thing." | **Claude.ai chat** |

Everything below elaborates this. If you remember only the table, you will be right most of the time.

---

## The three surfaces

| | Claude.ai chat | Cowork | Claude Code |
|---|---|---|---|
| **Lives in** | Browser / app | Claude Desktop app | Terminal / IDE |
| **Runs on** | Anthropic servers | Anthropic servers, isolated | **Your machine** |
| **Material** | The conversation | Folders of documents | A repository |
| **Output** | An answer | Finished files (xlsx, pptx, docx, md) | Commits, diffs, scripts |
| **Sees your files** | Uploads only | Folders you grant | Everything your user can |
| **Git** | No | No | **Yes** |
| **Shell / local tools** | No | No | **Yes** |
| **Survives closing laptop** | N/A | **Yes** | No |
| **Horizon** | One turn | Hours | Hours |
| **Cost profile** | Lowest | Higher than chat | Higher than chat |
| **Plugins & skills** | — | **Yes** | **Yes** (same format) |

---

## Flowchart

```
Is the deliverable an artifact, or an answer?
│
├─ An answer ─────────────────────────────► claude.ai chat
│
└─ An artifact
   │
   ├─ Does it need git, a shell, a local
   │  renderer, a dev server, or a GPU? ───► Claude Code
   │
   ├─ Does a script / test / build define
   │  "correct"? ──────────────────────────► Claude Code
   │
   ├─ Is the data barred from leaving
   │  your machine? ───────────────────────► Claude Code (local)
   │
   ├─ Must it be reproducible by someone
   │  else, later? ────────────────────────► Claude Code
   │
   └─ Otherwise — documents, research,
      spreadsheets, decks, synthesis,
      multi-hour, judged by reading ───────► Cowork
```

Note the asymmetry: Claude Code has four gates and Cowork is the default fall-through. That is deliberate and it is the correct bias. **Most knowledge work has none of those four properties**, and people reach for the terminal out of habit rather than need.

---

## The four cases people get wrong

### 1. Using chat for a job with an artifact

The tell: you are copy-pasting output into a file by hand. If you paste more than twice, you picked the wrong surface. Both agentic tools write to disk; let them.

### 2. Using Claude Code because you *can*

The most common error among engineers. The terminal is familiar, so it gets used for a literature review, a grant narrative, a slide deck. You then spend the session fighting environment problems that have nothing to do with the work. Familiarity is not fit.

### 3. Using Cowork for something that needed to be reproducible

The most expensive error, because it is invisible until the second run. You get an excellent deliverable, then six weeks later you need the same pass on a different book, and the procedure is gone. **If you think you will rerun it, get the script.**

### 4. Treating the sandbox as a correctness guarantee

The isolation boundary constrains what the agent can *break*. It says nothing about whether the output is *right*. A sandboxed agent will hand you a confidently wrong spreadsheet with the same equanimity as an unsandboxed one. Verification is still your job.

---

## The case for not choosing: use both

The fact-check in [`04-case-study-factcheck.md`](04-case-study-factcheck.md) is the argument. Two agents, same prompt, same corpus, different methods — and the union caught something neither caught alone, while the agreement on a single real error was far stronger evidence than either pass by itself.

For high-stakes work, **agreement between independently-configured agents is evidence in a way that one agent's confidence is not.** That is worth more than picking the right tool.

The practical pattern:

1. **Cowork** for the granular, reader-visible pass — per-claim sourcing, human-legible reports.
2. **Claude Code** for the reproducible pass — a committed script anyone can rerun.
3. Compare. Where they disagree is where you look.

And the one warning from that run: **both wrote to the same files**, leaving sixteen chapters carrying two overlapping reference blocks, with one pass overwriting the other's reports. Two agents on one corpus need separate output paths agreed in advance.

---

## A note on the false dichotomy

Skills and plugins use the **same format on both surfaces** — Anthropic's own knowledge-work plugins say "Built for Claude Cowork, also compatible with Claude Code."

So "which should I learn?" is largely the wrong question. Learn to write skills. They run on both. The surface is a deployment decision you make per task, and you can make it differently tomorrow.
