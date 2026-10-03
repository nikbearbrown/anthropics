# What Cowork Actually Is

*Mechanics before advocacy. You cannot argue about which tool to use until you know what the tool does.*

---

## One sentence

Cowork brings Claude Code's agentic capabilities to knowledge work — it breaks a complex goal into subtasks, manages parallel workstreams, and returns finished artifacts (spreadsheets, decks, documents) without step-by-step direction.

That phrasing is Anthropic's own, and the important word in it is **"brings."** Cowork is not a new agent. It is the existing agent given a different front door and a different kind of workpiece.

---

## Where it runs — and this surprises people

Cowork sessions run **in the cloud, on Anthropic's servers, in an isolated environment**. Not on your laptop.

This has three consequences that matter more than they sound:

1. **Work survives a closed laptop.** A long job keeps going. You are not babysitting a terminal.
2. **Sessions are account-scoped, not machine-scoped.** Start on the desktop, check it from your phone.
3. **It is isolated from your computer and your network.** The sandbox is a real boundary, not a UI convention.

Contrast with Claude Code, which runs as a process on your machine, with your shell, your credentials, your network. That is a genuine capability *and* a genuine exposure — see [`02-when-claude-code-wins.md`](02-when-claude-code-wins.md).

## How it reaches your files

On desktop, Claude reads local files directly through the Claude Desktop app — no manual uploading. Access is **folder-level and granted by you**. On web and mobile you retain the same control over which folders are readable and writable.

So the mental model is: *a sandboxed worker that you hand a specific drawer of the filing cabinet,* rather than *a process with your full user permissions.*

## The permission model

Three modes:

| Mode | Behavior |
|---|---|
| **Manual** | Asks for approval before acting. |
| **Auto** | Reviews its own actions for safety, proceeds. |
| **Skip** | No checks. |

Deletion is special-cased: **Claude requires explicit permission before deleting files**, independent of mode.

> **Teaching note.** "Skip" is the one to talk about in class. Every agentic system eventually offers a mode that turns off the brakes, and every user eventually turns it on because the prompts are annoying. That is a predictable human-factors failure, not a Claude-specific one. Worth an hour of discussion in a skepticism course.

## Plugins and skills

This is the part most comparisons miss, and it is the part that matters most for serious use.

A plugin bundles the skills, connectors, slash commands, and sub-agents for a specific job function. Anthropic open-sourced eleven of them in [`knowledge-work-plugins`](../knowledge-work-plugins/) — mirrored in this tree — covering productivity, sales, customer support, product management, marketing, legal, finance, data, enterprise search, bio research, and plugin management itself.

The line in that repo's README is the whole positioning argument in nine words:

> Built for Claude Cowork, also compatible with Claude Code.

**Same plugin format. Both surfaces.** Which means the skills you write are not a bet on one tool. This is why the "which should I learn?" framing is mostly a false choice.

## Stated limitations

From Anthropic's documentation, not from me:

- **No session sharing** with other people.
- **Some features are desktop-only.**
- **Higher usage consumption** than standard chat. Agentic loops cost more than answers. Budget accordingly.

## Status and timeline

- **2026-01-12** — announced as a research preview.
- **2026-02-10** — Windows, at parity with macOS.
- **As of 2026-09-12** — no longer labeled a research preview; a production feature on paid plans (Pro, Max, Team, Enterprise).

That eight-month arc is itself worth noting: if your course materials say "research preview," they are stale.

---

## What Cowork is *not*

Clearing up three things circulating in secondary coverage:

- **It is not a desktop computer-use agent.** Several third-party articles describe Cowork as screenshotting your screen and driving your GUI like a human. That conflates it with the Computer Use API. Cowork's documented model is file-and-folder access plus connectors — not screen scraping. Do not repeat that claim.
- **It is not "Claude Code for people who can't code."** That framing is condescending and also wrong: the constraint is the artifact, not the operator. Plenty of engineers should be using Cowork for their design docs.
- **It is not local.** Say this out loud when teaching. People assume the desktop app implies desktop execution. It does not.

---

*Sources for every claim above: [`05-sources.md`](05-sources.md).*
