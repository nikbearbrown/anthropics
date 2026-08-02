# Chapter 10 — Languages with AI
*Every translated sentence is a sentence you never spoke.*

> AI is a nearly infinite conversation partner and an extremely dangerous crutch. The difference is whether you generated the language.

---

Lucia is in Spanish 2 her sophomore year. She is on the AP track. Her writing assignments come back with high marks. Her teacher, Señora Vasquez, has noted multiple times that Lucia's written Spanish is *clean* — gendered agreement consistent, verb tenses appropriate to context, vocabulary varied.

What Señora Vasquez does not know — what Lucia herself has only half-admitted — is that every Spanish writing assignment this semester has been routed through ChatGPT. Lucia writes in English. AI translates. Lucia tweaks the output to match phrasing she has heard in class. Her receptive vocabulary has grown; she reads the Spanish news articles assigned in class and understands almost everything. Her grade is an A.

The semester-end oral exam is a fifteen-minute one-on-one conversation with Señora Vasquez. The prompts are simple: describe your family; describe what you did over winter break; describe what you want to do this summer. Lucia has prepared. She has memorized phrases. She walks in confident.

The first question lands: *¿Qué hiciste durante las vacaciones de invierno?* Lucia opens her mouth. She knows what she did. She drove with her family to her grandmother's house. She skied. She watched a Korean drama. She has the English version of every sentence ready. She does not have the Spanish version. She starts: *"Fui a... fui a la casa de mi abuela..."* The verb conjugation comes. The vocabulary for the second clause does not. She wants to say *"and we drove for six hours."* She does not know the verb *to drive*. She freezes. A long pause. Señora Vasquez waits, patient. Lucia tries: *"...y nosotros usamos el coche... seis horas."* It is approximately correct and clearly the production of a student who does not know the verb. She continues for fifteen minutes. By the end she has used the same six verbs about thirty times.

Lucia's written Spanish is flawless. Her oral Spanish is broken.

This is not a motivation problem. It is not a memory problem in the ordinary sense. It is the consequence of a specific cognitive event that should have happened — thousands of times, across an entire semester — and did not. Every sentence she submitted that semester was a sentence she never generated. Every word that AI supplied was a word she never retrieved from her own lexicon. The productive cognitive work the semester was designed to produce was absent, because AI had done it all. The grade did not reveal this. The oral exam did.

---

## Two Theories of How You Learn a Language

In the 1970s, Stephen Krashen proposed the *Input Hypothesis*: learners acquire a second language when they receive comprehensible input — language slightly above their current level that they can understand from context. The mechanism is largely implicit. Enough exposure to the right input and acquisition follows. Krashen's formulation became the dominant theory in language pedagogy for two decades, and it is not wrong. Comprehensible input is necessary. It is also not sufficient.

The most consequential critique came from Merrill Swain in 1985. Swain had studied French-immersion students in Canada — students who had gone to schools where French was the medium of instruction for years. They had read Maupassant. They had watched Quebecois films. Their receptive skills were strong; they understood almost everything. Their productive skills — grammar precision, vocabulary precision, the ability to generate sentences under pressure — lagged badly.

Swain's conclusion was precise: input alone is not enough. Learners need **pushed output** — moments where they have to produce language at or slightly above their current level, with sufficient communicative pressure that they must stretch their grammatical and lexical resources. Production does three things that reception cannot.

![Three-column diagram of the noticing, hypothesis-testing, and metalinguistic functions of pushed output. Each column contrasts what production does against what reception fails to do — production retrieves and updates; reception only recognizes.](../images/10-languages-with-ai-fig-01.png)
![Three things production does that comprehensible input cannot. Swain (1985).](images/10-languages-with-ai-fig-01.png)
*Figure 10.1 — Three things production does that comprehensible input cannot. Swain (1985).*

The first is what Swain called the *noticing function*. Producing language forces you to notice what you cannot yet say. You reach for a word; the word is not there; the absence becomes information you can act on. Reading the same passage a hundred times never creates that noticing event. The word is always there on the page. You never have to retrieve it.

The second is the *hypothesis-testing function*. Producing language forces you to make explicit guesses about how the language works. You try a sentence construction. It works or it doesn't. The feedback updates your developing internal grammar. Reception produces no hypothesis; there is nothing to test, because the native speaker already solved the construction problem for you.

The third is the *metalinguistic function*. Producing language creates the cognitive material that reflection can operate on. You can examine your own sentence in a way you cannot examine a sentence you read. The error in your sentence is yours to diagnose. The error in an AI-produced sentence belongs to AI.

Now look at Lucia's semester through this framework. Three semesters of comprehensible input — she has read enough Spanish that her receptive vocabulary is large. Zero pushed output — every writing assignment was AI-mediated. The oral exam result is exactly the receptive-productive gap Swain documented in 1985 in full-immersion environments. It took Swain's students years of genuine immersion to develop the gap. AI translation produces it in one semester.

The misconception worth retiring plainly: *"If I read enough Spanish, I'll be able to speak Spanish."* False. Swain showed it was false in the strongest possible setting. Reading produces receptive competence. Speaking and writing produce productive competence. The two draw on overlapping but distinct cognitive resources, and the productive resources require productive practice. Forty years of second-language-acquisition research confirms this. There is no shortcut.

---

## What Translation Tools Actually Do to Your Brain

The generation effect — established by Slamecka and Graf in 1978 — is the finding that self-generated information is remembered better than read information. The mechanism: generating an item requires you to retrieve it from existing memory, which strengthens the storage trace. Reading an item supplies it externally, which exercises recognition without building retrieval strength.

In language learning, nearly every productive act is a generation event. Producing a Spanish sentence requires lexical retrieval — pulling the word from your still-fragile second-language vocabulary. It requires grammar selection — choosing the syntactic frame, the tense, the agreement. It requires syntactic construction — building the sentence with rules that differ from your first language. And it requires error monitoring — watching the sentence as it forms, catching what sounds wrong, repairing mid-production.

Translation tools perform all of these for you in a single operation. The cognitive load drops to near-zero. The vocabulary is supplied externally; it is not retrieved from your lexicon. The grammar is constructed externally; you never select a tense. The error monitoring is done for you; there are no errors to catch. What appears in the output is correct Spanish. What does not appear — the retrieval events, the construction events, the monitoring events — is the schema that would have made you a Spanish speaker.

The empirical work on this is unambiguous. Research on machine translation tools in language learning found consistently that students who relied on them produced work that scored well on accuracy and badly on independent productive measures. More recent work in the LLM era finds the same pattern, often more severely, because LLMs produce better output than older translation systems — and so the gap between the artifact and the student's competence grows larger while remaining completely invisible in the grade.

A worked contrast — the same assignment, two workflows.

**Workflow A.** Student writes in English: *"The protagonist's loneliness intensifies when she realizes her family has moved on without her."* AI translates: *"La soledad de la protagonista se intensifica cuando se da cuenta de que su familia ha seguido adelante sin ella."* The student never retrieved *soledad*, never conjugated *se da cuenta*, never constructed *ha seguido adelante*. None of those productive events happened. The artifact is excellent. The cognitive structure is empty.

**Workflow B.** Student writes in Spanish from scratch: *"La soledad del protagonista se hace más fuerte cuando ella entiende que su familia ha continuado sin ella."* The Spanish has issues — a gender-agreement error (*del protagonista* for a female character), an idiomaticity gap (*se hace más fuerte* is grammatical but *se intensifica* is the more natural verb), a register choice (*ha continuado* versus the more natural *ha seguido adelante*). The student submits to AI with an error-explanation prompt after drafting. AI names the patterns and rules without correcting. The student rewrites by hand. The retrieval of *se intensifica*, the noticing of the gender error, the choice between two valid constructions — all of these are pushed-output events. The schema updates.

The artifact in Workflow A is better. The cognitive structure built in Workflow B is real.

| Cognitive event | Workflow A — AI translates | Workflow B — student drafts, AI explains |
|---|---|---|
| Who generates the sentence | AI | Student |
| Who selects vocabulary | AI | Student (from existing lexicon) |
| Who constructs grammar | AI | Student (tense, agreement, word order) |
| Error monitoring event | None — output is correct by construction | Student's own errors, named and studied |
| Productive memory built | None — no retrieval occurred | One trace per word retrieved |
| Interlanguage visible to teacher | No — artifact is AI's grammar | Yes — recurring rules diagnosable |
| What AI does | Everything | Names patterns *after* the draft is complete |

*Table 10.1 — Same tool. The difference is who did the generative work.*

---

## What Strategic Competence Is and Why AI Translation Destroys It

Michael Canale and Merrill Swain's 1980 framework for communicative competence identified four components of genuine fluency: grammatical competence (command of the rules), sociolinguistic competence (knowing what is appropriate in context), discourse competence (ability to produce coherent extended text), and **strategic competence** (ability to compensate when the other three fall short — paraphrasing, circumlocuting, asking for clarification when the precise word is unavailable).

Strategic competence is the one AI translation prevents from developing completely. You never have to compensate. You never have to ask *"how do I say this when I don't have the word?"* because AI always has the word. AI is a perfect vocabulary supply, which means you never develop the skill of communicating without perfect vocabulary. And perfect vocabulary is not what you have in any real conversation — in the airport, in the host family's kitchen, in the AP speaking section with a 20-second response window and no tools.

Two students in French 3 are asked to describe their summer vacation in conversation.

Student A has the larger vocabulary. She tries to say *"we went tubing on the river"* and doesn't know *tubing*. She freezes. Switches to English. The conversation breaks.

Student B has a smaller vocabulary. She wants to say the same thing. She says: *"On est allés à la rivière, dans des gros tubes en plastique, en flottant. Comme des pneus mais pour des personnes."* (We went to the river, in some big plastic tubes, floating. Like tires but for people.) The exchange student laughs and supplies *bouée*. The conversation continues.

Student B is the more fluent communicator. She has strategic competence. AI translation would have given Student A the word *bouée* instantly — and would have permanently prevented her from developing what Student B has.

![Two-path diagram showing the same trigger — an unknown word mid-conversation — splitting into an upper bypass path where AI supplies the word and strategic competence never builds, and a lower path where the student paraphrases, the interlocutor supplies the word, and strategic competence accrues.](../images/10-languages-with-ai-fig-02.png)
![The freeze is not the failure. The freeze that never becomes a paraphrase is.](images/10-languages-with-ai-fig-02.png)
*Figure 10.2 — The freeze is not the failure. The freeze that never becomes a paraphrase is.*

The oral fluency test is the right verification protocol for this chapter precisely because it tests all four competences simultaneously, with strategic competence load-bearing. Five minutes of unscripted conversation in the target language with no translation tools will reveal, with precision, whether you have surface vocabulary or productive fluency. A student who freezes at the word limit has been borrowing capability. A student who paraphrases around it has been building it.

---

## Why Your Errors Are Worth More Than You Think

Larry Selinker introduced the concept of *interlanguage* in 1972: the learner's evolving internal grammar — a rule-governed system that is neither the first language nor the target language but a developing third thing. Interlanguage progresses through stages in which specific errors are systematic (the learner has an internal rule that produces consistent errors) and then resolved (the rule restructures, those errors disappear, the next pattern emerges at a higher level).

The implication is counterintuitive: errors in your own production are not failures of learning. They are signatures of learning. A student whose Spanish is full of consistent gender-agreement errors has a visible interlanguage rule that can be diagnosed and addressed. A student whose Spanish has no errors because AI fixed them all has no interlanguage signature — there is nothing to diagnose, because no internal rule system has been built yet.

AI used correctly — error explanation after student-generated drafting — makes the interlanguage visible. AI returns: *you made this error three times; the underlying rule is X.* You see the signature directly. This is one of the genuinely novel pedagogical possibilities AI opens for language learners. But it is only possible if you have done the generative work that produces an interlanguage to read. A draft that AI produced has no interlanguage. It has AI's grammar.

![Two-panel diagram. Left panel — AI-translated workflow: ghosted steps from English draft to AI translation to grade A to no visible interlanguage and no schema. Right panel — student-generated workflow: solid steps from Spanish draft (with errors) to AI naming three patterns to student rewriting by hand to interlanguage visible and productive schema.](../images/10-languages-with-ai-fig-03.png)
![The errors in the right panel are evidence that learning is happening. Selinker (1972).](images/10-languages-with-ai-fig-03.png)
*Figure 10.3 — The errors in the right panel are evidence that learning is happening. Selinker (1972).*

A worked example — a French 2 student writes a paragraph and makes three consistent errors: using *à* where the verb requires *de*, conjugating *savoir* like a regular verb, defaulting to present *il y a* in a past-tense context. These are interlanguage signatures — each one reveals a specific rule the student has wrong. AI returns:

> *"Three patterns: verbs of the type **parler de** take **de**, not **à** — you used **à** three times with verbs requiring **de**. **Savoir** is irregular: **je sais, tu sais, il sait, nous savons, vous savez, ils savent**. You used **il y a** (present) in a past-tense context — **il y avait** is the imperfect equivalent. Which pattern would you like to work on first?"*

No correction. No rewriting. The student sees the interlanguage. She rewrites by hand, applying the three rules. The next paragraph has different errors. The cycle repeats. The interlanguage develops.

---

## The Human-Only Zone

The Human-Only Zone for languages is the strictest in this book. The cognitive event that builds productive competence happens at the level of every individual sentence. Every translated sentence is a sentence that did not get generated. Every word AI supplied during composition is a word that was not retrieved.

**AI-off zone:** drafting any text in the target language; selecting vocabulary during composition (mark gaps with bracketed English, do not look up until the draft is complete); constructing grammar during composition; forming any utterance during conversation.

**AI-on zone:** conversation practice in which you generate the language and AI responds in the target language; error explanation after independent drafting; vocabulary nuance clarification after a draft is complete; listening comprehension scaffolding.

The gate trigger is specific to languages: **AI opens for conversation (you speak first) or for error explanation (you draft first).** AI never opens for translation during composition. The gate must be enforced on each utterance, not each assignment. The Lucia failure mode is the cumulative consequence of small per-utterance violations — each individual translation seemed harmless; the semester-long total was the oral exam.

Two failure modes to name. The *mid-composition lookup* is the most common: you are writing in Spanish, you get stuck on a word, you reach for the translation. The fix is to write the English word in brackets and continue; address it after the draft. The *grammar-drill regression* is subtler: you use AI to generate conjugation exercises and become a fast conjugator without building discourse or strategic competence. Grammatical competence alone does not produce fluency. The conversation-partner prompt is where the load-bearing work happens.

| Situation | Gate | What you do | What AI does |
|---|---|---|---|
| Drafting text in target language | AI-off | Write; mark vocabulary gaps in brackets | Nothing |
| Vocabulary gap mid-composition | AI-off | Write the English word in brackets; continue | Nothing — look it up *after* the draft |
| Grammar construction | AI-off | Choose tense, agreement, word order yourself | Nothing |
| Conversation practice | AI-on (you speak first) | Generate every utterance; paraphrase when stuck | Responds in target language; holds back corrections |
| Error review post-draft | AI-on (you draft first) | Submit your draft; rewrite from AI's diagnostic | Names patterns and rules; does not correct |
| Vocabulary depth building | AI-on (after draft complete) | Use the target word in a new sentence each day | Evaluates idiomaticity; does not correct |

*Table 10.2 — The phase gate enforced per utterance, not per assignment.*

---

## The Six Prompts

### Prompt 1 — The Conversation Partner (Unscripted)

The most important prompt in this chapter. Use it 15–20 minutes a day.

```
We're going to have a conversation in [target language].

Rules:
1. We speak only [target language]. No English under any circumstances.
2. Match vocabulary and grammar to a learner at [your level: A2 / B1 /
   Spanish 2 / French 3]. Slightly above my comfortable level.
3. When I make an error, do NOT correct it. Continue the conversation.
4. When I cannot find a word, do NOT supply it. Wait. If I paraphrase
   or ask "¿cómo se dice X?" — still do not supply. Ask me a question
   that helps me arrive at it.
5. Ask follow-up questions to keep the conversation moving.

Start: ask me about my day.

After the conversation, when I say "review," switch to review mode:
identify recurring error patterns only — do not correct, just name.
```

### Prompt 2 — The Error Explanation Diagnostic (Post-Draft, No Correction)

Use after every piece of writing you produce independently.

```
I wrote this paragraph in [target language] without translation or
AI assistance. Pasted below.

Identify recurring error patterns. For each pattern:
1. Name the error category (gender agreement, verb conjugation,
   preposition selection, word order, register, etc.).
2. Quote the specific sentences where it appears.
3. Explain the underlying rule being violated — in English, briefly.
4. Do NOT correct the error. Do NOT rewrite any sentence.
   Do NOT propose alternatives.

Rank patterns by frequency. Tell me which one to focus on this week.
Ask me one question: which error pattern surprised me most?
```

### Prompt 3 — The Strategic Competence Builder

Use when you hit a word you don't know during conversation.

```
I'm trying to say [English idea] in [target language] but I don't
know the precise word.

Do NOT tell me the word.

Ask me three guiding questions that help me paraphrase using
vocabulary I already know:
1. What function does the word perform? What does it do or describe?
2. What related word might I already know?
3. What category does it belong to?

After my paraphrase attempt, evaluate ONLY whether a native speaker
would understand it. Do not propose the right word.
```

### Prompt 4 — The Vocabulary Depth Builder

Use after meeting a new word, across several days, to move it from receptive to productive memory.

```
I met this word today in [target language]: [word].
Context where I met it: [paste sentence or describe].
My current understanding: [one-sentence understanding].

1. Tell me ONE collocation it commonly appears with.
2. Tell me ONE register signal — formal, casual, regional?
3. Ask me to construct a sentence using the word in a different
   context from where I met it.
4. Evaluate ONLY whether my sentence is idiomatic. If not,
   do not correct — ask me to revise.

Tomorrow, ask me to use it in yet another new context.
The day after, use it in conversation.
```

### Prompt 5 — The Register / Sociolinguistic Explainer

Use when you have two of your own versions and are deciding which fits the relationship.

```
I'm trying to say [sentence in target language] in [specific context:
texting a friend / formal email to teacher / host family, etc.].

I have two versions:
- Version A: [paste]
- Version B: [paste]

Don't pick one. Don't write a third version.

Explain:
1. What register signal each version sends.
2. What the recipient would infer about my relationship to them.
3. Where each would be appropriate and where each would be wrong.

Ask me which version fits the relationship I want to establish.
```

### Prompt 6 — The Listening Comprehension Scaffold

```
I want to practice listening comprehension in [target language]
on [topic].

Generate a 3-minute script at [my level], at natural speed:
- Vocabulary I likely know with 2–3 new words inferrable from context.
- Grammar I have already met.
- Substantive content — not "Maria goes to the store."

Deliver line by line, pausing for me to acknowledge each line.
After the full script:
1. Ask me to summarize what I heard.
2. Identify the new words and ask what I think they meant from context.
3. Confirm meanings only after I've guessed.
```

---

## Lucia Redoes the Semester

After the oral exam, Señora Vasquez is gentle and direct: *Lucia, tu español escrito es excelente, pero algo no está conectando en la conversación. ¿Quieres hablar sobre esto?* Lucia, on the bus home, decides to do the second semester differently. She does not stop using AI. She changes how.

The new daily routine: 20 minutes of conversation practice per day using Prompt 1. The first three are painful — long pauses, English insertions, the same six verbs. The fourth is slightly better. The eighth is much better. By the end of the first week she has had over two hours of pushed-output practice — more than she had in the entire first semester.

Writing assignments, AI off for drafting. When Señora Vasquez assigns a written reflection on a film, Lucia drafts in Spanish, by hand, on paper. The first draft is slow and ugly. She marks gaps with bracketed English words — *[reluctant], [outskirts], [betrayed]* — and continues. The first draft takes 90 minutes. The old AI-mediated version took 25.

AI on, error explanation after drafting. Lucia submits to ChatGPT with Prompt 2. Five recurring error patterns come back: gender agreement on words ending in unexpected letters, preterite-imperfect confusion, missing personal *a* before direct-object people, the *ser*-vs-*estar* split, and over-use of *muy* where Spanish prefers the *-ísimo* intensifier suffix. AI ranks them by frequency. AI corrects nothing. Lucia rewrites by hand, applying the rules one pattern at a time.

The bracketed gaps become the vocabulary working list for the week. She uses Prompt 4 on each one. *Reluctant* becomes *reticente* — she uses it in three different sentences across three days. *Outskirts* becomes *las afueras*. *Betrayed* becomes *traicionar*. By the end of the week she has not merely learned three words — she has deployed them in her own output, with feedback, in varied contexts. They are in productive memory.

During her daily conversations she hits unknown words constantly. She uses Prompt 3 to get paraphrase questions rather than the word itself. After two weeks her conversations no longer break when she hits an unknown word. She has a repertoire of paraphrase strategies — *"como, pero más...", "es una cosa que sirve para...", "no recuerdo la palabra, pero..."* — and they keep things moving.

Twelve weeks later, Lucia sits down again with Señora Vasquez. She talks for fifteen minutes. She uses verbs she did not know in December. She paraphrases around two words she still doesn't know. She makes mistakes — gender agreement slips twice, a *ser*/*estar* confusion, one sentence she repairs mid-flow. Señora Vasquez nods. Afterward: *Lucia, esto es completamente diferente. Has trabajado mucho. Estás hablando ahora.* (This is completely different. You've worked hard. You're speaking now.)

AI did three things this semester: ran conversations, explained errors after independent drafts, deepened vocabulary across days. AI did not translate. AI did not draft. AI did not supply words mid-composition. The cognitive event that builds productive fluency — Swain's pushed output — happened thousands of times across the semester, each time in Lucia's head. The schema is hers.

![Grouped bar chart comparing Lucia's written and oral assessment scores across two semesters. Semester 1: written 92, oral 55 — a 37-point gap. Semester 2: written 88, oral 83 — a 5-point gap. Written grade falls 4 points; oral score rises 28 points.](../images/10-languages-with-ai-fig-04.png)
![Written falls 4; oral rises 28. The gap closes because productive competence was built, not borrowed.](images/10-languages-with-ai-fig-04.png)
*Figure 10.4 — Written falls 4; oral rises 28. The gap closes because productive competence was built, not borrowed.*

---

## Exercises

### Warm-Up

**1.** Locate the last writing assignment you produced in your target language. Without re-reading it, write down every vocabulary word you remember using. Then open the assignment and compare the list. The words on both lists are in productive memory. The words on the assignment but not on your list were supplied by AI or by a dictionary during composition and never retrieved since. *(Tests productive vs. receptive vocabulary distinction. No target language required — this is a diagnostic, not a production exercise.)*

**2.** Describe, in your target language, what you ate today. No dictionary, no AI, no notes. One paragraph. Mark every word you had to pause on with an asterisk. The asterisked words are the frontier of your productive vocabulary — the boundary where reception ends and productive uncertainty begins. *(Tests current productive vocabulary baseline; generates a personal working list.)*

**3.** In English, describe the difference between Krashen's Input Hypothesis and Swain's pushed-output hypothesis. Then describe what Lucia's oral exam revealed about which one she had been relying on. *(Tests whether the chapter's central theoretical distinction is understood well enough to be applied to a concrete case.)*

---

### Application

**4.** Use Prompt 1 for fifteen minutes in your target language. Immediately after, write down: the three moments you were most fluent, the three moments you most wanted to switch to English, and the single word whose absence cost you the most. The word whose absence cost you most is the first entry in this week's vocabulary depth-building list (Prompt 4). *(Tests application of the conversation-partner workflow; generates actionable vocabulary data.)*

**5.** Draft one paragraph in your target language on any topic, AI off, by hand. Mark vocabulary gaps with brackets. Then submit to Prompt 2. Write down the top-ranked error pattern AI identifies. Rewrite the paragraph by hand, addressing that pattern only — leave the others for next week. Compare the two drafts: did the targeted pattern improve? *(Tests the draft-then-diagnose workflow; forces deliberate interlanguage engagement rather than global correction.)*

**6.** Locate a sentence you would naturally say in English that contains a word you do not know in your target language. Use Prompt 3 to build a paraphrase rather than receiving the translation. Write down the paraphrase you arrived at, the word AI eventually confirmed (if it did), and one new sentence using that word in a different context. *(Tests strategic competence development — the paraphrase discipline is the exercise, not the vocabulary acquisition.)*

---

### Synthesis

**7.** A classmate argues: "I use Google Translate for my drafts, then I read the Spanish carefully to learn from it. That's basically the same as writing it myself, since I'm studying the output." Using Swain's three functions of pushed output — noticing, hypothesis-testing, metalinguistic — identify specifically which functions the classmate's workflow produces and which it does not. Then predict what that classmate's oral exam will look like. *(Tests integration of Swain's framework with the translation-bypass argument; requires applying all three functions to evaluate a concrete study behavior.)*

**8.** Design a two-week vocabulary acquisition plan for five words from your current unit using Prompt 4. The plan should specify: what sentence you will generate on day 1, what different context you will use on day 2, how you will incorporate each word into a conversation by day 3, and how you will verify productive memory (not just recognition) at day 14. *(Tests whether the student can operationalize the receptive-to-productive vocabulary transfer principle into a concrete, schedulable practice.)*

---

### Challenge

**9.** Run the five-minute cold conversation from the LLM Exercise. Then run it again one week later on the same topic without reviewing the first conversation. Compare the two recordings: which words were still unavailable the second time? Which new gaps appeared? Write a paragraph interpreting the pattern — what does it tell you about how your productive vocabulary is (or is not) consolidating? *(Open-ended; tests whether the student can function as their own longitudinal diagnostician using spacing-effect logic applied to productive vocabulary.)*

---

## LLM Exercises

**Exercise: Five-Minute Cold Conversation.** Open AI in voice mode or chat. Have a five-minute conversation in your target language. Topic: what you did today. No translation tools, no looking up words, no notes. Where you get stuck, paraphrase or ask for clarification *in the target language*. After the conversation, write down: (1) the words you could not retrieve, (2) the moments you switched strategies. The list of words is your productive-vocabulary gap for this week. The moments you switched strategies — or didn't and froze instead — tell you whether your strategic competence is forming. Run this exercise at the start of every new study unit and at the end. The gap between the two readings is the workflow working.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Maximilian Berlitz (1852–1921)** was a German-American language teacher who, in 1878, in a Providence, Rhode Island schoolroom, accidentally invented what would become the dominant method of immersive language instruction. The story is that he hired a French assistant, fell ill before classes began, and instructed the assistant by note to "just teach French" without explaining that the man spoke no English. The students, after a moment of panic, began to learn — by gesture, by repetition, by being unable to escape the target language. Berlitz noticed. He systematized. By 1900 his schools had spread across Europe and the United States; the *Berlitz Direct Method* was the standard alternative to the grammar-translation tradition that had ruled language teaching since the medieval Latin schools.

The Direct Method rules: only the target language in the classroom. No translation, ever. Vocabulary taught through objects and demonstration, not through L1 glosses. Grammar acquired inductively from examples, not deducted from rule lists. Speaking and listening come before reading and writing. Errors are corrected through reformulation in the target language, not through L1 explanation.

The pedagogical bet underneath the method is the same one this chapter has been making — that productive competence is built by producing the language, not by being shown its translation. Berlitz did not have Swain's vocabulary for pushed output or Selinker's for interlanguage. He had a hundred classrooms reporting the same result: students who were forced to generate the language produced fluency that students who studied translations did not. The method survived because the result was reproducible.

Read against the AI-translation problem in this chapter, Berlitz reads as a warning written before the technology existed. The Direct Method was an act of deliberate scarcity — the teacher pretended not to speak the student's language so the student would have to retrieve, paraphrase, fail, and try again. AI translation is the opposite act: the teacher who always has the word, the construction, the polished sentence. The students Berlitz refused to translate for went on to speak. Lucia, given perfect translation for every assignment, lost her voice. The mechanism is one mechanism. Berlitz built schools around it 140 years before Swain named it.

![Maximilian Berlitz, circa 1900. AI-generated portrait based on a public domain photograph.](../images/maximilian-berlitz.jpg)
*Maximilian Berlitz, circa 1900. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Maximilian Berlitz, and how does his 1878 Direct Method
(target-language-only immersion, no translation, vocabulary through
demonstration) connect to the AI-translation argument in this chapter —
specifically Swain's pushed-output hypothesis, Canale & Swain's strategic
competence, and Selinker's interlanguage? Keep it to three paragraphs.
End with the single most surprising thing about how the method spread.
```

→ Search **"Maximilian Berlitz"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to compare Berlitz's Direct Method to a contemporary AI conversation-partner prompt — what is the same mechanism, what is different about the tool?
- Ask what Berlitz would have done with an AI translator on every student's desk, and where his method would have to bend.

What changes? What gets better? What gets worse?

---

## Bridge to Chapter 11

The languages chapter has been the strictest application of the phase gate in this book — every productive utterance in the target language must be the student's, with no AI at the moment of composition. The next chapter moves to history, politics, and the social sciences, where the Human-Only Zone takes a different shape: the cognitive event that builds historical thinking is the interpretive event — moving from primary sources to causal argument, holding multiple theoretical frameworks in productive tension. The phase gate refigured for historical interpretation is what Chapter 11 builds. The argument is the same. The cognitive economy is different. The Nicholas thread that has run through this book finds its full operational form in the next chapter.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 10.1 — Three things production does that comprehensible input cannot. Swain (1985).

Create a standalone D3 v7 HTML file for a concept map titled "Three things production does that comprehensible input cannot. Swain (1985).". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-languages-with-ai-fig-01.html`

---

### Figure 10.2 — The freeze is not the failure. The freeze that never becomes a paraphrase is.

Create a standalone D3 v7 HTML file for a concept map titled "The freeze is not the failure. The freeze that never becomes a paraphrase is.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-languages-with-ai-fig-02.html`

---

### Figure 10.3 — The errors in the right panel are evidence that learning is happening. Selinker (1972).

Create a standalone D3 v7 HTML file for a concept map titled "The errors in the right panel are evidence that learning is happening. Selinker (1972).". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-languages-with-ai-fig-03.html`

---

### Figure 10.4 — Written falls 4; oral rises 28. The gap closes because productive competence was built, not borrowed.

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Written falls 4; oral rises 28. The gap closes because productive competence was built, not borrowed.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-languages-with-ai-fig-04.html`
