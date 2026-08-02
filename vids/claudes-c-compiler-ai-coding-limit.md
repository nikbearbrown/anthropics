## C10 — Claude Wrote a C Compiler From Scratch: What That Actually Proves

- **slug:** claudes-c-compiler-ai-coding-limit
- **source:** ../anthropics/claudes-c-compiler/README.md + blog post (anthropic.com/engineering/building-c-compiler)
- **bucket:** BUILD-WITH-CLAUDE / SDK → claude-scout lens → claude-explainer builder
- **premise:** Claude Opus 4.6 wrote a complete C compiler in Rust — frontend, SSA IR, optimizer, code generator, assembler, linker, DWARF debug info — with zero human pair-programming. The constraint: a human wrote test cases; Claude wrote everything else.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** The C compiler demo is not about Claude being good at coding — it's a proof of the test-driven-development methodology for long-horizon autonomous coding: write the tests, let the agent iterate; never pair-program to "help" it.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Claude, write me a C compiler from scratch in Rust`
- topic: `CLAUDE CODE · Long-Horizon Coding`
- segment: `No Human Pair-Programming`
- greeting: `Selam, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 what a C compiler actually requires (frontmatter: the 6 stages shown as a pipeline) → B02 the methodology: human writes tests, Claude iterates against them — the one rule that made it work → B03 what it produced: x86-64, i686, AArch64, RISC-V — 4 targets, no external toolchain dependencies → B04 the caveat (stated in their own README): "I do not recommend you use this code — none of it has been validated for correctness." What that caveat teaches about the methodology vs the artifact → HANDOFF → OUTRO

### Visual beats (4 suggested)
1. **B01 — Manim pipeline diagram:** The 6 compiler stages: Lexer → Parser → AST → SSA IR → Optimizer → Code Gen → Assembler → Linker. Each stage lights up in sequence as a block animation. The "from scratch" label: each stage is its own gray box, no library dependency arrows.
2. **B02 — Remotion concept card:** The TDD constraint illustrated as two boxes: human-writes (tests only, one golden rule) vs Claude-writes (everything else, iterates against tests, never gets human debugging help). The asymmetry is the methodology insight.
3. **B03 — Onda code-block:** Show the README's benchmark table: the 4 target architectures and their binary names. Then a working "hello world" compile-and-run loop. The payoff visual.
4. **B04 — ClaudeComposerAsk micro-beat:** Paste the README's own caveat quote as the ask. Then the result: "The caveat is the finding. A model that can build something it shouldn't be trusted to deploy is still a model that can build it." The Teardown judgment.

### Register notes
Teardown: the compiler's correctness disclaimer is not a weakness to gloss over — it IS the point. The methodology (test-driven, no pair-programming) is what this video teaches, not the artifact. Claude produced something that compiles C programs and generates ELF executables — that's real. Whether you'd run it in production is a different judgment.

### Est length
~120 s (4 beats, lighter mechanism weight)

### Scores
- Teachability: 4/5 — the TDD methodology is the clear takeaway
- Visual potential: 4/5 — the compiler pipeline diagram is a strong Manim beat
- Audience pull: 5/5 — "Claude wrote a compiler" is a headline
- Freshness: 4/5 — the blog post got attention, but the methodology story is underexplored
- **Total: 17/20**
