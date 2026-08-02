# AI for Commercial Real Estate — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Comp Audit: Catch Non-Market Comparables Before They Corrupt a Valuation with Claude

- Source: ai-for-commercial-real-estate/chapters/05-property-valuation-what-ai-can-model-and-what-the-market-actually-is.md
- Lane: BUILD (Claude Code)
- Hook: An AI valuation tool selected four comps. Three of them were wrong for reasons no model can see — an off-market relationship sale, a distressed disposition, a loan-maturity transaction. The number looked right. The analysis was not.
- The artifact: A screen recording of Claude auditing a set of 6 comps against a 5-question checklist: (1) arm's-length transaction? (2) non-market seller motivation? (3) tenant credit story comparable to subject? (4) location/pedestrian-pattern applicable? (5) transaction date within relevant market cycle? Each comp gets a pass/flag for each criterion and a final "use / exclude / adjust" recommendation. A D3 animated table renders the comp audit matrix with color-coded flags.
- Prompt seed: `claude "Audit these 6 commercial real estate comparables for a Beverly Hills retail property valuation. For each comp, answer 5 questions: (1) Was this an arm's-length transaction, or were there relationship or distress factors? (2) Was there seller motivation that would create non-market pricing (loan maturity, partnership dissolution, 1031 deadline)? (3) Does the tenant credit story match the subject property? (4) Is the location/foot traffic pattern comparable to the subject? (5) Is the transaction date within the relevant market cycle for this asset class? For each answer, rate Reliable / Uncertain / Exclude and give a one-sentence rationale. Then recommend: which comps to keep, which to exclude, and which require adjustment. [paste comp details]"`
- Read / check: Verify each of the 5 questions is addressed for each comp — no skipped criteria. Confirm "Uncertain" flagging is used when data is insufficient rather than defaulting to Reliable. Check that the exclude recommendation cites the specific criterion that failed.
- Human supplies: 6 comp records with basic details (address, sale price, date, tenant, transaction notes). Real comps from an active deal preferred; synthetic illustrative comps acceptable for the video.
- Output medium: screen-recording mp4 (Claude terminal) + D3 animated comp audit matrix (color-coded by flag status)
- The change: Ask Claude: "After removing the excluded comps, what does the revised comp set imply about the subject property's cap rate — and how does that differ from the AI valuation tool's original estimate?" Show the cap rate comparison.
- Teardown angle: The model does not know why a transaction happened. The broker does. The comp audit is the step that converts model output into professional opinion. Without it, the output is a pattern match, not a valuation.
- Exclusions: Cut hedonic price model theory; cut Rosen 1974 academic background; cut appraisal licensing and USPAP detail.
- Score: 9/10

---

## Candidate 02 — Build the Lease Abstraction Audit: Run the Seven-Item Checklist Against an AI Extract with Claude

- Source: ai-for-commercial-real-estate/chapters/07-lease-abstraction-the-95-that-hides-the-5.md
- Lane: BUILD (Claude Code)
- Hook: 95% accuracy sounds safe. But the 5% concentrates in exactly the clause types where money hides — CPI floors, co-tenancy triggers, CAM exclusions. One missed clause can change the deal.
- The artifact: A screen recording of Claude processing a commercial lease abstract against the seven-item checklist (rent escalation, renewal options, ROFO/ROFR, co-tenancy, CAM exclusions, exhibit-defined terms, amendment priority). For each checklist item: does the abstract report presence or absence? Is the reported information complete (mechanics, not just existence)? Is there an amendment that modifies the base lease provision? Output: a checklist report with source-citation verification flags. A Manim scene animates the seven-item checklist, with checkmarks appearing as each item is verified and warning icons appearing where verification fails.
- Prompt seed: `claude "Run the seven-item lease abstraction checklist against this AI-generated abstract for a retail lease: [paste abstract]. For each of the seven items — rent escalation, renewal options, ROFO/ROFR, co-tenancy, CAM exclusions, exhibit-defined terms, amendment priority — answer: (1) Does the abstract report this item? (2) Are the mechanics complete (not just existence but terms, conditions, notice windows, etc.)? (3) Is there any indication of an amendment that might modify the base lease provision? Mark each: Verified / Needs Source Check / Not Reported. For any 'Needs Source Check,' specify exactly what the source document should confirm."`
- Read / check: Verify all 7 checklist items are addressed — no skips. Confirm "Needs Source Check" flags are specific about what to verify, not generic. Check that the distinction between clause existence and clause mechanics is maintained — a renewal option that exists but whose notice window is missing should be flagged.
- Human supplies: An AI-generated lease abstract (from any lease abstraction tool output, or a manually summarized lease). The underlying lease document for source-citation verification in the change round. Synthetic illustrative abstract acceptable for the video; a real abstract from a real deal is more impactful.
- Output medium: screen-recording mp4 (Claude terminal) + Manim seven-item checklist animation (checkmarks and warning icons appearing sequentially)
- The change: Take one "Needs Source Check" item and open the actual lease document (or a synthetic version). Show Claude reading the amendment that changes the base lease provision — the CAM exhibit that adds a controllable expense cap. Show how the abstract was "95% accurate" and the amendment was the 5%.
- Teardown angle: High accuracy is not the same as low risk because the errors are not random. The seven-item checklist is not comprehensive lease review — it is targeted verification of the clause types where AI abstraction is most likely to produce a confident wrong answer.
- Exclusions: Cut vendor accuracy statistics comparison (Lextract, CAMAudit by name); cut hallucination theory; cut temporal priority legal analysis beyond practical implications.
- Score: 9/10

---

## Candidate 03 — Build the Market Forecast Variance: Write the Broker's Correction on Top of the Model's Baseline with Claude

- Source: ai-for-commercial-real-estate/chapters/10-market-analysis-when-the-model-is-behind-the-market.md
- Lane: BUILD (Claude Code)
- Hook: An AI market report says demand is stabilizing. Your tour data says it isn't — for tech tenants in Culver City. Both observations are correct. The model is behind the market. The broker's job is to write the variance.
- The artifact: A screen recording of Claude building a structured "baseline + variance" market memo. Input: (1) an AI-generated market forecast summary (paste or describe); (2) the broker's local data points (tour activity, tenant rep conversations, concession movement). Output: a 300-word market memo with explicit structure — model baseline (what the forecast says), local variance (where broker data diverges and why), synthesis (what the combination implies for the client's specific decision). A Manim scene animates the "baseline + variance = memo" workflow as a flow diagram.
- Prompt seed: `claude "Write a market analysis memo for a Westside Los Angeles office tenant client using this structure: (1) Model baseline: summarize this AI market forecast — [paste forecast summary]. (2) Local variance: I have the following broker-sourced observations — [paste: 3 tenant rep conversations, tour activity data, concession package movement]. For each observation, classify it as: consistent with the model, diverges from the model, or model silent on this. (3) Synthesis: write a 150-word interpretation that combines the baseline and variance into a specific recommendation for a tenant considering a 5-year lease commitment. Note where local knowledge reinforces the model and where it corrects it."`
- Read / check: Verify each local observation is classified (consistent/diverges/model silent) — not all lumped together. Confirm the synthesis is specific to the client's decision (5-year lease), not generic market commentary. Check that the memo distinguishes what is known from what is inferred.
- Human supplies: One AI-generated market forecast summary (from CoStar, CBRE, JLL, or similar — any recent market report excerpt). 3–5 real or realistic broker-sourced observations (tour activity, tenant rep calls, concession data). Real data preferred; synthetic illustrative observations acceptable.
- Output medium: screen-recording mp4 (Claude terminal) + Manim flow diagram animation (baseline + variance → memo structure)
- The change: Ask Claude: "What would a broker whose recent experience is entirely in entertainment tenants miss about the tech submarket in this analysis? Name three blind spots and how to correct for them."
- Teardown angle: Local knowledge is evidence when it is specific, repeated, and checked against transactions. The broker's correction is not a rejection of the model — it is the variance that makes the baseline usable.
- Exclusions: Cut office-demand paradox AI firm analysis detail; cut specific CoStar/VTS platform comparison; cut full submarket history.
- Score: 8/10

---

## Candidate 04 — Build the Lease Draft Reviewer: Flag the Five Structural Decisions Before You Negotiate with Claude

- Source: ai-for-commercial-real-estate/chapters/06-lease-drafting-the-first-draft-is-not-the-final-draft.md
- Lane: BUILD (Claude Code)
- Hook: A lease that looks finished is not the same as a lease that reflects the deal. The five structural decisions that determine a lease's economics are often buried in plain language. Find them before you negotiate.
- The artifact: A screen recording of Claude reviewing a standard commercial lease first draft against five structural decision categories: (1) rent structure (base rent, escalation mechanics, percentage rent); (2) expense responsibility (NNN, gross, modified gross, CAM specifics); (3) term and options (lease term, renewal rights, expansion rights, ROFO/ROFR); (4) use and exclusivity (permitted use, exclusivity protections, co-tenancy rights); (5) exit provisions (termination rights, assignment/subletting, holdover). For each category: what does the draft say, what is missing, and what should be negotiated. Output as a structured review document.
- Prompt seed: `claude "Review this commercial lease first draft against five structural decision categories. For each category, answer: (1) What does the current draft say? (2) What is absent or undefined that should be specified? (3) What is the negotiating leverage point for the tenant/landlord? Category 1: Rent structure (base rent, escalation, percentage rent). Category 2: Expense responsibility (what is NNN vs. included). Category 3: Term and options (length, renewals, expansion, ROFO). Category 4: Use and exclusivity (permitted use, exclusivity, co-tenancy). Category 5: Exit provisions (termination, assignment, holdover rate). [paste lease first draft]"`
- Read / check: Verify all 5 categories are addressed — no skips. Confirm "absent or undefined" flags are specific (e.g., "CAM cap not defined" not "expenses unclear"). Check that negotiating leverage points are specific to the deal structure, not generic advice.
- Human supplies: A commercial lease first draft (real or realistic template — any standard retail or office lease). Synthetic illustrative draft acceptable for the video; a real draft from an active deal is more impactful.
- Output medium: screen-recording mp4 (Claude terminal)
- The change: Ask Claude: "The attorney will review this draft next. What can the broker flag now — before it goes to legal — that would save negotiating time and legal cost? Name three items that don't require a lawyer to identify."
- Teardown angle: The first draft is not the deal. It is a starting position. The broker's job is to find the structural decisions that will determine the economics before the negotiation begins — not after the attorney has spent three hours on a provision that was always going to change.
- Exclusions: Cut lease drafting legal mechanics (warranty of title, SNDAs, estoppels); cut construction allowance TI negotiation; cut ground lease specifics.
- Score: 8/10

---

## Candidate 05 — Research the Liability Question: When AI Is Wrong and Your Name Is on It with Claude

- Source: ai-for-commercial-real-estate/chapters/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it.md
- Lane: RESEARCH (Claude assistant)
- Hook: The broker signs the valuation memo. The AI generated the number. When the deal closes at a different price, who is responsible? The answer is not the AI.
- The artifact: Claude synthesizes a research brief on broker liability in AI-assisted CRE transactions: (1) the current regulatory standard for broker professional responsibility in AI-assisted work (California DRE guidance cited explicitly); (2) three published cases or enforcement actions involving broker reliance on automated valuation tools; (3) the specific language that creates liability — "AI-generated valuation" vs. "broker opinion based on AI-assisted analysis"; (4) the disclosure and documentation practices that reduce (but don't eliminate) liability. Output: a sourced 400-word brief with a "minimum documentation checklist."
- Prompt seed: `claude "Research broker professional liability in AI-assisted commercial real estate transactions. Synthesize a brief covering: (1) what current regulatory standards say about broker responsibility when AI tools are used in valuations or lease reviews — cite California DRE 2026 advisory and any RICS or NAR guidance; (2) three documented cases or enforcement actions involving brokers who relied on automated tools and faced liability; (3) the specific language in client memos that creates vs. limits liability — quote where possible; (4) a minimum documentation checklist: what a broker must preserve to show professional judgment was exercised. Flag any claim you cannot verify. End with: what 'the model said so' cannot substitute for."`
- Read / check: Verify the California DRE 2026 advisory exists and the cited guidance is accurate. Confirm case references are real — spot-check one. Check that language examples are specific, not generic. Flag unverified cases for human follow-up.
- Human supplies: Nothing — Claude researches from public sources. Human must verify all flagged claims and case citations before relying on the brief professionally.
- Output medium: screen-recording mp4 (Claude building the brief) + slate (minimum documentation checklist as a formatted table)
- The change: Ask Claude: "If a broker can demonstrate they ran the seven-item lease abstraction checklist (from Ch. 7) and the comp audit (from Ch. 5), does that constitute evidence of professional judgment? Draft the memo language that documents that process."
- Teardown angle: Professional responsibility doesn't transfer to the tool. The broker who signs the memo owns the opinion. The model is a tool. Documenting the judgment the broker exercised is what protects the broker — not disclaiming the tool.
- Exclusions: Cut E&O insurance mechanics; cut attorney-client privilege; cut disclosure rules for buyer vs. seller representation.
- Score: 8/10

---

## Candidate 06 — Build the AI Workflow Decision Map: Which CRE Tasks to Delegate, Explore, or Protect with Claude

- Source: ai-for-commercial-real-estate/chapters/11-building-your-ai-workflow.md
- Lane: BUILD (Claude Code)
- Hook: The broker who decides once writes it down. The broker who decides every time pays the cost every time. Build the decision map that runs once and saves hours.
- The artifact: A D3 v7 interactive three-column decision map for CRE tasks: Delegate (AI handles after you set the frame), Explore-then-decide (AI generates options, broker decides), Protect (broker judgment only). 15 CRE-specific tasks placed in their correct column. Each task expandable with a one-sentence rationale. Screen recorded with the viewer following the logic for two tasks — one that clearly delegates, one that lands in "protect."
- Prompt seed: `claude "Build a self-contained D3 v7 HTML file rendering a three-column CRE task delegation map. Columns: 'Delegate' (green), 'Explore-then-Decide' (yellow), 'Protect' (red). Place these 15 tasks in their correct column: offering memorandum summary, lease abstraction first pass, comp selection, cap rate determination, client recommendation, market trend summary, co-tenancy clause verification, lease negotiation strategy, due diligence checklist generation, property condition assessment, investment memo draft, ROFO/ROFR identification, final valuation opinion, competing offer analysis, disclosure compliance. Each task is a clickable card that opens a one-sentence rationale. Inline CSS, D3 7.9.0 from cdnjs."`
- Read / check: Verify each task is in the correct column per the book's framework (e.g., cap rate determination = Protect; offering memo summary = Delegate; comp selection = Explore-then-decide). Check that rationale sentences are specific, not generic. Confirm all 15 tasks appear and the D3 file renders in a browser.
- Human supplies: Nothing — fully synthetic. Real-data upgrade: broker adds their own firm's task list and re-sorts.
- Output medium: screen-recording mp4 (browser interaction with D3 map — clicking through tasks, showing expand/collapse)
- The change: Add a "log your own task" input — broker types a task, answers two questions (Is it bounded? Does failure require professional judgment?), and the task is placed in the correct column. Show one live entry.
- Teardown angle: The decision is not made under pressure in a client meeting. It is made once, written down, and consulted. The broker who has built this map moves faster and makes fewer mistakes — not because AI improved, but because the workflow did.
- Exclusions: Cut AI tool market overview; cut platform pricing comparison; cut technology adoption curve.
- Score: 8/10

---

## Candidate 07 — Research the Protected Practice: What Will the Best Brokers Look Like in Five Years with Claude

- Source: ai-for-commercial-real-estate/chapters/13-the-protected-practice-what-the-best-brokers-will-look-like-in-five-years.md
- Lane: RESEARCH (Claude assistant)
- Hook: The brokers who last won't be the heaviest AI users. They'll be the ones who can say exactly what they use it for — and why the other half is irreplaceable. What does that practice actually look like?
- The artifact: Claude synthesizes a research brief on AI's structural effect on commercial real estate brokerage: (1) which CRE tasks the research shows AI performing at or above human baseline (document review, comp screening, market trend analysis); (2) which tasks have no evidence of AI parity (negotiation, relationship management, local market judgment, client trust); (3) three documented case studies of brokers who have successfully repositioned from execution to judgment work; (4) the skills the brief predicts will command premium in 5 years. Output: a sourced brief with a "protected practice" skills matrix.
- Prompt seed: `claude "Research the structural effect of AI on commercial real estate brokerage practice. Synthesize a brief covering: (1) which CRE tasks have published evidence of AI performing at or above human baseline — cite specific studies or platform benchmarks; (2) which tasks have no published evidence of AI parity and why — focus on tasks requiring local knowledge, negotiation, fiduciary judgment; (3) three documented examples of brokers or firms that have repositioned from execution to judgment roles as AI handles more execution; (4) which skills the evidence predicts will command premium in 5 years. End with a one-page 'protected practice skills matrix': skill, why it resists AI substitution, what practice builds it. Flag any claim you cannot verify."`
- Read / check: Verify cited AI-parity claims have a real source (study or published benchmark). Confirm the three case studies are real and specific, not illustrative. Check that the skills matrix entries have specific rationales. Flag unverified cases for human follow-up.
- Human supplies: Nothing — Claude researches from public sources. Human must verify flagged claims.
- Output medium: screen-recording mp4 (Claude building the brief) + slate (protected practice skills matrix as a formatted table)
- The change: Ask Claude: "If AI continues improving at its current rate for 5 more years, which items in the 'protected' column would move to 'explore-then-decide' — and what would brokers need to develop next?" Show the revised matrix.
- Teardown angle: The protected practice is not defined by refusing AI. It is defined by knowing which half of the work AI cannot do — and building the practice around that half before someone else does.
- Exclusions: Cut WEF Future of Jobs statistics; cut general labor market displacement; cut technology cycle history.
- Score: 7/10

---

## Candidate 08 — Build the Due Diligence Stack Reader: Surface Cross-Document Conflicts in a Data Room with Claude

- Source: ai-for-commercial-real-estate/chapters/08-due-diligence-the-stack-ai-cant-read.md
- Lane: BUILD (Claude Code)
- Hook: Extracting every document is not the same as understanding what they say to each other. The conflict that kills a deal is between the amendment and the base lease — not inside either one.
- The artifact: A screen recording of Claude processing three related documents simultaneously (base lease, amendment, estoppel certificate) and generating a cross-document conflict report: which provisions conflict across documents, which document governs (temporal priority), and what the governing provision actually says. A Manim scene shows the three documents as stacked layers, with conflict lines appearing between them.
- Prompt seed: `claude "Read these three documents — a base lease, its second amendment, and a recent estoppel certificate — and identify cross-document conflicts. For each conflict: (1) name the provision; (2) state what each document says about it; (3) identify which document governs based on execution date and supersession language; (4) state the governing provision in plain language. Also flag any provision in the estoppel certificate that the tenant certifies as true but that appears to conflict with the base lease or amendment. Output as a conflict report table: Provision | Base Lease | Amendment | Estoppel | Governing Document | Plain-Language Summary. [paste three documents]"`
- Read / check: Verify that conflicts identified are real — the provision actually appears differently in the cited documents. Confirm the temporal priority determination is correct (later document governs unless otherwise specified). Check that the estoppel flags are specific — not generic warnings. Confirm the plain-language summary is accurate to the governing provision.
- Human supplies: Three real or realistic related documents — a base lease, an amendment, and an estoppel certificate. Synthetic illustrative documents acceptable for the video; real documents from an active deal are more impactful.
- Output medium: screen-recording mp4 (Claude terminal) + Manim stacked document animation (conflict lines appearing between layers)
- The change: Ask Claude: "Which of these conflicts represents a material risk to the buyer — one that could change the underwriting? Which are procedural and low-stakes? Rank by materiality and explain the ranking."
- Teardown angle: The data room is not a collection of individual files. It is a system — and the risk lives in the relationships between documents, not inside any one of them. AI can extract individual documents. The broker reads the system.
- Exclusions: Cut environmental disclosure stack; cut zoning contradiction analysis; cut seller disclosure fraud legal standard.
- Score: 8/10
