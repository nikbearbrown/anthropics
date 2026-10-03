# Session Summary: Muse, Agent Economics, and Designing for Blast Radius
October 3, 2026 (source: Bear's session notes — inspiration)

Three connected threads: (1) a practical setup for using Meta's Muse to draft Brutalist films without exposing anything that matters; (2) Muse's business model and what it means for fans, artists, and small businesses; (3) risk theory — adversarial probability, unknown unknowns, compartmentalization — aimed at teaching ordinary people how to live with agents.

## Product comparison (and correction)
Muse vs. Cowork vs. Codex share a basic architecture (model + sandboxed computer + browser + terminal + connectors); they differ mainly in default scope, permissions, and target market. Key difference: reversibility — Codex works inside git and code review; Muse makes purchases and submits forms that can't easily be undone. Correction: the three-way split was overstated — Muse's persistent Linux VM + macOS app control means it does Cowork-style work too. What still differs: where files end up and under what policy (Meta's cloud, training on by default, vs. Cowork's local sandbox).

## The Brutalist setup (film-as-code economics)
An entire film is generated from code: Spark plans from source material, writes the beat sheet + Kokoro TTS audio, produces Remotion and Manim code, renders to 4K in 20–30 min on a 64GB MacBook. A Muse draft is just a diff. Workflow: render previews low-res; 4K only after merge; keep rendering out of the agent loop (watcher script as launchd job); keep Muse's instructions as a file in the repo; split work by difficulty (Spark: narrow mechanical jobs; Opus/Fable/Astra: judgment-heavy work). Track per film: tokens used, cleanup time, publishability as-is. YouTube risk: inauthentic/mass-produced content gets demonetized — the editorial voice must stay Nik's. Rendering is never the bottleneck; tokens and cleanup time are.

## The architecture
Muse doesn't need to be on any local machine — its cloud VM clones repos and works from them. Muse via muse.ai in a dedicated browser profile; clones public sandbox repos in its VM; writes beat sheets and film code; opens PRs through the GitHub connector as a bot account. Reviewer: Claude Code's GitHub Action. Gates: CI + CODEOWNERS. Burner MacBook pulls merged main read-only and renders. Why the gate still matters in a disposable sandbox: the renderer executes repo code incl. npm install scripts; an LLM reviewer can be prompt-injected through PR text.

## Credentials
No tokens in any chat, ever. Muse authenticates through its GitHub connector (OAuth) as a dedicated bot account; scoping via the account's access. Fine-grained token template if ever needed: select repos only; Contents (read/write), Pull requests (read/write), Metadata (read); Workflows unchecked; ~30-day expiry.

## Muse's business model
Transaction fees (merchants pay, like affiliate commission); subscriptions secondary; no ads inside Muse (stated) but merchant browsing shapes ads elsewhere on Meta; training data on by default improves Spark models; strategic goal is owning the intent layer. Skeptics doubt transactions alone sustain it. Implication: film-generating users produce no transactions — pure cost to Meta, first target when the free tier tightens. Sanctioned developer path: Muse Spark API ($1.25/$4.25 per M tokens, or $0.10/$0.20 with data sharing).

## Muse for small business (Sept 29 launch)
Connects to Instagram analytics, Facebook Pages, Meta ad accounts; drafts posts/ad campaigns for review; nothing spends without approval. Feeds Meta's ad business from the advertiser side: lowers the barrier to advertising, keeps advertisers in-ecosystem, closes the loop. With QuickBooks data it can optimize for actual profit — real value — but structural conflicts: it knows cash position; it grades its own campaigns with Meta's generous attribution; it only recommends Meta inventory; lock-in deepens per chore. Safeguards: hard budget caps outside Muse; holdout/Conversion Lift tests; cross-check against QuickBooks/Shopify revenue; UTM links; keep one number Muse doesn't produce (weekly revenue).

## Agents, tickets, and fandom
Price-based allocation resists agents; queues don't. Waiting becomes free → waiting signals nothing; agents turn queues into markets, surplus to subscriptions/reseller fleets, not artists. Devotion signals move to what agents can't fake cheaply: provable fan history, proof of personhood, in-person rituals, sanctioned agent channels. Goodhart's law: once engagement counts toward ticket access, agents farm it. Meta's moat: a decade of social history + unique connectors (Instagram DMs, Facebook, Threads, Messenger).

## Risk theory for the agent era
- Risk = probability × impact, refined: irreversibility gets extra weight (ruin problem); probability is adversarial, not random (prompt injection steers toward highest-impact action); small risks compound across volume.
- Unknown unknowns: hard caps are mathematically different — they bound the outcome without enumerating actions (a $100 cap holds under any distribution). Caps must be enforced outside the agent; enumerate dimensions of harm (money, data, reputation, irreversible comms, legal), not actions.
- Compartmentalization: bulkheads; Saltzer and Schroeder (1975); need-to-know; Qubes OS; recoverability as a second axis (2×2: impact × recoverability); main failure mode is erosion — keep walls cheap or they won't last.
- Education: 2.5M+ downloads in ~2 weeks, mostly untrained users; education alone has a weak track record — push safe platform defaults too.

## Five rules for ordinary people
1. An agent's access is the attacker's access.
2. Ask how bad it gets, not how likely.
3. Caps belong outside the agent.
4. Irreversible actions get a human.
5. Protect the short list: email, money, credentials, public voice get walls; everything else gets backups.
Plus: prefer tools that ask "what should I access?" over "what should I avoid?" — when the safe configuration is harder than the unsafe one, that reveals the vendor's priorities.

## Open items / unverified
Cloud VM limits; Remotion/Manim in Muse's VM; GitHub connector OAuth scopes; Muse-token ↔ raw-token mapping; free-tier durability; whether ads appear inside Muse; OmniRoute's Muse executor stays disabled.
