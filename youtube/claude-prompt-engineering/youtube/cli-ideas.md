# Claude Prompt Engineering — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Prompt Anatomy Auditor with Claude
- Source: claude-prompt-engineering/chapters/03-anatomy-of-an-effective-prompt.md
- Lane: BUILD (Claude Code)
- Hook: Most prompts fail not because the user doesn't know what they want, but because they've assembled all the right information in a structure Claude can't parse.
- The artifact: A Python CLI that reads any prompt and maps it against the six-component anatomy (Task, Context, Constraints, Output Format, Examples, Evaluation Criteria), scoring each component's presence and specificity. The output is an animated component map showing which slots are filled, which are implied, and which are missing entirely — alongside a specificity score for each filled slot.
- Prompt seed: `claude "Analyze this prompt against the six-component anatomy: Task (what to do), Context (relevant background), Constraints (limits/requirements), Output Format (structure/length/style), Examples (demonstration of desired output), Evaluation Criteria (how to judge quality). For each: present/implied/missing, specificity score 1-5, and one-sentence improvement suggestion." < prompt.txt`
- Read / check: Verify the auditor distinguishes between "implied" (the information is inferable from context) and "missing" (no basis for inference); check that specificity scores are calibrated — a Task slot that says "write a summary" should score lower than one that says "write a 3-sentence executive summary for a non-technical audience."
- Human supplies (Claude can't): A real prompt from their own work to audit. The book's before/after policy brief example is an ideal synthetic stand-in — it's the exact comparison the chapter builds toward.
- Output medium: d3 (animated) — six component bars animate to show fill level (0-100%), colored by specificity score; missing components appear as red empty bars.
- The change: Run the same prompt through two versions — original and improved — and animate the component bars updating to show exactly which components moved and by how much.
- Teardown angle: The anatomy is not a template to fill — it's a diagnostic. A prompt missing the Evaluation Criteria isn't failing because it's incomplete; it's failing because without it, Claude can't know when it's done.
- Exclusions: Full prompt library management, automated prompt optimization, A/B testing infrastructure.
- Score: 9/10

## Candidate 02 — Build a Criteria-First Prompt Generator with Claude
- Source: claude-prompt-engineering/chapters/05-criteria-first-specification.md
- Lane: BUILD (Claude Code)
- Hook: The single highest-leverage change to most prompts is putting the evaluation criteria first — and most people have never tried it.
- The artifact: A Python script that takes a natural-language description of a desired output and produces two prompts: a standard request-first version and a criteria-first version where the evaluation criteria are stated before the task. It then runs both through Claude and presents the outputs side by side for comparison. The terminal shows the prompt generation, both Claude runs, and the diff between outputs.
- Prompt seed: `claude "Rewrite this request as a criteria-first prompt: lead with the evaluation criteria (how to judge the output), then state what to produce. Keep the underlying task identical. The criteria should be specific and testable, not aesthetic ('good' is not a criterion; 'under 100 words' is)." < request.txt`
- Read / check: Verify the criteria in the rewritten prompt are genuinely testable (not "clear" or "engaging" but "under 100 words," "three bullet points," "no hedging language"); confirm the criteria-first prompt produces a meaningfully different output from Claude — this is the video's proof point.
- Human supplies (Claude can't): A real task they've been prompting Claude for with variable results. The book's policy brief example (with the before/after comparison) works as a synthetic stand-in.
- Output medium: screen-recording mp4 — terminal shows both prompt versions side by side, then both Claude outputs appearing with a diff tool highlighting the structural differences.
- The change: Add one more criterion to the criteria-first prompt and show how the output tightens in exactly the dimension the criterion specified — demonstrating that criteria are directly controlling, not just advisory.
- Teardown angle: Criteria-first prompting shifts Claude's attention from "what is this task typically like?" to "what does this specific output need to be?" — it's the difference between generating and targeting.
- Exclusions: Automated prompt optimization systems, multi-model comparison, prompt A/B testing at scale.
- Score: 9/10

## Candidate 03 — Build a Failure Criterion Generator with Claude
- Source: claude-prompt-engineering/chapters/06-what-would-make-this-wrong.md
- Lane: BUILD (Claude Code)
- Hook: "What would make this wrong?" is the most under-used question in prompt engineering — it surfaces constraints you didn't know you had until you try to articulate what bad looks like.
- The artifact: A Python CLI that takes a prompt and uses Claude to generate a failure criterion checklist: a list of specific, testable conditions that would make the output wrong. The checklist is then exported as a review tool. The terminal shows the generation process and the final checklist being applied to a sample output from the same prompt.
- Prompt seed: `claude "Generate a failure criterion checklist for this prompt: what specific, testable conditions would make any output from this prompt wrong, incomplete, or misleading? Format as a numbered checklist where each item is binary (pass/fail) and specific enough to apply without judgment calls. Aim for 8-12 criteria." < prompt.txt`
- Read / check: Verify all criteria are binary and specific — "contains factual errors" is not a criterion (requires judgment); "cites a source that doesn't exist" is a criterion. Check that the checklist covers failure modes the original prompt didn't mention.
- Human supplies (Claude can't): A prompt from their own work to analyze. The book's research brief prompt (the capstone example) is an ideal synthetic stand-in.
- Output medium: Manim — the prompt appears, then failure criteria animate in as a numbered checklist; then a sample output is shown on screen and each criterion lights up green or red as it's checked.
- The change: Take the three most common failure criteria from the generated list and add them as negative constraints directly to the prompt — then show that the rewritten prompt produces outputs that pass those criteria without requiring a separate check.
- Teardown angle: The failure criterion checklist is the prompt's test suite — you can't know if an output is good without knowing what bad looks like, and "what bad looks like" is almost always more specific than you initially think.
- Exclusions: Automated output scoring, failure criterion databases, multi-prompt comparison systems.
- Score: 9/10

## Candidate 04 — Build a 3-Pass Prompt Refinement Demo with Claude
- Source: claude-prompt-engineering/chapters/11-iterative-refinement.md + chapters/12-capstone-spec-and-revision.md
- Lane: BUILD (Claude Code)
- Hook: Most prompt iteration is random — try something, see what happens, try something else. The 3-pass refinement loop replaces that with a structured diagnostic that finds exactly what to fix.
- The artifact: A Python script that implements the 3-pass refinement loop on a single initial prompt: Pass 1 runs the original prompt, Pass 2 applies the diagnostic (identify what failed + target one thing + preserve what worked + verify the fix), and Pass 3 runs the refined prompt. The terminal shows all three outputs side by side with a change log explaining each refinement decision.
- Prompt seed: `claude "Diagnose this prompt-output pair: what specifically failed in the output? Target the single highest-impact change. State what to preserve from the original prompt. Then write the revised prompt." < prompt_and_output.md`
- Read / check: Verify the diagnostic targets a single change rather than rewriting the entire prompt; check that the change log explains the reasoning (not just "made it clearer" but "added word count constraint because the output was 3x longer than needed"); confirm Pass 3 output is measurably better on the targeted dimension.
- Human supplies (Claude can't): An initial prompt and its unsatisfying output. The book's research brief capstone (with its three-pass revision sequence) is an ideal synthetic stand-in — it's the chapter's worked example.
- Output medium: screen-recording mp4 — three terminal panes showing the three passes; a change log appears between Pass 1 and Pass 2 and between Pass 2 and Pass 3, annotating what changed and why.
- The change: Run the same 3-pass loop on a different failure mode (wrong format vs. wrong scope vs. wrong level of detail) to show the diagnostic routes to different fixes depending on the failure.
- Teardown angle: The 3-pass loop is not about prompting better — it's about diagnosing correctly. Most prompt failures aren't fixed by rewriting; they're fixed by identifying the one dimension that was off and adjusting exactly that.
- Exclusions: Automated iterative prompt optimization, multi-model comparison, prompt version control systems.
- Score: 8/10

## Candidate 05 — Build a Self-Critique Prompt Checker with Claude
- Source: claude-prompt-engineering/chapters/09-self-critique-and-revision.md
- Lane: BUILD (Claude Code)
- Hook: Claude is reasonably good at critiquing outputs when given specific criteria — but the critique quality degrades dramatically without structured guidance, and most people use the vague version.
- The artifact: A Python CLI that runs a two-step self-critique loop: first generates an initial output from a prompt, then asks Claude to critique that output against a specific checklist derived from the prompt's evaluation criteria, and finally generates a revised output incorporating the critique. All three stages appear in the terminal with the critique displayed between the two outputs.
- Prompt seed: `claude "Critique this output against these specific criteria: [list from original prompt]. For each criterion: pass/fail with one-sentence evidence. Then list the top 3 changes that would move failing criteria to passing. Do not make changes yet — only critique." < output.md`
- Read / check: Verify the critique uses the specific criteria from the original prompt (not generic quality feedback); check that "fail" verdicts cite specific evidence from the output (not "this section is weak"); confirm the revision addresses the top-3 changes and the revised output passes the criteria that failed.
- Human supplies (Claude can't): A prompt with evaluation criteria plus an initial Claude output to critique. Fully synthetic from any of the book's worked examples.
- Output medium: screen-recording mp4 — three panes: original output, critique with pass/fail cells, revised output; the critique cells animate between the two outputs.
- The change: Run the same loop with a vague self-critique prompt ("how could this be better?") and show the degradation in critique quality — no criteria, no evidence, generic suggestions — to contrast with the structured version.
- Teardown angle: Self-critique is only useful when the critique criteria are as specific as the original task criteria — otherwise you're asking Claude to evaluate against its own taste, which is just more of the same.
- Exclusions: Automated revision pipelines, multi-round critique loops, quality scoring systems.
- Score: 8/10

## Candidate 06 — Build a Constraint Extractor with Claude
- Source: claude-prompt-engineering/chapters/05-criteria-first-specification.md (constraint taxonomy section)
- Lane: BUILD (Claude Code)
- Hook: The five types of constraints in a prompt serve completely different functions — and conflating them is why prompts fail in ways that are hard to diagnose.
- The artifact: A Python CLI that reads a prompt and classifies each constraint into the five types (scope, evidence, uncertainty, privacy, tone), then generates a constraint inventory. Missing constraint types are flagged with an explanation of what failure mode their absence enables. The output is an animated constraint map showing the five types and their population level.
- Prompt seed: `claude "Parse this prompt and classify every constraint into one of five types: scope (what to include/exclude), evidence (what sources to use/avoid), uncertainty (how to handle things you don't know), privacy (what information to protect), tone (register and style). For each constraint, state the type and the failure mode if that constraint were removed. Flag any constraint type with zero entries." < prompt.txt`
- Read / check: Verify the five-type classification is consistent (scope and evidence are commonly confused — scope is "write about X," evidence is "cite only peer-reviewed sources"); check that the failure modes are specific ("without an uncertainty constraint, the model will state speculative claims as fact" rather than "results may be poor").
- Human supplies (Claude can't): A prompt from their own work to analyze. Fully synthetic from any of the book's worked examples.
- Output medium: d3 (animated) — five labeled segments of a constraint wheel fill in as each constraint is classified; empty segments glow red with the failure mode annotation.
- The change: Add one constraint of the missing type to the prompt and re-run — show the constraint wheel completing and the corresponding failure mode disappearing.
- Teardown angle: Constraint types are not interchangeable — a prompt with strong scope and weak uncertainty handling will confidently state things it doesn't know. Knowing which type is missing tells you exactly what failure to expect.
- Exclusions: Automated constraint generation, constraint templates for specific domains, multi-prompt constraint comparison.
- Score: 8/10

## Candidate 07 — Build an Agentic Prompt Handoff Auditor with Claude
- Source: claude-prompt-engineering/chapters/13-agentic-and-multi-step-prompts.md
- Lane: BUILD (Claude Code)
- Hook: Multi-step agentic prompts fail at handoffs — the boundary between what one step produces and what the next step expects is where the chain breaks.
- The artifact: A Python script that reads a multi-step agentic prompt chain and audits each handoff: what does Step N produce? What does Step N+1 expect? Does the output format match the input expectation? The output is an animated flow diagram showing each step's output contract and whether it satisfies the next step's input requirements.
- Prompt seed: `claude "Audit the handoffs in this multi-step agentic prompt chain. For each handoff between Step N and Step N+1: state what Step N's output format is, state what Step N+1 expects as input, and classify the handoff as: compatible, incompatible (will fail), or ambiguous (may fail depending on Claude's interpretation). Flag all incompatible and ambiguous handoffs." < prompt_chain.md`
- Read / check: Verify the auditor catches format mismatches (Step 1 outputs a numbered list; Step 2 expects a JSON array — should be flagged as incompatible); check that "ambiguous" handoffs are genuinely ambiguous, not just underspecified.
- Human supplies (Claude can't): A multi-step agentic prompt chain from their own work. The book's agentic handoff examples (including the approval gate example) work as a synthetic stand-in.
- Output medium: Remotion — a flow diagram where each step appears as a node; handoff arrows animate in and color-code green (compatible), red (incompatible), or yellow (ambiguous); flagged handoffs get annotation cards.
- The change: Fix one incompatible handoff by adding an explicit output format specification to Step N, re-run the audit, show the arrow turning from red to green.
- Teardown angle: Agentic chains are only as reliable as their weakest handoff — and the weakest handoff is never the one you think is obvious, it's the one where format was left to interpretation.
- Exclusions: Full agentic workflow orchestration, automated chain repair, multi-model handoff testing.
- Score: 8/10

## Candidate 08 — Build a Data Prompt GIGO Detector with Claude
- Source: claude-prompt-engineering/chapters/09-self-critique-and-revision.md (data prompts section)
- Lane: BUILD (Claude Code)
- Hook: Data analysis prompts are uniquely vulnerable to GIGO failure — garbage assumptions in, confident-sounding garbage out. The prompt itself rarely signals when this is happening.
- The artifact: A Python CLI that takes a data analysis prompt (with or without sample data) and produces a GIGO risk assessment: what assumptions does the prompt require to be true for the output to be valid? Which of those assumptions are unverified or unverifiable? The output is an animated assumption checklist with a risk score per assumption.
- Prompt seed: `claude "Analyze this data prompt for GIGO risk. List every assumption the prompt requires to be true for the output to be valid. For each assumption: state whether it is (a) verified by the data provided, (b) verifiable but not yet verified, or (c) unverifiable from the data provided. Mark all (c) assumptions as GIGO risks." < data_prompt.md`
- Read / check: Verify the assumption list is comprehensive — it should include data quality assumptions ("assumes no duplicate rows"), distribution assumptions ("assumes a normal distribution"), and scope assumptions ("assumes the sample is representative of the population"); check that the risk classification is calibrated (unverifiable from the data ≠ false, just unknown).
- Human supplies (Claude can't): A data analysis prompt plus sample data (CSV or markdown table). The book's examples using survey data or metrics files work; a 20-row synthetic CSV is acceptable and preferable for the video.
- Output medium: Manim — an assumption list builds up as an animated checklist, with each assumption color-coded (green = verified, yellow = verifiable, red = GIGO risk); a risk score appears at the bottom.
- The change: Add a data validation step before the analysis that verifies the verifiable assumptions — show the yellow items turning green and the risk score dropping.
- Teardown angle: The GIGO detector makes the invisible explicit — the prompt looks like it's asking for analysis, but it's actually asking Claude to make a set of assumptions about the data, and those assumptions are the analysis.
- Exclusions: Full data pipeline validation, automated data cleaning, statistical testing infrastructure.
- Score: 7/10

## Candidate 09 — Build a Prompt Card Library with Claude
- Source: claude-prompt-engineering/chapters/12-capstone-spec-and-revision.md (8-field prompt card section)
- Lane: BUILD (Claude Code)
- Hook: Prompts that work are constantly rewritten from scratch — because there's no standard format for capturing a prompt in a way that makes it retrievable and reusable.
- The artifact: A Python CLI that takes any successful prompt + output pair and extracts it into the 8-field prompt card format (Task, Context, Constraints, Output Format, Examples, Evaluation Criteria, Failure Modes, Version Notes), then writes it to a markdown library. The library is searchable by task type, constraint type, or domain. The terminal shows the extraction and the library entry being created.
- Prompt seed: `claude "Extract this prompt-output pair into an 8-field prompt card: Task (one-sentence statement of what to do), Context (what background is needed), Constraints (all limits and requirements), Output Format (structure/length/style), Examples (if provided), Evaluation Criteria (how to judge quality), Failure Modes (what would make this wrong), Version Notes (what was changed from the previous version, if known). Be specific on every field." < prompt_and_output.md`
- Read / check: Verify the Failure Modes field is populated from the prompt's actual constraints (not generic failure modes); check that the Evaluation Criteria field is testable (not "good quality"); confirm the output card is genuinely reusable — someone who hasn't seen the original prompt could use the card to regenerate a similar prompt.
- Human supplies (Claude can't): A successful prompt + output pair from their own work. Fully synthetic from any of the book's worked examples.
- Output medium: screen-recording mp4 — terminal shows the extraction running, then the 8-field card appearing in a formatted markdown view, then the card being added to a growing library file.
- The change: Extract two similar prompts into cards, then use Claude to merge them into a single canonical prompt card that covers both use cases — show the merge process and the resulting consolidated card.
- Teardown angle: The prompt card is the difference between a prompt that works once and a prompt that's a shared asset — the 8 fields capture everything needed to reuse, adapt, and explain the prompt without re-deriving it.
- Exclusions: Full prompt management platform, team-based prompt sharing, version control for prompts.
- Score: 7/10
