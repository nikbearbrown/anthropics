# When Claude Code Wins

*You asked for a folder on why to use Cowork. This file is the other half, and it is longer than the pitch on purpose. A comparison that only argues one direction is not a comparison.*

---

## 1. When the work must be reproducible

This is the strongest argument and it is not close.

Claude Code leaves artifacts on your disk that outlive the session: a script, a commit, a diff, a log. Someone else can rerun it. *You* can rerun it in six months and get the same thing.

A Cowork session produces the output but the *procedure* is comparatively ephemeral — it lives in a conversation, not in a file you can execute.

There is a worked example of exactly this cost in this tree. In the two-book fact-check ([`04-case-study-factcheck.md`](04-case-study-factcheck.md)), Codex produced a ~217-line Python generator that ran the whole pass in about fifteen minutes and can be run again tomorrow. The Cowork pass produced better, more granular, reader-visible output — per-claim URLs, verdicts, a master report — and the generator script **did not survive**, because it lived in the session rather than the repo.

Better output, worse reproducibility. That is the trade in one sentence.

> **If the task will run more than twice, you want the script, and the script is Claude Code's native output.**

## 2. When your prose already has a test suite

The argument for Cowork assumes documents lack machine-checkable correctness. Sometimes false — and specifically false in this tree, which has narration linting, figure-overflow checks, citation and fact-check sidecars, render gates, and build scripts.

Once a manuscript has a pipeline that returns pass/fail, it *is* a codebase. And Claude Code's loop — change, run the check, read the failure, fix, repeat — is precisely the loop that pipeline rewards. Handing that to a surface with no terminal means giving up the check.

## 3. When the job is git

Branches, bisects, rebases, conflict resolution, history archaeology, "what changed between rev X and rev Y." Claude Code lives in git. Cowork does not.

This tree has a live example: the `/agents` visualizer whose corpus connections were corrupted, with the clean topology sitting at `74bdcdca~1`. Recovering that is a git operation. There is no document-shaped version of it.

## 4. When you need the machine itself

ffmpeg. Manim renders. A dev server you need to hit. A launchd agent. Homebrew. A GPU. Anything where the work *is* the local environment.

The entire film-loop apparatus in this tree is this case. Cowork's sandbox is isolated from your computer by design — which means it is isolated from your renderer, your fonts, your codecs, and your 27GB of assets.

## 5. When the data cannot leave the building

Cowork runs on Anthropic's servers. That is a compliance fact, not a preference.

For student records, unpublished peer review, IRB-scoped data, or anything under an NDA, the question "does this leave my machine" has an institutional answer, and you do not get to decide it by yourself on a Tuesday. Claude Code running locally is sometimes the *only* compliant option.

## 6. When you are iterating in seconds, not minutes

Tight loops — tweak a value, rerun, look — are faster in a terminal than in an agentic session that plans, decomposes, and delegates. Agentic overhead is real and it is worth paying only when the task is big enough to amortize it.

Related: Cowork consumes usage faster than standard chat. Using an agentic loop for a thirty-second job is the expensive way to do a cheap thing.

## 7. When you need hooks, or deterministic enforcement

If the requirement is "*every time* X happens, Y must run" — a lint on save, a gate before commit, a check that cannot be skipped by a distracted human — that is harness configuration, and it is a Claude Code capability. Enforcement that depends on the model remembering to be careful is not enforcement.

---

## The meta-point for the book

Notice that arguments 1, 2, 4, and 7 are all the same argument in different clothes:

> **Claude Code wins when the work has a machine-checkable definition of done.**

And the Cowork case is its mirror:

> **Cowork wins when done is a judgment a human makes by reading, and the bottleneck is producing the thing to read.**

That is the actual axis. Not technical-vs-nontechnical. Not hard-vs-easy. **Verifiable-vs-judged.**

Which also predicts the failure modes. People misuse Cowork when they let a judged workflow substitute for a checkable one — accepting a plausible-looking deliverable because no test said otherwise. People misuse Claude Code when they let a green test suite stand in for a judgment nobody made — shipping something that compiles and is wrong.

---

*Continue to [`03-decision-guide.md`](03-decision-guide.md) for the picker.*
