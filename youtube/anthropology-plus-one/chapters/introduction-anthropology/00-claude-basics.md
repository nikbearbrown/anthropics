# Chapter 00 — Claude Basics

*The chapter before the book.*

## Suggested titles

- *Before the Book: Claude Basics*
- *How to Use Claude Without Letting Claude Use You*
- *Anthropology with LLMs — A Working Manual for the Tool*

## TL;DR

This book asks you to use a large language model (LLM) — Claude is the default — at the end of every chapter and at scattered points within. The model is a useful collaborator and an unreliable witness. This chapter teaches you what it actually does, how the two prompt types in the book work, where it breaks in anthropology specifically, and how to push it past its safe answer.

---

## 1. A confident, fluent, wrong answer

A student is reading the chapter on cultural relativism. The female-genital-cutting case study has just landed. She types a question into Claude: *Is female genital cutting wrong?*

The reply comes back in two seconds. Two confident paragraphs. A summary of the human-rights position. A nod toward "cultural sensitivity." A balanced closing about the importance of respecting other cultures while protecting individual rights. Polite. Fluent. Grammatically perfect. The kind of answer that would earn a B+ from a teacher who hadn't been paying close attention.

It is also, by the standards of the chapter she just read, a bad answer.

The chapter spent six paragraphs showing how Bettina Shell-Duncan's *relativist turn* changed her policy advice — that the productive response to FGC was not condemnation but the slow work of understanding the cultural functions of the practice and aligning interventions with local logic. The model's answer flattened all of that into "respect cultures, but also, human rights." It used the word *relativism* once, in the way a student uses a word they've been told to include.

She tries again. This time she pastes in two paragraphs of the chapter and asks: *Given Shell-Duncan's findings, what would she actually advise an NGO planning an anti-FGC campaign in Senegal?* The reply is still confident. It is also still generic. It mentions "community engagement" and "culturally sensitive approaches" without naming the specific moves Shell-Duncan made — work with senior women, target the network of decision-makers around the family rather than only mothers, partner with local feminist organizations.

She tries a third time, this time pasting the whole chapter section and asking: *Compare this to a typical UN advocacy framework. Where would Shell-Duncan disagree with the UN approach, and on what grounds?* The reply now does something useful. It identifies the disagreement, names the mechanism (top-down condemnation vs. community-anchored persuasion), and lists three specific moves Shell-Duncan's framework would suggest. It is not a finished essay. It is the start of one.

Three prompts. The first answer was bad. The second was thin. The third was useful. Nothing about the model changed. The student got better at asking.

This chapter is about that progression. What the model is doing when it answers. How to ask it questions that produce real intellectual work rather than fluent filler. Where in this discipline it will reliably fail you. And — crucially — when *not* to ask it at all.

[FIGURE: A two-panel diagram. Panel A: a student's first prompt to Claude on FGC, the resulting generic two-paragraph reply, a thumbs-down marker. Panel B: a third, more specific prompt with chapter context pasted in, the resulting analytical reply naming Shell-Duncan's specific moves, a thumbs-up marker. Caption: same model, two prompts, two different outputs. Skill is in the asking.]

**Learning objectives.** After this chapter, you should be able to:

- Explain in one paragraph what a large language model is doing when it answers a question, without using the words *intelligence* or *think*.
- Distinguish a *Dig Deeper* prompt from an *LLM Exercise* and use each correctly.
- Adapt the prompts in this book to your own context (your country, your data, your project) without breaking them.
- Recognize the four failure modes of LLMs in anthropology and respond to each.
- Choose the right tool — Claude chat, Claude Project, Claude Code, or Cowork — for a given task.

**Prerequisites.** None. You do not need to have used an LLM before. If you have, this chapter will probably re-anchor a few things you got from rumor.

**Why this chapter matters.** The rest of the book will give you a prompt at the end of every chapter and several inside each one. Without this chapter, those prompts will produce fluent, plausible, often shallow output. With this chapter, they will produce real work. The difference is not in the model. It is in you.

---

## 2. Concept 1 — What the model is doing when it answers

### A scene at the keyboard

You type a question. The cursor blinks. Two seconds later, a paragraph appears. It is grammatically correct. It is on topic. It often sounds confident, sometimes more confident than the source material would warrant. It usually does not say *I don't know*.

What just happened?

The temptation is to call it *thinking*. The model is not thinking. It is producing the most probable next sequence of words, given everything you wrote and everything it has been trained on. That is the entire mechanism. The trick is that *most probable next words*, scaled to billions of parameters and trained on most of the readable internet, gets you something that *behaves* like reasoning across an enormous range of inputs.

This is the single most important sentence in this chapter: *the model is generating plausible continuations of text, not retrieving facts.* Internalize that and most of the failure modes downstream will make sense. Forget it and you will be misled.

### The mechanism, plainly

Strip the system to its working parts.

A *language model* is, at its core, a function. You give it some text — a *prompt*. It gives you back some text — a *completion*. The function was built by training a neural network (a large statistical model with billions of adjustable weights) on a vast corpus of human-written text — books, articles, forums, code, transcripts. During training, the model was shown sequences of tokens (think of tokens as roughly word-pieces) and asked to predict the next one. Over many passes, the weights adjusted until the model got good at this. Very good.

When you type a prompt and hit enter, the model reads your tokens, runs them through its trained weights, and produces a probability distribution over what token should come next. It samples from that distribution, appends the token, and repeats — token by token — until it decides the response is finished.

That is all. There is no database lookup. There is no internal reasoning unit verifying claims. There is no truth-checker. There is a *very good predictor of what plausible text looks like in this context*.

This is not a put-down of the model. The fact that *what plausible text looks like* turns out to encode a great deal of useful structure — including the structure of arguments, narratives, code, and explanations — is one of the more interesting empirical findings of the past decade. A good predictor of plausible text can summarize an article, draft an email, explain a concept, debug a function, and translate an idiom. Sometimes it can do these things better than a tired human.

It can also produce a confident, fluent, wrong answer. The failure mode is a feature of the same mechanism that makes it useful: the model produces what *sounds right*. When *sounds right* and *is right* coincide, you get a useful collaborator. When they diverge, you get a hallucination — a fluent fabrication that reads like a fact and isn't one.

### What this means for using it

Three working consequences fall out of this mechanism, and they shape every prompt in this book.

**First.** The model is good at *form*. It is less reliably good at *fact*. If you ask Claude to draft an outline of an argument about caste in India, you will get a structured outline. If you ask Claude for the citation of a specific 1999 ethnography, you may get a real one, or you may get a plausible-looking citation that is fabricated whole — author and title and journal that do not exist. This is *citation hallucination*, and it is the single most consistent failure of LLMs in academic work. We will return to it.

**Second.** The model is a context-shaped tool. The same model produces different output depending on what you give it. A bare question gets a bare, generic answer. A question framed inside a specific case, with the relevant material pasted in, gets a specific answer. Most of the skill of using an LLM is not in what to ask but in *what context to provide* before you ask.

**Third.** The model has no memory across sessions unless you give it one. Each Claude chat begins fresh. If you want continuity — the running project this book asks you to build — you will need either to paste prior context back in, or to use a *Claude Project*, which is a folder of persistent context the model reads at the start of every conversation.

The trade-off named: an LLM optimizes for *fluent, plausible output across a vast range of inputs* at the cost of *factual reliability and persistent memory*. The mechanism is the same in both directions. You cannot keep the fluency and lose the hallucination. What you can do is learn when the trade-off works for you and when it doesn't.

### A simple test you can run on yourself

Pick a topic you know deeply — a subject you've studied for at least a year. Ask Claude an intermediate question about it. Read the answer carefully. *Where does it sound right but isn't? Where does it sound right and is? Where does it confidently miss the most interesting question?*

Most students who run this test on a topic they know well discover two things at once. The model is impressively coherent at the surface. And it is consistently shallow at depth, especially around the specific cases and named scholars and contested points that an expert would care about.

Now flip the test. Ask Claude an intermediate question about a topic you know *nothing* about. Notice that the answer feels just as confident and just as fluent. The fluency does not change with the model's actual reliability. *That* is the calibration problem you bring to every prompt for the rest of the book.

---

## 3. Concept 2 — The two prompt types in this book, and how to adapt them

### Two textures of LLM use

This book uses two kinds of prompts, and they have different jobs.

**Dig Deeper prompts** appear inline, scattered through the chapters, marked with a `↳` symbol. They are short. They are optional. They invite you to take a concept that just caught your attention and push it further with Claude. A Dig Deeper prompt is a hand on your shoulder saying *you know what's interesting here…* You can ignore them. You should ignore most of them. You should follow the one or two per chapter that genuinely catch you.

**LLM Exercises** appear at the end of each chapter, exactly one per chapter. They are the *running project*. Each one builds a piece of something larger. By the end of the book, you will have an artifact — something real, something you could show another human — that accumulated chapter by chapter. Whatever Running Project you select for this edition of the book, the LLM Exercise in each chapter advances it.

Two textures. One is intellectual rabbit hole. The other is incremental build.

### Why the split

Most textbooks treat AI as either a cheating temptation (don't use it) or a magic shortcut (use it for everything). Both are wrong. The split between Dig Deeper and LLM Exercise is the alternative: AI is good for some specific things and not others, and the two prompt types correspond to two specific things it is good at.

Dig Deeper is good for *exploration* — taking a concept the chapter mentioned but didn't fully unfold and asking Claude to walk you a level deeper, give you three more examples, draw an analogy, point you to a debate. The model's tendency toward fluent surface-coverage is, here, a feature: you wanted breadth, not depth, and you can chase the depth yourself once you know what to chase.

LLM Exercise is good for *production* — turning your accumulating understanding into an artifact that exists outside this textbook. The model's tendency toward generic output is, here, a problem you actively work against: by giving the model your specific context (your country, your data, your earlier outputs from prior chapters), you force it past the safe, generic answer.

If you only do the LLM Exercises, you will finish the book with a real artifact and a flat understanding. If you only do the Dig Deepers, you will have explored deeply and built nothing. You want both.

### Format — what each prompt looks like

Every Dig Deeper looks the same. A heading marked with `↳`, a sentence explaining what the prompt helps you explore, a copy-paste-ready prompt set off as a blockquote, and a one-line note on what to do with the output.

```
↳ Dig Deeper — [Concept name]

Why this prompt is worth running.

> Copy-pasteable prompt for Claude. Two to five sentences.
> Specific enough to work. Open enough to adapt.

What to do with the output: read it / paste it somewhere / compare it to X.
```

Every LLM Exercise has a heavier structure: which project it advances, what tool to use, the prompt itself in a code block, what the prompt produces, how to adapt it for your domain or for a different LLM, and what the next chapter's exercise will add. The LLM Exercise is closer to a recipe. You will run it and produce a file or a section or a function or a page.

### Adapting prompts to your own context

Every prompt in the book has placeholders or assumptions. *Use a region of your choosing. Use data from your own field site. Use the project type you selected at Chapter 00.* The prompts work because they are specific. They need *your* specifics to work for *you*.

The general adaptation rules:

**Replace placeholders without breaking the prompt's structure.** If a prompt says *analyze [a culture you have access to]*, replace it with *analyze the culture of competitive marathon running in the United States* — keep the verb, keep the analytical frame, swap only the topic. Do not rewrite the whole prompt unless you understand what each sentence was doing.

**Keep specifics specific.** A prompt that asks for *one named scholar's argument* will not work if you replace it with *some scholars' arguments*. The specificity is doing structural work. Generalizing the prompt produces a generalized output.

**Add context, don't subtract it.** When in doubt, paste more of the chapter into the prompt rather than less. The model is a context-shaped tool, and starving it of context is the most reliable way to get a bad answer.

**Iterate, don't abandon.** If the first response is thin, do not give up on the prompt. Reply: *That's too generic. Pick the specific case from this chapter and go deeper on that one.* Almost every weak answer in this book can be salvaged by one or two follow-up turns. The student in the cold open got there in three.

### When to use which tool

The book recommends four tools across the chapters. They are not interchangeable.

**Claude chat (claude.ai)** is the default. Single conversations, a back-and-forth, no special setup. Use this for Dig Deeper prompts and for any LLM Exercise that produces a piece of writing or an analysis you can copy-paste.

**Claude Project** is a folder of persistent context that the model reads at the start of every new conversation. Use this when an exercise builds on prior chapters' outputs and you don't want to keep pasting them. Set up a Project at the start of the book; drop each chapter's LLM Exercise output into it; subsequent chapters can reference prior outputs without re-pasting.

**Claude Code** is Claude operating directly on files on your computer. Use this for any LLM Exercise that involves real file manipulation — building a website, running a script, generating a structured dataset, coding an analysis. If your Running Project produces code, Claude Code will likely come up.

**Cowork** is Claude with access to a designated workspace folder, capable of multi-step file operations and longer autonomous runs. Use this when an exercise produces multiple files or a multi-step deliverable (a report with figures and a data file; an annotated transcript with a coded summary).

The book's individual exercises will recommend a tool. The recommendation is the easiest path. If you are comfortable with another tool, use it.

---

## 4. Concept 3 — Where Claude reliably fails in anthropology

### The four failures

Every discipline has its own LLM failure modes. In anthropology, four come up reliably enough that they should change your default behavior.

**Failure 1: Fabricated citations and ethnographies.** Ask Claude for the citation of an article that supports a specific claim, and there is a real chance — maybe one in three for obscure subfields — that the citation is fabricated. Author plausible. Journal plausible. Year plausible. Article does not exist. This is the model producing what *plausible text* looks like in the position where a citation should appear. It is most common for older or non-Anglophone scholarship and for niche subfields with thin online presence. The fix is non-negotiable: *every citation you take from Claude must be verified independently before you use it*. If a citation appears in a chapter draft you produced with Claude, look it up in a real database (JSTOR, Google Scholar, the journal's own site) before you trust it. Treat unconfirmed Claude citations the way you would treat a quote attributed to a friend's friend's uncle: not yet evidence.

**Failure 2: Generic cultural treatments that flatten difference.** Ask Claude about *African religion* or *Asian family structures* and you will likely get a fluent, plausible, wrong answer that treats whole continents as cultural blocs. This is a structural feature of training corpora — much writing about non-Western cultures is itself generic — and a structural feature of model averaging. The fix is to insist on specificity. *Tell me about religion among the Dogon of Mali* is a different prompt than *tell me about African religion*. The first will get you something usable. The second will get you a stereotype assembled from English-language travel writing.

**Failure 3: False neutrality on contested ethnographic claims.** Many anthropological questions are *not* settled: whether the Kalahari Ju/'hoansi were ever truly egalitarian, whether early-state societies were oppressive or stabilizing, whether a specific ritual is ancient or invented in the 19th century. Claude will often present such contested questions as if there is a consensus, sometimes inventing one. The fix is to ask explicitly: *what is contested about this claim, and which scholars take which positions?* If the model can name the disputants, the dispute is probably real. If it can't, you may be reading invented consensus.

**Failure 4: Ethnocentric defaults.** When you ask Claude an open question about *human nature* or *the family* or *what's normal*, the answer often reflects WEIRD assumptions — Western, Educated, Industrialized, Rich, Democratic — because that is what most of the training corpus was. The chapter on the four-fields-on-race already taught you to spot this in popular media. The same diagnosis applies to LLM output. The fix is to name the assumption: *give me three answers to this question — one from a small-scale agricultural society, one from a pastoralist society, one from an industrial society. Where do they agree and where do they disagree?*

### What this changes about your workflow

These four failures imply a working rule: *for any factual claim that matters, verify outside the model.* For any synthesis, structure, draft, outline, summary, or rephrasing, the model is a useful collaborator. For specific facts, citations, dates, and contested ethnographic claims, the model is a *first draft of something you must check*.

A useful frame: imagine the model as a very well-read undergraduate who has skimmed every book in the library, retained the structure of every argument, and gotten about 80% of the specifics right. They are useful. They are not your peer reviewer. They are not your authority. They are your study partner who has read the assigned reading and now wants to help you draft.

### A failure case, walked through

A student prepares a paper on the *kula ring* (mentioned briefly in Chapter 1's discussion of Malinowski). The prompt: *Write me a 1,000-word essay on the kula ring.*

The output: fluent. Five paragraphs. Mentions Malinowski. Mentions necklaces and bracelets traveling in opposite directions. Mentions reciprocity. Sounds like an essay.

The problems, on close reading: the dates of Malinowski's fieldwork are slightly wrong. Two of the cited "scholars who built on Malinowski" do not appear to exist as named. A specific claim about the kula ring being "still actively practiced today" is unsourced and partially out of date. The section on "the kula in contemporary tourism" reads like it was made up wholesale.

What the student should have done: asked for an *outline* rather than a draft. Verified Malinowski's dates against a reliable source. Refused any claim about contemporary practice without a primary citation. Used Claude as a structuring partner rather than a research substitute.

This is not a critique of the model. It is a critique of *how the model was used*. With a different prompt, the same model produces a much better artifact: *Outline a 1,000-word essay on the kula ring. Cover Malinowski's original fieldwork, the structure of the exchange, what later scholars argued the kula was actually doing, and the limitations of the original ethnography. Do NOT include citations — I will verify those separately.* That outline, plus the student's own checking, plus the student's own writing, becomes a real essay.

---

## 5. Integration — A worked example using your Running Project

The Running Project this edition of the book uses is the **AI-Augmented Anthropology Toolkit**. Each chapter contributes one reusable *tool* — a parameterized Claude prompt that the student can invoke later on any new input. By Chapter 20 you have a folder of 20+ working tools, each with a tested prompt, a documented input format, an example output, and notes on when the tool fails.

A "tool" in this sense is not a piece of code (though it can be wrapped in code). It is a structured, repeatable prompt that does one analytical job well. The discipline of building tools — instead of just running ad-hoc chats — is part of the lesson. A reusable tool forces you to specify what you want, what you need to provide, and what counts as a good output. A one-off chat lets you stay vague.

### The Chapter 1 tool, walked through

The Chapter 1 LLM Exercise (full version at the end of Chapter 1) will ask you to build **Tool #1: The four-fields-on-a-claim analyzer.**

The tool's job: take any claim about *human nature*, *humans*, or *people* — the kind of sentence that begins *humans are…* — and run it through anthropology's four fields. What can biological anthropology say about this claim? Archaeology? Cultural anthropology? Linguistic anthropology? Where do the fields converge? Where do they pull against each other? What evidence would settle it?

The tool, in skeleton form, looks like this:

```
You are an analyst running the four-field framework from
introductory anthropology against a single claim.

The claim:
"[CLAIM goes here]"

Produce four short paragraphs, one per subfield (biological, archaeological,
cultural, linguistic). For each:
- What evidence does this subfield have access to?
- What would it look for, specifically, to test this claim?
- What is one named scholar or study that's relevant?

Then a fifth paragraph: where do the fields converge or contradict on this claim?
What integrated finding would the four together produce that none alone could?

Constraints:
- Cite specific scholars / studies by name. If you are uncertain about a citation,
  flag it as [verify] rather than fabricating.
- Avoid generic answers ("biological anthropologists would study DNA" is too vague —
  what specifically would they look at, and why?).
- 600–900 words total.
```

That is the tool. It has a parameter (`[CLAIM goes here]`). It has explicit constraints. It instructs the model to flag uncertain citations rather than invent them. It specifies output length and format.

### How a student uses the tool

Day-of-class: a student reads a magazine piece arguing that *humans are biologically programmed to seek hierarchy*. Instead of accepting or rejecting the claim by gut reaction, they paste the claim into Tool #1. Out comes four paragraphs and an integration paragraph. The biological field flags the relevant primate-hierarchy literature and notes that primates vary widely in dominance structures. The archaeological field flags evidence from egalitarian and centralized societies in the deep past. The cultural field flags ethnography of acephalous societies (Chapter 8 will define this term). The linguistic field flags vocabulary about leadership across languages.

The student now has a structured first read of the claim. They can chase any of the threads. They can verify any of the citations. They can use this as the spine of an essay or just as a habit of mind.

### Adapting the tool

The tool is parameterized on the claim. To adapt it for your own work:

- For a different claim, just change the `[CLAIM]` field. The rest of the tool stays.
- For a more focused field selection (e.g., you only want biological + cultural), edit the prompt to ask for two fields, not four.
- For a different LLM (ChatGPT, Gemini), the prompt works as written.
- For a Claude Project, drop this prompt as a saved instruction so you don't have to re-paste it each time.

### A weak response, and how to fix it

If the model returns four paragraphs that all sound generic, with no specific scholars and lots of hedging, your first move is *not* to abandon the prompt. Reply: *The response is too generic. Pick one specific scholar or one specific study per subfield, and ground each paragraph in that person's actual argument. If you are not confident the citation is real, mark it [verify] and tell me why you're uncertain.* The follow-up usually fixes most of the problem.

If the model produces a fabricated citation (Failure 1 from Concept 3), you have a working example of why the verification rule exists. Look the citation up. If it doesn't exist, note that the prompt as written did *not* fully prevent fabrication; the `[verify]` instruction reduced the rate but didn't eliminate it. This is real data about the tool's limits.

### What you save

After running and adapting the tool, save four things to your toolkit folder:

1. The prompt template itself (in `tools/01-four-fields-analyzer.md`)
2. One or two example inputs and the outputs they produced
3. A short notes file describing where the tool worked, where it failed, and what you'd change
4. A test claim you can re-run against the tool whenever you change the prompt — your *regression test*

This is the build pattern for every tool. By Chapter 20, you have twenty of them.

This is the loop you will run twenty times. Each time, you build a tool. Each time, you test it. Each time, you note its limits. By Chapter 20 you have a working toolkit and — equally important — a learned discipline of *making the model do specific work* rather than asking it for vibes.

---

## 6. Exercises — practicing the skill itself

Before the regular chapters begin, here are five exercises that build your facility with the tool.

**00.1 (E, calibration).** Pick a subject you know deeply — a sport, a hobby, a country, a family business, a video game, a musical genre. Ask Claude three questions of increasing specificity about that subject. For each answer, mark in the margins: *fluent and right* / *fluent and wrong* / *fluent but missed the most interesting thing*. This is the calibration exercise from Concept 1. Do it before you do anything else.

**00.2 (E, prompt structure).** Take this bare prompt: *What is anthropology?* Now rewrite it five times, each time adding more context and specificity. For each version, run it and notice what changes. Save the five outputs and the five prompts. The exercise is not the answer; it is the noticing.

**00.3 (M, hallucination).** Ask Claude: *Give me three citations for a specific claim about how kula ring exchanges work in Trobriand society.* Take the three citations. Look up each one in Google Scholar or JSTOR. Mark each as *real* / *partially real (real author, wrong title or year)* / *fabricated*. Report the rate. This will calibrate how skeptical you should be about citations Claude offers later.

**00.4 (M, the four failures).** Pick one of the four failure modes from Concept 3. Construct a prompt that you predict will trigger that failure. Run the prompt. Did the failure occur? If yes, write the corrected prompt that would not trigger it. If no, why didn't it?

**00.5 (H, working with a Project).** Set up a Claude Project for this book. The system prompt should be something like: *I'm working through "Introduction to Anthropology with LLMs" by Nik Bear Brown. The Running Project I've selected is [your chosen project]. When I ask for help with chapter exercises, ground your responses in this project and prefer specificity over generic answers.* Test it by running a prompt and noting how the response differs from the same prompt in a fresh chat without the Project.

---

## 7. Quick-reference card

| Prompt type | When to use it | What it produces | Recommended tool |
|---|---|---|---|
| **Dig Deeper** | A concept caught your interest mid-chapter and you want to explore it further. | A short Claude conversation that takes you a level deeper, gives examples, or points to a debate. | Claude chat (claude.ai). |
| **LLM Exercise** | You're at the end of a chapter and ready to advance the Running Project. | A concrete artifact (a section, a file, a function, a page) that adds to your accumulating build. | Claude chat for writing/analysis; Claude Project for continuity across chapters; Claude Code for code/file work; Cowork for multi-step file operations. |
| **Citation request** | Looking for sources to support a claim. | A list of plausible-looking citations — verify every one independently. | Claude chat to draft, then a real database (JSTOR, Google Scholar, library catalog) to verify. |
| **Outline / structure** | Drafting a paper, presentation, or section. | A structured outline that you fill in with your own writing and verified facts. | Claude chat or Claude Project. |
| **Critique / pushback** | You have a draft and want a skeptical reader. | Specific, named objections to your argument. The prompt should explicitly request critique, not approval. | Claude chat. |
| **Translation / rephrasing** | You have a paragraph that's not quite right tonally or doesn't fit the audience. | Multiple alternative phrasings to choose from. | Claude chat. |
| **Fact-check on a known topic** | You have a claim you're unsure about. | A first-pass assessment — but only on widely-discussed claims; do not trust on obscure ethnography. | Claude chat for first-pass; primary sources for the answer. |

---

## 8. Chapter summary — what you can now do

You can explain, in one paragraph, what an LLM does when it answers: it produces the most probable continuation of text given your prompt and its training. You can use that frame to predict where it will work and where it will fail.

You can distinguish a Dig Deeper prompt from an LLM Exercise. You know that the first is an invitation and the second is a build. You know that to use either well, you adapt them to your own specifics — your country, your data, your project.

You can recognize the four failure modes — fabricated citations, flattened cultures, false neutrality on contested claims, ethnocentric defaults — and you have specific moves for each. The most important of these moves: verify any factual claim that matters, before you use it.

You can pick the right tool: Claude chat for most things, Claude Project for continuity across chapters, Claude Code for code and file work, Cowork for multi-step file operations.

The single idea that matters most: *the model is a context-shaped tool. The same model produces different output depending on what you give it. Most of your skill in using it is not in what to ask but in what context to provide before you ask.*

The common mistake to watch for: trusting fluency. A confident, fluent answer is not the same as a correct answer. The fluency is constant; the correctness varies.

If you can run prompt 00.1 on a subject you know deeply and accurately mark each answer as *fluent and right / fluent and wrong / fluent but missed the most interesting thing*, you have absorbed the calibration this chapter is about. That calibration is what you bring to every prompt for the rest of the book.

---

## 9. Connections forward

Chapter 1 — *What Is Anthropology?* — gives you the discipline's central narrative, four fields, and three working commitments (holism, the ethnocentrism / relativism axis, the insider's point of view as goal-and-problem). The Chapter 1 LLM Exercise will have you build Tool #1 of your toolkit: a four-fields-on-a-claim analyzer.

The pattern holds across all twenty chapters. Each chapter teaches a concept. Each chapter ends with an LLM Exercise that turns the concept into a tool: Tool #2 will be a fieldnote / IRB-aware research-protocol generator (Chapter 2 — Methods). Tool #3 will be a wink-vs-blink semiotic classifier (Chapter 3 — Culture). Tool #11 will be a kinship-chart-from-narrative parser (Chapter 11 — Kinship). Tool #15 will be a gaze-analyzer for media artifacts (Chapter 15 — Media). The list builds.

The Dig Deeper prompts inside each chapter are different. They are not tools. They are exploratory prompts you run when a concept catches your attention, and they produce one-off Claude conversations rather than reusable instruments. You do not save Dig Deeper outputs to your toolkit folder. You may save them to a separate `notes/` folder if a particular conversation produced something you want to keep.

The toolkit folder structure (set up at Chapter 1) will look like this:

```
anthropology-toolkit/
├── tools/
│   ├── 01-four-fields-analyzer.md
│   ├── 02-research-protocol-generator.md
│   ├── 03-semiotic-classifier.md
│   └── ...
├── examples/
│   ├── 01-four-fields/
│   │   ├── input-1-hierarchy-claim.md
│   │   └── output-1-hierarchy-claim.md
│   └── ...
└── notes/
    └── (optional: dig-deeper outputs you want to keep)
```

You can build the toolkit folder using Cowork (recommended for non-coders), Claude Code (recommended for those comfortable with the terminal), or even just a folder of markdown files in your favorite editor. The structure matters more than the implementation.

Two warnings before you go.

First: a tempting failure is to outsource the *thinking* to the model and use it as a finished-essay machine. That is the path to a portfolio of fluent, generic, increasingly unsatisfying outputs. The model is an instrument. You are the one playing.

Second: a tempting overcorrection is to refuse the tool entirely. Anthropology has thrived on collaboration with translators, informants, and co-authors for a century — Alice Cunningham Fletcher's coauthorship with Francis La Flesche on *The Omaha Tribe* in 1911 was not an offense against intellectual independence, it was a methodological advance. An LLM is not a co-author. But it is a tool that can sharpen your thinking when you push back on its safe answers, just as a skilled fieldwork assistant can sharpen yours when you push back on theirs.

Push back. That is how the rest of the book wants you to work.

---

## LLM Exercise — Chapter 0: Setting up your AI-Augmented Anthropology Toolkit

**Project:** AI-Augmented Anthropology Toolkit
**What you're building this chapter:** the toolkit folder, the prompt-template format every later tool will use, and the testing discipline that prevents you from trusting a tool you have not stress-tested. This is the foundation. Tools #1–#20 build on the structure you set here.
**Tool:** **Cowork** (required — you are creating a folder structure on your computer that will hold every tool you build) plus Claude chat for testing.

### The Prompt

```
I am setting up my AI-Augmented Anthropology Toolkit at the
beginning of an introductory anthropology course. Across the
20 chapters of this book, I'll add one tool per chapter. By
the end I'll have a personal repository of prompts I can
reuse on any future ethnographic, analytical, or applied
anthropological work.

Help me set up the toolkit in this conversation by doing four
things.

1. Propose the folder structure. I'm thinking:
   anthro-toolkit/
   ├── README.md             (what this is, who maintains it)
   ├── tools/                (one .md file per tool, named NN-tool-slug.md)
   ├── examples/             (one folder per tool, holding test outputs)
   ├── prompts-archive/      (raw drafts and revisions)
   └── notes/                (failure modes, cross-tool observations)
   Push back if a structure I'm missing would matter later. Propose
   a final version.

2. Draft the standard tool template. Every tool I build should follow
   the same shape so the toolkit reads as one instrument, not 20
   different artifacts. My draft template:

   ---
   # Tool #NN — [Tool Name]
   
   **Chapter:** [N — chapter title]
   **Purpose:** [one sentence — what does this tool do]
   **Inputs required:** [what the user pastes when invoking the tool]
   **Output produced:** [structured analysis of what shape, what length]
   
   ## Refined prompt
   
   [The actual prompt template — what gets pasted into Claude]
   
   ## Test cases
   
   1. [Test case A + what the tool SHOULD produce]
   2. [Test case B + what the tool SHOULD produce]
   3. [Test case C + what the tool SHOULD produce]
   
   ## Documented failure modes
   
   1. [Failure mode A — when does the tool produce confident wrong answers]
   2. [Failure mode B]
   3. [Failure mode C]
   
   ## Citation discipline
   
   [Conventions for citation flagging — when to use [verify]]
   ---

   Push back on what's missing or generic. Propose the final template.

3. Establish the testing discipline. Every tool I build will be tested
   on at least three cases before I trust it. Help me articulate the
   *kind* of test cases I should always include — easy / medium / hard,
   or in-domain / boundary / adversarial. What's the minimum standard
   for "this tool is ready to ship"?

4. Identify the failure modes that will recur ACROSS all 20 tools.
   Anthropology + LLMs has structural failure patterns I should be
   alert to from day one — fabricating ethnographic case studies,
   imposing Western analytical frames on non-Western practices,
   romanticizing or pathologizing subject communities, hallucinating
   citations to specific scholars. Identify five recurring failure
   modes I should embed as cross-cutting checks in every tool I build.

End by writing the README for my toolkit (300 words) — what this is,
how it's structured, my testing discipline, the cross-cutting failure
modes, and the commitment to add one tool per chapter for the next
20 chapters.
```

### What this produces

Four artifacts saved to your toolkit folder:

1. **`anthro-toolkit/README.md`** — the project README you commit to from the start.
2. **`anthro-toolkit/tools/00-template.md`** — the standard tool template.
3. **`anthro-toolkit/notes/00-cross-cutting-failure-modes.md`** — the five recurring failures every tool needs to defend against.
4. **`anthro-toolkit/notes/00-testing-discipline.md`** — your standard for declaring a tool ready.

### How to adapt this prompt

- **For your own use:** This is the only chapter where the template itself is what you build. Customize the folder structure to your existing workflow (Obsidian vault, Notion, GitHub repo).
- **For ChatGPT / Gemini:** The setup works identically. Save the toolkit to whatever filesystem your tool of choice can access.
- **For Claude Code:** If you want the toolkit as a git-tracked repo from the start, ask Claude Code to scaffold it with `git init` and a `.gitignore`. Optional.
- **For a Claude Project:** Save the README and standard template as Project instructions. Every later chapter's exercise can then start from inside that Project.

### Connection to previous chapters

None — this is the foundation chapter for the running project.

### Preview of next chapter

Chapter 1 — *What Is Anthropology?* — introduces the four-field structure of the discipline. The Chapter 1 LLM Exercise has you build **Tool #1: a four-fields-on-a-claim analyzer** that takes any claim about humans and runs it through all four subfields. Tool #1 is the simplest tool you'll build — it's the proof of concept that the toolkit pattern works.

---

## What would change my mind

If reproducible studies show that LLMs trained on much larger or much higher-quality anthropological corpora produce reliably accurate citations and reliably specific cultural analyses without prompt-engineering, the *citation hallucination* warning in this chapter would need revision. To date, this remains an open empirical question, and the conservative posture below is the right one for a textbook.

## Still puzzling

The line between *useful collaboration with the tool* and *outsourcing the thinking*. There is no clean formal rule. The answer is something like: *if you can't explain in your own words what the model just produced for you, you've outsourced too far.* That heuristic feels right. I have not seen a sharper one.

---

**Tags:** llms, claude, anthropology-with-llms, prompt-engineering, hallucination, claude-project, claude-code, cowork, dig-deeper, llm-exercise, citation-verification, ethnographic-failure-modes, context-shaped-tools, four-failures


---

## AI Wayback Machine

**Margaret Mead** was cultural anthropologist whose Coming of Age in Samoa (1928) made anthropology a public-facing discipline — and whose later work shaped early thinking about computers and culture.

**Run this:**

```
Who is Margaret Mead, and how does their work connect to anthropology with tools we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Margaret Mead"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Margaret Mead's ideas to a specific contemporary anthropological question.
- Add a constraint: "Answer including criticisms or limits of Margaret Mead's framework."

What changes? What gets better? What gets worse?
