# Why Cowork Rather Than Claude Code

*Five arguments. Each one gets its limit stated in the same breath, because an argument without its boundary is advertising.*

---

## 1. The artifact is a document, and documents are not repositories

This is the whole thing. Everything below is a footnote to it.

A repository has properties Claude Code is built around: a git history to diff against, a test suite that returns a hard pass/fail, a compiler that rejects nonsense, a file tree with semantic structure. Claude Code's entire verification loop leans on those.

A manuscript has none of them. There is no `make test` for "is chapter 8's argument sound." The output of knowledge work is judged by reading it.

Cowork is shaped for that: produce the artifact, put it on disk in finished form, let a human read it. It builds spreadsheets with working formulas and decks you can actually present — not descriptions of them.

**The limit:** this cuts the other way when your prose *does* have a test suite. If you have built lint rules, link checkers, citation validators, and a render pipeline — as this tree has — your manuscript *is* a repository, and Claude Code's verification loop is the better fit. See [`02`](02-when-claude-code-wins.md).

---

## 2. Work that outlives the session

Cowork runs on Anthropic's servers, so **closing the laptop does not kill the job**, and the session is reachable from another device.

For a four-hour job across sixteen chapters, this is not a convenience feature. It is the difference between a job that completes and a job you have to nurse. Claude Code dies with its terminal, its machine, its sleep cycle, its VPN drop.

**The limit:** cloud execution means your files travel to Anthropic's infrastructure. For most work that is fine and is in fact *safer* than the alternative. For anything under an NDA, a data-use agreement, an IRB protocol, or FERPA, "it leaves the machine" is a compliance question with a real answer that is sometimes no. Ask before assuming.

---

## 3. The sandbox is a feature, not a training wheel

Cowork sessions run isolated from your computer and your network, with folder-level grants and a hard stop before deletion.

Claude Code runs with **your** shell, **your** credentials, **your** network reach. Every capability Claude Code has is one you also have — including the destructive ones. The blast radius of a confused agent is the blast radius of a confused you.

The usual framing is that Cowork is the beginner-safe option. Invert it: **Cowork has a principled permission boundary and Claude Code has your whole user account.** For a long autonomous run you are not watching, the sandbox is the more defensible engineering choice, not the more timid one.

**The limit:** the boundary is only as good as the mode. Set permissions to Skip and you have opted out of most of this argument. And an isolated sandbox does not make the *output* correct — it constrains what the agent can break, not what it can get wrong.

---

## 4. Connectors reach where a terminal does not

Cowork integrates with configured connectors — Google Drive, Gmail, DocuSign, FactSet, and the long tail bundled into the open-source plugins (Slack, Notion, Linear, Jira, HubSpot, Snowflake, Databricks, BigQuery, PubMed, and so on).

For knowledge work this is usually the actual bottleneck. The hard part of "synthesize last quarter's customer escalations" is never the synthesis — it is that the material lives in Intercom, Slack, and a Drive folder. Claude Code can reach those through MCP, but you are assembling the plumbing yourself.

**The limit:** each connector is a new trust edge. Content arriving from Slack, email, or a web page is *data*, not instructions — and an agent with both a mail connector and a document connector is a prompt-injection surface with a delivery mechanism attached. Treat connector breadth as a risk budget you are spending, not a free win.

---

## 5. You stop paying the terminal tax

The terminal tax is not "I can't type commands." It is the accumulated overhead of environment: which Python, which venv, which node version, why does this shell not have that on PATH, why did the launchd agent fail to read `~/Documents`.

That last one is not hypothetical in this tree. Environment friction is a real tax, and for a document job it buys you nothing.

**The limit:** you are trading control for convenience, and sometimes you needed the control. The terminal tax is also what buys you reproducibility — a script you can rerun, commit, and hand to someone else. See the next file.

---

## What none of these arguments say

They do not say Cowork is more capable. Same model, same agentic architecture — the difference is where they run and who they serve.

Anyone claiming one is "smarter" is selling something. The engine is shared. **You are choosing a surface and a permission model, not an intelligence.**
