# SHOW-DON'T-TELL Audit — claude-liam-vox-two-gate-bell-pair

**Date:** 2026-07-25
**Palette:** claude

| Beat | Narration (gist) | Classification | Reason |
|---|---|---|---|
| B01 | This is Liam, in for Bear. Start with two ordinary zero | EXEMPT | remotion:ClaudeComposerAsk |
| B02 | The input is zero-zero. Each qubit has its own pure sta | TELLS | static display while narration implies motion |
| B03 | Hadamard sends the control from zero to plus: zero plus | SHOWS | multi-step animation (2 play calls) |
| B04 | After H, the joint state is zero-zero plus one-zero ove | TELLS | motion=compare but no animation (only FadeIn/static) |
| B05 | Now controlled-NOT flips the target only on the branch  | TELLS | static display while narration implies motion |
| B06 | The output is phi plus: zero-zero plus one-one over roo | TELLS | static display while narration implies motion |
| B07 | Measure both in the computational basis and the outcome | TELLS | motion=compare but no animation (only FadeIn/static) |
| B08 | Yet each qubit alone is maximally mixed. Its reduced Bl | TELLS | static display while narration implies motion |
| B09 | The information did not vanish. It moved into correlati | TELLS | static display while narration implies motion |
| B10 | Order matters. CNOT on zero-zero does nothing; applying | TELLS | motion=compare but no animation (only FadeIn/static) |
| B11 | Your turn. After Hadamard but before CNOT, are the qubi | EXEMPT | remotion:ClaudeComposerAsk |
| B12 | Two gates tie the quantum knot: H creates branches, and | TELLS | static display while narration implies motion |

**SHOWS:** 1  **TELLS:** 9  **EXEMPT:** 2

## Rebuilt TELLS

- **B02** REBUILT: The input is zero-zero. Each qubit has its own pure state, a
- **B04** REBUILT: After H, the joint state is zero-zero plus one-zero over roo
- **B05** REBUILT: Now controlled-NOT flips the target only on the branch where
- **B06** REBUILT: The output is phi plus: zero-zero plus one-one over root two
- **B07** REBUILT: Measure both in the computational basis and the outcomes mat
- **B08** REBUILT: Yet each qubit alone is maximally mixed. Its reduced Bloch v
- **B09** REBUILT: The information did not vanish. It moved into correlations: 
- **B10** REBUILT: Order matters. CNOT on zero-zero does nothing; applying H af
- **B12** REBUILT: Two gates tie the quantum knot: H creates branches, and CNOT