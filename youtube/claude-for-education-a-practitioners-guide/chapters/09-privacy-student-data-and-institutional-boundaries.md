# Chapter 9 — Privacy, Student Data, and Institutional Boundaries

**Capability built:** Decide what student information should not be put into Claude, and when local institutional policy controls the workflow.

---

## The Scene

It is Thursday afternoon and you have seventeen advising notes open in a browser tab, a stack of accommodation letters from the disability services office, and a student whose writing has suddenly deteriorated in ways that suggest something is wrong at home. You want to do something useful. You open Claude.

Before you type anything, stop.

This chapter is about what happens in the pause before the prompt. Most AI-in-education discussions rush past that pause. This one does not, because the pause is where your students are protected or exposed.

The risk here is not that Claude will do something malicious with student data. The risk is that you will do something routine — something you have done with email or a shared drive before — and not realize that the same action, in an AI context, has different legal exposure, different institutional implications, and different potential for harm. Student data is regulated data. Regulated data has rules. The rules exist before you open the chat window, and they survive after you close it.

---

## What This Chapter Lets You Do

By the end of this chapter you will be able to:

- Apply data minimization: ask Claude for help with the pattern, not the person.
- Anonymize or aggregate student information before any external tool touches it.
- Identify the regulated categories your institution handles and why they require extra caution.
- Run a five-question policy check before using Claude with student-adjacent content.
- Know which tasks should go to your institution's IT, legal, or data-governance team rather than to Claude.

This chapter does not give legal advice. It gives a working method and a set of questions to ask your institution before and during AI adoption.

---

## Core Concepts and Terms

**Data minimization** means giving Claude only the information it needs to assist with the task — nothing more. If you are asking Claude to suggest language for a mid-semester check-in email, it does not need the student's name, course grade, accommodation status, or personal history. It needs the situation type and the tone you want. Minimization is the first line of defense.

**Anonymization** means removing or replacing identifying details before sharing information with an external system. A student's name becomes "Student A." A diagnosis becomes "a documented accommodation." A specific incident date becomes "last month." Anonymization is not perfect protection — highly specific combinations of details can re-identify individuals — but it substantially reduces risk.

**Aggregation** means describing patterns across a group rather than any individual. Instead of pasting an individual student's essay and diagnostic notes into Claude, you describe what you are seeing across a cohort: "I have several students who seem to be confusing X with Y. Help me design a re-teaching activity." Aggregation gives Claude enough to help you without exposing anyone.

**FERPA and its international equivalents** — In the United States, the Family Educational Rights and Privacy Act (FERPA) governs who can see education records and under what conditions. Records covered include grades, transcripts, enrollment information, financial aid data, disciplinary records, and related documents. Similar frameworks govern student data in many other countries: GDPR applies in European jurisdictions, and provincial or national laws govern student privacy in Canada, Australia, and elsewhere. This chapter uses "FERPA-like caution" as shorthand for the general posture these frameworks share: student records belong to the student, not the institution, and sharing them with external parties requires justification.

The practical implication for Claude use is this: pasting identifiable student education records into a third-party AI system is an action that almost certainly requires your institution's explicit approval. That approval may exist. Your institution may have an enterprise agreement with Anthropic that covers this workflow. Or it may not. You do not get to assume it does. You check. [verify — current as of writing]

**Sensitive and regulated categories** that require extra caution include:

- Grades and academic records (FERPA-covered in the U.S.)
- Disability documentation and accommodation letters
- Counseling and mental health records (often separately protected)
- Immigration status documentation
- Financial aid and billing records
- Student conduct and disciplinary records
- Health records (may be covered under HIPAA or institutional policy)
- Records involving minors

Any workflow that involves these categories should not reach an external AI tool without explicit institutional approval. Period.

**Institutional data classification** is the system your institution uses to label how sensitive different data is. Most universities and school districts assign tiers — public data, internal data, confidential data, restricted data — with rules about what can be stored, shared, or processed externally at each tier. Before using Claude in any workflow that involves student information, find out how your institution classifies the data involved. Your IT office, data governance office, or legal counsel can tell you. This is not bureaucratic excess. It is your professional protection as well as your students'.

---

## The Five-Question Policy Check

Before using Claude in a workflow that involves any student information — even something that feels minor — ask five questions. If you cannot answer all five clearly, consult your institution before proceeding.

**1. Is any individual student identifiable in what I am about to share?**
Names, student ID numbers, email addresses, and specific combinations of details can all identify someone. If yes, either anonymize or do not proceed until policy is clear.

**2. Does this involve a regulated category?**
If the content involves grades, accommodations, mental health, discipline, financial aid, immigration, or health, treat it as regulated until told otherwise.

**3. Has my institution approved this tool for this data type?**
Enterprise agreements, data processing agreements, and institutional AI policies may determine what is allowed. "I haven't been told not to" is not institutional approval. [verify — current as of writing]

**4. Is there a way to complete the task without including the sensitive detail?**
Most of the time, there is. Claude can help you draft a communication about a sensitive situation without knowing whose situation it is. Use the minimum data necessary.

**5. Where will the output go, and is that appropriate?**
If Claude generates a draft advising note, a summary of a student's challenges, or a recommended intervention plan, that output itself may be sensitive. Treat it with the same care as the input.

---

## Worked Walkthrough: From Exposure Risk to Safer Practice

Consider the following scenario — realistic, and common.

A high school teacher has three students who are struggling significantly. She wants to use Claude to draft differentiated support plans. She has their names, their current grades, their IEP documentation, and notes from a conversation with the school counselor.

**Version 1 — the unsafe approach:**
The teacher pastes the full set of notes into Claude, including the students' names, grade levels, accommodation details, and counselor notes. Claude produces thoughtful, specific support plans. The teacher saves them in a shared Google Drive folder.

What has happened: Identifiable student education records, including accommodation information potentially covered under both FERPA and disability law, have been processed by an external system without documented institutional approval. The output now lives in a cloud storage system the institution may not have reviewed for this use. The teacher had good intentions and a useful outcome. The risk remains.

**Version 2 — the safer approach:**
The teacher decides what she actually needs Claude for: generating varied scaffolding strategies for students who are struggling with reading comprehension and time management. She describes the pattern, not the people.

Her prompt: "I am working with several high school students who are struggling with complex texts and with managing long-term projects. They have varied needs. Help me draft a set of tiered support strategies — one for a student who needs reading scaffolds, one for a student who needs project-planning structure, one for a student who needs both. These are general templates I will adapt."

Claude provides useful templates. The teacher adapts them using her professional knowledge of the specific students. The identifiable records stayed in the secure systems where they belong. The adaptation judgment stayed with the teacher.

This is data minimization in practice. Claude contributed pattern-level help. The teacher contributed person-level knowledge. No regulated data crossed into an external system.

---

## What Claude Cannot Know — and the Teacher Must Hold

Even with a data-minimization workflow, some things cannot and should not be delegated. When you know a student is in crisis — struggling at home, dealing with housing instability, navigating immigration status, managing a mental health episode — that knowledge came to you through a professional relationship, a system of trust, and sometimes a legal obligation of confidentiality.

Claude does not know that student. Claude cannot judge whether an accommodation plan is appropriate for their actual situation. Claude cannot weigh the relational history between you and that student. Claude does not know what happened last Tuesday in the hallway.

You do. That is not a limitation of AI. That is where teaching lives.

The professional and institutional boundaries around student data are not bureaucratic inconveniences. They encode hard-won understanding of what happens when sensitive information about young people or vulnerable adults is mishandled: discrimination, embarrassment, loss of trust, legal action, and harm to the students the system was supposed to serve (EDUCAUSE, 2024; UNESCO, 2023; U.S. Department of Education, 2023).

---

## The Human Gate

For every workflow involving student-adjacent content, the human gate has two parts.

**Before Claude:** Did I minimize the data? Did I anonymize? Did I check policy? If no to any of these, stop or consult.

**After Claude:** Does this output contain or imply anything sensitive that I should not store, share, or act on without review? AI outputs can sometimes reproduce or infer things you did not consciously include. Read the output before treating it as ready.

The after-review matters especially in cases where Claude produces language about a student situation — even an anonymized one — that feels too specific, too confident, or too definitive. Claude does not have diagnostic authority. If Claude's response to an anonymized scenario sounds like a clinical assessment, treat it as a draft to review, not a conclusion to act on.

---

## Common Mistakes

**Mistake 1: Assuming "I didn't name them" is enough.**
Aggregated details can re-identify students, especially in small classes or small institutions. "The only student in the class who uses a wheelchair and is failing calculus" is identifiable even without a name. Think about combinations, not just individual fields.

**Mistake 2: Treating institutional approval as obvious.**
Some institutions have enterprise AI agreements that cover certain tools for certain data types. Many do not. Verify before you build a workflow that assumes approval. [verify — current as of writing]

**Mistake 3: Storing AI outputs carelessly.**
If Claude generates a summary of a student situation — even an anonymized one — ask whether that output should be stored in your personal notes, in an institutional system, or not at all. Outputs inherit the sensitivity of the information they were derived from.

**Mistake 4: Skipping the check because the task feels minor.**
"I just wanted help phrasing an email" is the beginning of many privacy incidents. The data classification does not change based on how routine the task feels to you. Apply the five-question check even for small tasks.

**Mistake 5: Using Claude as a diagnostic authority.**
Claude can help you generate possible explanations for patterns you observe. It cannot assess, diagnose, or evaluate individual students. Presenting AI-generated language about a specific student as professional judgment is both a pedagogical error and a potential ethical violation.

---

## Try This

**Exercise 1: The Redaction Practice**

Find a realistic support note you have written or a template from your institution. Work through the following steps:

1. Identify every element that could identify a specific student: names, IDs, specific dates, location references, diagnostic labels.
2. Replace each with a placeholder: [Student A], [Fall semester], [documented accommodation], [reported incident].
3. Read the redacted version. Does it still contain enough information for Claude to help with the task you have in mind?
4. If yes: use the redacted version.
5. If no: decide whether to use aggregated language instead, or to complete the task without Claude.

The goal is to develop the habit of reading your prompt before you send it — seeing it as a data-sharing decision, not just a text entry.

**Exercise 2: The Policy Check**

Before next week, find the answers to these three questions for your institution:

1. What is your institution's data classification policy, and how is student record data classified?
2. Does your institution have an approved AI tool list or an enterprise AI agreement, and what does it cover?
3. Who is the correct contact for questions about AI tool use and student data — IT, legal, the data governance office, or another function?

Write the answers down. Put them somewhere you can find them when you are setting up a new workflow. This is not homework for its own sake. It is the professional groundwork that allows you to use AI tools responsibly without second-guessing yourself every time.

---

## What Would Change My Mind

The data-minimization posture in this chapter is deliberately conservative. What would justify loosening it?

Documented, audited enterprise agreements between institutions and AI providers that include specific data processing terms, retention limits, and compliance certifications (for example, FERPA compliance attestation) would support more permissive workflows — but only for the data types and use cases the agreement covers. If your institution has such an agreement and your workflow falls within its scope, that changes the calculus. Talk to your institution's data governance or legal team to know for certain. [verify — current as of writing]

Better tooling — locally hosted models, on-premise AI systems with no external data transmission — would also change the analysis for the highest-sensitivity workflows. Institutions investing in this infrastructure are creating a different risk environment than one where all AI use goes through external cloud services.

What would not change the core principle: good intentions, time pressure, the fact that other teachers are doing it, or the observation that the data is "basically public anyway." None of those are institutional approval.

---

## Still Puzzling

A few genuinely open questions in this space:

**Where is the line between a teaching reflection and an education record?** If a teacher writes anonymized notes about a student's learning patterns as part of their own professional reflection, does that become a regulated record if it is saved in an institutional system? Institutions and legal scholars disagree about edge cases. Your legal counsel is the right resource, not this book.

**How do international frameworks interact?** A teacher at a U.S. institution serving international students, or working in partnership with institutions abroad, may face overlapping regulatory frameworks. GDPR, FERPA, and national laws do not always point in the same direction. The answer is to flag the question to your institution's legal team, not to navigate it alone.

**What happens to AI outputs over time?** If Claude processes an anonymized prompt and generates a document that is then stored in an institutional system, how does that document's status change over time? This is an area where institutional records management and AI governance are still catching up to each other.

---

## Bridge to Chapter 10

Privacy is a constraint that operates before the student ever opens an AI tool. The next chapter turns to what happens when they do: how to design student-facing AI-use policies that are teachable, enforceable, and grounded in learning rather than fear.

The underlying question is the same in both chapters: whose judgment is doing the work? In this chapter, that judgment belongs to you and your institution. In Chapter 10, you are designing conditions for students to develop judgment of their own.

---

## Sources Used

- EDUCAUSE. (2024). AI and privacy resources for higher education. EDUCAUSE.
- UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO.
- U.S. Department of Education. (2023). *Artificial intelligence and the future of teaching and learning*. U.S. Department of Education.
- NIST. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)*. National Institute of Standards and Technology.
- Anthropic. (2024). *Claude for education*. https://www.anthropic.com/news/introducing-claude-for-education [verify — current as of writing]
- Anthropic. (2024). *Privacy policy*. https://www.anthropic.com/legal/privacy [verify — current as of writing]
- FERPA, 20 U.S.C. § 1232g; 34 CFR Part 99. Family Educational Rights and Privacy Act. U.S. Department of Education.
- OECD. (2019). *Recommendation of the Council on Artificial Intelligence*. OECD.
