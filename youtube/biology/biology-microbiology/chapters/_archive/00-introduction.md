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

Microbiology is a vocabulary-dense field with high-stakes clinical applications. The model is fluent in microbial taxonomy, pathology, and the canonical microorganism case studies. It is unreliable on species-level specifics — exactly the level where the field's most clinically important content lives.

The model has read every introductory microbiology textbook. It will produce competent paragraphs on bacterial cell structure, viral replication, fungal biology, microbial metabolism, antibiotic mechanisms, and the major host-pathogen interactions. The fluency is real and useful for the conceptual scaffolding the course is building. The problems begin at the level of specific organisms — naming a specific *Pseudomonas* species, identifying a particular toxin's mechanism, listing the resistance genes carried on a specific plasmid — where the model can confabulate plausible-sounding answers that are not correct.

Where the model genuinely helps: explaining mechanisms (how peptidoglycan is synthesized and what beta-lactams disrupt, how a retrovirus integrates, how spore formation works, how a phage life cycle plays out), surveying the major classes of microorganisms with attention to the structural features that distinguish them, walking through the standard methods of microbiological identification (Gram staining, culture, biochemical tests, MALDI-TOF, sequencing), and producing structured comparisons across organism classes.

Where the model does damage: stating specific facts about specific organisms. Microbial nomenclature is dense and continually revised, and the model has absorbed enough of the nomenclature to fluently invent plausible variants. A model-stated species name may be correct, incorrect, or a name that exists for a different organism than the one being described. Mechanism descriptions for specific virulence factors, toxins, and resistance genes can be similarly confabulated with the same confidence the model uses for textbook material.

A specific failure mode worth naming: the model is particularly unreliable on antibiotic resistance — which organisms carry which resistance, what the local resistance patterns are, what current first-line treatments are for a specific infection. These details depend on geography, time, and surveillance data the model does not have. Any clinical-microbiology specific from the model must be verified against current local antibiograms, CDC surveillance reports, or clinical guidelines.

The rule that covers all three: mechanisms and concepts from the model; species-specific facts from textbook diagrams, primary literature, NCBI, or current clinical guidelines. The model is a useful tutor on principles. It is not authoritative on any specific microorganism, and treating it as such can produce confident wrong knowledge that hurts clinical reasoning.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
