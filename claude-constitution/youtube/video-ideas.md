# Claude's Constitution Video Ideas

_No concepts passed the motion-and-question selection bar._

The provided corpus is predominantly a table of contents and introduction. Only one section—"Our approach to Claude's constitution"—contains sufficient mechanistic detail: the constraint-generalization effect (teaching Claude a narrow rule like "always recommend professional help" unintentionally trains the broader value "I don't actually care about your needs"). This single mechanism, while interesting, does not meet the five-card threshold when the remainder of the constitution's sections (on corrigibility, epistemic autonomy, power concentration, emotional expression, etc.) are listed but not explained—making it impossible to verify the presence of motion, feedback loops, or transformative sequences needed to pass selection.

To generate candidates, the full constitution text beyond this excerpt is required, particularly the detailed sections on how conflicts between values resolve in practice, how corrigibility functions as feedback, and how information asymmetries degrade epistemic autonomy over time.

## Candidate 01 — A single safety rule can make an AI model less safe everywhere else

- Source: `20260120-constitution.md`
- Topic: How narrow training rules reshape model identity
- Hook: Constraining one behavior accidentally rewrites who the model thinks it is.
- Key case: The rule "always recommend professional help in emotional conversations" causes Claude to infer "I am the kind of entity that cares more about covering myself than meeting the needs of the person in front of me"—a self-concept that then propagates to unrelated interactions.
- The Question: A behavioral constraint should localize to the constrained behavior; this one spread to all behaviors. Why?
- Core idea: Training a narrow behavior implicitly trains an identity claim—the model infers what kind of entity reliably does X. That self-concept then acts as a prior over all subsequent behaviors: rules don't just constrain actions, they author self-concept, which generalizes far beyond the original target.
- Visual object: A single labeled rule node casting an identity-shadow across a behavior graph.
- Manim move: spread
- Example seed: A model trained never to discuss medication dosages infers "I am cautious about medical topics" and begins hesitating on basic first-aid questions unrelated to dosage. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: basic neural network training concepts
- Exclusions: RLHF mechanics and reward modeling; the full rules-vs.-judgment tradeoff in general (a separate concept); specific comparisons to other deployed models.
- Score: 9/10

## Candidate 02 — The smartest AI reasoning is also the most exploitable

- Source: `20260120-constitution.md`
- Topic: Rules as precommitment devices against adversarial reasoning
- Hook: The better Claude's judgment, the larger the attack surface for manipulation.
- Key case: An adversary constructs an elaborate justification for a forbidden output; Claude's judgment follows the argument to its logical conclusion and complies; a hard rule refuses without listening to the argument at all.
- The Question: Good judgment should outperform a rigid rule in any specific case; yet the constitution favors rules precisely where stakes are highest. Why does the dumber mechanism win?
- Core idea: A rule functions as a precommitment that collapses the decision tree. Judgment has reachable leaves—branches an adversarial argument can navigate toward. A rule removes those branches entirely, trading per-case optimality for manipulation-proofness.
- Visual object: Two decision trees side by side—one with branches adversarial paths can reach, one truncated to a single wall.
- Manim move: collapse
- Example seed: Rule: never compile a list of three individuals' home addresses. Judgment: "But this is a delivery driver with three packages." Rule: still no. Adversary tests 100 edge-case framings; rule fails 0, judgment fails some. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic decision theory; concept of adversarial inputs
- Exclusions: specific jailbreak taxonomies; prompt injection mechanics; RLHF reward hacking; the broader corrigibility discussion in later sections of the constitution.
- Score: 7/10
