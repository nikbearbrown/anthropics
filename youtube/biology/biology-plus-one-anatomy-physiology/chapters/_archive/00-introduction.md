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

Anatomy and physiology is a memorization-heavy field with high-stakes downstream applications. The model is fluent in anatomical terminology and casual about anatomical specifics. The gap matters because the field's students go on to become clinicians, surgeons, physical therapists, and researchers — and confident wrong anatomical knowledge is the kind of thing that ends careers and harms patients.

The body has a fixed structure. The names of muscles, the courses of nerves, the branching patterns of arteries, the layer-by-layer organization of an organ — these are facts, not interpretations. The model has read every anatomy textbook ever published. It will produce the canonical description of any structure on request. The description will be correct most of the time and confidently wrong some of the time, and the failure modes cluster around the structures that are most clinically important: the variant anatomy, the unusual nerve course, the artery that does not follow the textbook path.

Where the model genuinely helps: drilling you on terminology (Latin names, eponymous structures, layer sequences), explaining mechanisms (how the kidney concentrates urine, how the baroreceptor reflex works, how a muscle contraction couples to an action potential), producing the canonical mnemonic for a confusing arrangement of structures, generating practice questions at varied difficulty, and translating between textbook formal anatomy and the way clinicians actually talk about the body in practice.

Where the model does damage: producing specific anatomical details that contradict the textbook or the cadaver in front of you, hallucinating innervation patterns, confabulating arterial branching, and treating contested or variant anatomy as standard. The model has read enough anatomy to know that variation exists; it does not have the discipline to flag variation when it is reciting a structure. A model-generated description of the brachial plexus may include a branch that exists in 15% of people, presented as if it were the rule.

A specific failure mode worth naming: the model is good at the *systems* description (the cardiovascular system does X) and unreliable on the *structural* description (this nerve runs along this fascia, between this muscle and this vessel). The systems descriptions are taught at a level of abstraction the model handles well. The structural descriptions are taught at a level of specificity where small errors compound into large ones.

The rule that covers all three: the model knows physiology better than anatomy. Use it for mechanism, drilling, and mnemonics. Verify any specific anatomical claim against a textbook diagram, an atlas, or a cadaver. The body is the ground truth. Anatomy is the discipline of describing it correctly, and the model is too fluent to be trusted on the specifics.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
