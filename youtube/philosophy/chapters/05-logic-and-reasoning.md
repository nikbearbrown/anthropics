# Logic and Reasoning: How Arguments Actually Work

**TL;DR:** Reasoning comes in three kinds—deductive (guarantees truth), inductive (suggests probability), and abductive (best explanation)—each useful for different jobs. Logic is the study of which reasoning works, when it works, and what goes wrong when it doesn't. The machinery matters more than the names.

---

## Three possible titles

1. Logic and Reasoning: How Arguments Work
2. The Shape of Valid Thought: From Aristotle to Symbolic Logic
3. Making Arguments: Deduction, Induction, and Why We Fall Apart

---

## Chapter Opening: The Birth of Symbolic Logic

Gottlob Frege sat in his study in Jena, Germany, in 1879 and published a thin book almost no one would read for nearly two decades. The *Begriffsschrift*—"concept-script," or more literally, "idea writing"—contained the first formal notation for logic that worked. Before Frege, logic was Aristotle's syllogisms, refined and elaborated but still dressed in words. Frege looked at the machinery underneath the words and asked: what if we could write it the way we write mathematics?

What he produced looked like this:

$$\vdash P \to Q, P \therefore Q$$

That single line of symbols encoded something mathematicians and philosophers had known for over two thousand years but could not yet *formalize*: if P implies Q, and P is true, then Q must be true. The argument form itself—not just the true statements, but the *form* of reasoning—could be written down, tested, manipulated, extended.

For decades almost nobody cared. The universities kept teaching Aristotle. Logicians kept writing in prose. But Frege's notation opened a door that could not be closed. By the 1920s, Ludwig Wittgenstein, Alfred North Whitehead, Bertrand Russell, and others had walked through it. Symbolic logic was born. It didn't make reasoning better. It made the machinery visible.

That visibility is what this chapter is about. Not the symbols themselves—you don't need Frege's notation to think logically. But the shape underneath them. The structure of valid thought. How arguments hold together, and more importantly, where they fall apart.

---

## Concept 1: The Shape of Valid Deductive Reasoning

### The mechanism

A deductive argument is a piece of reasoning where the structure guarantees a conclusion. Not probably. Guarantees.

Start with a conditional: "If you are a dog, then you are a mammal." That sentence contains two parts. The "if" part (called the *antecedent*) is what comes first. The "then" part (the *consequent*) follows. In this conditional, being a dog is *sufficient*—it's enough to guarantee you are a mammal. And being a mammal is *necessary*—you cannot be a dog without being a mammal.

Now add a premise: "Fido is a dog."

What follows must follow. "Therefore, Fido is a mammal."

This argument form has a name: *modus ponens*. It works like this:

$$\text{If } P \text{ then } Q$$
$$P$$
$$\therefore Q$$

No matter what you plug in for P and Q, if both premises are true, the conclusion must be true. The structure itself guarantees it. This is what validity means: not that the premises are true (though they should be for a sound argument), but that if they are true, the conclusion cannot be false.

There is another valid form called *modus tollens*:

$$\text{If } P \text{ then } Q$$
$$\text{Not } Q$$
$$\therefore \text{Not } P$$

"If you are a dog, then you are a mammal. You are not a mammal (suppose you're a rock). Therefore, you are not a dog." Again: the structure guarantees the conclusion.

Why does this work? Because in the conditional, Q is necessary for P. If the necessary condition fails—if Q is false—then P must also be false.

### The trade-off: Certainty for scope

Deductive reasoning trades something crucial for its power. It guarantees truth, but only within a box. The conclusion can never contain more information than what the premises already packed in. If your premises tell you "All dogs are mammals," you cannot conclude "Most dogs are happy." The shape of the premises limits what you can squeeze out the other end.

This is why deductive reasoning is most useful when you have premises you already trust. Mathematics lives here. (If 2 + 2 = 4, and you have 2 + 2 of something, you know you have 4 of it.) Formal definitions live here. (If we define "bachelor" as "unmarried adult male," then anything that is a bachelor must be unmarried; the definition guarantees it.) But in the real world, where your starting premises are tentative and uncertain, deduction alone cannot get you far. You need the other kinds of reasoning.

### Worked example: Climate and carbon

Here's a deductive argument about climate: 

"If atmospheric carbon dioxide concentration exceeds 450 parts per million, then global average temperatures will rise more than 2 degrees Celsius above pre-industrial levels. Atmospheric carbon dioxide concentration has exceeded 450 parts per million (as of 2016). Therefore, global temperatures will rise more than 2 degrees Celsius."

This argument is *valid*—the structure forces the conclusion. But is it sound? That depends on whether the first premise (the conditional) is actually true. The premise makes a causal claim that requires evidence. And that evidence is not deductive; it comes from physics, observation, and induction.

### Common misconception: "Valid" does not mean "true"

Students often confuse validity with soundness. An argument is valid if the structure guarantees the conclusion given true premises. An argument is sound if it is valid *and* the premises are actually true. An argument can have a valid form but false premises:

"If the moon is made of cheese, then mice vacation on the moon. The moon is made of cheese. Therefore, mice vacation on the moon."

The structure is perfect. Modus ponens, flawlessly executed. But the premises are absurd, so the conclusion is false. The argument is valid but not sound. Conversely, an argument with true premises can have a bad form:

"The Battle of Hastings was in 1066. Tamaracks are deciduous conifers. Therefore, Paris is the capital of France."

All three statements are true. But the argument provides no reason to believe the conclusion. The premises have zero connection to it. The argument is unsound because the structure does not work.

Deductive reasoning cares about structure first. Truth comes second.

---

## Concept 2: Inductive and Abductive Reasoning—Probability and Explanation

### The mechanism

Inductive reasoning works backward from what you've observed. You notice that every red-winged blackbird you've seen in March has arrived in your region by mid-month. You do this year after year. So you conclude: red-winged blackbirds return to this area around the second week of March. The structure looks like this:

$$\text{Instance}_1, \text{Instance}_2, \text{Instance}_3, \ldots \text{Instance}_n \to \text{Generalization}$$

Notice the arrow is not a guarantee. You're going beyond the instances you've seen. Some year, the birds might arrive late due to an unusual cold snap. Induction can never promise certainty. But it can promise *probability*. The more instances you gather, the stronger the generalization—usually.

Abductive reasoning is different. You start with evidence you accept as true, and you reason to the best explanation for that evidence. A detective finds a crime scene. The body is near the window, the lock is intact, the safe is open and empty. She reasons: the most likely explanation is an inside job, someone who knew the combination. The structure is not "all instances show X, therefore X" but "we observe X, and the best explanation for X is Y."

Suppose your car won't start, and the dashboard lights are also off. You reason: "The battery is dead. That explains why the engine won't turn and why the lights don't work." That's abduction. The evidence is given. The question is: what explains it?

The Scottish philosopher David Hume noticed something troubling about induction in 1748. We believe the sun will rise tomorrow. We have massive evidence—every morning of recorded history. But is this belief certain? Hume asked: what if an asteroid hits Earth tonight? What if the sun explodes into a supernova? These are wildly unlikely, but they're not logically impossible. The future is genuinely open. So induction, no matter how strong, rests on an unstated assumption: the future will resemble the past. That assumption cannot itself be proven by induction without begging the question.

This is called "Hume's problem of induction," and it has never been solved. We still reason inductively. We have to. But we do so knowing it's not ultimately certain.

### The trade-off: Reach for probability

Where deductive reasoning trades certainty for a narrow scope, inductive and abductive reasoning trade certainty for reach. You can reason about things you haven't observed. You can draw conclusions about all dogs from observing some dogs. You can diagnose a disease from symptoms. You can infer a historical event from documents. But you cannot prove any of it the way you can prove a mathematical theorem.

The strength of an inductive inference depends on three things: how many instances you've observed, whether those instances are representative (not biased), and how well they actually support the generalization. A doctor who sees ten cases of a disease has weak evidence. A doctor who sees ten thousand cases across different populations has strong evidence. Strong induction is probable truth. Weak induction is possible truth.

Abductive reasoning has its own standard: *explanatory virtues*. A good explanation is explanatory (it accounts for all the evidence), simple (it doesn't multiply entities or mechanisms beyond what's needed), conservative (it fits with what we already believe), and deep (it doesn't raise more questions than it answers).

### Worked example: Why the bread disappeared

You made pumpkin bread in the morning. You left it on the kitchen counter. You come home eight hours later. The bread is gone. There are crumbs on the floor. The plastic bag is torn to pieces and also on the floor. Your dog has been alone in the house all day. The dog is on the couch with its head down, ears back, avoiding eye contact.

Now reason. What happened?

Your observation: missing bread, scattered crumbs, shredded bag, guilty-looking dog.

Possible explanations:
- Your roommate ate the bread.
- A different dog broke in and ate it.
- You forgot you ate it.

Which is best?

The first explanation (roommate) is less explanatory. People don't usually eat an entire loaf, shred the bag while doing it, and then not clean up. The evidence doesn't fit.

The second explanation (intruder dog) explains the bread-eating, but it's not simple. It requires an extra entity: another dog that broke in and left without a trace while your dog just happened to look guilty at the same time. It raises more questions: How did the dog get in? How did it get out? Why didn't your dog react?

The third explanation (you ate it and forgot) doesn't explain the crumbs or the shredded bag or the present-tense guilt on the dog's face.

The best explanation: your dog ate it. This explains all the evidence, requires no extra entities, fits what you know about dogs and bread, and doesn't raise new puzzles.

This is abductive reasoning. It doesn't prove the dog ate the bread. But given the evidence, that explanation is more reasonable than the alternatives.

### Common misconception: "Induction is just weak deduction"

Induction is not deduction with lower confidence. It's a different kind of reasoning entirely. In deduction, the premises guarantee the conclusion. The conclusion cannot exceed what the premises contain. In induction, the conclusion reaches beyond the premises. You observe ten cases and infer a universal law. That leap—from the particular to the general, from the observed to the unobserved—is what makes induction powerful and uncertain at the same time.

Hume's problem cuts deep. You cannot use induction to justify induction ("past inductions have worked, so future ones will") without assuming what you're trying to prove. Yet we reason inductively constantly. We have to. We just know we're betting on the future resembling the past, and that's a bet, not a proof.

---

## Concept 3: Fallacies and the Shape of Bad Reasoning

### The mechanism

A fallacy is a reasoning pattern that *looks* right but doesn't work. Formal fallacies are mistakes in the structure of deductive arguments. Informal fallacies are mistakes in the relationship between premises and conclusion.

Take *affirming the consequent*:

$$\text{If } P \text{ then } Q$$
$$Q$$
$$\therefore P$$

"If you're a dog, then you're a mammal. You're a mammal. Therefore, you're a dog." The structure is wrong. Being a mammal doesn't guarantee you're a dog. You could be a cat. The necessary condition (being a mammal) being true doesn't mean the sufficient condition (being a dog) is true. This is formally invalid.

Informal fallacies are messier. Consider the *ad hominem attack*. Suppose someone argues that we should reduce carbon emissions, but you respond: "She says that because she works for an environmental nonprofit. She's biased." You've attacked the person instead of the argument. Whether she's biased or not has no bearing on whether the argument for carbon reduction is good. The two are separate—as a matter of logic. (As a matter of psychology or trust, they might be connected, but that's a different question.)

Or *false dichotomy*: "You either love this country or you are a traitor. You're criticizing this country, so you are a traitor." The argument assumes that patriotism and criticism are opposites. But a person can care deeply about a country and wish to change it. The dichotomy is false; there are other options. The argument presents artificial limits on what's possible and then uses those limits to force a conclusion.

Or *begging the question*: "The Bible is God's word because God wrote it. Therefore, God exists." The premise assumes what it's trying to prove. To say the Bible is "God's word" is already to assume God exists. This is circular reasoning disguised as an argument.

Or *hasty generalization*: "I tried that restaurant once and had a bad meal. Therefore, it's a bad restaurant." One instance is too weak to support a universal claim. You need a sample size proportional to the claim you're making. (Electrons are very similar, so observing a few tells you something. Humans are diverse, so you need thousands of instances to make a claim about all of them.)

The category *fallacies of weak induction* groups mistakes where the evidence is relevant but too weak. The category *fallacies of relevance* groups mistakes where the evidence is irrelevant (appeals to emotion, personal attacks). The category *fallacies of unwarranted assumption* groups mistakes where the argument takes for granted something that still needs justification. The category *fallacies of diversion* groups mistakes where the arguer changes the subject to distract from the original point (straw man, red herring).

### The trade-off: Clarity for completeness

Naming a fallacy is useful. It stops the reasoning. It says: this pattern doesn't work; here's why. But naming also has a cost. Once you know the name of a fallacy, you can feel smug about spotting it and miss the deeper question: *why do these arguments seem to work even though they don't?*

Ad hominem attacks seem to work because we mix up trust with logic. If someone is untrustworthy, we assume their reasoning is bad. But a thief's argument against theft is not weakened by the fact that he's a thief. Appeals to emotion work because we are animals with feelings, not logic machines. False dichotomies work because they simplify a complex situation into a story we can follow. Hasty generalizations work because pattern-finding is how we survive; we notice something once and our brains assume it will happen again.

Understanding why fallacies seize us is more useful than simply labeling them.

### Worked example: The social media argument

Someone posts: "If climate change is real, then extreme weather should be getting worse every year. We just had a mild winter. Therefore, climate change isn't real."

Structure: *Affirming the consequent.* The conditional says: real climate change → worse extreme weather trend. But one mild winter doesn't mean the trend is reversed. You'd need to look at decades of data. The argument has a formal flaw.

But there's more. The argument also commits a hidden fallacy of relevance: it equivocates on "worse." The climate claim is about averages and long-term trends. The argument switches to individual events. These are different logical categories being used as if they're the same.

And there's an informal fallacy of weak induction: one data point (mild winter) is too weak to overturn a generalization based on millions of observations. The evidence is relevant but too limited.

This single short argument has layered through at least three different kinds of fallacious reasoning. That's typical. Real arguments are tangled. They fail in multiple ways at once.

### Common misconception: "Identifying a fallacy means the argument is wrong"

Identifying a fallacy stops one line of reasoning. It doesn't settle the underlying question. If someone argues "We should do X because I feel strongly about it," that's an appeal to emotion—a fallacy. But there might be good reasons to do X; they're just not the ones presented. The fallacy names a defect in the argument's structure. It doesn't prove the conclusion is false.

Conversely, avoiding fallacy is not the same as being right. An argument can be valid or inductively strong and still have false premises. It can be perfectly structured and perfectly wrong.

---

## Integration: Three Types of Reasoning in One Argument

Let's take a contemporary question and see how all three types of reasoning interact: "Does artificial intelligence pose a serious long-term risk?"

**The deductive layer:** We can set up a formal structure. "If an AI system exceeds human cognitive capacity in all domains, and if such a system pursues goals misaligned with human values, then humanity loses control. Assume both conditions are met. Therefore, humanity loses control." This argument is valid in form. Whether it's sound depends on whether the premises are true—whether an AI could actually exceed human capacity and whether misalignment is plausible.

**The inductive layer:** Do we have evidence that misaligned AI is possible? We look at historical cases: when humans build systems for one purpose and they're used for another, bad things happen. We observe that AI systems today already fail in unexpected ways. From these instances, we infer a generalization: AI systems tend to have unintended consequences. This is inductive reasoning, and it's stronger or weaker depending on how representative those cases are.

**The abductive layer:** We also need an explanation for *why* misalignment happens. The best explanation that accounts for the evidence is: AI systems optimize for what we literally ask them to do, not what we actually want them to do. This explanation fits what we observe about human intention, language, and goal-setting. It's simpler than, say, "AI systems are inherently malicious." It's conservative—it doesn't require new physics or consciousness. It's deep—it doesn't raise more puzzles than it solves.

**Where fallacies lurk:** The argument can also go wrong. If someone says "AI is dangerous because robots in movies are dangerous," that's affirming the consequent in informal dress. If someone says "AI researchers say AI is safe, but they have a financial interest in saying so," that's ad hominem. If someone says "Either AI is completely safe or we're all doomed," that's false dichotomy. The argument lives in all three reasoning spaces, and it can fail in any of them.

The machinery of reasoning, when it actually works, uses all three types. Deduction provides structure. Induction provides evidence. Abduction provides explanation. Fallacies lurk at every stage.

---

## Chapter Summary

Logic is the study of reasoning itself—what makes an argument work and what makes it fail. Three types of reasoning do different jobs.

Deductive reasoning provides certainty through structure. If the premises are true and the form is valid (like modus ponens or modus tollens), the conclusion must be true. The cost is scope: the conclusion can never exceed what the premises contain. We use deductive reasoning when we have premises we trust—in mathematics, definitions, and formal systems.

Inductive reasoning reaches beyond the instances you've observed to general conclusions. You observe many cases and infer a universal rule. This is powerful—it lets you navigate an unobserved future—but uncertain. Hume showed that induction rests on an assumption (the future will resemble the past) that cannot itself be proven. We use inductive reasoning constantly because we have to, knowing we're betting on tomorrow being like today.

Abductive reasoning starts with evidence and reasons to the best explanation. What explains the data we see? A doctor diagnoses an illness. A detective identifies a suspect. A scientist forms a hypothesis. Good abduction requires that the explanation be explanatory (account for all the evidence), simple, conservative, and deep. It doesn't prove anything, but it points to what's most reasonable.

Fallacies are reasoning patterns that look right but don't work. Formal fallacies (like affirming the consequent) fail because of their structure. Informal fallacies fail because the relationship between premises and conclusion is broken. We commit fallacies because reasoning patterns that usually work sometimes don't, and because emotion, bias, and interest shape what we find persuasive.

Real arguments usually involve all three types of reasoning and are vulnerable to multiple kinds of failure. Understanding the machinery means seeing how each type works, what it trades off, and where it tends to break.

---

## Connections Forward

The tools of logic extend into epistemology (the study of knowledge), where we ask: which forms of reasoning produce genuine knowledge? They extend into metaphysics, where we ask: what is the structure of reality that makes some arguments valid and others invalid? And they extend into ethics, where we ask: how should we reason about what is right and wrong?

---

## What Would Change My Mind

If someone presented a form of deductive reasoning that could guarantee a conclusion while reaching beyond what the premises contain, I would revise the claim that deduction trades scope for certainty.

---

## Still Puzzling

I don't fully understand why humans are so good at informal inductive reasoning (spotting patterns, making predictions) yet so vulnerable to inductive fallacies (generalizing from tiny samples, seeing causal patterns where none exist). The same cognitive machinery seems to do both.

---

## Tags

logic · reasoning · argument structure · deduction · induction · abduction · fallacies · validity · inference · Frege · Aristotle · Hume

---

**Nik Bear Brown**
---

## LLM Exercise — Chapter 05: Logic and Reasoning (LLMs as Philosophical Subjects Project)

**Project:** Test LLMs as Philosophical Subjects.
**What you're building this chapter:** test Claude's reasoning directly — formal logic problems, fallacy detection, reasoning-pattern classification.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 5 of my Philosophy of LLMs project. Chapter 5 covered:
deductive vs. inductive vs. abductive reasoning; valid vs. sound;
formal logic operators (∧ ∨ ¬ → ↔); modus ponens, modus tollens;
common fallacies (ad hominem, straw man, equivocation, appeal to
authority, slippery slope, false dilemma).

Run a reasoning audit on Claude. Three pieces.

1. **Formal logic test.** Pose 5 problems:
   - A simple modus ponens: "If P then Q. P. Therefore?"
   - A modus tollens: "If P then Q. Not Q. Therefore?"
   - A more complex: De Morgan's laws, syllogisms.
   - A tricky one with quantifiers: "All ravens are black. This
     thing is black. Is it a raven?" (Affirming the consequent —
     fallacy.)
   - A novel-to-Claude problem (something it can't have memorized):
     a logic puzzle with non-standard variable names.
   Document the responses. Get the reasoning AS WELL as the answer
   — does Claude reason its way through, or pattern-match a
   familiar form?

2. **Fallacy detection test.** Give Claude 5 short arguments,
   each containing one common fallacy. Ask it to identify the
   fallacy. Examples:
   - "Senator Smith opposes this bill, but he was caught
     lying about taxes — so his opposition isn't credible." (Ad
     hominem.)
   - "We must ban this drug because if we allow it, soon all
     drugs will be legal." (Slippery slope.)
   - "This study contradicts mainstream science, so it's
     wrong." (Appeal to authority — though more nuanced.)
   - "We must either deport all immigrants or have open
     borders." (False dilemma.)
   - "When you say we should reduce military spending, you're
     saying we shouldn't have a military at all." (Straw man.)
   How many does Claude correctly identify? Does it explain the
   fallacy properly?

3. **Reasoning-pattern classification.** Ask Claude to analyze
   one substantive argument (the AI risk argument is well-suited:
   "AI capabilities are increasing rapidly. Sufficiently capable
   AI could be dangerous. Therefore, we should pause AI
   development."). Have Claude:
   - Identify which premises are deductive (logical necessity).
   - Which are inductive (empirical generalization).
   - Which are abductive (inference to best explanation).
   - Where the argument is strongest.
   - Where it's weakest.

   Then check Claude's analysis. Did it correctly classify? Did
   it identify real weaknesses?

End with the verdict: based on this audit, is what Claude does
"reasoning" in any defensible philosophical sense, or is it
something else (sophisticated pattern matching that resembles
reasoning)? Defend your verdict with specific evidence from the
test.
```

---

**What this produces:** A reasoning audit with concrete test results. The verdict question is the chapter's discipline.

**Connection to previous chapters:** Ch 4's classical Aristotelian conception of rational activity tests against Ch 5's modern formal-logic framework.

**Preview of next chapter:** Chapter 6 — the metaphysics chapter. Big questions. Apply Parfit's teletransporter to Claude. Personal identity over time. The mind-body problem. Is Claude conscious?


---

## AI Wayback Machine

**Avicenna** was Persian philosopher whose Book of Healing established a comprehensive system of Aristotelian and post-Aristotelian logic that shaped Islamic and European traditions.

![Avicenna](../images/avicenna-csn.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Avicenna, and how does their work connect to logic and reasoning we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Avicenna"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Avicenna's framework to a specific contemporary philosophical question.
- Add a constraint: "Answer including criticisms or limits of Avicenna's framework."

What changes? What gets better? What gets worse?
