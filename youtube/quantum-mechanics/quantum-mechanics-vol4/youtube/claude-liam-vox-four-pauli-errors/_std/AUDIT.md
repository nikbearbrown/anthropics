# SHOW-DON'T-TELL Audit — claude-liam-vox-four-pauli-errors

**Date:** 2026-07-25
**Palette:** claude

| Beat | Narration (gist) | Classification | Reason |
|---|---|---|---|
| B01 | This is Liam, in for Bear. A qubit can suffer infinitel | EXEMPT | remotion:ClaudeComposerAsk |
| B02 | I does nothing. X flips zero and one. Z changes their r | TELLS | static display while narration implies motion |
| B03 | Together I, X, Y, and Z are linearly independent and sp | SHOWS | multi-step animation (2 play calls) |
| B04 | For example, a small rotation about a tilted axis looks | SHOWS | has transform/animate |
| B05 | This does not mean nature secretly chooses one Pauli er | TELLS | motion=compare but no animation (only FadeIn/static) |
| B06 | A suitable code correlates correctable error components | SHOWS | multi-step animation (2 play calls) |
| B07 | If the syndrome identifies X, the recovery reverses X.  | TELLS | static display while narration implies motion |
| B08 | The deeper principle is linearity: if a code corrects a | TELLS | static display while narration implies motion |
| B09 | Real noise can also be probabilistic and entangle the q | TELLS | motion=compare but no animation (only FadeIn/static) |
| B10 | So four does not replace infinity by magic. Four suppli | SHOWS | multi-step animation (2 play calls) |
| B11 | Your turn. A tiny rotation is not exactly X, Y, or Z. W | EXEMPT | remotion:ClaudeComposerAsk |
| B12 | Every one-qubit operator is built from four: identity,  | TELLS | static display while narration implies motion |

**SHOWS:** 4  **TELLS:** 6  **EXEMPT:** 2

## Rebuilt TELLS

- **B02** REBUILT: I does nothing. X flips zero and one. Z changes their relati
- **B05** REBUILT: This does not mean nature secretly chooses one Pauli error b
- **B07** REBUILT: If the syndrome identifies X, the recovery reverses X. If it
- **B08** REBUILT: The deeper principle is linearity: if a code corrects a set 
- **B09** REBUILT: Real noise can also be probabilistic and entangle the qubit 
- **B12** REBUILT: Every one-qubit operator is built from four: identity, bit f