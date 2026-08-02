# Chapter 11 — Coding with AI: An Introduction


## TL;DR

- The bottleneck was never your lack of syntax.
- The chapter moves through LLM exercises.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The bottleneck was never your lack of syntax. It was your lack of specification.*

---

A high school math teacher — call her Ms. R — had wanted the same thing for fifteen years. An interactive page where a student could drag a slider, change the coefficient *a* in a cubic, and watch the curve bend in real time. She wanted the labels she wanted. She wanted the zoom range she wanted. She did not want Desmos's version of the demo or GeoGebra's version. She wanted *her* version, because the lesson she was teaching Monday had a specific point and she wanted the demo to land that point exactly.

She had three problems. She did not know how to code. The afternoon was Sunday. The lesson was Monday.

What she did know — because she had been thinking about this demo every spring for fifteen years — was exactly what she wanted the page to do. So she opened an AI coding assistant and typed a paragraph.

Not code. A paragraph.

*Single HTML page. Plot y = ax³ + bx² + cx + d. x from −5 to 5. Four sliders for a, b, c, d, each ranging from −5 to 5 in steps of 0.1. When any slider moves, the curve updates. Show the equation across the top in standard form. Mark real roots as dots on the x-axis. Label the y-intercept. White background. Self-contained — no internet required at runtime.*

Three hours later she had a working HTML file she could drop on a USB stick and open on the classroom Chromebook in front of thirty students. The first attempt had a bug — the root detector missed repeated roots. She did not read the code to find it. She described the bug back to the assistant the same way she had described the page: *when a = 0, the cubic becomes a quadratic, and the root display does not update.* The assistant fixed it. She tested five coefficient combinations she had worked out by hand, plus one designed to break things — all zeros. She showed it to the math teacher next door to see if the labels made sense. She saved the prompt history. She closed the laptop.

She did not write a single line of code. She wrote specifications.

This chapter is about what she did, why it worked, why it might have gone badly, and what you would need to do to build something similar for one of your recurring tasks — safely.

---

For most of computing history, the bottleneck to building a tool was knowing how to type the right characters in the right order. Semicolons, brackets, indentation, the exact names of library functions. A person who could not type those characters could not build the tool, regardless of how clearly they understood what it should do.

What changed between 2022 and 2024 is that a particular kind of model — trained on enormous quantities of source code paired with natural-language descriptions — became good enough at translating English-shaped intent into code-shaped output that the *typing-of-the-characters* step could be delegated. The bottleneck moved. It moved to where it actually belongs: to the description of what the tool should do.

This is not a new idea. Brad Myers at Carnegie Mellon and Margaret Burnett at Oregon State, along with collaborators across human-computer interaction research, spent forty years asking how non-programmers could create software for their own purposes. Spreadsheet formulas. Visual programming languages. Programming by example. Web macro recording. Each approach got partway; each had a ceiling. The ceiling was always the same: how do you describe behavior to a computer when you cannot write code? Spreadsheets answered it for grids of numbers. Nothing generalized.

What changed in 2022–2024 is that the answer became *describe it in English*. Not because the question changed — Wing was asking it in 2006, Myers was asking it in 1990 — but because a particular model became good enough at the translation. The forty-year research program did not end. It got a new tool.

The teacher's job in this new arrangement is specification, and specification is not typing. It is thinking. Look at Ms. R's paragraph again. She identified the inputs — four sliders, with ranges and step sizes. She identified the outputs — curve, roots, intercept, equation display. She decomposed the problem into rendering, interaction, and calculation. She anticipated an edge case — what if *a* = 0? She constrained the runtime environment — no internet. Every one of those moves is what Jeannette Wing, in her 2006 *Communications of the ACM* essay "Computational Thinking," called the intellectual work that should survive the syntactic layer: abstraction, decomposition, anticipating failure modes, naming boundaries. The bottleneck for a non-coding teacher building tools with AI is not syntax fluency. It is this thinking. The model can supply the semicolons. It cannot supply the judgment about what the tool should do.

![the bottleneck shift](../images/11-coding-with-ai-an-introduction-fig-01.png)
![the bottleneck shift.](images/11-coding-with-ai-an-introduction-fig-01.png)
*Figure 11.1 — the bottleneck shift.*

---

A specification, in the sense this chapter uses the term, is the document a careful person writes before handing work to someone else. An architect's drawing for a contractor. A recipe for a baker. A wiring diagram for an electrician. It names what is to be built so that the person doing the building does not have to guess.

A working specification for a coding task contains five things. The *intent* — not just the immediate task but the goal it serves. *Make a spreadsheet that flags students whose average has dropped three or more points in the past two weeks*, not *make a spreadsheet*. The *constraints* — format, privacy, environment, library restrictions. The *success criteria* — how you will know the output is correct after the fact; the three inputs you have already computed the expected output for by hand. The *exclusions* — what the tool must not do, must not include, must not touch. And the *output format* — what the deliverable looks like structurally.

A teacher who writes a paragraph containing all five of those things, in any order, in plain English, can now generate working software. A teacher who supplies one or two of them — say, intent and format — will get something that compiles, runs, looks professional, and is wrong in ways they will not immediately see.

That gap is the entire chapter.

![five-component specification diagram](../images/11-coding-with-ai-an-introduction-fig-02.png)
![five-component specification diagram.](images/11-coding-with-ai-an-introduction-fig-02.png)
*Figure 11.2 — five-component specification diagram.*

---

Most teacher coding tasks fall into one of three buckets, and understanding which bucket a task is in tells you how much care the verification needs.

The lowest-stakes bucket is spreadsheet processing. Take a CSV, transform it, output a CSV. Reformat a roster between platforms. Compute summary statistics on quiz scores. Pivot attendance from long to wide format. Produce the list of students who missed three of the last five days that you used to make by hand. If the data is anonymized, the risk is low. The script runs on your laptop, processes a file you already had access to, and produces a file you review before any further use.

The middle bucket is grade management — computing grades from raw scores, applying weighting policies, generating per-student feedback summaries from a rubric. The risk is elevated because grade calculations have consequences and bugs in them are *silent*. A script that systematically misweights one rubric category will produce wrong grades for the entire class with no visible symptom. The verification load is heaviest here.

The highest-stakes bucket is communication tools — per-student mail-merge emails, per-family progress reports, templated messages to families. The risk is highest because the artifact reaches people outside the school and any error becomes visible externally. A misnamed student, a misaddressed parent, a misstated grade in a templated message becomes a relationship problem you inherit.

All three share a shape — structured input, transformation, structured output — that current coding assistants handle most reliably, because there are thousands of examples of each shape in the training data. A common instinct is to automate the most painful task first. The better move is to automate the highest-volume task with the lowest per-instance risk first. That is almost always spreadsheet processing, not grade computation. Build the verification habit on a low-stakes script before the script touches anyone's grade.

| Bucket | Typical task | Who sees the output | Failure mode | Verification load | Recommended entry order |
|---|---|---|---|---|---|
| Spreadsheet processing | Reformat a roster; pivot attendance; flag drops in score | You, on your laptop | Wrong rows in a CSV you review before use | Light — diff against hand-computed test rows | 1 — start here |
| Grade management | Compute weighted grades; generate rubric summaries | You, then students and families downstream | Silent — a systematic miscalculation invisible until grades go out | Heavy — sentinel rows, edge cases, audit every category | 2 — only after the habit is built |
| Communication tools | Per-family mail-merge drafts; templated progress messages | Parents and guardians outside the school | Visible externally — a misnamed student or misstated grade in a sent message | Heaviest — every artifact reviewed individually before send | 3 — last, with a human-in-the-loop draft step |

*Table 11.1 — Risk classification of teacher coding tasks*

---

Here is the hardest conceptual move in the chapter, and the one that professional instinct most resists: you must be able to verify a tool whose source code you cannot read.

The natural move when someone hands you unfamiliar work is to inspect it. A copy-editor reads the manuscript. A nurse reviews the chart. When you receive AI-generated code and look at unfamiliar function names and library imports, the natural conclusion is that the tool is unverifiable. That conclusion is wrong, and understanding why is essential.

You do not verify the *code*. You verify the *behavior*. The behavior is observable. The code is not, to you, legible. So you test what you can see.

Concretely, this is five passes. First, the spec pass: construct three inputs you have already worked out the expected output for by hand, run the script, compare. Second, the edge pass: what if a cell is blank? What if a name has an apostrophe — O'Brien, D'Angelo? What if a score is written as "95%" with the percent sign rather than as the number 95? What if the CSV uses semicolons instead of commas? You do not need to know which case will break. You need to systematically test the cases the spec did not contemplate, because AI-generated code most reliably fails on edges the typical training example did not include. Third, the wrong-input pass: feed it something that should fail. An empty file. A corrupted file. The wrong file altogether. Does it fail with a clear error message, or does it silently produce nonsense? Silent nonsense is the dangerous failure mode. Fourth, the privacy pass: ask the assistant explicit questions. *What data does this script read? What does it write? Does it communicate over a network? Does it create files I did not request?* Document the answers. Run the script with Wi-Fi off and confirm it still works. Fifth, the sentinel pass: insert one row into your test file whose expected output you have hand-written in advance. If the script gets that row wrong, every other row is suspect.

That is the protocol. Slow the first time. Fast by the fifth.

![five-pass verification protocol as a numbered checklist](../images/11-coding-with-ai-an-introduction-fig-03.png)
![five-pass verification protocol as a numbered checklist.](images/11-coding-with-ai-an-introduction-fig-03.png)
*Figure 11.3 — five-pass verification protocol as a numbered checklist.*

The single most-cited study on AI coding assistants is Peng, Kalliamvakou, Cihon, and Demirer's 2023 study of GitHub Copilot. Professional developers using Copilot completed a clearly specified task 55.8% faster than controls. The number is real. It measures *time-to-complete on a clearly specified task*. It does not measure whether the code is secure, maintainable, or correct on inputs not in the test set.

The follow-on evidence on code quality is more sobering. Veracode's 2025 evaluation found roughly 45% of AI-generated code samples contained at least one OWASP Top 10 security flaw. A 2025 large-scale arXiv analysis found vulnerability rates around 16–18% for Python. And a user study cited across this literature found something worth repeating carefully: developers using AI assistants both produced less secure code *and rated their insecure solutions as more secure than controls rated theirs*. The fluency-confidence trap shows up here with the same shape it shows up in every chapter of this book. The tool is fast and fluent and sounds confident. The speed is real. The confidence is uncorrelated with the safety.

What protects teachers in this space is not technical sophistication. It is a few stubborn habits. Anonymize before any AI interaction with student data. Test on synthetic data first. Run the verification protocol. Refuse to deploy a student-facing tool the same day you built it.

---

In February 2025, Andrej Karpathy coined the phrase "vibe coding" in a short post: the practice of building software by describing what you want to a model and accepting what it produces by feel, without much review. The phrase went viral and became, briefly, the cultural framing for AI-assisted development.

A year later, in his 2025 LLM year-in-review, Karpathy was sharper: industry practice had converged not on vibe coding but on spec-driven development — the developer writes the specification, the AI writes the code, the developer reviews against the spec. The retraction is not embarrassing. It is the field correcting itself in roughly twelve months, which is fast. The workflow you are learning here is not the one that briefly went viral. It is the one that survived.

---

Take a concrete specification and walk it through. The task: a script that reads a CSV of students and missing assignments and produces a draft email for each parent, with all student data anonymized before the AI sees any of it.

The bad specification:

> *Make me a script that emails parents about missing assignments.*

The code that comes back will look professional, will run, and will be wrong — because the model has no idea what columns the CSV has, what counts as missing, what tone the emails should use, who sends them, what to do with families whose contact information is blank, whether FERPA permits what it is about to do with the data, or how to handle a name like O'Brien. It will guess on all of these. Some guesses will be invisible to you until they cause a problem.

The good specification:

    INTENT:
      Produce a per-student draft email summarizing missing assignments,
      ready for me to review and send. The script does not send email.

    INPUT:
      A CSV named "missing.csv" with these columns:
        student_pseudonym  — a code I have assigned (NOT a real name)
        parent_pseudonym   — a code for the parent (NOT a real name)
        assignment_name    — string
        due_date           — YYYY-MM-DD
        days_overdue       — integer

    OUTPUT:
      A single file "drafts.txt". One block per student. Each block:
        To: [parent_pseudonym]
        Re: missing work for [student_pseudonym]
        Body: warm, factual, three sentences max, lists assignments
              with due dates. No grade information. No
              characterization of the student's character or effort.
      Blocks separated by a line of dashes.

    CONSTRAINTS:
      - No network calls. Script runs entirely locally.
      - No external libraries beyond Python standard library.
      - Skip any student whose days_overdue < 3.
      - If parent_pseudonym is blank, skip that row and log it to
        a separate file "missing_contacts.txt".
      - Handle apostrophes and accented characters in pseudonyms.
      - Trim leading and trailing whitespace from every CSV field.

    SUCCESS CRITERIA:
      Tested against my hand-prepared test file with 5 rows, the
      output contains exactly 3 blocks (2 should be skipped: 1 below
      threshold, 1 missing parent code), and missing_contacts.txt
      contains exactly 1 row.

    EXCLUSIONS:
      - Do NOT include grade letters or numeric scores.
      - Do NOT include real names. The CSV contains pseudonyms only.
      - Do NOT call any AI service or any external API.
      - Do NOT impute missing data.

That specification contains all five components: intent, constraints, success criteria, exclusions, output format. It anchors anonymization at the spec level — pseudonyms only, noted twice. It anticipates edge cases before the script breaks on O'Brien.

The assistant produces about thirty lines of Python. You do not read them. You run the script on your test file. You count the blocks. You verify the sentinel row matches your hand-written draft. You run the Wi-Fi-off test. You ask the assistant what the script reads and writes and confirm the answers. The script passes. The draft emails wait in a text file for your review before anything reaches a family.

What made the script safe was not reading the code. It was writing the specification before the code existed, and testing the behavior after.

![before/after specification comparison](../images/11-coding-with-ai-an-introduction-fig-04.png)
![before/after specification comparison.](images/11-coding-with-ai-an-introduction-fig-04.png)
*Figure 11.4 — before/after specification comparison.*

---

The teacher who deploys a tool with students is responsible for the tool's behavior, regardless of who wrote the code. The AI did not deploy the tool. You did. Accountability runs to the deployer.

This is not a novel doctrine — it is standard professional responsibility in software engineering applied to the teaching context. FERPA does not distinguish between a script you wrote and a script an AI wrote. If the script touches identifiable student information, FERPA's restrictions apply equally to both. The specific criteria vary by district and state interpretation and are referred to district counsel rather than asserted here. The principle is not: the teacher who deploys owns the deployment.

The practical consequences follow from that principle. Never paste real student data into a cloud coding assistant. Anonymize first. Test on synthetic data before touching real data. Any script that crosses district systems — pulling from the student information system, pushing to the gradebook — is not personal automation; it is district-adjacent infrastructure. Run it past IT. If students interact with a teacher-built artifact, the disclosure principles from earlier chapters apply. Keep a copy of the specification. Spec plus generated code, dated, with the assistant noted. The equivalent of keeping a lesson plan: a record of what was deployed and why.

---

A common misconception deserves a direct answer: *if AI can write the code, why teach computational thinking at all?*

Wing's 2006 answer pre-dates the question and survives it. Computational thinking is what you need to *specify a problem to a computer at all* — whether the computer's translator is a compiler, a programmer-colleague, or a generative model. Decomposition is unchanged. Abstraction is unchanged. The discipline of imagining what could go wrong is unchanged. What changed is which step takes the most time.

Look at Ms. R's polynomial specification again. She identified the inputs and their ranges. She identified the outputs and their labels. She decomposed rendering, interaction, and calculation. She abstracted from the specific cubic to a parameterized polynomial form. She anticipated the edge case where the leading coefficient vanishes. She constrained the runtime environment. A teacher who can do this for a polynomial demo can do it for a missing-assignments script. A teacher who cannot do it cannot. The bottleneck for non-coding teachers building tools with AI is not syntax. It is the thinking Wing named in 2006, which is the same thinking this chapter has been calling specification all along.

![Wing's computational thinking moves mapped onto Ms](../images/11-coding-with-ai-an-introduction-fig-05.png)
![Wing's computational thinking moves mapped onto Ms.](images/11-coding-with-ai-an-introduction-fig-05.png)
*Figure 11.5 — Wing's computational thinking moves mapped onto Ms.*

---

Two things I need to be honest about before closing.

The first is the security evidence. The numbers from Veracode and the arXiv analysis are real findings on general AI-generated code. What they do not establish is a defect rate specifically for the narrow class of locally-run spreadsheet processing and template-generation scripts that most teachers will actually build. The verification protocol in this chapter is designed to catch behavioral defects — wrong output, silent failure, incorrect handling of edge cases. Whether it would catch *security* defects in a locally-run Python script handling anonymized data is a different question, and the honest answer is that no study has measured this specifically for teacher use cases. The protocol is the best available tool. It is not a guarantee.

The second is maintenance. This chapter says nothing useful about what happens to a teacher-built script when the teacher changes schools, retires, or simply forgets what the script does. The public literature is essentially silent on this. A specification kept with the code is better than a script in a folder with no documentation. It is not a solved problem.

---

## LLM exercises

**Exercise 1 — Write a workflow automation spec.** Pick one recurring spreadsheet task you do by hand each week. Using the five-component template below, write a 100–200-word specification for it. Do not yet generate code. Trade the spec with a colleague, or paste it into a fresh AI chat and ask the assistant to describe back what it would build. If their description does not match what you want, the spec is not yet a spec.

    WORKFLOW AUTOMATION SPECIFICATION
    INTENT:        [What the script is for. Why you want it.]
    INPUT:         [Filename, columns, types, where it comes from.]
    OUTPUT:        [Filename, structure, format. What goes in it.]
    CONSTRAINTS:   [No network calls / library limits / runtime /
                    locale / special characters / row volume.]
    SUCCESS CRITERIA:
                   [How you'll know it worked. 3 hand-computed test cases.]
    EXCLUSIONS:    [What it must NOT do. What it must NOT include.
                    What data it must NOT touch.]

**Exercise 2 — Verify against three edge cases.** Take the spec from Exercise 1 and an AI-generated implementation of it. Design three edge cases the spec does not explicitly handle — a blank field, a special character (apostrophe, accent, em-dash), an unusually large input. For each, predict the output *before* you run, then run and compare. Where prediction diverges from reality, those are the spec's missing clauses. Update the spec. Regenerate. Test again.

**Exercise 3 — Design a deployment checklist for a student-facing tool.** Imagine you have built an interactive practice tool that students will use during a lesson. Write a one-page checklist covering: anonymization (what student data, if any, the tool touches); environment (device, browser, whether internet is required); privacy surface (does the tool phone home, log anything, require accounts); failure mode (what happens if it crashes mid-lesson); documentation (what you would save so a colleague could re-deploy it next year); and disclosure (what you would tell students about the tool's origin). Walk through the checklist with a colleague.

---

## References

- Karpathy, A. (2025, February). "Vibe coding" [X post]. x.com/karpathy/status/1886192184808149383
- Karpathy, A. (2025, December). *2025 LLM Year in Review*. karpathy.bearblog.dev/year-in-review-2025/
- Ko, A. J. et al. (2011). "The State of the Art in End-User Software Engineering." *ACM Computing Surveys*, 43(3), Article 21. DOI 10.1145/1922649.1922658
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot." arXiv:2302.06590
- Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). "Do Users Write More Insecure Code with AI Assistants?" *Proceedings of ACM CCS 2023*. arXiv:2211.03622
- U.S. Department of Education. *Family Educational Rights and Privacy Act (FERPA)*. studentprivacy.ed.gov/ferpa
- Veracode. (2025). *2025 GenAI Code Security Report*. veracode.com/resources/analyst-reports/2025-genai-code-security-report/
- Wing, J. M. (2006). "Computational Thinking." *Communications of the ACM*, 49(3), 33–35. DOI 10.1145/1118178.1118215
- "Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis." (2025). arXiv:2510.26103

---

##  AI Wayback Machine
Hopper invented the first compiler (A-0, 1952) and wrote much of what became COBOL. Her teaching ethos — *the most dangerous phrase in the language is we have always done it that way* — and her habit of explaining computing to non-programmers in their own vocabulary is the disposition this chapter asks teachers to bring to coding with AI. A teacher learning to code is doing what Hopper spent her career doing: insisting that the machine be made legible to the person who needs it, not the other way around.

![Grace Hopper, 1906-1992. AI-generated portrait based on a public domain photograph.](../images/grace-hopper.jpg)
*Grace Hopper, 1906-1992. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![Grace Hopper](../images/grace-hopper-w8h.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Grace Hopper, and how does their work connect to the ideas in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or thinking.
```

→ Search **"Grace Hopper"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Hopper's framework to a specific scenario in this chapter — what gets surfaced that the chapter's prose left implicit?
- Ask about the critics of Hopper's work and which criticisms still bite today.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 11.1 — the bottleneck shift.

Create a standalone D3 v7 HTML file for a concept map titled "the bottleneck shift.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-coding-with-ai-an-introduction-fig-01.html`

---

### Figure 11.2 — five-component specification diagram.

Create a standalone D3 v7 HTML file for a checklist or diagnostic card titled "five-component specification diagram.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-coding-with-ai-an-introduction-fig-02.html`

---

### Figure 11.3 — five-pass verification protocol as a numbered checklist.

Create a standalone D3 v7 HTML file for a phase-gate workflow diagram titled "five-pass verification protocol as a numbered checklist.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-coding-with-ai-an-introduction-fig-03.html`

---

### Figure 11.4 — before/after specification comparison.

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "before/after specification comparison.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-coding-with-ai-an-introduction-fig-04.html`

---

### Figure 11.5 — Wing's computational thinking moves mapped onto Ms.

Create a standalone D3 v7 HTML file for a concept map titled "Wing's computational thinking moves mapped onto Ms.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-coding-with-ai-an-introduction-fig-05.html`
