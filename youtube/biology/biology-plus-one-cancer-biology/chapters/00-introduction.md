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

Cancer biology is the subject-matter textbook where AI's failure modes most directly intersect with patient harm. The chapter-by-chapter notes in this book name the specific vulnerabilities at each topic; this book-level note names what is true across the whole.

The model is fluent in cancer biology vocabulary, mechanisms, and the canonical case studies. It will explain oncogenes and tumor suppressors, walk through the hallmarks of cancer, recite the major chemotherapy classes, and describe the architecture of checkpoint inhibitors. The fluency reflects the model's training on textbooks, review articles, and clinical guidelines. It does not reflect training on the patient in front of any clinician, and that gap is the source of every important failure mode.

Where the model genuinely helps: explaining mechanisms (how p53 normally arrests the cell cycle, how a chromosomal translocation produces an oncogenic fusion protein, how a checkpoint inhibitor releases a T cell), walking through the historical development of a treatment class, summarizing the structural arguments for and against contested approaches (e.g., whether early-detection screening is net beneficial for a given cancer at a given population), and producing accessible explanations students can use to teach the material back to themselves. The model is also useful for vocabulary drills, mnemonic generation, and producing structured comparisons across cancer types.

Where the model does damage: producing specific clinical claims — drug doses, trial results, survival statistics, drug interactions, treatment recommendations. The clinical literature is enormous, contested, and time-sensitive. The model has read summaries rather than primary trials. It will state a five-year survival rate with confidence when the rate depends on subtype, stage, treatment, and time period. It will recommend a treatment without flagging that the recommendation depends on guidelines that update yearly and on the specific tumor profile in a specific patient. Specific patient-care decisions made on the basis of model output are unsafe.

A specific failure mode worth naming: the model fabricates clinical trial names, dosing protocols, and specific outcomes with the same confidence it uses for established textbook material. The fabrications follow the shape of real trials (recognizable acronyms, plausible patient counts, conventional endpoints) and can fool a careful reader. Any clinical specific from the model must be verified against ClinicalTrials.gov, the trial's primary publication, or current NCCN/ESMO guidelines.

The rule that covers all three: textbook mechanism and history from the model; specific clinical claims from primary sources. The students in this book are training to do work where the cost of fluent wrong information is measured in lives. The model is a useful tutor. It is not a clinician. The boundary has to be visible at every chapter, which is why each chapter in this book has its own note about AI applied to the local content.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
