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

Calculus is a field with two distinct skills: doing the procedure and understanding why the procedure works. The model is more useful for the second than the first, and the textbook is structured around developing both. The note examines where each skill lives.

The model has read every calculus textbook in print. It will explain limits, derivatives, integrals, and the fundamental theorem in plain language; it will produce worked examples at any level of detail; it will translate between geometric, algebraic, and analytic interpretations of the same result. This conceptual fluency is genuinely useful — calculus is taught by a sequence of explanations that have to land, and the model is good at producing alternative framings until one lands for a given student.

Where the model genuinely helps: explaining a concept three different ways (geometric, algebraic, analytical), walking through a proof with attention to which step is doing the work, producing worked examples at graded difficulty, surfacing common student errors before they happen, and translating between notations (Leibniz vs. Lagrange, definite vs. indefinite, partial vs. total derivatives). The model is also useful as a sanity check on your own derivation — paste your work and ask the model where it would have gone differently.

Where the model does damage: performing the actual arithmetic and algebra of a specific problem. The model is fluent in the language of calculus and unreliable as a calculator. It will simplify an expression incorrectly, miss a sign change, fumble the chain rule on a composition with three nested functions, and confidently present the wrong answer as the right one. The wrongness is often subtle — the structure of the answer is right and one term is wrong — which is the worst possible failure mode for a student trying to learn.

A specific failure mode worth naming: the model produces *plausible-looking* derivations that contain a single wrong step buried in correct steps. A student copying the derivation as a study aid imports the error without noticing. The model will also defend the wrong step when asked, because the structure of the surrounding work is correct and the model uses the surroundings as confidence.

The rule that covers all three: concepts and explanations from the model; the actual computation from your pen. Calculus is taught through procedure and only the procedure builds the muscle. If you let the model do the algebra, you have not done the algebra, and the next problem (which is structurally similar) will reveal the gap.

---

## Closing

<!-- [12] Callback to the opening scene. End with a directive. -->

[CLOSING PLACEHOLDER]

---

**Tags:** <!-- [13] 5–8 discoverability tags --> [TAGS PLACEHOLDER]
