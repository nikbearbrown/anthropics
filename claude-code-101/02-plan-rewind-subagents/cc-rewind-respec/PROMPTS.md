# PROMPTS — cc-rewind-respec

The exact `claude -p` invocations that produced the four runs the reel reconstructs. Everything the film shows in a session block traces to one of these.

## Fix-forward chain — one session, three turns

Session id: **`a09ae7ad-3d64-4ab6-ae9d-77f894563768`** (in `evidence/sid-ff.txt`).

### FF1 — the vague ask
```bash
cd scratch/ && claude -p "The dedupe tests in test_dedupe.py are failing. Fix dedupe.py." \
  --session-id a09ae7ad-3d64-4ab6-ae9d-77f894563768 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-ff1.jsonl
```
Result: turns=9, 33.2 s.

### FF2 — "speed it up" (same session)
```bash
cd scratch/ && claude -p "That's O(n squared). Speed it up for large lists." \
  --resume a09ae7ad-3d64-4ab6-ae9d-77f894563768 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-ff2.jsonl
```
Result: turns=3, 12.4 s.

### FF3 — "simpler" (same session — the drift lands here)
```bash
cd scratch/ && claude -p "Simpler. One data structure." \
  --resume a09ae7ad-3d64-4ab6-ae9d-77f894563768 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-ff3.jsonl
```
Result: turns=3, 53.8 s. Wrote `return list({repr(x): x for x in items}.values())`. Tests pass; `dedupe([1, 1.0])` returns `[1, 1.0]`.

## The rewind (Liam, plain shell)

```bash
cd scratch/
git reset --hard f5ef78b        # HEAD is now at f5ef78b buggy start
cat dedupe.py                    # def dedupe(items): return list(set(items))
SID=$(uuidgen | tr A-Z a-z)      # 96c45930-f2c9-4a95-b152-e01653e11d07
# no --resume anywhere below; a new `claude -p` is /clear.
```

## Respec — fresh session, one turn

Session id: **`96c45930-f2c9-4a95-b152-e01653e11d07`** (in `evidence/sid-respec.txt`).

```bash
cd scratch/ && claude -p "The dedupe tests in test_dedupe.py fail. Fix dedupe.py so that: (1) order is preserved (first occurrence stays); (2) unhashable items like lists work; (3) equality is Python \`==\`, not \`repr\` — so dedupe([1, 1.0]) must return [1]. Use hashing with a linear-scan fallback via try/except. Do not modify the test." \
  --session-id 96c45930-f2c9-4a95-b152-e01653e11d07 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-respec.jsonl
```
Result: turns=7, 33.7 s. Wrote the two-branch equality-correct implementation. Tests pass; `dedupe([1, 1.0])` returns `[1]`.

## Notes

- All four runs used the same tool fence — no widening between fix-forward and respec.
- `Bash(python:*)` is deliberately NOT in the fence (SKILL: "keep `python3`, not `python`, in the allow-list"). This is why Claude's first two `python -m unittest` attempts were denied on FF1 and again on respec, before landing `python3 -m unittest`. The denials are omitted from the shot for height per the exemplar convention.
- Scratch was NOT `git clean`'d between FF3 and the rewind — `git reset --hard f5ef78b` was enough because the only file edited was `dedupe.py`, which is tracked. Evidence is preserved in `evidence/dedupe.ff3.py` and `evidence/dedupe.respec.py`.
