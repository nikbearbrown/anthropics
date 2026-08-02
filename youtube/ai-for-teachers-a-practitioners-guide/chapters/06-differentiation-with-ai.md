# Chapter 6 — Differentiation with AI: Reading Levels, Scaffolds, and Supports


## TL;DR

- Here is a deceptively simple fact about how readability scores work.
- The chapter moves through Two things that look the same and aren't, What Bjork says about this, The WIDA vocabulary, and why it matters for prompts, IEP and 504: where the phase gate is legal, not pedagogical, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Speed is the problem. The AI hits the Lexile band in seconds, and the question you didn't ask is whether the concept survived.*

---

Here is a deceptively simple fact about how readability scores work. The Lexile Framework — the scale most U.S. schools use to match readers to texts — assigns a number to a passage by running two statistics: average sentence length and average word frequency.[^lexile] That is the whole formula. Longer sentences, rarer words: higher Lexile. Shorter sentences, common words: lower Lexile.

This means that when an AI "lowers the Lexile" of a passage, it is doing something specific and mechanical. It is shortening clauses, breaking compound sentences, and swapping low-frequency words for higher-frequency ones. *Symbiotic* becomes *tiny plants that live with the coral*. *Photosynthesis* becomes *the way plants make food from sunlight*. The model is doing exactly what the Lexile formula scores, and it does it reliably and fast.

Here is the deception. The Lexile formula does not measure inferential demand. It does not measure how abstract the ideas are, how much prior knowledge they require, or whether the causal structure of the argument survived the rewrite. A passage can hit 700L and still be conceptually opaque if the underlying ideas were never touched by the simplification. More dangerously: a passage can hit 700L and have its entire mechanism stripped out, leaving behind a sequence of facts that reads fluently and teaches nothing.

The speed is precisely the problem. AI produces a structurally correct lower-Lexile version in twelve minutes, and the version looks finished. The question of whether the concept the lesson was designed to teach is still in the document — that question is invisible unless you ask it.

![Two input boxes labeled "Average sentence length" and "Average word frequency" feeding into a single formula box that outputs a Lexile score. To the right, a callout lists what the formula does not measure: inferential demand, prior knowledge load, causal structure, abstractness of ideas.](../images/06-differentiation-with-ai-fig-01.png)
![What the Lexile formula measures and what it does not. Two surface statistics in; one number out. Everyth](images/06-differentiation-with-ai-fig-01.png)
*Figure 6.1 — What the Lexile formula measures and what it does not. Two surface statistics in; one number out. Everything that decides whether the concept survived sits in the callout.*

This chapter is about asking it.

---

## Two things that look the same and aren't

Before anything else about workflows and templates, the distinction that governs the whole chapter. There are two moves teachers make under the name "differentiation," and they are fundamentally different things.

**Leveling** changes the text. The student reads a different version of the passage. What the student encounters — the sentence structures, the vocabulary, the concepts, the causal chain — is not what other students encounter. The lower-band reader reads a different document.

**Scaffolding** does not change the text. The student reads the original. Around the text, the teacher places supports: a sentence frame, a vocabulary glossary, a graphic organizer, a model paragraph, a partner read. These supports absorb the *extraneous* load — the cognitive effort that comes from unfamiliar sentence structures or unknown academic words — so the *germane* load, the actual thinking the lesson requires, can be carried.

The difference matters because genuine learning requires cognitive friction. Not struggle for its own sake, but the specific event in which a learner's current model of the world meets material that doesn't fit — and has to revise. That prediction error is the trigger. Without the trigger, there is no consolidation. Without consolidation, there is no durable learning.

A scaffold that absorbs extraneous load preserves the trigger. A leveled text that absorbs germane load removes it. They look similar from the outside — in both cases the student has something more accessible in front of her. They are not similar. The student with the scaffold is working on the same concept at a lower linguistic cost. The student with the aggressively leveled text is working on a concept that may no longer be the one the lesson is about.

This is the failure mode AI-assisted differentiation is particularly susceptible to, because the optimization target — a lower Lexile number — is exactly the surface signal that can be hit without touching the underlying problem.

The discipline: every time you accept a lower-band version of a passage, ask whether the simplification dropped any of the work the lesson was designed to do. There is a one-sentence test. *Would I be teaching the same concept tomorrow if every student were on this version?* If no, you have not differentiated. You have quietly routed some students out of the lesson.

![Two parallel columns. Leveling on the left shows an original passage being rewritten into a different document; arrows label "extraneous load reduced" and "germane load at risk." Scaffolding on the right shows the original text untouched, surrounded by sentence frames, a glossary, and a graphic organizer; arrows label "extraneous load reduced" and "germane load preserved." Both end with a student reading. The scaffolding column carries a checkmark on "same concept as class"; the leveling column carries a warning on "concept may be lost."](../images/06-differentiation-with-ai-fig-02.png)
![Leveling versus scaffolding. The same student ends up reading something more accessible in both columns; ](images/06-differentiation-with-ai-fig-02.png)
*Figure 6.2 — Leveling versus scaffolding. The same student ends up reading something more accessible in both columns; only one of the two leaves the concept the lesson was designed to teach inside the document.*

---

## What Bjork says about this

There is a research tradition in cognitive psychology — Robert Bjork's work on desirable difficulties is the central thread — that established something counterintuitive about learning: conditions that make acquisition feel easy often impair long-term retention and transfer.[^bjork] The mechanism is that easy acquisition produces high *retrieval strength* (you can access the material now) without high *storage strength* (you have encoded it deeply enough to access it later, in other contexts, in different forms).

A 400L version of a 900L science passage can produce a student who reads fluently, answers the exit ticket correctly, and cannot reconstruct the concept two weeks later. Not because the student is weak, but because the easy version did not require the effortful processing that makes memory durable. The student processed words. She did not process the idea.

This is not an argument against leveling. It is an argument for being precise about when leveling is the right move. When the goal is fluent access to current events, an age-appropriate story, a daily reading practice — leveling opens access without much loss. When the goal is understanding a causal mechanism, constructing an argument, or applying a concept to a novel case — leveling may be buying short-term fluency at the cost of the learning the lesson was supposed to produce.

The test is still: *would I be teaching the same concept if every student were on this version?* Bjork's work explains why the answer matters.

---

## The WIDA vocabulary, and why it matters for prompts

Forty-one states and territories use the WIDA English Language Development Standards Framework to assess and scaffold multilingual learners.[^wida] WIDA differentiates language development across six proficiency levels — Entering, Emerging, Developing, Expanding, Bridging, Reaching — along three dimensions (word/phrase, sentence, discourse) and organizes around four Key Language Uses: Narrate, Inform, Explain, Argue.

For AI-assisted differentiation, WIDA gives you vocabulary the model does not have by default. The vague prompt "*generate sentence frames for ELL students*" produces generic frames. The specific prompt "*generate sentence frames at WIDA Level 2 (Emerging) and WIDA Level 4 (Expanding) for sixth-grade students arguing whether coral bleaching is reversible, using the Key Language Use of Argue*" produces a usable artifact — one that distinguishes between the structural support a Level 2 student needs and the discourse-level support a Level 4 student needs.

What WIDA cannot supply to the model, and what no prompt can supply, is where this particular student sits on the continuum, the home language she is translanguaging from, and the academic registers she has and hasn't encountered in prior schooling. The model knows the framework. The teacher knows the student.

A misconception worth naming directly: translation is not differentiation. A perfectly translated Spanish version of an inaccessible English text is still an inaccessible text in Spanish. WIDA's framing — that multilingual learners can engage with grade-level content given appropriate linguistic scaffolds — explicitly resists the deficit reading in which "ELL version" means "easier content." The scaffold gives access to the same concept at a lower linguistic cost. It does not substitute a different concept.

A sentence frame at WIDA Level 3 — *One piece of evidence for [claim] is [evidence]. This is important because [reasoning]* — gives the multilingual learner the structure of academic argument while leaving the cognitive work, the actual claim and evidence, to her. The frame lowers the linguistic friction. It does not lower the conceptual friction. That distinction is the whole game.

---

## IEP and 504: where the phase gate is legal, not pedagogical

The differentiation phase gate in this chapter has two levels. The first is pedagogical: the teacher verifies that the simplification did not strip the concept. The second is legal, and it applies specifically to students with IEPs and 504 plans.

An Individualized Education Program under IDEA is a legal document developed by a multi-disciplinary team.[^idea] Federal law specifies the minimum team membership: a parent, a general-education teacher if applicable, a special-education teacher, a Local Education Agency representative qualified to supervise special education, and someone qualified to interpret evaluation results. The team — not the general-education teacher alone, not the AI — authorizes accommodations and modifications. Section 504 of the Rehabilitation Act of 1973 covers students with disabilities who do not qualify under IDEA but require accommodations to access the general curriculum; 504 plans go through a similar team process.

AI can draft accommodation language. It can suggest accommodations consistent with an anonymized student profile — extended time, graphic-organizer supports, audio versions of text, modified workload, sentence frames. The proposal is a starting point. The authorization is a legal act made by the team, with the licensed specialist present, on the basis of this student's history, evaluation results, and documented response to prior interventions.

The phase gate, stated: AI proposes from an anonymized profile. The licensed specialist and team authorize. The teacher implements what the team authorized.

The reason this gate exists is not procedural caution. It is that the team holds knowledge the model cannot have: the student's history, the interventions that have and haven't worked, the clinical judgment that distinguishes an accommodation that opens access from one that removes challenge inappropriately. A teacher who accepts AI-generated accommodations without team review has not just violated a procedural requirement under IDEA. She has skipped the substantive judgment the gate exists to protect.

![Three sequential boxes with arrows. Box 1: "AI proposes — from anonymized profile, suggests accommodations from standard library." Box 2: "Licensed specialist and team authorize — review against student history, evaluation results, and response to prior intervention." Box 3: "Teacher implements — what the team has authorized, no more." A red X marks a shortcut arrow from Box 1 directly to Box 3, labeled "skips legal authorization and clinical judgment."](../images/06-differentiation-with-ai-fig-03.png)
![The IEP and 504 phase gate. The middle box is the legal act, performed by the team. The shortcut arrow lo](images/06-differentiation-with-ai-fig-03.png)
*Figure 6.3 — The IEP and 504 phase gate. The middle box is the legal act, performed by the team. The shortcut arrow looks like efficiency and reads, in court and in practice, as the skipped step.*

---

## FERPA and the anonymization rule

The Family Educational Rights and Privacy Act protects personally identifiable information in education records from disclosure to third parties without consent.[^ferpa] When a teacher pastes a student's name, ID, behavioral history, or evaluation results into a public AI chatbot, the teacher has disclosed PII to a third party — the AI vendor, who is not bound by FERPA unless under a written service agreement with appropriate provisions.

The operational rule is simple to state: anonymize before submitting. Replace student names with role labels. Strip identifying detail. Keep educationally relevant features. *A sixth-grade student with an IEP for ADHD, extended-time and break-frequency accommodations, reading at approximately Lexile 600* — that description supports a useful prompt. It does not identify a student.

What counts as sufficient anonymization in a specific district is not a question this chapter answers. Whether quasi-identifiers — free-lunch status combined with grade and class size in a small school — can re-identify a student depends on population size, the specific data, and the tool's terms of service. The district's data-privacy officer and counsel decide what is sufficient in a given setting. If the district has contracted with a vendor under a FERPA-compliant agreement, the rules inside that walled garden differ from the rules in a public chatbot.

Default outside the walls: the anonymization rule. Strip the name. Keep the profile. The AI's suggestion can be applied back to the specific student by the teacher and team who know who Student A is.

| Field | What you know (do not submit) | What the prompt receives (safe to submit) |
|---|---|---|
| Student name | Jordan Martinez | Student A |
| Grade and school | 8th grade, Lincoln Middle School | 8th grade |
| IEP detail | Jordan has ADHD; struggles to sustain attention during long reading tasks | Student with IEP for ADHD; benefits from frequent breaks and chunked reading |
| Reading level | Jordan reads at about 5th grade | Reads at approximately Lexile 750 |
| WIDA level | Not applicable here | Not applicable |
| Re-identification risk | High | Low |

*Table 6.1 — The anonymization rule, applied. The left column is what you carry as the teacher. The right column is what the prompt receives. The translation in between is the discipline that keeps PII inside the room.*

---

## A worked example: one paragraph, three bands, one decision

Take a single paragraph from a middle-school science article on coral bleaching. Original, approximately 1050L:

> *Between 2014 and 2017, repeated marine heatwaves drove the Great Barrier Reef into the most severe bleaching event on record. When sea surface temperatures rose more than one degree Celsius above the long-term summer maximum, the symbiotic algae that live inside coral tissues — called zooxanthellae — were expelled, leaving the coral skeleton visible through transparent tissue. Without the algae's photosynthetic products, much of the affected coral starved within weeks.*

A prompt structured to preserve the mechanism — specifying that every scientific claim, every date, and the causal chain from heat to algal expulsion to coral starvation must survive — produces three versions. Here is the 600L version a reasonable model might return:

> *Between 2014 and 2017, the ocean got very warm three years in a row. The tiny algae that live inside coral (called zooxanthellae) leave when the water gets too warm. Without the algae, the coral turns white. Without the food the algae made, much of the coral died within weeks.*

Run the spot-check.

The dates survived. The algae survived (by name, in parentheses). The starvation outcome survived. What did not survive: the specific temperature threshold — one degree Celsius above the long-term summer maximum — and the word *photosynthesis*. The causal chain is present as a sequence of events; the mechanism that makes the chain a mechanism — temperature operating on a specific symbiotic relationship, cutting off a specific metabolic process — has been gentled into "the water gets too warm."

Tomorrow's lesson asks students to argue whether the bleaching is reversible. That argument requires the mechanism. A student who can only access the 600L version knows *what happened*. She may struggle with *under what condition* and *through what process* — which is where the argument lives.

Three choices, and the model cannot make any of them for you.

The first choice: accept the 600L version as written. The lowest-band readers get the sequence of events. The argument becomes inaccessible to them. This is leveling that stripped the germane load. Avoid it.

The second choice: edit the temperature threshold and the word *photosynthesis* back into the 600L version with a gloss. The text becomes something like 680L and preserves the mechanism. This is the right move when the mechanism is the lesson and the student can handle the slightly higher band with the terms defined.

The third choice: give the lowest-band readers the 800L version — which preserved the mechanism — paired with a partner-read scaffold and a graphic organizer that maps the causal chain. This uses scaffolding to compensate for the higher band rather than leveling to remove it. Often the best choice precisely because it keeps the student in the same conceptual lesson as everyone else.

None of these choices is made by the Lexile formula. The formula measured sentence length and word frequency. The choice requires knowing what the lesson is trying to do.

This is the moment the chapter has been building toward. The AI produced three versions in twelve minutes. The differentiation happened in the thirty minutes of spot-checking, choosing, and editing. The speed was real. The dividend was in the judgment that followed it, not in the generation itself.

| Element | Present in original (1050L) | Survived in 600L version? | Action required |
|---|---|---|---|
| Dates 2014–2017 | yes | yes | none |
| Temperature threshold 1°C above long-term max | yes | NO — became "too warm" | edit back in |
| Zooxanthellae named | yes | yes (in parentheses) | none |
| Photosynthesis as mechanism | yes | NO — became "food the algae made" | edit term back, or use 800L version |
| Starvation outcome | yes | yes | none |
| Causal chain intact | yes | PARTIAL — sequence present, mechanism lost | choose Option B or C |

*Table 6.2 — The coral bleaching spot-check. A template you can copy onto any passage. The "Action required" column is the differentiation; the rest is bookkeeping.*

---

## The prompt that does not make the mistake

Here is the structure of a prompt that reduces the chance of stripping the mechanism. The key moves are the explicit preservation constraints and the self-check requirement.

```
ROLE: You are an editor adapting [grade-level] [subject] text
for grade-level readers.

CONTEXT: Source passage is approximately [estimated Lexile] L, from
a [grade] unit on [topic]. Class includes readers from approximately
[lower band] L to [upper band] L.

TASK: Produce [n] versions at target bands [list bands]. Preserve:
- Every factual claim and date
- Every named entity
- The causal mechanism the passage is built around: [state it
  explicitly in one sentence]

CONSTRAINTS:
- Keep the following terms in all versions: [list terms]. In the
  lowest band, define each in plain English and keep the term in
  parentheses on first use.
- Do not invent facts not in the source.
- After each version, list every concept you simplified that I
  should verify before delivering the text to students.
- Do not include student names, IDs, or identifying information.

SOURCE PASSAGE:
[paste passage]
```

The constraint that matters most is the one that names the causal mechanism explicitly before the model writes a word. If you can state the mechanism in one sentence — *heat above a threshold stresses the symbiotic algae, which are then expelled, cutting off the coral's photosynthetic food supply* — the model has a target to preserve, and you have a test to run against every version it returns. If you cannot state the mechanism in one sentence, the problem is not the prompt. The problem is that you have not yet been precise enough about what the lesson is teaching.

---

## The scaffold analog

The scaffolding prompt follows the same logic but has an additional constraint baked in: the scaffolds must reduce extraneous load without reducing cognitive demand. Here is how to state that in a prompt the model can act on.

```
ROLE: You are an instructional designer producing scaffolded supports
for a writing or discussion task.

CONTEXT: Grade [grade], subject [subject], standard [code].
The task asks students to [task in one sentence].
Student population: [anonymized description — e.g., "two multilingual
learners at approximately WIDA Levels 2 and 4," "one student with an
IEP for a specific learning disability in reading who benefits from
graphic-organizer supports for compare-contrast tasks"].

TASK: Produce three supports: (1) sentence frames at the specified
WIDA levels using the Key Language Use of [Narrate/Inform/Explain/Argue];
(2) a graphic-organizer template matching the task structure;
(3) a vocabulary glossary of 5–8 academic terms with student-friendly
definitions.

CONSTRAINTS:
- Supports must reduce extraneous load (linguistic, organizational),
  not the cognitive demand of the task.
- Do not produce a simpler version of the task that removes conceptual
  work.
- Do not include student names, IDs, or identifying information.
- Label any supports intended for use under an IEP or 504 plan as
  "draft for IEP/504 team review — not for direct student delivery."
```

The label requirement on IEP/504 supports is not bureaucratic caution. It is the mechanism that keeps the phase gate from collapsing: a draft labeled "team review required" is a draft the teacher cannot inadvertently treat as authorized.

---

## Three things that would make me revise this chapter

The chapter's central claim is that hitting a target Lexile band is a necessary but insufficient condition for useful differentiation, and that the spot-check for conceptual fidelity is the substantive act — the part AI cannot do. Two kinds of evidence would force revision.

First: a well-powered, peer-reviewed study showing that commercial LLMs reliably hit specified Lexile bands at K–12 grade levels *while* preserving inferential demand, causal mechanism fidelity, and standards-aligned content — measured by independent expert review, not by the readability metric alone — would shift the spot-check from the primary differentiation act to a quality-assurance step. That evidence does not exist as of this writing. The closest adjacent evidence is a 2025 study of GPT-4 simplifying medical radiology reports, which found that 34 percent of simplified outputs omitted at least one clinically relevant fact.[^khazanchi] Different domain, different stakes, adult text — the rate is not transferable. The shape of the failure is.

Second: if UDL-designed AI-assisted differentiation were shown, in a randomized trial with long-run follow-up, to produce durable learning gains for students with IEPs and ELL students at the same rate as specialized human instruction, the chapter's emphasis on human clinical judgment at the phase gate would need to be revisited. That trial does not exist.

Until the evidence exists, the spot-check is the differentiation.

---

## Exercises: using AI to understand AI differentiation

These exercises are done with an AI tool. The first two build the habit of the spot-check. The third builds the FERPA muscle before it is needed.

**Exercise 1: The Lexile audit.**

Take one passage from a current unit at its native Lexile. Use the prompt structure from this chapter to generate two lower-band versions. For each version: (1) list every factual claim, named entity, date, and causal connection in the original; (2) check whether each survived; (3) run the Frictional check — would the lesson the original was designed to teach still be the lesson if the student read this version? Write one sentence about what the audit revealed about how the model was simplifying. Then ask the model: *list every concept you simplified in producing this version.* Compare its list to yours. Where do they diverge?

**Exercise 2: The scaffolding versus leveling experiment.**

Choose a passage and a student profile (anonymized). Generate two products: (1) a lower-Lexile version of the passage; (2) a scaffold set for the original passage — sentence frames, graphic organizer, vocabulary glossary. Give each to the same (hypothetical) student for the same lesson. Ask: which version preserves the cognitive demand the lesson is built around? Which reduces it? Write one sentence naming the trade-off each version makes, and one sentence about which you would use and why.

**Exercise 3: The FERPA-safe prompt.**

Think of a real student in your current class. Without writing the student's name, ID, or any identifying detail, rewrite the profile as a prompt: replace the name with a role label, strip identifying detail, keep educationally relevant features (grade, approximate reading level, IEP or 504 status by category, WIDA level if applicable, known supports). Use the scaffolded-assignment prompt to generate a differentiation move. Then ask yourself: if I had submitted this prompt, would any PII have left the room? The exercise is the editing. Write one sentence about what you had to remove to get there, and whether any educationally relevant information was lost in the process.

---

The AI hits the Lexile band in seconds. Whether the concept survived is a question you ask in the thirty minutes after. The speed is the tool's. The judgment is yours — and for IEP and 504 students, the judgment belongs to the team, not to the tool, and not to you alone. Chapter 7 takes the camera outward: what teachers communicate to parents, administrators, and IEP teams, and how AI can draft the message while the teacher retains the relationship and the professional responsibility for what the message says.

---

[^lexile]: MetaMetrics — Lexile Framework for Reading. <https://www.metametrics.com/lexile-for-reading/>. Technical basis: Stenner, A. J., Burdick, H., Sanford, E. E., & Burdick, D. S. (2007). *The Lexile Framework for Reading Technical Report.* <https://metametricsinc.com/wp-content/uploads/2017/07/Stenner_Burdick_Sanford__Burdick-_The_LFR_Technical_Report.pdf>.

[^bjork]: Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press. The storage-strength / retrieval-strength distinction: Bjork, R. A., & Bjork, E. L. (1992). A new theory of disuse and an old theory of stimulus fluctuation. In A. Healy, S. Kosslyn, & R. Shiffrin (Eds.), *From learning processes to cognitive processes: Essays in honor of William K. Estes* (Vol. 2, pp. 35–67). Erlbaum.

[^wida]: WIDA (2020). *WIDA English Language Development Standards Framework, 2020 Edition.* Board of Regents of the University of Wisconsin System. <https://wida.wisc.edu/resources/wida-english-language-development-standards-framework-2020-edition>. 41 states and territories as consortium members as of mid-2025.

[^idea]: Congressional Research Service (2025). *The Individuals with Disabilities Education Act (IDEA), Part B: Key Statutory and Regulatory Provisions.* CRS R41833. <https://www.congress.gov/crs-product/R41833>. IEP team membership requirements: U.S. Department of Education, *A Guide to the Individualized Education Program* (2000). <https://www.ed.gov/sites/ed/files/parents/needs/speced/iepguide/iepguide.pdf>.

[^ferpa]: Family Educational Rights and Privacy Act, 20 U.S.C. § 1232g. U.S. Department of Education Office of Educational Technology (2023). *Artificial Intelligence and the Future of Teaching and Learning.* <https://www.ed.gov/sites/ed/files/documents/ai-report/ai-report.pdf>. Future of Privacy Forum (2024). *Vetting Generative AI Tools for Use in Schools.* <https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf>.

[^khazanchi]: Khazanchi, R., et al. (2025). Evaluating the accuracy of GPT-4 in simplifying spine imaging reports. *Skeletal Radiology*. <https://doi.org/10.1007/s00256-025-05027-9>. Finding: 34% of simplified outputs omitted at least one clinically relevant fact. Domain and population differ from K–12 education; failure shape is transferable, failure rate is not.

---

##  AI Wayback Machine
The framework this chapter rests on did not start with the Lexile score. It started with a Russian psychologist who died in 1934. **Lev Vygotsky** named the gap between what a student can do alone and what she can do with help the *zone of proximal development*. The support that lives inside that gap — the sentence frame, the partner read, the worked example — is what later researchers called *scaffolding*. The distinction between leveling (which changes the text) and scaffolding (which changes the support around the text) is Vygotsky's distinction made operational. If you take only one idea from the prior literature into your AI-assisted differentiation workflow, take this one.

![Lev Vygotsky, circa 1930. AI-generated portrait based on public domain photographs.](../images/lev-vygotsky.jpg)
*Lev Vygotsky (1896–1934). AI-generated portrait based on public domain photographs (Wikimedia Commons).*

![Lev Vygotsky](../images/lev-vygotsky-755.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Lev Vygotsky, and how does his Zone of Proximal Development
connect to the distinction between leveling and scaffolding in this
chapter? Keep it to three paragraphs. End with the single most
surprising thing about the publication history of his work.
```

→ Search **"Lev Vygotsky"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to map a specific WIDA Level 2 sentence frame and a graphic-organizer scaffold to Vygotsky's ZPD — which part is the "more knowledgeable other," which part is the "tool," and what does the student supply?
- Ask it about why Vygotsky's work was suppressed in the USSR for almost three decades, and what that does to the timeline of how scaffolding entered Western education research.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 6.1 — What the Lexile formula measures and what it does not. Two surface statistics in; one number out. Everyth

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "What the Lexile formula measures and what it does not. Two surface statistics in; one number out. Everyth". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/06-differentiation-with-ai-fig-01.html`

---

### Figure 6.2 — Leveling versus scaffolding. The same student ends up reading something more accessible in both columns; 

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Leveling versus scaffolding. The same student ends up reading something more accessible in both columns; ". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/06-differentiation-with-ai-fig-02.html`

---

### Figure 6.3 — The IEP and 504 phase gate. The middle box is the legal act, performed by the team. The shortcut arrow lo

Create a standalone D3 v7 HTML file for a phase-gate workflow diagram titled "The IEP and 504 phase gate. The middle box is the legal act, performed by the team. The shortcut arrow lo". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/06-differentiation-with-ai-fig-03.html`
