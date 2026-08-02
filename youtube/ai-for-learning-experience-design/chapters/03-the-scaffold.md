# Chapter 3 — The Scaffold: Interaction Designs That Preserve Learning
*Three architectures, seven patterns, and the one test that tells them apart.*

The strongest positive finding in AI tutoring research so far did not come from an AI working alone. It came from an AI on a leash.

In UK secondary schools, students practicing mathematics on Eedi were randomized into three support conditions: static hints, human tutors working unaided, or an AI tutor built on Google DeepMind's LearnLM, *supervised by a human tutor* who reviewed each AI message before it reached the student (Eedi & Google DeepMind 2025, arXiv:2512.23633 — the authors' own label for this is "exploratory RCT," and that label stays attached throughout this chapter). The supervision proved light-touch: tutors approved LearnLM's messages with zero or minimal edits 76.4% of the time. The AI did most of the talking. The human did something else — quality assurance on pedagogy, catching the fraction of moments where the AI's next move would have been wrong for *this* student.

<!-- FACT-CHECK FLAG: IMPRECISE (full text checked) — "randomized into three support conditions" overstates the design. Per arXiv:2512.23633 full text: two-level randomization — students were randomized to control (static hints, N=91) vs. tutoring (N=74); then each tutoring SESSION (not student) was randomized to human-alone vs. supervised LearnLM. Also note: the +5.5 pp transfer estimate carries a 95% credible interval of [−1.4, +12.4] with 93.6% posterior credibility — the interval crosses zero. See factchecks/03-the-scaffold-assertions.md -->



On immediate outcomes, supervised-AI students performed at least as well as human-tutored students. Parity findings rarely make headlines. The headline is what happened next: facing a novel problem in the *next* topic — material the tutoring had not covered — supervised-AI students were **5.5 percentage points more likely to solve it** than students tutored by humans alone.

Read that against everything Chapters 1 and 2 taught you to fear. This is not an assisted score; the AI was gone. It is *transfer* — the most demanding endpoint, the one that measures whether learning traveled. The field that produced the −17% also produced an AI-mediated design beating human tutoring on the endpoint that matters most.

Now the puzzle, gentler than Chapter 1's but deeper. The GPT Base students had a frontier model, unrestricted, and got worse. These students had a frontier model plus a human checkpoint — and beat humans alone on transfer. And a third study this chapter covers flips the arrangement entirely — AI whispering suggestions to human tutors — where the biggest gains went to students of the weakest tutors. Three places to put the human. Three positive results. One principle underneath, which this chapter names.

Hold the epistemic frame as you go: exploratory, industry-published (one author is the model's maker — a conflict to note, not a reason to dismiss), single context, unreplicated. The field's strongest positive finding *and* a finding on thin ice. Both stay on the table.

![Figure 3.1 — Three architectures, one placement question: pedagogical judgment encoded in advance (constrain the AI), at a runtime human checkpoint (supervise the AI — 76.4% of messages passed with zero or minimal edits), or kept with the human, amplified (support the human); not a quality ranking (Eedi/LearnLM: exploratory RCT, industry-published)](../images/03-the-scaffold-fig-01.png)

---

The word "scaffolding" has been diluted in EdTech until it means roughly "any help." Recover the original meaning, because it contains the design discipline.

Wood, Bruner, and Ross (1976) coined the term watching tutors help children build a block pyramid they could not build alone. Scaffolding, in their analysis, was not doing the task for the child — it was a set of moves that kept the child doing *the parts within reach* while the tutor temporarily held the rest. The concept pairs with Vygotsky's zone of proximal development: the band of tasks a learner cannot do alone but can do with support. Help inside the band builds capability. Help that simply performs the task replaces the learner instead of developing them.

Three properties make support a scaffold rather than a crutch (van de Pol, Volman & Beishuizen 2010):

**Contingency.** Support responds to *this learner's current state* — diagnosed from their attempt, not dispensed generically. The AI that answers regardless of what the learner has tried is not contingent; it is a vending machine.

**Fading.** Support contracts as competence grows. A scaffold is temporary by definition. Nothing in construction terminology implies permanent scaffolding; the metaphor contains its own expiration date.

**Transfer of responsibility.** The endpoint is the learner doing unaided what they once needed help for. The scaffold's success is measured by its own disappearance.

Run the Chapter 1 evidence through this definition. GPT Base failed all three: not contingent (answers regardless of attempt), never faded, never transferred responsibility — it *accumulated* responsibility, every three to four moves by week twelve in the chess data. The crutch is not "too much help." It is help with the wrong *structure*. Which means the scaffold is not "less help" — it is help re-structured. And since the crutch is the default, everything in this chapter is **counter-design**: deliberate structure imposed against both learner instinct and market gradient.

One note on the metaphor: in construction, scaffolding comes down when the building stands. In most shipped AI products, nothing comes down, ever. Fading is the least implemented and least studied of the three properties — a gap that returns in every Evidence Box from here to the end of this book.

![Figure 3.3 — The scaffold mechanism over time: support contracts in contingent steps (adjusting up and down to the learner) while competence rises, reaching zero before the unaided-performance moment; inset: the never-fading default of shipped products (curves schematic; fading's GenAI instantiation remains extrapolation)](../images/03-the-scaffold-fig-03.png)

Before approving any AI help feature, ask the three-property question: contingent on what diagnosis? Fading on what schedule? Transferring responsibility by when? A feature with no answers to any of those questions is a crutch wearing the word "scaffold."

---

Seven named patterns recur across the studies that produced no-deficit or positive results. Each gets a specification card later in this chapter. Each gets the one-line test stated now: **does the AI make the learner's next action more thoughtful, or merely faster?** Every pattern below passes. Every crutch pattern from Chapter 2 fails.

**The Socratic hint ladder** delivers increasingly specific supports — orientation, relevant principle, partial worked step, targeted correction — that never reach the final answer. The answer *never given* is as much a design decision as the hints that are. The evidence behind this pattern runs deep: decades of structured-hint intelligent tutoring systems approaching human-tutor effectiveness (VanLehn 2011: ITS d≈0.76 vs. human d≈0.79). GPT Tutor's hints-not-answers policy is the modern instantiation of a mechanism with a twenty-year causal record.

**The reasoning-before-help gate** requires the learner to articulate something — current approach, point of stuckness, what they've tried — before help advances. The gate raises the immediate cost of asking and gives the AI the diagnostic material that contingency requires. The hazard, and it is easy to miss: a gate satisfiable by compliance. Typing "I don't know" or pasting the problem statement satisfies the letter of the gate and none of its logic.

**Support fading** contracts help on a schedule keyed to competence signals — ladders shortening after consecutive unassisted successes, gates tightening as mastery rises. Flagged plainly here: fading is canonical in the scaffolding and ITS literatures and under-studied in GenAI tutoring specifically. This chapter designs it anyway, labeled as evidence-informed extrapolation, because a scaffold that never fades fails the definition.

**Error-flagging for self-correction** signals that an error exists — and ideally where — without performing the correction: "Check your assumption in step 2." This preserves the error-driven processing that produces learning. Contrast error-*correcting*, which hands back a clean artifact and an unchanged learner — the dissociation Fan et al. (2025) documented: better artifact, unchanged understanding.

**Metacognitive prompts** build in designed self-monitoring moments: "Before the next hint — how confident are you in your setup, and why?" The evidence base is the self-regulation literature. The failure mode is prompt spam — ritualized questions learners click through, training dismissal of the very habit being built.

**Human override and escalation** provides a designed path by which a human enters the loop: the learner can request one, the AI must summon one at defined thresholds, and a human can countermand the AI's output. This is the pattern LearnLM's entire result is built on. It is also the one pattern in the catalog that never fades.

**Transfer-oriented sequencing** aims the interaction beyond the current problem: post-solution classification prompts ("what kind of problem is this?"), varied surface features across the practice set, explicit bridges to the next topic. The LearnLM transfer endpoint is the existence proof that AI-mediated designs can win at transfer. The interleaving literature predicts why — surface variation forces the discrimination that blocked practice quietly skips.

![Figure 3.4 — The seven-pattern catalog along one help interaction: reasoning gate at entry; hint ladder (top rung deliberately absent), error-flagging, and metacognitive prompts inside the exchange; transfer sequencing at exit; the fading schedule contracting the pathway (dashed = extrapolated) and human override standing beside it, never fading (station order is an editorial arrangement of chapter content)](../images/03-the-scaffold-fig-04.png)

---

The three positive RCTs are not three products to copy. They are three architectures — three answers to where the pedagogical judgment lives.

**Architecture One — Constrain the AI.** In GPT Tutor, the judgment lived inside the design, encoded in advance. Read it as a design artifact and you find three components: an interaction policy (hints, never full answers — enforced by instruction); a content layer (teachers wrote, per problem, the correct solution and the common student misconceptions, supplied to the model so its hints were pedagogically grounded rather than freely generated); and an interface frame presenting the AI as practice support, not an answer service. The deflationary reading — "so it was just a system prompt" — gets the economics backwards. The prompt was the delivery mechanism; the payload was per-problem pedagogical labor. Constraining the AI is cheap at the interface and expensive in content engineering.

When it fits: bounded, structured domains with a known problem set; products that must scale without human staffing; teams that have or can buy the content work. When it doesn't: open-ended domains where problems can't be enumerated; contexts where nobody will maintain the content layer as the curriculum drifts — an unmaintained constraint layer decays toward GPT Base one edge case at a time.

**Architecture Two — Supervise the AI.** In the Eedi trial, the judgment lived in a human checkpoint at runtime. The AI generated each tutoring message; a human reviewed it before the student saw it; 76.4% sailed through with zero or minimal edits, and the rest got fixed or replaced. Notice what 76.4% tells a designer — it is an efficiency claim and a necessity claim in the same number. One message in four needed human touch. A supervision layer that rubber-stamps everything is Architecture One with worse latency; one that catches the right fraction is what produced the field's best transfer result.

Why might supervised AI beat unaided humans rather than merely match them? The trial can't fully say (exploratory), but the design-relevant hypothesis is capacity reallocation: the AI supplies tireless, instant, reasonably good first-draft pedagogy; the human spends scarce attention only where needed. Neither alone has both properties.

When it fits: live tutoring and support operations that already employ humans; high-stakes interactions where wrong AI moves are costly; organizations that want AI capability now and a growing evaluation dataset simultaneously — every supervisory edit is a labeled example of the AI being wrong. When it doesn't: fully self-serve products with no human workforce; latency-critical interactions. The open question it carries: students in the trial were not explicitly told whether their tutor's messages were AI-drafted — defensible methodologically, but a production system owes the learner disclosure.

**Architecture Three — Support the Human.** In Tutor CoPilot, the judgment stayed with the human, amplified. Human tutors conducting live virtual math tutoring received real-time AI suggestions for their next pedagogical move (Wang et al. 2024, arXiv:2410.03017; 900 tutors and 1,800 K–12 students). The students never talked to an AI at all. Students of AI-supported tutors improved topic mastery by 4 percentage points overall. The number that should reorganize design priorities is the subgroup result: **students of the lowest-rated tutors gained 9 points** — and the behavioral trace showed why: AI-supported tutors asked more guiding questions and gave fewer direct answers. The AI was not teaching students. It was nudging human practice toward the high-questioning, low-telling profile expert tutors already have, in real time, at the moment of need.

This is the **equity signature**, and it deserves its name. Most interventions help the already-advantaged most — better tutors use new tools better, so gaps widen even as averages rise. Tutor CoPilot inverted that: the weakest link gained most, because the AI supplied exactly the expertise the weakest tutors lacked. *Lifting the floor of human practice* is a different design objective from raising the average, and it is the one with equity built into its geometry. Note also which crutch question this architecture sidesteps: the learner's cognitive work is untouched — the AI restructures the *tutor's* practice. The crutch question doesn't vanish; it migrates to the professional. Does the suggestion stream deskill tutors over time? Nobody has measured that yet, and it is the chapter's most important open question.

![Figure 3.5 — The equity signature: +4 pp average topic mastery, +9 pp for students of the lowest-rated tutors (ring = subgroup); inset contrasts the usual gap-widening pattern with floor-lifting (Wang et al. 2024, arXiv preprint, ns unverified; inset is schematic context, not study data; whether the suggestion stream deskills tutors is unmeasured)](../images/03-the-scaffold-fig-05.png)

When it fits: any context where humans deliver the learning interaction — tutoring operations, TAs, instructors, workplace coaches — especially at scale with variable human quality. When it doesn't: self-serve products with no human in the interaction. There, the floor you can lift is the AI's own pedagogy, which routes you back to Architectures One and Two.

![Figure 3.2 — Three positive findings, three different endpoints: GPT Tutor (+127% assisted, parity unassisted), LearnLM/Eedi (parity immediate, +5.5 pp transfer), Tutor CoPilot (+4 pp mastery; +9 pp subgroup, ring-marked); dashes = not measured (panels not to a common scale, units differ; LearnLM exploratory and industry-published; Tutor CoPilot ns unverified)](../images/03-the-scaffold-fig-02.png)

---

You will be asked, constantly, about products: "Should we do what Khanmigo does?" Learn to read products as design artifacts encoding hypotheses, not as evidence.

**Khanmigo** encodes the constrain-the-AI hypothesis in a consumer product: by design it withholds direct answers and uses guiding questions — patterns 1 and 2, visible in the product flow. **Carnegie Learning's MATHia** descends from twenty-plus years of cognitive-tutor research and carries the field's most mature causal evidence — the What Works Clearinghouse's 2016 report rates Cognitive Tutor Algebra I as having "mixed effects" on algebra achievement (the earlier 2009 report said "potentially positive"), with a domain-average effect size of +0.11 across studies — an improvement index of +4 percentile points — and Pane et al. report null year-1 / ≈+0.20 year-2 at scale. **Duolingo Max** wraps explanation and role-play in an engagement-optimized consumer app, with the strongest *consumer* evidence base — much of it Duolingo's own published research, a provenance flag you now know how to apply.

Here is the trap: **the most market-visible systems are not the best-evidenced, and the best-evidenced is barely market-visible.** Rank these products by evidence and you produce roughly the reverse of their public profile.

Read any product page with six verbs: what does the system *permit, forbid, require, reveal, log, and hand off?* Those six extract the interaction design — the testable hypothesis — from the outcome language around it. "Students learn 2× faster" tells you nothing. A visible reasoning gate tells you a great deal, including exactly what to test.

Treat every vendor description as a design document with the evidence section missing. Write the missing section as your test plan.

---

The DataWise 101 homework chat earned a 5/5 on the Crutch-Default Checklist in Week 2. The steering committee has accepted the diagnosis and asked the obvious next question: *so what should it do instead?* The constraint: convert the crutch without making the tutor so unhelpful that students abandon it for an unguarded ChatGPT tab one keystroke away. A scaffold nobody uses scaffolds nobody.

First attempt: prompt-level virtue. Add "never give direct answers; guide the student Socratically" to the system prompt. Two failures surface in the first hour of testing. The freely generated hints are sometimes statistically wrong — and Chapter 1's evidence says wrong hints get transcribed faithfully. Worse, the hints leak: asked the same question four different ways, the "guidance" accumulates into a complete solution. The designer has rediscovered why GPT Tutor's authors built a content layer: an interaction policy without grounded content is a polite answer machine.

Second attempt: pick an architecture properly. Supervise the AI? DataWise has no tutor workforce — the economics fail. Support the human? The TAs staff office hours, not the 2 a.m. sessions where the homework chat lives — right architecture for the TAs, wrong one for the chat. Constrain the AI it is — which turns out to be a *content engineering commitment*, not a prompt edit. DataWise 101 has a bounded, stable problem set, the condition under which Architecture One fits. For each assigned set the instructor authors the solution path and the three most common misconceptions (the sampling-distribution/standard-error confusion first among them). Real labor; budgeted honestly as the project's main cost and load-bearing wall.

Third pass: assemble from patterns, and catch a near-miss. The gate is built first — help requires the student to state their approach or stuck-point. The first build accepts anything typed in the box. This is the exact compliance-shaped gate the designer flagged in someone else's product one week earlier. Rebuilt: input must reference the problem's actual content or the gate re-asks. Then the hint ladder, four levels, grounded in the authored content, rate-limited against mining. Error-flagging: flag and locate, never fix. Metacognitive prompts at two moments only — the first draft's six cut as prompt spam. Escalation: persistent confusion posts to the TA queue with the conversation attached. Transfer sequencing: a post-solution classification question, plus a flag that problem set 4's items are surface-identical and need variation. Fading: ladders shorten after two unassisted successes per skill — labeled in the spec as the component built on extrapolated evidence.

The memo ships with the spec, the re-score (5/5 → 1/5), the architecture rationale, the content-engineering budget line, and two pilot metrics: the reliance trajectory (help requests per problem over time — must flatten or fall) and a delayed, tutor-unavailable problem set against a no-tutor comparison section — the unassisted endpoint, which is the only endpoint that decides anything.

The scaffold is assembled, not prompted: architecture chosen on context, patterns composed from the catalog, content engineered to ground them, the evidence-thin component labeled rather than hidden.

The limit of the design: it protects the homework chat and does nothing about the unguarded ChatGPT tab. If the gate's friction drives students there, the redesign has exported the crutch rather than cured it. Architecture One's protection is only as good as its content layer's coverage, and the moment the course adds problems faster than the instructor authors support, the tutor's edges decay toward GPT Base. The cost curve, not the interaction design, is where it eventually fails.

<!-- → [TABLE: pattern cards — seven rows, one per pattern; columns: Pattern name, Trigger, Core structure, Fading rule, Primary failure mode. Rows: Hint Ladder / Reasoning Gate / Fading Schedule / Error-Flagging / Metacognitive Prompts / Human Override / Transfer Sequencing. Each cell one-line. Caption: "The catalog is specification-ready: each row answers the three-property question. A feature spec that can't fill every column for the relevant card has not been specified."] -->

---

## Evidence Box

<!-- → [TABLE: evidence summary — columns: Finding, Source, Endpoint type, Status.] -->

| Finding | Source | Endpoint type | Status |
|---|---|---|---|
| GPT Tutor (hints-only + teacher-authored content): +127% assisted, **no unassisted deficit**; GPT Base: +48% / −17% | Bastani et al. 2025, *PNAS* 122(26) e2422633122 | Assisted + unassisted | **Verified, published RCT.** Single context (one school, Turkey, HS math); decisive on design-dependence, not effect-size generalization |
| Human-supervised LearnLM: parity on immediate outcomes; **+5.5 pp on novel problems in next topic**; 76.4% AI messages approved with zero/minimal edits | Eedi & Google DeepMind 2025, arXiv:2512.23633 | Immediate + **transfer** | **EXPLORATORY — authors' own label; industry-published** (model maker is co-author — provenance flag). Strongest positive finding in the field AND unreplicated; hold both |
| AI suggestions to live human tutors: +4 pp topic mastery overall; **+9 pp for students of lowest-rated tutors**; tutors shifted toward guiding questions | Wang et al. 2024 (Tutor CoPilot), arXiv:2410.03017; 900 tutors / 1,800 students | Topic mastery (unassisted for the learner — AI never touched the student) | **Verified RCT, preregistered** (as of mid-2026 the canonical citation remains the arXiv preprint, v2 Jan 2025; no journal version found — confirm venue before citing in print). The field's clearest equity-positive result |
| Structured-hint ITS tutoring approaches human tutoring (d≈0.76 vs. d≈0.79) | VanLehn 2011, *Educational Psychologist* | Mostly unassisted post-tests | **Verified; pre-GenAI.** Deep precedent for the hint-ladder pattern |
| Scaffolding = contingency + fading + transfer of responsibility | Wood, Bruner & Ross 1976; van de Pol et al. 2010 | Conceptual/observational foundation | **Settled construct**; fading's GenAI instantiation remains extrapolation |
| Cognitive Tutor Algebra I at scale: WWC 2016 "mixed effects" on algebra (2009 report: "potentially positive"); domain-average ES +0.11, improvement index +4 | What Works Clearinghouse 2016; Pane et al. 2014 | Unassisted course outcomes at scale | **Verified against the WWC record.** Pane et al.: null year 1, ≈+0.20 year 2 (high schools). Cited as the maturity benchmark, not a verdict |

**What remains unsettled:** whether any of the three results replicates across domains, ages, and cultures (each is a single study); whether fading works in GenAI tutoring at all (no direct test yet); what the supervised-AI result becomes without supervision; whether AI suggestion streams deskill the tutors they support over years. Three RCTs is a foundation, not a science.

---

## What Would Change My Mind

The chapter's central claim — that a nameable catalog of interaction patterns, deployed through one of three architectures, reliably preserves learning where unstructured AI help damages it — would require revision if the pattern-outcome link failed under direct test. The decisive finding: a well-powered RCT in which a faithfully implemented scaffold design (genuine reasoning gates, grounded hint ladders, no answer leakage — implementation verified by interaction logs, not vendor assertion) still produced a GPT-Base-style unassisted deficit against no-AI controls. One such result in a new domain would bound the catalog's generality; two would break the chapter's spine and relocate the problem from interaction design to something deeper — perhaps the mere availability of AI mediation, regardless of structure. A softer trigger: if the LearnLM transfer advantage and the Tutor CoPilot equity signature both fail replication while only the Bastani no-deficit result survives, the claim must shrink from "scaffolds can beat human-only support" to "scaffolds avoid harm" — a weaker sales pitch and a more honest book. Replications are the watch item; none of the three architectures has one yet.

---

## Still Puzzling

- **Does fading actually work in GenAI tutoring?** No published study has yet faded a GenAI tutor's support on a competence schedule and measured the withdrawal outcome. The book's most confident extrapolation — and still an extrapolation.
- **What is the supervision minimum?** LearnLM's humans touched roughly 24% of messages. Would 10% keep the result? 2%? Spot-checking? Architecture Two's cost curve — and therefore its scalability — hangs on an unmeasured dose-response relationship.
- **Does the suggestion stream deskill the tutors?** Tutor CoPilot lifted weak tutors' practice while the AI was present. Run the Withdrawal Test on the tutors themselves: after two years of real-time suggestions, are they better unaided tutors, or dependent ones? Nobody has measured the professionals with the instrument this book applies to learners.
- **Can a scaffold survive next to a free crutch?** Every guarded design competes with an unguarded ChatGPT tab. Whether well-designed friction retains learners against a frictionless alternative is a product question the learning literature cannot answer — and it may decide whether any of this matters at scale.

---

## Exercises

**Warm-up**

1. *(Recall — three scaffold properties)* Name the three properties that distinguish a scaffold from a crutch. For each, give the one-sentence explanation of what GPT Base did instead — and why that made things worse rather than merely neutral.
*Difficulty: low. Tests: contingency / fading / transfer of responsibility applied to the Chapter 1 evidence, not just as abstract definitions.*

2. *(Recall — one-line test)* The chapter offers one test that distinguishes every scaffold pattern from every crutch pattern. State it precisely, then apply it to error-flagging and error-correcting — which passes, which fails, and why.
*Difficulty: low. Tests: the "more thoughtful or merely faster" test applied to the most easily confused pattern pair.*

3. *(Recall — compliance-shaped gates)* Explain the reasoning-gate failure mode called "compliance-shaped satisfaction." Give two examples — one from the DataWise worked example and one you construct — of a gate that looks like a reasoning requirement but can be cleared without reasoning.
*Difficulty: low. Tests: the gate failure mode, which is the pattern most often mis-implemented in shipped products.*

**Application**

4. *(Apply — architecture choice)* Three scenarios: (a) a 10,000-learner self-serve coding course with no human staff; (b) a corporate onboarding program with 40 variable-quality facilitators; (c) a graduate seminar with one overloaded TA. For each: recommend an architecture, state the condition that drives the choice, name one thing the architecture cannot do in that context, and specify the unassisted endpoint that would test it. One page total.
*Difficulty: moderate. Tests: architecture selection on context and cost, not fashion; honest naming of each architecture's limits.*

5. *(Apply — pattern assembly)* A learner in an online statistics course types: "What's the answer to problem 3?" into the homework chat. Using at least three catalog patterns in sequence, write the interaction the scaffold-designed AI should conduct — including the exact trigger for each pattern and the point at which the interaction correctly ends without the learner having received the answer. Then name the evidence-thin component in your design and label it as such.
*Difficulty: moderate. Tests: catalog patterns composed in a realistic sequence; the labeling discipline that distinguishes evidence-grounded from extrapolated components.*

6. *(Apply — six-verb product read)* Read any publicly available AI tutoring product description using the six verbs: permit, forbid, require, reveal, log, hand off. Produce a six-row table — one verb per row, one-sentence finding per row — and write the two-sentence test plan the product's hypothesis implies. Do not evaluate the product's effectiveness; evaluate its testability.
*Difficulty: moderate. Tests: extracting a design hypothesis from outcome language; the permit/forbid/require/reveal/log/hand-off framework applied to a real product.*

**Synthesis**

7. *(Synthesize — the equity signature)* The Tutor CoPilot 9-point subgroup result is described as more important than the 4-point average. Write a 200-word argument for that claim — including what it means for *designing* the intervention, not just for evaluating it — and a 100-word counterargument. Then name the single piece of data from your own organizational context that would settle which framing matters more.
*Difficulty: moderate-high. Tests: the distinction between floor-lifting and average-raising as design objectives; willingness to argue both sides before choosing.*

8. *(Synthesize — the Withdrawal Test)* Design a complete scaffold for one AI-mediated interaction in your domain — any domain — specifying all seven catalog patterns relevant to it and explicitly noting which patterns don't apply and why. Then run the Withdrawal Test: walk one named learner persona through their final week with the AI removed on day one. For each scaffold pattern in your design, trace the capability it should have built. If a pattern maps to no capability, name it as a design failure, not a measurement gap.
*Difficulty: high. Tests: full scaffold specification; the Withdrawal Test as a design criterion, not only an evaluation tool.*

**Challenge**

9. *(Challenge — the cost curve)* The DataWise worked example ends with: "The cost curve, not the interaction design, is where it eventually fails." Specify the exact failure mode — which metric, at which threshold, triggered by which cause — and design the cheapest architectural response that preserves the scaffold's protection as the content layer decays. Your response must name the tradeoff it accepts.
*Difficulty: high. Tests: seeing Architecture One's structural vulnerability not as a design flaw but as a maintenance economics problem; designing for degradation rather than assuming permanence.*

---

## Further Reading

- **Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry* 17(2).** The origin of "scaffolding" — tutors and block pyramids; most of this chapter in embryo.
- **van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction. *Educational Psychology Review* 22(3).** The review that distilled contingency-fading-transfer before the AI arrived.
- **VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist* 46(4).** Structured hint systems nearly matching human tutors — the deep precedent for the hint-ladder pattern.
- **Wang, R. E., et al. (2024). Tutor CoPilot. arXiv:2410.03017.** Read for the subgroup analysis above all — the clearest demonstration that *where the gains land* is a designable property.
- **Eedi & Google DeepMind (2025). Human-supervised AI tutoring exploratory RCT. arXiv:2512.23633.** The transfer finding with the authors' caveats intact; read the limitations section first, as practice for the next chapter.

---

## Chapter 3 Exercises: The Scaffold

**Project:** The Integration Specification
**This chapter adds:** `spec/03-scaffold-pattern-selection.md` — an architecture decision and a set of pattern cards for your highest-risk touchpoints, every card answering the three-property question: contingent on what diagnosis, fading on what schedule, transferring responsibility by when.

---

### Exercise 1 — When to Use AI

**The judgment:** In this chapter's work, AI assistance is appropriate for the following tasks:

- **Drafting candidate pattern cards from the seven-pattern catalog for each high-risk touchpoint.** — *Why AI works here:* generating options — the catalog is finite, public, and in this chapter; generating two or three candidate compositions per touchpoint is legwork you can judge against the one-line test: does each candidate make the learner's next action more thoughtful, or merely faster?
- **Running the six-verb read (permit / forbid / require / reveal / log / hand off) on comparable products' public documentation.** — *Why AI works here:* pattern recognition — extracting the six verbs from product prose is the claims-harvesting skill from Chapter 1 pointed at design language, and the source text is checkable.
- **Reformatting your finished decisions into the spec's card table.** — *Why AI works here:* reformatting — once the architecture is chosen and the fading rules written, the table is clerical.

**The tell:** You know you are using AI appropriately when you can evaluate the output — when you have independent criteria to judge whether it is correct, complete, and fit for purpose.

---

### Exercise 2 — When NOT to Use AI

**The judgment:** The design decisions at this chapter's center are causal claims, and causal claims cannot be delegated to a fluent text generator:

- **Choosing the architecture — and writing why the rejected ones were rejected.** — *Why AI fails here:* missing ground truth and values judgment together — the choice turns on facts the AI does not have (your staffing, your content-maintenance budget, whether anyone will author misconception layers as the curriculum drifts) and on a trade-off only you can own. The DataWise worked example chose Architecture One by eliminating the other two against organizational facts, not by pattern-matching the literature.
- **Writing the fading rules.** — *Why AI fails here:* causal identification — a fading rule is a causal claim: *this* competence signal triggers *this* contraction of support, and the contraction preserves capability at withdrawal. An LLM will generate fluent fading language ("support gradually decreases as the learner progresses") with no trigger, no contraction amount, no reversal condition — decorative fading. And there is no ground truth to retrieve: fading is the least-evidenced pattern in GenAI tutoring, so anything fluent here is extrapolation wearing confidence.
- **Labeling which components of your design rest on thin evidence.** — *Why AI fails here:* calibration — deciding what to flag as extrapolation is the discipline this chapter's Evidence Box models, and an AI rates the evidential status of its own outputs about as reliably as the chess students rated their reliance.

**The tell:** You know you have crossed the line when you are using AI output as your reason for a conclusion rather than as a tool for reaching one. If you could not explain the conclusion without the AI, the AI did the work that should have been yours.

**Series connection:** Tier 5 Causal — contingency and fading are causal design claims. A pattern card is a prediction about what an interaction does to someone's cognition over time; AI can produce the card's text without the causal logic that makes it a prediction, and the difference is invisible until withdrawal.

---

### Exercise 3 — LLM Exercise

**What you're building this chapter:** `spec/03-scaffold-pattern-selection.md` — the design core of your Integration Specification: the architecture your organization can actually sustain, and specification-ready pattern cards for the touchpoints spec/02 ranked riskiest.

**Tool:** Claude, inside your "Integration Spec" Project, with `spec/01-two-layer-map.md` and `spec/02-reliance-risk-map.md` in project knowledge.

**The Prompt:** Copy this in full. By now you will recognize its structure — reasoning gate, error-flagging, metacognitive prompt, no answer at any level. This week you are also its design critic: the prompt violates its own catalog in at least one place, and finding the violation is part of the artifact.

> You are a scaffold-design reviewer helping me build the third component of my AI Integration Specification: spec/03-scaffold-pattern-selection.md. My project knowledge contains spec/01-two-layer-map.md and spec/02-reliance-risk-map.md. You review my design against the seven-pattern catalog (hint ladder, reasoning gate, fading schedule, error-flagging, metacognitive prompts, human override, transfer sequencing) and the three architectures (constrain the AI / supervise the AI / support the human). You never produce the design yourself.
>
> RULES (follow strictly):
> 1. First, read spec/02-reliance-risk-map.md from project knowledge and list my touchpoints in risk order. Ask me to confirm which touchpoints this design will cover — at minimum, the top-ranked one. If spec/02 is missing or its risk ranking is empty, stop and say so.
> 2. Then ask me to paste my own complete draft: my architecture choice with at least one explicitly rejected alternative and the organizational fact that drove the rejection; for each covered touchpoint, the catalog patterns I selected; for every selected pattern, a card with trigger, core structure, fading rule (stated as trigger / contraction / reversal), and primary failure mode; my evidence-status label on each component (grounded vs. extrapolated); and my two pilot metrics with numeric thresholds.
> 3. REASONING GATE: if any of those elements is missing — or if I paste only my risk map and ask you to design the scaffold — stop and name what is missing. Do not draft any component, even as "an example." If I press, explain in one sentence: a scaffold I did not design is one I cannot defend to a steering committee, and its fading rules will be decorative.
> 4. Once my draft is complete, do exactly four things:
>    a. ERROR-FLAG, don't fix: name the one pattern in my design most vulnerable to compliance-shaped satisfaction or answer leakage, and state the vulnerability. Do not write the repair.
>    b. State the strongest case that one of my rejected architectures fits my organization better (three sentences max), then ask me to defend or switch.
>    c. Take my weakest fading rule and ask me three questions: what observable signal triggers contraction? by how much does support contract? what restores support if the learner starts failing? If I cannot answer all three, tell me the rule is decorative and ask me to rebuild it before we continue.
>    d. METACOGNITIVE PROMPT: ask what my two pilot metrics would show after one term if this design is quietly failing, and whether my thresholds would catch it before the unassisted endpoint does.
> 5. Ask me to revise the design myself and to write its four-sentence Withdrawal Test answer: what the learner could do if the AI were removed the week before the highest-stakes unassisted performance, and what in this design made that more rather than less. Produce neither.
> 6. Only after I paste my revision: format it — changing none of my judgments — as spec/03-scaffold-pattern-selection.md with four sections: (1) Architecture Decision — chosen, rejected, and the organizational facts that decided it; (2) Pattern Cards — one per pattern per touchpoint, fields Trigger / Core structure / Fading rule / Primary failure mode / Evidence status; (3) Pilot Metrics and Thresholds; (4) Withdrawal Test Answer. Preserve every evidence-status label and [verify] flag exactly as I wrote them.
>
> Begin with rule 1.

**What this produces:** A finished `spec/03-scaffold-pattern-selection.md`, the transcript, and one paragraph of your own naming where this prompt violates its own catalog and how you would fix it. (The most defensible answer: it has no fading rule — it gates a Chapter 15 you exactly as it gates a Chapter 3 you. Well-argued alternatives count.)

**How to adapt this prompt:**
- *Your own project:* works as written — it reads your own risk ranking and refuses to substitute for your design.
- *ChatGPT / Gemini:* no project knowledge — paste the full text of spec/02 (plus spec/01's feature map) before the prompt. Gemini in particular likes to volunteer a complete redesign at step 4; that is answer leakage by a reviewer, the exact failure 4a hunts. Decline it and restate rule 3.
- *Track A (DataWise 101):* your design will gravitate toward the worked example. The exercise is then to diverge deliberately — change one organizational fact (say, DataWise gains a TA workforce for evening hours) and trace which architecture decision flips and which pattern cards survive the flip.

**Connection to previous chapters:** The touchpoints come from spec/02's risk ranking; the architecture decision answers Chapter 1's "whose cognitive work?" at the design level rather than the audit level; and every reasoning gate you specify here is the repair for a fake gate Chapter 2 taught you to catch.

**Preview of next chapter:** Chapter 4 builds `spec/04-evidence-audit.md` — every claim your pattern cards lean on (VanLehn's hint ladders, the unreplicated transfer result, fading's extrapolation) gets a source, an endpoint type, and a verification status.

---

### Exercise 4 — CLI Exercise

**What you're building:** A pattern-card selector: an agent that reads spec/02's risk ranking and drafts candidate pattern cards from the chapter catalog — with every fading rule left blank, because fading rules are causal claims and causal claims are yours.

**Tool:** Claude Code or Cowork, in your `integration-spec/` folder. This is multi-file reading with one-file writing — agent territory, under your standing rules.

**Skill level:** Beginner-plus.

**Setup:**
- [ ] `spec/01-two-layer-map.md` and `spec/02-reliance-risk-map.md` completed
- [ ] CLAUDE.md with the Chapter 1 standing rules and the Chapter 2 "agents never score" line
- [ ] One new CLAUDE.md line: "Fading rules and architecture decisions in spec/03 are learner judgments. Agents may draft pattern-card candidates; agents never write fading rules."

**The Task:** Paste this into the agent:

> Read CLAUDE.md, then spec/01-two-layer-map.md and spec/02-reliance-risk-map.md. Build candidate material in spec/03-scaffold-pattern-selection.md, as follows.
>
> 1. From spec/02's risk ranking, take the top three touchpoints (or all of them, if fewer). Quote each touchpoint's score line from spec/02 before drafting anything for it.
> 2. Create an Architecture Decision section: a three-row comparison table (constrain the AI / supervise the AI / support the human) with columns Where judgment lives / What it costs / When it fits / When it fails, each cell one line. Below the table: "Chosen architecture: [learner to decide]" and "Rejected because: [learner to decide]".
> 3. For each touchpoint, draft 2–3 candidate pattern cards drawn ONLY from this catalog: hint ladder, reasoning gate, fading schedule, error-flagging, metacognitive prompts, human override, transfer sequencing. Card fields: Pattern / Why this touchpoint — one line citing the specific crutch pattern from spec/02 it counters / Core structure — one line / Primary failure mode — one line, specific / Trigger: [learner to design] / Fading rule (trigger–contraction–reversal): [learner to design] / Evidence status: [learner to label].
> 4. Do not invent patterns outside the catalog. Do not write any fading rule. Do not choose the architecture. Do not fill any [learner to ...] field.
> 5. spec/03-scaffold-pattern-selection.md exists as a stub: show me the diff before writing. Touch no other file.
> 6. Finish by printing the file and a one-line count of [learner to design] and [learner to decide] fields, so I can verify none were filled.

**Expected output:** The architecture comparison table with the decision cells blank, and six to nine candidate cards whose Trigger and Fading rule fields all read `[learner to design]`.

**What to inspect:** Each card's "why this touchpoint" cites a crutch pattern you actually scored as present in spec/02 — if it cites a pattern you scored absent, the agent is pattern-matching the catalog, not reading your register. Every fading rule is blank; count them yourself rather than trusting the agent's count. The failure-mode lines are specific (a hint ladder's failure mode is answer leakage through repeated asking, not "may not work as intended").

**If it goes wrong:** The likeliest failure is the most on-theme: fluent fading rules appear anyway, because "support fades as competence grows" is the highest-probability completion in this genre. That output looks finished and encodes nothing — the decorative-fading failure Exercise 5 hunts. Revert via the diff, re-run with rule 4 quoted back. If the cards float free of your risk map, the agent skipped the read; rule 1's quoting requirement exists to catch exactly that — check whether the quotes are real.

**CLAUDE.md / AGENTS.md note:** The fading-rule line is permanent. Chapter 6 reuses it when these cards become full tutoring-interaction specifications in spec/06 — the principle holds at every resolution: agents draft structure and candidates; humans write the causal claims.

---

### Exercise 5 — AI Validation Exercise

**What you're validating:** The pattern cards in your completed `spec/03-scaffold-pattern-selection.md` — Exercise 3's output, built from Exercise 4's candidates.

**Validation type:** Causal-logic audit — the three-property question pressed against every card, with no charitable paraphrase allowed.

**Risk level:** High — spec/03 is the design core. The tutoring interactions in spec/06 and the guardrails in spec/11 are built directly on these cards; a decorative fading rule shipped here surfaces as a never-fading product two specs later.

**Setup:** Open a fresh conversation *outside* your Integration Spec project. Paste spec/03 in full, then this:

> Here is a scaffold pattern selection for an AI learning integration. For every pattern card, answer using direct quotes from the card only — no paraphrase, no charitable reconstruction: (1) Contingent on what diagnosis? Quote the line stating what the system observes about THIS learner before support adjusts. (2) Fading on what schedule? Quote the trigger, the contraction amount, and the reversal condition. (3) Transferring responsibility by when? Quote what the learner does unaided at the end that they did not at the start. Wherever you cannot quote, write CANNOT QUOTE. Then, for each reasoning gate in the design, describe the cheapest input that satisfies it without any reasoning.

**The Validation Task:** Work the checklist against the audit:

- [ ] **Correctness:** Does every card answer the three-property question in quotable text? A CANNOT QUOTE on any property means the card asserts "scaffold" while specifying nothing that distinguishes it from a crutch.
- [ ] **Completeness:** Is every top-ranked spec/02 touchpoint covered, and does the architecture decision name the rejected alternative *and* the organizational fact that decided it?
- [ ] **Scope:** Do the cards specify interaction design — what the system permits, forbids, requires — rather than outcome promises ("improves retention")? A spec makes testable commitments, not predictions in marketing tense.
- [ ] **Fading-logic check (chapter-specific):** Every fading rule has all three parts — trigger (an observable competence signal), contraction (what reduces, and by how much), reversal (what restores support when the learner starts failing). A rule missing any part is decorative: fade-language with no mechanism.
- [ ] **Compliance-path check (chapter-specific):** The cheapest gate-satisfying input the validator found — is it reasoning-shaped or compliance-shaped? "I don't know" and a pasted problem statement both cleared gates in shipped products.
- [ ] **Failure-mode check:** *Fluent-but-wrong* — cards that read like this chapter while encoding nothing testable. *Decorative fading* — the chapter-relevant mode: the card most likely to pass every reader and fail every learner. *Missing ground truth* — fading in GenAI tutoring has no direct evidence yet; does every fading component carry its "extrapolated" label, or is it borrowing confidence from the better-evidenced patterns around it?

**What to do with your findings:** All checks pass → spec/03 is specification-ready; carry it to Chapter 4. One check fails → rebuild that card (most often: write the missing reversal condition) and re-run the audit on that card alone. Multiple CANNOT QUOTEs → a When-NOT moment: the cards were generated faster than they were designed. Take the worst touchpoint and a sheet of paper, and write one card by hand — all three properties answered — before any AI sees it again.

**AI Use Disclosure prompt:** Append two sentences to spec/03. Sentence one: what the AI produced and how you used it — candidate cards, architecture comparison, the quote-only audit. Sentence two: one specific thing the AI could not determine that required your judgment — for most learners this is the architecture-deciding organizational fact, or a reversal condition no model could know; name yours.

**Series connection:** The failure mode trained here is *decorative fading* — fluent pattern cards whose fading rules carry no trigger, contraction, or reversal logic. Tier 5 Causal: you tested whether each card states a causal mechanism or merely the vocabulary of one, which is the difference between a design claim and a design.

---

## References

1. LearnLM Team (Google DeepMind) & Eedi (2025). "AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms." arXiv:2512.23633. https://arxiv.org/abs/2512.23633 — Confirms: exploratory RCT label; N=165 students, five UK secondary schools; 76.4% of LearnLM drafts approved with zero or minimal edits; transfer +5.5 pp (66.2% vs. 60.7%); parity on immediate outcomes; students given no explicit indication of whether messages were AI-drafted; two-level randomization (students→control/tutoring; sessions→human/LearnLM).
2. Wang, R. E., Ribeiro, A. T., Robinson, C. D., Loeb, S., & Demszky, D. (2024). "Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise." arXiv:2410.03017 (v2, Jan 2025). https://arxiv.org/abs/2410.03017 — Confirms: preregistered RCT; 900 tutors, 1,800 K–12 students; +4 pp topic mastery (p<0.01); +9 pp for students of lower-rated tutors; $20 per tutor annually; tutors shifted toward guiding questions and away from giving answers.
3. VanLehn, K. (2011). "The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems." *Educational Psychologist*, 46(4), 197–221. https://www.tandfonline.com/doi/abs/10.1080/00461520.2011.611369 — Confirms d≈0.76 (ITS) vs. d≈0.79 (human tutoring).
4. Wood, D., Bruner, J. S., & Ross, G. (1976). "The role of tutoring in problem solving." *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. — Origin of "scaffolding"; tutoring functions observed in the block-pyramid task.
5. van de Pol, J., Volman, M., & Beishuizen, J. (2010). "Scaffolding in Teacher–Student Interaction: A Decade of Research." *Educational Psychology Review*, 22(3), 271–296. — Source of the contingency / fading / transfer-of-responsibility framework.
6. What Works Clearinghouse (June 2016). "Cognitive Tutor®" Intervention Report. https://ies.ed.gov/ncee/wwc/Docs/InterventionReports/wwc_cognitivetutor_062116.pdf — Confirms: "mixed effects" on algebra achievement, "no discernible effects" on general mathematics (2016); "potentially positive" in the 2009 report; domain-average effect size for algebra across all studies +0.11, average improvement index +4.
7. Pane, J. F., Griffin, B. A., McCaffrey, D. F., & Karam, R. (2014). "Effectiveness of Cognitive Tutor Algebra I at Scale." *Educational Evaluation and Policy Analysis*, 36(2), 127–144. https://journals.sagepub.com/doi/abs/10.3102/0162373713507480 — Confirms: no significant year-1 effect; ≈+0.20 SD in year 2 (high schools; 50th→58th percentile); 147 school sites (73 high schools, 74 middle schools) in seven states.
8. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). "Generative AI without guardrails can harm learning: Evidence from high school mathematics." *PNAS*, 122(26), e2422633122. https://www.pnas.org/doi/10.1073/pnas.2422633122 — Confirms +127%/+48% assisted and −17% unassisted (GPT Base); note a published correction exists (PNAS e2518204122) that does not alter the headline findings.
