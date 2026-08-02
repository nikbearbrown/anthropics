# Chapter 9 — Live Deck vs. Study Artifact


## TL;DR

- Is this deck a visual anchor for your spoken explanation, or is it the self-contained explanation itself — and could a student make sense of it without you?
- The chapter moves through Two channels, one bottleneck, What the failure looks like, What the repair looks like, The prompt that forces the declaration, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Is this deck a visual anchor for your spoken explanation, or is it the self-contained explanation itself — and could a student make sense of it without you?*

---

Here is a complaint that comes in two forms, and the two forms seem to contradict each other.

First form: *the slides are so dense, I can't listen to you and read at the same time.* Second form: *I went back to the slides to study and they don't make sense without the lecture.* These are not complaints about different decks. They are complaints about the same deck, from different students, at different moments — the first during the lecture, the second three weeks later before the exam.

The instructor who hears both complaints is usually puzzled. The deck that was "too dense" during the lecture is also the deck that "doesn't make sense" without it. How can both be true at once?

Both are true because a single deck cannot simultaneously be a live anchor for spoken explanation and a self-contained study artifact. The two use cases impose opposite design constraints, and the constraints are opposite for a reason rooted in how working memory processes information. Understanding the reason is what makes the constraint precise rather than just frustrating.

![A horizontal bar split into two halves: the left half labeled "Live Mode" shows a speaker, a sparse slide with a single assertion, and an arrow flowing mouth-to-ear; the right half labeled "Study Mode" shows a student at a desk, a dense annotated slide, and an arrow flowing eye-to-brain. A vertical divider down the center reads "You cannot be on both sides."](../images/09-live-deck-vs-study-artifact-fig-01.png)
![Two modes, two design constraints. A deck that satisfies one violates the other.](images/09-live-deck-vs-study-artifact-fig-01.png)
*Figure 9.1 — Two modes, two design constraints. A deck that satisfies one violates the other.*

---

## Two channels, one bottleneck

Working memory is divided. There is a verbal channel — the one that processes language, whether spoken or read. There is a visual-spatial channel — the one that processes images and spatial relationships. These two channels are largely independent, which is why a spoken narration and a diagram can run in parallel without degrading each other. A voice explaining structure while a diagram shows it: two streams, two channels, no collision. That parallel processing is the core design insight behind good multimedia instruction.

The constraint arrives when both inputs to working memory are *language*. Text on a slide is processed through the verbal channel. The speaker's voice is also processed through the verbal channel. When a speaker narrates content that is already on the screen in text form, both inputs arrive at the same channel at the same time and compete. One wins; the other is suppressed. Usually the screen wins, because it is stable and effortless to attend to. The speaker becomes an audio track competing with printed text for the same limited resource.

Richard Mayer calls this the Redundancy Principle, and the experimental evidence is substantial: students given animation plus narration outperform students given animation plus narration plus on-screen text that duplicates the narration. The extra text made learning worse. Not neutral — worse. Both channels were flooded with the same content, and the collision extracted a real cost.

Now here is where it gets interesting. Mayer also established the Modality Principle, which seems to point in the opposite direction: people learn more deeply from pictures plus spoken words than from pictures plus printed words. The spoken narration uses the verbal channel while the visual uses the visual-spatial channel — two parallel streams, no bottleneck. A live lecture with sparse slides and a speaking instructor is the optimal configuration by this principle.

But Mayer specifies the boundary conditions under which the modality advantage holds. It is strongest for live, novel, instructor-paced instruction. It weakens or disappears when the material is learner-paced, when the content is highly technical and needs re-reading, when the learner is non-native, or when there is no narration available. Those boundary conditions describe study mode almost exactly. The principle that argues for sparse slides in live use is the same principle that argues against sparse slides in async study — because the principle depends on the narrator being present, and in study mode the narrator is gone.

This is the asymmetry. In live delivery, you have a narrator. The verbal channel is occupied by speech; the visual channel carries images cleanly; on-screen text becomes redundant and harmful. In async study without a narrator, the verbal channel is silent: the slide must carry text, because nothing else carries the verbal content. The same design move that respects the Modality Principle in one mode violates it in the other.

The decision that closes this gap is upstream of any individual slide: *which mode is this artifact for?* A slide tool will happily generate either. It cannot decide which one you need, because the answer depends on what your students are about to do with the deck — a fact the tool does not have. That is the moment to specify mode explicitly, before the file becomes one product that can never satisfy two contradictory specifications.

| Design dimension | Live mode | Study mode |
|---|---|---|
| Verbal channel source | Speaker's voice | On-screen text |
| Visual channel source | Diagram, minimal labels | Annotated visual with caption |
| Slide-body word count | 0–20 words | 60–150 words |
| Notes-field role | Full speaker script | Optional references |
| Retrieval mechanism | Speaker-enforced verbal prompt | Artifact-embedded attempt-then-reveal |

*Table 9.1 — The same design decision that serves live use violates study-mode requirements, and vice versa. A single deck cannot meet both columns.*

---

## What the failure looks like

The slide I want to examine is on the Central Limit Theorem, from an introductory statistics course. The instructor needs this slide for Monday's live lecture and for the async section that watches a recording later in the week. One deck. Both uses.

The slide has a topic-label headline — "The Central Limit Theorem" — followed by five bullets running to about seventy-five words. The bullets describe the theorem, its conditions, its conclusions. Reading time is roughly twenty seconds.

In live use, the instructor advances to the slide and begins explaining the CLT verbally. The students have already started reading the bullets — they are text, they are present, the verbal channel cannot resist processing them. By the time the instructor is two sentences in, half the room is still on bullet three. The verbal channel is split between reading and listening. The instructor is narrating content that is already on the screen. That is the Redundancy violation in real time.

In study use, three weeks later, a student pulls up the slide before the midterm. The five bullets are there. They are correct. They do not contain a worked example, a diagram of the sampling distribution narrowing as n grows, a derivation of the standard error formula, or a retrieval prompt to test understanding. They are five statements of fact arranged in a list. The student can read them and verify they have encountered the CLT. They cannot, from this slide alone, reconstruct what the CLT *does* or why it works. The slide stands alone in the sense that the words are present. It does not stand alone in the sense that the words explain.

![A rendered slide mockup of the slideument CLT slide: topic-label headline "The Central Limit Theorem" with five bullets running to about seventy-five words filling the body and an empty notes pane below. Two annotation callouts point in: one at the bullets reads "Live failure — student reads while speaker narrates (Redundancy violation)"; one at the empty notes pane reads "Study failure — no worked example, diagram, or retrieval prompt."](../images/09-live-deck-vs-study-artifact-fig-02.png)
![The slideument CLT slide. Too dense for the live moment; too sparse for the study moment.](images/09-live-deck-vs-study-artifact-fig-02.png)
*Figure 9.2 — The slideument CLT slide. Too dense for the live moment; too sparse for the study moment.*

Both complaints are valid. The deck is too dense for the live moment and too sparse for the study moment. The instructor is not at fault for trying to make one deck serve two purposes — that is the obvious, efficient choice. The fault is in not naming the constraint that makes the obvious choice structurally impossible.

---

## What the repair looks like

The repair is to produce two artifacts from one source.

The live deck carries a single assertion as the headline: *The sampling distribution narrows toward normality as n grows.* The body is an animation — the skewed source distribution at the top, sampling distributions for n of 2, 10, 30, and 100 rendered below it, each progressively narrower and more bell-shaped. That is the entire slide. The visual channel carries the mechanism. The verbal channel carries the speaker's explanation. The notes field holds the full speaker script: the derivation of the standard error, the worked example of halving the standard error by quadrupling the sample size, the connection to why inference methods work on non-normal populations. The notes are what the speaker reads, not what the audience sees.

The study artifact carries the same headline. The animation now has full labels — the standard error formula at each n, the population mean marked, the four distributions annotated with their standard errors. Below the animation: two paragraphs of prose that explain, in the absence of a speaker, why the sampling distribution narrows, what the formula σ/√n means, and why the result holds regardless of the population's shape. After the explanation: an embedded retrieval prompt — *A population has σ = 20 and you are sampling n = 100. You want to halve your standard error. How large does n need to be?* — followed by a reveal of the answer.

The content is identical across both artifacts. The assembly differs in five specific places: word count on the slide body, labels on the visual, presence of a prose explanation, presence of a caption, and the form of the retrieval moment. The live deck assumes a speaker. The study artifact cannot.

![Two slide mockups side by side, both carrying the same assertion headline "The sampling distribution narrows toward normality as n grows." Left panel "Live Deck" shows four sampling distributions at n = 2, 10, 30, 100 with minimal labels and a notes pane filled with speaker-script text. Right panel "Study Artifact" shows the same distributions fully labeled with σ/√n at each n, two paragraphs of prose explanation, and an embedded retrieval prompt with a hidden reveal. Annotation arrows mark the five specific differences between panels.](../images/09-live-deck-vs-study-artifact-fig-03.png)
![Same content, two artifacts. Word count, labels, prose, caption, and retrieval form differ; the head](images/09-live-deck-vs-study-artifact-fig-03.png)
*Figure 9.3 — Same content, two artifacts. Word count, labels, prose, caption, and retrieval form differ; the headline ports.*

What this requires is that the instructor declare, before designing the slide, which artifact they are making. That declaration is the design decision most slide failures begin by skipping. It feels unnecessary — "it's the CLT slide, it's the same either way" — but it is not the same either way, and the students feel the difference even when the instructor does not name it.

---

## The prompt that forces the declaration

When working with AI slide tools, the structural move is to give the tool a mode directive before it generates. Not "make this a lecture slide" — a mode flag that commits the output to a specific use case and makes a hybrid unacceptable.

---

*From this content source, produce two outputs.*

*Output 1 — live-lecture deck: each slide is a sparse anchor for spoken explanation. Headlines are full-sentence assertions. Body text is minimal — one image, one diagram, or one phrase. The slide does not stand alone; the speaker carries the explanation. The notes field is populated with the full speaker script for each slide.*

*Output 2 — study artifact deck: each slide is a self-contained explanation. Headlines are the same full-sentence assertions as in the live deck. The slide body contains the prose explanation as on-screen text. Visuals are captioned. Every three to five slides includes an embedded retrieval prompt the student attempts before revealing the answer.*

*Do not produce a hybrid. A hybrid is a slideument — text-heavy enough that the live audience reads instead of listens, but not detailed enough to study from when the speaker is absent. The hybrid serves neither use case.*

---

Two things to notice. First, the assertion headline is the same across both outputs. That is the one convention that ports: a full-sentence claim rather than a topic label. The student in the live lecture and the student studying alone both need to leave with an assertion in their head rather than a filing category. The assertion-evidence structure — full-sentence headline, visual or textual evidence in the body — is the shared grammar. What differs is how much the slide body carries and whether the notes field is the speaker's script or the student's study text.

Second, the explicit refusal of the hybrid is not aggressive. It is a constraint that protects both artifacts. The tool's default, without the directive, is to produce something that looks professional and complete — which is the failure mode disguised as thoroughness.

![A three-panel spectrum of slide mockups. Left "Live Deck": assertion headline, single animation, no body prose, notes pane filled with speaker script. Center "Slideument (the default)": topic-label headline, seventy-five-word bullet list, empty notes pane — a red X overlays this panel. Right "Study Artifact": same assertion headline as the live deck, labeled animation, two-paragraph prose, embedded retrieval prompt.](../images/09-live-deck-vs-study-artifact-fig-04.png)
![The spectrum. The tool's default lands in the center; both endpoints require explicit mode directive](images/09-live-deck-vs-study-artifact-fig-04.png)
*Figure 9.4 — The spectrum. The tool's default lands in the center; both endpoints require explicit mode directives.*

---

## Where retrieval lives in each mode

The two-artifact split makes visible how differently retrieval moments must be handled across the two use cases, and this difference is worth staying with.

In a live lecture, retrieval is something the speaker manages. A question posed out loud. A moment of paired discussion. A clicker prompt where the audience attempts before the instructor reveals the answer. The instructor enforces the attempt — the room waits, the timer runs, students cannot skip the effort. The slide may show the question; it does not need to embed the reveal mechanism, because the speaker is the mechanism.

In a study artifact, no speaker is present to enforce the attempt. A student who wants to skip the retrieval prompt and scroll to the answer will scroll to the answer, unless the artifact resists. The embedded reveal — the question visible, the answer hidden behind a click — is the study artifact's only leverage. It is a weak mechanism compared to a live instructor, but it is the best available. Slides that contain only declarative statements, with no retrieval structure, produce passive re-reading rather than active recall. Active recall is what produces durable memory; passive re-reading produces the feeling of knowledge without its substance.

A deck built for live use has no embedded retrieval because the speaker handles it. Posted as a study artifact after the lecture, the same deck invites passive re-reading. A deck built for study with embedded reveals and annotated visuals is disruptive in a live lecture, because the attempt-and-reveal sequence requires time the live session does not have. Each mode needs its own retrieval architecture, and the two architectures are not compatible in a single file.

![A two-column retrieval-architecture diagram. Left column "Live Mode" flows top-to-bottom: speaker icon, "poses question verbally," "room waits," "timer," "speaker reveals." Right column "Study Mode" flows top-to-bottom: "embedded question on slide," "student attempts," "click to reveal," "answer appears." A failure band beneath both columns reads "Passive re-reading — no retrieval structure — produces the feeling of knowledge without its substance."](../images/09-live-deck-vs-study-artifact-fig-05.png)
![Two retrieval architectures. The speaker is the mechanism in live mode; the artifact must be the mec](images/09-live-deck-vs-study-artifact-fig-05.png)
*Figure 9.5 — Two retrieval architectures. The speaker is the mechanism in live mode; the artifact must be the mechanism in study mode. A posted live deck provides neither.*

---

## Why the hybrid is the default

The slideument failure for a full deck has the same invisibility property as the slideument failure for a single slide.

At the point of design, the instructor is working alone. The live use case is not present; the study use case is not present; only the content is present. The deck that tries to serve both feels more responsible than the deck that commits to one — it feels like covering the bases. The two conflicting complaints arrive only after the deck has been used, at which point fixing it requires redesigning from scratch.

AI tools compound this in a specific way. The tool produces a deck that looks finished — professional, dense enough to seem complete, sparse enough to seem projectable. It has learned the aesthetic of the polished slide and has no way to measure what happens to the verbal channel in the room, or what a student's working memory does with the content in the absence of the speaker. The tool produces the slideument not because it is bad at design but because the slideument is what the training signal calls done.

The fix is upstream of the design tool: declare the mode before generating. The instructor who opens a slide tool and starts building is already in the negotiation between live and study, and the negotiation produces the hybrid by default. The instructor who says "this build is the live deck; the study artifact is a separate build from the same source" has already made the only decision that matters.

---

## A genuine disagreement

Once the two-artifact principle is accepted, there is a real disagreement worth naming about the notes field.

One position: a well-populated notes field converts a live deck into a functional study artifact. The slide carries the visual anchor; the notes carry the explanation; the student who downloads the deck in notes-view gets a complete document. The two-artifact workflow is unnecessary — one source file, one deck, notes field populated, and the student can study from it.

The other position: students do not use the notes field. They download the PDF of the slides and study from that, in slide view, without ever opening the notes. The notes field is technically a study channel but its actual adoption rate is too close to zero to count on as a design commitment. The instructor who relies on the notes field as the study artifact is designing for behavior they believe students should exhibit, not behavior the evidence suggests they do.

Both positions are defensible. The empirical answer depends on the LMS configuration — some learning management systems show notes by default when a student opens course materials; others hide them. The chapter's recommendation does not require resolving the disagreement. It only requires that the instructor know which configuration their students are actually using before deciding that the notes field is the study artifact.

| LMS configuration | Students reliably access notes | Students download slide PDF only |
|---|---|---|
| **LMS shows notes by default** | Notes field is a viable study channel; one-deck workflow may be sufficient | Notes field is visible but bypassed; study channel unused |
| **LMS hides notes by default** | Students actively seek notes; unusual but possible | Notes field is invisible to most students; two-artifact workflow required |

*Table 9.2 — The notes-field argument is conditionally valid. Verify your LMS configuration and student download behavior before relying on it.*

There is also a question about recorded narrated decks — slidecasts with sparse slides and dense audio narration — which seem to function reasonably well as async study materials despite being live-deck configurations. If the recording is what the student studies, then the recording is the study artifact and the sparse slide is the visual outline. The two-artifact rule generalizes here to "one deck and one recording," where the recording substitutes for the annotated study deck. Whether the substitution is complete is something I do not have a clean answer to. My intuition is that a recording is better than a sparse slide without audio and worse than a designed study artifact with embedded retrieval — but that is a guess about a spectrum, not a claim about a boundary. The vocabulary that makes the question answerable: *which channel is carrying the verbal content in this specific artifact, under the conditions the student is actually using it?* Answer that for the specific LMS, the specific student behavior, and the specific content, and the design decision follows.

---

**What would change my mind:** Empirical evidence that a single well-designed deck produces equal or better outcomes than a matched two-artifact pair on both the live-attendance retention measure and the post-lecture study-from-slides retention measure. The component evidence — Modality, Redundancy, assertion-evidence structure — supports the two-artifact split. A direct comparison of one-artifact versus two-artifact workflows on student outcomes is, as far as I have found, missing. That is the central empirical gap in this chapter's argument, and I hold the recommendation with appropriate tentativeness.

**Still puzzling:** The boundary between "sparse live deck plus its recording" and "designed study artifact" is not as clean as the chapter implies. Mayer's boundary conditions for when the modality advantage fades include learner-paced material, which a recording is — the student can pause and rewind. If pausing and rewinding closes the gap between a recorded lecture and a designed study artifact, the two-artifact workflow may matter less for institutions that systematically record. I have not worked through the cases carefully enough to know.

---

## Exercises

### Warm-up

**1.** A faculty member teaches a Tuesday lecture and posts the same slide deck to the LMS for students who missed class. The deck has 60-word-per-slide bullets and a speaker who narrates most of what the bullets say. Name the two Mayer principles being violated simultaneously, state which violation occurs in live use and which occurs in study use, and explain in one sentence why a single fix cannot resolve both.
*Tests: distinguishing the Redundancy and Modality violations and recognizing them as structurally opposed rather than additive. Difficulty: low.*

**2.** The Modality Principle argues for sparse slides paired with spoken narration. List the four boundary conditions Mayer specifies under which the modality advantage weakens or disappears. Then state which of those conditions apply to an async student studying from posted slides at midnight before an exam.
*Tests: understanding that the Modality Principle is conditioned, not universal, and that study mode satisfies the conditions that invert it. Difficulty: low.*

**3.** An instructor posts lecture slides as the study artifact. One student emails: "the slides have everything on them but I can't tell what mattered." A second student emails: "the slides don't make sense without the lecture." Both complaints are about the same deck. Explain how one deck produces both complaints simultaneously, using the channel-asymmetry argument from this chapter.
*Tests: tracing the two-complaint failure to a single structural cause. Difficulty: low.*

---

### Application

**4.** Design the live-deck version of a slide on a statistics concept of your choosing — confidence intervals or p-values, not the CLT. Write the assertion headline, describe the visual the body would show, and write three sentences of the notes-field speaker script. Then describe what changes in the study-artifact version: what labels are added to the visual, what prose is written on the slide body, and what retrieval prompt is embedded. You do not need to build both; describe both.
*Tests: generating the two-artifact split from scratch on new content; applying the five difference-points (word count, labels, prose, caption, retrieval form). Difficulty: medium.*

**5.** An instructor argues: "I populate my notes field with the full script. Students who want the explanation can read it there. I only need one deck." Construct the strongest rebuttal. What empirical fact about student behavior does the instructor need to verify before their argument holds? What LMS configuration question do they need to answer? Under what specific conditions does their argument become valid?
*Tests: identifying what makes the notes-field argument conditionally valid and what would falsify it; applying the decision matrix from this chapter. Difficulty: medium.*

**6.** A colleague records all lectures as slidecasts — sparse slides with dense audio narration — and posts the recordings to the LMS. They argue this makes a separate study artifact unnecessary. Identify the strongest version of their case and the weakest point in it. What does a recording provide that a designed study artifact also provides? What does an embedded-retrieval study artifact provide that a recording cannot?
*Tests: reasoning about the slidecast as a special case; identifying the specific gap that a recording does not close. Difficulty: medium.*

---

### Synthesis

**7.** Take a deck you currently use for a live lecture that you also post to students for study. Audit it: count the average words per slide body, check whether the notes field is populated, and ask whether a student who missed class could reconstruct the argument from the slides alone. Classify it honestly as live deck, study artifact, or slideument. If it is a slideument, identify the three slides that would require the most significant redesign to split into two proper artifacts, and state specifically what changes in each direction.
*Tests: applying the audit to one's own work; identifying the highest-cost redesign points rather than the easiest ones. Difficulty: medium-high.*

**8.** The chapter claims that "the features that make a slide good for live use are exactly the features that make it bad for study use." Find the strongest counterexample — a design decision that genuinely serves both modes without compromise. If you find one, name it and explain why it escapes the asymmetry. If you cannot find one, explain why the constraint is structural rather than typical.
*Tests: stress-testing the chapter's central claim; the assertion headline is the expected candidate, and the student should recognize both that it ports and why it is the exception rather than the rule. Difficulty: high.*

---

### Challenge

**9.** The chapter's "what would change my mind" section admits that a direct comparison of one-artifact versus two-artifact workflows on student outcomes does not exist. Design that study. Specify: the independent variable with both conditions described precisely, at least two dependent variables measured at different timescales (immediate retention vs. transfer three weeks out), how you would control for instructor, content difficulty, and prior knowledge, and what statistical result would constitute evidence that the two-artifact workflow is not worth the additional production cost. Then state the single biggest threat to internal validity in your design.
*Tests: ability to specify a missing study precisely enough to evaluate whether it would actually answer the question; scientific thinking about confounds and what "not worth it" means operationally. Difficulty: high.*

---

*The next chapter zooms back to the individual slide and asks the question that anchored both builds above: is this headline a claim or a label? The assertion-evidence structure is the slide-level expression of the live-deck philosophy, and it is where the chapters before it converge into a single practical commitment about what the top of every slide is for.*

---

##  AI Wayback Machine
The argument of this chapter — that the delivery medium dictates the message — has its sharpest pre-AI formulation in **Marshall McLuhan**. *Understanding Media* (1964) named it: *the medium is the message*. Print, radio, and television were not neutral pipes carrying content; each medium reshaped what the content could be, who received it, and how it was understood. A live lecture and a posted PDF are different media in McLuhan's exact sense, and the slideument is what happens when an author treats them as the same.

![Marshall McLuhan, circa 1970. AI-generated portrait based on a public domain photograph.](../images/marshall-mcluhan.jpg)
*Marshall McLuhan, circa 1970. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![Marshall McLuhan](../images/marshall-mcluhan-2tn.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Marshall McLuhan, and how does his "the medium is the message" argument from Understanding Media (1964) connect to the live-deck vs. study-artifact distinction in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Marshall McLuhan"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to map McLuhan's "hot" vs. "cool" media distinction onto the live-deck (cool — requires the speaker to fill in) vs. study-artifact (hot — fills itself in) split. Does the mapping hold? Where does it break?
- Ask about McLuhan's 1969 *Playboy* interview, his concept of the "global village," and what he would have said about a Zoom lecture posted to an LMS.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 9.1 — Two modes, two design constraints. A deck that satisfies one violates the other.

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Two modes, two design constraints. A deck that satisfies one violates the other.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-live-deck-vs-study-artifact-fig-01.html`

---

### Figure 9.2 — The slideument CLT slide. Too dense for the live moment; too sparse for the study moment.

Create a standalone D3 v7 HTML file for a concept map titled "The slideument CLT slide. Too dense for the live moment; too sparse for the study moment.". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-live-deck-vs-study-artifact-fig-02.html`

---

### Figure 9.3 — Same content, two artifacts. Word count, labels, prose, caption, and retrieval form differ; the head

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Same content, two artifacts. Word count, labels, prose, caption, and retrieval form differ; the head". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-live-deck-vs-study-artifact-fig-03.html`

---

### Figure 9.4 — The spectrum. The tool's default lands in the center; both endpoints require explicit mode directive

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "The spectrum. The tool's default lands in the center; both endpoints require explicit mode directive". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-live-deck-vs-study-artifact-fig-04.html`

---

### Figure 9.5 — Two retrieval architectures. The speaker is the mechanism in live mode; the artifact must be the mec

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "Two retrieval architectures. The speaker is the mechanism in live mode; the artifact must be the mec". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-live-deck-vs-study-artifact-fig-05.html`
