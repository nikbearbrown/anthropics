# Sources

*Verified 2026-09-12. Cowork is a fast-moving product — re-check before teaching.*

---

## Primary (Anthropic)

| Claim | Source |
|---|---|
| Cowork "brings Claude Code's agentic capabilities to knowledge work"; decomposes tasks, parallel workstreams, delivers spreadsheets/presentations | [Get started with Claude Cowork — Claude Help Center](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) |
| Runs in the cloud on Anthropic's servers in an isolated environment; sessions persist across desktop/web/mobile; "work continues if you close your laptop" | same |
| Desktop reads local files directly without uploads; folder-level permissions you control | same |
| Sessions isolated from your computer and network; explicit permission required before deleting files | same |
| Three permission modes — Manual, Auto, Skip | same |
| Limitations: no session sharing, some desktop-only features, higher usage consumption than standard chat | same |
| Not labeled a research preview as of this date; production feature on Pro, Max, Team, Enterprise | same |
| Plugins bundle skills, connectors, slash commands, sub-agents per job function; eleven open-sourced; "Built for Claude Cowork, also compatible with Claude Code" | [`knowledge-work-plugins/README.md`](../knowledge-work-plugins/) (local mirror) · [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| Connector lists per plugin (Slack, Notion, Linear, Jira, HubSpot, Snowflake, Databricks, BigQuery, PubMed, …) | same |

## Secondary (press — used only for dates and market framing)

| Claim | Source |
|---|---|
| Announced 2026-01-12 as a research preview; "computer agent" for non-technical users | [Aragon Research](https://aragonresearch.com/anthropic-claude-cowork/) · [TechRadar](https://www.techradar.com/pro/anthropics-new-cowork-tool-offers-claude-coding-help-to-non-experts) |
| Windows launch 2026-02-10 at parity with macOS; enterprise connectors incl. Google Drive, Gmail, DocuSign, FactSet | [CNBC, 2026-02-24](https://www.cnbc.com/2026/02/24/anthropic-claude-cowork-office-worker.html) |
| Positioning toward knowledge workers rather than software engineers | [Aragon Research](https://aragonresearch.com/anthropic-claude-cowork/) · [eMarketer](https://www.emarketer.com/content/anthropic-slips-daily-work-through-slackbot-claude-cowork) |
| "Same engine, two jobs" framing; Code in terminal/IDE, Cowork in desktop app | [DataCamp](https://www.datacamp.com/blog/claude-cowork-vs-claude-code) · [Forte Labs](https://fortelabs.com/blog/the-difference-between-claude-code-and-cowork/) · [Parallel](https://parallel.ai/articles/claude-cowork-vs-claude-code-which-agentic-tool-to-use-and-when) |

## Local (this tree)

| Claim | Source |
|---|---|
| Entire fact-check case study — counts, the Larkin/Eisenberg error, method differences, the Ch 12 catch, the file collision | [`factcheck-comparison-codex-vs-cowork.md`](../../../factcheck-comparison-codex-vs-cowork.md) |
| Claude Code terminal-side companion material | [`claude-code-101/`](../claude-code-101/) |
| A local Cowork plugin marketplace manifest exists | `/Users/bear/Documents/CoWork/cowork-marketplace/.claude-plugin/marketplace.json` |

---

## Claims deliberately excluded

Flagged so nobody adds them back later:

- **"Cowork uses the Computer Use API, captures 3.75 MP screenshots, and navigates your desktop like a human."** Appears on several SEO-oriented sites (`coworkerai.io`, `claudecowork.im`). This conflates Cowork with the separate Computer Use API. Anthropic's own documentation describes file-and-folder access plus connectors. **Do not repeat.**
- **"Cowork runs in a virtual machine isolated from the wider internet."** A third-party gloss. The documented language is "isolated environments separate from your computer and network" — close, but do not attribute the VM detail to Anthropic.
- **"Claude Code is more open to leaks and attacks."** Directionally defensible — local execution does carry your credentials and network reach — but as phrased it is a third-party opinion, not a documented comparison. [`01`](01-why-cowork-over-claude-code.md) and [`02`](02-when-claude-code-wins.md) make the argument from the documented permission models instead.

## Unsourced by design

Statements in this folder marked *(experience, not doc)*, plus all of the pedagogical framing — the "verifiable-vs-judged" axis in [`02`](02-when-claude-code-wins.md), the decision flowchart in [`03`](03-decision-guide.md), and the four common errors — are editorial. They are arguments, not facts, and should be attacked on their merits rather than checked against a source.
