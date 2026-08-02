# Chapter 11 — Research, Advising, and Faculty Workflows

**Capability built:** Use Claude for faculty work beyond lesson planning — literature exploration, grant framing, advising preparation, manuscript feedback, and administrative tasks — while keeping verification and professional judgment in human hands.

---

## The Scene

It is late on a Tuesday. You have a tenure file to review by Friday, a graduate student waiting for feedback on a draft chapter, three advising appointments tomorrow morning, and a grant letter of intent due next week. The lesson plan was the easy part of your week.

Faculty work extends far past the classroom door. Research reading, advising conversations, committee responsibilities, manuscript reviews, grant applications, and administrative correspondence — these are the workflows that fill the hours that students never see. They are also the places where AI assistance has arrived quietly, with real utility and real risk.

This chapter treats Claude as a professional thinking partner for the full range of faculty work. The same principle that runs through every chapter still governs: assistance, review, and responsibility. Claude can generate, draft, and organize. You still verify, judge, and sign your name.

---

## What This Chapter Lets You Do

By the end of this chapter you can:

- Use Claude to accelerate literature exploration while maintaining source verification discipline.
- Draft and critique grant outlines with Claude without handing it the scholarly claim.
- Prepare for advising meetings with Claude's help while protecting student privacy.
- Use Claude as a first reader for manuscript drafts and reviewer-response letters.
- Redesign assignments and course materials through a structured faculty workflow.
- Apply a verification checklist to any faculty-facing Claude output before it enters professional use.

---

## Core Concept: The Faculty Workflow Zone

The classroom-facing chapters of this book have focused on what teachers produce for students. Faculty members also produce for themselves and for the scholarly community: findings, arguments, appraisals, and records. These outputs carry a different kind of authority. A lesson plan misread can be corrected next week. A grant claim that misstates the literature damages your credibility. An advising note that reveals a student's situation can violate FERPA [verify — institutional policy varies].

Claude can assist in all of these zones. The discipline required is higher, not lower, than it is in classroom planning — because the consequences of unverified output are professional and sometimes legal.

Three categories organize faculty use:

**Research-adjacent tasks** — exploring literature leads, identifying gaps, generating grant framing, structuring manuscript arguments, preparing reviewer responses. High utility; high verification requirement. Claude does not know what is currently published, cannot access paywalled journals, and will hallucinate citations (Anthropic Claude docs, 2024) [verify — current as of writing]. Treat every source name as a lead, not a citation, until you have verified it.

**Advising and relational tasks** — preparing for advising meetings, drafting follow-up notes, summarizing a student's stated goals before a meeting, and thinking through a difficult advising situation. High utility; high privacy obligation. No student name, ID, grade, or identifying information should enter Claude unless your institution has a data processing agreement with Anthropic that covers it (FERPA guidance; U.S. Department of Education AI report, 2023).

**Administrative and communication tasks** — drafting committee reports, professional correspondence, peer-review comments, and bureaucratic language. Moderate utility; verification of facts, institutional accuracy, and tone required before sending.

---

## The Integrity Boundary

Before any workflow, one rule: **Claude cannot be the author of your scholarly claim.**

The Committee on Publication Ethics (COPE) has issued guidance stating that AI tools cannot be listed as authors and that authors remain responsible for work assisted by AI (COPE, 2023). Most major journal publishers have now adopted AI-disclosure requirements, though policies vary [verify — publisher policies change rapidly]. The NIST AI Risk Management Framework (NIST, 2023) frames responsible AI use in professional contexts around auditability and human accountability — not just output quality.

What this means practically: Claude can help you think through your argument, find the right framing, draft a section you will rewrite, or suggest counterarguments you had not considered. Claude cannot determine whether your data supports your conclusion. Claude cannot read the three papers you need to cite. Claude cannot know whether your methodology matches the field's expectations. You can use the thinking; you must own the claim.

---

## Workflow 1: Literature Exploration

You are starting a new research project and need to understand what the field has said about adaptive feedback in first-year writing courses. You do not yet know the key journals, the major theorists, or the likely fault lines in the debate.

**What Claude can do here:** Generate a map of likely concepts, sub-debates, adjacent literatures, and search terms. Think of this as a knowledgeable colleague helping you sketch the terrain before you go to the library.

**What Claude cannot do:** Give you real, current, verified citations. Its training has a cutoff date. It will name real scholars and real journals — and it will sometimes attach those names to titles that do not exist (Anthropic Claude docs, 2024) [verify — current as of writing]. Every specific citation must be verified in your library database before it enters your work.

**Worked prompt:**

> I am beginning a research project on adaptive feedback practices in first-year writing courses at the postsecondary level. I am not yet expert in this literature. Please sketch the major conceptual debates, name the scholars most associated with each position, suggest the journals most likely to publish in this area, and suggest database search terms I should try. Flag anything you are less confident about.

**What to do with the output:**

1. Take the conceptual map as a starting framework, not a final one.
2. Take every scholar name to your library database and verify that they have published what Claude suggests.
3. Run the search terms and see what the database actually returns.
4. Use the gap Claude names — "I am less confident about recent empirical work on peer feedback in digital environments" — as a signal to search more carefully there.

This is a lead-generation use, not a citation use. The verification step is not optional.

---

## Workflow 2: Grant Framing and Critique

You have a research idea and need to write a letter of intent for a federal education grant. You know the research area but find the funder's language and the significance-statement conventions difficult to navigate.

**What Claude can do here:** Help you translate your scholarly language into a funder's framing, identify likely weaknesses in your logic of support, draft an outline for the significance section, and ask you questions that reveal gaps in your argument before reviewers do.

**What Claude cannot do:** Know the current funding priorities of the specific program officer, accurately represent data about outcomes in your field from the last year, or verify that your proposed methodology matches funder expectations.

**Worked prompt:**

> I am writing a letter of intent for an NSF [or equivalent] education research grant. My project investigates how adaptive feedback tools affect revision behavior in first-year college writers. Help me draft an outline for the significance and innovation sections. Then critique the outline as if you are a skeptical grant reviewer looking for weak logic of support, overclaimed novelty, or missing prior work.

**Key discipline:** When Claude critiques your argument, treat it as a useful adversarial reader — but you must verify whether the weaknesses it names are actual weaknesses in the literature or just weaknesses in how you described your project in the prompt. The critique is a rehearsal, not a verdict.

---

## Workflow 3: Advising Preparation

You have three advising appointments tomorrow. One student is navigating a late withdrawal. One is exploring a career change from engineering to education policy. One has been missing office hours and you are concerned.

**What Claude can do here:** Help you think through your approach to difficult conversations, suggest questions to ask, generate a list of institutional resources to mention, and help you draft a follow-up email template after the meeting.

**What Claude cannot do:** Know your student. And — critically — your student must not be brought into the conversation.

**Privacy rule:** Do not enter the student's name, student ID, grades, enrollment status, declared major, disclosed disability, or any other identifying information into Claude unless your institution has a current data agreement that covers this use [verify — consult your institution's data governance office]. FERPA protects educational records; your professional obligation to your advisee is also a relational one. The fact that you are using a third-party AI system to think about a specific identified student is not a neutral act (FERPA guidance; U.S. Department of Education AI report, 2023).

**How to use Claude for advising without violating this boundary:**

Use anonymized or composite scenarios. Instead of "My student Maria Chen is a junior who received an incomplete in Chem 301 and is now considering withdrawing," use "I have an advising appointment tomorrow with a junior student who received an incomplete in a science course and is considering late withdrawal. Help me think through the conversation."

**Worked prompt:**

> I have an advising appointment with a student who has been absent from several recent interactions and is now asking to meet. I am not sure whether the issue is academic difficulty, a personal situation, or disengagement. Help me plan a conversation approach that opens with genuine curiosity rather than concern that might feel like surveillance. Suggest three or four opening questions that invite the student to frame the situation themselves.

Claude is a thought partner here, not an advising record. The judgment in the meeting remains entirely yours.

---

## Workflow 4: Manuscript Feedback and Reviewer-Response Planning

You have a co-authored paper out for revision and must respond to three reviewers. Reviewer 2 is skeptical of your methodology. Reviewer 3 raised three points you genuinely think are wrong. You need to draft a response letter that is substantive, civil, and strategically organized.

**What Claude can do here:** Help you organize the response, draft sections of the reply that explain your rationale, identify the strongest version of each reviewer's concern, and flag where your response is defensive rather than engaged.

**What Claude cannot do:** Read the reviewers' comments (unless you paste them in), know the field's methodological norms, or verify whether your revised analysis actually addresses the concern.

**Worked prompt:**

> I am writing a response letter to peer reviewers for a journal submission. I will paste Reviewer 2's comments below. Help me: (1) summarize what the reviewer is actually asking for — not what they said, but what the underlying concern is; (2) suggest a response structure that acknowledges the concern before defending our approach; (3) draft a paragraph that explains why we used [method] and what it does and does not allow us to claim. I will revise based on our actual data and your draft.

**After Claude drafts:** You verify that the methodological explanation is accurate. You verify that what you claim you changed in the revision is actually changed. You write the final letter yourself from Claude's scaffold.

This is a pattern the book has named elsewhere: Claude as first draft, you as final author.

---

## Workflow 5: Assignment Redesign

You have taught the same major paper assignment for four years. Students are now submitting AI-generated work, and you suspect the assignment design is partly responsible — it asks for product rather than process.

**What Claude can do here:** Serve as an outside reader for your existing assignment, identify the features that make it easy to complete without learning, suggest redesign moves that build in process evidence, and generate alternative assignment formats.

**Worked prompt:**

> I am going to paste an assignment prompt I have used for several years. I want you to read it as if you are a student who would rather use AI than do the intellectual work. Identify every place in the prompt where AI output would satisfy the requirement without demonstrating student learning. Then suggest three redesign moves that build in process evidence or make the core intellectual work harder to outsource.

This is one of the highest-leverage uses of Claude for faculty members: asking it to stress-test the assignment before students do.

---

## The Human Gate for Faculty Work

Every faculty workflow ends at the same gate:

1. **Verification:** Every factual claim — citation, statistic, institutional policy — must be independently checked.
2. **Privacy review:** No identified student information. No student record data. Anonymize before prompting.
3. **Disclosure:** Where your field or publisher requires AI-use disclosure, disclose. COPE's guidance is clear that responsibility for the final text belongs to the human author (COPE, 2023).
4. **Professional judgment:** Claude does not know your institutional norms, your field's unwritten standards, your relationship with a specific student, or your scholarly reputation. You do. The final decision is yours.

**Faculty Verification Checklist:**

- [ ] Sources verified independently against library databases?
- [ ] Student or advisee data minimized or removed?
- [ ] AI use disclosed where required by publisher or institution?
- [ ] Final professional judgment made by a human?
- [ ] Output checked against institutional norms and field standards?

---

## Common Mistakes

**Using Claude output as a citation source.** Claude will produce plausible-sounding references. Treat every citation as unverified until you find it in a database.

**Entering student names or records into Claude.** Even if you trust that Claude does not retain data, the entry itself may constitute a disclosure under FERPA [verify — institutional policy varies]. The safer habit is to never put identifying student information into a public AI tool.

**Assuming Claude knows your field.** Claude has broad knowledge but uneven depth. A hallucinated methodological claim in a grant application or manuscript response damages credibility that took years to build.

**Using grant language Claude generates without verifying funder specifics.** Funder priorities, required language, and program definitions change. Every specific claim about a funder's goals must be verified against current program guidelines [verify — current as of writing].

**Outsourcing the scholarly claim.** There is a difference between using Claude to think through an argument and using Claude to produce an argument you present as your own intellectual contribution. The first is a tool use. The second is a professional integrity question.

---

## Try This

**Exercise 1 — Literature Map with Source Audit**

Choose a research question from a project you are currently working on or teaching. Prompt Claude to sketch the conceptual terrain, major scholars, and key debates. Then take the five most confident-sounding scholar names Claude produces and search for them in your library database. Record: How many exist? How many have published what Claude said they did? What does the gap tell you about how to use this output?

**Exercise 2 — Assignment Stress Test**

Select a major assignment you assign regularly — a paper, a project, a lab report. Paste the prompt into Claude and ask: "Read this as a student who wants to complete this assignment with minimal intellectual effort, possibly using AI tools. Where are the easiest places to shortcut? What is the assignment actually measuring?" Review Claude's response. What would you change?

---

## What Would Change My Mind

This chapter assumes that faculty use of Claude for research-adjacent tasks is legitimate as long as verification and disclosure discipline is maintained. What would change that judgment?

If publishers adopt absolute prohibitions on any AI use in manuscript preparation — not just authorship claims but even drafting assistance — the framing of this chapter would need revision. Current guidance from COPE and major publishers draws the line at authorship claim, not at all assistance (COPE, 2023) [verify — publisher policies vary and change rapidly]. Watch this space.

If institutional AI policies begin restricting faculty use of external AI tools for research activities — on intellectual property, data security, or confidentiality grounds — then the entire workflow menu here would need an institutional-approval gate added. Check your own institution's current AI policy before adopting any of these workflows [verify — institutional policy].

---

## Still Puzzling

Three questions this chapter does not fully resolve:

**Where does AI-assisted grant writing end and undisclosed ghost-writing begin?** Using Claude to improve clarity and structure seems clearly legitimate. Using it to produce the significance section wholesale and submitting it as your scholarly argument feels like a different act — but the line is not yet drawn by most funding agencies. The professional norm is forming in real time.

**How should advising records reflect AI-assisted meeting preparation?** If you use Claude to prepare questions for a difficult advising meeting, does that appear anywhere in the record? Should it? Current guidance does not address this (U.S. Department of Education AI report, 2023).

**What happens when students ask whether their professor uses AI?** The chapter on student use (Chapter 10) addresses student disclosure. If you ask students to disclose, the reciprocal question is whether faculty should disclose their own AI use in course design and research. This is an emerging professional norm, not yet a settled one.

---

## Sources Used

- Anthropic Claude docs. (2024). Available: https://docs.anthropic.com/ [verify — current as of writing]
- Committee on Publication Ethics (COPE). (2023). AI authorship guidance.
- FERPA guidance. U.S. Department of Education.
- NIST AI Risk Management Framework (NIST AI RMF). (2023). National Institute of Standards and Technology.
- U.S. Department of Education. (2023). Artificial intelligence and the future of teaching and learning.
- UNESCO. (2023). Generative AI in education guidance.

---

*Next chapter: Chapter 12 brings everything together. You will build a complete Claude-supported teaching unit from first outcomes to final verification checklist.*
