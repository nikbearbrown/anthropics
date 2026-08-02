# Introduction

A patient walks out of a clinic with a positive result on a test that is 99% accurate for a disease that affects one person in a thousand. How worried should they be? Most people — including, in a famous 1978 study, most of the Harvard medical staff asked — answer "about 99%." The actual answer is closer to 9%. The test is excellent. The intuition is catastrophic. And the gap between the two is the subject of this book.

That gap is not a trick. It is the difference between two questions that sound identical and are not. *How surprising is this result if the patient is healthy?* and *How likely is this patient to be sick?* are different questions with different answers, and a great deal of confusion — in medicine, in courtrooms, in published science — comes from answering the first while believing you have answered the second.

## What This Book Is

This book teaches statistical inference by solving every problem two ways: first with frequentist methods (the p-values, confidence intervals, and significance tests most readers have already met), then with Bayesian methods (which assign probabilities directly to the hypotheses you care about), set side by side on the same data. It is a working course, not a survey. Each chapter takes a concrete problem, builds both solutions completely, shows exactly where the frequentist approach strains, shows what the Bayesian approach buys and what it costs, and ends by asking the reader to choose.

## What This Book Is Not

This book is not an argument that Bayesian methods are superior. They are not, in general — there are problems and settings where frequentist methods are the right and even the required choice, and the book names them plainly. It is not a full course in Markov chain Monte Carlo or probabilistic programming; where that depth is needed, the reader is pointed onward (McElreath's *Statistical Rethinking* is the standard next step). And it is not a coding manual: implementation is done with AI assistance, so the reader can concentrate on the reasoning.

## The Concept Running Through the Book

The recurring idea is **the choice itself**. Neither paradigm is universally correct. Competent practice is selecting the right approach for the problem in front of you — given what the decision-maker actually needs, whether defensible prior information exists, how much data there is, and who will receive the result. Every chapter is built to make that choice visible by performing both analyses, so that by Chapter 13 the reader has a framework for choosing rather than a default to reach for.

A second thread runs underneath: the division of labor between human and machine. The book uses AI to *execute* analyses and asks the reader to *judge* them — to formulate the question, specify the prior, and verify that the output is right rather than merely fluent. That division is the heart of the Irreducibly Human series, laid out in the appendix *The Fundamental Themes*.

## How This Book Is Organized

A short **Chapter 0** resolves the only prerequisites — conditional probability and Bayes' theorem as arithmetic — and can be skipped by readers already comfortable with them. **Act One (Chapters 1–4)** establishes that the paradigms answer different questions and teaches AI-assisted implementation. **Act Two (Chapters 5–9)** builds the methods where the divergence carries decision weight: regression, model comparison, priors, sparse data, hierarchical models. **Act Three (Chapters 10–13)** covers time and sequential updating, classification as a decision under costs, a guided capstone on a real dataset, and a closing framework for choosing.

## How to Read This Book

Read Chapter 0 first if conditional probability is rusty, then Chapter 2 before relying on the AI-implementation sections in later chapters — the rest of the book assumes that skill. After that, the chapters build in order, but a reader consulting the book for a specific problem can jump to the nearest chapter, provided they keep the comparative habit: always ask what each approach can and cannot tell you.

## A Note About AI

This book is written for the AI era and uses AI throughout — to generate code, run analyses, and produce comparisons. It is not an invitation to outsource understanding. An AI will write statistical code that runs cleanly and computes the wrong thing; it will explain a result in language that quietly swaps a p-value for a posterior probability. Catching that requires exactly the judgment this book builds. The machine executes. You decide what to ask, which prior to defend, and whether the answer is true.

## Closing Return

Return to the patient with the positive test. The arithmetic that turns 99% into 9% is not advanced — it is in Chapter 0. What is hard is knowing that the question demands it, recognizing when a confident answer is answering the wrong question, and being able to defend the method you chose. That recognition is the work this book is about. Begin with the next chapter.

## Tags

#bayesian #probability #statistics #frequentist #inference #AI #Medhavy #Medhavi #IrreduciblyHuman #intelligent-textbook
