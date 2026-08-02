# Chapter 1 — The Definition Problem

Here is a strange thing to start with.

In 1986, the psychologists Robert Sternberg and Douglas Detterman did something that sounds almost too simple to be a research project. They asked roughly two dozen of the leading experts on intelligence to write down, plainly, what they meant by the word. Not to review the literature. Not to argue. Just to say what the thing was.

They got two dozen answers. Not two dozen phrasings of one idea — two dozen definitions that did not fit together, and in several cases barely seemed to be describing the same subject. One expert located intelligence in the capacity to learn. Another in the ability to adapt to the environment. Another in abstract reasoning, another in the speed of mental processing, another in metacognition — the mind watching itself think. The volume has a title that reads, in hindsight, like a confession: *What Is Intelligence?*

Now, you might say: young field, give it time. Except that eight years later, a different group put its name to the opposite claim. In December 1994, the *Wall Street Journal* ran an open letter titled "Mainstream Science on Intelligence," drafted by the psychologist Linda Gottfredson, offering twenty-five numbered statements as settled scientific consensus. *Intelligence is a general mental capability. It can be measured accurately. It predicts outcomes across the domains of life.* Confident. Settled. Done. Fifty-two researchers signed it.

I want to be careful here, because the easy version of this story is wrong, and the true version is better. The two documents were not signed by the same people. The 1986 contributors were a broad mix — cognitive psychologists, developmentalists, artificial-intelligence researchers, psychometricians — gathered by Sternberg and Detterman precisely to air disagreement. The 1994 signatories were largely a different community, a bloc of differential and psychometric psychologists rallying, in the heat of the *Bell Curve* controversy that fall, to assert agreement. These are not the same fifty-two people changing their minds. They are two snapshots of one field, eight years apart, pointed in opposite directions.

And the 1994 letter carries a detail that tells you more than its confident tone does. Gottfredson sent it to 131 experts. Fifty-two signed. Forty-eight explicitly declined. Thirty-one did not answer. A document asserting consensus could not get a majority of the people it was mailed to even to put their name on it. That refusal rate is the better illustration of where the field actually stood. There was no consensus. There was a letter claiming one.

![A single horizontal bar divided into three segments representing the 131 experts contacted for the 1994 letter: a red segment of 52 who signed, a grey segment of 48 who declined, and a light-grey segment of 31 who did not answer, with a dashed line marking the halfway point that the signed group falls short of.](images/01-the-definition-problem-fig-02.png)

*Figure 1.2 — Of 131 experts mailed the 1994 consensus letter, only 52 signed — fewer than 40%; the refusal rate, not the confident wording, marks where the field stood.*

Sit with that for a moment — not because it means the researchers were confused. They were not. Not because intelligence is not real. It is. It means something more interesting: the word *intelligence* has been doing different jobs for different people, and each job is legitimate. The path forward is not to crown a winner. It is to figure out which job you need the word to do, and then use it for that job consistently, without pretending the others do not exist.

That is what this chapter is about.

---

Let me show you what I mean with a single case. This is the cleanest move I know — take one example, run it through several definitions, watch what changes.

A border collie named Chaser lived at Wofford College in South Carolina, where the psychologist John Pilley spent some five hours a day, over three years, teaching her the proper names of objects. Not categories — proper names. One toy, one word, the way you name a person. By the end she knew 1,022 of them, the largest tested vocabulary of any non-human animal. But the number is not the interesting part. The interesting part is what happened when Pilley set a new toy she had never seen among familiar ones and asked her to fetch a name she had never heard. She went for the new one. Not because she knew what the new name meant. Because she knew it was not any of the thousand things she already knew. Whatever the word pointed to, it had to be the unfamiliar object. She reasoned by exclusion.

Is that intelligent?

Hold the question. Do not answer it. Watch instead what happens when you run Chaser through five different definitions, each a different sieve.

Run her through Alfred Binet's, from 1905, the definition built into the first practical intelligence test. Binet asked for judgment, initiative, and above all *autocritique* — the mind's capacity to examine and correct its own reasoning. Chaser adapts; she shows something like initiative. But a self watching itself reason is hard to attribute to a dog retrieving by elimination. Under Binet: uncertain.

Run her through David Wechsler's, from 1944 — "the aggregate or global capacity of the individual to act purposefully, to think rationally, and to deal effectively with his environment." Chaser acts purposefully. She handles novel words across changing arrangements of toys. She deals effectively. Under Wechsler: included, without hesitation.

Run her through Howard Gardner's framework of multiple intelligences — the claim that the mind holds several neurally distinct capacities rather than one. Chaser maps over a thousand referents and responds to the structure of a request. Under Gardner, at least for linguistic intelligence: included.

Run her through the definition this book will adopt. The computer scientists Shane Legg and Marcus Hutter collected more than seventy published definitions of intelligence and distilled the shared content into one sentence: *intelligence measures an agent's ability to achieve goals in a wide range of environments.* Chaser's goal is to retrieve the right object; the environment varies — new toys, new names, new arrangements — and she achieves the goal across the variation. Under Legg–Hutter: included, without qualification.

Run her, finally, through François Chollet's, from 2019, which asks not what an agent can do but how efficiently it learns to do new things given what it already knows. Chaser did learn words from small amounts of data. But the deeper transfer Chollet is probing — does she take what she learned about words and use it to solve some unrelated novel problem — is hard to test in a dog. Under Chollet: uncertain.

![A five-row matrix listing the definitions of Binet, Wechsler, Gardner, Legg–Hutter, and Chollet, each with the criterion it asks for and a verdict on Chaser the border collie: uncertain, included, included, included, uncertain. The Legg–Hutter row is highlighted in red and marked as the definition adopted by the book.](images/01-the-definition-problem-fig-01.png)

*Figure 1.1 — The same dog run through five definitions yields different verdicts; the book adopts Legg–Hutter (red), under which Chaser is included without qualification.*

Same facts. Same dog. Two confident inclusions, two uncertains, one partial. None of these verdicts is wrong. Each is correct given the sieve it uses. The disagreement is not about Chaser. The disagreement is about which question to ask.

---

Now I owe you some honesty about the ground under the most influential of these traditions, before we go further.

Much of psychometrics rests on a quantity called *g* — the general factor that emerges when you run a battery of cognitive tests through factor analysis. People who do well on one test tend to do well on the others; that shared variance is *g*. It is heritable. It predicts outcomes. It has neural correlates. And a great deal of the field treats it as a discovered thing, a real property of the mind that the tests are detecting because it is genuinely there.

The statistician Cosma Shalizi made an argument about this with a sharp edge. Take any set of variables that happen to be positively correlated with one another — it does not matter what they measure — and run them through factor analysis, or the closely related principal-component analysis, and you will always extract a first factor that loads positively on all of them. The mathematics forces it. His example: take the horsepower, top speed, and sticker price of cars. They are correlated. Run the analysis and a "general car-quality factor" pops out, loading positively on all three. Nobody believes there is a single hidden essence called car quality humming underneath the steel. The algebra manufactures the appearance of one whether the thing exists or not.

Shalizi's point is not that the tests are useless or the correlations faked. They are real. His point is that interpreting *g* as a single unified biological entity runs well ahead of what the data can show. The heritability, the neural signatures, the predictive power are all genuine; whether they trace back to one underlying capacity or to a family of overlapping capacities that happen to correlate is the open question, and the factor analysis cannot settle it. This is not a fringe complaint. It is a serious methodological dispute among people who agree on every number. And it should make us modest about any definition that stakes too much on *g* as bedrock.

A second critique cuts from a different angle, and it comes from the primatologist Frans de Waal. His subject is the whole enterprise of testing whether animals are intelligent, and his charge is uncomfortable because it applies to most of the literature before about 1990. The history of animal-intelligence testing, de Waal argues, is largely the history of building a test inside the human sensory world and then concluding, from an animal's failure inside it, that the animal lacks the capacity. The biologist Jakob von Uexküll had a word for the bubble of perception each organism inhabits — the *Umwelt*, the self-world. Every creature lives in its own. The error was to keep building tests inside the human Umwelt and grading other animals on how well they could operate there.

Chimpanzees were judged poor tool-users until researchers watched them in the wild. Octopuses were tested in cold, dim tanks at the wrong temperature and pronounced dull. Dogs were scored on whether they would imitate humans, by watching humans, rather than other dogs. Each animal failed; each failure was read as absence of capacity rather than failure of design. De Waal's claim is not that animals are always smarter than we thought — sometimes yes, sometimes no. It is that you cannot know until you build the test inside the organism's own Umwelt.

Keep both critiques in your pocket. Shalizi cuts at the statistical foundation under psychometric definitions. De Waal cuts at the assumption that there is any neutral place to judge intelligence from at all. Neither argument destroys the project. Both constrain how confident any single verdict is allowed to be.

---

Now I have to make a choice, and I want you to see exactly why.

This book is going to compare a nematode, a slime mold, a honeybee, a crow, a dog, and a large language model on the same question. You cannot run that comparison without deciding in advance what you are comparing. Refusing to pick a definition is not neutrality — it just lets whatever definition happens to float into view do the work invisibly, which is worse.

Watch what the same organisms do as you move across four definitions.

The nematode *C. elegans* has 302 neurons. It habituates. It learns by association. It tunes its behavior to experience. Under Binet, who demanded judgment and self-correction, the worm is out — a worm climbing a chemical gradient through a fixed circuit, however elegant, is not what Binet meant. Under Wechsler, who asked for aggregate adaptive capacity, the worm begins to slip through; it does adapt, modestly, to its world. Under Legg–Hutter, the worm is in: it achieves goals in its environment. The interesting question stops being *whether* it qualifies and becomes *how* intelligent it is, and in what shape.

A chess engine beats every human alive and cannot learn checkers without being rebuilt. Under Binet: out — no judgment, no autocritique. Under Wechsler: out — no broader purpose, nothing resembling an environment. Under Legg–Hutter: in, within one vanishingly narrow environment and absent everywhere else. Under Chollet, whose entire point is that towering performance on a single task tells you almost nothing: dramatically out. High skill without transfer is precisely the failure mode his definition was built to catch.

A large language model, trained on the bulk of human text, scores well enough on standardized tests to be unsettling. Under Legg–Hutter it is in within text environments, largely absent outside them. Under Chollet — and here is the live debate — the verdict hinges on a question nobody yet knows how to answer cleanly: when the model handles a new prompt, is that genuine learning on the spot, or retrieval from a training set so vast that almost nothing is truly new? The model has, in a sense, already seen everything. Hand it a novel visual-reasoning puzzle with three worked examples and ask it to infer the rule — the way a child can from almost nothing — and it stumbles in a way that is diagnostic. The failure is not about how much the system knows. It is about whether knowing turns into learning.

I am adopting Legg–Hutter, and I want to tell you exactly why and exactly what it costs.

The reasons are three. First, it is substrate-neutral — it never mentions neurons, language, or carbon. A bacterium and a transformer get judged on the same criterion, which is the only way the comparative work in this book can be done at all. Second, it is graded, not binary; a worm and a human are both in the conversation, and the question becomes the shape of intelligence rather than the pass/fail. Third, it is operational: hand me an agent and an environment and I can, in principle, run an experiment. The formal version of the definition is a sum over all computable environments, each weighted by its Kolmogorov complexity — the length of the shortest program that would generate it — so that simpler environments count for more. It is Occam's razor written as an equation. The sum is uncomputable in practice, but the principle is testable by comparison, and comparison is all this book needs.

The cost is real, and I will name it. The definition flattens affect. It treats agents as goal-pursuers when real animals are also moods, attachments, memories — inner worlds a reward signal does not easily capture. It will strain hardest in the chapters on emotion, on social cognition, on creativity. There I will reach for other tools: Chollet when the question is whether a model is learning or retrieving; de Waal when a test has been built around the wrong Umwelt. A working instrument is allowed to be imperfect. It is not allowed to be hidden.

---

Let me close with the thing people find hardest to accept about all this.

There is a widespread intuition that a century of research should have converged on a definition by now — that if the thing is real, we ought to be able to say what it is, and the failure to do so smells like a scandal. I do not think that is the right reading. Consider the word *gene*. Biologists worked with it productively for some fifty years before molecular biology handed them a clean physical definition. They were not confused in the meantime; they were using an operational concept carefully and building real knowledge with it. Consider *species*. There are more than two dozen competing species concepts in working use across biology, and biologists argue about the right one constantly while making enormous progress. Science does not require a complete definition. It requires an operational specification inside a given study — a clear statement of which sieve is being used and what is being measured.

So the argument is not that intelligence has no definition. It is that intelligence picks out a family of overlapping capacities — judgment, adaptation, goal achievement, the efficiency of learning — and different definitions foreground different members of the family for different purposes. The cases share overlapping features with no single feature running through all of them. Wittgenstein called this *family resemblance*: the way the members of a family share a nose here, a brow there, a gait somewhere else, with no one feature common to every face. Intelligence is closer to family resemblance than to atomic number. That is not a retreat. It is the accurate description of what is going on.

The question mark in this book's title is the thesis, then — not a hedge, not a rhetorical flourish. The study of intelligence has not arrived. It is in the middle of something, the way evolutionary biology was in the middle of something in 1859, with variation and selection in hand but no mechanism of inheritance, and the way physics was in the middle of something in 1905, with special relativity but neither general relativity nor quantum mechanics yet. The right response to being in the middle of something is not to pretend you are at the end.

The next chapter walks further back than most discussions of intelligence dare to go — to bacteria, to slime molds, to plants — and asks whether anything a brainless organism does deserves the word. The answer will depend entirely on the sieve we just chose. By the end of it you should feel that the choice was real, and that it was worth making.

The worm in the dish is waiting.

---

## Sources

- Sternberg, R. J. & Detterman, D. K., eds. (1986). *What Is Intelligence? Contemporary Viewpoints on Its Nature and Definition.* Ablex.
- "Mainstream Science on Intelligence," *Wall Street Journal*, December 13, 1994 (drafted by Linda S. Gottfredson; 52 signatories of 131 contacted).
- Pilley, J. W. & Reid, A. K. (2011). "Border collie comprehends object names as verbal referents." *Behavioural Processes* 86(2):184–195. (Chaser; 1,022 names; inference by exclusion.)
- Legg, S. & Hutter, M. (2007). "A Collection of Definitions of Intelligence." arXiv:0706.3639; and "Universal Intelligence: A Definition of Machine Intelligence." *Minds and Machines* 17(4):391–444.
- Chollet, F. (2019). "On the Measure of Intelligence." arXiv:1911.01547.
- Binet, A. & Simon, T. (1905), foundational definition emphasizing judgment, direction, and autocritique.
- Wechsler, D. (1944). *The Measurement of Adult Intelligence.* Williams & Wilkins.
- Gardner, H. (1983). *Frames of Mind: The Theory of Multiple Intelligences.* Basic Books.
- Shalizi, C. (2007). "g, a Statistical Myth." http://bactra.org/weblog/523.html
- de Waal, F. (2016). *Are We Smart Enough to Know How Smart Animals Are?* W. W. Norton.
- von Uexküll, J. (1909). *Umwelt und Innenwelt der Tiere.* (Origin of the *Umwelt* concept.)
- White, J. G., Southgate, E., Thomson, J. N. & Brenner, S. (1986). *Phil. Trans. R. Soc. Lond. B* 314:1–340. (*C. elegans*, 302 neurons.)
