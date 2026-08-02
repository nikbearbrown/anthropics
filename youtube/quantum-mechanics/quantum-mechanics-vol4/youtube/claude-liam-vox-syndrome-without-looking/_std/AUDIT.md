# SHOW-DON'T-TELL Audit — claude-liam-vox-syndrome-without-looking

**Date:** 2026-07-25
**Palette:** claude

| Beat | Narration (gist) | Classification | Reason |
|---|---|---|---|
| B01 | This is Liam, in for Bear. You cannot copy an unknown q | EXEMPT | remotion:ClaudeComposerAsk |
| B02 | Take the three-qubit repetition code. The logical state | SHOWS | multi-step animation (2 play calls) |
| B03 | This code protects against one bit flip, an X error. It | TELLS | static display while narration implies motion |
| B04 | Suppose the middle physical qubit flips. The encoded st | SHOWS | has transform/animate |
| B05 | Instead, ask whether qubits one and two agree, and whet | TELLS | motion=compare but no animation (only FadeIn/static) |
| B06 | With no error, both pairs agree: syndrome zero-zero. If | TELLS | static display while narration implies motion |
| B07 | A flip on qubit two makes both checks disagree: one-one | TELLS | static display while narration implies motion |
| B08 | Crucially, the same syndrome appears for the zero-zero- | TELLS | motion=compare but no animation (only FadeIn/static) |
| B09 | Syndrome one-one therefore tells the controller to appl | SHOWS | multi-step animation (3 play calls) |
| B10 | The trick is not measurement without disturbance. It is | TELLS | static display while narration implies motion |
| B11 | Your turn. Syndrome one-zero appears in this convention | EXEMPT | remotion:ClaudeComposerAsk |
| B12 | Fixing quantum errors without looking: measure the erro | TELLS | static display while narration implies motion |

**SHOWS:** 3  **TELLS:** 7  **EXEMPT:** 2

## Rebuilt TELLS

- **B03** REBUILT: This code protects against one bit flip, an X error. It does
- **B05** REBUILT: Instead, ask whether qubits one and two agree, and whether q
- **B06** REBUILT: With no error, both pairs agree: syndrome zero-zero. If qubi
- **B07** REBUILT: A flip on qubit two makes both checks disagree: one-one. A f
- **B08** REBUILT: Crucially, the same syndrome appears for the zero-zero-zero 
- **B10** REBUILT: The trick is not measurement without disturbance. It is a ca
- **B12** REBUILT: Fixing quantum errors without looking: measure the error's f