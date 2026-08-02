# Bear's Doodles — AI for Slides: A Practitioner's Guide Video Ideas

**Scouted:** 13 chapters (intro + 01–12 + fundamental-themes).

**Why this slate is short — and why that's correct.** This is a slide-*design* book, so it is built almost entirely out of "bad slide → good slide" before/after comparisons. Those are *static-sufficient*: a reader sees both end states side by side and learns fine — there's no transition to watch, so they are not Bear's Doodles candidates no matter how instructive. I held the motion bar hard and rejected every redesign whose teaching lives in comparing two layouts. What survived, in every case, is a genuine **cognitive mechanism** underneath the design rule — dual-channel working memory, attention capture, a scan path, an overflow — where the learning really is in watching the process unfold. That's 10 candidates, not 20, and padding it would mean shipping static comparisons dressed up as animations.

**Consolidation notes for pick-time.** The book teaches a few core mechanisms repeatedly under different chapter titles; I merged those into one card each and cited where they recur:
- **The verbal-channel collision (redundancy)** anchors Chapter 1 and returns in Chapters 3 and 9 — one video services all three.
- **The seductive-detail / schema mis-routing** mechanism spans Chapters 3 and 7 — carded once from the fuller Chapter 7 treatment.
- **Working-memory overflow** appears in Chapters 2, 6, and 8 — but as *two genuinely distinct* dynamics: one dense figure flooding at once (06) vs. a whole deck that never lets memory discharge (08). Both kept; they share a "WM tank" motif, so differentiate the visuals.
- **Chapters 11 and 12 (owning your design / the diagnostic checklist) yielded zero** — they're framework and checklist chapters with nothing to animate. That's the honest result, not a gap.

---

## Candidate 01 — Why saying it out loud AND putting it on the slide teaches less than either alone

- Source: `ai-for-slides-a-practitioners-guide/chapters/01-the-slideument-problem.md`
- Production mode: Manim visualization
- Hook: Reading your point on the slide while you also say it should double the teaching — instead the two identical streams collide in one channel and one gets erased.
- Core idea: On-screen text and the speaker's voice are both language, so they pour into the single verbal channel and compete — the stable screen wins, the speaker is suppressed — while a diagram runs in the separate visual-spatial channel with no interference.
- Visual object: A two-lane pipe — the verbal lane, into which a stream of on-screen words and a stream of spoken words both pour and jam at a bottleneck; the visual-spatial lane beside it carrying a diagram cleanly
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: you read and listen at the same time; the feeling of a slide being "too dense to listen to"
- Exclusions: no full working-memory-model lecture; the collision-and-suppression is the whole video. This mechanism recurs in Ch 3 and Ch 9 — build once. (Mayer's Redundancy Principle: adding on-screen text made outcomes *worse*, not neutral)
- Score: 9/10

## Candidate 02 — Why the eye tours your slide in exactly the wrong order

- Source: `ai-for-slides-a-practitioners-guide/chapters/02-no-clear-hierarchy.md`
- Production mode: Manim visualization
- Hook: Every element was placed on purpose — and the eye still visits them in the wrong order and leaves with the wrong idea.
- Core idea: The visual system lands on the highest-contrast element first, in ~50 ms, before any reading happens; if a heavy "Did you know?" callout out-weighs a thin-ratio title, the eye goes callout → bullets → title, and only a real 2:1 size hierarchy re-routes it to land on the claim first.
- Visual object: One slide with a moving gaze-dot (or spotlight) tracing its actual landing order, numbered 1-2-3 as it hops — then re-routing after the hierarchy fix
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: you look before you read; the idea that bigger/bolder pulls the eye
- Exclusions: no magnocellular/parvocellular neuroscience detail; the scan path is the teaching — a static "before/after layout" cannot show the reading order, which is the entire point
- Score: 8/10

## Candidate 03 — Why "as you can see" fails when the headline is just a label

- Source: `ai-for-slides-a-practitioners-guide/chapters/10-the-headline-that-says-nothing.md`
- Production mode: Manim visualization
- Hook: The speaker says "as you can see, infection rates dropped 66%" — and the audience genuinely can't see it, because they're hunting the wrong graph.
- Core idea: A label headline ("Results") forces the viewer to reconstruct the claim from the evidence first, so the eye hunts across all three panels burning the working memory that should process them; a claim headline hands over the assertion up front, pre-activating a slot the evidence drops straight into and pointing the eye at the right panel before the speaker talks.
- Visual object: One "Results" slide with three graphs; a gaze-dot either wanders all three searching (label) or arrows straight to the middle panel (claim), while a "slot" above the slide stays empty or lights up ready to receive
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: slides have titles; a graph shows evidence
- Exclusions: no assertion-evidence-structure history lecture; the scan-path re-route and the "assertion arrives before evidence" timing are the mechanism — a static label-vs-claim table can't show either. (Alley & Neeley 2005; twelve-word ceiling)
- Score: 8/10

## Candidate 04 — Why a comparison in bullets makes you rebuild it in your head

- Source: `ai-for-slides-a-practitioners-guide/chapters/04-the-wrong-visual-form.md`
- Production mode: Manim visualization
- Hook: The whole comparison is right there on the slide, nothing hidden — yet you can't answer "which option handles equity best?" without re-reading three times.
- Core idea: A comparison is secretly a matrix (attributes × things), and rendering it as parallel bullet columns deletes the axes — so the reader must hold one bullet in memory, shift attention, search the other column for its match, hold both, and compare, leaking precision at every hop; a table restores the axes as row labels at near-zero cost.
- Visual object: Three bullet columns with a gaze-dot ricocheting back and forth trying to line up matching items, then the content snapping into a table where the comparison axes simply appear as rows
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: bullet points; a comparison table
- Exclusions: no full Cleveland-McGill accuracy-ranking tour; the ping-pong reconstruction and the snap-to-table are the lesson — a calm static bullets-vs-table pair never makes you feel the reconstruction tax
- Score: 8/10

## Candidate 05 — Why the most interesting fact on the slide is the one they'll remember instead of the point

- Source: `ai-for-slides-a-practitioners-guide/chapters/07-seductive-details.md`
- Production mode: Manim visualization
- Hook: Adding genuinely interesting, on-topic material to a lesson made students remember *less* — not because it distracted them, but because it worked.
- Core idea: The vivid detail arrives first and primes the wrong schema in working memory, so when the structural content shows up its correct slot is already occupied — it attaches weakly under the wrong frame and is lost ("diversion").
- Visual object: A working-memory space with two scaffolds; an anecdote drops in and lights up the wrong scaffold, then the real content-pieces arrive too late and visibly bounce off / drift
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: you build mental models around what stands out; the idea of a memory "hook"
- Exclusions: mechanism is partly internal — anchor on the sequence (wrong scaffold primed first, content can't attach); no meta-analysis walkthrough. This spans Ch 3 and Ch 7 — build once. (Harp & Mayer 1998: seductive details ≈ one-third the retention; damage shows up two weeks later)
- Score: 8/10

## Candidate 06 — Why the complete, accurate figure is the one the back row learns nothing from

- Source: `ai-for-slides-a-practitioners-guide/chapters/06-the-textbook-figure-on-the-slide.md`
- Production mode: Manim visualization
- Hook: The complete, correct, beautifully labeled figure — the excellent one — is exactly the figure from which nobody learns.
- Core idea: A ten-step figure dumped at once floods working memory within ~30 seconds and none of it encodes; built across four slides that reset and accumulate a schema piece by piece, the same figure lands last as recognition rather than overload.
- Visual object: A working-memory "tank" beside the slide — the one-shot figure floods and overflows it; the segmented build drips in and fills it in stable, absorbable increments as the diagram assembles
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: working memory has a limit; a complex diagram
- Exclusions: don't storyboard all four fix-panels statically (the chapter already does) — the overflow event is what motion adds; keep the WM-tank visually distinct from Candidate 07. (Mayer's Segmenting & Pre-Training Principles)
- Score: 8/10

## Candidate 07 — Why you can cover all sixty slides and still teach nothing

- Source: `ai-for-slides-a-practitioners-guide/chapters/08-the-deck-that-covers-but-doesnt-teach.md`
- Production mode: Manim visualization
- Hook: You covered every slide, missed nothing, finished at the bell — and two weeks later a third of the class can define the terms but can't do the thing.
- Core idea: Each concept depends on the last, but they arrive faster than the student can consolidate, so the schema for slide 4 is still fragile when slide 11 pulls on it; with zero retrieval moments, working memory fills with reception and never discharges — recognition accrues, production never does.
- Visual object: A working-memory vessel filling as dependent blocks stack on a wobbling foundation with no drain valve, overflowing by the worked example — then the fix inserts retrieval moments you watch the vessel drain
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: concepts build on each other; the difference between recognizing and doing
- Exclusions: keep the vessel visually distinct from Candidate 06 (that's one figure flooding; this is a whole deck never discharging); no spacing-effect meta-analysis. (Karpicke & Roediger 2008: recall ~60% vs restudy ~40% at one week)
- Score: 7/10

## Candidate 08 — Why the slide that's perfect live is useless for studying

- Source: `ai-for-slides-a-practitioners-guide/chapters/09-live-deck-vs-study-artifact.md`
- Production mode: Manim visualization
- Hook: The sparse slide that works beautifully in the talk becomes useless three weeks later — and the fix isn't editing the slide, it's that one source has to become two different decks.
- Core idea: Live, the speaker's voice fills the verbal channel so the slide can be near-empty; remove the speaker and that channel goes silent with nothing to carry the words, so the study artifact must grow on-screen prose, labels, and an embedded retrieval reveal — and the assertion headline is the one element that ports to both.
- Visual object: A single deck that splits down the middle into a "Live" copy and a "Study" copy, the shared headline anchored across the seam while five attributes diverge
- Manim move: split
- Short-form fit: Medium
- Prerequisites: Candidate 01's verbal channel helps; a slide vs. a handout
- Exclusions: the causal beat is "pull the speaker out, watch the verbal content vanish, forcing the study slide to add text" — not a static three-panel spectrum; name the five diverging attributes, don't belabor each
- Score: 7/10

## Candidate 09 — Why six "professional" colors cost you more than two

- Source: `ai-for-slides-a-practitioners-guide/chapters/05-color-is-doing-nothing-or-harm.md`
- Production mode: Manim visualization
- Hook: A slide with six tasteful colors looks more designed than a two-color slide — and that extra polish is quietly taxing the audience.
- Core idea: The instant a color appears the brain hunts for the rule it encodes; when four decorative colors mean nothing the search fails and burns working memory for no return, and the one color that should matter is drowned at equal weight — strip to one neutral plus one accent and the noise drains, leaving the eye nowhere to go but the claim.
- Visual object: A six-color status slide where a gaze-dot darts among the colored elements probing for a code and finds none, then five colors desaturate to gray and the single accent on the one thing that matters is left standing
- Manim move: collapse
- Short-form fit: Medium
- Prerequisites: color can carry meaning; the idea of signal vs. noise
- Exclusions: the futile rule-search and the noise-draining-to-reveal-signal are the two beats — a static failing-vs-fixed pair shows neither; the "if you can't say what a color means in one word, it shouldn't be on the slide" line is the closer
- Score: 7/10

## Candidate 10 — Why removing the struggle removes the learning

- Source: `ai-for-slides-a-practitioners-guide/chapters/97-fundamental-themes.md`
- Production mode: Mixed (Doodle metaphor + Manim cascade)
- Hook: Students who used AI freely scored 48% higher during practice and 17 points lower on the unassisted exam — they felt mastery while their brains never changed.
- Core idea: Learning is a physical event — cognitive friction (a prediction error) fires a cascade of dopamine, BDNF, synapse strengthening, and dendritic-spine growth — and removing the friction removes the trigger, so no consolidation happens even though the output looks finished.
- Visual object: A single synapse — a "prediction error" spark fires the cascade and grows a spine on the friction path, while the same synapse sits inert as a fluent AI answer scrolls past on the frictionless path
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: neurons strengthen with use; "productive struggle"
- Exclusions: **Cross-book note — this is the "AI for X" series' recurring fundamental-themes cascade and is already carded for the AI-for-Learning-Experience-Design book; dedupe across books before building.** Teach the cascade as a *motivated hypothesis* — the source's own fact-check calls the strict chain "overdrawn as a universal mechanism" and the 55%-connectivity figure a single preprint. Tangential to slide design specifically
- Score: 8/10

---

## Cutting-room floor (rejected — and why this list is long)

The overwhelming majority of this book is **static before/after redesigns**, which teach fine from a still image and are not motion candidates: the oxidative-phosphorylation slideument rebuild (01); the 134-words→36-words repair and the bad-vs-good hierarchy slide (02/03); the wrong-form→right-form table across six structural types and the decorative-vs-structural diagram (04); the failing six-color slide→two-color slide, the colorblind simulation, and the gradient-background contrast strip (05); the textbook-figure→cropped/enlarged/simplified panels and the instructor-vs-student experience columns (06); the Krebs failing-vs-repaired slide and the diagram-area proportion mockup (07); the coverage-vs-teaching decision table and backward-vs-forward design flowchart (08); the live-vs-study dimension table and the notes-field configuration matrix (09); the assertions-as-argument vs labels-as-contents side-by-side and the label-vs-claim grammar table (10). Rejected as **checklist/framework with nothing to animate**: design tokens, the owned-vs-unowned DESIGN.md, and the ownership 2×2 (11); the entire diagnostic do-confirm checklist, the Boeing 299 story, and the Pronovost/Haynes numbers (12); and the phase-gate, seven-tier taxonomy, AI+1 premium, and Boondoggle Score frameworks (97). Rejected as **static PQ** (a real number, but a bar/line chart carries it): the Harp-Mayer retention bars (07), the Karpicke-Roediger recall bars and Cepeda spacing curve (08). Chapters 11 and 12 produced zero motion candidates, as expected. Many of these are strong *written* explainers — they simply aren't videos.
