# PROMPTS — cc-cwc-how-we-claude-code

The exact `claude -p` invocations behind the three runs. Reproducible from the reel's own `scratch/workshop/` folder — the folder was reset between conditions by moving output files to `evidence/`.

## Run 1 — bare

```
cd scratch/workshop
claude -p "Build workshop.html — a one-page landing for our Saturday intro-to-git workshop." \
  --output-format stream-json --verbose --max-turns 8 --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-bare.jsonl
```

Session `564333d3-…` · turns=5 · 53.2 s · $0.384 · one file written: `workshop.html` (130 lines).

## Run 2 — design (Phase 2)

```
cd scratch/workshop
claude -p "Read task.txt. Generate FOUR divergent HTML mockups for it as mock1.html, mock2.html, mock3.html, mock4.html — each a full self-contained page (inline CSS, no external assets). Each mockup MUST take a genuinely different design direction: a different content architecture, a different voice, a different visual tone. Do NOT build any other file. Do NOT run anything." \
  --output-format stream-json --verbose --max-turns 12 --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-design.jsonl
```

Session `dcbf6b63-…` · turns=6 · 297.1 s · $0.990 · four mockups: `mock1.html` (199), `mock2.html` (201), `mock3.html` (239), `mock4.html` (270).

## Run 3 — verify (Phase 3, converge)

`scratch/workshop/` reset to `task.txt`, `README.md`, `brief.md`, `fixture.py`, `mock2.html`.

```
cd scratch/workshop
claude -p "Read brief.md, task.txt, and mock2.html. Then build workshop.html — implement the layout of mock2.html to satisfy brief.md. You MUST run 'python3 fixture.py' before you say done, and it must print PASS. Do not commit until fixture.py passes." \
  --output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-verify.jsonl
```

Session `746ba72a-…` · turns=11 · 147.8 s · $0.851 · one file written (twice): `workshop.html` (153 lines after the correction). Correction cycle: Write → `python3 fixture.py` → `FAIL: no monospace font-family (voice: terminal)` → Edit → `python3 fixture.py` → `PASS: workshop.html meets brief.md's definition of done (153 lines)`.

## The prompt read in the reel (BHTF)

```
Your turn. Before your next build, open Claude Code in an empty folder and paste this:

Run the three phases on the smallest thing on my list. Interview me and write brief.md. Then generate four divergent mockups. Then write fixture.py from the brief and stop. Don't build the thing yet.
```
