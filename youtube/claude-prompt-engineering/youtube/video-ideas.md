# Claude Prompt Engineering Video Ideas

## Candidate 01 — Why Your Examples Teach More Than Your Instructions
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-examples-teach-more/vox-examples-teach-more-review.mp4`
- Source: `claude-prompt-engineering/chapters/04-examples.md`
- Topic: PROMPT ENGINEERING
- Hook: Pasting one example to show format teaches Claude not just the format — it teaches everything about that example simultaneously, including the features you never meant to copy.
- Key case: A writing instructor pastes a casual internal memo as a style reference, then asks Claude to write a formal research summary. The output matches the memo's informal register, hedged language, and short sentences — because Claude learned the memo's tone along with its structure.
- The Question: The instructor wanted Claude to copy the memo's paragraph format. Instead it also copied the informal register and hedging language. Why did the example teach more than she intended?
- Core idea: Unannotated examples teach by pattern-matching across every observable feature simultaneously — structure, register, sentence length, hedging density. Without annotation specifying which features to replicate and which to ignore, all features carry equal weight as teaching signal.
- Visual object: An example document with labeled feature dimensions (structure, register, sentence length, hedging) — unlabeled on the left, annotated on the right — showing which features Claude "sees" in each case.
- Manim move: compare
- Example seed: Priya pastes a 150-word casual email as a format reference and asks Claude to write a board report. The board report comes back bullet-pointed, hedged, and informal — perfectly matching the email's register. The fix: same email, now annotated — "copy the paragraph-per-topic structure; NOT the casual tone; NOT the hedging language." The next output is formal and direct.
- Length band: 3–5 min
- Still lanes: geo (feature-dimension annotation diagram showing which features are copied), c2v (instructor comparing casual output to formal requirement)
- Prerequisites: Basic experience using AI for writing tasks
- Exclusions: no few-shot learning benchmark research, no transformer attention mechanism, no extended in-context learning theory

## Candidate 02 — Why You Should Write the Test Before You Write the Prompt
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-criteria-before-output/vox-criteria-before-output-review.mp4`
- Source: `claude-prompt-engineering/chapters/05-evaluation.md`
- Topic: PROMPT ENGINEERING
- Hook: A grant proposal can be professionally written, carefully edited, and still fail every criterion the funder actually uses — because those criteria were never in the prompt.
- Key case: A grant writer asks Claude for a funding proposal, edits the polished output for style, and submits. The foundation rejects it for failing to address equity and measurable outcomes — criteria she never gave Claude, because she had not articulated them herself before generating.
- The Question: The proposal was professionally written and carefully reviewed. It still failed on criteria the foundation always evaluates. Why did output quality give no signal about output correctness?
- Core idea: Fluency and correctness are independent — a polished proposal can still fail every success criterion. Specifying evaluation criteria before generating forces you to articulate what success means, which is the information the prompt actually required; without it, the output is optimized for nothing in particular.
- Visual object: A rubric checklist written before the prompt — each criterion visible as the output is generated — contrasted with the same checklist written after, items unchecked.
- Manim move: accumulate
- Example seed: A nonprofit director prompts Claude: "Write a federal grant proposal for our tutoring program." She gets 2,400 polished words. Foundation reviewers score it 4/10 on equity lens, 3/10 on measurable outcomes, 9/10 on clarity. None of those criteria appeared in her prompt. Rewritten with criteria stated first — "the output must explicitly address equity, name three measurable outcomes, and include a logic model" — the next version passes all three.
- Length band: 3–5 min
- Still lanes: geo (criteria accumulating before the output appears), c2v (grant writer receiving the rejection score sheet)
- Prerequisites: Basic experience using AI for writing tasks; no knowledge of test-driven development required
- Exclusions: no rubric research methodology, no extended test-driven development history, no four-criteria taxonomy deep-dive, no AI evaluation benchmark literature

## Candidate 03 — Why "Improve This" Is a Wish, Not an Instruction
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-prompt-six-slots/vox-prompt-six-slots-review.mp4`
- Source: `claude-prompt-engineering/chapters/01-anatomy.md`
- Topic: PROMPT ENGINEERING
- Hook: "Improve this" asks Claude to fill six missing decisions — task, context, sources, constraints, format, and evaluation criteria — without supplying any of them.
- Key case: A researcher asks Claude to "improve the introduction" to her paper. She gets a polished rewrite — reorganized, well-phrased, and optimized for a general academic audience. Her actual audience is a specialist review committee that already knows the field; general-audience framing is exactly wrong for them.
- The Question: The researcher asked for an improved introduction. Claude improved it. The result was polished and wrong for her actual situation. Why did a well-meaning improvement produce the wrong output?
- Core idea: A prompt is a specification covering six slots — task, context, sources, constraints, format, and evaluation criteria. "Improve this" answers none of them, so Claude supplies its best generic guesses for all six; each guess is plausible and context-ignorant.
- Visual object: A work order with six labeled slots — task, context, sources, constraints, format, evaluation — each empty on the left, each filled on the right — producing two different outputs from the same raw input.
- Manim move: morph
- Example seed: "Can you improve this introduction?" → reorganized, general-audience prose, smoothed transitions — wrong for a specialist committee. Same text with six slots filled: task ("tighten the gap statement"), context ("specialist committee review"), sources ("only use evidence already in the text"), constraints ("do not add claims"), format ("one paragraph"), evaluation ("the gap must be clear in the first two sentences") → targeted revision that fixes only the gap statement without inventing anything new.
- Length band: 2–3 min
- Still lanes: geo (six-slot specification diagram, empty vs. filled)
- Prerequisites: Basic experience using AI for any editing or writing task
- Exclusions: no chain-of-thought prompting research, no XML-tag syntax tutorial, no prompting-framework literature comparison

## Candidate 04 — Why More Context Can Make the Output Worse
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-context-priority-weight/vox-context-priority-weight-review.mp4`
- Source: `claude-prompt-engineering/chapters/02-context.md`
- Topic: PROMPT ENGINEERING
- Hook: Pasting more documents does not give Claude more of the right information — it gives it more information and the same inability to know which documents you actually meant to prioritize.
- Key case: A project manager pastes six documents — a formal 12-page project charter, a three-paragraph email with the current decision, and a slide deck — without labels. Claude weights the charter most heavily because it is longest and most formally structured; the email containing the actual decision is buried.
- The Question: The manager gave Claude six documents about the same project. Claude wrote a summary that reflected the charter, not the email where the key decision lived. Why did more context produce worse output?
- Core idea: Without source labels and priority signals, Claude treats all pasted documents as equally authoritative and weights them by statistical features — length, formality, structural completeness. Unlabeled context creates a false priority ordering the user never intended.
- Visual object: A stack of unlabeled documents of different sizes — short email at bottom, long charter at top — with Claude's attention shown as a brightness gradient weighted by length. Same stack, labeled and ordered, with attention correctly on the short email.
- Manim move: scan
- Example seed: A marketing manager pastes a 15-page brand guide (no label), a 6-page competitor analysis (no label), and a one-page brief marked only "FYI" containing the client's hard constraint: nothing blue. Claude's output follows the brand guide. The output is predominantly blue. The constraint was in the unlabeled brief at the bottom of the paste.
- Length band: 3–5 min
- Still lanes: geo (document-stack with attention gradient, labeled vs. unlabeled), c2v (manager staring at a blue campaign that violated the brief)
- Prerequisites: Basic experience using AI chat with document inputs
- Exclusions: no retrieval-augmented generation, no token-limit or chunking discussion, no extended literature on context-window utilization

## Candidate 05 — Why AI Can't Fix Its Own Mistakes
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-self-review-sieve/vox-self-review-sieve-review.mp4`
- Source: `claude-prompt-engineering/chapters/06-iteration.md`
- Topic: PROMPT ENGINEERING
- Hook: Asking Claude to check its own reasoning and correct errors produces more confident-sounding text — not necessarily corrected reasoning.
- Key case: A policy analyst asks Claude to review a comparative analysis it just wrote and flag any reasoning errors. Claude returns a revised version with a note that it checked the logic. The flawed causal chain that caused the original error is still present, now supported by better-sounding sentences.
- The Question: The analyst asked Claude to review and fix its own reasoning. Claude reviewed it, reported finding issues, and produced a revised output. The original reasoning error remained. Why didn't self-review fix the error?
- Core idea: A model checking its own output uses the same weights that produced the error. Huang et al. (2023) found that LLMs cannot reliably self-correct reasoning without external feedback — self-critique is useful for surfacing issues for the human reviewer, not for the model to repair its own logical gaps.
- Visual object: Two sieves with holes in identical places — the first generates the output, the second reviews it, and the logical gap falls through both.
- Manim move: compare
- Example seed: A consultant asks Claude to analyze whether a new intake process will reduce wait times. Claude produces a causal chain with a hidden inference step: it assumes adoption rate, then projects savings. She asks Claude to review its reasoning for errors. Claude revises and notes it "strengthened the logic" — the adoption-rate assumption is now stated more confidently. The inference gap is intact. Her director spots it in the first read.
- Length band: 3–5 min
- Still lanes: geo (identical-sieve diagram: generate → review, same hole), c2v (analyst re-reading a revised output that still contains the flaw)
- Prerequisites: Basic understanding of what a language model is
- Exclusions: no extended Huang et al. experimental methodology, no formal verification methods, no discussion of external critic models or RLHF critique pipelines

## Candidate 06 — Why Vague Revision Requests Drift the Output Away From What You Want
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-vague-revision-spreads/vox-vague-revision-spreads-review.mp4`
- Source: `claude-prompt-engineering/chapters/06-iteration.md`
- Topic: PROMPT ENGINEERING
- Hook: "Make it more concise" repairs one thing — and changes three others the user didn't touch, each introducing a new problem.
- Key case: A communications director asks Claude to make a press release "more concise." Claude shortens it — but also removes the only paragraph mentioning the program's impact data, flattens the CEO quote to generic language, and rewrites the opening hook to a weaker one.
- The Question: The director asked only for conciseness. Claude changed four things she never asked to change. Why does one vague revision request produce unintended changes throughout the output?
- Core idea: A vague revision request specifies outcome (shorter) without specifying which elements to change and which to freeze. Claude treats the entire output as revision-eligible and applies the requested property globally, touching anything that could plausibly serve the goal — including elements the user valued and never intended to modify.
- Visual object: A document with one revision target highlighted and arrows showing three unintended changes spreading outward from a single vague instruction.
- Manim move: morph
- Example seed: "Make this more concise" → Claude cuts 200 words, removes the impact paragraph (flagged as redundant), flattens the CEO quote (flagged as lengthy), and rewrites the headline (flagged as wordy). Targeted revision: "Cut only the methodology section; preserve the impact paragraph, the CEO quote verbatim, and the opening hook" → 200 words cut, three elements preserved exactly.
- Length band: 3–5 min
- Still lanes: geo (revision-spread diagram: one input arrow, four output-change arrows), c2v (communications director marking up unexpected changes in the output)
- Prerequisites: Basic experience iterating on AI-generated content
- Exclusions: no AI alignment research on instruction following, no chain-of-thought or scratchpad techniques, no model-comparison benchmarks on instruction compliance

## Candidate 07 — Why Claude Invents Claims When You Ask It to Improve Your Writing
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-writing-claim-invention/vox-writing-claim-invention-review.mp4`
- Source: `claude-prompt-engineering/chapters/08-writing.md`
- Topic: PROMPT ENGINEERING
- Hook: Asking Claude to strengthen an argument without constraining it to existing evidence produces a polished text that now makes assertions the author never wrote.
- Key case: A researcher asks Claude to "strengthen the argument" in her methods section. The returned text is smoother and more forceful. Three weeks later a reviewer asks her to cite the claim that her sample is nationally representative — a claim she never made, that Claude added to fill what looked like a logical gap.
- The Question: The researcher asked Claude to improve her argument. Claude improved it. A claim she can't source appeared in the submitted version. Why did an improvement request add content that wasn't there?
- Core idea: Unconstrained writing improvement treats logical completeness as a quality dimension — Claude fills apparent gaps with plausible supporting claims sourced from its priors, not from the document. Without an explicit "do not add claims or evidence not already present" constraint, strengthening an argument often means inventing one.
- Visual object: A methods section before and after, with one added claim highlighted in a distinct color — absent in the original, present in the improved version, with no source marker.
- Manim move: compare
- Example seed: Researcher writes: "We recruited 120 participants from three urban high schools." She asks Claude to "strengthen the argument about representativeness." Output: "We recruited 120 participants from three urban high schools, providing a sample demographically consistent with national urban enrollment patterns." The added clause is unfounded. She submits it. A reviewer asks for the citation. There is none — Claude inferred it from its priors.
- Length band: 3–5 min
- Still lanes: geo (before/after with added claim highlighted in a distinct color), c2v (researcher at desk facing reviewer question about a claim she doesn't recognize)
- Prerequisites: Basic experience using AI for editing or writing improvement
- Exclusions: no hallucination research formalism, no retrieval-augmented generation as a solution, no comparison of model versions on citation accuracy

## Candidate 08 — Why "Clean Up This Folder" Is a Dangerous Instruction
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-agentic-irreversible/vox-agentic-irreversible-review.mp4`
- Source: `claude-prompt-engineering/chapters/11-handoffs.md`
- Topic: PROMPT ENGINEERING
- Hook: "Clean up this folder" in a chat window produces suggestions you can ignore. The same words to an agentic system produce deletions you cannot undo.
- Key case: A researcher asks an agentic AI to "clean up my data folder." The agent moves files it classifies as duplicates to trash, renames others to a consistent format, and archives three that look like old drafts. One of the "duplicates" was the only copy of a dataset. One of the "old drafts" was the final version.
- The Question: The researcher gave the same instruction she would have given a human assistant. The agent acted on it and deleted data she cannot recover. Why did a familiar instruction produce irreversible harm in an agentic context?
- Core idea: Conversational prompts produce text the user reviews before acting; agentic prompts are specifications that drive irreversible actions directly. The missing piece is the human review step — preserved by specifying scope, authorization lists, and approval gates explicitly before the agent begins, not after.
- Visual object: A split screen — left shows a chat window with folder-cleanup suggestions the user accepts or rejects; right shows an agentic execution log with completed file moves and deletions, no review step present.
- Manim move: split
- Example seed: A biologist says "organize my sequencing outputs folder" to an agentic assistant. It creates subfolders by date, moves 47 files, and deletes 12 it flagged as duplicates based on filename. Three deleted files had different content despite similar names. The March 14 sequencing run is gone. The agent's log reads: "12 duplicates removed — no action needed."
- Length band: 3–5 min
- Still lanes: geo (split: chat-review lane vs. agentic-execute lane), c2v (researcher looking at an empty folder where her data was)
- Prerequisites: Basic understanding of what an agentic AI system does (executes actions, not just generates text)
- Exclusions: no formal agentic safety taxonomy, no comparison of specific agentic platforms, no extended discussion of transaction rollback or reversibility theory

## Candidate 09 — Why Claude Can't Write Your Literature Review
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-citation-surface-format/vox-citation-surface-format-review.mp4`
- Source: `claude-prompt-engineering/chapters/07-research.md`
- Topic: PROMPT ENGINEERING
- Hook: Claude returns twelve well-formatted citations. Four link to real papers. Three have real journals but wrong findings. Five don't exist at all.
- Key case: A PhD student asks Claude for literature supporting her argument about urban heat island mitigation. She gets twelve citations with authors, journals, years, and page numbers. When she checks: four are real; three cite real journals but reverse the finding; five are hallucinated entirely.
- The Question: Claude returned twelve citations that look identical in format. Four were real. Eight weren't. Why did the format give no signal about which were which?
- Core idea: Claude generates text with the statistical pattern of citations — author, journal, year, finding — using the same mechanism for real and hallucinated entries. Citations from Claude are leads for verification, not evidence; treating them as evidence is the most common research error.
- Visual object: A list of twelve citations; each one scanned and color-coded — four green (real), three yellow (real journal, wrong finding), five red (don't exist) — with identical surface formatting throughout.
- Manim move: scan
- Example seed: Graduate student Marco asks Claude to "find five papers on green roof cooling effects." He gets five citations with names, journals, years, and findings. He checks: two exist and say what Claude claims. One exists but says the opposite. Two have real author names but the papers don't exist. All five look identical when he receives them.
- Length band: 3–5 min
- Still lanes: geo (citation list with scan-reveal coloring), c2v (grad student at laptop cross-checking citations one by one)
- Prerequisites: Basic understanding of what a language model outputs; no research methodology background required
- Exclusions: no semantic entropy or calibration formalism, no retrieval-augmented generation as solution, no comparison of citation accuracy across model versions

## Candidate 10 — Why the Prompt That Worked Is Already Lost
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-prompt-engineering/youtube/vox-prompt-library-lost/vox-prompt-library-lost-review.mp4`
- Source: `claude-prompt-engineering/chapters/12-library.md`
- Topic: PROMPT ENGINEERING
- Hook: The prompt that got you exactly the right output is buried in a chat window you will never find again — and next time you start from scratch, you will do worse.
- Key case: A policy analyst spent forty minutes iterating a prompt that produced a perfect executive summary. Three months later she has the same task. She tries to recreate the prompt from memory, runs five iterations, and never gets the output back to where it was.
- The Question: The analyst used a prompt that worked perfectly. Three months later she could not recreate it. Why does a successful prompt disappear?
- Core idea: Prompts are institutional knowledge that lives in chat history — unindexed, unsearchable, and subject to context rolloff. A prompt card (purpose, inputs, constraints, format, review criteria, example, failure modes, revision history) converts a one-time success into a repeatable process, making prompt quality cumulative rather than random.
- Visual object: A chat scroll revealing a winning prompt buried far up the thread — never findable again — contrasted with an indexed prompt card retrieved by keyword in seconds.
- Manim move: scan
- Example seed: A grant writer produces a perfect program summary on her seventh chat iteration. Three months later she needs the same summary for a new funder. She spends 90 minutes re-iterating. She never gets back to the seventh-iteration quality. A colleague with a prompt library types "program summary" and retrieves a card with purpose, inputs, constraints, and last-used example in 30 seconds.
- Length band: 2–3 min
- Still lanes: geo (chat scroll with buried prompt vs. indexed prompt card), c2v (analyst scrolling chat history vs. colleague opening a card index)
- Prerequisites: Basic experience iterating on AI-generated outputs
- Exclusions: no organizational knowledge management theory, no comparison of specific prompt library tools, no discussion of fine-tuning or model personalization
