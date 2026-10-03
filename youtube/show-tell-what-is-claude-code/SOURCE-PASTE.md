# Source: Claude Code product page (pasted by Bear, 2026-09-27)

**What this is.** The text of https://claude.com/product/claude-code as Bear pasted it on 2026-09-27 (reached from a LinkedIn ad; tracking parameters stripped, navigation and footer link lists dropped). **Why.** It is the source for the show-tell film "What Is Claude Code?". **Use.** Every claim in the film traces to a line here, or to the live docs at https://code.claude.com/docs/en/overview (attributed).

---

## Hero

Claude Code
Hand Claude a bug fix, test, or multi-day migration. Steer and review from your terminal, IDE, Slack, or web.
Claude Code is included in Claude Pro and Max plans.
[Download for macOS] [Read documentation]
Available for macOS, Linux, and Windows.
Other ways to use Claude Code: Terminal, Web, iOS, Android, GitHub, VS Code, JetBrains, Slack.

## Product mock (desktop app screenshot on the page)

Sidebar: Home, Code, New session, Routines, Customize, More. Pinned: "Add a dark mode toggle to settings". Scheduled: "Weekly dependency audit". Recents: "Fix the double-charge bug in checkout", "Write tests for the payments module", "Explain what this repo does", "Layout's broken on mobile", "Debug flaky CI tests". User: Susan Sample (a sample name).

Session "acme-storefront / Fix the double-charge bug in checkout":
- User: "We're seeing duplicate charges when customers double-click the pay button. Can you find and fix it?"
- Claude: "I can reproduce it: the checkout form fires two `POST /charges` requests when the button is clicked twice before the first response lands. Tracing where the idempotency key should be."
- "Read 3 files, searched the checkout flow"
- "Ran agent · Reproduce the double-submit against a test charge"
- Claude: "Root cause: `createCharge()` generates a new idempotency key per call instead of per checkout session, so the gateway treats the second click as a fresh charge. Fixing that and disabling the button while a charge is in flight."
- "Edited charges.ts +9 -3"
- Footer chips: "Auto", "Opus", "Extra high".

## Plans (Individual)

- Pro: "Claude Code is included in your Pro plan. Perfect for short coding sprints in small codebases." $17 per month with annual subscription discount ($200 billed up front). $20 if billed monthly.
- Max 5x: "Great value for everyday use in larger codebases." $100 per month.
- Max 20x: "Even more Claude Code included in your Max plan. Great value for power users with the most access to Claude models." $200 per month.
- "Usage limits apply. Prices shown don't include applicable tax. Price and plans are subject to change at Anthropic's discretion."

## Latest feature announcements

- Projects: Group related coding sessions so you can run and easily supervise multiple Claude agents at once. Available on Claude Code Desktop. (Blog, Sep 17, 2026)
- Auto mode by default: Claude Code now runs in auto mode by default on Pro, Max, and Team plans, so it can work longer while still catching risky commands. (Blog, Aug 7, 2026)
- Self-hosted environments: Run Claude Code sessions on your own infrastructure, inside your network and next to your internal services. Now in public beta. (Blog, Aug 6, 2026)
- Artifacts: Preview in-progress work as a live, interactive artifact built from your session context, and share it with your team. (Blog, Jun 18, 2026)

## What Claude Code can take on

"Claude Code builds the plan, asks clarifying questions, and handles work that runs for hours or days."

Install: `curl -fsSL https://claude.ai/install.sh | bash`

Tabs: Onboarding / Triage issues / Migrate code. The Onboarding tab shows a terminal transcript:

> I'm new to this codebase. Can you explain it to me?
> ⏺ I'll analyze the Excalidraw codebase structure and provide a high-level overview.
> ⏺ Analyze(what: "Excalidraw codebase structure …")
> Excalidraw is an open-source virtual whiteboard application with a hand-drawn style. … [Purpose, Architecture (monorepo: packages/excalidraw core, excalidraw-app/, support packages common/element/math/utils, examples, dev-docs), Key Features, Technology Stack (React, TypeScript, Firebase, Jotai, Vite, IndexedDB/LocalStorage)]

- **Code onboarding.** "Claude Code maps and explains entire codebases in a few seconds. It uses agentic search to understand project structure and dependencies without you having to manually select context files."
- **Turn issues into PRs.** "Stop bouncing between tools. Claude Code works with GitHub, GitLab, and your command line tools to read issues, write code, run tests, and open pull requests."
- **Run multi-hour refactors and migrations.** "Claude Code follows imports across the repo, runs your tests, and keeps going when something breaks."

## Meets you where you code

- Start in your terminal: "Super powerful terminal integration. Works with all your CLI tools alongside any IDE."
- Integrate with your editor: "Native extensions for VS Code (+ Cursor, Devin Desktop) and JetBrains IDEs."
- Access anywhere: "Quick access from browser, mobile app, or Claude on desktop. Great for parallel work or on-the-go coding."
- Kick off coding tasks in Slack.

## What developers are saying (customer quotes, attributed)

- Anton Biryukov, Staff Software Engineer (Ramp story): notebook EDA code → ask Claude to convert it into a Metaflow pipeline; "saves 1-2 days of routine (and often boring!) work per model."
- Fergal Reid, VP of AI (Intercom story): customer service quote (about Claude, not Claude Code).
- Simon Last, Co-founder (Notion story): "we decide what needs to happen, and smooth the process so it can build and verify end-to-end. A big part of my job now is to keep as many instances of Claude Code busy as possible."

## Connects with your favorite command line tools

"Your terminal is where real work happens. Claude Code connects with the tools that power development—deployment, databases, monitoring, version control. Rather than adding another interface to juggle, it enhances your existing stack."

## FAQ (questions only; answers collapsed in the paste except the first)

- How do I get started with Claude? "You can access Claude Code with a Claude Pro or Max plan, a Team or Enterprise plan, or a Claude Console account. Download Claude Code and sign in with your respective Claude or Console credentials."
- What kind of tasks can Claude Code handle? / How does Claude Code work with my existing tools? / Is Claude Code secure? / What are the system requirements? / How much does Claude Code cost? / Does Claude Code work with the Claude desktop app? / What is fast mode on Claude Code?

Further reading linked: Claude Code documentation (code.claude.com/docs/en/overview), Common workflows, "Using CLAUDE.md files", "Introduction to agentic coding", "How Anthropic teams use Claude Code", "Fix software bugs faster with Claude".
