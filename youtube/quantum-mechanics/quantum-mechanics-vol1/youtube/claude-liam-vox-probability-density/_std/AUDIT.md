# SHOW-DON'T-TELL Audit — claude-liam-vox-probability-density

**Date:** 2026-07-25
**Palette:** claude

| Beat | Narration (gist) | Classification | Reason |
|---|---|---|---|
| B01 | This is Liam, in for Bear. A normalized wave function c | EXEMPT | remotion:ClaudeComposerAsk |
| B02 | For a continuous position, absolute psi squared is a pr | TELLS | static display while narration implies motion |
| B03 | In one dimension its units are inverse length. A value  | TELLS | static display while narration implies motion |
| B04 | The probability for an interval is the integral of the  | SHOWS | has curve/axes/area animation |
| B05 | Consider psi equals one over square root a times e to t | TELLS | motion=derive with only one self.play (no step-by-step build |
| B06 | Its density is one over a times e to the minus two abso | TELLS | motion=calculate with only one self.play (no step-by-step bu |
| B07 | Now ask for the particle within plus or minus 0.1 nanom | SHOWS | multi-step animation (2 play calls) |
| B08 | The peak density exceeds one, yet the highlighted inter | TELLS | motion=compare but no animation (only FadeIn/static) |
| B09 | For an ideal continuous variable, the probability of on | SHOWS | static but narration ok with it |
| B10 | The density's numerical height also changes when you ch | TELLS | motion=convert but no animation (only FadeIn/static) |
| B11 | Population density works the same way. Ten thousand peo | TELLS | motion=analogy but no animation (only FadeIn/static) |
| B12 | Never ask whether a continuous density is below one. Ch | SHOWS | static but narration ok with it |
| B13 | Your turn. A nearly constant density is three per nanom | EXEMPT | remotion:ClaudeComposerAsk |
| B14 | Density may exceed one. Its integrated area may not. | EXEMPT | remotion:ClaudeTitleOutro |

**SHOWS:** 4  **TELLS:** 7  **EXEMPT:** 3

## Rebuilt TELLS

- **B02** REBUILT: For a continuous position, absolute psi squared is a probabi
- **B03** REBUILT: In one dimension its units are inverse length. A value of tw
- **B05** REBUILT: Consider psi equals one over square root a times e to the mi
- **B06** REBUILT: Its density is one over a times e to the minus two absolute 
- **B08** REBUILT: The peak density exceeds one, yet the highlighted interval p
- **B10** REBUILT: The density's numerical height also changes when you change 
- **B11** REBUILT: Population density works the same way. Ten thousand people p