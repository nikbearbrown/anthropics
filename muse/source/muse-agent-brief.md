# Meta Muse: What It Does, Security Concerns, and Business Model
As of October 3, 2026 (source: Bear's research brief — inspiration)

## 1. What Muse is
Muse is Meta's consumer AI agent, launched in the US on September 8, 2026, and marketed as the first personal AI agent "built for everyone." Its official framing is "personal superintelligence," with the TV tagline "AI That Hustles for You." Even Meta's own launch post describes it as just a first step: an agent that takes on more of your work.

Unlike a chatbot, Muse is designed to act. You give it a goal, it builds a plan, and it carries out the steps on its own, checking in for approval before consequential actions. It runs on Meta's Muse Spark models, and in Nik's experience these are noticeably less capable than GPT-6 Astra, Claude Fable, or Claude Opus.

Adoption has been fast: over 2.5 million US downloads in about two weeks.

## 2. What it does
### The core machinery
Every user gets a persistent Linux virtual machine in Meta's cloud, with its own browser, filesystem, and terminal. Muse keeps working there after you close the app. It's the same basic architecture as Claude Cowork and OpenAI Codex: a model plus a sandboxed computer plus connectors. The products differ mainly in target audience and default permissions.

### Consumer errands
Its main purpose. It can book travel, restaurants, and appointments; shop and check out through merchant partners; fill in forms and handle registrations; negotiate on your behalf; manage subscriptions; find event tickets (Ticketmaster is a launch partner, with purchases completing on Ticketmaster's side). Its real strength is endurance, not intelligence: waiting, refreshing, and grinding through tedious steps. It saves time, not thought.

### Interfaces
Web (muse.ai), plus iOS and Android apps. WhatsApp, with smart glasses announced as coming. A customizable persona: you can name it and give it an avatar, marketed with a friendly, Baymax-like robot character. A Mac app (added at Meta Connect, September 23) that can control macOS apps and read local files, Messages, Notes, and Mail. No Linux or native Windows app; those platforms get the web version.

### Connectors
Commerce first: Shopify checkout, OpenTable, Ticketmaster, Duffel flights, Instacart, Expedia, Link by Stripe (including one-time card numbers), plus ten retailers announced at Connect. Amazon blocked Muse, citing terms-of-service violations. Productivity: Gmail and Google Docs, Notion (since September 18), and a September 29 batch including Figma, Asana, Canva, Slack, Zoom, GitHub, QuickBooks, and Klaviyo. Meta-only: Instagram (including DMs), Facebook (including Marketplace), Threads, and Messenger. Missing: creative production tools such as Blender, Higgsfield, and DaVinci Resolve. Custom connectors: Muse can build a connector for any service with an API. Meta doesn't review them.

### Small business
Launched September 29, using the same plans. Muse connects to Meta Business Manager (Instagram analytics, Facebook Pages, Meta ad accounts), drafts posts and ad campaigns for review, reads QuickBooks financials, and works across tools like Klaviyo and Shopify's merchant side. Meta says nothing publishes, sends, or spends without approval.

### Developer-ish use
Because the cloud VM has a terminal, Muse can clone GitHub repos, write code, and open pull requests through the GitHub connector. This works, but it isn't what the product is for, and Meta controls it through pricing rather than product design. The sanctioned developer route is the Muse Spark API.

## 3. Pricing
| Tier | Price | Weekly allowance |
| Free | $0 | 100M Muse tokens |
| Power | $20/month | 500M |
| Maximum | $100/month | 3B |
All tiers have the same features; you pay only for volume. A payment card is required even for the free tier. "Muse tokens" may not map one-to-one onto raw model tokens. Muse Spark API coding pricing: $1.25 per million input tokens and $4.25 per million output, or $0.10/$0.20 with data sharing.

## 4. The business model
Stated model: transaction fees. Meta takes a small cut of transactions Muse completes, paid by merchants, not users, much like an affiliate commission. Users never see a charge, but merchant costs tend to work their way into prices eventually. Secondary revenue: subscriptions for heavy users, Muse Spark API sales. The ad business, from the advertiser side: Meta says there are no ads inside Muse, but Muse helps businesses buy Meta ads — lowering the barrier for small businesses, keeping advertisers inside Meta's ecosystem, closing the loop (ad → tracked purchase → sometimes the transaction). What Muse browses at merchants can still shape the ads you see elsewhere on Meta's apps. Training data: on by default (opt-out available); it improves the Spark models used across Meta's apps and its paid API. Strategic goal: own the intent layer — the point where people say what they want before money changes hands. Skepticism: one analysis estimates only about 11 of the average 47 monthly consumer payments are realistic to automate, suggesting transaction fees alone may not carry the business. Who it's designed for: non-technical consumers and small-business owners. Technical users running code workloads on the free tier are pure cost to Meta — a side effect of the subsidy, likeliest target when the free tier tightens.

## 5. Security concerns (summary)
- Full Disk Access instead of folder-level access (Mac app covers the entire disk; a behavioral promise, not a technical boundary).
- Deny-list instead of allow-list: violates fail-safe defaults (Saltzer and Schroeder, 1975).
- "Optional" in name only: without Full Disk Access the Mac app can do little locally.
- Known vulnerabilities: Malwarebytes zero-day (dictation traffic redirect → auth token theft); runtime data exposure (~6.8 GB incl. SSH keys); early prompt-extraction reports.
- Data handling depends on policy, not cryptography: training on by default; no published independent audit of ad-system separation; every file Muse reads is processed in Meta's cloud.
- Credential exposure: tokens pasted into chat live in Meta's cloud; anything on a Full-Disk-Access machine is readable.
- Prompt injection: agents reading untrusted content can be steered; failure probability is adversarial, not random.
- Approval fatigue: repeated prompts become reflex approvals.
- Trust by design: the mascot is a deliberate trust shortcut.
- Conflicts of interest in business use: affordability advice, self-graded reporting, narrow (Meta-only) optimization, lock-in.
- Platform dependence: features developers rely on can change without warning.

## 6. How the concerns were resolved (Nik's setup)
Assume breach, bound the blast radius, enforce limits outside the agent. Mac app removed from the main machine (verified: no processes, no launch agents, no app left). Web-only via muse.ai in a dedicated browser profile. Muse works only in its own cloud VM on public sandbox repos; authenticates via GitHub connector as a dedicated bot account; opens PRs only; branch protection + CODEOWNERS; Claude Code's GitHub Action reviews; deterministic CI; a burner MacBook with no Muse installed renders. General rules: an agent's access is the attacker's access; ask how bad it gets, not how likely; caps belong outside the agent; irreversible actions get a human; protect the short list (email, money, credentials, public voice) with real walls.

## Sources (from the brief)
Meta, Introducing Muse — https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ · Meta Help Center, Muse on Mac · Axios, Meta debuts Muse (2026-09-08) · TechCrunch, Muse for small businesses (2026-09-29) · CNBC, Muse and the Amazon block (2026-09-27) · Malwarebytes, Muse zero-day (2026-09) · Pivot to AI, Muse security critique (2026-09-28) · Postfast, Muse connectors list · Tech Insider, Muse launch and pricing · The Rundown, Muse desktop setup guide · Coursiv, Muse privacy and pricing
