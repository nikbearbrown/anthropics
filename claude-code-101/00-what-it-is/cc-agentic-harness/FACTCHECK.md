# FACTCHECK — cc-agentic-harness

Status: PASS — checked 2026-09-08 by the build session against `SESSION.md` (six real headless Claude Code runs: A `c9907c1a-…`, A2 `f53fd535-…`, B `ab5c9393-…`, loop1 `f6c45914-…`, loop2 `7aac741c-…`, loop3 `4effe52c-…`) and their `evidence/` files.

**Verification boundary.** Every factual claim in this reel is a claim about runs that happened on 2026-09-08 and are transcribed in `SESSION.md`, with the raw stream-json in `evidence/`. The "what a harness is" framing (prompt engineering → context engineering → harness engineering; the loop with fresh context) is Bear's brief for film 00 and is grounded here only in what the runs showed; no third-party video or article is quoted. Anthropic's engineering posts are cited in `SOURCES.md` as the public background for the terms, not as sources of any on-screen fact. Product strings on screen are rendered by the CC kit from `tokens/claudecode.ts`.

**Display convention.** Commands Liam ran in the plain shell between runs (`ls`, `cat`, `git diff --stat`, the `ls | grep -c jsonl`) are shown as bang commands inside the session shell — same command, same output verbatim. The shell invocation that made each run what it was (`--tools ""`, `--allowedTools …`, `--output-format stream-json`) is carried in the `CCSession` title of that beat.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Liam's line 'Claude Code is not a better model. It's the same model you talk to in the chat window' — the writer corrects 'better' → 'different' | PASS | both init events carry the same model id; the harness rings (B07) are what differs | — |
| 2 | BDEFS | Definitions card: headless · tools list · connector (MCP) · permission mode · stream-json | PASS | `claude --help` (`-p/--print`, `--tools`, `--allowedTools`, `--permission-mode`, `--output-format stream-json`, `--mcp-config`); high-level, one line each | — |
| 3 | B00 | The ask, verbatim in the prompt block | PASS | `SESSION.md` (the shared ask); `evidence/askA.txt` | — |
| 4 | B00 | With `--tools "" --strict-mcp-config`, Claude replied "Creating the file now." and no file appeared; `ls` → `README.md` | PASS | `SESSION.md` → Run A2; `evidence/runA2.jsonl` (one assistant text block, zero `tool_use` blocks; `ls` afterwards: `README.md`) | — |
| 5 | B00 | "no tools, none" | PASS | Run A2 init: `"tools": []`, `"mcp_servers": []` | — |
| 6 | B01 | The init event's keys and counts: `permissionMode acceptEdits`; 30 built-in tools + 140 `mcp__…`; 5 MCP servers; 40 skills; 9 agents; 56 slash commands; `cwd`; `memory_paths` | PASS | `evidence/runB.jsonl` init event, counted by script (`SESSION.md` → Run B → init). Bracketed counts on screen stand in for the arrays; the keys are verbatim | — |
| 7 | B01 | "a hundred and forty more from connectors on this Mac" | PASS | the 140 `mcp__…` tool names come from the claude.ai connectors and the Vercel plugin listed in `mcp_servers` | — |
| 8 | B01, B02, B03 | Status-line figures (`0m 03s`, `↓ 0.2k tokens`) | EXEMPT | kit chrome; headless prints no status line; real timing/usage in RESULT lines, not spoken | — |
| 9 | B02 | With `--allowedTools "Read,Write,Bash(ls:*),Bash(cat:*)"`: one `Write hello.txt`, "Created `hello.txt` with the single line `hello`.", two turns; `cat hello.txt` → `hello` | PASS | `SESSION.md` → Run B; `evidence/runB.jsonl` (`num_turns: 2`) | — |
| 10 | B02 | "Same model" | PASS | both init events: `"model": "claude-opus-4-7[1m]"` (on screen nowhere; never spoken by name — datable) | — |
| 11 | B03 | With `--tools ""` but connectors attached: `mcp__claude_ai_Google_Drive__create_file` `{"title": "hello.txt", …}` → "Claude requested permissions to use mcp__claude_ai_Google_Drive__create_file, but you haven't granted it yet."; then `Write` → "No such tool available: Write. Write exists but is not enabled in this context." | PASS | `SESSION.md` → Run A; `evidence/runA.jsonl`. The Write error line is shortened to its first sentence on screen | — |
| 12 | B03 | Claude's explanation: "I don't have a filesystem write or shell tool available in this session — only MCP tools (Artlist, Higgsfield, Google Drive, Microsoft 365, Vercel)." | PASS | `SESSION.md` → Run A → CLAUDE; the list is truncated with `…` on screen | — |
| 13 | B03 | "the permission layer stopped it" | PASS | the tool result is the harness's permission refusal, not a Drive error | — |
| 14 | B04 | `tasks.md`, `LOOP.md`, and the `for i in 1 2 3` loop with `--allowedTools Read,Write,Edit --strict-mcp-config` | PASS | `SESSION.md` → Run C; `evidence/tasks.md` (pre-loop content in `evidence/tasks.diff`), `evidence/LOOP.md`. The on-screen loop omits `--permission-mode acceptEdits --output-format stream-json --verbose > loop$i.jsonl` for width; the full line is in `SESSION.md` | — |
| 15 | B04 | "ten lines" | PASS | 4 (tasks.md) + 1 (LOOP.md) + 3 (the loop) + 2 (its flags) ≈ ten; the shell shows nine | — |
| 16 | B05 | Iteration 1: `Read tasks.md`, `Write a.md`, `Edit tasks.md` (`- [ ] write a.md…` → `- [x] write a.md…`), reply "Did task: write a.md: one line, alpha", 4 turns | PASS | `SESSION.md` → Run C → Iteration 1; `evidence/loop1.jsonl` | — |
| 17 | B05 | "It didn't do b, it didn't do c" | PASS | `evidence/loop1.jsonl`: exactly one Write (`a.md`) and one Edit; `git diff --stat` after the loop: `tasks.md` 3 insertions, 3 deletions | — |
| 18 | B06 | `cat tasks.md` → three `[x]`; `cat a.md b.md c.md` → `alpha`, `bravo`, `charlie`; `git diff --stat` → `tasks.md \| 6 +++---`; `ls ~/.claude/projects/*harness*/ \| grep -c jsonl` → `6` (the glob matches one directory) | PASS | `SESSION.md` → Liam's VERIFY after the loop. `alpha  bravo  charlie` is the three-line output joined on one screen line | — |
| 19 | B06 | "No iteration ever saw another's transcript" | PASS | three separate session ids; each `loop*.jsonl` starts with its own init event; the only shared state is the repo | — |
| 20 | B07 | Ring items are strings from the runs: `"tools": [ 30 built-in ]`, `"mcp_servers": [ 5 ]`, `"memory_paths"`, `"permissionMode"`, `--max-turns`, `for i in 1 2 3`, `tasks.md` | PASS | Run B init event; the shell lines in `SESSION.md` | — |
| 21 | B07 | "the system prompt, your CLAUDE.md" as the PROMPT ring; "the fence around the folder"; "a turn limit" | PASS | `claude --help` (`--system-prompt`, `--append-system-prompt`, CLAUDE.md auto-discovery under `--bare`; `--max-turns`); the cwd fence is the blocked-`ls` behaviour shown in `cc-five-claudes-explained` and implied by the init `cwd` | — |
| 22 | B07 | "assistant → tool → result" as the loop | PASS | the event order in every `evidence/*.jsonl` | — |
| 23 | B09 | Six steps, handoffs, tally PF 1 · PA 1 · TO 1 · IJ 0 · EI 0 | PASS | each step maps to a run in `SESSION.md` (2 → A2; 3 → the A2 stream; 4 → B; 5 → C setup; 6 → loop1–3) | — |
| 24 | B10 | Ledger rows ("it did" rows → Run A's explanation; the three stops → loop replies) | PASS | `SESSION.md` | — |
| 25 | BVDT | Verdict lines | PASS | as rows 2, 7, 9, 14–16 | — |
| 26 | BHTF | The viewer's prompt | EXEMPT | an instruction to the viewer | — |
| 27 | all | Version strings / model id in the jsonl | EXEMPT | `2.1.150` never shown; the model id never shown or spoken (datable) | — |
| 28 | metadata | Run costs (A $0.725, A2 $0.037, B $0.136, loops ≈ $0.13 each) | EXEMPT | recorded in `SOURCES.md`, not spoken | — |

## Not used — what Bear's reference pointed at that this reel does not repeat

Bear pasted a third-party video transcript on "harness engineering" as the concept pointer. Its history claims (when the term was coined, which products did what first, a sponsor segment) are not repeated, quoted, or paraphrased here; the reel shows the idea from six real runs instead. Anthropic's own engineering posts on agents, harnesses and context engineering are the public background named in `SOURCES.md`.
