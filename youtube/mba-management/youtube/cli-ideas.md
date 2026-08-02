# MBA Management: with LLMs — CLI Video Ideas ("X with Claude")

Lane: RESEARCH+BUILD (organizational behavior and management theory — RESEARCH for qualitative/behavioral synthesis; BUILD for diagnostic tools and scored outputs)
Book: mba-management (19 substantive chapters covering individual behavior, teams, leadership, structure, power, HR, entrepreneurship)

---

## Card 1 — Cognitive Bias Audit for a Business Decision

**Source:** Chapter 6 (Perception and Managerial Decision Making) — Kahneman's System 1 / System 2, loss aversion, framing effect, bounded rationality, satisficing; the investment-professionals coin-flip experiment
**Lane:** RESEARCH
**Hook:** An entire room of investment professionals made opposite decisions when the same math was reframed as losses. Claude audits a real business decision for the cognitive biases that shaped it — and suggests a de-biasing protocol.
**The artifact:** A decision-audit report: given a description of a past business decision, Claude identifies (1) which System 1 heuristics or biases likely operated (anchoring, availability, representativeness, framing, overconfidence, sunk cost); (2) what the decision-maker couldn't know because of bounded rationality constraints; (3) a de-biasing checklist: pre-mortem, reference-class forecasting, devil's advocate assignment, structured deliberation.
**Prompt seed:** `claude "Analyze the following business decision for cognitive biases: [describe decision]. Apply the System 1/System 2 framework from Kahneman. Identify: (1) which heuristics likely operated (anchoring, availability heuristic, representativeness, framing, sunk cost fallacy, overconfidence); (2) how bounded rationality constrained the information considered; (3) a de-biasing protocol — list 4 specific interventions (pre-mortem, reference-class, devil's advocate, structured criteria) that would have improved the outcome."`
**Read/check:** Verify the coin-flip/loss experiment from Chapter 6 (Kahneman room of investment professionals). Confirm bounded rationality attribution to Herbert Simon (1947, Chapter 6 citation). Check that the de-biasing interventions are grounded in the chapter's recommendations.
**Human supplies:** A decision narrative — 3-5 paragraphs describing a real or illustrative business decision. The video uses the chapter's opening scenario (the Kahneman investment room) then applies it to a fictional product-launch go/no-go decision. A synthetic decision scenario is perfectly acceptable.
**Output medium:** Manim animated decision tree — the decision is shown on the left; bias icons appear as overlays at each decision node (anchor icon, sunk-cost icon, etc.); the de-biasing protocol populates as a numbered checklist on the right; final frame shows the decision re-made under the protocol.
**The change:** Apply the loss-aversion frame to the same decision — show how describing the project as "preventing a $2M loss" vs. "achieving a $2M gain" changes the instinctive response. Narrate: "Same math, opposite gut reaction. That's the frame, not the fact."
**Teardown angle:** Ask Claude to categorize the decision as "routine and reversible" vs. "novel and irreversible" using Chapter 6's matrix — and recommend whether System 1 satisficing or System 2 structured analysis was appropriate for this decision type.
**Exclusions:** No clinical psychology assessment. No individual bias testing (the chapter focuses on organizational decisions, not individual cognitive profiles).
**Score:** 9/10 — the Kahneman setup is textbook-memorable, the audit report has a clean four-beat structure (bias identification, bounded rationality, protocol, recommendation), and the framing-effect change is a perfect narrative pivot.

---

## Card 2 — Motivation Theory Matcher

**Source:** Chapter 7 (Work Motivation for Performance) — content theories (Maslow's hierarchy, Herzberg's two-factor, McClelland's acquired needs); hygiene vs. motivator factors; the Janet/Ken performance review opening in Ch. 8
**Lane:** RESEARCH
**Hook:** Maslow says give people safety. Herzberg says don't mistake safety for motivation — it's just the absence of dissatisfaction. McClelland says some people are wired for achievement, others for affiliation, others for power. Claude matches an employee profile to the right theory and prescribes the right intervention.
**The artifact:** A motivation diagnostic report: input is an employee description (role, behaviors, expressed concerns, what energizes them). Output: (1) Maslow level — which need level is currently unmet? (2) Herzberg diagnosis — is the issue a hygiene factor (fix first) or a motivator gap (then cultivate)? (3) McClelland dominant need (nAch, nAff, nPow) and its management implications; (4) three specific manager actions recommended.
**Prompt seed:** `claude "Apply three content theories of motivation to this employee profile: [describe employee]. (1) Maslow: which need level is currently unmet — physiological, safety, belonging, esteem, self-actualization? What does the manager need to address first? (2) Herzberg: is the issue a hygiene factor (compensation, working conditions, job security) or a motivator gap (recognition, growth, achievement)? (3) McClelland: what is the dominant acquired need — achievement (nAch), affiliation (nAff), or power (nPow)? Give three specific manager actions."`
**Read/check:** Verify Herzberg's hygiene vs. motivator distinction from Chapter 7 — confirm hygiene factors prevent dissatisfaction but don't create satisfaction. Confirm McClelland's three needs are nAch, nAff, nPow. Verify Maslow's five levels.
**Human supplies:** An employee profile — a 2-3 paragraph description of an employee's role, behaviors, expressed frustrations, and what they seem energized by. The video uses a synthetic composite (a mid-level analyst who's technically excellent but recently disengaged). Synthetic profiles are fine for the video.
**Output medium:** Manim animated three-panel grid — left panel shows Maslow pyramid with the unmet level highlighted; center panel shows Herzberg two-factor scale (hygiene left, motivators right) with diagnosis marked; right panel shows McClelland three-circle diagram with dominant need colored; all three panels feed into a final action list.
**The change:** Shift the employee profile to someone who has all hygiene factors satisfied (good pay, stable job) but is still disengaged — Herzberg predicts this correctly (hygiene is not motivation). Watch the diagnosis flip from "fix the hygiene" to "build the motivators (recognition, growth, achievement)." Narrate: "Fixing the environment won't fix the engagement. That's the Herzberg trap."
**Teardown angle:** Ask Claude which of the three theories best explains the Janet vs. Ron review outcome from Chapter 8 — and what motivation lever Ken failed to pull. This bridges to the performance appraisal card.
**Exclusions:** No process theories (equity theory, expectancy theory) — those are in Chapter 7's second half and would require a separate card. No compensation design analysis.
**Score:** 8/10 — three theories mapped onto one employee profile in one run; the "hygiene trap" change is a clean revelation; the three-panel animation is visually structured. High practical value for any manager.

---

## Card 3 — BARS Performance Dimension Builder

**Source:** Chapter 8 (Performance Appraisal and Rewards) — graphic rating scale failure (Ken's 24-minute review), Behaviorally Anchored Rating Scale (BARS) design; the measurement-shapes-behavior principle
**Lane:** BUILD
**Hook:** Ken's review form says "cooperation." It means nothing. Claude builds BARS — behaviorally anchored rating scales — for any job dimension, replacing vague words with observable behaviors that two different managers would rate the same way.
**The artifact:** A Python script that takes: (a) a job title, (b) a list of performance dimensions (e.g., "client communication," "team collaboration," "technical quality"), and outputs for each dimension a five-level behavioral anchor set (Outstanding → Good → Satisfactory → Fair → Unsatisfactory) as observable, specific behaviors. Rendered as a Manim animated table with each level populating in sequence.
**Prompt seed:** `claude "Build a Behaviorally Anchored Rating Scale (BARS) for a software engineer at a B2B SaaS company. Dimensions: (1) client communication, (2) code quality, (3) cross-functional collaboration, (4) problem ownership. For each dimension, write five behavioral anchors at levels Outstanding / Good / Satisfactory / Fair / Unsatisfactory. Each anchor must describe an observable behavior that two different managers would rate identically — no vague words like 'demonstrates excellence.' Use specific, verifiable actions."`
**Read/check:** Verify the BARS design process from Chapter 8 — confirm the requirement that anchors are interview-derived from experienced workers (not invented) and describe specific observable actions. Cross-check that the cooperation BARS example in the chapter is correctly represented.
**Human supplies:** Job title and list of 3-5 performance dimensions to anchor. The video uses a synthetic software engineer role. For real use, the manager supplies their team's actual job dimensions. Synthetic is fine for the video.
**Output medium:** Manim animated table — each dimension's row populates level by level (Outstanding → Unsatisfactory); each anchor appears with a behavioral specificity badge (green = observable, red = vague) to show the contrast with the graphic scale; final frame shows full BARS table.
**The change:** Apply the same five-level structure to a dimension Ken used ("personal qualities") — watch Claude struggle to produce behavioral anchors for a vague dimension, then recommend replacing it with two specific dimensions ("client feedback quality" and "conflict escalation pattern"). Narrate: "If you can't write the behavior, you can't measure the performance."
**Teardown angle:** Ask Claude to score the synthetic employee from Chapter 8 (Janet) against the BARS it just built — and compare her BARS score to the "satisfactory" Ken gave her. Show the gap: under BARS, Janet is "Outstanding" on problem ownership.
**Exclusions:** No 360-degree feedback design. No forced distribution / bell-curve ranking (Chapter 8 discusses these but they require a separate card for proper treatment).
**Score:** 8/10 — BUILD artifact (the BARS table is a deliverable managers can immediately use), the vague-to-specific transformation is visually demonstrable, and the Janet scoring teardown provides a satisfying narrative payoff.

---

## Card 4 — Negotiation Interest Map (Fisher-Ury BATNA Builder)

**Source:** Chapter 14 (Conflict and Negotiations) — task/process/relationship conflict taxonomy, interest-based negotiation (positions vs. interests), BATNA framework
**Lane:** RESEARCH
**Hook:** Two parties are fighting over a window — one wants it open, one wants it closed. Fisher and Ury say the conflict is about positions, not interests: one wants ventilation, one wants to avoid a draft. Claude maps the real interests and finds the integrative solution neither party thought of.
**The artifact:** A negotiation preparation package: given two parties and their stated positions, Claude outputs (1) interest mapping for each party (underlying needs behind the stated position); (2) BATNA (Best Alternative to a Negotiated Agreement) for each party; (3) ZOPA (Zone of Possible Agreement) identification; (4) three integrative options that satisfy both parties' interests without either conceding their position.
**Prompt seed:** `claude "Prepare a negotiation analysis for the following scenario: Party A (described) holds position [X]. Party B (described) holds position [Y]. Apply interest-based negotiation: (1) Map the underlying interests behind each party's position — what do they actually need? (2) Estimate each party's BATNA — what do they do if no deal is reached? (3) Identify the ZOPA — the range where a deal is possible. (4) Generate three integrative proposals that satisfy both parties' core interests."`
**Read/check:** Verify Chapter 14's distinction between task conflict (content of work), process conflict (how work is done), and relationship conflict (interpersonal). Confirm Fisher-Ury interest-based negotiation is the recommended approach (principled negotiation). Check that BATNA and ZOPA are correctly defined.
**Human supplies:** A negotiation scenario — two parties, their stated positions, and context. The video uses the classic salary negotiation between a manager and an employee as the example (manager: position is 5% raise; employee: position is 15% raise). Synthetic scenario is fine.
**Output medium:** Manim animated interest map — two columns (Party A / Party B) with position at the top and interests below; arrows connect shared interests in the center ZOPA zone; three integrative proposals appear as synthesis boxes at the bottom.
**The change:** Reveal that Party A's BATNA just worsened (e.g., the employee has a competing job offer) — ask Claude to re-analyze how this shifts the ZOPA and changes the integrative proposals. The map reorganizes: Party A's minimum acceptable outcome moves up; Party B must offer more to stay in the zone.
**Teardown angle:** Ask Claude to classify the conflict type (task/process/relationship) and recommend whether mediation, arbitration, or direct negotiation is most appropriate for this conflict type.
**Exclusions:** No legal contract drafting. No multi-party/multi-issue negotiations (Chapter 14 covers two-party scenarios).
**Score:** 9/10 — the interest-mapping visual is one of the clearest negotiation teaching tools possible; the BATNA-shift change has real narrative drama; the ZOPA zone animation is elegant. Highly applicable to every viewer's professional life.

---

## Card 5 — Power Base Analyzer for an Organizational Influence Challenge

**Source:** Chapter 13 (Organizational Power and Politics) — Weber's power definition, French and Raven's five bases (referent, expert, legitimate, reward, coercive), the CFO/hallway gap, the VP-who-lost-despite-authority case
**Lane:** RESEARCH
**Hook:** The VP had the title. The org chart showed him in charge. He never changed anything. Claude diagnoses why by mapping which power base he was relying on vs. which ones he needed — and prescribes how to build the missing ones.
**The artifact:** A power-base diagnostic report: given a description of an influence challenge ("I need X to change but they aren't responding"), Claude identifies (1) which of the five power bases the requestor currently holds with respect to the target; (2) which bases are absent; (3) what behavioral response each missing base would generate (commitment/compliance/resistance); (4) a three-step power-building plan using the bases that are achievable in the timeframe.
**Prompt seed:** `claude "Analyze the following organizational influence challenge: [describe situation — who is trying to influence whom, what they are trying to change, what has been tried]. Apply French and Raven's five power bases: (1) Referent — does the influencer have personal appeal/admiration with this target? (2) Expert — is their relevant expertise visible and credible to the target? (3) Legitimate — what is the scope of their formal authority with this target? (4) Reward — what rewards can they credibly offer? (5) Coercive — what sanctions are available and believable? Score each base 0-5 and prescribe three power-building actions."`
**Read/check:** Verify the five bases (French and Raven, 1950s) from Chapter 13. Confirm the behavioral response mapping: referent → commitment; expert/legitimate/reward → compliance; coercive → resistance. Verify the VP/hiring-cycle case from Chapter 13.
**Human supplies:** An organizational influence challenge description — who needs to be influenced, what behavior change is needed, what formal authority exists. The video uses the Chapter 13 case (VP trying to streamline background-check cycle time). Synthetic scenarios are fine.
**Output medium:** Manim animated five-bar scorecard — each power base scored 0-5 as a horizontal bar, color-coded (green = strong, red = weak); behavioral response labels appear next to each bar; three-step plan appears as animated action items below the scorecard.
**The change:** Shift the target from a peer to a superior (upward influence scenario) — watch legitimate power drop to near-zero (you have no formal authority over them) and the prescription shift entirely to referent and expert power building. Narrate: "Managing up requires different tools than managing down."
**Teardown angle:** Ask Claude to identify one behavior the VP should stop (reliance on coercive escalation through HR) and one behavior he should start (public expert-knowledge contribution to build referent power) within the next 30 days.
**Exclusions:** No organizational politics strategy (coalition building, issue framing — Chapter 13 covers these but they require a separate card). No stakeholder mapping analysis.
**Score:** 8/10 — the five-bar scorecard is visually clean, the upward-influence change prompt reveals a genuinely different prescription, and the VP case is a memorable anchor. The concept is abstract but Claude operationalizes it into concrete scores.

---

## Card 6 — Organizational Structure Designer

**Source:** Chapter 16 (Organizational Structure and Change) — Burns and Stalker's mechanistic vs. organic spectrum, Weber's structural levers (specialization, hierarchy, formalization, centralization, span of control), Sloan's multidivisional GM, contingency theory
**Lane:** RESEARCH+BUILD
**Hook:** The CEO moved boxes on the org chart. Nothing changed. Claude diagnoses the gap between the formal structure and the actual coordination flow — then recommends the structural levers that match this organization's environment.
**The artifact:** A structural design report: given an organization's size, environment (stable vs. turbulent), and current structural symptoms (slow decisions, coordination failures, inconsistent quality, etc.), Claude outputs (1) environment classification (stable/turbulent); (2) current structure diagnosis (mechanistic/organic/hybrid); (3) recommended settings for each of Weber's five levers; (4) the one change most likely to have the biggest impact.
**Prompt seed:** `claude "Design the optimal organizational structure for the following organization: [describe size, industry, environment, current problems]. Apply Burns and Stalker's contingency theory: classify the environment as stable, moderately turbulent, or highly turbulent. Then recommend settings for each of Weber's five structural levers: (1) specialization (narrow vs. broad roles), (2) hierarchy depth (flat vs. deep), (3) formalization (few vs. many written rules), (4) centralization (centralized vs. decentralized decisions), (5) span of control (wide vs. narrow). Identify the single highest-leverage structural change."`
**Read/check:** Verify Burns and Stalker's study (20 British electronics firms, 1961, Chapter 16). Confirm the contingency principle: stable + mechanistic works; turbulent + organic works; the other two quadrants fail. Verify Sloan's GM multidivisional structure from Chapter 16.
**Human supplies:** An organization description — size, industry, operating environment, and current structural complaints. The video uses a 200-person SaaS company that grew from 20 to 200 in two years and is experiencing coordination breakdowns. Synthetic is acceptable.
**Output medium:** Manim animated matrix — Burns/Stalker 2×2 (environment × structure) with the organization's current position marked; a separate five-slider visualization shows each Weber lever with its current setting (red) vs. recommended setting (green); the delta animates as a slide.
**The change:** Fast-forward: the company enters a stable phase (government contract, long-term SLA). Ask Claude to re-run the analysis — the prescribed structure shifts toward more mechanistic (more formalization, narrower spans, deeper hierarchy). Narrate: "The right structure is contingent on the environment, not a permanent identity."
**Teardown angle:** Ask Claude to identify the two informal coordination mechanisms that are doing the most work that the formal structure doesn't capture — these should be preserved and formalized in the redesign rather than disrupted.
**Exclusions:** No change management communications plan. No culture change strategy (the chapter explicitly notes the informal organization changes on its own timeline — Claude acknowledges this but doesn't prescribe culture change here).
**Score:** 8/10 — the five-lever slider animation is visually instructive, the contingency-theory principle is testable, and the stable-phase change prompt shows the model is dynamic. The "informal coordination preserved" teardown is practically valuable.

---

## Card 7 — Leadership Style Selector

**Source:** Chapter 12 (Leadership) — trait research (heritability of leadership, Big Five), Ohio State behavioral studies (initiating structure vs. consideration), Fiedler's contingency model, transformational vs. transactional leadership
**Lane:** RESEARCH
**Hook:** Leadership researchers spent decades hunting for the traits that make a leader. They found a list. Then they found the list doesn't predict outcomes — situations do. Claude assesses a leadership situation and prescribes the right behavioral style.
**The artifact:** A leadership prescription report: given a description of a leader, their team, and their situation, Claude outputs (1) trait summary (Big Five relevant dimensions); (2) Ohio State behavioral position (high/low on initiating structure and consideration — four quadrants); (3) Fiedler situational favorability assessment (leader-member relations, task structure, position power); (4) recommended leadership style for this specific situation; (5) one behavioral change the leader should make immediately.
**Prompt seed:** `claude "Prescribe a leadership approach for the following situation: [describe leader, team, and situation]. Apply three frameworks: (1) Ohio State: score this leader on Initiating Structure (task focus, role clarity, goal-setting) and Consideration (relationship quality, employee welfare) — place them in the four-quadrant model. (2) Fiedler: assess situational favorability — rate leader-member relations, task structure, and position power as high/low. (3) Based on the favorability, prescribe either task-oriented or relationship-oriented leadership. Give one specific behavioral change."`
**Read/check:** Verify the Ohio State studies from Chapter 12 (initiating structure and consideration as independent dimensions — not a single continuum). Confirm Fiedler's key finding: task-oriented leaders outperform in very high and very low favorability; relationship-oriented leaders outperform in the middle. Check heritability figure (approximately 30% for leadership emergence, Chapter 12).
**Human supplies:** A leadership scenario — a leader's profile and their team's current situation. The video uses a synthetic new manager inheriting a disengaged team with unclear processes (moderate Fiedler favorability). Synthetic scenario is acceptable.
**Output medium:** Manim animated three-panel analysis — Panel 1: Ohio State 2×2 grid with the leader plotted; Panel 2: Fiedler favorability scale (leader-member relations, task structure, position power scored); Panel 3: prescription arrow pointing to the recommended style with behavioral action items.
**The change:** The team's task structure improves (the company implements clear project management processes) — favorability rises. Re-run Fiedler. The prescription shifts from "task-oriented" to "relationship-oriented." Narrate: "The effective leader is not one style — it's the right style for the situation, which changes."
**Teardown angle:** Ask Claude to identify the gap between this leader's natural style (as described) and the prescribed style — and give one coaching conversation structure the leader could use with their manager to get support for the transition.
**Exclusions:** No full transformational/transactional leadership scoring (Chapter 12 covers this but it requires a separate card focused on vision and inspiration rather than situational contingency). No 360-degree leadership assessment.
**Score:** 8/10 — three frameworks synthesized in one run, the favorability-shift change is a clean demonstration of contingency logic, and the Ohio State 2×2 animation is a reliable teaching visual.

---

## Card 8 — Startup Runway and Pivot Decision Analyzer

**Source:** Chapter 19 (Entrepreneurship) — Sara's 11 PM spreadsheet (runway = savings ÷ burn), product-market fit, actual startup survival rates (Bureau of Labor Statistics: 50% at 5 years, not 10%), effectuation vs. causation
**Lane:** BUILD
**Hook:** Sara has $47,000, burns $8,000 a month, and two customers paying a combined $450. How many months until she must make a decision? Claude builds the runway calculator, models the inflection scenarios, and tells her when she must pivot or raise.
**The artifact:** A Python startup runway model: inputs are current cash, monthly burn, current MRR, projected MRR growth rate. Outputs: (1) current runway in months; (2) a scenario matrix showing runway under three growth cases (bear/base/bull); (3) the month when cash hits a critical threshold (e.g., 2 months runway remaining = fundraising trigger); (4) a pivot-or-raise decision framework based on MRR trajectory vs. burn.
**Prompt seed:** `claude "Build a startup runway model. Inputs: cash=47000, monthly_burn=8000, current_mrr=450, mrr_growth_rate_bear=0.05, mrr_growth_rate_base=0.15, mrr_growth_rate_bull=0.30. Compute monthly cash balance for each scenario until cash hits zero. Identify: (1) runway in each scenario; (2) the month when 2-month trigger is hit (fundraising or pivot decision point); (3) the MRR level needed to reach default-alive (monthly revenue >= monthly burn). Animate three cash curves in Manim."`
**Read/check:** Verify Sara's financial data from Chapter 19 (cash=$47,000, burn=$8,000, two customers at $300+$150=$450/month). Confirm the Bureau of Labor Statistics survival rate (50% at 5 years) is cited correctly from Chapter 19.
**Human supplies:** Nothing — synthetic inputs from the chapter. For real use, founder supplies their own burn rate and MRR. Synthetic is fine for the video.
**Output medium:** Manim animated three-curve chart — bear/base/bull runway curves sweep month by month; the "2-month trigger" horizontal line appears as a threshold; the "default alive" MRR level annotated as a second horizontal line; each scenario's runway labeled at the x-axis crossing.
**The change:** Add one new enterprise customer at $2,000/month in month 3 (a realistic discovery pivot from SMB to enterprise). Watch the base-case curve reverse slope — the company reaches default-alive in month 7 instead of running out in month 6. Narrate: "One customer at the right price point changes everything. That's a pivot, not a failure."
**Teardown angle:** Ask Claude to compute the minimum number of customers at the current average ($225) needed to reach default-alive — and compare that to the number of customers achieved by month 6. This surfaces the product-market fit quantification problem: the math shows how many customer conversations Sara needs to have this month.
**Exclusions:** No VC fundraising valuation model (that requires a separate card). No unit economics / LTV:CAC analysis (out of scope for this chapter's level).
**Score:** 9/10 — clean BUILD artifact (the three-curve animation is vivid), the chapter's own data makes the numbers concrete, the enterprise-customer change is a realistic pivot scenario with genuine emotional impact. One of the highest-scored cards in the batch.
