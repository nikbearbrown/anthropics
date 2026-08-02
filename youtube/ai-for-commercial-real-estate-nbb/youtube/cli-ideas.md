# AI for Commercial Real Estate (NBB Edition) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Comp Audit: Expose What the AVM Selected and Why It's Wrong with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/05-property-valuation-what-ai-can-model-and-what-the-market-actually-is.md
- Lane: BUILD (Claude Code)
- Hook: The model picked four comps. One was an off-market relationship sale. One had tenant credit that doesn't exist in your deal. One is outside the pedestrian pattern that makes your property valuable. The number looks authoritative. It was built on the wrong evidence.
- The artifact: A screen-recording of Claude ingesting a CSV of 8–10 comp candidates (address, sale price, date, distance, conditions) and flagging each against a four-criteria audit checklist (arm's-length test, relevant submarket, comparable tenant credit, non-distressed sale). Claude outputs a markdown table marking each comp as Keep / Exclude / Investigate, with one-line rationale. A D3 v7 standalone HTML then renders the before/after valuation — original AVM number vs. audited comp set — as a two-bar animated chart.
- Prompt seed: `claude "I have a comp set for a retail property in Beverly Hills. Here are the raw comps: [paste CSV]. For each comp, evaluate it against four criteria: (1) arm's-length transaction — no relationship pricing; (2) relevant submarket — within the pedestrian demand pattern; (3) comparable tenant credit profile; (4) no distressed-seller motivation (loan maturity, partnership dissolution). Output a markdown table: Comp Address | Keep/Exclude/Investigate | Criterion Failed | Rationale. Then estimate how removing the excluded comps changes the indicated value range."`
- Read / check: Verify each exclusion rationale maps to a specific criterion from the chapter. Confirm the value range shifts meaningfully when flagged comps are removed. Check that the D3 chart's before/after bars are labeled with the specific counts of included comps, not just raw numbers.
- Human supplies: A realistic synthetic comp CSV (8–10 rows) with planted exclusion triggers — one off-market, one wrong submarket, one wrong tenant profile. The chapter's Beverly Hills scenario is the direct stand-in.
- Output medium: screen-recording mp4 (terminal session + D3 animated two-bar chart)
- The change: Add a second pass where Claude generates follow-up research questions for the "Investigate" flagged comps — what broker, what public record, what data source would confirm or exclude each one. Show those questions appear in the output as a numbered checklist.
- Teardown angle: The model does not know which transactions are evidence of what a willing buyer would pay today. The broker who audits the comp set is not overriding the model — she is doing the step the model cannot do.
- Exclusions: Cut terminal cap rate sensitivity analysis; cut ARGUS field-level discussion; cut portfolio screening use case.
- Score: 9/10

---

## Candidate 02 — Build the Lease Abstraction Gate: Catch the 5% Before It Costs You with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/07-lease-abstraction-the-95-that-hides-the-5.md
- Lane: BUILD (Claude Code)
- Hook: The AI extraction was 95% accurate. The 5% it missed included the co-tenancy clause and the kick-out provision. Both change the deal economics. The tool doesn't know what it doesn't know.
- The artifact: A screen-recording of Claude receiving a realistic lease excerpt (900–1,200 words, synthetic) and running it against a seven-item material-clause checklist: rent escalation, renewal options, ROFO/ROFR, co-tenancy, CAM exclusions, exhibit-defined terms, amendment priority. For each item Claude outputs: Found / Not Found / Requires Verification, plus the exact clause text or "absent." A Manim animation then renders the seven-item checklist as a vertical progress bar — items light up green (found) or red (not found/requires verification) in sequence.
- Prompt seed: `claude "Extract and evaluate the following seven material clauses from this lease excerpt: (1) rent escalation — fixed steps or CPI-linked; (2) renewal options — number, notice period, rent basis; (3) ROFO or ROFR on adjacent space; (4) co-tenancy trigger and remedy; (5) CAM exclusions — what the landlord cannot charge; (6) exhibit-defined terms — any clause that defers its definition to an exhibit; (7) amendment priority — which document governs if there is a conflict. For each: Found / Not Found / Requires Verification, clause text verbatim if found, location in document. Flag any clause that could materially change deal economics if misread. [paste lease excerpt]"`
- Read / check: Verify all seven checklist items appear in the output, even when the clause is absent. Confirm the "Requires Verification" category triggers appropriately on exhibit-defined terms. Check that the Manim animation sequence is readable at video resolution.
- Human supplies: A synthetic 900–1,200 word lease excerpt with at least two planted gaps (a co-tenancy clause buried in a rider, an amendment that supersedes a base lease term). The chapter's worked example provides the scenario logic.
- Output medium: screen-recording mp4 (terminal) + Manim (seven-item checklist animation)
- The change: Run the same checklist on a second, cleaner lease and show how the green/red pattern shifts. Then prompt Claude: "Which of the Not Found clauses in lease one would a landlord-favorable form omit by default?" — show Claude's answer naming the strategic omission pattern.
- Teardown angle: The AI produces a confident output whether the extraction is clean or not. The checklist is what converts the AI output into a professional work product. The gate is not distrust — it is the specific cognitive operation the tool cannot perform.
- Exclusions: Cut FERPA; cut portfolio abstraction at scale workflow; cut SNDA discussion.
- Score: 9/10

---

## Candidate 03 — Build the Working Line: Map Your Task List Against Delegate / Review / Guard with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/02-the-tasks-you-should-hand-off-today.md
- Lane: BUILD (Claude Code)
- Hook: Most brokers who get into trouble with AI do one of two things: treat Delegate-with-Review tasks as Delegate tasks, or hand off Guard tasks entirely. The working line prevents both. It takes 20 minutes to build and saves you the expensive mistake.
- The artifact: A D3 v7 standalone HTML file rendering an interactive three-column workflow map: Delegate (green) / Delegate with Review (yellow) / Guard (red). Ten CRE task labels — property description, rent roll cleanup, OM data extraction, lease abstract, comp sheet, market summary, valuation opinion, negotiation position, disclosure decision, client recommendation — populate the columns as draggable cards. Clicking a card reveals a one-sentence rationale and the specific review checkpoint for Delegate-with-Review items. Screen-recorded with the broker walking one task through the classification logic live.
- Prompt seed: `claude "Build a self-contained D3 v7 HTML file that renders a three-column task classification board for a CRE broker's AI workflow. Columns: Delegate (AI does it, light review), Delegate with Review (AI does first pass, structured review before client), Guard (AI may assist, human owns output). Populate with 10 task cards: property description draft, rent roll cleanup, OM data extraction, lease abstract for internal use, comp sheet, market summary, cap rate opinion, negotiation position, disclosure decision, client recommendation memo. Each card clickable — expands to show specific review checkpoint. Color-code by column. Inline CSS and D3 7.9.0 from cdnjs."`
- Read / check: Verify all 10 tasks route to the correct column per the chapter's three-position framework. Confirm the review checkpoints for Delegate-with-Review tasks are specific (not "review carefully") — each should name the failure mode to check. Confirm the Guard column tasks carry the correct rationale.
- Human supplies: Nothing — fully synthetic. Real-data upgrade: broker inputs their own weekly task list and classifies each one, generating a personal operating rule.
- Output medium: screen-recording mp4 (browser interaction of D3 board with expand/collapse)
- The change: Add a fourth card slot — "Add your task" — that prompts the viewer to name a task they use AI for today and drop it into a column. Show the empty slot appear in the final frame with a voiceover: "Where does your task sit?"
- Teardown angle: The expensive way to use AI is to decide from scratch every time. The cheap way is to make the decision once, write it down, and stop making it again. The board is the one-page operating rule.
- Exclusions: Cut California DRE licensee supervision detail; cut team-management scenario; cut FERPA.
- Score: 8/10

---

## Candidate 04 — Build the Market Variance Memo: Separate What the Model Knows from What the Market Is Doing with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/10-market-analysis-when-the-model-is-behind-the-market.md
- Lane: BUILD (Claude Code)
- Hook: The model's training data is last quarter's transactions. The buyer pool changed this week. The capital markets moved on Tuesday. The broker who reads the model output as current market intelligence is reading last quarter's news with today's date on it.
- The artifact: A screen-recording of Claude receiving a market summary (from a real data provider or a realistic synthetic one) and generating a two-section "baseline + variance" memo: Section 1 replicates what the model can reliably infer from historical data (average cap rates, absorption, vacancy, rent trends over 24 months); Section 2 lists what the model cannot know — this week's buyer pool, recent capital markets movement, local relationship trades not in closed-transaction data, demand signals from forward-looking platforms. A Manim animation shows two labeled boxes (model layer / market layer) with arrows indicating what data flows into each and what stays outside.
- Prompt seed: `claude "I have this market summary for [submarket]: [paste summary]. Generate a two-section memo. Section 1 — Baseline (what the model reliably infers): summarize the historical cap rate range, absorption trend, vacancy trajectory, and rent movement from this data. Section 2 — Variance (what this model cannot know): list the specific market factors not captured here — current buyer pool activity, recent capital markets shifts, off-market transaction conditions, forward-looking demand signals, and cycle position. For each variance item, name one specific data source or broker action that would close the gap."`
- Read / check: Verify Section 1 draws only from what's in the provided summary (no fabricated statistics). Confirm Section 2 names specific gap items rather than generic "unknown factors." Check that each variance item has a specific gap-closing action — not "do additional research" but a named source or action.
- Human supplies: A realistic synthetic market summary (can be generated from public CoStar/CBRE/JLL market report excerpts). Optionally a real market report for a specific submarket.
- Output medium: screen-recording mp4 (terminal session) + Manim (two-layer diagram animation)
- The change: Show the broker adding a third section manually — "Local intelligence" — with three bullets the model couldn't supply: a relationship trade that doesn't show in closed data, a tenant requirement tracked on a platform, a capital markets signal from this week. Contrast the three-section memo against the raw model output.
- Teardown angle: The model does not know where you are in the cycle. It knows where the market was when the training data was collected. The variance memo is how you use the model correctly — as a baseline, not a conclusion.
- Exclusions: Cut specific vendor platform comparisons; cut appraisal methodology detail; cut ARGUS discount rate sensitivity.
- Score: 8/10

---

## Candidate 05 — Build the Negotiation Prep Brief: What AI Can Map Before You Walk In the Room with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/09-negotiation-the-room-ai-has-never-been-in.md
- Lane: BUILD (Claude Code)
- Hook: Both brokers walk in AI-prepared. The information asymmetry that used to define CRE negotiation leverage has narrowed to nearly nothing. The new asymmetry is in the room — the signals AI prep materials will never contain.
- The artifact: A screen-recording of Claude receiving a deal summary and generating a structured negotiation prep brief: (1) interests-and-options analysis — likely underlying interests for each party, structured options satisfying multiple interests, objective criteria both parties might accept; (2) counterargument map — the three most likely objections and responses; (3) fallback term sheet — the minimum acceptable positions for each key term. A second prompt then asks Claude to name the five signal categories it cannot supply — commitment vs. parallel negotiation, likelihood of retrade, principal alignment, relationship history, moment to stop pushing — and what the broker needs to supply for each before the meeting.
- Prompt seed: `claude "I'm preparing for a lease negotiation on a 15,000 SF office renewal in [submarket]. Tenant: [profile]. Landlord: [profile]. Key terms in dispute: renewal rate, TI allowance, term length. Generate a negotiation prep brief: (1) interests-and-options analysis — separate positions from interests for each party, generate three options satisfying multiple interests, list two objective criteria references; (2) counterargument map — three most likely objections from the other side and specific responses; (3) fallback term sheet — minimum acceptable position for rent, TI, and term. Then list what this brief cannot tell me — name the five in-room signals that require direct observation."`
- Read / check: Verify the interests-and-options analysis separates stated positions from underlying interests (not just restating what each party wants). Confirm the counterargument map includes at least one non-obvious objection. Check that the "cannot tell me" section names all five signal categories from the chapter.
- Human supplies: A synthetic deal summary (tenant profile, landlord profile, disputed terms). Optionally a real deal in progress with identifying details changed.
- Output medium: screen-recording mp4 (terminal session showing both prompt rounds)
- The change: Add a third prompt: "For each of the five in-room signals, give me one specific question I can ask or one observation I can make in the first 15 minutes of the meeting to read that signal." Show Claude's response, then label each answer: "Claude can script the question. The broker reads the answer."
- Teardown angle: Preparation and performance are different activities requiring different capabilities. The gap is not vague — it is located at a specific moment in every negotiation. The broker who knows where to look has an advantage.
- Exclusions: Cut Fisher-Ury-Patton literature review; cut Lax-Sebenius academic framing; cut Garmaise-Moskowitz research citation.
- Score: 8/10

---

## Candidate 06 — Build the Offering Memorandum Screener: Extract and Pressure-Test the Seller's Assumptions with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/04-when-it-works-real-wins-from-the-field.md
- Lane: BUILD (Claude Code)
- Hook: The cap rate in the OM is the seller's assumption. Your job is to test whether it's defensible. The tool gets you to the data faster. The judgment — whether it holds — is still yours.
- The artifact: A screen-recording of Claude receiving a realistic OM excerpt (600–900 words, synthetic) and extracting key screening fields: asking price, NOI, implied cap rate, tenant roster, lease expiration schedule, TI assumptions. Claude then runs a pressure-test pass: (1) compares the implied cap rate to a stated market range; (2) flags any lease expiration within 24 months as a rollover risk; (3) identifies any vacancy or lease-up assumptions and labels them as stated vs. evidenced. Output as a structured markdown table. A Manim animation renders the screening output as a traffic-light matrix — green (verified), yellow (requires validation), red (flags stated assumption only).
- Prompt seed: `claude "Extract and pressure-test the key screening fields from this offering memorandum excerpt: [paste OM excerpt]. Step 1 — Extract: asking price, stated NOI, implied cap rate, tenant roster (name, % of rent, lease expiration), TI allowance assumptions, vacancy assumptions. Step 2 — Pressure-test: (1) is the implied cap rate within the stated market range for this asset class? (2) are any leases expiring within 24 months? flag as rollover risk; (3) which assumptions are stated vs. evidenced by closed comparables? Output as a structured markdown table with a Flag column: Verified / Requires Validation / Stated Assumption Only."`
- Read / check: Verify the extraction covers all six field categories. Confirm the pressure-test logic distinguishes stated assumptions from evidenced ones (does not treat seller claims as confirmed). Check that the Manim traffic-light animation is legible and the red/yellow/green mapping matches the Flag column logic.
- Human supplies: A synthetic OM excerpt (600–900 words) with planted assumption gaps — a cap rate above market range, a tenant expiring in 18 months, a lease-up assumption with no comp support. The chapter's Dealpath scenario provides the framework.
- Output medium: screen-recording mp4 (terminal session) + Manim (traffic-light matrix animation)
- The change: Show a second pass where Claude generates a due-diligence follow-up list from the red and yellow flags — one specific action item per flag (what to request, from whom, by what method). Contrast the raw OM number against the flagged output to show the judgment gap visually.
- Teardown angle: Speed to informed attention is not the same as speed to conclusion. The tool handles the mechanical work of finding and formatting the data. The broker handles the interpretation — does this assumption hold for this deal in this market today?
- Exclusions: Cut ARGUS field-level mapping; cut portfolio-scale screening workflow; cut Dealpath vendor discussion.
- Score: 8/10

---

## Candidate 07 — Build the Workflow Policy: Write the One-Page Operating Rule for Your Team with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/11-building-your-ai-workflow.md
- Lane: BUILD (Claude Code)
- Hook: Four agents, same brokerage, same tool. Agent A reviews carefully. Agent B sends without review. Agent C doesn't use it. Agent D delegates the final recommendation. One of those tracks is a liability. The broker who can't describe the team's AI workflow can't demonstrate the supervision the license requires.
- The artifact: A screen-recording of Claude generating a one-page team AI workflow policy from a broker's task list and risk tolerance input. The output is a three-column markdown table: Task | Category (Delegate / Delegate-with-Review / Guard) | Review Checkpoint (specific failure mode to check). Eight to ten tasks populate the table. A second prompt asks Claude to generate a "review protocol" for the three Delegate-with-Review items — naming the specific failure modes to check for each, not "review carefully" but a named checklist. The final document exports as a readable one-pager.
- Prompt seed: `claude "I'm a supervising broker building a one-page AI workflow policy for my team of four agents. Our tasks include: property description drafts, rent roll cleanup, OM data extraction, lease abstracts for client delivery, comp sheets, market summaries, pricing opinions, negotiation positions, and client recommendation memos. For each task, classify it as Delegate (AI produces, light review), Delegate-with-Review (AI produces, structured review before client delivery), or Guard (AI assists, human owns output). For each Delegate-with-Review task, name the specific failure mode to check — not 'review carefully' but the exact thing that can go wrong. Output as a three-column markdown table. End with two sentences: what triggers a reclassification, and what the document does not replace."`
- Read / check: Verify the classification matches the chapter's three-position framework. Confirm each Delegate-with-Review review checkpoint names a specific failure mode (comp selection criteria, clause accuracy, source dates). Check that Guard tasks include the correct rationale — accountability cannot transfer.
- Human supplies: Nothing — the task list is fully synthetic. Real-data upgrade: broker inputs their actual task list and the policy generates for their specific team.
- Output medium: screen-recording mp4 (terminal session showing the policy build in two prompt rounds)
- The change: Add a third prompt: "What are the three most likely ways this policy breaks down under deadline pressure? For each, add one structural safeguard to the policy that would survive that pressure." Show the final policy with the three added safeguards — compare before/after to show the policy hardening.
- Teardown angle: The broker who makes the AI decision case-by-case under deadline pressure is not protecting himself. The documented workflow is not a compliance exercise — it is a cognitive efficiency tool. The decision gets made once, in a calm moment, and applied every time.
- Exclusions: Cut California DRE regulatory citation; cut 90-page policy warning; cut multi-platform tool comparison.
- Score: 7/10

---

## Candidate 08 — Research the Liability Line: What Happens When AI-Assisted CRE Advice Is Wrong with Claude

- Source: ai-for-commercial-real-estate-nbb/chapters/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it.md
- Lane: RESEARCH (Claude assistant)
- Hook: The AI was wrong. Your name is on the memo. What does the liability framework actually say about that? The answer is not in the tool's terms of service — it's in agency law, E&O coverage, and state licensing regulations.
- The artifact: A sourced 4-section research brief synthesized by Claude: (1) the current legal framework for professional liability when AI-assisted advice is wrong in a real estate transaction — agency law, negligent misrepresentation, E&O insurance coverage triggers; (2) three documented or hypothetical case scenarios where the AI-human accountability split creates a gap; (3) what state licensing boards currently say about AI use in licensed practice — cite at least two states; (4) three specific workflow controls a broker can implement today that would survive a liability review. Rendered as a formatted markdown document, screen-recorded as the synthesis builds.
- Prompt seed: `claude "Research the professional liability framework for AI-assisted advice in commercial real estate. I need a sourced brief covering: (1) how agency law and negligent misrepresentation apply when a broker relies on AI-generated market analysis or valuation data that turns out to be wrong; (2) whether E&O insurance typically covers AI-assisted errors — check current policy language trends; (3) what at least two state real estate licensing boards have said about AI tool use in licensed practice; (4) three specific workflow controls — documentation practices, review protocols, disclosure language — that would reduce liability exposure. Cite sources. Flag any claim you cannot verify."`
- Read / check: Verify the legal framework citations are real and current — do not accept fabricated case citations. Check that the E&O coverage discussion reflects actual policy trends, not assumptions. Confirm the state licensing board citations name real jurisdictions with real guidance. Flag all unverified claims for human legal review before any professional use.
- Human supplies: Nothing — Claude synthesizes from public sources. Human (ideally an attorney) must verify all legal claims before applying them professionally. Research is a starting point for due diligence, not legal advice.
- Output medium: screen-recording mp4 (Claude chat session building the brief) + slate (the final formatted brief as a document image)
- The change: Ask Claude to stress-test its own brief: "What is the strongest argument that these workflow controls would be insufficient in a high-stakes transaction? Where is the remaining gap?" Show Claude's response, then label: "This is the follow-up question to take to your E&O broker and legal counsel."
- Teardown angle: The tool's terms of service indemnify the vendor, not the broker. The liability lives in the professional relationship — the fiduciary duty, the license, the signed deliverable. The workflow control is not optional risk management. It is the specific act that determines whether the broker or the AI is accountable.
- Exclusions: Cut specific case law citations beyond what Claude can verify; cut insurance premium detail; cut state-by-state regulatory mapping beyond two examples.
- Score: 7/10
