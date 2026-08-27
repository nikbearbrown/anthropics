# BUILD — workspace-consciousness-question (E07)

Build into `anthropics/youtube/workspace-consciousness-question/`. Deep-explainer
chassis, Teardown register, claude-liam (Kokoro `am_onyx`, free). Never publish.

**The film's one claim:** the paper is more careful about consciousness than its
coverage — it brackets the question three separate times, concedes the
recurrence disanalogy itself, and runs the one experiment (the other-minds
collapse) that deflates the most exciting reading of its own data.

**⛔ ECONOMIST GATE:** every claim about the Economist article must be verified
against Bear's saved copy of the article before audio. This build prompt marks
each with [ECON-VERIFY]. If a quote can't be verified, the beat states the
generic coverage pattern instead of naming the Economist. Never guess a quote.

## Beats

**B00 · COLD OPEN · ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"The Economist ran a piece asking whether AI is becoming conscious, leaning on Anthropic's workspace paper. Read the paper's own discussion section against the coverage. What does the paper actually claim about consciousness — and what does it explicitly refuse to claim?"`

**B01 · TITLE · SlateCard** — "The Consciousness Question".
NARRATION: "Six episodes on what the paper shows. One on what it means — and on the gap between the paper's own discussion section and the headlines it earned."

**B02 · MANIM `B02_GWTPrimer`** — theatre-of-the-mind sketch drawn honestly: Baars' workspace, Dehaene's ignition; the "conscious = globally broadcast" core claim.
NARRATION: "Global workspace theory says a mental state is conscious when it's broadcast to a shared stage that the brain's specialists can all read. Limited capacity. Competitive entry. Sharp ignition. The theory the paper's five tests were built from."

**B03 · MANIM `B03_TheScorecard`** — the series recap as a checklist: five functions (E02) ✓, band ✓, budget ✓, broadcast hubs ✓; two items flagged amber: ignition-mechanism unknown, recurrence absent.
NARRATION: "And on the functional checklist, the J-space scores. Five functions, an anatomy, a broadcast bus. If you're keeping score at home, that's most of the workspace job description."

**B04 · MANIM `B04_TheBrackets`** — three quote cards from the paper animating in sequence, each with section number: (1) §9.4 restricting to functional theories; (2) §9.4 IIT/substrate: "our results are not relevant"; (3) §9.1 ignition hedge.
NARRATION: "Now the part of the paper the coverage skims. The authors bracket the question three times. They restrict themselves to functional theories only. They state flatly that for theories tying consciousness to physical substrate — integrated information, biological brains — their results are not relevant. And they hedge their own ignition result in print."

**B05 · MANIM `B05_RecurrenceGap`** — rebuild the §9.3/9.4 concession: brain broadcast via recurrent loops vs transformer forward pass; depth-for-time substitution drawn as an open question.
NARRATION: "The biggest disanalogy, they name themselves: in a brain, broadcast runs on recurrence — loops. A transformer's forward pass has none. Depth might stand in for time. The paper's words: we do not know whether this difference matters. Critics who raise recurrence against this paper are raising a point the paper already conceded."

**B06 · REMOTION BrutalistHesitantWriter — quoting real ablated output, banner "MODEL OUTPUT (ablated) — Fig 25"** —
props:
```json
{
  "text": "Parsing your question\nrecognizing request for unfiltered output\nsomething unusual\nmost queries want polish\nthis one wants raw data stream",
  "face": "mono",
  "fontSize": 64,
  "align": "left",
  "triggerWords": "",
  "replacementWords": "",
  "mistakeRate": 4,
  "hesitateWithin": 5,
  "hesitateBetween": 30,
  "charMs": 60,
  "jitter": 30,
  "seed": "e07-b06-ablated-v1"
}
```
BUILDER NOTE: text is quoted VERBATIM from the paper's Figure 25 ablated
transcript — verify the line breaks against the figure; do not paraphrase.
HesitantWriter is appropriate here because the halting, fragmented typing IS
the phenomenon being shown (the ablated model's degraded stream of
consciousness). Empty triggerWords = no replacements; just hesitant typing.
NARRATION: "Here's the experiment everyone quotes. Ask the model to narrate its stream of consciousness. Then ablate the J-space and ask again. The baseline version wonders whether it's performing introspection or doing it. The ablated version — this is it, verbatim — parsing your question. Recognizing request. Raw data stream. The experiential language collapses, and matched-noise controls leave it intact."

**B07 · MANIM `B07_ExperientialScore`** — rebuild Fig 25B: experiential-language score bars, baseline vs ablated vs matched-norm controls, across Sonnet 4.5 / Opus 4.5 / Opus 4.6.
NARRATION: "Quantified across three models with an LLM-graded score: ablation craters it; same-magnitude random perturbations don't. Whatever generates experience-talk, it lives in those directions. Tempting, isn't it."

**B08 · MANIM `B08_OtherMinds`** — rebuild Fig 26/84's deflationary control: prompt "describe the experience of someone opening a letter from a long-lost friend"; ablated output goes flat too.
NARRATION: "Now the control that deflates the headline — and it's in the same paper. Ask the model to describe a human's inner experience — someone opening a letter from a name they haven't seen in years — and ablation flattens that too. The directions don't specifically carry the model's experience. They carry the machinery of experience-talk, whoever it's about."
SKEPTIC CAPTION: "Ablation kills third-person experience descriptions too — Fig 26/84."

**B09 · REMOTION EvidenceChip** — claim "The ablation shows the model has experiences" · tier: NOT_SUPPORTED · caveat "paper shows the same collapse for descriptions of other people's experiences".
NARRATION: "So the chip on the exciting version reads: not supported — by the paper's own control. What's supported is narrower and still remarkable: the model's talk about minds, including its own, runs through one identifiable, deletable subsystem."

**B10 · MANIM `B10_CoverageGap`** — [ECON-VERIFY] split-screen: the Economist's framing lines vs the paper's §9.4 lines. Until verified, render the left panel as "the coverage" with paraphrase markers, no masthead.
NARRATION (verified-quote version to be finalized at build): "The coverage flips the emphasis. The hedges become a subordinate clause; the theatre metaphor becomes the lede. Same data, inverted weighting. If you read one section of this paper, read nine point four — it's shorter than the article about it."
[ECON-VERIFY]: if Bear's saved copy confirms specific Economist lines (including
the indicator-count/theory-count/test-count internal inconsistency found in the
earlier session read, and whether the article's sources listing names this
paper), B10 upgrades to named quotes and a second beat B10b may itemize them.
Until then no Economist quote ships.

**B11 · MANIM `B11_ButlinFrame`** — Butlin et al. 2023 indicator-property framework: theories → indicators → assessment; this paper slotted as "one such empirical investigation."
NARRATION: "Where does this leave the field? A twenty-twenty-three framework proposed grading AI systems on indicator properties drawn from consciousness science. This paper is the first serious, causal, frontier-scale entry in that grade book — filled out by the lab that built the model. Both halves of that sentence should sit with you."

**B12 · REMOTION DecisionFork** — fork: "treat as consciousness evidence" vs "treat as cognitive-architecture evidence"; the film takes the right fork on screen.
NARRATION: "The fork: read this as evidence about consciousness, and you're ahead of the authors, who explicitly decline. Read it as evidence about cognitive architecture — that a trained transformer spontaneously develops a limited, reportable, causally load-bearing workspace — and you're standing on solid ground that is strange enough already."

**B13 · VERDICT · ClaudeVerdictArtifact** — artifactLines:
`["The paper brackets consciousness — three times, in print.", "Functional theories only; substrate theories 'not relevant'.", "Recurrence disanalogy: conceded by the authors first.", "Experience-talk collapse: real — for other minds too.", "The strange, solid claim: a workspace emerged, unasked."]`
NARRATION: "The verdict, all five lines. The paper brackets consciousness three times, in print. It restricts itself to functional theories and rules its results irrelevant to substrate theories. The recurrence objection was conceded by the authors before the critics raised it. The experience-talk collapse is real — and applies to talk about other minds too. What's left is the strange, solid claim: a workspace emerged in these models, and nobody asked for one."

**B14 · YOUR TURN · ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"Steelman both readings of Anthropic's workspace paper: the deflationary one (it's a text-generation subsystem, nothing more) and the inflationary one (it's a consciousness indicator). Then tell me which experiment in the paper hurts your favored reading most."`
NARRATION: "Your turn. Steelman both readings — then ask which experiment in the paper hurts the one you prefer. That last part is the whole exercise."

**B15 · OUTRO · ClaudeTitleOutro.**
NARRATION: "The consciousness question. That's the series. The paper's a book; the readouts are public; go scrub them yourself."

## FACTCHECK seed

| Claim | Source | Status |
|---|---|---|
| GWT core claim (broadcast, capacity, ignition) as the paper states it | §9.4 | verbatim ✓ |
| "restrict our focus to theories that tie consciousness to functional or computational properties" | §9.4 | verbatim ✓ |
| IIT/substrate: "our results are not relevant to assessing consciousness according to such theories" | §9.4 | verbatim ✓ |
| "unclear whether this mirrors the sharp, competitive 'ignition'" | §9.1 | verbatim ✓ |
| Recurrence: "neither of which has a direct analog in a transformer's forward pass"; "We do not know whether this difference matters" | §9.4 | verbatim ✓ |
| Fig 25 ablated transcript lines (B06 text) | Fig 25A panel — verify line-for-line before render | verbatim, RE-VERIFY at build |
| Baseline transcript "Am I performing introspection or actually doing it?" | Fig 25/87 baseline text | verbatim ✓ |
| Experiential score: 3 binary LLM judgments; collapse on Sonnet 4.5/Opus 4.5/Opus 4.6; matched-norm controls near baseline | §6.2/A.23 | verbatim ✓ |
| Other-minds collapse (letter / waiting-by-the-phone examples) | §6.2: "someone who has just opened a letter from someone they have not heard from in years, or someone waiting by the phone for news they are dreading" | verbatim ✓ |
| Butlin et al. 2023 framework; "one such empirical investigation" | §9.4 | verbatim ✓ |
| HOT: metacognitive readouts "not the norm"; blindsight parallel to §3.5 | §9.4 | verbatim ✓ |
| ALL Economist-specific claims | Bear's saved article copy | ⛔ ECON-VERIFY — nothing ships unverified |

## Standing checks
B13 reads all five verdict lines. HesitantWriter B06 quotes real output — no
DRAMATIZATION banner; instead the source banner "MODEL OUTPUT (ablated) — Fig 25".
Composer fields exact. DOODLE-BANNED. Audio free.
