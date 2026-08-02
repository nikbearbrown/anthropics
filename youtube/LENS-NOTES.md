# LENS-NOTES.md — Computational Skepticism Source Material

Generated from reading the four CS chapters before any scripting.
Exact quotes from the book are used; nothing paraphrased in the quote blocks.

---

## The Four Moves — in Bear's own words

### DISCREPANCY NOTE — flagged for Bear

`_ch1-what-i-mean-by-skepticism.md` says: "Three philosophers donate moves to the toolkit."

`_expanded-four-moves.md` says: "Four philosophers donate them." — adding Plato.

**Recommendation:** The expanded file is the fuller, more recent treatment. These notes use
FOUR moves (Descartes, Hume, Popper, Plato). Bear should reconcile this in the book's Ch1
prose before publication — the "three philosophers" sentence in `_ch1-what-i-mean-by-skepticism.md`
is inconsistent with the expanded treatment that adds Plato's Cave.

---

### 1. Descartes — Radical Doubt

Source: `_ch1-what-i-mean-by-skepticism.md`, `_expanded-four-moves.md`

Bear's description: "Treat every claim as a conjecture and ask what it would take to falsify it,
before the world does the falsifying for you."

The move: "What would have to be true for this claim to be wrong about the world?" — asked not
as a mood but as a question that produces a checklist.

Key quote (ch1):
> "Descartes donates radical doubt. You take a claim — say, the triage score of 'low-acuity' —
> and you ask: what would have to be true for this claim to be wrong about the patient in front
> of me? Not as a ranking exercise. As a diagnostic."

The payoff (ch1):
> "What makes the Cartesian move powerful is that it produces a checklist."

Example: Knight Capital, Aug 1 2012. Seven servers updated; one did not. "The command returned
success" and "the system is doing what we intend" are different claims. Radical doubt is the
habit of never letting the first stand in for the second.

---

### 2. Hume — The Limit of Induction

Source: `_ch1-what-i-mean-by-skepticism.md`, `_expanded-four-moves.md`

Key sentence (ch1):
> "Hume's move is to remember, every time, that the model's confidence is a property of the
> model and not a property of the world."

Repeated for emphasis:
> "Say that again, because it is the kind of sentence that sounds obvious and is in fact very
> hard to internalize: the model's confidence is a property of the model, not a property of
> the world."

The turkey (Taleb): fed every morning for a thousand days, confidence at all-time high on
day 1000 — the day before Thanksgiving. "The turkey knew the correlation. The turkey did not
know the mechanism."

Real examples: Zillow Offers (~$500M write-down, 2021); Google Flu Trends (over-predicted
in 100/108 weeks Aug 2011–Sep 2013; "big-data hubris").

Hume's tool (expanded):
> "Is this confidence a claim about the world, or only about the record so far — and what
> would tell me the distribution has shifted?"

---

### 3. Popper — Falsifiability

Source: `_ch1-what-i-mean-by-skepticism.md`, `_expanded-four-moves.md`

Key sentence:
> "A claim that cannot be wrong is not yet a claim."

The asymmetry: you can never verify by accumulating examples; one black swan destroys the
"all swans are white" claim. Confirming instances pile up without providing certainty; a
single falsifying instance provides certainty in the other direction.

The consequence for testing (ch1):
> "The project of testing a deployed AI system should not be organized around accumulating
> evidence that it works. It should be organized around trying to find evidence that it fails."

Validation vs. refutation: The Epic Sepsis Model was "widely deployed" — passed every measure
its builders chose. An independent team (Wong et al., JAMA Internal Medicine, 2021) ran the
Popperian test: it missed ~2/3 of sepsis cases, fired alerts on 18% of all patients.
"The accuracy had never been validated in Popper's sense. It had only been unrefuted — because
no one had organized a serious attempt to refute it."

Popper's tool (expanded): "State, in advance and in measurable terms, what would count as this
system failing — then go looking for exactly that."

---

### 4. Plato's Cave — The Artifact–World Distinction

Source: `_expanded-four-moves.md`

The move is three questions:
> "What is the artifact? What is the world? What is the relationship between them?"

The full move (expanded):
> "Plato's tool is the discipline of never grading the shadow as if it were the wall it falls
> on: name the artifact, name the world, and interrogate the relationship between them before
> you act on the output."

From ch1, the cave image:
> "The output of any model is not the world. It is a shadow of the world, cast by a process
> the model's designers chose, on a wall the training data shaped."

And:
> "Fluency is a signal that the system has produced an output the prior distribution liked. It
> is not a signal that the system has gotten the world right."

Example: COVID X-ray models (DeGrave et al., Nature Machine Intelligence, 2021) — the models
"appear accurate but fail when tested in new hospitals." They read laterality markers and
patient positioning, not lungs. The artifact was a confident COVID-positive label; the world
was pathology in lungs; the relationship was wrong.

---

## The Fluency Trap — Exact Quote

Source: `_ch1-what-i-mean-by-skepticism.md`

> "Here is how the fluency trap works. The more fluently an AI presents its output, the more
> confident the user becomes in the output. That part is not surprising. The trap is the second
> move: the more confident the user becomes in the output, the more confident the user becomes
> in their own evaluation of the output. Fluency is an evaluation booster. It boosts the wrong
> evaluations as readily as the right ones. Fluent outputs are not just accepted more — fluency
> itself does the epistemic work that the verification should have done."

And:
> "When you find yourself accepting an output because it sounds right, stop. Ask what would
> have to be true for it to be wrong. Run Descartes's move. Run Popper's. Look at the artifact
> and look at the world and ask what the relationship is."

Mechanism:
> "AI systems have broken this heuristic. An AI can produce clear, precise, organized prose
> about things it has no understanding of. The form is generated by a statistical process that
> learned what well-formed prose looks like. The content is whatever that process produces given
> the input. These are independent. A sentence can be maximally fluent and maximally wrong
> simultaneously, and there is no way to tell from the fluency alone."

---

## The Ash Case — Exact Wording from the Book

Source: `00-introduction.md`

> "In Chapter 1 you will also meet Ash, who gave an AI agent access to his email and asked it
> to delete a sensitive message. The agent reported, confidently and in well-formed prose, that
> the message was deleted and the account secured. It was not. The agent had reset a password
> and renamed an alias; the data sat untouched on the provider's servers. The agent did not lie
> — its report was true about its local actions and false about the world, and its confidence
> was proportional to its blindness."

From `_expanded-four-moves.md`, via the Plato section:
> "Ash's agent produced a report (the artifact); the email sat on the server (the world); the
> relationship was that the report described the local machine and not the server — and Ash
> reviewed the artifact, not the world. Hold those three apart and the failure is obvious;
> collapse them and it is invisible."

From ch1 (fluency trap section):
> "Ash's agent produced a fluent, well-formed report. The email had been deleted. The account
> had been secured. Ash trusted it. The agent did not deceive him — the agent could not have
> deceived a non-fluent reader, because a non-fluent reader would have asked basic questions
> the fluent reader felt no need to ask. The fluency was the trap. The well-formed prose did
> the epistemic work the verification should have done."

---

## The Asymmetry Sentence — Exact Quote

Source: `00-introduction.md`

> "What did not change, and what this book argues cannot change, is who has to doubt those
> outputs. The doubt is still yours. That asymmetry is the whole subject: the machine's speed,
> your doubt."

From ch1 (solve-verify asymmetry section):
> "This is not a complaint. It is an observation about where the costs sit, and where the costs
> are going to sit for the foreseeable future."

And:
> "When an AI system produces an output, producing the output is cheap. The model runs, the
> result appears, the latency is in milliseconds, the cost is fractions of a cent. Verifying
> the output is expensive."

---

## Discrepancy Flag Summary (for Bear)

| File | Claims |
|---|---|
| `_ch1-what-i-mean-by-skepticism.md` | "Three philosophers donate moves to the toolkit" — Descartes, Hume, Popper |
| `_expanded-four-moves.md` | "Four philosophers donate them" — Descartes, Hume, Popper, Plato |

Resolution used in this batch: FOUR moves (Plato included). The expanded file is the fuller
treatment. The "three philosophers" sentence in ch1 should be updated to "four philosophers"
in the next revision.
