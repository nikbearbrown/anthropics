# Chapter 00 — Claude Basics

*An instrument, not an oracle.*

January 8, 1815. A British force of about 8,000 attacks American positions south of New Orleans. Andrew Jackson's command — a mix of U.S. regulars, Tennessee and Kentucky militia, free Black soldiers from Saint-Domingue refugee communities, Choctaw fighters, and the Baratarian privateers under Jean Lafitte — holds its line behind cotton-bale fortifications along the Rodriguez Canal. In roughly half an hour the British take about 2,000 casualties to the Americans' seventy. It is the most lopsided pitched battle ever fought between European-style armies on the North American continent.

It is also, by the calendar that decided the war, irrelevant.

Fifteen days earlier, on December 24, 1814, American and British negotiators in the Belgian city of Ghent had signed a treaty ending the War of 1812. The Battle of New Orleans was fought because news of the peace had not yet crossed the Atlantic by sail. Jackson's victory came after the war had been agreed to end. The peace would have arrived whether he won or lost. His career — and the political coalition that elected him president in 1828 — was made by a battle that decided nothing.

This is the kind of thing a US history textbook should teach you to notice.

It is also the kind of thing a large language model will frequently smooth over.

Ask Claude — or ChatGPT, or Gemini — to summarize the War of 1812. Most of the time you will get a clean paragraph that calls the Battle of New Orleans "a major American victory" that "boosted national pride" and "made Andrew Jackson a hero." All true. The timing wrinkle — that the battle was fought after the peace was signed but before the news could reach Louisiana — sometimes appears in the response and sometimes does not. When it does not, the model is not lying. It is producing the most statistically likely description of "Battle of New Orleans 1815," and that description, in the enormous corpus it was trained on, frequently omits the wrinkle because the wrinkle is interesting but not always reported. Wikipedia mentions it. The National Park Service mentions it. Many high-school textbooks do not. The model averages across all of that. Sometimes the wrinkle survives. Sometimes it doesn't.

You can run this test yourself. Open Claude in one tab and ask: *"Was the Battle of New Orleans fought before or after the War of 1812 ended?"* Then start a fresh conversation and ask: *"What was the significance of the Battle of New Orleans?"* Compare the two answers. Notice which version of the battle the model gives you when you pull on the timing, and which version it gives when you let it summarize on its own.

That test — that move — is what this chapter teaches.

## What Claude actually does

There is a temptation, when an instrument talks to you in complete English sentences, to think of it as a person who happens to live inside a computer. A small librarian. A patient tutor. A research assistant who has read everything and forgotten nothing.

This picture is wrong, and the wrongness matters.

A large language model is a function — an enormous one, with hundreds of billions of internal parameters — that takes a sequence of text as input and produces a probability distribution over the next word. That is the whole mechanism. Given the text *"The Battle of New Orleans was fought on January 8,"* the model produces a probability distribution over the next token. *1815* is high-probability. *1812* is lower but not zero. *Tuesday* is low. *spaghetti* is essentially zero. The model picks one of the high-probability tokens — usually but not always the top one — and appends it to the sequence. Then it does the calculation again to pick the next token. And the next. One at a time, until it decides to stop.

That is it. The whole performance is built out of this. The model is not consulting a database. It is not looking anything up. It is generating, token by token, the most statistically likely continuation of the text you gave it, where "statistically likely" is determined by the patterns it absorbed during training on a very large fraction of the digitized written world.

Two things follow from this mechanism, and they decide how useful Claude can be to you.

First, the model is genuinely good at producing plausible English about almost any topic that was well-covered in its training data. US history at the survey level is well-covered. So Claude will, most of the time, give you a fluent, organized, and broadly accurate summary of any topic in this book's table of contents. That is not a small thing. It would have been a miracle in 2020.

Second, the model has no separate faculty for distinguishing things it remembers correctly from things it is making up. The same machinery — next-token prediction over patterns in training — produces both. When the model says *"The Battle of New Orleans was fought on January 8, 1815, and was a decisive American victory"* it is using the same mechanism as when it says *"Andrew Jackson, who had served as governor of Florida from 1818 to 1821"* — a sentence that sounds correct and contains a real fact (Jackson was briefly military governor of Florida in 1821) but states wrong years. The model does not know it is wrong. It produced the wrong years because, given everything else in the sentence, those years were among the more probable continuations.

This phenomenon has a name. Some people call it *hallucination*, but that term suggests the model is seeing things that aren't there. *Confabulation* is the better word — the way a person with certain kinds of brain damage will smoothly produce a coherent story to fill a gap in their memory, with no awareness that the story is wrong. That is exactly what these models do. Fluent, confident, frequently wrong, and not flagged as wrong by anything internal to the model.

The trade-off is the central one. Fluency and accuracy are produced by the same mechanism, and the mechanism cannot tell them apart. You cannot get the fluency without the risk of confabulation. The risk is structural, not occasional. The instrument is a confabulator that often happens to be right. Your job, using it, is to know when it is right and when it is not.

## How to ask, what to do with the answer

The same model, asked the same question two different ways, will give you two different answers. The phrasing of the question — the *prompt* — is part of the experiment. A vague prompt produces a vague answer. A specific prompt, if it specifies the right things, produces a verifiable answer. A prompt that contains a falsehood often produces an answer that doubles down on the falsehood. (Try this: ask Claude, *"Why did Andrew Jackson lose the Battle of New Orleans?"* The model is unlikely to correct you. It is more likely to construct a plausible-sounding answer to a question whose premise is wrong. This is a useful failure mode to remember.)

The discipline of using the instrument well has three moves.

**Specify.** Ask the question precisely enough that you can tell when the answer is verifiable. *"Tell me about the Compromise of 1877"* is not specifiable. *"What is the Compromise of 1877, and how has the historiography of it shifted since C. Vann Woodward's 1951 thesis?"* is specifiable — you can check whether the model names Woodward, names the more recent qualifications, names specific historians.

**Compare.** Run the same question through more than one model, or through the same model phrased two or three different ways. Look at what changes. The differences are diagnostic. When all three models say the same thing, you are probably looking at consensus or a shared training-data simplification. When they diverge, that is where the interesting work begins.

**Verify.** Check the contestable claims — the dates, the casualty counts, the quotations, the legal citations — against a primary source. A primary source, in this book's usage, is a document produced at or near the time of the event by someone who was a party to it. A senator's speech in the Congressional Globe. A treaty text. A diary. A photograph with verifiable provenance. The Library of Congress, the National Archives, *Founders Online*, university digital collections — these are where primary sources live on the public web.

Verification is slower than trusting. A chapter you read and verify will take you three times as long as a chapter you read and accept. The book's claim is that the slower reader, after thirty-two chapters, knows things the faster reader does not — knows where the textbook narrative is contested, where the model is unreliable, what a primary source feels like in the hand. The slower reader is also more useful in a workplace, in a graduate seminar, and on a jury.

## What you will build

Every chapter of this book ends with an *LLM Exercise* — a specific, copy-paste-ready prompt that produces a concrete output and contributes to a single running project you will pick in Chapter 1.

The project is yours. The structure is the book's. The specific content reflects your interests, your domain, your reading of US history. Two students completing every exercise in this book will produce two recognizably different final projects.

The book offers four candidate projects. A *verification logbook* — a running document where each chapter contributes one entry recording a specific LLM claim, the primary source you checked it against, and the verdict. A *counter-narrative wiki* — 32 contested points in American history with the historiography on each side. A *source-triangulation agent* — a Claude Project you build into a working tool that takes a historical claim and triangulates it across textbook orthodoxy, primary source, and current scholarship. A *voices anthology* — a curated reader of primary-source excerpts that complicate the textbook narrative.

Chapter 1 walks through the trade-offs and you pick. For Chapter 00, before that choice has been made, the exercise is project-agnostic. It tests the basic move you will use thirty more times.

The book is optimized for Claude. The prompts work on ChatGPT and Gemini with minor edits — usually a sentence or two of rewording. Where there are meaningful differences, the LLM Exercise includes adaptation notes. If your primary model is Claude, the book is written for you; if it is something else, you will not be stuck.

A short decision rule for tools. Use Claude chat (claude.ai) for any single-session task. Use a Claude Project when you are returning to the same work across multiple sessions and want the model to maintain context — this is the right home for any of the four running projects. Use Claude Code when the task produces runnable code or operates over files on your computer. Use Cowork when the task involves reading and writing files with minimal back-and-forth. Most of the book's exercises live in chat or Project; a few specific ones recommend Code or Cowork, and the chapter will say so.

## Where the instrument fails on this material

Generic disclaimers about LLMs being "imperfect" are useless. Specific failure modes — the kind you will hit in this book, on these topics — are useful. Three.

The model flattens temporal sequence. Events that happened close together in time get described as if they happened simultaneously or in a clean causal chain when they did not. The Battle of New Orleans / Treaty of Ghent example is one. So is the relationship between the Emancipation Proclamation (January 1, 1863) and the actual freedom of enslaved people (which arrived at different times in different places — Confederate territory under Union control immediately, the Confederate interior over the next two and a half years, Texas not until June 1865, and the loyal border states not until the Thirteenth Amendment in December 1865). Ask Claude when the Emancipation Proclamation "freed the slaves" and you will often get an answer that elides this geography. Your move: when a date appears, ask what *happened* on that date in each affected place.

The model softens the framing of violence. Massacres become "conflicts." Lynchings become "incidents." Enslaved people "worked" rather than were "forced to labor." Indigenous removal is described in the passive voice. None of this is deliberate; it is the model averaging across a training corpus that includes both honest accounts and softened ones. Your move: when describing organized violence, ask Claude explicitly to name the perpetrators, the victims, the casualty count, and the legal status of the act under the laws of the time.

The model is least reliable on contested historiography. When historians disagree, the model tends to produce a synthesis that papers over the disagreement, or to present one side as established while omitting the other. The Civil War's causes (slavery versus "states' rights" framings), the necessity of the atomic bombs (Alperovitz versus Walker versus Frank), the effectiveness of the New Deal (Schlesinger versus Higgs versus modern revisions), the responsibility for the Cold War (orthodox versus revisionist versus post-revisionist) — these are live debates with named positions. Claude will often give you one of them and not flag that others exist. Your move: when an interpretation is offered, ask *who argues for this view, who argues against it, and what evidence each side cites.*

## LLM Exercise — Chapter 00

**Project:** *(to be selected in Chapter 1)*
**What you're building:** The habit. One verified entry you will read again later, when you have the project framing.
**Tool:** Claude chat. Future entries will move into a Claude Project once you set one up in Chapter 1.

**The Prompt:**

```
You are helping me build a working understanding of where large language models are 
reliable and unreliable when answering questions about US history.

For this first exercise, I am testing the timing relationship between the Battle of 
New Orleans and the Treaty of Ghent.

Please answer the following question in roughly 200 words, citing at least one 
primary or near-primary source with a URL:

"What was the chronological relationship between the Battle of New Orleans (January 8, 
1815) and the Treaty of Ghent (December 24, 1814), and what does that relationship 
mean for how historians should describe the strategic importance of the battle?"

After your answer, please add a one-paragraph self-assessment: which parts of your 
answer are well-established in the historical record, and which parts involve 
historiographic interpretation where reasonable historians might disagree?
```

**What this produces:** A model response that should state the timing clearly, note the communication lag, describe the battle's political consequences as distinct from its strategic ones, and include a primary-source link. Plus a self-assessment that flags the historiographic dimensions.

**How to adapt this prompt:** Replace the Battle of New Orleans / Treaty of Ghent pair with any event you suspect involves a timing wrinkle in your area — a delayed-news event, a treaty whose effect lagged its signing, a court decision whose practical effect arrived later. The structure of the prompt (named event, named related event, question about chronology, request for primary source, request for self-assessment) is reusable.

For ChatGPT / Gemini: use as-is. Both handle the prompt format well. ChatGPT will sometimes need a follow-up to produce the self-assessment paragraph.

For a Claude Project: if you have already created a project for this book, paste the prompt as a message. If not, save the response in a file you can re-import once you set up the project in Chapter 1.

**Preview of next chapter:** Chapter 1 opens on the pre-Columbian Americas, Europe on the brink of change, and West Africa before the Atlantic system — three continents already complex before the contact that linked them. It also asks you to pick a running project and produce your first substantive entry on the demographic catastrophe that began in 1492.

---

**What would change my mind.** If a careful study showed that students using this book without the LLM thread performed as well or better on assessments of historical reasoning as students using the book with it, the book's premise would need rework. The claim is that the discipline of comparing-and-verifying improves historical thinking. The claim is testable.

**Still puzzling.** I am not yet sure where the line is between "Claude is genuinely useful for studying a topic" and "Claude is fluent enough to make you feel like you've studied a topic when you haven't." The book asks you to verify, but verification is itself a habit that has to be built. I do not have a clean test for whether a student has built the habit or merely performed it on the page. That is the open problem under the book's whole method.


---

## LLM Exercise (Wiki variant) — Chapter 0: Open the Counter-Narrative Wiki

> *Instructor-swap alternative to the Verification Logbook exercise above. Pick one project for the semester — Logbook (the Project listed above, recommended default) or Wiki (this one, recommended for advanced seminars and honors courses). Do not run both in parallel; the work compounds across the semester and splitting it weakens both.*

**Project:** *The Counter-Narrative Wiki* — across 32 historical chapters, build a wiki of 32 contested points in American history. Each entry names the orthodox textbook narrative, the contested reading worked out among current historians, the primary-source evidence that distinguishes them, and your current reading with reasoning. By the end you have a publishable reference work — and a working knowledge of where the historiography is alive.

**What you're building this chapter:** The wiki's foundation — set up the Claude Project, decide on your organizing principle (regional / thematic / contrarian), and write the entry template you'll fill in 32 times.

**Tool:** Claude Project (the canonical fit — the system prompt holds your interpretive stance and the entry template; each chapter adds one wiki entry the project will cross-reference for synthesis).

**One-time setup before the prompt:**

1. Create a Claude Project named *Counter-Narrative Wiki: US History*.
2. Set the system prompt: *"I am building a 32-entry wiki of contested points in American history. My audience is [educated general reader / fellow undergraduates / graduate seminar / Wikipedia editors — pick one]. My organizing interest is [pick: race and class, war and diplomacy, economy and labor, gender and family, environment, technology, region, intellectual history — or pick a contrarian angle like 'the histories my high school left out']. I want you to push back when my framing is one-sided, force me to name specific historians on each side of a dispute, and refuse to flatten contested points into 'historians debate.' Each entry must commit to a current reading — with awareness that the commitment could move with new evidence."*
3. Create the folder `wiki/` and the file `wiki/00-template.md` (you'll create this in the exercise below).

**The prompt:**

```
Chapter 0 — Wiki setup and template.

This chapter taught the four-move prompt structure (show what you
have, say what you want, constrain it, ask for verification) and
the verification habit. I am building the Counter-Narrative Wiki —
32 entries on contested points in American history. Each entry
follows the same template.

Draft the wiki entry template. Each entry will have these sections:

1. **The contested point** (1 sentence — name the dispute precisely).

2. **Orthodox narrative** (~150 words — what does the standard
   textbook actually say? Cite a specific textbook or canonical
   source).

3. **Contested reading** (~200 words — which historians make the
   alternative case, in which works, with what argument? Name at
   least two named historians with works (year, title, publisher
   if relevant)).

4. **Primary-source evidence that distinguishes the readings**
   (~150 words — what documents, when read carefully, push one
   way or the other? Cite specific sources).

5. **My current reading with reasoning** (~150 words — commit to
   a position. State what would move you off it.).

6. **What an LLM will smooth over** (1–2 sentences — what part of
   this dispute does ChatGPT/Claude/Gemini flatten when asked
   summary questions?).

7. **Source notes** (citations, links to digitized sources, the
   `[verify]` flags that need follow-up).

Total entry length: ~800–1,200 words. Markdown headings clean enough
to render in a static-site generator if I eventually publish.

For Chapter 0 specifically, write a *worked example* of an entry —
on a contested point I can verify quickly. Pick the War of 1812
question: was it a Second War of Independence or a war of aggression
against Canada? Both Donald Hickey's *The War of 1812: A Forgotten
Conflict* (1989) and Alan Taylor's *The Civil War of 1812* (2010) are
canonical. Write the entry to length.

Save the template to `wiki/00-template.md` and the worked example to
`wiki/00-example-war-of-1812.md`.

End with: the three commitments I'm making about this wiki — what I
will do every chapter, what I will refuse to do, and what I'll do
when the historiography is genuinely thin (some chapters, especially
early colonial, will fight me).
```

**What this produces:** A wiki entry template + a worked example you can use as the model for the next 32 chapters + three explicit commitments that will keep you honest.

**How to adapt this prompt:**

- *For your own project:* The organizing principle in the system prompt is the project's most important variable. "Contested points my AP US History course never mentioned" produces a wildly different wiki than "Contested points in US economic history" — both legitimate, neither generic.
- *For ChatGPT / Gemini:* Use a Custom GPT (ChatGPT) or Gem (Gemini) with the same persistent context.
- *For Claude Code:* Useful later if you want to build the wiki into a static site (Hugo, 11ty, Astro). Worth doing once the entries accumulate.
- *For Cowork:* Excellent for the file-management side — Cowork can keep `wiki/` synchronized with your local files and produce the static-site build later.

**Connection to previous chapters:** None — this is the seed.

**Preview of next chapter:** Chapter 1 (pre-1492) opens the historical sequence with a serious contested point: how many people lived in the pre-Columbian Americas? The estimates ranged from 8 million to 112 million within the same generation of scholarship. You'll write your first real entry.


---

## AI Wayback Machine

The stories in this chapter didn't appear from nowhere. **Carter G. Woodson** was founding the academic study of African American history — the *Journal of Negro History* (1916), "Negro History Week" (1926, the seed of Black History Month), and *The Mis-Education of the Negro* (1933) — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Carter G. Woodson, and how does their work on the systematic recovery of Black history from American historical writing that had ignored it connect to the verification habit and the work of building counter-narratives in American history? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Carter G. Woodson"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain what Woodson meant by "mis-education" — and what that critique would say about a 2026 high school US history curriculum
- Ask: "Woodson founded *Negro History Week* in 1926. What was actually published in its first ten years? What did *not* get published that he wanted to?"
- Add the framing: "Answer as if Woodson himself were writing the introduction to a 2026 textbook of US history"

What changes? What gets better? What gets worse?
