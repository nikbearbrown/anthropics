# BUILD-PROMPT — cc-prompt-is-a-wish-spec-is-a-contract

The one-line brief this reel was built to answer:

> Show, in the terminal, that a "clear ask" Claude can execute is a **wish**, not a **prompt** — and that the fix is a short **spec** written before Claude touches anything. Do it with a real, checkable session: run the same one-sentence ask with and without a spec, and show the diff.

## Scope

- Genre: `cc-explainer` (terminal-first; every body beat defaults to CCSession).
- Series: Claude Code 101, tier `04-spec-before-code`, film 01 of that tier.
- Operator: Liam, in for Bear (LIAM LAW). Kokoro `am_onyx`, Teardown register.
- Aspect: 16:9 (no Shorts cut). Native 4K target.
- Publish: never from the reel folder. Master stays here; TOPOST via `post` skill on ask only.

## Method

1. Design a real, checkable session — `scratch/wish/`, `scratch/spec/`, `scratch/testsonly/` — same tiny stdlib password module, three conditions.
2. Run each condition headless (`claude -p --output-format stream-json --verbose --strict-mcp-config`), fenced tools, `AskUserQuestion` NOT allowed (the denial is part of the pedagogy).
3. Save transcripts + outputs to `evidence/`.
4. Author every `CCSession` block from `SESSION.md` verbatim (product strings, tool names, file paths, ✓/OK all authentic).
5. Kokoro narration; measured mp3s become the master clock.
6. Compile: `./art run` → gates → `./art final`.

## What the film is NOT

- Not a security tutorial. It uses `hashlib.pbkdf2_hmac` because it's stdlib and reproducible; the film's subject is *how choices happen*, not *which hash to pick*.
- Not a benchmark of Claude. The wish run's output is competent (pbkdf2, salt, `compare_digest`); the point is that competence is not consent — the model made decisions the human should have made.
- Not a critique of Claude Code. The tool fence works as advertised; the denied AskUserQuestion IS the mechanism the film uses to reveal what a "prompt" leaves unspecified.
