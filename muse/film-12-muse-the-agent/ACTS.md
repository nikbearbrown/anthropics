# ACTS.md — Muse the Agent: What It Does, Who Pays, and How to Survive It (Film 12 of 12)

**Exact title:** Muse the Agent: What It Does, Who Pays, and How to Survive It

**Core promise:** By the end, the viewer understands what Meta's consumer
agent actually is (goal → plan → acts), how Meta makes money from it
(transaction fees now, the intent layer forever), where the sharp edges are
(Full Disk Access, deny-lists, adversarial failure), and the five rules that
keep an agent from ruining their week.

**Structure:** hook + key terms + three acts (12 body beats) + recap + your
turn + outro. 17 beats, ~386 s (~6m26s). This is the series capstone: longer
than the middle films because the whole-source requirement covers four
source documents.

- **Hook (BIDEA):** the other Muse — not the models you rent, not the harness
  you drive, the agent that runs errands.
- **Key terms (BDEFS):** Agent · Intent layer · Blast radius · Allow-list.
- **Act 1 — What it does (4 beats):** B01 goal in, plan out, actions taken —
  its own cloud computer, approval before consequential actions; B02 consumer
  errands and connectors (commerce first, productivity second); B03 the three
  pricing tiers (same features, pay for volume, card required even free);
  B04 endurance, not intelligence — "it saves time, not thought".
- **Act 2 — Who pays (4 beats):** B05 transaction fees: merchants pay Meta a
  cut, like an affiliate commission, costs drift into prices; B06 the intent
  layer: the moment you say what you want before money moves — no ads inside
  Muse (Meta's word), but merchant browsing shapes ads elsewhere; B07 agents
  turn queues into markets: waiting becomes free → waiting signals nothing →
  surplus goes to subscriptions and reseller fleets, not artists; B08 loyalty
  drift: from frequent flyers to spending; devotion signals move to fan
  history, proof of personhood, in-person rituals, sanctioned agent channels;
  visible unfairness becomes invisible unfairness.
- **Act 3 — How to survive it (4 beats):** B09 Full Disk Access (the whole
  disk, not a folder — a behavioral promise) and deny-lists vs allow-lists
  (Saltzer & Schroeder, 1975: deny unless explicitly allowed); B10 prompt
  injection: failure probability is adversarial, not random; approval fatigue;
  the mascot as trust shortcut; B11 compartmentalization: the 2×2 of impact ×
  recoverability; the short list (email, money, credentials, public voice)
  gets real walls; B12 the five rules for the agent era.
- **BVDT:** exactly 3 lines, one per act.
- **BHTF:** audit one agent you use — what can it touch, what can it spend,
  what can it never do — and put a cap outside the agent.
- **BOUT:** SERIES FINALE: "Muse, in for Bear. Thanks for watching the
  series." No next-film teaser; the series closes.

**Tone:** clear-eyed, honest, unsentimental. This film is analysis and
commentary, not a tutorial — it teaches a way of thinking (risk, blast
radius, compartmentalization), not a button to click. Judgments are voiced
as the film's analysis; records are voiced as records.

**What this film is not:** not about the Muse Spark API or Muse Code (Films
1–11); not a review of the app's UI; not financial advice; not a claim that
any specific attack has happened to the viewer. Speculative material from
Bear's notes is voiced as analysis, never as established fact.

**Cast per act (one look):** Act 1 uses cards and a loop diagram (terracotta
nodes, blue connectors, green checks); Act 2 uses flow diagrams and a
queue→market transformation; Act 3 uses a deny-list vs allow-list contrast
pair, an adversarial steering diagram, the 2×2 matrix (top-right cell in
terracotta), and five numbered rule cards.

**Source facts (the record):**
- Muse is Meta's consumer AI agent, launched in the US on September 8, 2026,
  marketed as the first personal AI agent "built for everyone"; tagline "AI
  That Hustles for You"; "personal superintelligence" framing.
  (muse-agent-brief.md §1)
- Every user gets a persistent Linux VM in Meta's cloud with its own browser,
  filesystem, and terminal; Muse keeps working after the app closes.
  (muse-agent-brief.md §2)
- It takes a goal, builds a plan, carries out the steps, checks in for
  approval before consequential actions. (muse-agent-brief.md §1–2)
- Consumer errands: travel, restaurant, and appointment booking; shopping and
  checkout through merchant partners; forms and registrations; subscriptions;
  event tickets (Ticketmaster is a launch partner, purchase completes on
  Ticketmaster's side). (muse-agent-brief.md §2)
- Connectors: Shopify, OpenTable, Ticketmaster, Duffel, Instacart, Expedia,
  Link by Stripe; Gmail, Google Docs, Notion, Figma, Asana, Canva, Slack,
  Zoom, GitHub, QuickBooks, Klaviyo; Instagram/Facebook/Threads/Messenger.
  Amazon blocked Muse. (muse-agent-brief.md §2)
- Pricing tiers: Free (100M Muse tokens/week), Power ($20/mo, 500M/week),
  Maximum ($100/mo, 3B/week); same features, pay for volume; card required
  even for the free tier. (muse-agent-brief.md §3)
- Stated business model: transaction fees paid by merchants, like an
  affiliate commission; secondary: subscriptions, API sales; Meta says no ads
  inside Muse. (muse-agent-brief.md §4)
- "Its real strength is endurance, not intelligence… It saves time, not
  thought." (muse-agent-brief.md §2, session-summary-blast-radius.md)
- In the instructor's experience, the Spark models are noticeably less
  capable than GPT-6 Astra, Claude Fable, or Claude Opus. (muse-agent-brief.md §1)
- Security concerns from the brief: Full Disk Access instead of folder-level
  access; deny-list instead of allow-list (Saltzer & Schroeder, 1975);
  Malwarebytes zero-day; prompt injection; approval fatigue; trust by design.
  (muse-agent-brief.md §5)
- The five rules for ordinary people: an agent's access is the attacker's
  access; ask how bad it gets, not how likely; caps belong outside the agent;
  irreversible actions get a human; protect the short list (email, money,
  credentials, public voice). (session-summary-blast-radius.md)
- Compartmentalization: bulkheads; Saltzer & Schroeder (1975) least
  privilege / fail-safe defaults; the recoverability 2×2; the short list for
  the top-right cell. (compartmentalization.md)
- Queues: waiting becomes free → waiting signals nothing → queues become
  markets, surplus to subscriptions/reseller fleets; price-based allocation
  resists agents, queues don't. (agent-queues-fandom-risk.md)
- Airline loyalty drifted from frequent flyers to spending; status systems
  are unfair invisibly. (agent-queues-fandom-risk.md)
- Risk refined for agents: irreversibility gets its own weight; probability
  is adversarial, not random; small risks compound across volume.
  (agent-queues-fandom-risk.md, session-summary-blast-radius.md)

**LEFT OUT (with reasons):**
- The Muse Spark API and Muse Code harness — Films 1–11; this film is about
  the consumer agent, and the distinction is load-bearing.
- The Malwarebytes zero-day and the 6.8 GB data-exposure report — real
  incidents from the brief, but the film's subject is the structural shape of
  the risk (deny-lists, adversarial probability), not incident history.
- The "11 of 47 payments" skepticism figure — a single analysis, not enough
  to voice as a number.
- Goodhart's law on engagement farming — true to the notes, but the loyalty
  beat already carries the argument; one more mechanism would overstuff it.
- Small-business features (Meta Business Manager, ad drafting) — a real
  product surface, but the business-model argument is clearer through
  transaction fees and the intent layer.
- The Mac-app removal / bot-account / burner-MacBook setup — the brief's
  specific operational answer; the film teaches the principles (caps outside
  the agent, the short list) instead of one person's rig.
