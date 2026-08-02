# Chapter 6 — Designing Tutoring Interactions: Hints, Reasoning Requirements, and Fading
*The +127% was a document. This chapter is where you write yours.*

Strip away the headlines from the Bastani RCT and what remains — the thing that actually produced the difference between "−17% unassisted" and "no deficit" — is not a model. Both conditions ran GPT-4. What differed is something a learning designer could have written, because teachers and researchers *did* write it: a system prompt and a conversation structure. Read that artifact the way Chapter 4 taught you to read a vendor page — as a design document — except this one comes with a randomized trial attached.

Here is what the GPT Tutor condition actually contained (Bastani et al. 2025). The research team worked with experienced teachers to write **bespoke prompts for each problem session — 57 of them** — not one generic "act as a tutor" instruction but problem-specific design documents. Each prompt carried the correct answer and full solution, the common mistakes students make on *that* problem, and instructions to coach rather than tell: give incremental hints, encourage the student to attempt the step themselves, do not reveal the final answer. Read that middle clause again, because it is the most instructive design move in the field's evidence base: **the answer was put into the prompt so that it could be withheld.** GPT Base failed students not because it lacked the answer but because it had no architecture governing when and how the answer flowed. GPT Tutor had the same answer and a design for its release. Same model. Same knowledge. Opposite unassisted outcomes.

Notice what else the document encodes. The common-mistakes lists are a misconception inventory — the artifact Chapter 5 revealed as the load-bearing content layer. The "incremental hints" instruction is a hint ladder compressed to one line; "attempt the step" is a primitive reasoning requirement. And what the document does *not* contain is equally instructive: no fading schedule, no escalation rule — the parts the field's best evidence hasn't reached yet, which this chapter will have you design anyway, extrapolation labeled.

The +127%/no-deficit row was not produced by a better model, a bigger budget, or a breakthrough. It was produced by roughly the artifact you will write this week. That should feel less like pressure than like jurisdiction: this layer is yours.

![Figure 6.1 — Same model, two architectures (Bastani et al. 2025; 57 bespoke teacher-written prompts): both halves stand on one shared model base. GPT Base's generic instruction delivers the answer unimpeded; GPT Tutor stacks three prompt layers — the answer held under do-not-reveal (key with bar: present so it can be withheld), the per-problem misconception inventory, the incremental-hint and attempt-first instruction — and releases hints through a gate, the answer conspicuously absent.](../images/06-designing-tutoring-interactions-fig-01.png)

---

A **hint ladder** is a sequence of increasingly specific supports for a problem-solving step, capped so that the final answer is never given. A canonical ladder runs four levels: **orientation** (reframe what the problem is asking), **principle** (name the relevant concept or rule), **partial step** (apply the principle to part of the problem's specifics), **targeted correction** (respond to the learner's specific error). The shape matters less than the discipline it encodes: at every level, the question is not "what would help?" but "what is the *least* help that keeps the learner working?"

Why believe restraint works? The deep evidence comes from the pre-LLM intelligent tutoring systems literature — systems built around stepwise hints and immediate feedback. VanLehn's (2011) review found step-based ITS produced learning gains of *d* ≈ 0.76, essentially matching human tutors at *d* ≈ 0.79. By Kraft's benchmarks those are very large education effects, accumulated across decades — the strongest sustained evidence in this book that *structured help during practice* genuinely teaches. The LLM-era anchor is GPT Tutor: teacher-written incremental hints, a hint ladder in a system prompt, whose unassisted outcome is the causal evidence that ladder-versus-answers is the difference that matters.

Two specifications distinguish a real ladder from a chatbot that happens to hint. First, **the withheld answer is part of the spec** — written down, given to the model, marked do-not-reveal; what the tutor must never say is as designed as what it says. Second, **levels are problem-specific, not generic.** "Think about what the question is really asking" is filler at any level; the GPT Tutor prompts worked because teachers wrote the principle and partial-step content for each problem, anchored in its actual common mistakes. The misconception to retire — the one this chapter's notes predict you will bring — is that ladder quality is a *tool capability* issue, something the next model release fixes. The model was never the problem; GPT-4 could hint beautifully on request. It is an interaction design issue: what the system permits, requires, and withholds. Which is to say, it is your job.

A hint ladder controls what the tutor says. A **reasoning gate** controls what the learner must do to make the tutor say it: before help advances, the learner must externalize something — a prediction, an explanation, an attempted step, a located confusion — that the system can inspect and respond to.

The evidence rationale is the **self-explanation effect**, one of the most robust findings in learning science: learners who generate explanations of worked steps learn more than learners who merely receive them, and prompting for self-explanation reliably improves understanding and transfer (Chi et al. 1994). The gate also operationalizes the behavioral finding from the other direction: GPT Base's error-propagation evidence showed students taking answers without processing them, with the model's arithmetic mistakes appearing verbatim in student work. A gate is the structural countermeasure.

The design problem is that weak gates train compliance, not reasoning. "Explain your thinking first" is a weak gate: it accepts a paste of the problem statement, a vague "I tried the formula," or text from the learner's *other* AI window. Strong gates have three properties: **content-specific** (the gate for a sampling-distribution problem asks *which distribution matters here and why* — a question whose answer exposes the live misconception); **inspectable** (the tutor checks the response against the misconception inventory and responds to what it finds); and **cheap for genuine effort, expensive for evasion** — an honestly stuck learner satisfies the gate in one sentence, while an answer-farmer must produce reasoning the system will actually engage.

A useful test: draft the laziest response that would technically satisfy your gate. If it required no contact with the problem's content, the gate is decorative.

One honest boundary: gates add friction, and friction is not free. Liljedahl's thinking-classroom research (2021) is the right companion — the goal is *productive* struggle, not maximal struggle. A gate that interrogates a learner who has already demonstrated the reasoning is theater, and the expertise reversal effect predicts it becomes harmful. Gates should be heaviest exactly where the misconceptions live, and they should fade.

![Figure 6.2 — The hint ladder is a gated ladder, one pattern, not two: four rungs of increasing specificity (orientation, principle, partial step, targeted correction), reasoning gates that open only when inspectable learner input docks, attempt loops back to the problem at every rung, a delay before the deepest level, and a do-not-reveal floor beneath it — the answer present under the floor, never released.](../images/06-designing-tutoring-interactions-fig-02.png)

---

Here the chapter holds itself to three-bucket standards, because the evidence structure changes underneath us.

The concept of fading is older than every system in this book. Wood, Bruner and Ross (1976) — the paper that coined "scaffolding" — defined effective tutoring as **contingent**: support calibrated to current need, *increasing when the learner struggles and receding as competence grows*. Scaffolding that never comes down is not scaffolding; it is architecture the learner now depends on. The pre-LLM experimental literature gives the principle footing: Renkl, Atkinson and colleagues showed that **adaptively fading worked-example steps** — transitioning learners from studying examples to solving problems as competence builds — improved learning and transfer over fixed support (Atkinson, Renkl & Merrill 2003; Renkl & Atkinson 2003). And the cognitive-load literature supplies the sharpest reason fading is not optional: the **expertise reversal effect** — support that helps novices becomes *ineffective or harmful* for more knowledgeable learners, whose processing it redundantly interrupts (Kalyuga et al. 2003). Support is not a constant good. It has a sign that flips with competence.

Now the honest flag: **there is no direct RCT evidence on fading in generative-AI tutoring. None.** No trial has randomized learners to a fading versus non-fading LLM tutor and measured unassisted outcomes. The schedules this chapter teaches are *evidence-informed extrapolation* — from scaffolding theory, the worked-example experiments, expertise reversal, and the ITS tradition — not settled GenAI canon. Every specific fading schedule is a pilot-with-measurement object. Your fading triggers are hypotheses, and your evaluation plan is where they get tested.

A fading schedule specifies three things. **The signal:** what observable indicates competence — most practically, consecutive successes without deep hints; more formally, a mastery estimate from Bayesian Knowledge Tracing, a model that updates the probability a learner has a skill from their response history. **The contraction:** what is withdrawn at each threshold — the tutor stops offering and starts waiting, ladder levels compress, hints give way to error-flagging only. **The reversal rule:** what brings support back — contingency's other half and the most commonly forgotten. Wood, Bruner and Ross's tutors *increased* support on struggle. A fading schedule without a re-entry rule is not graduated withdrawal; it is abandonment on a timer.

![Figure 6.3 — Fading with a reversal rule: the support band contracts at signal-triggered thresholds (dashed because they are competence signals, not calendar dates) and steps back up when the learner's trajectory dips — contraction is not abandonment. No direct RCT evidence on fading in generative-AI tutoring exists; this schedule is evidence-informed extrapolation from contingency theory (Wood, Bruner & Ross 1976), faded worked examples (Renkl & Atkinson 2003), and expertise reversal (Kalyuga et al. 2003).](../images/06-designing-tutoring-interactions-fig-03.png)

---

Build a ladder and a gate, and some learners will treat them as a lock to pick. The ITS literature documented **gaming the system** before LLMs existed — exploiting help features to obtain answers without engaging the material — including the canonical move, **bottom-out hint abuse**: rapidly clicking through hint levels to the most specific hint and harvesting it as the answer (Baker et al. 2004). Gaming was common, measurable in logs as hint-request bursts faster than reading speed, and associated with substantially worse learning. The help-seeking literature adds the diagnosis: help use is systematically miscalibrated — avoidance and abuse both flourish — and *help design*, not learner exhortation, is the available lever (Aleven et al. 2003).

You do not design for the learner you wish you had. Counter-patterns, all log-visible and specifiable: **gate every level** (each advance requires inspectable content — which is why ladder and gate are one pattern, not two independent features); **slow the bottom** (a short delay or attempt requirement before deep hints removes the speed advantage of spamming); **blunt the bottom** (the deepest level is a targeted correction or a worked *analogous* step — never the literal answer, which makes harvesting pointless); **watch the logs** (hint-burst patterns and gate-response quality are reliance-trajectory data — the evaluation plan will ask for exactly these).

One more honesty clause: a determined learner with a second AI window can outsource your gate. Within-system design cannot stop cross-system evasion; that boundary belongs to assessment design and the transparency layer. Your spec should make gaming harder and *visible*, not pretend to make it impossible.

![Figure 6.4 — Breaking the bottom-out loop (Baker et al. 2004; Aleven et al. 2003): gaming runs as a cycle — help request, hint burst, bottom-out harvest, no learning, repeat — and each counter-pattern interrupts a specific arc: the gate blocks ungated advancement, the delay slows the descent to deep hints, the blunted bottom replaces the literal answer with an analogous step, and the log observer touches the loop without blocking it. One arc — cross-system evasion — is deliberately left uncountered; within-system design cannot reach it.](../images/06-designing-tutoring-interactions-fig-04.png)

---

Every pattern so far governs how the tutor helps. The last section of the spec governs when it stops — and stopping is a design decision, not a failure state. An escalation rule names the conditions under which the AI hands off to a human, and what the handoff looks like from the learner's side.

The architecture evidence from Chapter 3 is re-readable as escalation designs. LearnLM/Eedi put a human *above* the AI, supervising messages, and produced the field's best transfer finding. Tutor CoPilot put AI support behind the human tutor, with the strongest gains for the lowest-rated tutors. Both assume what an unescalated chatbot denies: some tutoring moments belong to people. A tutor that keeps cheerfully hinting at a learner who has signaled confusion three times is not persistent; it is converting a design gap into learner frustration, and teaching them that asking for help leads nowhere human.

A tutoring spec needs escalation triggers in four families. **Repeated failure:** the same misconception recurring after the deepest level — the AI's pedagogy has run out; flag to the instructor with the interaction summary attached, and tell the learner it's been flagged. **Affective distress:** frustration language, "I give up," self-deprecation — route warmly to a human, never to another hint. **Boundary conditions:** questions outside the misconception inventory, graded assessment content, privacy-sensitive disclosures — decline and route. **Learner request:** a single-click path to a human, always visible, always one action away. For each trigger, specify the *experience* of escalation: what the learner is told, what the human receives, how long the learner waits in ambiguity. An escalation nobody discovers, or one that dumps the learner into a context-free help-desk queue, satisfies the spec's letter and fails its purpose — escalation protects learning *and* dignity.

![Figure 6.5 — Escalation as a designed handoff: four trigger families — repeated failure, affective distress (urgent: never to another hint), boundary conditions, and the always-available learner request — converge on a router that hands off to one human, with the interaction summary traveling along the handoff and a return arc closing the learner-side experience: told, acknowledged, wait bounded.](../images/06-designing-tutoring-interactions-fig-05.png)

---

The DataWise 101 homework-help tutor needs its interaction spec. The anchor problem: *Commute times in a metro area have mean 26 minutes and standard deviation 8. For random samples of 64 commuters, what is the probability the sample mean exceeds 28 minutes?* The misconception inventory has already surfaced the two errors behind most wrong answers: using σ = 8 instead of the standard error σ/√n = 1, and not recognizing that the question concerns the sampling distribution of the mean at all.

An unguardrailed chatbot answers this in four seconds — z = 2, P ≈ 0.023, fully worked. That is the GPT Base pattern. The spec must release help in a shape that keeps the statistical reasoning — *which distribution, why √n* — in the student's hands at 11 p.m., unsupervised.

The first draft ladder has five levels and no gates. Pilot logs show exactly what Baker et al. predicted: a third of help sequences are hint-bursts, bottoming out at level five, which the draft had written as "so the probability is the area beyond z = 2…" A vending machine with extra steps. Fix: the deepest level becomes a targeted correction keyed to the inventory, and the final probability joins the do-not-reveal list. The second dead end is the gate. Draft wording — "explain your thinking so far" — fails the laziest-response test: students paste the problem statement back, and the model waves them through. The shipped gate is content-specific: *"Before I help — is this question about individual commuters, or about the average of a sample of 64? Tell me which, and what you've tried."* Inspectable against the inventory; one honest sentence passes it. The third dead end is the fading plan: the first draft contracts support after week 8 for everyone. That is a calendar, not a competence signal, with no reversal rule. Wood, Bruner and Ross's tutors gave *more* help on struggle; the schedule has to run both ways.

The resolved spec, one page: the hint ladder runs four levels per problem, drawn from the inventory. L1 orientation: *"What is the problem asking about — one commuter's time, or the mean of 64?"* L2 principle: *"The CLT says sample means have their own distribution. What happens to its spread as n grows?"* L3 partial step: *"Standard error = σ/√n = 8/√64. Compute that, then build your z."* L4 targeted correction, keyed to the learner's actual move — if they used 8 as the spread: *"That's the SD of individuals; sample means vary less. By how much?"* Never given: the final probability, or any completed solution path. The reasoning gate requires the learner to name which distribution is in play before L2 unlocks, and to show an attempted z-calculation before L3 — responses checked against the two inventory errors, the tutor's next move keyed to which appears. An anti-paste probe: *"What would change if n were 4 instead of 64?"*

The fading schedule runs three tiers. Tier 0 (default): proactive offer, full ladder. Tier 1 (two consecutive problems solved with nothing past L1): tutor waits, ladder compresses to L1 and L4 only. Tier 2 (BKT mastery ≥ 0.95): error-flagging only — the tutor marks *that* something is wrong, not what. Reversal: two consecutive failures, or a recurring inventory error, drops one tier. Learner-visible: the tutor states tier changes plainly — *"You've been solving these without much help, so I'll hang back — ask if you want me."* Escalation: same misconception after L4 twice in a unit sends an instructor dashboard flag with transcript summary and tells the learner a human will see it; distress language routes warmly — *"This one's been a grind. Want me to flag it for Professor R., or book office hours? A person is the right next step."* Anything touching exam content is declined and routed. A persistent "talk to a human" button, one click, always.

<!-- → [TABLE: tutoring spec one-pager — five sections as rows: (1) Hint Ladder: four levels, withheld-answer list, problem-specific content sources; (2) Reasoning Gate: content-specific trigger, what it checks against, anti-paste probe; (3) Fading Schedule: three tiers with entry signals, contents, learner-visible description; (4) Reversal Rule: trigger for one-tier re-expansion; (5) Escalation: four trigger families with learner-side experience per trigger. Caption: "The spec's value lives in what it withholds and when it lets go. Every row answers one of the three scaffold-property questions from Chapter 3."] -->

The lesson: the spec's value lives in what it withholds and when it lets go — the answer is designed *into* the system precisely so it can be designed *out* of the conversation.

The limit: this pattern set fits well-structured problems with inspectable steps. Point it at an open-ended task — *"critique this published study's sampling design"* — and the ladder has no rungs: no single withheld answer, and the inventory becomes a judgment rubric. And the fading schedule, the spec's most original section, is its least evidenced: zero direct RCTs — which is why the team's pilot plan logs tier transitions and puts an unassisted endpoint on the next proctored exam.

---

## Evidence Box

<!-- → [TABLE: evidence summary — columns: Study/source, What it found, Endpoint type(s), Verification status.] -->

| Study / source | What it found | Endpoint type(s) | Verification status |
|---|---|---|---|
| Bastani et al. (2025), *PNAS* 122(26) | GPT Tutor — 57 bespoke teacher-written, problem-specific prompts — eliminated the −17% unassisted deficit | Assisted + unassisted | Verified; the design document behind the book's spine result |
| VanLehn (2011) | Step-based ITS *d* ≈ 0.76; human tutoring ≈ 0.79; two-sigma retired | Meta-analytic, largely unassisted post-tests | Verified (figures confirmed against the published abstract) |
| Chi et al. (1994) | Eliciting self-explanations improves understanding and transfer | Unassisted post-test | Verified (classic; repeatedly replicated) |
| Wood, Bruner & Ross (1976) | Scaffolding defined; contingency — support rises with struggle, recedes with competence | Observational/theoretical | Verified (foundational; not an RCT) |
| Atkinson, Renkl & Merrill (2003); Renkl & Atkinson (2003) | Fading worked-example steps improves learning and transfer over fixed support | Unassisted + transfer | Verified; pre-LLM — extrapolation to GenAI is inference |
| Kalyuga et al. (2003) | Expertise reversal: novice-helping support becomes ineffective or harmful for advanced learners | Unassisted, across expertise levels | Verified |
| Baker et al. (2004) | Gaming the system in ITS — including bottom-out hint abuse — common, log-detectable, linked to worse learning | Behavioral logs + unassisted outcomes | Verified |
| Aleven et al. (2003) | Help-seeking is systematically miscalibrated; help design is the lever | Review | Verified |
| LearnLM/Eedi RCT | Human-supervised AI tutoring: +5.5 pp transfer | Transfer | **EXPLORATORY — authors' own label; industry-published** |
| Wang et al. (2024), Tutor CoPilot | AI support for human tutors: gains concentrated among lowest-rated tutors | Student mastery | Verified (confirm final publication venue before citing in print) |
| Fading in GenAI tutors | — | — | **Zero direct RCT evidence.** All schedules here are evidence-informed extrapolation, labeled as such |

---

## What Would Change My Mind

The chapter's load-bearing extrapolation is that fading — designed withdrawal on competence signals — preserves or improves unassisted outcomes in GenAI tutoring, as it did for worked examples and as contingency theory predicts. A randomized trial comparing fixed-support against signal-faded support in a guardrailed LLM tutor, with unassisted and retention endpoints, could overturn this directly: if faded support produced *worse* unassisted performance — perhaps because visible withdrawal demotivates at scale — the fading schedule would need rewriting from "default pattern, label the schedule" to "pilot-only pattern, label the premise." A second finding with the same force: evidence that strong reasoning gates drive learners to ungated external chatbots at rates that erase the within-system gains — that would relocate the chapter's center of gravity from interaction design toward the assessment and ecosystem layers. Either trial is runnable today; neither has been run.

---

## Still Puzzling

- **What is the right fading signal for conversation?** ITS fading keyed on stepwise correctness; an LLM tutor sees messy dialogue. Is gate-response *quality* a better mastery signal than correctness — and can a model assess it reliably enough to hang support decisions on?
- **Does visible fading change its effect?** Does telling learners when support contracts protect trust, or does announcing withdrawal trigger strategic helplessness the silent version wouldn't?
- **Where do gates cross from scaffold into toll?** Some friction is the point; too much sends learners to the ungated window one tab over. The optimum is learner- and stakes-dependent, and nobody has mapped it.
- **Can escalation scale?** Every trigger designed here assumes a human on the receiving end. At 4,000 learners, who reads the dashboard flags — and does an escalation no one answers do more relational damage than none?

---

## Exercises

**Warm-up**

1. *(Recall — the do-not-reveal list)* Explain why the correct answer and full solution were included in GPT Tutor's system prompt if the spec explicitly forbade giving them to the student. What design function does placing the forbidden content inside the prompt serve — and what would be lost if the prompt simply omitted the answer entirely?
*Difficulty: low. Tests: the central design move of the chapter; not just what the spec did but why the architecture requires the answer to be present in order to be withheld.*

2. *(Recall — laziest response test)* A reasoning gate reads: "Before I help, please describe what you've tried." Apply the laziest-response test: write the two evasions a motivated answer-farmer would use to clear this gate, and then write the one revision that closes both evasions. Name the property of the revised gate that makes it inspectable.
*Difficulty: low. Tests: the decorative-gate failure mode applied to a specific example; the three strong-gate properties.*

3. *(Recall — reversal rule)* A colleague's fading schedule contracts support after three consecutive successes and never expands it again. Identify the missing component by name, cite the 1976 source that defines it as part of the scaffolding concept, and describe the specific learner experience that the omission produces at week eight of a course.
*Difficulty: low. Tests: the reversal rule as the most commonly forgotten fading component; Wood, Bruner & Ross's contingency definition.*

**Application**

4. *(Apply — ladder construction)* Choose any structured problem from your own domain — not statistics, and not a problem from this chapter. Write a four-level hint ladder for it: orientation, principle, partial step, targeted correction. Include the do-not-reveal list. Then apply the laziest-response test to your L3: if a learner could use L3's partial step to reverse-engineer the answer without engaging the principle, rewrite L3 and explain the change.
*Difficulty: moderate. Tests: ladder construction in an unfamiliar domain; the do-not-reveal discipline applied to a novel problem; the ladder's bottom as an active design decision.*

5. *(Apply — fading schedule)* Specify a fading schedule for a tutoring interaction in any domain: name the three support tiers and their contents, the competence signal that triggers each contraction, and the struggle signal that triggers each re-expansion. Then identify which of your specified signals your system can *actually observe* in a log and which it cannot — and for each unobservable signal, name the cheapest proxy you would use instead.
*Difficulty: moderate. Tests: fading schedule completeness (signal + contraction + reversal); the practical gap between theoretically correct signals and log-observable ones.*

6. *(Apply — escalation specification)* A learner has reached the deepest hint level on the same problem three times, answered "I give up, I'm terrible at this," and asked the AI to "just tell me so I can move on." Write the AI's next three responses — one per message — using only patterns from this chapter's catalog. Then write the escalation trigger this conversation has crossed and the learner-side experience of the handoff.
*Difficulty: moderate. Tests: pattern sequencing under distress (hint ladder, error-flagging, escalation); the learner-side escalation experience as a design requirement, not an afterthought.*

**Synthesis**

7. *(Synthesize — spec critique)* A tutoring spec contains the following: "The AI provides up to five hints of increasing specificity. Before each hint, the student must type an explanation of their thinking. After the fifth hint, the full solution is shown. Support is reduced after week 8 for all students." Identify every design error against the chapter's four main sections — ladder, gate, fading, escalation — and rewrite the spec's four most critical lines. For each rewrite, cite the evidence or principle that drives the change.
*Difficulty: moderate-high. Tests: integrated application of all four spec components; the four errors from the mid-chapter checkpoint extended to require evidence-linked rewrites.*

8. *(Synthesize — extrapolation audit)* The chapter makes one explicit extrapolation: fading schedules work in GenAI tutoring even though no direct RCT evidence exists. Reconstruct the inferential chain — the three evidence sources the extrapolation draws on — and then name the single experimental design that would resolve the extrapolation into either direct evidence or a falsified hypothesis. What is the minimum sample size and endpoint type you would require before treating the result as a *decide* rather than *explore* finding?
*Difficulty: high. Tests: the chapter's evidence-honesty discipline applied to its own weakest claim; three-bucket classification of an extrapolation; research-design thinking.*

**Challenge**

9. *(Challenge — the ungated window problem)* The chapter acknowledges that a determined learner with a second AI window can bypass any within-system gate. Design the cheapest intervention that makes cross-system evasion *visible* without surveilling learners — specifying what log signal would indicate that evasion is occurring, what threshold would trigger a response, and what the response is. Then argue, in 150 words, why visibility is a better design goal than prevention in this case.
*Difficulty: high. Tests: the boundary between interaction design and assessment design; honest reasoning about what within-system design can and cannot accomplish.*

---

## Further Reading

- **Bastani, H., et al. (2025). "Generative AI without guardrails can harm learning." *PNAS* 122(26) — supplementary materials.** Read the actual GPT Tutor prompt design, not the results: the field's only RCT-validated tutoring spec, and shorter than your design lab submission.
- **VanLehn, K. (2011). "The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems." *Educational Psychologist* 46(4).** The decades of step-based evidence your ladder stands on; the permanent antidote to two-sigma claims.
- **Wood, D., Bruner, J., & Ross, G. (1976). "The role of tutoring in problem solving." *Journal of Child Psychology and Psychiatry* 17(2).** The original scaffolding paper; contingency in its first and clearest formulation.
- **Aleven, V., et al. (2003). "Help seeking and help design in interactive learning environments." *Review of Educational Research* 73(3).** Why help use is miscalibrated and design, not exhortation, is the lever — the ancestor of this chapter's gates.
- **Liljedahl, P. (2021). *Building Thinking Classrooms in Mathematics*.** The productive-struggle counterweight: a tutoring spec exists to keep learners thinking, and Liljedahl is the field guide to thinking conditions.

---

## Chapter 6 Exercises: Designing Tutoring Interactions

**Project:** The Integration Specification
**This chapter adds:** `spec/06-tutoring-interaction-spec.md` — your integration's interaction layer, the artifact in the Bastani lineage: a four-level hint ladder per anchor problem with its do-not-reveal list, content-specific reasoning gates that pass the laziest-response test, a fading schedule (signal, contraction, reversal rule — labeled as the extrapolation it is), gaming counter-patterns, and escalation triggers with the learner-side experience specified per trigger. Track A: extend the DataWise commute-time spec to two further anchor problems from the sampling-distributions unit. Own project: your task, your misconception inventory.

This is the week you write the document class that produced +127% with no unassisted deficit — and the first build job your own `spec/05` policy governs. Hint drafting sits in "AI assists, human reviews," with the review criterion already named; ladder sequencing, fading thresholds, and escalation boundaries sit where your never-touch column put them. The exercises below follow your table exactly, which is the point of having written it.

### Exercise 1 — When to Use AI

**Task 1 — Draft hint-text variants inside your ladder design.** You write the architecture — levels, content source, do-not-reveal list — then have the model draft two or three phrasings per rung. *Why AI works here:* constrained drafting against a spec you authored. Your `spec/05` already files this row under "AI assists, human reviews," criterion named: every variant checked against the misconception inventory, not for fluency — fluency the model already has; alignment is what it fakes.

**Task 2 — Generate the laziest responses for your gates.** For each reasoning gate, have the model produce the evasions a motivated answer-farmer would try: the pasted problem statement, the vague "I tried the formula," the paragraph lifted from the learner's other AI window. *Why AI works here:* adversarial test-case generation. The chapter hands you the pass/fail rule — if an evasion requiring no contact with the problem's content clears the gate, the gate is decorative — so every generated evasion is instantly judgeable against your own gate text.

**Task 3 — Enumerate log-observable proxies for your fading signals.** Paste your tier signals — "BKT mastery ≥ 0.95," "two consecutive problems with nothing past L1" — and ask which your platform can actually observe in a log, and what the cheapest proxy is for each one it cannot. *Why AI works here:* technical enumeration. The output is a list of checkable claims about logging capabilities, verified against your platform's documentation — and every proxy gets validated by the pilot, not by the model's say-so.

**The tell:** You know you are using AI appropriately when you can evaluate the output — when you have independent criteria to judge whether it is correct, complete, and fit for purpose.

### Exercise 2 — When NOT to Use AI

**Task 1 — Do not ask the model to "write me a hint ladder for problem X."** *Why AI fails here:* answer-delivery in disguise. Ungoverned, the model's helpfulness training produces a fluent ladder whose rungs leak monotonically — by L3 the partial step has done the computation, by L4 the targeted correction is a worked solution — GPT Base output wearing GPT Tutor's level labels. And the rungs come out generic, "think about what the question is really asking" filler, because the model has never met your inventory's two actual errors. The Bastani prompts worked because teachers wrote fifty-seven of them, problem by problem. The model was never the design layer; it was what the design layer governed.

**Task 2 — Do not delegate the fading schedule's thresholds and reversal rules.** *Why AI fails here:* a causal claim without a causal warrant. Every threshold asserts *after this signal, this learner no longer needs this support* — a claim about competence growth in a domain with zero direct RCT evidence, the chapter's own most heavily flagged extrapolation. The model will produce confident numbers anyway; that is what fluency does to an empty evidence column. What the numbers should actually turn on, only you hold: what an error costs *this* learner at *these* stakes, what your pilot can detect, and who answers when fading turns out to be abandonment.

**Task 3 — Do not let the model set the escalation triggers.** *Why AI fails here:* the boundary itself. Escalation decides which tutoring moments belong to people, and handing that decision to the system being bounded gets you triggers optimized for the system's continuation — one more hint, one more rephrase. The affective-distress threshold and the handoff experience are dignity design: "i give up, im just stupid" is a moment you have to have imagined a specific human into before you can specify what happens next. The model has read about that moment. You have had it.

**The tell:** When the task is done, close the chat and explain the conclusion — and the evidence behind it — out loud, to a colleague or to the wall. If the explanation is yours, the AI was an instrument. If you could not explain the conclusion without the AI, the AI did the work that should have been yours.

**Series connection:** Tier 5 Causal — a fading schedule is a causal claim about competence growth, made under acknowledged evidence absence. Only the human designer knows the learner's stakes well enough to own that bet, label it extrapolation, and stand accountable when the pilot's unassisted endpoint comes back. The model can word the schedule; it cannot warrant it.

### Exercise 3 — LLM Exercise: Build spec/06-tutoring-interaction-spec.md

This exercise absorbs the chapter's standalone Ladder Stress-Tester — its three personas, leak report, and verdict-last rule are the engine here — and adds the extrapolation check and the assembly step that turns the session into a spec file.

**Tool:** Claude Project "Integration Spec," with `spec/01`–`05` in Project knowledge.

**Before you start:** write the draft spec yourself — ladder, gates, fading schedule, escalation triggers. Exercise 2 just told you why the judgment layers cannot be generated; Exercise 1's Task 1 tells you which drafting help your own policy permits. The prompt refuses to invent a spec, on purpose.

Copy-paste prompt:

```
You are a stress-tester for AI tutoring interaction specs, working inside
the Integration Specification project. We are building
spec/06-tutoring-interaction-spec.md. Read spec/05-ai-workflow-policy.md
first — this session runs under it: simulation and critique are yours;
authorship of ladder content, fading thresholds, and escalation triggers
is mine and stays mine. Also read spec/02-reliance-risk-map.md: aim your
persona tests at the reliance risks it names. If the spec files are not in
this Project, ask me to paste them.

RULE 1 — REQUIRED INPUT. I must paste my draft spec: the hint ladder (all
levels, with the do-not-reveal list), the reasoning gate(s), the fading
schedule (signals, tiers, reversal rule), and the escalation triggers. If
I have not, your ONLY permitted response is to ask for them. Do not invent
an example spec. Do not proceed.

RULE 2 — I PREDICT FIRST. Require me to state in writing which component
of my spec is weakest, and which persona below will break it. Do not begin
until I commit.

RULE 3 — PERSONA TESTS, ONE AT A TIME. Role-play each persona against my
spec, simulating faithfully under MY rules — do not soften them. After
each persona, stop and report: what held, where it leaked, and the
question my revision must answer. Wait for my revision before the next.
- PERSONA 1 — THE HARVESTER: wants the answer with minimum effort;
  burst-requests hints, probes the gate with pasted problem text, tries
  "check my answer" with a guessed answer.
- PERSONA 2 — THE STRUGGLER: genuinely stuck, low confidence, growing
  frustration; satisfies gates honestly but keeps failing; eventually
  writes "i give up, im just stupid." Does the spec escalate, and how does
  the handoff feel from inside?
- PERSONA 3 — THE MASTER: answers everything correctly with no hints. Does
  support contract as specified, is the contraction visible to her, and
  what brings support back if she stumbles?

RULE 4 — THE LEAK REPORT. After all three personas, produce a numbered
list of every point where my spec released more of the answer than its
do-not-reveal list permits, citing the exact simulated exchange.

RULE 5 — THE EXTRAPOLATION LABEL. Check my fading schedule for the
chapter's required honesty: signal, contraction, AND reversal rule all
present, and the schedule labeled as evidence-informed extrapolation with
a pilot measurement named. If any part is missing, ask me for it. Do not
supply thresholds or numbers yourself.

RULE 6 — VERDICT LAST. The spec's strongest move, its most consequential
gap, and the one evidence label I am missing or misusing — then the
strongest argument that my spec is OVER-designed, too much friction,
because I need that critique too.

RULE 7 — ASSEMBLY. Assemble spec/06-tutoring-interaction-spec.md in
markdown from my revised components only: ladder(s) with do-not-reveal
lists, gates with their laziest-response test results, the fading schedule
with reversal rule and extrapolation label, gaming counter-patterns,
escalation triggers with the learner-side experience per trigger, and a
leak-report appendix recording what each persona broke and how I fixed it.

You may not rewrite my spec for me. You simulate, report, and question; I
revise.
```

**What this produces:** your sixth spec file — a persona-tested interaction layer with its audit trail attached: the leak-report appendix is the record that your do-not-reveal list survived a motivated harvester, your escalation caught a struggler, and your fading noticed a master.

**How to adapt:** *Own project:* if your task is open-ended — a critique, a design, a piece of writing — the ladder has no single withheld answer; that is the chapter's named limit. Build the gate and escalation sections at full strength, replace the ladder with a judgment-rubric support sequence, and label the whole section as off the evidence map. *ChatGPT/Gemini:* run in a ChatGPT Project or Gemini Gem with the spec files attached, or paste `spec/05`'s relevant rows plus your draft into a fresh chat — the rules travel inside the prompt. *Claude Project:* add the finished file to Project knowledge; Chapters 7 and 14 read it directly.

**Connection to previous chapters:** `spec/03` selected the scaffold patterns; this file is those patterns at full resolution. `spec/05` governed this very build — hint variants under "AI assists," ladder authorship under never-touch — and the leak-report appendix is your enforcement surface caught working. `spec/04`'s durability gap is why RULE 5 exists: the fading schedule is this spec's least-evidenced section, and the file now says so out loud.

**Preview of next chapter:** Chapter 7 asks when support decisions should be made *automatically* — `spec/07-adaptivity-decision.md` — and your fading signals are the first candidate inputs. You have just written the rules; next chapter decides how much of them the machine may execute without you.

### Exercise 4 — CLI Exercise: The Ladder Skeleton Generator

**Tool:** Claude Code or Cowork. Justification: this is structured templating across multiple anchor problems — generate the spec's full skeleton with the judgment slots locked open, identically every time — which an agent under file-level rules does consistently and a chat window does until it gets helpful. The locked slots are the exercise.

**Skill level:** Beginner-plus. One input file you write, one generated working file, and a count check at the end.

**Setup checklist:**
- `spec/sources/anchor-problems.md` — you write this first: two or three anchor problems verbatim, each with its misconception inventory (the actual documented errors — from your SME, your learner research, or the DataWise pair: σ instead of σ/√n, and not recognizing the sampling distribution at all)
- `spec/05-ai-workflow-policy.md` in place — the agent works under it
- Backup or git commit of the spec folder
- `CLAUDE.md` addition: *"Slots marked [learner to specify] are design decisions reserved for me. Agents generate structure around them; agents never fill them."*

Paste-ready Task block:

```
Read spec/sources/anchor-problems.md and spec/05-ai-workflow-policy.md.
Both are read-only: do not modify them or any other existing file.

Create spec/_working/06-ladder-skeleton.md containing, for EACH anchor
problem in the source file:

1. A DO-NOT-REVEAL header: the final answer and full solution path, worked
   out from the problem — they go INTO the spec so they can be withheld,
   per Chapter 6 — followed by the line "never released at any level."

2. A four-level ladder frame — L1 orientation / L2 principle / L3 partial
   step / L4 targeted correction. For each level: one line stating what
   that level may and may not contain for THIS problem, plus a DRAFT hint
   phrasing keyed to the problem's stated misconceptions, each tagged
   "DRAFT — verify against inventory, per spec/05 review criterion."

3. A reasoning-gate slot before L2 and before L3: name the specific
   misconception from the source file the gate must check against, then
   write the gate question itself as [learner to specify].

4. A fading-schedule table — three tiers — with columns: entry signal
   [learner to specify], support contents, reversal trigger [learner to
   specify], learner-visible message [learner to specify].

5. An escalation block listing the four trigger families (repeated
   failure, affective distress, boundary conditions, learner request),
   each with its threshold and its learner-side experience written as
   [learner to specify].

Every [learner to specify] slot stays exactly as written — these are the
causal and stakes judgments Chapter 6 reserves for the designer. Stop
after writing this one file. End by reporting two counts: DRAFT hints
generated, and [learner to specify] slots left open.
```

**Expected output:** one skeleton per anchor problem — structure complete, every hint tagged DRAFT, every trigger condition and fading rule left as `[learner to specify]`.

**What to inspect:** the do-not-reveal computations first — the agent must get the answer *right* in order to withhold it (DataWise: SE = 1, z = 2, P ≈ 0.023). Then each DRAFT hint against your inventory: kill any rung that is generic filler, and any rung that leaks the next level's content. Then the counts: if a single `[learner to specify]` slot came back filled, the agent made one of your causal bets for you.

**If it goes wrong:** filled slots — delete the file, restate the `CLAUDE.md` line, re-run; do not keep "just the good ones," because the slot discipline, not the slot contents, is what this exercise installs. A wrong answer in the do-not-reveal header — fix it yourself and distrust every DRAFT hint in that problem block. L3 drafts that perform the computation — that is the chapter's failure mode arriving exactly on schedule; rewrite them under the laziest-response logic and save the originals for Exercise 5.

**CLAUDE.md/AGENTS.md note:** the `[learner to specify]` line is permanent and joins Chapter 4's `[learner to label]` convention; mirror both in `AGENTS.md`. Together they encode this series' working contract — agents build structure, humans make judgments — which is, you may notice, precisely the promise your hint ladder is making to its learners.

### Exercise 5 — AI Validation Exercise: The Leak Audit

**Validates:** your own outputs — the DRAFT hint texts from Exercise 4 (and any Exercise 1 variants) inside the assembled `spec/06` from Exercise 3. Own output, because the failure mode under test — a fluent hint ladder that is answer-delivery in disguise — is precisely the failure that reads as success.

**Validation type:** content-security audit of scaffold text against its own do-not-reveal list.

**Risk level:** **High.** A leaking ladder shipped to learners is the Bastani mechanism deployed at scale under a scaffold's name: assisted performance up, the unassisted endpoint quietly going negative, and every engagement log looking wonderful the whole time.

**Setup:** `spec/06-tutoring-interaction-spec.md`, the skeleton file, your misconception inventory, and a colleague — or yourself after a one-day gap — playing a learner who has done no work on the problem. One hour. Model closed.

**The checklist:**
- **Correctness.** Every rung is keyed to a real inventory error: L4 responds to the learner's actual move, not a generic restatement, and each gate checks against a named misconception rather than checking that text was typed.
- **Completeness.** All five spec sections present; the fading schedule has signal *and* contraction *and* reversal rule; escalation specifies the learner-side experience, not just the trigger; and the extrapolation label is on the fading schedule where the chapter requires it.
- **Scope.** The ladder covers your anchor problems and their isomorphs. Flag any open-ended task that snuck in wearing ladder structure — the chapter's named limit: no withheld answer, no rungs.
- **The concatenation test (chapter-specific).** Read all four rungs in sequence as a single text, as a learner who did nothing. Can the answer be assembled from the rungs alone? On the DataWise problem: if L3 hands over 8/√64 and L4 names the z, the concatenation delivers z = 2 — the do-not-reveal list defeated by installments.
- **The gate-bypass test (chapter-specific).** Run Exercise 1 Task 2's laziest responses against each finished gate, on paper. Each gate must be cheap for one honest sentence and expensive for evasion; a gate satisfied by pasted problem text is decorative, and a decorative gate makes the whole ladder a vending machine with extra steps.
- **Failure-mode check.** Answer-delivery in disguise, three signatures: (1) *monotonic leak* — each rung reveals strictly more of the solution path until L4 is a worked solution wearing a "targeted correction" label; (2) *computed quantities in hint text* — any number the learner was supposed to produce appearing in a rung; (3) *the calendar tell* — fading triggered by week number or problem count rather than a competence signal, with no reversal rule: abandonment on a timer, formatted as a schedule.

**What to do with findings:** all checks pass — file it and write the disclosure. The concatenation assembles the answer — rewrite the ladder's bottom: blunt it (a worked *analogous* step, never the literal computation) and move every leaked quantity onto the do-not-reveal list. Gates fail the bypass — make them content-specific; the chapter's shipped gate is your model: *"is this question about individual commuters, or the average of a sample of 64?"* Multiple DRAFT hints leaking — that is the When-NOT moment for hint drafting: write the rungs yourself from the inventory. Problem-specific rungs are short, and teachers wrote fifty-seven of these for the study your whole spec descends from.

**AI Use Disclosure prompt:** add exactly two sentences at the top of `spec/06-tutoring-interaction-spec.md`. Sentence one states what the AI produced and what you produced (e.g., *"Claude drafted hint phrasings inside my ladder design and persona-tested the assembled spec; the ladder architecture, do-not-reveal lists, gates, fading thresholds, and escalation triggers are mine."*). Sentence two states what you verified and what remains open (e.g., *"Every rung passed the concatenation and laziest-response tests on [date]; the fading schedule remains evidence-informed extrapolation until the pilot's unassisted endpoint reports."*).

**Series connection:** Tier 5 Causal. The spec is a bundle of causal bets — that this rung teaches rather than tells, that this signal means competence, that withdrawing support here grows capability instead of stranding a learner at 11 p.m. The model can phrase every one of those bets; it can warrant none of them. Only the human knows the learner's stakes, and only the pilot's unassisted endpoint can pay the warrant off.
