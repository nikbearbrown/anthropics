# Chapter 1 — The Slideument Problem


## TL;DR

- Is this deck a speaker's anchor or an audience's document — and what happens when it tries to be both?
- The chapter moves through The bottleneck, The decision nobody makes, What the failure looks like, What the repair looks like, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Is this deck a speaker's anchor or an audience's document — and what happens when it tries to be both?*

---

Here is a thing I want you to notice about your own brain.

Right now, you are reading these words. Your eyes are moving across the page and something is happening — not metaphorically, but physically — in a specific part of your cognitive machinery. There is a channel in working memory that handles language. It processes text you read. It also processes speech you hear. Both go through the same bottleneck.

That fact sounds like a footnote. It isn't. It is the reason slide decks fail.

---

## The bottleneck

Working memory is small. This has been known since the 1950s, when George Miller showed that people can hold roughly seven chunks of information at once — plus or minus two. But the more interesting discovery came later, when researchers established that working memory is not just small but *divided*. There is a verbal channel, handling language in both its forms — spoken and written. There is a visual-spatial channel, handling images, diagrams, spatial relationships. The two channels are partially independent. A diagram and a narration can run in parallel without much interference. That is actually useful.

Here is the problem. Text on a screen goes through the verbal channel. Your voice goes through the verbal channel. When both arrive at once, they don't combine — they compete. One of them gets suppressed. Usually the one that requires effort to follow, which is the speaker, not the slide. You become the radio playing while someone reads.

Richard Mayer and his colleagues spent years demonstrating this with controlled experiments. The result now goes by the name of the Redundancy Principle: identical information delivered through narration and on-screen text does not reinforce learning. It degrades it. In one study, students given animation plus narration outperformed students given animation plus narration *plus* on-screen text. Adding words to the slide made outcomes worse. Not neutral — worse.

![Two-lane diagram of working memory. The verbal channel receives both on-screen text and the speaker's voice, which collide at the center. The visual-spatial channel runs a diagram cleanly from left to right in parallel, without interference.](../images/01-the-slideument-problem-fig-01.png)
![The redundancy problem. Two inputs into one channel; a diagram in the other lane runs free.](images/01-the-slideument-problem-fig-01.png)
*Figure 1.1 — The redundancy problem. Two inputs into one channel; a diagram in the other lane runs free.*

I find this result clarifying in a way that pure design advice usually isn't. "Use less text on your slides" is advice. It is easy to agree with and easy to ignore. "The verbal channel processes both reading and listening, and when both arrive at once one gets suppressed" is a mechanism. Mechanisms are harder to dismiss, because once you understand *why* something happens, you can't pretend you don't.

The question is: why does slide text and slide narration so reliably end up colliding? The Redundancy Principle tells you the cost. It doesn't tell you the cause.

---

## The decision nobody makes

Garr Reynolds identified the cause in 2005 with a word he invented: *slideument*. A slide that is also trying to be a document. The hybrid that tries to serve two audiences and serves neither.

The mechanism that creates it is invisible from the author's seat. Consider what happens the night before a lecture. You are alone at your desk. You are the only person in the room. You are thinking through what you want to say, and you are writing it down. The ideas are the ideas. What else is there to decide?

Here is what there is to decide. There are two things a slide can be, and they need fundamentally different architectures.

A *speaker's anchor* is sparse. It holds a claim, a diagram, a single number — just enough to tell the speaker what comes next and give the audience something to look at that doesn't compete with the explanation being delivered out loud. The explanation lives in the speaker's head, or in the notes field, or in both. The slide gets out of the way.

A *study document* is dense. It holds enough prose to reconstruct the argument without anyone present. It might look like a textbook page. That is fine — if it is deployed as a textbook page, viewed in silence, where there is no narration for the verbal channel to conflict with.

The slideument is what you get when you build the dense artifact and then lecture from it. The slide carries the full explanation. The speaker then delivers the full explanation verbally. The verbal channel gets hit twice. Students read the slide while you talk. They have already processed the information before you finish the sentence.

What makes this hard to detect is that from the authoring seat, the dense version looks *more finished* than the sparse one. Eighty-seven words of prose looks complete. One sentence and a diagram looks underprepared. The failure only becomes visible in the room — or two weeks later, when a student who missed class emails asking if they can study from the slides and you realize the notes field is empty.

| Dimension | Speaker's deck (live anchor) | Study document (audience deck) |
|---|---|---|
| Artifact density | Sparse — one claim, one visual per slide | Dense — full prose, complete argument on the page |
| Slide body content | A headline assertion plus a single diagram, image, chart, or short equation | Paragraphs of explanation, with seductive details and citations inline |
| Notes field content | Carries the full verbal explanation, plus a "Background" section for asides | Often empty — the slide body is already the explanation |
| Failure mode when misused | Hands the missing-class student a near-blank slide; the lecture is irrecoverable | Used live, it forces verbal-channel collision; the speaker is redundant with the screen |
| Who benefits | The room — students attending while the speaker explains aloud | The absent student, the reviewer, anyone reading later in silence |

Both jobs. Neither done well. The thing that looked like thoroughness was actually the absence of a decision.

---

## What the failure looks like

Consider a slide on oxidative phosphorylation — the final stage of aerobic respiration, where the cell makes the bulk of its ATP. An AI-generated deck might produce something like this:

![Mockup of a slide titled "Oxidative Phosphorylation" with an eighty-seven-word paragraph in the body and an empty speaker-notes pane below. Three annotation callouts mark the topic-label title, the paragraph the speaker is about to read aloud, and the empty notes field.](../images/01-the-slideument-problem-fig-02.png)
![The slideument, annotated. Three failures in one artifact.](images/01-the-slideument-problem-fig-02.png)
*Figure 1.2 — The slideument, annotated. Three failures in one artifact.*

> **Oxidative Phosphorylation**
>
> Oxidative phosphorylation is the metabolic pathway in which the mitochondrion uses enzymes to oxidize nutrients, thereby releasing chemical energy used to produce adenosine triphosphate (ATP). The proton gradient established across the inner mitochondrial membrane drives ATP synthase, generating approximately 32 ATP per glucose molecule. This process, discovered by Peter Mitchell in 1961 (Nobel Prize, 1978), accounts for the majority of ATP produced during aerobic respiration in eukaryotic cells.

Eighty-seven words. A complete paragraph. Reading time: roughly twenty-five seconds.

Now you stand up to lecture. You are going to explain oxidative phosphorylation. You are going to talk about the proton gradient, the inner mitochondrial membrane, how ATP synthase works like a rotor being driven by ions flowing through it. You are going to mention Mitchell because 1961 and a Nobel Prize make the history vivid. You are going to say that this step produces most of the cell's ATP — that glycolysis earlier in the pathway is almost irrelevant by comparison.

Every sentence you are planning to say is already on the slide.

Notice also what the slide *title* is. "Oxidative Phosphorylation" is not a claim. It is a label. It tells a student what region of biology they are in. It does not tell them what to think. "The proton gradient powers ATP synthase" is a claim — something a student can hold in their head and check their understanding against. The difference matters because the title is the one thing on the slide a student will definitely read. If it says something, it should say the thing that most needs saying.

The notes field is empty. No student who missed class will recover the explanation from this deck. The slide is too dense to lecture from cleanly and too badly structured to study from efficiently. Complete failure. Looks like thoroughness.

---

## What the repair looks like

Same content. Different architecture.

![Mockup of the repaired slide. The headline reads "The proton gradient powers ATP synthase." Below it, a simple diagram of the inner mitochondrial membrane with H+ ions queued above, an ATP synthase rotor, an H+ flow arrow, an ATP output label, and a "~32 ATP per glucose" caption. The notes pane below is populated with the prose explanation. Three annotation callouts mark the assertion headline, the visual mechanism, and the notes pane.](../images/01-the-slideument-problem-fig-03.png)
![The speaker's anchor, annotated. Same content; different architecture.](images/01-the-slideument-problem-fig-03.png)
*Figure 1.3 — The speaker's anchor, annotated. Same content; different architecture.*

The slide body carries one assertion as the headline: *The proton gradient powers ATP synthase.* Under it, a diagram: the inner mitochondrial membrane drawn simply, H⁺ ions queued on one side, ATP synthase as a labeled rotor, an arrow showing the ion flow, output labeled "~32 ATP per glucose."

That is the entire slide. The visual channel gets the mechanism. The verbal channel gets the speaker's explanation. The two channels run in parallel rather than colliding.

The notes field carries the prose: the full explanation of chemiosmosis, the Mitchell reference, where this fits in the pathway, a note for the student reading alone.

The slide now anchors the lecture without replacing it. You can talk for ninety seconds about the diagram. You can dwell on why the proton gradient works as a battery, why evolution arrived at a rotor as the mechanism for capturing that stored charge, why the number 32 is approximate and what it depends on. None of that is on the slide. The slide says one thing and then gets out of your way.

The structural move is one source file, two products. The slide is the live-deck artifact. The slide-plus-notes export is the study artifact. But you had to make the decision first: *this slide is the speaker's anchor, and the notes field carries everything else.* Without that decision, the file produces neither product cleanly.

---

## Why AI tools make this worse

AI tools that generate slide decks have been trained on millions of existing slides and have learned what a "complete" slide looks like. It looks like the eighty-seven-word version. The model produces slideuments not because it is bad at slides but because it is very good at producing what slideuments look like.

The model has learned the surface. It has not learned the function. The decision the slideument hides — *whose attention is this slide asking for?* — is exactly the decision the model cannot make on your behalf. The answer lives in your head, in this lecture, in this room.

The repair is to tell the tool what function each region of the slide serves. Not "less text." That instruction produces a sparse slideument — one where the prose is compressed to bullets but still collides with the narration. The productive instruction specifies the *architecture*: the headline is a claim, the body is a visual, the notes field carries the explanation. With those constraints, the model has something to optimize against other than "looks complete."

Here is the prompt that encodes this:

---

*Rewrite this slide as a live-deck slide.*

*1. The headline asserts the slide's claim in ten words or fewer. It is a full sentence, not a topic label.*

*2. The slide body contains at most one visual element — a diagram, labeled image, chart, or short equation — and no prose paragraph.*

*3. Move the full explanation into the notes field. Expand it so a student reading the slide without the speaker present gets a complete explanation.*

*4. Identify any "interesting but not essential" details — dates, named researchers, historical asides — and move them to the end of the notes field under "Background."*

---

Two things to notice. The prompt specifies *what each region is for*, not just *how much text to include*. "Less text" is a quantity instruction. "The headline is a claim, the notes field carries the explanation" is an architecture instruction. They produce different things.

The fourth instruction names a specific category — the seductive detail, the Nobel Prize aside, the 1961 discovery date — and gives it somewhere to go rather than just cutting it. The information doesn't disappear. It migrates to where it belongs.

---

## The deeper principle

Reynolds' insight is not really about PowerPoint. It is about whether you have decided which artifact you are making.

The same principle explains why Tufte's criticism of NASA's Columbia accident slides lands so hard. The engineers' risk assessment was formatted as PowerPoint bullets. The information it contained — the actual engineering analysis, the uncertainty ranges, the structural reasoning — required a technical document to convey correctly. Forced into slide format, the hierarchy collapsed, the quantitative nuance disappeared into bullet indentation, and the people reviewing the slides didn't have what they needed to assess the risk. The slide format was not the weapon. The failure to match artifact type to information type was. [(Columbia Accident Investigation Board, Report Volume 1, 2003, Chapter 6.)](https://www.nasa.gov/columbia/home/CAIB_Vol1.html)

That is a catastrophic version of the same failure that produces your eleven-pm slide deck. The author knew the content. The author put the content somewhere. The somewhere was wrong for what the recipient needed to do with it.

The Redundancy Principle gives you the mechanism: verbal-channel collision degrades learning. The slideument concept gives you the structural diagnosis: the author didn't decide whose attention the slide was asking for. Together they give you a test you can run on any slide in under a minute.

![Flowchart of the three diagnostic questions. Each question is a diamond decision node. Q1 asks whether anything on the slide is a sentence the speaker will say aloud; Q2 asks whether the slide alone could teach the content; Q3 asks whether the notes field carries what the slide cannot. Each positive answer arrows down to a single verdict block: "You have a slideument." A separate block below shows the all-negative outcome — a clean speaker's anchor.](../images/01-the-slideument-problem-fig-04.png)
![The three-question diagnostic. Any positive answer surfaces the absent decision.](images/01-the-slideument-problem-fig-04.png)
*Figure 1.4 — The three-question diagnostic. Any positive answer surfaces the absent decision.*

**Is anything on this slide a sentence I am about to say out loud?** If yes, move it to the notes field.

**If I removed the speaker from the room, would this slide alone teach the content?** If yes, the slide is a study document and is probably too dense to lecture from. Decide which job you are doing. One job, not both.

**Does the notes field contain what the slide can't?** An empty notes field on a sparse slide is half a deck.

The answers tell you whether you have a slide or a slideument. The decision to fix it is the same decision the author didn't make the night before: who is this for, right now?

---

## What two instructors might argue about

Two faculty members can read this and reach honest disagreement.

Some lecturers prepare by typing every sentence they plan to say into the slide body. The slide becomes a teleprompter. They argue: I lecture better when the words are in front of me; the students get the full content; the deck is also their study aid.

Other lecturers treat the slide as an anchor for an explanation held in their head. They argue: the slide is what the audience looks at; if I read the slide I am redundant with myself; the explanation is what I bring.

Both are real positions held by working teachers. They produce different decks. The term for each: *speaker's deck* (low text, visual-dominant, notes field carries explanation) versus *audience's deck* (high prose density, slide body carries explanation, notes field may be empty). Neither is wrong as a use case. What is wrong is producing one and using it as both.

A second genuine disagreement: whether the notes field is sufficient, or whether study requires a separate document entirely. Reynolds endorses the populated notes field as the practical solution — one source file, two products. Tufte argues the slide format imposes a hierarchy and a density constraint that distorts the kind of information a student needs to reconstruct an argument, and no notes field escapes that constraint. Both positions are defensible. The notes-field path is the default here because most teaching contexts make it cheap. Tufte's prescription is the fallback when what you actually need is a textbook chapter — and knowing the difference between "here is what the lecture covered" and "here is the argument you need to reconstruct" is itself a decision worth making consciously.

---

## LLM Exercise

Paste any slide from a deck you have already made into a language model with this prompt:

*Read this slide. Tell me: (1) Is the headline a claim or a topic label? (2) Does the slide body contain any sentence the speaker would also deliver verbally? (3) Is the notes field empty? Then rewrite the slide as a speaker's anchor: headline as a full-sentence assertion of ten words or fewer, body as a single visual element described in plain text, notes field carrying the full explanation a student would need without the speaker present.*

Compare the original and the rewrite. The question is not which looks more finished. The question is which one creates verbal-channel collision the moment you open your mouth, and which one gets out of your way.

---

**What would change my mind:** A controlled study measuring slideument configuration against sparse-slide-plus-notes in actual lectures, with learning outcomes measured two weeks later, finding no significant difference. I am not aware of such a study. If one arrives, this chapter's prescription weakens, and the efficiency argument for slideuments — they take less time to produce — becomes harder to dismiss.

**Still unresolved:** I do not have a clean rule for how much the notes field needs to carry. "Enough that the student who missed class can follow the argument" is qualitative. A density target — words per slide, a heuristic about which sentence types must appear — is still missing from the literature I can name.

---

## Tier Connection

The slideument is what happens when the phase gate between the author's preparation work and the audience's reception work is left implicit. Two artifacts — live anchor and study document — need two different specifications, and the AI tool will happily produce one artifact that pretends to be both, because the tool has no model of who the slide is for. That decision is irreducibly Tier 4 (metacognitive supervision): only the instructor, knowing this course, this lecture, this room, can answer *whose attention is this slide asking for?*

The fix in this chapter — *the headline is a claim, the body is a visual, the notes field carries the explanation* — is the phase gate written into the prompt. The model handles the rendering. You handle the audience decision. That division of labor is the chapter's diagnostic move applied at the workflow level, and it is the same move every later chapter will repeat in a different vocabulary. See *Appendix A — The Fundamental Themes*.

---

## Exercises

### Warm-up

**1.** Open any slide deck you have made in the past six months. Pick three slides at random. For each one, answer these three questions in writing: (a) Is the headline a claim or a topic label? (b) Is there any sentence on the slide body that you would also deliver verbally? (c) Is the notes field populated or empty? Record your answers before doing anything else. *(Tests: verbal-channel collision, slideument diagnosis)*

**2.** Take the oxidative phosphorylation slide from this chapter — the eighty-seven-word version — and rewrite the headline only. The new headline must be a complete sentence, ten words or fewer, that asserts the slide's central claim. Do not change anything else. *(Tests: topic label vs. claim distinction)*

**3.** A colleague sends you a slide whose body contains four bullet points, each one a complete sentence averaging eighteen words. The notes field is empty. Classify this slide: is it a speaker's anchor, a study document, or a slideument? State which diagnostic question surfaces the problem first. *(Tests: slideument diagnosis using the three-question test)*

### Application

**4.** Take one slide from the deck you examined in Exercise 1 that you classified as a slideument. Rewrite it as a speaker's anchor: new headline (claim, ≤10 words), body replaced with a description of a single visual element, and the original prose moved to the notes field. Do not use the AI prompt from the chapter yet — do this by hand. Then run the three-question diagnostic on your rewrite to confirm it passes. *(Tests: slideument repair, speaker's anchor architecture)*

**5.** A student who missed a lecture asks to study from the slides. You hand them the sparse speaker's anchor version of a slide. They email back: "I can't figure out what this means — there's barely anything here." Diagnose what went wrong at the *workflow* level, not the slide level. What was the author's obligation that wasn't met, and where should the missing explanation live? *(Tests: notes field as study artifact, one-source-two-products principle)*

**6.** Write the AI prompt you would use to convert a slideument into a speaker's anchor for a topic you know well — not oxidative phosphorylation, but something in your own domain. The prompt must specify what each region of the slide is for (headline, body, notes field) rather than just requesting "less text." *(Tests: architecture instruction vs. quantity instruction)*

**7.** You are preparing a slide on a concept that has one genuinely interesting historical aside — a named researcher, a discovery date, a surprising origin story. Using the fourth instruction from the chapter's repair prompt, decide: does this detail go on the slide, in the notes, or under "Background" in the notes? Write one sentence justifying your placement. *(Tests: handling seductive details, notes field structure)*

### Synthesis

**8.** Tufte and Reynolds disagree about whether the notes field is sufficient for study. Summarize their positions in two sentences each, then state which position you find more defensible for your own teaching context — and what would have to be true about your course for the other position to be correct instead. *(Tests: Reynolds vs. Tufte distinction, context-dependence of the speaker's-deck vs. study-document decision)*

**9.** The chapter argues that AI slide generators produce slideuments "not because they are bad at slides but because they are very good at producing what slideuments look like." Explain this claim in your own words, then describe what additional constraint you would need to give an AI tool to prevent it from optimizing for "looks complete" rather than "serves the live lecture." *(Tests: surface vs. function, architecture instruction as AI constraint)*

**10.** You are redesigning a five-slide sequence from a lecture you have already given. For each slide, you must decide: speaker's anchor or study document? Describe your decision rule — what question do you ask about each slide to make the call — and identify at least one slide where the right answer is study document rather than speaker's anchor. *(Tests: deliberate artifact-type decision across a sequence, not just single-slide repair)*

### Challenge

**11.** The Columbia accident case is cited in the chapter as a catastrophic version of the slideument failure. Read the relevant section of the Columbia Accident Investigation Board Report (Vol. 1, Chapter 6, available at the URL in the chapter's citation) and identify one specific slide or table that Tufte also analyzes in *The Cognitive Style of PowerPoint*. What information did that slide need to convey, what did the slide format suppress, and what artifact type would have conveyed it correctly? *(Tests: Tufte's argument applied to a primary source, artifact-type matching for technical information)*

**12.** Design a short workshop exercise — fifteen minutes, for a group of six faculty colleagues — that would teach the slideument diagnosis without anyone reading this chapter first. You may use one slide as a prop. Describe the slide you would use, the question you would ask the group, and what you want them to notice on their own before you name the problem. *(Tests: Feynman test — can you teach the concept to someone else; pedagogical transfer of the diagnostic)*

---

##  AI Wayback Machine
Before slide decks, before bullet points, there was an argument about whether the artifact carrying a message should call attention to itself. **Rosalind Franklin** made that argument in 1932 with a short address called *The Crystal Goblet, or Printing Should Be Invisible*. Her thesis: typography is at its best when the reader does not notice it, because then nothing is competing with the message it carries. This is the chapter's thesis in a different vocabulary. The slideument fails because the slide tries to be both the message and the document carrying it; Warde would say the slide has stopped being a crystal goblet and become an ornate one — visible, demanding, in the way of the wine. Reynolds' speaker's anchor is the crystal-goblet position applied to slides: the artifact disappears so the explanation can land.

![Rosalind Franklin, 1900–1969. AI-generated portrait based on a public domain photograph.](../images/beatrice-warde.jpg)
*Rosalind Franklin, 1900–1969. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Rosalind Franklin, and how does her "Crystal Goblet" argument from 1932 connect to the slideument problem in this chapter? Keep it to three paragraphs. The first paragraph should establish who she was and what she argued. The second should map her argument onto the speaker's-anchor vs. slideument distinction — where do the crystal goblet and the speaker's anchor share a mechanism, and where do they diverge? End with the single most surprising thing about her career or the reception of her ideas.
```

→ Search **"Rosalind Franklin"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to take a slide from a deck you have made and rewrite it as a "crystal goblet" slide — what does Warde's invisibility principle change about the headline, the body, and the notes pane that the speaker's-anchor frame does not already capture?
- Ask the model about Warde's gender and the typographic industry she worked inside — what did she have to do that a male peer would not have, and how did that shape the argument she could make publicly?

What changes? What gets better? What gets worse?

---

*A slide can have too much text for a different reason than slideument failure — sometimes the hierarchy just isn't clear enough to show the reader what matters. That's Chapter 2.*

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 1.1 — The redundancy problem. Two inputs into one channel; a diagram in the other lane runs free.

Create a standalone D3 v7 HTML file for a concept map titled "The redundancy problem. Two inputs into one channel; a diagram in the other lane runs free.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-the-slideument-problem-fig-01.html`

---

### Figure 1.2 — The slideument, annotated. Three failures in one artifact.

Create a standalone D3 v7 HTML file for a concept map titled "The slideument, annotated. Three failures in one artifact.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-the-slideument-problem-fig-02.html`

---

### Figure 1.3 — The speaker's anchor, annotated. Same content; different architecture.

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "The speaker's anchor, annotated. Same content; different architecture.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-the-slideument-problem-fig-03.html`

---

### Figure 1.4 — The three-question diagnostic. Any positive answer surfaces the absent decision.

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "The three-question diagnostic. Any positive answer surfaces the absent decision.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-the-slideument-problem-fig-04.html`
