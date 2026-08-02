<!--
00-introduction.md — Book-level introduction.

The Introduction does different work than the Preface:
  - Preface  = why the book exists, why you wrote it (author's voice)
  - Introduction = what the book argues and how it is organized (reader's roadmap)

This file is a stub. Sections 1–10 and 12–13 are placeholders for a later pass.
Section 11 (A note about AI) is substantive and written.

A good model for the full version: Pearl's "The Mind Over Data" introduction,
Molnar's Interpretable ML introduction. Both are argument-first and tell the
reader exactly what to expect from each chapter.
-->

# Introduction

<!-- [1] COLD OPEN
     A specific named scene with real stakes.
     No "this book will...", no throat-clearing.
     Open on a sentence that contains the whole problem.
     Like the Swedish triage case in computational-skepticism-for-ai. -->

[COLD OPEN PLACEHOLDER]

<!-- [2] THE CENTRAL CLAIM — one sentence.
     "This book is about the gap between [X] and [Y]." -->

[CENTRAL CLAIM PLACEHOLDER]

<!-- [3] THE CENTRAL ARGUMENT — a testable, contestable claim
     about what the book is doing. -->

[CENTRAL ARGUMENT PLACEHOLDER]

<!-- [4] AUDIENCE LOCATION — one sentence locating who this is for. -->

[AUDIENCE PLACEHOLDER]

---

## What This Book Is

<!-- [5] Scope. The work the book names. Vocabulary it teaches. -->

[SCOPE PLACEHOLDER]

## What This Book Is Not

<!-- [6] Explicit exclusions. Prerequisites. -->

[EXCLUSIONS PLACEHOLDER]

---

## A Central Concept That Runs Throughout

<!-- [7] A recurring idea readers should watch for across chapters.
     Like "the fluency trap" in computational-skepticism-for-ai. -->

[CENTRAL CONCEPT PLACEHOLDER]

<!-- [8] (OPTIONAL) A RUNNING NARRATIVE THREAD
     A case that recurs across chapters as a worked example.
     Like "Ash" in computational-skepticism-for-ai.
     Delete this section if not using a running thread. -->

## A Running Narrative Thread

[NARRATIVE THREAD PLACEHOLDER — delete this section if not using one]

---

## How This Book Is Organized

<!-- [9] Chapter-by-chapter map. Group into movements (clusters of 3–5)
     if applicable. One sentence per chapter is enough. -->

[CHAPTER MAP PLACEHOLDER]

## How to Read This Book

<!-- [10] Order. Prerequisites for skipping around.
     Self-contained chapters. Chapter-closing features
     (e.g., "What would change my mind", "Still puzzling", exercises). -->

[READING GUIDE PLACEHOLDER]

---

## A Note about AI

Organic chemistry is the field where the model is most fluently and most dangerously confident. The model has read every organic chemistry textbook in print. It will explain any reaction mechanism, produce any synthesis, predict any product — and a meaningful fraction of what it produces will be wrong in specific ways that look right to a student.

The textbook teaches a vocabulary of structures and a grammar of reactions. The grammar is rules — what attacks what, what migrates, what eliminates, what conformation a transition state takes. The model knows the rules. The application of the rules to a specific molecule is where most failure modes live, and the failures are subtle: a regiochemistry the model gets backward, a stereochemistry it ignores, a side product it predicts as the main product, a mechanism that looks textbook and contains a step that does not happen.

Where the model genuinely helps: explaining a named reaction in plain language (what the Diels-Alder is, what makes a Grignard reagent reactive, why an E2 elimination requires anti-periplanar geometry), walking through the conceptual logic of a reaction class (why electron-poor alkenes are reactive in conjugate addition, why aromatic rings resist addition but undergo substitution), drilling on nomenclature and functional-group identification, and producing the canonical mechanism for the cases the textbook treats as canonical. The model is useful as a vocabulary scaffolder for the dense jargon of the field.

Where the model does damage: predicting products and writing mechanisms for specific molecules. The model will get regiochemistry wrong on Markovnikov-style additions, get stereochemistry wrong on cyclic substrates, predict the kinetic product when the thermodynamic product is the answer, and miss neighboring-group participation that changes the outcome. The wrongness is structural — the *shape* of the answer is right and the *details* are wrong — which is the worst failure mode for a student trying to learn.

A specific failure mode worth naming: the model is fluent in producing curly-arrow mechanism diagrams (in text form) and will produce mechanism arrows that violate octet rules, move electrons in directions that do not happen, or invent transition states that contradict the rules the textbook just taught. A student who copies these mechanisms imports specific structural misunderstandings that surface badly on exams.

The rule that covers all three: vocabulary and conceptual logic from the model; specific predictions, mechanisms, and stereochemistry from your pen, the textbook diagrams, and (when available) the literature. Organic chemistry is taught through the discipline of pushing electrons correctly. The model has read the discipline; it does not perform it reliably. Every mechanism the model produces should be checked against the textbook's rules, not against the model's confidence.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
