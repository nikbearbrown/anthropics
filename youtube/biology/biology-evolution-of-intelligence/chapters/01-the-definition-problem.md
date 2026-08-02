# Chapter 1 — The Definition Problem

Here is a strange thing to start with.

In 1986, two dozen serious researchers were each asked to write down what they meant by the word *intelligence*. Not to review the debate. Not to summarize the literature. Just to say, plainly, what the thing was.

They produced twenty-four definitions. Not twenty-four phrasings of the same idea. Twenty-four definitions that did not fit together and in several cases barely seemed to be addressing the same subject.

Now, you might think: well, this is a young field. Give it time. Except that eight years later, fifty-two of those same researchers — overlapping communities, serious people — signed an open letter in the *Wall Street Journal* offering twenty-five numbered statements as settled scientific consensus. *Intelligence is a general mental capability. It can be measured accurately. It predicts outcomes across life domains.* Confident. Settled. Done.

Two documents. Both careful. Endorsed by many of the same people. One describing irreducible disagreement. The other describing resolved consensus.

I want you to sit with that for a moment. Not because it means the researchers were confused — they were not. Not because it means intelligence is not real — it is. It means something more interesting than either of those things: the word *intelligence* has been doing different jobs for different people, and each job is legitimate. The path forward is not to pick the winner and crown it. The path forward is to figure out which job we need the word to do — and then use it for that job consistently, without pretending the other jobs do not exist.

That is what this chapter is actually about.

---

Let me show you what I mean with a single example. This is the cleanest move I know: take one case, run it through several definitions, watch what changes.

A border collie named Chaser, studied at Wofford College, was taught the proper names of objects. Not categories — proper names. One toy per word, like names for people. By the end of three years she knew 1,022 of them. But here is the part that is interesting. When her handlers placed a new object she had never seen among familiar ones and asked her to fetch "Darwin" — a name she had never heard — she went for the new one. Not because she knew what Darwin was. Because she knew what it was not. Whatever "Darwin" meant, it was not any of the thousand things she already knew. So it had to be the new one.

Is that intelligent?

Hold the question. Do not answer it yet. Instead, watch what happens when you run Chaser through five different definitions.

Run her through Alfred Binet's 1905 definition: intelligence as practical judgment, initiative, and above all *auto-critique* — the capacity to examine and correct one's own thinking. Chaser adapts. She shows something like initiative. But auto-critique, a self examining its own reasoning process, is hard to attribute to a dog retrieving by elimination. Under Binet: uncertain.

Run her through David Wechsler's 1944 definition: the aggregate or global capacity to act purposefully, think rationally, and deal effectively with the environment. Chaser deals effectively. She acts purposefully. She handles novel referents across varying arrangements. Under Wechsler: included, without hesitation.

Run her through Howard Gardner's framework: multiple distinct intelligences, each neurally independent, each visible in those unusual cases where one capacity is superhuman and the others unremarkable. Chaser has referential mapping over a thousand names. She responds to syntactic structure — "to ball, take frisbee" means something different to her than "to frisbee, take ball." Under Gardner: included, at minimum for linguistic intelligence.

Run her through the definition this book will use. Shane Legg and Marcus Hutter surveyed over seventy definitions of intelligence and distilled their common content into one sentence: *intelligence is an agent's ability to achieve goals in a wide range of environments*. Chaser's goal is retrieving the correct object. The environment varies — new objects, new names, different arrangements. She achieves the goal across those variations. Under Legg–Hutter: included, without qualification.

Run her through François Chollet's 2019 definition, which focuses not on what an agent can do but on how efficiently it learns to do new things given what it already knows. Chaser did learn new words from small amounts of data. But the cross-domain transfer Chollet is really asking about — does she take what she learned about word-object mapping and use it to, say, figure out tool use she has never seen — is hard to test in a dog. Under Chollet: uncertain.

Same facts. Same dog. Two confident inclusions. Two uncertains. One partial. None of these verdicts is wrong. Each is the correct verdict given the sieve it uses. The disagreement is not about Chaser. The disagreement is about which question to ask.

---

Now I need to be honest with you about something that should give any careful reader of intelligence research real pause, before we go any further.

Much of the psychometric tradition rests on a thing called *g* — the general factor that appears when you run principal component analysis on a battery of cognitive tests. It loads positively on all of them. It predicts outcomes. It is heritable. Researchers treat it as a discovered property of the mind, something the tests are measuring because it is actually there.

The statistician Cosma Shalizi made a technical argument about this that has a sharp conclusion: any set of positively correlated variables, regardless of what they actually measure, will produce a first principal component that loads positively on all of them. The mathematics forces it. Take horsepower, top speed, and sticker price of cars. Run principal component analysis. A "general car-quality factor" pops out. Nobody thinks there is a single thing called *car quality* hidden underneath those numbers. The algebra creates the appearance of it whether or not it is real.

Shalizi's claim is not that the tests are useless, not that the correlations are fabricated. The claim is that interpreting *g* as a unified biological entity runs far ahead of what the data demonstrates. The biological correlates defenders point to — heritability, neural signatures, predictive validity — are real. Whether they trace back to a single underlying capacity or to a family of partially overlapping capacities that happen to be correlated is the open question, and the principal component analysis does not resolve it.

This is not a fringe position. It is a serious methodological debate among people who agree on every number. And it should make us modest about any definition that stakes too much on *g* as its foundation.

The second critique cuts differently and comes from the primatologist Frans de Waal. His observation is about comparative cognition research — the enterprise of testing whether animals are intelligent — and it is uncomfortable because it applies to almost everything in the literature before about 1990.

The history of testing animal intelligence, de Waal argues, is largely the history of designing tests around a human's perceptual and behavioral world and then concluding from the animal's failure that the animal lacks the capacity. The biologist Jakob von Uexküll called this the *Umwelt* — the self-world, the bubble of sensory experience each organism inhabits. Every organism lives in its own Umwelt. The problem is that experimenters kept building tests inside the human Umwelt and scoring animals on whether they could operate there.

Chimpanzees were judged unable to use tools until researchers spent time watching them in the wild. Octopuses were tested in dim laboratory conditions at the wrong temperature and concluded to be cognitively limited. Dogs were evaluated on whether they would imitate humans by watching humans, not other dogs. In each case the organism failed. In each case the conclusion was *absence of capacity* rather than *failure of experimental design*.

De Waal's point is not that animals always turn out smarter than we thought. Sometimes they do; sometimes they do not. The point is that you cannot know until you build the test inside the organism's own Umwelt. And the methodological correction has been happening slowly, lab by lab, as researchers discover that the animal they thought was failing was solving a different problem than the one they had posed.

Keep both of these critiques in your back pocket. Shalizi cuts at the data infrastructure psychometric definitions rest on. De Waal cuts at the assumption that there is a neutral place to evaluate intelligence from at all. Neither argument destroys the enterprise. Both arguments constrain how confident we should be in any particular verdict.

---

Now here is where I have to make a choice, and I want you to see exactly why.

This book is going to compare a nematode, a slime mold, a honeybee, a crow, a dog, and a large language model on the same question. You cannot do that comparison without deciding in advance what you are comparing. Refusing to pick a definition is not neutrality — it is leaving whatever definition floats into view to do the work invisibly. And that is worse.

Watch what happens across the same organisms as you move through just four of the definitions:

The nematode *C. elegans* has 302 neurons. It habituates. It learns associatively. It modulates its behavior based on experience. Under Binet, who required judgment — an active, self-correcting engagement with a problem — the nematode is excluded. A worm following a chemical gradient via a fixed neural circuit, however elegant that circuit is, is not what Binet meant. Under Wechsler, who asked for aggregate adaptive capacity, the nematode starts to slip through — it does adapt, in modest ways, to its environment. Under Legg–Hutter, the nematode is included: it achieves goals in its environment. The interesting question is not whether it qualifies but how intelligent it is and in what shape.

A chess engine beats every human player alive. It cannot learn to play checkers from scratch without being rebuilt. Under Binet, excluded — no auto-critique, no general judgment. Under Wechsler, excluded — it has no broader purpose and does not deal with anything resembling a human environment. Under Legg–Hutter, included in one extremely narrow environment and absent everywhere else. Under Chollet, whose whole point is that high performance on a single task tells you almost nothing — excluded dramatically. High performance without transfer is the failure mode his definition was built to detect.

A large language model, trained on the bulk of human text, scores impressively on enough standardized tests to be unsettling. Under Legg–Hutter it is included within text environments and largely absent outside them. Under Chollet — and this is the live debate — the verdict turns on a question we do not yet know how to answer: is what the model does when it handles a new prompt genuine in-context learning, or is it retrieval from a training distribution so broad that almost nothing is genuinely new? The model has in a sense already seen everything. Give it a novel visual reasoning puzzle and three examples and ask it to infer the rule — the way a human can from almost nothing — and it fails in a way that is diagnostic. The failure is not about how much the system knows. It is about whether knowing transfers to learning.

The definition I am adopting is Legg–Hutter, and I want to tell you exactly why and exactly what it costs.

The reason is threefold. First, it is substrate-neutral. It does not mention neurons, language, or carbon-based chemistry. A bacterium and a transformer are evaluated on the same criterion. That is the only way to do the comparative work this book requires. Second, it is graded, not binary. A nematode and a human are both in the conversation; the interesting question is the shape of their intelligence, not whether they qualify. Third, it is operational. Given an agent and an environment, you can in principle run an experiment.

The formal version is a measure over agents expressed as a sum across all computable environments, weighted by the Kolmogorov complexity of each environment — the length of the shortest program that would generate it. Simpler environments count more. It is Occam's Razor formalized. The sum is incomputable in practice, but the principle is testable comparatively, and that is all we need.

The cost is real and worth naming. The definition flattens affect. It treats agents as goal-pursuers when real animals are also moods, memories, attachments, whole inner worlds that a reward signal cannot easily capture. It will struggle most in chapters on emotion, on social intelligence, and on creativity. In those chapters I will reach for other tools — Sternberg when the organism is reshaping the environment that is reshaping it back; Chollet when the question is whether a language model is learning or retrieving; de Waal when the experimental design has been built around the wrong Umwelt. A working instrument is allowed to be imperfect. It is not allowed to be hidden.

---

Let me close with the thing I think people find hardest to accept about this situation.

There is a widespread intuition that a century of research should have converged on a definition by now. If the thing is real, we should be able to say what it is. The failure to converge feels like a scandal or a sign that the whole enterprise is confused.

I do not think that is the right reading. Consider *gene*. Biologists worked productively with the gene concept for fifty years before molecular biology gave it a clean physical definition. They were not confused; they were using an operational concept within studies, carefully, and building knowledge the whole time. Consider *species*. There are at least twenty-six competing species concepts in current use across biology. Biologists argue about the right one constantly. They also make enormous progress. What science requires is not a complete definition. It requires an operational specification within a study — a clear statement of which sieve is being used and what is being measured.

The argument is not that intelligence has no definition. The argument is that intelligence picks out a family of overlapping capacities — judgment, adaptation, goal achievement, skill acquisition — and different definitions foreground different members of the family for different purposes. The cases share overlapping features without any single feature they all share. Wittgenstein called this family resemblance. It is closer to *family resemblance* than it is to *atomic number*.

That is not a retreat. That is the accurate description of what is going on.

The question mark in this book's title is the thesis. Not a hedge. Not a rhetorical gesture. The study of intelligence has not arrived at its destination. It is in the middle of something, the way evolutionary biology was in the middle of something in 1859 when it had variation and selection but not yet a mechanism for inheritance — the way physics was in the middle of something in 1905 when it had special relativity but not yet general relativity or quantum mechanics. The right response to being in the middle of something is not to pretend you are not.

The next chapter walks further back than most discussions of intelligence dare to go — to bacteria, slime molds, and plants — and asks whether anything a brainless organism does deserves the word. The answer depends entirely on the sieve we just chose. By the end of that chapter you should feel that the choice was real and that it was worth making.

The worm in the petri dish is waiting.

---

## LLM Exercise — build `01-definition-sieve.html`

**Project:** Skeptic's Notebook on Frontier AI — Chapter 1 artifact

**What you're building:** A small interactive page that lets the reader pick a definition and an organism and see the verdict plus the criterion that produced it. By the end of the chapter you will have a sieve-runner that makes the central argument visible.

**Tool:** Claude Code (preferred), or a Claude/ChatGPT project with file output.

---

This is the four-move scaffold for every LLM-coding task in the book. Use it explicitly the first time; internalize it after.

**SHOW** — give the model the artifact specification, in full:

```
I am building 01-definition-sieve.html for a textbook chapter on the
definition of intelligence.

UI elements:
1. A dropdown for "Definition": Binet, Wechsler, Sternberg, Gardner,
   Legg–Hutter, Chollet.
2. A dropdown for "Organism": bacterium, honeybee, archerfish, border
   collie, chimpanzee, human, GPT-4.
3. A "Verdict" panel that shows: verdict (Included / Excluded /
   Uncertain), the specific criterion that drove the verdict, and a
   one-sentence reason.
4. A table view showing all organisms × all definitions, color-coded
   by verdict (green = included, red = excluded, yellow = uncertain).

Visual: clean, no framework dependencies. Plain HTML + CSS + vanilla JS
in one file. The verdict data lives in a single JS object literal at the
top of the file so the reader can edit it directly.
```

**SAY** — give the model the data, explicitly, so it does not invent it:

```
Use exactly this verdict data. Do not invent additional rows.
(Then paste the verdict matrix from §6 of the chapter.)
```

**CONSTRAIN** — name what the model must not do:

```
Constraints:
- Single HTML file. No build step. No npm.
- No external CSS or JS dependencies.
- No fabricated verdicts beyond the matrix supplied.
- The file must open correctly in a modern browser by double-click.
- Total file size under 25KB.
```

**VERIFY** — name how you will check the output:

```
Verification:
1. Open the file. Does the dropdown change the verdict panel correctly
   for all 6 × 7 = 42 combinations?
2. Does the table view color-code correctly?
3. Are the criteria stated in the chapter the same as the criteria
   shown in the verdict panel?
4. Does the file pass an HTML validator?
```

---

Once the artifact builds, push on three things:

1. Add an eighth organism: a slime mold (*Physarum polycephalum*). What verdict do you write under each definition? Where does Binet land you that Legg–Hutter does not?
2. Add a seventh definition: Searle's Chinese Room criterion — does the system have genuine understanding or syntactic manipulation only. Which systems flip verdict?
3. Add a "confidence" field for each cell — high / medium / low. Which cells are you confident about? The pattern of confidence is its own argument.

In Chapter 2 you will add three brainless organisms to the page: *E. coli* (chemotaxis), *Physarum* (slime mold), and an oak seedling (phototropism). The same six-definition sieve will make visible whether each definition has anything to say about agents without nervous systems. Save your `01-definition-sieve.html` file. You will edit it next chapter, not replace it.
