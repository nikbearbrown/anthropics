# Chapter 12 — The Diagnostic Checklist


## TL;DR

- On October 30, 1935, the prototype Boeing Model 299 crashed during a demonstration flight at Wright Field.
- The chapter moves through How to use it, The checklist, Per-slide items, Per-deck items, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*One reference page. Use it before every deck ships.*

---

On October 30, 1935, the prototype Boeing Model 299 crashed during a demonstration flight at Wright Field. Two of the five crew died. The investigation was short. The pilots had forgotten to release a control lock before takeoff. The aircraft was not too complex to fly — one of the country's most experienced test pilots was at the controls. It was too complex to fly from memory alone, under the pressure of a demonstration, without any external scaffold for the steps that had to happen in order.

Boeing's response was the pre-flight checklist. A short, ordered list of items printed on a single card. With the checklist, the Model 299 went on to fly 1.8 million miles without an accident attributable to pilot oversight.

Atul Gawande spent a decade studying checklists in medicine and aviation before writing *The Checklist Manifesto*, and he is precise about what the checklist actually does. The pilots did not crash because they did not know to release the control lock. They knew. They crashed because the knowledge was not retrievable at the right moment, under pressure, when attention was elsewhere. The checklist offloads retrieval from working memory to a stable external artifact. Working memory is freed for the parts of the job that actually require judgment.

The evidence from medicine runs the same argument. Pronovost and colleagues implemented a five-item central-venous-catheter checklist across 103 Michigan ICUs. Items as simple as: wash hands, use full sterile barriers, clean skin with chlorhexidine, avoid femoral insertion, remove unnecessary catheters. The median rate of catheter-related bloodstream infections fell from 2.7 per 1,000 catheter-days at baseline to zero within three months, sustained at 66% below baseline at 16 to 18 months. The Haynes WHO Surgical Safety Checklist study, run across eight hospitals in high-income and low-income settings, found in-hospital mortality dropped from 1.5% to 0.8% and inpatient complications from 11% to 7%.

![The intervention was a card with five to nineteen items. The mechanism was working-memory offload, not new knowledge.](images/12-the-diagnostic-checklist-fig-01.png)
*Figure 12.1 — Two paired bar charts showing the Pronovost and*

There is an honest critique of this evidence. Bosk, Dixon-Woods, Goeschel, and Pronovost wrote in *The Lancet* three months after Haynes that the checklists worked because they sat inside broader organizational change — empowered nurses, leadership commitment, data feedback loops. Deploy the checklist alone, without the surrounding work, and it becomes paperwork. "A technical solution to a cultural problem is likely to fail or to be resented."

This matters here. The checklist that follows works for a reader who has worked through Chapters 1 through 11. Hand it to someone who has not read the book and it will read as a list of arbitrary questions. The checklist is the visible artifact. The reading was the work that makes it usable. Both are required.

![Diagram ](images/12-the-diagnostic-checklist-fig-02.png)
*Figure 12.2 — Diagram *

---

## How to use it

Gawande distinguishes two checklist architectures. A *read-do* checklist is executed step by step: read the item, do the item, move to the next. A recipe is read-do. A *do-confirm* checklist runs after the task is complete: you build the thing, then confirm nothing was missed. A surgeon's pre-incision checklist is do-confirm.

This checklist is do-confirm. Build the deck. Then run the checklist before shipping. The questions are framed as diagnostics — *is the headline a claim or a label?* — rather than instructions — *write a claim headline*. Running it before each slide during construction would interrupt more than it helps. Running it after the deck exists catches the failures that crept in while attention was elsewhere.

One discipline. If a question does not apply to a slide, the answer is *this question does not apply because [reason in framework vocabulary]*, not *skip*. A reader who can articulate why a question does not apply is using the checklist correctly. A reader who skips without reflection is producing paperwork — Bosk's failure mode, at the individual level.

There is a familiarity gradient to expect. The first few times, the checklist is slow. You are retrieving the vocabulary the chapters built and applying it deliberately. By the tenth deck, most questions answer themselves before you finish reading them. The eye does the claim-or-label test reflexively. The hierarchy diagnostic fires without prompting. The checklist has become what it is meant to be — the redundancy check that catches the slides you built at 11 p.m. on a Sunday when the defaults crept back in.

![Slowness on deck 1 is not a bug. It is the vocabulary being loaded. By deck 10 it is a redundancy check, not a procedure.](images/12-the-diagnostic-checklist-fig-03.png)
*Figure 12.3 — Two-axis chart *

---

## The checklist

### Per-slide items

**Chapter 1 — Slideument**

Who is this slide for right now — the speaker or the audience? A live-deck slide serves the speaker's anchor function. An async-study slide serves the document function. One slide, one job.

If the speaker were removed from the room, would this slide alone teach the content? If yes, it is probably too dense to lecture from. If no, the notes field needs to carry what the slide cannot.

Is anything on this slide a sentence the speaker is about to say out loud? Cut it from the slide and move it to the notes field. Verbal-channel collision is a real cognitive cost.

Does the notes field contain what the slide cannot? An empty notes field on a sparse slide is half a deck.

---

**Chapter 2 — No Clear Hierarchy**

Where does the eye go first, and is that where it should go? If the eye lands on the wrong element, the size hierarchy is broken.

How many type sizes are on this slide, and what is each one for? Title, primary message, supporting detail. If everything is the same size, there is no hierarchy. If everything is bold, nothing is.

Are elements that belong together physically close? Proximity signals *these are one thing*. Elements separated in space are perceived as unrelated.

Is whitespace grouping the right elements? White space is syntax, not wasted space.

---

**Chapter 3 — Too Much Text**

Which learning objective does each text element serve? If the answer is "general context" or "it's interesting," cut it.

Is any text repeating what the speaker will say aloud? Redundancy violation. Move it to the notes field.

Is any text interesting but not essential? Seductive detail. Coherence violation. Cut it or move it to notes.

Is the total word count above 50 for a live deck? A working ceiling. Above 75 words, the slide is a document wearing a slide's clothes.

---

**Chapter 4 — The Wrong Visual Form**

What is the relationship between the elements on this slide? Comparison? Process? Trend? Part-to-whole? Cause-effect? Name the relationship before choosing the form.

Is that relationship best shown as text, diagram, chart, or table? Most relationships are not best shown as a bulleted list. The bulleted list is the zero-decision form — what appears when no one has asked what the content is actually shaped like.

Would a reader understand the relationship faster with a visual? If yes, the visual is the right form. Text is the fallback, not the default.

Is this a 3D chart? Never. The depth axis adds visual complexity without information and distorts magnitude perception.

---

**Chapter 5 — Color Is Doing Nothing or Harm**

What does each color encode? Can it be stated in one word? Brand. Emphasis. Primary series. Warning. If the answer is "decoration," remove it.

Does every text element pass 4.5:1 contrast against its background? WCAG 2.1 AA standard. In projection environments with ambient light, target 7:1 or higher.

Would a colorblind reader lose information? Eight percent of men have red-green color vision deficiency. A slide that relies on red and green alone fails for one in twelve male students.

Is any color present for aesthetics rather than meaning? The Signaling Principle requires color to mean the same thing every time it appears. A color that means nothing is a cue that misleads.

---

**Chapter 6 — The Textbook Figure on the Slide**

Was this figure designed for print or for projection? Print figures are studied at fourteen inches over several minutes. Slide figures are scanned at fifty feet in three seconds. Different media, different design requirements.

Can the student in the last row read every label? If the label cannot be read from the back of the room, the label does not exist for most of the class.

Is there a visual signal — accent color, arrow, callout — directing attention to the specific point this slide is making? The audience cannot study the figure. They can only follow where it points.

Have labels that do not serve this slide's objective been removed? A figure labeled for a whole textbook chapter is over-labeled for a single lecture slide.

Does any simplification applied distort the relationships between the remaining elements? Simplification can cross into misrepresentation. Name the limit explicitly before shipping.

---

**Chapter 7 — Seductive Details**

Which learning objective does this element serve? If the answer is "it's interesting" or "it motivates students" or "it provides context," it is a seductive detail.

Is it interesting without being essential? Harp and Mayer's coherence violation. Cut it or move it to notes.

Would removing it make the core content clearer? Usually yes. The seductive-detail damage is asymmetric — they hurt more than they help.

Is it appearing early in the deck, where prior knowledge is lowest and the damage is highest? The effect is strongest in the opening slides, before the student has built the schema that would let them file the interesting detail correctly.

---

### Per-deck items

**Chapter 8 — The Deck That Covers but Doesn't Teach**

What should the student be able to *do* after this lecture? State it with an action verb — explain, apply, analyze, compare, evaluate, produce. If the answer is "be familiar with," the deck has no destination.

Does the deck open with a problem or question, or with a definition? A deck that opens with definitions has skipped the hook.

Are concepts in dependency order — prerequisites before the ideas that depend on them?

Is there at least one consolidation moment before the 20-minute mark, and another before the deck closes? Working memory needs to discharge before it can take on more.

Is this deck organized around the textbook's structure, or around the build the learner needs? Coverage and teaching are different operations.

---

**Chapter 9 — Live Deck vs. Study Artifact**

What is this deck for — live delivery, async study, or hybrid? Design follows from this decision. A deck that has not answered it is a slideument waiting to happen.

If live: is the text minimal enough that students will listen instead of read? Roughly 30 to 50 words per slide as a working ceiling.

If async: does the slide carry enough explanation without a speaker? The slide is the whole instructional artifact. It must teach alone.

Is the notes field populated for whichever mode this deck is not? Either the slide carries the explanation or the notes field does. Rarely both on the same slide.

---

**Chapter 10 — The Headline That Says Nothing**

Is the headline a claim or a label? A claim is a sentence with a verb that asserts something. A label is a noun phrase that names the subject. Different grammars do different jobs.

Could a student leave this slide with a specific thought in their head? If the only thought available is "the slide was about X," the headline did no teaching work.

Does the body provide visual evidence for the headline's claim? A diagram, a chart, a labeled image, an annotated comparison — not a vertical list of noun fragments.

Could the slide be summarized in one sentence to a colleague in the hallway? That sentence is the assertion. If it cannot be produced, the slide does not know what it is claiming.

Is this a teaching slide or a reference slide? Teaching slides default to assertions. Reference slides — agenda, glossary, section divider — correctly use labels. Name the type before challenging the headline.

---

**Chapter 11 — Owning Your DESIGN.md**

Can every variable in the DESIGN.md be explained in one sentence? The sentence is the decision. A variable without a one-sentence justification is still a default, still owned by the tool.

Is each decision traceable to a principle from cognitive science or visual design? A justification that lives outside the framework — "I like it better" — is not yet a decision.

Are reference-slide conventions named separately from teaching-slide conventions? A course with multiple slide types needs the DESIGN.md to acknowledge them.

When the system generated a slide that was wrong, was DESIGN.md updated or just the slide? The slide tweak fixes one slide. The DESIGN.md update fixes the class of failure. Structural failures want structural fixes.

---

## The deck-level check

Run these once per deck, after the per-slide pass.

| Item | Question | Pass condition | Fail signal |
|---|---|---|---|
| **D1** | What is this deck for? | Named: live, async, or hybrid — and the notes field is populated for the mode the slide is not. | "Both, I guess." Notes field empty on sparse slides. |
| **D2** | Read the headlines top to bottom. Do they tell the lecture's argument? | Headlines form a sequence of claims, each following from or building on the previous. | Headlines read as a list of topics (labels) with no visible logical thread. |
| **D3** | Is there a consolidation moment before the 20-minute mark, and another before the close? | Two consolidation slides at minimum — recap, worked example, or "what we just established." | Continuous new content from open to close, no breath. |
| **D4** | Does any single slide carry the deck's central claim? | A load-bearing slide exists; you can point to it. | No slide stands out; the thesis is implied, not asserted. |
| **D5** | If a colleague glanced through cold, would they know which course this is? | Headline grammar, figure conventions, and visual rhythm read as this course's. | The deck could belong to anyone — the DESIGN.md has not been owned. |

*Table 12.1 — The five deck-level checks. Run after the per-slide pass; under two minutes total.*

**D1.** What is this deck for? Live delivery, async study, or hybrid with notes field populated. A deck that has not answered this is a slideument waiting to happen.

**D2.** Is the deck's arc legible from the headlines alone? Read just the headlines, top to bottom. Do they tell the argument of the lecture? If they read as a list of topics, the deck has labels rather than claims.

**D3.** Is there at least one consolidation moment before the 20-minute mark, and another before the deck closes? Working memory needs to discharge before it can receive more.

**D4.** Does any single slide carry the deck's central claim? The deck without a load-bearing slide has no spine. Find that slide. If it cannot be found, the deck does not have a thesis.

**D5.** If a colleague glanced through the deck cold, would they know the course it belongs to? If the deck reads as generic, the DESIGN.md has not been owned.

---

## What the checklist does not catch

The checklist is a diagnostic for the eleven failure modes this book has named. There are failures it cannot see.

**Pedagogical misalignment.** The checklist catches whether the deck opens with a hook or a definition. It does not catch whether the learning objective for the lecture is the right objective for the course. That is a backward-design question — *what should the student be able to do at the end of this lecture?* — that no per-deck checklist can mechanize. Solving it is the work of instructional design for an entire course, not a pass over a finished deck.

**Audience misreads.** Some failures only show up in delivery. A slide that passes every checklist item can still fall flat with a particular audience — the analogy lands for engineers but not historians; the cultural reference dates the speaker. The checklist runs at the artifact level. The audience-level test is the lecture itself, and there is no shortcut to it.

**Decks built without the prior reading.** This is Bosk's failure mode at the reader level. A faculty member who downloads this checklist without reading Chapters 1 through 11 will find the questions vague and unanswerable. *Is the headline a claim or a label?* requires the vocabulary built in Chapter 10. *Does the body provide visual evidence?* requires Chapter 4. The questions are diagnostic instruments only for a reader who has the vocabulary. Without the vocabulary, the checklist is paperwork. I am being honest about this rather than pretending otherwise.

| What the checklist catches | What it cannot catch | What fills the gap instead |
|---|---|---|
| Per-slide failure modes — slideument, hierarchy, density, color, wrong visual form | Pedagogical misalignment — whether this lecture's objective is the right objective for the course | Backward course design — running the *what should the student be able to do?* question at the course level, not the deck level |
| Slideument / hierarchy / text / color failures inside the deck's artifact form | Audience misreads — the analogy that lands for engineers but not historians; the cultural reference that dates the speaker | Live delivery and iteration — the lecture itself, with the audience present, is the only test for this |
| Any of the eleven named failure modes for a reader who has the framework vocabulary | First-time reader with no vocabulary — *is the headline a claim or a label?* requires Chapter 10 to be answerable | Reading Chapters 1–11 — the vocabulary is what makes the questions diagnostic; without it, the checklist is paperwork |

*Table 12.2 — The checklist is complete for what it names. It is silent about what it does not name. Know the boundary.*

---

## When to stop using the checklist

Never. But what you do with it changes.

The first few decks: read each question, retrieve the relevant chapter vocabulary, apply it deliberately. The checklist is slow. You will find failures that surprise you — slides the eye missed because the eye was new. Each failure is the vocabulary being cashed out into actual seeing.

By the tenth deck: most items are answered before you finish reading the question. The eye does the assertion-or-label test reflexively. The hierarchy diagnostic fires without prompting. The checklist is no longer a procedure. It is the redundancy check that catches the slides built at 11 p.m. on a Sunday, when the defaults crept back in.

![The goal is internalization. The artifact is the net you fall into when the eye is tired.](images/12-the-diagnostic-checklist-fig-04.png)
*Figure 12.4 — A timeline or arc showing the familiarity gradient*

The surgeons who have run the WHO checklist for years still run it. The argument is the same here. The day you stop running the checklist because "I've got this" is the day the failures it was catching return.

Eleven chapters built the eye. This page is the redundancy check.

Run it once per deck. Then ship.

---

**What would change my mind:** A study of self-administered diagnostic checklists in non-clinical, non-aviation skilled-professional contexts showing that the working-memory-offload argument does not generalize to artifact production — that the checklist either fails to improve outcomes or actively interferes with the development of underlying judgment. The clinical and aviation evidence is strong; the inference to slide design is by structural analogy, not direct demonstration.

**Still puzzling:** The familiarity gradient — first read to reflexive — is consistent with the clinical evidence on sustained checklist use, but I do not have a study that calibrates how quickly internalization happens for self-administered diagnostic checklists applied to slide design, or under what conditions it stalls. The chapter argues from first principles and from analogy. A direct study would either confirm or revise the gradient.

---

## Exercises

### Warm-up

**1.** Gawande distinguishes read-do from do-confirm checklists. State in one sentence why this checklist is do-confirm rather than read-do, and identify the specific property of deck-building that makes the do-confirm architecture the correct choice.
*Tests: understanding the checklist architecture decision and why it fits artifact production rather than step-by-step procedure execution. Difficulty: low.*

**2.** The chapter identifies three things the checklist cannot catch: pedagogical misalignment, audience misreads, and decks built without the prior reading. For each of the three, name what replaces the checklist — what actually catches that failure if the checklist cannot.
*Tests: understanding the limits of the artifact and what fills each gap. Difficulty: low.*

**3.** A colleague says: "I skip the checklist questions that don't apply to my slide — I just mark them N/A and move on." According to the chapter, what is the correct behavior when a question does not apply, and why does the distinction matter?
*Tests: the one-discipline rule — N/A with articulated reason versus skip without reflection — and why the articulation is the point. Difficulty: low.*

---

### Application

**4.** Run the per-slide checklist items for Chapters 1 through 7 on this slide: headline reads "Machine Learning," body contains four bullets totaling 90 words that include a brief history of the term from the 1950s and a list of application domains, notes field is empty. For each chapter category, state Pass, Fail, or N/A, and for each Fail name the principle violated and the specific fix.
*Tests: applying the full per-slide diagnostic to a described slide; distinguishing seductive detail (history of the term) from redundancy from density. Difficulty: medium.*

**5.** Run the five D-level deck checks on a ten-slide deck with the following properties: all headlines are topic labels, no consolidation slides, deck opens with a definition of the course topic, notes field empty throughout, same visual template as the university's default PowerPoint theme. State Pass or Fail for each D-item, and for each Fail write the one-sentence fix.
*Tests: applying the deck-level checks rather than the per-slide items; recognizing that multiple D-level failures can occur simultaneously. Difficulty: medium.*

**6.** The chapter claims the checklist works because it offloads retrieval from working memory to a stable external artifact — the same mechanism Gawande identifies in aviation and medicine. A skeptic argues: "Slide design isn't life-or-death. The checklist analogy is overblown." Construct the best response to this argument that does not appeal to severity. The argument about working memory and retrieval failure should stand independently of whether the stakes are high.
*Tests: separating the mechanism argument (working-memory offload) from the stakes argument; showing the mechanism applies regardless of domain. Difficulty: medium.*

---

### Synthesis

**7.** After running the per-slide checklist on a hypothetical fifteen-slide deck, you find the following pattern: Chapter 1 (Slideument) fails on 11 of 15 slides, Chapter 3 (Too Much Text) fails on 9 of 15 slides, all other categories mostly pass. Using the DESIGN.md logic from Chapter 11, propose two specific DESIGN.md updates — not per-slide fixes — that would address the class of failure rather than the individual instances. For each update, state the variable name, the change, and a one-sentence rationale in framework vocabulary.
*Tests: recognizing systematic failure as a structural problem requiring a structural fix; applying the DESIGN.md update logic to the checklist's output. Difficulty: medium-high.*

**8.** The familiarity gradient — from slow deliberate retrieval on deck 1 to reflexive firing by deck 10 — is described by analogy to clinical checklist use. The chapter admits this is analogy, not direct demonstration. What would it mean for the gradient to "stall" — for a reader to still need deliberate retrieval at deck 15 or deck 20? Name two conditions that might cause the gradient to stall, and for each condition describe what a reader could do to restart internalization.
*Tests: thinking critically about the chapter's most uncertain empirical claim; applying the framework vocabulary to diagnose a meta-level failure in one's own learning. Difficulty: high.*

---

### Challenge

**9.** The Bosk critique applies not just to medical checklists but, by the chapter's own acknowledgment, to this checklist too: it works inside a broader context (having read the book) and becomes paperwork without it. Design a minimal "cultural change" scaffold — the analog of Pronovost's empowered nurses and data feedback loops — that would make this checklist usable for an instructor who has not read the book. What is the smallest set of background reading or orientation that substitutes for the full eleven chapters? Specify what each element provides and what failure modes it enables the checklist to catch. Be honest about what would remain uncatchable even with your scaffold.
*Tests: taking the Bosk critique seriously as a design problem rather than a caveat; reasoning about what the vocabulary actually requires and how much of it can be compressed. Difficulty: high.*

---

## LLM Exercises

**Exercise 1 — Single-slide audit**
Choose any slide from your current deck. Paste its full content — title, body, any figure description — to an LLM with this prompt: *"Run this slide through the per-slide diagnostic checklist. For each of the seven chapter categories (Slideument, Hierarchy, Too Much Text, Wrong Visual Form, Color, Textbook Figure, Seductive Details), assess: Pass, Fail, or N/A. Where N/A, state the reason. Where Fail, state which principle is violated and what the fix is. Do not fix the slide — only diagnose it."* Compare the LLM's findings to your own reading of the same slide.

**Exercise 2 — Deck-level arc check**
Extract just the slide headlines from an existing deck and paste them in sequence to an LLM with this prompt: *"Read these slide headlines in order. Answer the D2 deck-level check: do the headlines, read top to bottom, form a coherent argument — each claim following from or building on the previous? Or are they a sequence of independent topics with no visible logical thread? If the latter, identify where the argument breaks and name what connecting claim is missing between those two slides."* If the headlines do not form an argument, rebuild the arc before touching any individual slide.

**Exercise 3 — Systematic failure diagnosis**
After running the full per-slide checklist on a deck of ten or more slides, paste the list of failures to an LLM with this prompt: *"Here are the checklist failures I found across this deck, organized by slide number and chapter category: [list]. Identify any patterns — failure categories that appear on more than three slides. For each pattern, propose a DESIGN.md update that would fix the class of failure rather than requiring per-slide fixes. For each proposed update, state: the variable name, the change (from / to), and a one-sentence rationale in framework vocabulary."* Use the proposed updates as candidates for your DESIGN.md, not automatic changes.

**Exercise 4 — Do-confirm practice**
Build a new slide on any topic without consulting the checklist during construction. When finished, run the per-slide items for Chapters 1 through 7 on the slide and record which items you passed and which you failed. Then ask an LLM: *"I built this slide without consulting any checklist. Here is the slide and here are my self-assessed checklist results: [results]. Do you agree with my self-assessment? For any item I marked Pass that you would mark Fail, explain what I missed."* Repeat on three consecutive slides and look for the items you consistently miss — those are the failure modes your intuition is not yet catching.

**Exercise 5 — Checklist calibration**
After using the checklist on ten or more decks, reflect on the familiarity gradient by asking an LLM: *"Here are the checklist items I find myself answering automatically and the items that still require deliberate retrieval: [list both]. Based on this pattern, which failure modes have I internalized and which are still external to my intuition? For the items still requiring deliberate retrieval, suggest a one-sentence heuristic I could apply during slide construction — before the do-confirm pass — that would catch that failure mode earlier."* Use the heuristics as build-time prompts rather than only post-build diagnostics.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 12.1 — Two paired bar charts showing the Pronovost and

Create a standalone D3 v7 HTML file for a ranked or grouped bar chart titled "Two paired bar charts showing the Pronovost and". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-the-diagnostic-checklist-fig-01.html`

---

### Figure 12.2 — Diagram

Create a standalone D3 v7 HTML file for a concept map titled "Diagram". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-the-diagnostic-checklist-fig-02.html`

---

### Figure 12.3 — Two-axis chart

Create a standalone D3 v7 HTML file for a concept map titled "Two-axis chart". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-the-diagnostic-checklist-fig-03.html`

---

### Figure 12.4 — A timeline or arc showing the familiarity gradient

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "A timeline or arc showing the familiarity gradient". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-the-diagnostic-checklist-fig-04.html`
