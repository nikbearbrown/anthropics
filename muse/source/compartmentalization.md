# Compartmentalization: Theory and a Practical Framework
(source: Bear's research notes — inspiration)

## Core idea
Accept that you can't prevent every failure; limit how far any one failure spreads. Decide in advance what is allowed to fail, and make sure those failures can't reach what isn't. Key move: most people care deeply about only a handful of things — compartmentalize the irreplaceable few, back up or accept losses on the rest. Compartmentalizing everything equally is expensive and erodes.

## 1. Physical engineering: bulkheads
Ship's watertight bulkhead: a hull breach floods one compartment, not the vessel. Titanic: bulkheads didn't extend high enough — water spilled over (same failure as a sandbox with a shared credential leaking across it). Nygard's Release It! (2007) brought the "bulkhead pattern" to software; cloud "cell-based architectures" limit one failure to a slice of customers.

## 2. Security design principles
Saltzer and Schroeder (1975), The Protection of Information in Computer Systems: least privilege; separation of privilege (critical actions need more than one key — like Muse opening a PR and a separate reviewer merging); least common mechanism (minimize shared parts — shared parts are the channels failures travel through); fail-safe defaults (deny unless explicitly allowed); psychological acceptability (protection must be easy enough to actually use — explains erosion: painful compartments get torn down).

## 3. Military/intelligence: need-to-know
Compartmentalize by need to know, not just sensitivity. Models: Bell–LaPadula (1973, confidentiality); Biba (1977, integrity — "untrusted data shouldn't flow into trusted components," the formal version of "untrusted content shouldn't steer a privileged agent"); Brewer–Nash "Chinese Wall" (1989, conflicts of interest).

## 4. Personal computing: Qubes OS
Rutkowska's "security by compartmentalization": isolated VMs by trust domain (banking, work, untrusted browsing, disposable). A compromise in browsing can't touch banking. Nik's multi-machine Muse setup is Qubes done with hardware and accounts instead of VMs.

## 5. Finance: ring-fencing and limited liability
Limited liability caps loss at what's put in — a legal blast radius. Post-2008 UK ring-fencing separated retail deposits from investment banking. Position limits and diversification keep any single bet from ending the game.

## 6. Deciding what to compartmentalize: threat modeling
EFF's Surveillance Self-Defense (five questions — the fifth, "how much trouble am I willing to go through," makes cost explicit). Shostack's four questions (2014): What are we working on? What can go wrong? What are we going to do about it? Did we do a good job? Crown jewels analysis: find the few assets whose loss would be catastrophic.

## 7. The recoverability axis (the 2×2)
Impact and recoverability are separate dimensions:

| | Recoverable | Unrecoverable |
| High impact | Back it up well (photos, documents, code) | Isolate hard (identity, bank access, credentials, irreversible comms) |
| Low impact | Accept the risk | Minor isolation, or accept |

Backups move assets from right column to left (3-2-1 rule; RPO/RTO). The top-right cell is the short list worth real walls — for most people: identity (email = master key to password resets; phone; government ID), money (bank/brokerage/cards), credentials (password manager, SSH keys, API tokens), irreversible voice (accounts that speak for you publicly).

## Practical rule of thumb
List the top-right few. Put them behind hard, external walls: separate accounts, hardware keys, no agent access. Back up everything high-impact but recoverable, and test the restore. Let agents roam freely everywhere else. Keep the walls cheap (psychological acceptability) or they won't survive six months.

## Reading list (cited from memory — verify before filming)
Saltzer & Schroeder (1975); Bell & LaPadula (1973); Biba (1977); Brewer & Nash (1989); Nygard, Release It! (2007/2018); Shostack (2014); Rutkowska, Qubes OS docs; EFF, Surveillance Self-Defense.
