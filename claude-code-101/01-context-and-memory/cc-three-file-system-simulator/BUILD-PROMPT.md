# BUILD-PROMPT — cc-three-file-system-simulator

## What this reel is

A 14-beat cc-explainer for **Claude Code 101 · tier 01 (context and memory)**.
Same one-sentence ask ("Build a sorting simulator for a ninth-grade class as
index.html.") issued twice to a headless Claude Code session — first to an
empty folder (bare), then to the same folder with three files (CLAUDE.md,
DESIGN.md, PROJECT.md) and a definition-of-done script (check.py) that Liam
wrote first. The bare page fails the checker on five constraints. The
three-file page passes — after a real correction cycle where Claude fails
`font-family: inherit`, and, following CLAUDE.md's rule, fixes the page, not
the script. Then the three-file page runs, on screen, as the film's receipt.

## Skill

`cc-explainer` (SKILL.md is in `brutalist-art/skills/make/cc-explainer/`).
BUILD-SHOW LAW **armed** (`metadata.build: true`): BFLOW (`FlowDiagram`) +
BSHOW (captured recording of the sim running) sit immediately before CONDUCT.

## Voice

Liam (Kokoro `am_onyx`, free/local), in for Bear, throughout — body and
closing block. Teardown register.

## Rebuild

```
cd anthropics/claude-code-101/01-context-and-memory/cc-three-file-system-simulator
python3 author_sheet.py            # writes beat_sheet.json (14 beats, ~5 min narrated)
python3 ../../../../brutalist-art/runtime/scripts/generate_audio_kokoro.py .
python3 ../../../../brutalist-art/runtime/qc/factcheck_check.py .    # must print `clean`
# from books/:
./brutalist-art/art run  anthropics/claude-code-101/01-context-and-memory/cc-three-file-system-simulator
./brutalist-art/art final anthropics/claude-code-101/01-context-and-memory/cc-three-file-system-simulator
```

## Never publish

Master stays in the reel folder. TOPOST via `post` only, only on Bear's ask.
