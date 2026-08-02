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

Astronomy is a field with two clocks. The classical content — orbital mechanics, stellar evolution, the structure of the solar system, the basic taxonomy of galaxies — is stable. The frontier — what JWST observed last month, what the latest gravitational-wave detection means, what the current best estimate of the Hubble constant is — moves week by week. The model is fluent on the first clock and unreliable on the second.

The model has read centuries of astronomy textbooks and decades of observational papers. It will recite Kepler's laws, explain the proton-proton chain, walk through stellar nucleosynthesis, and describe the Big Bang nucleosynthesis predictions on request. The fluency is real and useful. It becomes a problem when the question shifts to what we have learned recently — because the model's training cutoff is months or years before today, and astronomy's most interesting claims are usually about results that postdate any cutoff.

Where the model genuinely helps: walking through the classical mechanics (orbits, conservation laws, tidal forces), explaining the canonical observational techniques (spectroscopy, parallax, photometry, interferometry), telling the historical story of major discoveries with attention to what was contested at the time, and producing structured comparisons across object classes (how a brown dwarf differs from a giant planet, how a Type Ia supernova differs from a core-collapse supernova).

Where the model does damage: stating specific values for cosmological parameters, declaring the resolution of contested questions in current astronomy (the Hubble tension, the nature of dark energy, the existence of Planet Nine), and reporting on observations made by current missions as if the reports were settled. The model also confidently mishandles the order of magnitude on specific numerical questions — the temperature of a particular star, the luminosity of a specific quasar, the redshift of a recently announced object — because the specific values come from specific papers and the model's training samples those papers unevenly.

A specific failure mode worth naming: the model treats theoretical predictions and observational measurements interchangeably. Asked what the mass of a black hole is, the model may produce a theoretical estimate, an observational measurement, or a confident average of the two, without flagging which is which. The distinction matters because theoretical estimates are based on assumptions and observational measurements have error bars.

The rule that covers all three: classical astronomy from the model; current astronomy from primary sources (NASA mission pages, arXiv preprints, the latest editions of textbooks, named observatories' press releases). The training cutoff is the boundary. Treat any specific numerical claim about a current object or a current parameter as a starting point, not as an answer.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
