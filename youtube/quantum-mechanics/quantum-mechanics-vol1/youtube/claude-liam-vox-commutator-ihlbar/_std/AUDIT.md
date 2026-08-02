# SHOW-DON'T-TELL Audit — claude-liam-vox-commutator-ihlbar

**Date:** 2026-07-25
**Palette:** claude

| Beat | Narration (gist) | Classification | Reason |
|---|---|---|---|
| B01 | This is Liam, in for Bear. Ordinary numbers commute: x  | EXEMPT | remotion:ClaudeComposerAsk |
| B02 | Position is the multiplication operator: x hat acting o | TELLS | motion=derive with only one self.play (no step-by-step build |
| B03 | Momentum in the position representation is a derivative | TELLS | motion=derive with only one self.play (no step-by-step build |
| B04 | First apply momentum, then position. The result is minu | TELLS | motion=calculate with only one self.play (no step-by-step bu |
| B05 | Now reverse the operators: momentum acts on x psi. Diff | TELLS | motion=calculate with only one self.play (no step-by-step bu |
| B06 | Subtract in the order x p minus p x. The x psi prime te | SHOWS | multi-step animation (2 play calls) |
| B07 | Because this holds for every suitable wave function, th | TELLS | static display while narration implies motion |
| B08 | Reverse the commutator and the sign reverses: p x minus | TELLS | motion=compare but no animation (only FadeIn/static) |
| B09 | This algebra is not literally position measurement foll | TELLS | static display while narration implies motion |
| B10 | The Robertson relation turns a nonzero commutator into  | SHOWS | multi-step animation (2 play calls) |
| B11 | The bound describes the spreads of a prepared state. It | TELLS | static display while narration implies motion |
| B12 | One derivative product rule creates the remainder. That | SHOWS | static but narration ok with it |
| B13 | Your turn. Compute p x minus x p acting on psi, and pre | EXEMPT | remotion:ClaudeComposerAsk |
| B14 | Multiplication and differentiation miss commuting by ex | EXEMPT | remotion:ClaudeTitleOutro |

**SHOWS:** 3  **TELLS:** 8  **EXEMPT:** 3

## Rebuilt TELLS

- **B02** REBUILT: Position is the multiplication operator: x hat acting on psi
- **B03** REBUILT: Momentum in the position representation is a derivative: p h
- **B04** REBUILT: First apply momentum, then position. The result is minus i h
- **B05** REBUILT: Now reverse the operators: momentum acts on x psi. Different
- **B07** REBUILT: Because this holds for every suitable wave function, the ope
- **B08** REBUILT: Reverse the commutator and the sign reverses: p x minus x p 
- **B09** REBUILT: This algebra is not literally position measurement followed 
- **B11** REBUILT: The bound describes the spreads of a prepared state. It does