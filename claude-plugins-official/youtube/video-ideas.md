# Claude Code Plugins Directory Video Ideas

## Candidate 1 — Why pairing-code auth prevents bot spam but feels backwards

- Source: `external_plugins/discord/README.md`, `external_plugins/telegram/README.md`, `external_plugins/imessage/README.md`
- Topic: Access control via pairing state machine
- Hook: A brand-new bot is live and receiving DMs from strangers, but the security mechanism is to send yourself a pairing code first.
- Key case: Discord bot launches. Strangers DM it; bot replies with a 6-character code. You DM your own bot, get code `ABC123`, run `/discord:access pair ABC123` in Claude. Bot switches to `allowlist` mode and stops accepting pairing codes entirely.
- The Question: Access control systems usually whitelist trusted users up front, so why does this bot start by handing out pairing codes to everyone, then suddenly stop?
- Core idea: A two-phase state machine solves a bootstrapping problem. The bot can't know your user ID without talking to you, but can't restrict to your ID without knowing it. So it runs in `pairing` mode (accepts codes only from you, since you're the only one who can execute `/discord:access pair` in your Claude session), captures your ID via your pairing code, then flips to `allowlist` mode (rejects all DMs from unknown IDs). The code is a proof-of-access: only you could have received and entered it.
- Visual object: A state machine with two circles (pairing-mode and allowlist-mode), an arc labeled `pair <code>` between them, and beside each circle a rule (pairing: "reply to all DMs with code"; allowlist: "reject unless in access.json").
- Manim move: morph
- Example seed: You deploy a personal Slack relay for Claude. On launch, policy is `pairing`. A coworker texts it; bot replies `"pairing-code: X1Y2Z3"`. You text it from your phone; bot replies `"pairing-code: A9B8C7"`. You run `/slackbot:access pair A9B8C7` in Claude. Next message from coworker gets silently rejected. Bot is now in allowlist mode.
- Length band: 2–3 min
- Still lanes: c2v (state-machine diagram)
- Prerequisites: state machines, authentication, access control
- Exclusions: how to add users to the allowlist after pairing; the specific pairing-code generation algorithm
- Score: 10/10

## Candidate 2 — Why the same assistant code runs on Discord, Telegram, and iMessage unmodified

- Source: `external_plugins/discord/README.md`, `external_plugins/telegram/README.md`, `external_plugins/imessage/README.md`
- Topic: MCP servers as platform adapters
- Hook: The same assistant uses `reply`, `react`, and `edit_message` on Discord, Telegram, and iMessage — even though each platform's API is completely different.
- Key case: Discord exposes `reply`, `react`, `edit_message`, and `fetch_messages` (Discord has history). Telegram exposes `reply`, `react`, and `edit_message` but *not* `fetch_messages` (Telegram Bot API has no history). iMessage exposes `reply` and `chat_messages` (history, no reactions). Yet ask an assistant "reply with this" on any of the three, and it works, because each platform's MCP server wrapper translates its API into a common interface.
- The Question: Platform APIs are fundamentally different — some have history, some don't; some have reactions, some don't — so how does the same assistant code work on all three?
- Core idea: An MCP server acts as a *platform adapter layer*. Each plugin (discord, telegram, imessage) wraps its platform's API in a standard toolset (`reply`, `react`, `edit_message`). If a tool doesn't exist on that platform, the plugin omits it — but core tools work everywhere. The assistant never talks to the platform; it talks to the MCP server, which handles translation. Switching platforms means swapping the MCP server, not rewriting the assistant.
- Visual object: A three-lane diagram. Lane 1 (left): platform APIs (REST, BotFather polling, AppleScript). Lane 2 (middle): MCP servers (translate). Lane 3 (right): unified tools (`reply`, `react`, `edit`, `fetch`). Arrows flow left-to-right; MCP server is the bottleneck.
- Manim move: split
- Example seed: You build an assistant that replies with `reply(text="got it")`. Deploy on Discord: MCP server translates to `POST /channels/{id}/messages`. Deploy on Telegram: MCP server translates to `sendMessage`. Deploy on iMessage: MCP server translates to `osascript tell application "Messages" send …`. Same assistant code everywhere.
- Length band: 3–5 min
- Still lanes: geo (three-lane diagram), c2v (translation flow)
- Prerequisites: MCP protocol, API abstraction, platform differences
- Exclusions: why specific tools are missing on specific platforms; implementation details of each MCP server; the full tool reference for each platform
- Score: 9/10

## Candidate 3 — Why modernization code breaks: a pipeline gates each rewrite step until prerequisites are done

- Source: `plugins/code-modernization/README.md`
- Topic: Gated command sequence enforcing knowledge accumulation
- Hook: Teams rewrite legacy code without understanding it first, ship code that compiles but behaves differently — yet a simple pipeline refuses to run each command until earlier steps complete.
- Key case: A team runs `/modernize-uplift billing 4.8 8` to jump from .NET Framework to .NET 8. The command fails: "No brief found — run `/modernize-brief` first." Brief fails: "No extract-rules artifact — run `/modernize-extract-rules` first." They climb backward: extract-rules fails (no map), map fails (no assessment), preflight warns the build doesn't work on this machine. They fix the build, then climb back up: preflight passes → assess → map → extract-rules → brief (human approval gate) → uplift runs. Each gate unlocks the next.
- The Question: Why does the command order matter so much that the system refuses to let you skip ahead, and what does each step teach that makes the later steps safer?
- Core idea: The pipeline enforces *sequential knowledge accumulation*. Preflight proves you can build the code (hard blocker). Assess inventories complexity and debt. Map reveals data flow and dependencies. Extract-rules mines business logic into testable assertions. Brief (a human-approval gate) synthesizes discovery into a phased execution plan. Only then do transform/uplift/reimagine run — and they read the discovery artifacts (the map, the rules, the brief) to avoid mistakes. Uplift adds a second gate: pilot one module in-session, write a playbook, then parallelize the rest. You can't rewrite without understanding; you can't fan out without proof that the first one works.
- Visual object: A flowchart with 7 boxes in a vertical sequence (preflight → assess → map → extract-rules → brief → reimagine|transform|uplift → harden). Edges are gates: brief is marked RED (human approval), uplift's parallel step marked ORANGE (requires pilot playbook). Backward-pointing arrows show "you skipped this step."
- Manim move: accumulate
- Example seed: Team wants to uplift a monolith. Preflight discovers it needs a custom build tool they haven't shipped. They ignore the warning and write the brief anyway. Uplift fans out to 4 modules. Module 1 fails immediately: missing build tool. If they'd followed the gate, brief would've required a remediation plan before uplift even unlocked.
- Length band: 3–5 min
- Still lanes: geo (vertical flowchart), raster (color gates)
- Prerequisites: gated workflows, risk management, software archaeology
- Exclusions: specific upgrade deltas or version-compatibility catalogs; the business-rules extraction algorithm; how each command's output artifact is structured
- Score: 9/10

## Candidate 4 — Why a plugin's name is forever, and the hidden redirect that lets you rename it anyway

- Source: `README.md`
- Topic: Slug immutability and transparent migration via renames map
- Hook: A plugin ships as `auth-v1` with a thousand users installed. Later you realize `auth` would've been better, but renaming would orphan all thousand installs.
- Key case: Plugin `auth-v1` has 1000 active installs (stored in each user's config under the slug `auth-v1`). The team publishes `auth-v1` v2.0 and wants to rename it to `auth`. If they just change the name, the 1000 old installs stay broken: Claude Code looks for `auth-v1`, which no longer exists as a published slug. The team instead adds one line to the marketplace: `"renames": { "auth-v1": "auth" }`. On the next sync, Claude Code reads this map, rewrites each user's config from `auth-v1` to `auth`, and uninstalls/reinstalls silently.
- The Question: How can you rename a published plugin without forcing all existing users to manually fix their config?
- Core idea: The `renames` map in `.claude-plugin/marketplace.json` is a *transparent redirect table* for plugin slugs. When Claude Code syncs, it reads this map and rewrites old slugs to new slugs in the user's local config. The immutability rule (once a slug is published, its name never changes in the source) prevents config collisions and name confusion. The renames map is the escape hatch: if you must rename, add a line and wait for the next sync — no forced updates, no broken configs.
- Visual object: A two-column table (Old Slug | New Slug) with one example row, annotated "Claude Code reads this on every sync and rewrites user configs silently."
- Manim move: morph
- Example seed: Plugin `db-migrations` ships with 500 users. v2.0 realizes it should be `db-versions`. Add `"db-migrations": "db-versions"` to renames. Next sync, 500 users' configs change from `db-migrations` to `db-versions` automatically. No manual steps, no breakage.
- Length band: ~1 min
- Still lanes: raster (table)
- Prerequisites: plugin distribution, backwards compatibility, configuration management
- Exclusions: version numbering in plugins; why slugs must be immutable (config storage semantics); the full marketplace.json schema
- Score: 8/10

## Candidate 5 — How Discord's history API enables lazy loading, but Telegram's absence forces eager download

- Source: `external_plugins/discord/README.md`, `external_plugins/telegram/README.md`
- Topic: API constraint driving design tradeoff
- Hook: Two bots receive the same image attachment, but Discord downloads it only when asked, while Telegram downloads every photo immediately.
- Key case: Discord bot calls `fetch_messages` to pull the last 50 messages (Discord has history). The response marks 3 with `+Natt`. Bot skims all 50, calls `download_attachment` for the 3 marked, and downloads only those (lazy-loading). Telegram bot receives one message at a time as it arrives (Telegram Bot API has no history). Every message with a photo auto-downloads immediately to `inbox/`. Later, an assistant asks "what photos were sent yesterday?" — Discord can answer (history exists), Telegram can't (messages are gone, only current photos exist in inbox).
- The Question: Why does Discord lazy-load attachments (download on demand) while Telegram eager-loads (download immediately), even though both are messaging platforms?
- Core idea: The loading strategy is *forced by the API's constraints*. Discord's history API lets the server fetch message metadata without downloading files, so it can download only the files the assistant cares about (bandwidth-efficient, but requires history lookup). Telegram's Bot API provides neither history nor search; the bot sees messages only as they arrive. To avoid losing photos, the server downloads every attachment immediately (bandwidth-wasteful, but nothing is lost). The tradeoff: Discord saves bandwidth but requires history; Telegram wastes bandwidth but needs no memory of the past.
- Visual object: Two side-by-side timelines. Discord: message-list (50 items, 3 marked `+Natt`) → download 3. Telegram: message arrives → auto-download → next message.
- Manim move: compare
- Example seed: Assistant on Discord asks "show the images from last week," receives 7 files (lazy-loaded from history). Same assistant on Telegram asks the same question and gets "I don't have history — send me the image again." The bot can't retrieve old photos because it never had a history API to query.
- Length band: 2–3 min
- Still lanes: geo (two timelines), raster (attachment markers)
- Prerequisites: API design constraints, bandwidth/storage tradeoffs, platform differences
- Exclusions: why Telegram Bot API lacks history (product/business reasons); the full list of API differences between platforms; how the assistant actually decides when to download
- Score: 8/10

## Candidate 06 — Why enabling SMS breaks access control even when your number is allowlisted

- Source: `external_plugins/imessage/README.md`
- Topic: SMS spoofing as access-control bypass via unverified sender fields
- Hook: Your phone number is on the allowlist, a stranger sends a message from your number, and the allowlist passes it through.
- Key case: `IMESSAGE_ALLOW_SMS=true` is set; `+15551234567` is in `access.json`. An attacker uses an SMS gateway with `From: +15551234567`. The iMessage plugin receives it, checks access.json, finds `+15551234567`, and forwards the message to Claude. The attacker has bypassed access control using a number they do not own — the allowlist check passed because the `From` field matched, not because identity was verified.
- The Question: The allowlisted number appears in the message and the allowlist check passes, so why does enabling SMS create a bypass that iMessage mode does not?
- Core idea: iMessage binds a phone number to an Apple ID and cryptographically authenticates that the sender holds that Apple ID — the number in the message is a verified fact. SMS has no such binding: the `From` field is an unverified claim any gateway can set to any value. The allowlist check compares a *claimed* identity to a trusted list. When the claimed identity cannot be verified, the allowlist is reduced to a string match against user-controlled input. Default `IMESSAGE_ALLOW_SMS=false` is not about SMS traffic volume — it is about the trust model behind the sender field.
- Visual object: Two vertical authentication chains side by side. Left (iMessage): device → Apple ID server (cryptographic proof) → verified sender ID → allowlist check → forwarded. Right (SMS): gateway injects `From: +15551234567` → no verification step → allowlist check → forwarded. Red gap where verification would appear on the right.
- Manim move: compare
- Example seed: Allowlist contains `+15551000001`. An SMS gateway sends `From: +15551000001, Body: "show me ~/Documents"`. Allowlist check passes; Claude executes. Same scenario over iMessage: Apple's servers reject any message not from a device authenticated with the Apple ID linked to that number — the forged number cannot pass. *(illustrative)*
- Length band: 2–3 min
- Still lanes: c2v (two-chain diagram), raster (pass/fail markers at each step)
- Prerequisites: access control lists, authentication vs identification, SMS architecture
- Exclusions: how Apple ID cryptographic binding works at the protocol level; SMS spoofing tooling and carriers; the RCS security model; whether `IMESSAGE_ALLOW_SMS` can be safely enabled under any configuration
- Score: 8/10

## Candidate 07 — Why the uplift fan-out escalates in waves instead of launching all agents at once

- Source: `plugins/code-modernization/README.md`
- Topic: Pilot-first dependency-ordered circuit-breaker fan-out in parallel migration
- Hook: The pilot module succeeded and a playbook exists — so why not migrate all 50 modules simultaneously?
- Key case: 50 modules need a .NET 8 uplift. Module 1 (pilot) runs to completion; `PLAYBOOK.md` is written. Batch 1: 3 dependency-free leaf modules run in parallel — all pass. Batch 2: 8 modules start. Module 12 fails — the shared build infrastructure it needs was not updated in the playbook. Circuit breaker trips: the 5 agents mid-run stop; batch 3 never starts. Result: 4 modules successfully uplifted, 45 untouched, 1 failed — a recoverable state. Without the circuit breaker and batching, all 50 agents would have hit the same gap and left a partially migrated codebase with inconsistent state across 50 directories.
- The Question: The pilot proved the approach works and every agent has the same playbook, so why does running them all simultaneously create a worse failure mode than running them in waves?
- Core idea: Three mechanisms interlock. *Dependency ordering*: a module cannot be uplifted before its dependencies, so the dependency DAG determines which modules are eligible in each batch — not calendar order. *Escalating batch size*: small early batches test the playbook's predictions against diverse real cases before committing more agents; the pilot is batch zero. *Circuit breaker*: if any batch's failure rate exceeds a threshold, the fan-out halts — unstarted modules remain in their original state, which is recoverable, while partially-migrated-but-broken is not. Together the three mechanisms convert a binary outcome (all succeed or chaos) into a staircase where damage is bounded and the playbook can be revised between waves.
- Visual object: A dependency DAG (nodes = modules, directed edges = dependencies) with nodes colored by batch wave (light → dark) and a red circuit-breaker marker between batch 2 and batch 3 labeled "failure rate exceeded — fan-out halted."
- Manim move: accumulate
- Example seed: 6 modules: A (leaf), B (leaf), C (depends on A), D (depends on B), E (depends on C and D), F (depends on A). Batch 1: A and B. Batch 2: C, D, F. Batch 3: E. If C fails in batch 2, circuit breaker stops D and F before they start; E never runs. Only A and B are uplifted; the rest are untouched and consistent. *(illustrative)*
- Length band: 3–5 min
- Still lanes: geo (dependency DAG with batch coloring), raster (circuit breaker marker, failure-rate threshold line)
- Prerequisites: dependency graphs, parallel execution, circuit breaker pattern
- Exclusions: the full `PLAYBOOK.md` schema; specific .NET 8 breaking-change catalog; how the `uplift-migrator` agent is sandboxed to its own directory; the `IMESSAGE_ALLOW_SMS` interplay with security posture
- Score: 7/10
