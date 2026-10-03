# Agents, Queues, Fandom, and Risk — inspiration for Film 12
(source: Bear's notes — inspiration)

## Why overnight queues for events still happen (and what agents do to them)
Physical overnight lines mostly disappeared for the biggest tours. The 2022 Eras Tour presale was an online queue that crashed Ticketmaster; "devotion" became screenshots of queue positions. Agents finish the job by making waiting free. A line only signals devotion because waiting costs something — a night on the sidewalk, hours refreshing. Once an agent waits for you at no cost, waiting signals nothing.

Consequence: agents quietly turn the queue into a market, but the money goes to the wrong party. Queues reward people with time (skews young — the fans artists want). Agent queues reward whoever has the best agent, or the most of them; a $100/month plan becomes a ticket-buying tool. Underpricing persists, but the gap between face value and willingness-to-pay goes to agent subscriptions and reseller fleets instead of fans. Worst outcome for artists: lower revenue AND lost goodwill.

Devotion signals move to things agents can't fake cheaply:
- Provable fan history (streaming, past attendance, fan-club tenure; Ticketmaster Verified Fan leans this way).
- Proof of personhood: identity-bound, non-transferable tickets — an agent can enter you but can't flip the ticket.
- In-person rituals as content: venue-only presales, merch drops, listening events where physical presence is the point.
- Sanctioned agent channels: Ticketmaster is already a Muse partner (purchase completes on Ticketmaster's side); platforms may block outside agents while running their own — the Amazon move plus a toll booth.
The overnight line becomes staged marketing; allocation moves to data and identity. But fan history can be gamed (streaming farms exist) — expect an arms race over what counts as proof of a real fan.

## The airline analogy (where loyalty drifts)
Airline loyalty started as rewarding frequent flyers; status ended up tracking spending. Credit-card spend earns miles, premium cabins earn status faster; loyalty programs became so lucrative United and Delta borrowed billions against them in the pandemic, valued above the airlines themselves. Fan-loyalty systems will likely drift the same way: "reward real fans" becomes "reward fans who spend."

Two kinds of history:
- Spending history (merch, tickets, VIP) favors wealth directly — the airline model.
- Engagement history (streaming, tenure, attendance) is fairer in principle (a broke teenager can stream all day) but easier to game with farms and bots.

The Muse angle: whoever holds your purchase history across merchants is positioned to be that loyalty layer — the "owning intent" position. That profile is worth more than any single transaction fee.

The worry: lines are unfair visibly — everyone sees who waited. Status systems are unfair invisibly: a fan-scoring algorithm quietly deciding presale access is harder to see and harder to challenge. Overnight lines at least had transparent rules.

## The engagement hierarchy (what's hard to fake)
A like is nearly free for an agent. A thoughtful reply costs a little more. Fan art used to be the strongest proof (hours of work) but generative AI made it cheap. What stays hard to fake takes TIME, not effort:
- A long, consistent history — can't be backdated; agents can grind but not rewrite the past.
- Recognition from other real fans — a social-graph signal, harder than solo activity.
- Physical presence — past concerts, in-person events; a body has to show up.

Two problems:
- Goodhart's law: once replies/fan art count toward ticket access, they become a grind to optimize; fandom turns into a status game; agents farm it; the signal dies.
- Whoever scores engagement must watch it: a fan score means monitoring social activity, and the companies best placed own the social graph — Instagram, Threads, plus an agent that knows your purchases. Engagement-based allocation is the most Meta-shaped version of all.

## Risk theory refinements (for agents)
Base formula probability × impact, mapped to approval tiers (act freely where blast radius is small; dig deep where large), plus three agent-specific refinements:
1. Irreversibility deserves its own weight. Expected value treats recoverable and unrecoverable $1,000 losses the same. Agents do irreversible things (send the email, make the purchase, delete the files). Small chance of an irreversible outcome deserves more caution — the "ruin" problem from finance.
2. Probability is adversarial, not random. Prompt injection steers the agent toward its highest-impact action deliberately. The question isn't just "how likely to go wrong" but "what's the worst this agent could be made to do" (hence scoping the GitHub token tightly).
3. Small risks add up. A thousand low-risk actions a week isn't low-risk overall; 0.1% error at agent volume is a weekly occurrence.

Working formula: probability × impact, adjusted for reversibility, with probability assumed adversarial and summed across volume.
