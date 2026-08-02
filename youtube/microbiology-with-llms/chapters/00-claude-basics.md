# Chapter 00 — Claude Basics

*A large language model is a tool. Tools have things they are good at, things they are bad at, and ways of being held that matter.*

## The question before the answer

You are about to read a microbiology textbook that asks you to do something most textbooks don't. At the end of every chapter — and at occasional moments inside chapters — the book invites you to work through a problem with a large language model. The LLM is not the teacher. The LLM is not the textbook. The LLM is the third party in a conversation between you and the material.

This chapter is about how to do that well.

The default LLM the book uses is **Claude** (claude.ai). The prompts also work, with minor modification, in ChatGPT (GPT-4o and later), Gemini, Llama, and other large language models. If you have a strong preference, use it. The book does not require a specific tool; it requires that you bring some tool to the conversation.

But I want to be honest about one thing before we start. LLMs are not search engines. They are not encyclopedias. They are not infallible reference works. They are probabilistic text generators that have been trained on enormous corpora and tuned to be helpful, and they are wrong, sometimes, in interesting ways. Using them well means using their strengths (synthesizing, comparing, generating examples, explaining alternative views) while staying skeptical of their weaknesses (specific numbers, recent events, edge-case clinical details). The point of the LLM exercises in this book is not to delegate your thinking to a machine. It is to use the machine as a partner in your thinking — one that gets challenged, corrected, and pressed for evidence.

## Learning objectives

By the end of this chapter, you will be able to:

1. Explain why a microbiology student should bother using an LLM at all.
2. Distinguish the two types of LLM prompts in this book (Dig Deeper and chapter-end LLM Exercises) and decide when to use each.
3. Choose the right tool (Claude chat, Claude Project, Claude Code, Cowork) for a given task.
4. Recognize the failure modes of LLMs in microbiology and adapt your use accordingly.
5. Carry useful LLM output forward across multiple chapters of the book.

Prerequisites: None except access to an LLM and curiosity.

## Why this book uses LLMs

Microbiology is unusually rich territory for LLM-assisted learning. Several reasons.

**The vocabulary is dense and Latin-heavy.** A typical introductory microbiology lecture introduces fifty new terms, most of them with Greek or Latin etymologies, many of them species names that are themselves sentences in Latin. An LLM is exceptionally good at explaining etymologies, breaking down terminology, and offering memory aids. "What does *Staphylococcus aureus* mean, and what does each part of the name tell me about the organism?" is a question an LLM answers in seconds, with substantially correct etymology and clinical context.

**The clinical reasoning is pattern-based.** Differential diagnosis — "what could this patient have, given these symptoms?" — is one of the things LLMs are surprisingly good at. They have been trained on enormous medical corpora; they have read thousands of case presentations; they can reason about probabilities the way a clinician does, with the caveat that they sometimes confabulate plausible-sounding details. Practicing differential diagnosis with an LLM as a sparring partner is an effective way to build clinical reasoning skill — provided you stay critical.

**The mechanisms are explainable but unfamiliar.** Most microbiology, at the molecular level, is biochemistry that happens at scales students do not have intuition for. LLMs are good at producing analogies and at explaining mechanisms in plain language. Bad explanations can be probed; the LLM can be asked to try again with different framing.

**The literature is open.** Most landmark microbiology papers — Pasteur, Koch, Watson and Crick, Avery-MacLeod-McCarty, Mitchell, Margulis, Marshall — are part of the cultural record the LLMs have ingested. You can have a substantive conversation with an LLM about the experimental logic of the Meselson-Stahl experiment in a way you could not have about, say, an obscure proprietary topic. The history of the field is well-represented in the training data.

**The field changes fast.** Antibiotic resistance, vaccine updates, emerging diseases, microbiome research — these all move on a timescale faster than textbook revision. LLMs are not perfect on recent events (their training data has cutoffs, and they sometimes claim more confidence about current state than they should), but they are usually closer to current than a printed textbook. With appropriate verification, they can update you on what has changed since this book was written.

What LLMs are *not* good at, in microbiology:

- **Specific numbers and dates** they cannot verify. An LLM may tell you, plausibly, that the mortality rate of untreated bacterial meningitis is 95%, or 98%, or 99%, and the number it gives is not the result of looking up a citation. Verify any specific number that matters.
- **Drug dosing**. Do not get drug doses from an LLM. Use a reference (UpToDate, IDSA guidelines, hospital formulary).
- **Recent outbreaks** post-training. Use WHO, CDC, ECDC, ProMED.
- **Specific patient management** for actual patients. Use a clinician, a current guideline, and a clinical pharmacist.

The LLM is good for learning, generating hypotheses, exploring ideas, and synthesizing. It is bad as a final authority for clinical decisions.

## Two kinds of prompts in this book

You will find two kinds of LLM-related content embedded in the chapters.

### Dig Deeper prompts

These are inline invitations. When the chapter introduces a concept that has more depth than there is space to explore, a Dig Deeper prompt appears after the paragraph. The format is:

> ↳ **Dig Deeper — [Concept name]**
>
> *One sentence about what this explores and why it's worth following.*
>
> **Prompt:**
> > [The prompt text, ready to paste into Claude.]
>
> **What to do with the output:** [One sentence.]

Dig Deeper prompts are **optional**. They do not feed the chapter-end LLM Exercise. They do not feed a final project. Skipping them costs you nothing. Following them rewards curiosity. The point is to give you a head start when something in the chapter catches your attention — a topic the book mentioned but did not unpack, a name you want to know more about, an analogy you want to test.

You will not see Dig Deeper prompts in the draft chapters of this book yet; they are planned for the revision pass. The chapter-end LLM Exercises are already present in every chapter.

### Chapter-end LLM Exercises

At the end of every chapter, you will find a block titled **LLM exercises**. Each block contains five reflective prompts designed for you to do with an LLM. They are not multiple-choice questions. They are not one-shot lookups. They are *thinking exercises with the LLM as your partner.*

The format of a typical exercise:

> 1. **Title of the exercise.** Brief setup. The actual question for the LLM. A line about what to do with the answer.

Some of the exercises ask the LLM to generate something (a differential diagnosis, an experimental design, a hypothesis). Some ask the LLM to walk through a mechanism. Some ask the LLM to play a role (a skeptical reviewer, a senior clinician, a defender of a hypothesis). Some ask you to compare the LLM's answer to a known correct answer in the chapter or in a primary source.

The exercises are deliberately open-ended. There is no answer key. The point is not to get the right answer; the point is to think through the problem with the LLM and to develop habits of using the tool well.

### Running projects (optional)

If you are reading this book in a course, your instructor may have selected a **running project** — a build that threads through every chapter, with a deliverable at the end of each chapter. The running project options are described in a separate document accompanying this book. If you are reading the book independently and would like to choose a project, see that document; it offers 3–5 options.

The running project is the most substantial work you will do with the LLM. By the end of the book, you will have built a real artifact — a clinical case-study library, a diagnostic decision-tree, a teaching workbook, a literature-review pipeline, depending on which project you choose.

The running project does not have to be done. The chapter exercises and Dig Deeper prompts stand on their own. The running project is an optional intensifier for students who want to go deeper.

## Choosing the right tool

Anthropic's Claude is available in several modes. Different modes are suited to different kinds of work.

**Claude chat (claude.ai)** is the default. Open a conversation in your browser, paste a prompt, get an answer. Use this for most of the LLM Exercises and Dig Deeper prompts. A single chat thread keeps context across turns — you can ask a follow-up question and Claude will remember what you were discussing.

A chat is good when:
- The exercise is self-contained and will be done in one sitting.
- You want to interrogate an answer ("what did you mean by that?" "explain that again").
- The output is short prose or a list.

**Claude Projects** is the right tool when you are returning to the same build across many sessions. A Project has persistent context: documents you upload, system instructions you set, and conversation history that the model can refer back to. For a running project that develops across all 26 chapters, a Project is the right home.

Use Claude Projects when:
- The work spans more than one sitting.
- You need the LLM to remember decisions you made in a previous session.
- You want a shared workspace for documents you keep returning to (e.g., a glossary, a case-study template, a microbe-profile database).

**Claude Code (claude.com/code)** is the right tool when the work involves actual code or file manipulation — writing Python scripts, organizing folders of files, building a small database, generating a static website. Some of the running project options involve technical components that benefit from Code.

Use Claude Code when:
- The output is runnable code.
- You need to work with files in a folder structure.
- You want the LLM to test what it has written before declaring it done.

**Cowork** (Anthropic's beta desktop tool) lets the LLM read and write files on your computer through your Documents folder. Useful for projects where the artifact is a folder of files (case studies, notes, structured documents) you want to keep on your computer.

Use Cowork when:
- The project produces a folder of files (rather than a single output).
- You want the LLM to organize, edit, and update files across sessions.
- You prefer working in your local file system rather than a web interface.

A reasonable default: **Claude chat for the chapter exercises, Claude Projects for the running project if you choose one, Claude Code if your project involves code, Cowork if your project involves file management.**

If you are using a different LLM (ChatGPT, Gemini), the equivalents are roughly:

| Claude | ChatGPT | Gemini |
|---|---|---|
| Claude chat | ChatGPT chat | Gemini chat |
| Claude Projects | Custom GPTs | Gems |
| Claude Code | Various code-focused interfaces | Code Interpreter / Colab |
| Cowork | (No direct equivalent; some via plugins) | Google Workspace integration |

The chapter exercises will work in any of these. The exact phrasing of prompts is sometimes optimized for Claude but rarely fails on another model.

## How to use the prompts

A few principles that have come out of using LLMs to learn things.

**Read the prompt before pasting it.** The prompts in this book are written to be informative on their own. The setup tells you what concept the prompt is probing. The "what to do with the output" line tells you what to look for. Skipping these and going straight to the LLM means you are spending the LLM's effort on something you may not even want.

**Adapt for your domain.** The chapter exercises are written for the typical reader, but the typical reader is a fiction. If you are pre-med, you will read clinical scenarios closer to your eventual practice; if you are a research-track student, you will care more about experimental design. Most exercises can be adapted by replacing a generic scenario with one closer to your interest. The LLM does not mind.

**Iterate.** The first answer is usually not the best answer. If the LLM gives you a vague or generic response, ask for specifics. "Give me three concrete examples." "Pick one and walk me through it step by step." "What evidence would distinguish this from the alternatives?" The follow-up questions are where the learning happens.

**Push back.** If the LLM says something you think is wrong, say so. "I don't think that's right — can you check?" Sometimes the LLM will defend its answer with citations and reasoning; sometimes it will correct itself. The model is generally helpful about being challenged.

**Verify the specific.** When the LLM gives you a number, a date, a dose, a citation — and the specific thing matters — look it up. The LLM is often right, but the failure mode of LLMs is confident wrongness, and you cannot tell from the response which is which.

**Don't ask the LLM to do your thinking.** If the chapter asks you to design a hypothetical experiment, do not ask the LLM to design it for you. Ask the LLM to react to your design, to point out flaws, to suggest improvements. The thinking is yours; the LLM is a sounding board.

**Carry output forward.** Some chapter exercises build on previous ones (particularly within a running project). Keep the LLM's earlier output — in a Project context, in a notes file, in your head. When you start a new exercise, give the LLM the context it needs from earlier chapters.

## Worked example

The most accessible chapter-end LLM Exercise in this book is in Chapter 1. Let me walk through it.

The exercise is:

> **Taxonomy stress-test.** Give the LLM a list of ten organisms — some clearly bacterial, some archaeal, some viral, some prion. Ask it to classify each on the three-domain tree (or off it). Where does it hesitate? Where does it get it wrong? What questions does it raise that the chapter doesn't answer?

Here is how you might run it.

**Step 1**: Open Claude chat. Paste:

> I'd like you to help me practice taxonomic classification. I'll give you ten organisms. For each, tell me which of the three domains (Bacteria, Archaea, Eukarya) it belongs to, or whether it doesn't belong to any of them. For each placement, give a one-sentence reason.
>
> The organisms are:
> 1. *Escherichia coli*
> 2. *Methanobrevibacter smithii*
> 3. *Saccharomyces cerevisiae*
> 4. Influenza A virus
> 5. Variola virus (smallpox)
> 6. PrP^Sc prion
> 7. *Plasmodium falciparum*
> 8. *Mycobacterium tuberculosis*
> 9. *Halobacterium salinarum*
> 10. *Trichuris trichiura* (whipworm)

**Step 2**: Read Claude's answer. You should see the bacteria placed in Bacteria, the archaea in Archaea, the eukaryotes in Eukarya, and the viruses and prion noted as not on the tree. *Plasmodium* is a eukaryote (protist). *Trichuris* is a eukaryote (animal — but still in microbiology because of microscopic eggs, as discussed in Chapter 5).

**Step 3**: Now press for the hard cases. Ask:

> What would change about your classification if I told you that *Halobacterium salinarum* lives in 25% salt water — does that affect its domain placement, or is the placement based on something else?

The LLM should respond that the placement is based on its 16S rRNA sequence (it's an archaeon despite the bacterial-sounding genus name; the genus name predates the discovery of Archaea). If it gives a less precise answer, push for the molecular basis.

**Step 4**: Push on a genuinely hard case. Ask:

> What about a giant virus like mimivirus, with a genome larger than some bacteria? Where does it go?

The LLM should acknowledge that this is unsettled and that some researchers argue giant viruses deserve their own domain (sometimes called TRUC or "fourth domain"). A weaker answer might just place them off the tree without acknowledging the controversy. The point of this question is to see if the LLM holds onto certainty when it should hold ambiguity.

**Step 5**: Bring in the chapter material. Ask:

> Chapter 1 mentions that no archaeon has been confirmed as a human pathogen. Does your list include any archaea that have been *suggested* as possible pathogens?

The LLM may name candidates (*Methanobrevibacter* species have been investigated in periodontal disease and other conditions). Compare to the chapter's claim, which is that nothing has been confirmed. The LLM and the chapter agree on the basic fact while exploring the texture differently.

**Step 6**: Write down what you learned. You ran a few minutes of conversation. The chapter said archaea live in human gut but don't appear to cause disease. You verified that the LLM's domain assignments matched the chapter's framework. You learned that *Halobacterium*'s name is historically misleading. You learned that some researchers want a separate domain for giant viruses. You noticed that the LLM hedges appropriately on giant viruses but might have been overconfident if you hadn't asked.

That's how a chapter exercise is supposed to work. You don't memorize the answer. You exercise the reasoning.

A weak version of the same exercise would be: paste the list of ten organisms, copy down the LLM's response, and move on. You would have learned nothing the chapter didn't already teach you. The reasoning happens in the follow-up, not the first reply.

## Claude's limitations in microbiology

A few concrete failure modes you will hit. Knowing them in advance helps.

**Specific drug doses are unreliable.** "What is the dose of vancomycin for adult bacterial meningitis?" — the LLM will give you a number that is plausible but you should verify against a current reference. Doses can be wrong; weight-adjusted dosing can be miscomputed; renal-adjustment guidance can be slightly off. For learning, the LLM's dose is fine. For a real patient, look it up.

**Recent outbreaks may be outdated.** If you ask about the current status of mpox or an emerging *Candida auris* outbreak, the LLM's answer reflects its training cutoff. For current numbers, use WHO, CDC, or ECDC.

**Resistance patterns are local.** "What is the resistance rate of *E. coli* to TMP-SMX?" — the answer depends on your country, your hospital, your time period. The LLM may give you a global average that is not relevant to your situation. Use local antibiogram data.

**Confidently wrong about uncommon organisms.** Ask about a well-studied organism (*S. aureus*, *E. coli*, HIV) and the LLM is usually accurate. Ask about an unusual organism (*Ehrlichia chaffeensis*, *Bartonella henselae*, *Capnocytophaga canimorsus*) and the LLM may invent plausible-sounding details. Cross-check against a clinical reference.

**Confabulated citations.** If you ask the LLM for a reference, the citation it gives may be real, partially real (a real author, plausible but nonexistent paper), or entirely invented. Always verify citations before quoting them. This is one of the most persistent LLM failure modes and the most likely to embarrass you.

**Synthesized but not necessarily accurate clinical pathways.** When you ask about a workup or treatment sequence, the LLM produces a coherent-sounding pathway that may be approximately right but may also have specific steps in the wrong order. Use it as a draft, not a final.

The pattern across these failures: **the LLM is overconfident about specifics it cannot verify**. When the specifics matter, verify. When the gist matters, the LLM is usually right.

## Quick-reference card

| Question | Best tool | Why |
|---|---|---|
| "Explain a concept I just read" | Claude chat | Fast, conversational, can probe |
| "Generate a differential diagnosis" | Claude chat | Pattern matching; you must verify |
| "Help me design an experiment" | Claude chat or Project | Iterate over multiple turns |
| "Building a running project across chapters" | Claude Project | Persistent context across sessions |
| "Generate code or data analysis" | Claude Code | Code-focused interface |
| "Manage a folder of files" | Cowork | Local file system access |
| "Look up the current dose of vancomycin" | UpToDate / IDSA guideline | Drug doses, not LLM |
| "Find out the latest CDC recommendation" | CDC website | LLM training has cutoffs |
| "Compare two textbook treatments of a topic" | Claude chat | Synthesis is an LLM strength |

## What the chapter is really about

The LLM is a thinking partner. It is good when you treat it as a collaborator — someone you converse with, push back against, and use for the parts of the work it is good at while doing the rest yourself. It is bad when you treat it as an oracle — a black box you ask for an answer and accept whatever comes out.

This book's premise is that microbiology rewards the first approach. The material is complex enough that an LLM partner accelerates your learning; the stakes are high enough (the eventual application is medicine and public health) that verifying matters. The exercises throughout the book are designed to develop both habits simultaneously: use the LLM, and stay critical of the output.

A reasonable measure of success: by the end of the book, you should be able to read a microbiology paper, generate a clinical hypothesis, run it past an LLM for synthesis and critique, identify the LLM's weaknesses, verify the specifics that matter, and reach a conclusion that is yours. The LLM is in the pipeline, but the conclusion is still yours.

## Still puzzling

I do not fully understand how to teach LLM use as a generalizable skill. The exercises in this book teach prompting in the context of microbiology specifically. Whether those skills transfer to using LLMs in a different domain (programming, writing, history, law) is unclear. Some of the patterns generalize — verify specifics, push for evidence, iterate, treat as a partner. Some are domain-specific. I suspect each field's relationship with LLM tooling will develop its own conventions over the next decade, and what looks generic now will look domain-specific in retrospect.

## What would change my mind

If LLM performance on specific microbiology tasks (dose lookup, current outbreak reporting, citation generation) improves to the point where the failure modes I described no longer reliably occur, the verification recommendations in this chapter would need to be relaxed. Each new generation of models has reduced the rate of confabulation; future generations may eliminate it for routine queries. As of this writing, the failure modes are real and frequent enough to warrant caution. `[verify: 2026 state of LLM reliability for clinical reference]`

## LLM exercises

These exercises are meta — they ask you to develop your own habits of LLM use rather than learn microbiology content.

1. **Catch a hallucination.** Pick a topic you know well (it doesn't have to be microbiology). Ask the LLM a question with a specific factual answer you can verify. Probe until you find an error. Then ask the LLM how it could have known its answer was wrong. The goal is to see the failure mode firsthand.
2. **Iterate from vague to useful.** Ask the LLM a deliberately vague question ("Tell me about bacterial meningitis"). Note the response. Then ask three increasingly specific follow-ups, each constraining the answer. Compare the first response to the final one. The skill is learning to move from open to closed.
3. **The role-play test.** Ask the LLM to argue, in turn, for and against a contestable position (say, "antibiotics should be available without a prescription"). Note whether the two arguments are equally strong. If the LLM is much stronger on one side, that may tell you something about its training. The skill is recognizing that LLMs can be coaxed into both sides.
4. **The "explain like I'm five" test.** Ask the LLM to explain a concept in increasingly simple terms. At each step, ask the LLM to check whether anything important was lost. The skill is seeing what gets simplified out — and whether the simplifications are reasonable.
5. **Set up your toolkit.** Before starting Chapter 1, decide where you will keep notes from chapter exercises, whether you will use a Claude Project, and whether you will set up Cowork. Spend 20 minutes establishing your workflow. The chapter exercises will be substantially more useful if you have an organized place to keep their outputs.

## References

(This chapter is about meta-skills rather than scientific content. The references would be guides to LLM use rather than primary scientific literature. Anthropic's documentation at docs.anthropic.com and the prompt engineering guides at prompt engineering documentation are the standard starting points for Claude specifically.)
---

## LLM Exercise — Chapter 00: Claude Basics (Microbe Profile Database Project)

**Project:** Microbe Profile Database — across the semester, build a structured database of ~40–60 microbe profiles you can search, study from, and reference. Each chapter adds rows (new microbes) and/or columns (new fields) to the database.
**What you're building this chapter:** the database schema — pick the format, define the fields every entry will share, choose the tool path.
**Tool:** **Cowork** (folder of markdown files with YAML frontmatter) OR **Claude Code** (SQLite database + query interface). The choice in this chapter shapes the project.

---

**The Prompt:**

```
I'm starting a semester-long Microbe Profile Database project. By
Chapter 26 I'll have ~40–60 microbe entries with consistent fields,
plus richer cross-linking accumulated across chapters. The database
should be searchable, study-able, and exportable.

Help me set it up. Ask me ONE question at a time, waiting for my
answer.

1. Format choice. Three plausible options:
   (a) **Markdown files with YAML frontmatter** — one file per
       microbe, frontmatter holds structured fields, body holds
       free-form notes. Searchable with grep/ripgrep. Reads like
       documentation. Easy to extend. (Recommended for most students.)
   (b) **CSV or Excel spreadsheet** — one row per microbe. Best
       for tabular comparison. Limited to flat fields.
   (c) **SQLite database** — full SQL queries. Most powerful for
       cross-microbe analysis. Requires comfort with Claude Code.

   Pick one. Most students should pick (a).

2. Tool path. If you picked (a) → Cowork manages the folder of
   files; Claude chat helps you write each entry. If (b) →
   spreadsheet + Claude chat. If (c) → Claude Code for the SQL
   layer.

3. The fields. Every entry will have these "core" fields,
   regardless of microbe type:
   - Name (binomial, e.g., *Staphylococcus aureus*)
   - Domain/kingdom (Bacteria / Archaea / Eukarya / Virus / Prion)
   - Gram or class (Gram-positive / Gram-negative / N/A)
   - Cell type (cocci / bacilli / spirilla / unicellular eukaryote
     / multicellular / viral capsid type / N/A)
   - Oxygen requirement (obligate aerobe / obligate anaerobe /
     facultative / microaerophilic / N/A)
   - Primary clinical relevance (one sentence — what disease(s)
     it causes, or what role it plays in the microbial world)
   - Discovery (year and discoverer, where known)
   - Genome size (approx. base pairs)
   - References (citations or links)

   Later chapters will add MORE fields:
   - Virulence factors (Ch 15)
   - Resistance patterns (Ch 14)
   - Immune-evasion mechanisms (Ch 17–18)
   - Diagnostic tests (Ch 20)
   - Transmission/epidemiology (Ch 16)

   For now, lock the 9 core fields above. Confirm or adjust.

4. The naming convention. Each entry's filename will be the
   binomial name with underscores: `Staphylococcus_aureus.md` or
   `staphylococcus_aureus.md`. Decide one convention and stick to
   it.

5. The cross-linking convention. When one entry references another,
   how is that linked? In Markdown: `[[E_coli]]` or `[*E. coli*](
   E_coli.md)`. Decide.

After all five answers, output:
- A **schema document** (one page) that defines every field, with
  example values for each.
- A **template entry** (a blank entry with all fields, ready to
  fill in for any new microbe).
- A **starter directory structure**:
   /microbes/
     /bacteria/
       Staphylococcus_aureus.md
       ...
     /archaea/
     /eukaryotes/
     /viruses/
     /prions/
     schema.md
     template.md
     README.md
- Five sample queries you'd want to be able to run by Ch 26 (e.g.,
  "all Gram-positive cocci in skin infections"; "all obligate
  anaerobes"; "all microbes with known antibiotic resistance"). The
  query design tests whether the schema is rich enough.
```

---

**What this produces:** A schema document + template entry + directory structure. The schema is the project's foundation; every later chapter assumes these fields exist.

**How to adapt this prompt:**

- *For your own project:* If you're board-prep focused, prioritize fields that match USMLE-style content (virulence mechanisms, treatment, resistance). If you're research-focused, prioritize molecular details.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you picked SQLite, Claude Code is the right tool — generates the table-creation SQL and inserts the first entries.
- *For a Claude Project:* Optional — the schema can live in the project instructions for quick reference.

**Connection to previous chapters:** This is the project's opening.

**Preview of next chapter:** Chapter 1 adds the first real entries — four microbes from across the three domains plus a prion. The database goes from empty schema to first populated entries.


---

## AI Wayback Machine

**Robert Koch** was developed the postulates for proving a microbe causes disease in 1884 — still the foundation of medical microbiology.

**Run this:**

```
Who is Robert Koch, and how does their work connect to microbiology basics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Robert Koch"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Robert Koch's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Robert Koch's framework."

What changes? What gets better? What gets worse?
