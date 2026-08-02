# Claude for Legal Video Ideas

## Candidate 01 — One bit of context flips every legal position to its mirror image
- Source: `commercial-legal/README.md`
- Topic: Playbook polarity reversal in contract review
- Hook: The "correct" legal position on liability caps, indemnity, IP ownership, and termination rights reverses completely when a single context flag switches from customer to vendor.
- Key case: A vendor MSA arrives. Customer-side: push the vendor to indemnify you, raise the liability cap, grant you broad IP license. Vendor-side on the identical clause structure: resist each of those positions.
- The Question: Liability direction should be determined by contract language; this case shows it is determined first by which side of the deal you occupy — why does flipping one flag change every downstream answer?
- Core idea: Playbook polarity: each substantive position is stored as a directed value anchored to a side flag. Review mode reads the flag before reading any clause; the same text triggers opposite redlines depending on which polarity is active.
- Visual object: A bilateral contract clause with two opposing annotation arrows — one pointing left (customer-favoring), one pointing right (vendor-favoring) — that swap when the side flag flips.
- Manim move: morph
- Example seed: Vendor MSA §12 caps vendor liability at 1× fees paid. Customer-side analysis: "too low — push to 2×." Vendor-side analysis: "too high — resist any increase." Same clause, opposite playbook action. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic contract review concepts
- Exclusions: the redline drafting mechanics, how the side flag is set during setup, the cold-start interview process
- Score: 9/10

## Candidate 02 — Your real playbook is in your deviations, not your policy document
- Source: `commercial-legal/README.md`
- Topic: Deviation accumulation as playbook signal
- Hook: Every time a lawyer accepts a clause that deviates from the stated playbook, a clause-specific counter increments; at five overrides in a rolling twelve-month window, the monitor proposes rewriting the playbook to match practice.
- Key case: Playbook says "never accept uncapped data-breach liability." Deviation log shows it was accepted in five different SaaS agreements within the year. Playbook monitor fires a proposed update.
- The Question: Playbook enforcement should decrease deviations over time; this team's deviation count kept climbing anyway — why does the gap between stated policy and actual practice accumulate instead of correcting?
- Core idea: Rolling-window threshold as policy-lag detector: the counter measures how far practice has drifted from written policy. When the threshold fires, it signals that the policy never reflected real risk appetite and proposes closing the gap in the document rather than in the next deal.
- Visual object: A rolling 12-month window with a clause-specific counter bar incrementing toward the threshold of 5, then triggering a proposal card.
- Manim move: accumulate
- Example seed: Clause: "Vendor may modify fees on 30 days' notice." Playbook: reject. Accepted: month 2 (small startup), month 5 (small deal value), month 7, month 9, month 11. Counter hits 5. Monitor proposes: "update playbook — accept this clause for contracts under $50K." [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic contract review, playbook concept
- Exclusions: how the deal-debrief agent runs mechanically, the specific YAML renewal register, NDA triage
- Score: 8/10

## Candidate 03 — Every AI legal citation is either verified or a guess — the tool shows which
- Source: `README.md`
- Topic: Citation trust states in AI-generated legal output
- Hook: Without a connected research tool, every case citation in an AI legal memo is drawn from training data — potentially years old, potentially overruled — and explicitly marked [verify]; connecting a live database transforms the same output's citation status inline.
- Key case: A commercial-legal review cites three cases supporting a limitation-of-liability position. Without CourtListener: all three are [verify]. With CourtListener connected: two are confirmed current, one was overruled the prior year and is flagged for replacement.
- The Question: Legal citation quality should be uniform across AI outputs; this case shows citation trustworthiness is binary and connector-dependent — why does the same model produce structurally different trust signals based on a tool connection?
- Core idea: Citation provenance tagging: the tool records the source of each citation (research API vs. training data) and exposes it inline. The [verify] tag is not a disclaimer — it is a claim about epistemic status that the reviewing attorney uses to allocate checking effort.
- Visual object: A legal memo with inline citation badges shifting from [verify] to source-tagged as a connector is plugged in.
- Manim move: transform
- Example seed: Memo cites "Eastman Chemical Co. v. Niro [verify]." After CourtListener connects: "Eastman Chemical Co. v. Niro [CourtListener, confirmed 2024]." Third cite resolves to "[overruled 2023 — see replacement]." [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: how CourtListener works internally, the full connector list, installation mechanics
- Score: 7/10

## Candidate 04 — An M&A closing checklist that writes its own new items from diligence documents
- Source: `corporate-legal/README.md`
- Topic: Self-updating closing checklist in M&A diligence
- Hook: The closing checklist starts from the purchase agreement's stated conditions precedent, then grows itself as diligence surfaces consents, novations, and assignments that were not anticipated at signing.
- Key case: Purchase agreement lists four closing conditions. Diligence reveals the target holds three federal contracts requiring government novation consent — not mentioned in the purchase agreement. Checklist auto-adds three new blocking items with counterparty and deadline populated.
- The Question: Closing checklists should be complete at signing; this deal kept adding blocking items as diligence ran — why do conditions accumulate after the agreement is executed?
- Core idea: Checklist initialization plus diligence feed: the checklist begins as a parse of the purchase agreement's conditions precedent; each diligence finding that surfaces a third-party consent or regulatory approval appends a new item, so the checklist reflects what is actually blocking close rather than what was predicted at signing.
- Visual object: A closing checklist growing downward as diligence document batches are processed and new blocking items appear with status columns.
- Manim move: accumulate
- Example seed: Start: 4 items (board approval, financing, HSR clearance, MAC). Diligence batch 1 finds government contract → adds "GSA novation consent." Batch 2 finds software license change-of-control clause → adds "vendor consent – Acme Corp." Final: 8 items, 4 unresolved, 2 critical-path. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic M&A deal structure, closing conditions concept
- Exclusions: the material contracts disclosure schedule, the integration management workplan, post-closing mechanics
- Score: 7/10

## Candidate 05 — Three legal disciplines that must hand off to each other when AI crosses a boundary
- Source: `ai-governance-legal/README.md`
- Topic: Explicit cross-plugin handoff protocol in AI governance
- Hook: A single AI use case can simultaneously breach the scope of product review, AI governance assessment, and a mandatory GDPR DPIA — and each boundary triggers an explicit handoff rather than an attempted answer.
- Key case: HR proposes AI-powered resume screening. Product counsel flags it as a launch requiring review. AI governance classifies it as high-risk under EU AI Act. Privacy detects personal data processing requiring a mandatory GDPR DPIA. All three run; none substitutes for another.
- The Question: A legal use case should have a single accountable owner; this case required three simultaneous assessments from separate disciplines — why can't one plugin absorb the others?
- Core idea: Scope discipline through explicit routing: each plugin is bounded to one legal discipline and names the responsible plugin for out-of-scope questions in its output rather than answering them. The handoff message is part of the deliverable, not an error state.
- Visual object: A triangle with three nodes (product, AI governance, privacy) and directed routing arrows that activate when a use case crosses a boundary line.
- Manim move: trace
- Example seed: Use case: "HR screening AI." Product: "launch review required → /ai-governance-legal:use-case-triage." AI governance: "high-risk EU AI Act deployer → /privacy-legal:pia-generation for DPIA." Privacy: "DPIA complete — no further handoff." [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic understanding of legal practice areas, awareness of GDPR
- Exclusions: EU AI Act risk tier specifics, the GDPR DPIA threshold test, internal mechanics of each plugin
- Score: 7/10

## Candidate 06 — 100 NDAs in, 15 need a lawyer — the triage that sorts automatically
- Source: `commercial-legal/README.md`
- Topic: NDA GREEN/YELLOW/RED risk triage
- Hook: Legal teams are bottlenecked by NDAs that do not actually require legal review — triage automatically sorts a stack so attorneys only read the ones that matter.
- Key case: 100 inbound NDAs. Triage: 72 GREEN (route to signature), 21 YELLOW (flag for quick scan), 7 RED (need full negotiation). Lawyer reads 28 instead of 100.
- The Question: NDA review time should scale linearly with NDA volume; this system decoupled lawyer time from volume — how does sorting a document by risk tier change the scaling relationship?
- Core idea: Triage as workload concentrator: the triage scores each NDA against the playbook and assigns a tier. GREEN means standard terms are acceptable as-is and no attorney reads it. Legal effort concentrates on genuinely contested terms, not document count.
- Visual object: A stack of 100 NDA envelopes splitting into three piles — large GREEN (auto-sign), medium YELLOW (quick read), small RED (negotiate).
- Manim move: split
- Example seed: Inbound NDA: mutual, 1-year term, standard exclusions, no residuals clause. Playbook: mutual NDAs under 2 years with no residuals → GREEN. Routes to DocuSign. No attorney reads it. [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific playbook positions driving classification, how redlines are generated for RED NDAs, the deviation log
- Score: 6/10

## Candidate 07 — The cold-start interview that turns your signed contracts into a playbook
- Source: `commercial-legal/README.md`
- Topic: Practice profile extraction from historical agreements
- Hook: A cold-start interview reads your recent signed agreements, extracts your actual negotiated positions from what you agreed to, and writes them into a practice profile that every future skill reads before touching a new contract.
- Key case: Attorney provides 20 signed vendor agreements. Interview extracts: "you always accepted 30-day payment terms, you never accepted vendor IP ownership of customer data, you cap your own liability at 2× fees paid." Profile written. Next review flags first deviation from those positions.
- The Question: A generic AI tool given the same contract gives generic advice; this tool gave attorney-specific advice after one interview — how does reading historical agreements change the output on the next contract?
- Core idea: Document-to-profile extraction: the cold-start treats signed agreements as evidence of accepted positions, not as templates. Each clause that appears consistently across signed contracts becomes a playbook position; future reviews compute deviation from the learned baseline.
- Visual object: A stack of 20 signed agreements feeding into a single CLAUDE.md practice profile file, which then feeds into a contract review flagging a deviation.
- Manim move: accumulate
- Example seed: 20 agreements. 18/20 cap liability at 1–2× fees paid. Profile writes: "standard cap: 1× fees; escalation required above 2×." Next vendor proposes uncapped → flagged as red deviation. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: plugin installation mechanics, YAML format of the profile, the deviation accumulation threshold mechanism
- Score: 6/10

## Candidate 08 — A contract's cancel-by deadline decays through urgency zones over time
- Source: `commercial-legal/README.md`
- Topic: Renewal deadline urgency decay
- Hook: A renewal deadline does not become urgent when it arrives — it enters an urgency zone weeks earlier, when there is still time to act; contracts that miss this window leave attorneys with a known deadline and no options.
- Key case: SaaS contract has a 60-day cancel-by notice window. Attorney learns about the renewal 45 days before the renewal date — the cancel window closed 15 days ago. The tracker would have surfaced it at day 89 before renewal.
- The Question: Renewal risk should be proportional to deadline proximity and known in advance; this attorney missed the cancel window on a tracked contract — why does a known deadline still produce a surprise?
- Core idea: Urgency-zone decay: the renewal tracker maintains a time-decaying priority score. Entry into the 90-day horizon triggers weekly digest appearance; inside 14 days it triggers red-flag escalation. The mechanism surfaces contracts while action is still available, not after the option has expired.
- Visual object: A timeline with contracts entering three urgency zones — horizon, watch, red-flag — as their cancel deadlines approach from right to left.
- Manim move: decay
- Example seed: Contract renews January 1. Cancel-by: November 1 (60-day notice). October 3: enters 90-day horizon → appears in weekly digest. October 18: enters 14-day red-flag → Slack escalation posted. Attorney acts October 20. [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: how the renewal register is populated, the deal-debrief agent, the playbook-monitor agent
- Score: 6/10

## Candidate 09 — The same worker engagement is legal in Texas and illegal in California simultaneously
- Source: `employment-legal/README.md`
- Topic: Worker classification as a jurisdiction-selected algorithm
- Hook: The same freelance arrangement clears the federal independent-contractor standard and fails California's ABC test — both conclusions are legally correct at the same time.
- Key case: Software developer: multiple clients, own equipment, sets own hours. Federal common law: IC. California ABC test fails prong B (work is within the usual course of the hiring company's business) → employee. The company has a contractor in Texas and an employee in California for the same role description.
- The Question: Worker classification should produce one correct answer from one fact set; this case produces two contradictory correct answers — why does geographic location change the legal conclusion without changing any fact?
- Core idea: Test selection precedes fact application: each state implements classification as a distinct algorithm run over the same inputs. The controlling algorithm is selected by the state where the worker performs services, not by the facts themselves. Running the engagement through every applicable state's test is the only way to know whether the company is compliant across its full footprint.
- Visual object: A single worker-engagement card feeding into three parallel state-test boxes, each returning a separate binary classification output.
- Manim move: split
- Example seed: Developer, 3-client portfolio, own laptop. Federal: IC ✓. California ABC: employee ✗ (fails prong B). Illinois economic-realities: inconclusive — more facts needed. One engagement, three different legal statuses. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic independent contractor vs. employee concept
- Exclusions: IRS classification rules, specific factor weights within each state test, retroactive reclassification exposure calculation, the leave-tracker agent
- Score: 8/10

## Candidate 10 — After three amendments, the liability cap in the contract you signed may not be the one that controls
- Source: `commercial-legal/README.md`
- Topic: Amendment layering and controlling-language version drift
- Hook: A base agreement says "liability capped at $100K" — signed, filed, on file — but two amendments later a different cap controls, and the base agreement still says $100K on every page.
- Key case: MSA base: liability capped at $100K. Amendment 1: raises cap to $500K for a named project. Amendment 2: adds an uncapped carve-out for data breaches. Current controlling cap: $500K for most claims, uncapped for data breaches — but the base agreement both parties signed says $100K throughout.
- The Question: The controlling liability cap should be readable from the signed contract; this case requires tracing three documents in chronological order to find it — why does signing a contract not make its terms legible?
- Core idea: Amendment layering: each amendment partially overwrites prior text. The controlling language for any provision is the most recent amendment to touch it. The tracer processes documents in chronological order, tracks which version of each clause last superseded the prior, and surfaces the chain — so the attorney reads the currently-controlling term without holding three documents simultaneously.
- Visual object: A contract §12 clause with three sequential amendment layers annotated on a timeline, each layer overwriting part of the prior text, with the current-controlling layer highlighted.
- Manim move: trace
- Example seed: §12 liability. Base: $100K. Amend 1: $500K (project scope). Amend 2: uncapped data-breach carve-out. Amend 3: $500K extended to all scopes. Current §12: $500K base, uncapped for data breach. Base still says $100K on every page. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic contract amendment concept
- Exclusions: integration clauses and their legal effect, how courts resolve conflicts between amendments, the full amendment-history command output format
- Score: 7/10

## Candidate 11 — A blank cell in a diligence table is more informative than a paragraph of narrative
- Source: `corporate-legal/README.md`
- Topic: Schema imposition as a gap-detection mechanism in M&A diligence
- Hook: A narrative diligence summary can say "all contracts reviewed, no major issues" while hiding that 12 of 50 contracts were never checked for change-of-control clauses — a typed table cell cannot hide that.
- Key case: 50 material contracts reviewed in a data room. Narrative summary: "contracts reviewed; standard terms." Tabular extraction with a "change-of-control clause (Y/N/term)" column: 38 cells answered with citations, 12 blank. The blank cells surface 12 contracts where either the clause was absent or the reviewer did not check — either is a blocking item before close.
- The Question: Diligence completeness should be apparent from the review output; this case shows narrative summaries can obscure gaps that typed columns expose — why does output format change what the reviewing attorney can see?
- Core idea: Schema imposition: a typed column schema forces every document to answer the same question set. A document without an answer produces a blank cell — not an omitted sentence. Blank cells are machine-readable; missing paragraphs are not. Every answered cell is cited to source. The table's structure makes incompleteness visible at a glance before close, whereas a narrative summary flattens both present and absent findings into prose.
- Visual object: A diligence table with document rows and typed data-point columns — some cells filled with cited answers, others conspicuously blank.
- Manim move: scan
- Example seed: Column: "Change-of-control clause (Y/N/term)." 50 contracts. 38 cells answered (cited). 12 blank. Pre-close flag: 12 contracts require review. 3 of the 12 lack the clause entirely — counterparty consent required for any asset transfer. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic M&A diligence concept
- Exclusions: how the tabular-review skill generates the Excel output, materiality thresholds in issue extraction, the closing checklist derivation, the disclosure schedule build
- Score: 7/10

## Candidate 12 — Explaining why you're asking a question is part of the legal intake template, not a courtesy
- Source: `legal-clinic/skills/client-intake/references/intake-templates/README.md`
- Topic: Purpose-explanation as a structural component of legal intake sequences
- Hook: In immigration intake, asking "do you have a criminal history?" without first explaining why produces a different answer than asking with an explanation — so the template encodes the explanation as mandatory preceding text, not optional preamble.
- Key case: Immigration clinic intake. Bare sequence: "Do you have any criminal history?" → client says no. Explanation-first sequence: "I need to ask about criminal history because it directly affects which applications you're eligible for — anything you tell me is privileged — do you have any criminal history?" → client discloses a prior arrest. The second sequence produces a material fact the first missed.
- The Question: Intake accuracy should depend on what questions are asked; this case shows it depends on what the client is told before the question arrives — why does pre-question explanation change the answer?
- Core idea: Sensitive-question sequencing: undisclosed purpose is perceived as threat, and perceived threat suppresses disclosure. Encoding the explanation as a structural preceding element — mandatory, not optional — removes the threat signal before the question arrives. The template treats the explanation as a data-collection mechanism with measurable yield, not as a politeness convention, and orders it before the sensitive question in every intake sequence.
- Visual object: Two intake sequences displayed side by side — bare question on the left, mandatory purpose-explanation followed by question on the right — showing different disclosure outcomes below each.
- Manim move: compare
- Example seed: 10 immigration clinic clients. Bare sequence: 3 disclose criminal history. Explanation-first: 8 disclose. 5 additional disclosures produce facts that change eligibility analysis and prevent filing an application that would have been denied. [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific eligibility consequences of criminal history in immigration law, how intake facts feed into case analysis, the full intake template format for other practice areas
- Score: 7/10

## Candidate 13 — "Can we fire this employee?" has a different answer in every state you operate in
- Source: `employment-legal/README.md`
- Topic: Jurisdictional employment footprint as a state-indexed rule matrix
- Hook: The same termination question — "can we let this person go for performance?" — produces a different legal answer depending on which state the employee is in, and the practice profile holds all the answers before you ask.
- Key case: GC asks: "Can we terminate this employee without a PIP?" California row: risky — FEHA exposure, document progressive discipline first. Texas row: yes, at-will, no PIP required. New York row: recommended — NYCHRL adds exposure. Same question, three different answers, one practice profile.
- The Question: Employment Q&A should produce one answer for one question; this system produces a different answer per state for the same question — how does the practice profile know which state's rule applies before the attorney specifies it?
- Core idea: Jurisdictional matrix routing: the cold-start interview builds a table indexed by state × employment-question-category. When a Q&A call arrives, the system reads the employee's state from context and routes through the correct row before applying any rule. Without the matrix, the tool would apply a default — likely federal or majority-state — that may not control in the jurisdiction where the employee actually works.
- Visual object: A grid of state rows × employment-question columns, with one cell lighting up as a Q&A call routes through its state row to the controlling answer.
- Manim move: scan
- Example seed: Q: "PIP required before termination?" CA: "Yes — progressive discipline." TX: "No — at-will." NY: "Recommended — NYCHRL." WA: "Depends — check protected-class overlap." Same question, four answers, one grid. [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: basic at-will employment concept
- Exclusions: specific state-law threshold tests, FMLA/CFRA intersection, the leave-tracker agent, RIF mechanics, the worker-classification screener
- Score: 6/10

## Candidate 14 — Building and deploying the same AI system creates two separate compliance obligation sets
- Source: `ai-governance-legal/README.md`
- Topic: EU AI Act role-based obligation doubling for in-house-built AI tools
- Hook: A company that builds an AI tool and deploys it internally occupies two EU AI Act roles simultaneously — provider and deployer — and each role carries its own independent obligation set, so the compliance burden nearly doubles compared to licensing equivalent capability from a vendor.
- Key case: Internal performance-review AI, built in-house, deployed to HR. Provider obligations (built it): technical documentation, conformity assessment, CE marking. Deployer obligations (uses it): human oversight measures, fundamental rights impact assessment, staff training, register entry. Licensing equivalent capability from an external vendor: deployer obligations only.
- The Question: AI compliance obligations should follow system risk level; this case shows they also follow the company's role relative to the system — why does building-and-deploying produce substantially more obligations than deploying a vendor tool at equivalent risk?
- Core idea: Role inventory precedes obligation assignment: the EU AI Act applies different duty sets to providers and deployers. A company that built and deploys internally occupies both roles for the same system. The `ai-inventory` skill classifies each system by active role first, then generates the combined obligation checklist — preventing the common error of treating in-house deployment as deployer-only scope.
- Visual object: A single AI system node at center, one company entity connected by two labeled arrows — "provider" and "deployer" — each expanding into a separate obligation checklist column.
- Manim move: split
- Example seed: Internal HR-screening AI, built in-house. Provider checklist: 12 items. Deployer checklist: 8 items. Total: 20. Equivalent vendor tool: 8 deployer items only. Building it added 12 obligations. [illustrative]
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: basic EU AI Act awareness
- Exclusions: specific high-risk category triggers, conformity assessment mechanics, the AIA generation process, the plugin triangle cross-handoff
- Score: 6/10
