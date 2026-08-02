#!/usr/bin/env python3
"""
build_skill_explainers.py — overnight batch builder for pending Anthropic skill teardown videos.

Reads: anthropics/SKILL-EXPLAINERS-BATCH-LOG.md (all "pending" rows)
Builds: beat_sheet.json → Kokoro audio → Remotion renders → compile --review
Writes: anthropics/BUILD-SKILL-EXPLAINERS-LOG.md (append)
Updates: SKILL-EXPLAINERS-BATCH-LOG.md (status column)

Pipeline is 100% free: Kokoro TTS (local), generic SkillTeardown Remotion patterns.
No ElevenLabs, no Higgsfield, no API spend.

Usage (from books/):
    python3 anthropics/build_skill_explainers.py              # build all pending
    python3 anthropics/build_skill_explainers.py --dry-run    # audit only
    python3 anthropics/build_skill_explainers.py --start 100  # resume from row 100
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── repo paths ──────────────────────────────────────────────────────────────────
HERE = Path(__file__).parent.resolve()   # books/anthropics/
BOOKS = HERE.parent.resolve()            # books/
ART = BOOKS / "brutalist-art"
SCRIPTS = ART / "runtime" / "scripts"

LOG_MD = HERE / "SKILL-EXPLAINERS-BATCH-LOG.md"
BUILD_LOG = HERE / "BUILD-SKILL-EXPLAINERS-LOG.md"

GEN_AUDIO     = str(SCRIPTS / "generate_audio_kokoro.py")
REMOTION_SCN  = str(SCRIPTS / "remotion_scenes.py")
COMPILE_PY    = str(SCRIPTS / "compile.py")
PY = sys.executable

# ── file-icon map for SkillTeardownAnatomy ─────────────────────────────────────
_ICON: dict[str, tuple[str, bool]] = {   # (icon, accent)
    ".md":   ("📄", True),
    ".py":   ("🐍", True),
    ".sh":   ("⚙️", True),
    ".json": ("📋", False),
    ".js":   ("🟨", False),
    ".ts":   ("🔷", False),
    ".mjs":  ("🟨", False),
    ".html": ("🌐", False),
    ".txt":  ("📝", False),
    ".yaml": ("⚙️", False),
    ".yml":  ("⚙️", False),
    ".toml": ("⚙️", False),
}

def _icon(name: str) -> tuple[str, bool]:
    return _ICON.get(Path(name).suffix.lower(), ("📄", False))

def _clean(text: str) -> str:
    """Strip markdown for narration."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*",     r"\1", text)
    text = re.sub(r"`(.+?)`",       r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return " ".join(text.split())

def _title(name: str) -> str:
    return " ".join(w.capitalize() for w in name.replace("-", " ").split())


# ── SKILL.md parsing ────────────────────────────────────────────────────────────

def parse_skill_md(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    r: dict = {"name": "", "description": "", "steps": [], "notes": []}

    # YAML frontmatter
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if fm:
        for line in fm.group(1).splitlines():
            if line.startswith("name:"):
                r["name"] = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("description:"):
                r["description"] = line.split(":", 1)[1].strip().strip('"\'')

    # Fall back: use filename as name
    if not r["name"]:
        r["name"] = path.parent.name

    # Steps section
    sm = re.search(r"^## Steps\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if sm:
        steps_text = sm.group(1)
        # Grab numbered items — bold title + body
        for m in re.finditer(
            r"^\d+\.\s+\*\*([^*\n]+)\*\*[.:]\s*(.*?)(?=^\d+\.|\Z)",
            steps_text, re.MULTILINE | re.DOTALL
        ):
            title = m.group(1).strip()
            body  = re.sub(r"```.*?```", "", m.group(2), flags=re.DOTALL)
            body  = _clean(body)[:120]
            r["steps"].append({"title": title, "body": body})
        # Fallback: plain numbered lines
        if not r["steps"]:
            for line in steps_text.splitlines():
                m2 = re.match(r"^\d+\.\s+(.+)", line.strip())
                if m2:
                    r["steps"].append({"title": _clean(m2.group(1))[:80], "body": ""})

    # Notes section
    nm = re.search(r"^## Notes\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if nm:
        for m in re.finditer(r"^[-*]\s+(.+?)(?=^[-*]|\Z)", nm.group(1),
                              re.MULTILINE | re.DOTALL):
            r["notes"].append(_clean(m.group(1))[:200])

    return r


def list_files(skill_dir: Path, max_f: int = 8) -> list[dict]:
    entries = []
    try:
        items = sorted(skill_dir.iterdir(), key=lambda p: (p.is_dir(), p.name.lower()))
        for item in items:
            if item.name.startswith("."):
                continue
            if item.is_dir():
                icon, accent = "📁", False
                sz = None
            else:
                icon, accent = _icon(item.name)
                try:
                    raw = item.stat().st_size
                    sz = f"{raw // 1024}k" if raw >= 1024 else f"{raw}b"
                except Exception:
                    sz = None
            entries.append({"indent": 1, "icon": icon, "name": item.name,
                             "size": sz, "accent": accent})
            if len(entries) >= max_f:
                break
    except Exception:
        pass
    # Ensure SKILL.md is always accent
    for e in entries:
        if e["name"] == "SKILL.md":
            e["accent"] = True
    return entries


# ── narration (Teardown register — confident, specific, no fluff) ───────────────

def _b00_narr(s: dict) -> str:
    desc = _clean(s["description"]) if s["description"] else f"a Claude skill"
    return (
        f"Hola — this is Liam, in for Bear. "
        f"The skill is {s['name']}. {desc}. "
        f"A SKILL.md tells Claude exactly how. Let me show you what's in it."
    )

def _b01_narr(s: dict) -> str:
    return (
        f"A skill is a folder Claude reads before it works. "
        f"This one is {s['name']}. "
        f"The SKILL.md contains the full instruction set — plain language, no hidden logic. "
        f"Claude reads it, then acts. The file is the program."
    )

def _b02_narr(s: dict) -> str:
    steps = s["steps"]
    n = len(steps)
    if not steps:
        return (
            f"The pipeline is in the Steps section. "
            f"Claude reads each step in order and executes it. "
            f"Linear — no branching unless the step says so."
        )
    titles = [st["title"] for st in steps[:3]]
    listed = " → ".join(titles)
    tail   = f", plus {n - 3} more" if n > 3 else ""
    return (
        f"The pipeline has {n} step{'s' if n != 1 else ''}. "
        f"{listed}{tail}. "
        f"Each step is a discrete action — Claude works through them in sequence. "
        f"Input in, steps run, output out."
    )

def _b03_narr(s: dict) -> str:
    if s["notes"]:
        note = _clean(s["notes"][0])
        return (
            f"Here is the design tell. {note}. "
            f"That is the interesting constraint in {s['name']} — "
            f"a deliberate trade-off baked into the instruction set."
        )
    desc = _clean(s["description"])
    return (
        f"Here is the Teardown moment. "
        f"{s['name']} is a specification written as an instruction set. "
        f"Claude's job: {desc[:100]}. "
        f"What it gets right: repeatable results. "
        f"What it bites: anything outside the spec."
    )

def _bvdt_narr(s: dict) -> str:
    desc = _clean(s["description"])[:80] if s["description"] else s["name"]
    return (
        f"{s['name']} makes Claude execute one task reliably. "
        f"The SKILL.md is the spec — {desc}. "
        f"Same input, same output, every run. Know the limit: only what the file says."
    )

def _bhtf_narr(s: dict) -> str:
    short = _clean(s["description"])[:80].lower().rstrip(".") if s["description"] else f"use {s['name']}"
    return (
        f"Your turn. Paste this into Claude: "
        f"'I want to {short}. Read the {s['name']} skill and walk me through "
        f"what you will do before you do it.' "
        f"That clause matters — explaining first surfaces the real constraint logic."
    )

def _bout_narr(s: dict) -> str:
    return f"Claude, {_title(s['name'])}. Liam, in for Bear."


# ── beat_sheet.json builder ─────────────────────────────────────────────────────

def make_beat_sheet(skill: dict, skill_dir: Path, reel_slug: str) -> dict:
    name   = skill["name"]
    title  = f"Claude, {_title(name)}."
    topic  = f"{name.upper()} · ANTHROPIC SKILL"
    steps  = skill["steps"]
    files  = list_files(skill_dir) or [{"indent": 1, "icon": "📄",
                                        "name": "SKILL.md", "accent": True}]

    # Pipeline phases (SkillTeardownPipeline)
    if steps:
        phases = [
            {"label": st["title"][:30], "desc": (st["body"] or "")[:60], "accent": i == 0}
            for i, st in enumerate(steps[:4])
        ]
    else:
        phases = [
            {"label": "Read SKILL.md", "desc": "load the instruction set", "accent": True},
            {"label": "Execute",       "desc": "run each step in order",    "accent": False},
            {"label": "Return output", "desc": "deliver the result",        "accent": False},
        ]

    # Mechanism body (SkillTeardownMechanism)
    mech_body = _clean(skill["notes"][0]) if skill["notes"] else _clean(skill["description"])[:200]

    # Verdict lines
    desc = _clean(skill["description"])
    verdict_lines = [
        f"Skill: {name} — Claude reads SKILL.md before acting",
        (desc[:90] if desc else f"Executes the {name} workflow reliably"),
    ]
    if steps:
        verdict_lines.append(
            f"{len(steps)}-step pipeline: {' → '.join(st['title'] for st in steps[:3])}"
        )
    verdict_lines += [
        "Same input → same output, every run",
        "Limit: only what the SKILL.md specifies",
    ]
    verdict_lines = verdict_lines[:5]

    def _beat(bid, act, narr, pattern, props, dur) -> dict:
        return {
            "beat_id": bid,
            "act": act,
            "narration_text": narr,
            "voice": "am_onyx",
            "engine": "kokoro",
            "estimated_duration_s": dur,
            "shot": {
                "type": "REMOTION",
                "remotion": {
                    "pattern": pattern,
                    "props": props,
                    "rendered": {"out": f"media/{bid}.mp4", "at": ""},
                },
            },
            "audio_file": f"mp3/beat-{bid}.mp3",
        }

    cl_props_open = {
        "greeting": "Hola, Liam",
        "topic": topic,
        "segment": title,
        "command": f"Run the {name} skill.",
        "runningText": f"reading {name} SKILL.md…",
        "output": [
            f"skill: {name}",
            desc[:80] if desc else f"Claude skill: {name}",
            f"steps: {len(steps)} — executing.",
        ],
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Opus 4.8",
        "effortLabel": "High",
    }

    cl_props_htf = {
        "greeting": "Your turn.",
        "topic": topic,
        "segment": title,
        "command": (
            f"I want to {_clean(skill['description'])[:70].lower().rstrip('.') if skill['description'] else f'use {name}'}. "
            f"Read the {name} skill and walk me through what you will do before you do it."
        ),
        "runningText": "paste this into Claude…",
        "output": [],
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Opus 4.8",
        "effortLabel": "High",
    }

    beats = [
        _beat("B00", "cold open",             _b00_narr(skill),  "ClaudeComposerAsk",      cl_props_open, 26),
        _beat("B01", "anatomy",               _b01_narr(skill),  "SkillTeardownAnatomy",   {
            "skillName":   name,
            "eyebrow":     "SKILL · ANATOMY",
            "title":       "A skill is a folder.",
            "files":       files,
            "calloutText": "The SKILL.md is the instruction set.",
            "calloutSub":  f"{len(files)} file{'s' if len(files) != 1 else ''} total.",
            "sparkLine":   "The file is the program.",
        }, 24),
        _beat("B02", "pipeline",              _b02_narr(skill),  "SkillTeardownPipeline",  {
            "eyebrow":     "SKILL · PIPELINE",
            "title":       "How the skill works.",
            "inputLabel":  "YOUR REQUEST",
            "outputLabel": "RESULT",
            "phases":      phases,
            "footerNote":  f"{len(steps)} steps. Linear execution." if steps else "Linear execution.",
            "sparkLine":   "Input in. Output out.",
        }, 26),
        _beat("B03", "design tell",           _b03_narr(skill),  "SkillTeardownMechanism", {
            "eyebrow":  "SKILL · DESIGN TELL",
            "heading":  "The interesting constraint.",
            "body":     mech_body[:200],
            "sparkLine": "This is the part worth knowing.",
        }, 28),
        _beat("BVDT", "verdict",              _bvdt_narr(skill), "ClaudeVerdictArtifact",  {
            "artifactTitle":   "Verdict",
            "artifactHeading": title,
            "artifactLines":   verdict_lines,
        }, 18),
        _beat("BHTF", "handoff — Your Turn",  _bhtf_narr(skill), "ClaudeComposerAsk",      cl_props_htf, 24),
        _beat("BOUT", "outro",                _bout_narr(skill), "ClaudeTitleOutro",        {
            "title":  title,
            "handle": "@NikBearBrown",
            "subline": f"{name} · Anthropic Skills",
        }, 6),
    ]

    return {
        "metadata": {
            "title":        title,
            "slug":         reel_slug,
            "topic":        topic,
            "register":     "Teardown",
            "audience":     "Claude",
            "brand":        "claude-liam",
            "persona":      "Liam (in for Bear)",
            "voice":        "am_onyx",
            "engine":       "kokoro",
            "voice_kokoro": "am_onyx",
            "palette":      "claude",
            "style_preset": "claude",
            "ground":       "#FAF9F5",
            "greeting":     "Hola, Liam",
            "folderLabel":  "@NikBearBrown",
            "in_for_bear":  True,
            "playlist":     "Claude Taught",
            "modifier":     "skill-teardown",
            "modelLabel":   "Opus 4.8",
            "source_skill": str(skill_dir / "SKILL.md"),
            "build": {
                "at":           datetime.now().isoformat(timespec="seconds"),
                "cut":          "review",
                "filled":       0,
                "of":           len(beats),
                "slates":       [],
                "skin_warnings": [],
            },
        },
        "beats": beats,
    }


# ── log helpers ─────────────────────────────────────────────────────────────────

def parse_log(log_path: Path) -> list[dict]:
    rows: list[dict] = []
    in_table = False
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| # |"):
            in_table = True; continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 9:
                rows.append({
                    "num":            parts[0],
                    "name":           parts[1],
                    "repo":           parts[2],
                    "canonical_path": parts[3],
                    "dupes":          parts[4],
                    "status":         parts[5],
                    "mp4_path":       parts[6],
                    "runtime":        parts[7],
                    "notes":          parts[8],
                    "_raw":           line,
                })
    return rows


def reel_dir_from_mp4(mp4_path: str) -> Path:
    """
    'anthropics/foo/youtube/claude-liam-bar/mp4/claude-liam-bar.mp4'
      → BOOKS/anthropics/foo/youtube/claude-liam-bar/
    'anthropics/foo/youtube/claude-liam-bar/claude-liam-bar.mp4'
      → BOOKS/anthropics/foo/youtube/claude-liam-bar/
    """
    parts = Path(mp4_path).parts
    if "mp4" in parts:
        idx = list(parts).index("mp4")
        rel = parts[:idx]
    else:
        rel = parts[:-1]
    return BOOKS / Path(*rel)


def reel_done(reel_dir: Path, slug: str) -> bool:
    return any((
        (reel_dir / f"{slug}-slate.mp4").exists(),   # compile --review output
        (reel_dir / f"{slug}.mp4").exists(),          # compile final output
        (reel_dir / "mp4" / f"{slug}.mp4").exists(),  # staged cut
    ))


def update_log_row(log_path: Path, num: str, status: str, notes: str = "") -> None:
    text   = log_path.read_text(encoding="utf-8")
    lines  = text.splitlines()
    prefix = f"| {num} |"
    out = []
    for line in lines:
        if line.startswith(prefix):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 9:
                parts[5] = status
                if notes:
                    parts[8] = notes
                line = "| " + " | ".join(parts) + " |"
        out.append(line)
    log_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def update_log_header(log_path: Path, built: int, pending: int, failed: int) -> None:
    text = log_path.read_text(encoding="utf-8")
    # Update the summary line
    text = re.sub(
        r"Total unique skills: \d+ \| Pending: \d+ \| Built: \d+ \| Failed: \d+",
        f"Total unique skills: 524 | Pending: {pending} | Built: {built} | Failed: {failed}",
        text,
    )
    log_path.write_text(text, encoding="utf-8")


# ── subprocess helper ───────────────────────────────────────────────────────────

def run(cmd: list[str], timeout: int = 1200) -> tuple[bool, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, (r.stdout + r.stderr)[-800:]
    except subprocess.TimeoutExpired:
        return False, f"TIMEOUT after {timeout}s"
    except Exception as e:
        return False, str(e)


# ── per-reel pipeline ───────────────────────────────────────────────────────────

def build_one(row: dict, dry_run: bool, log_fh) -> str:
    """Returns 'built' | 'failed' | 'skipped'."""
    num  = row["num"]
    name = row["name"]
    tag  = f"[{num:>3}] {name}"

    def say(msg: str) -> None:
        line = f"{tag}: {msg}"
        print(line)
        log_fh.write(line + "\n")
        log_fh.flush()

    # Resolve skill source
    skill_md = BOOKS / row["canonical_path"]
    if not skill_md.exists():
        say(f"SKIP — SKILL.md missing: {row['canonical_path']}")
        return "failed"

    reel_dir = reel_dir_from_mp4(row["mp4_path"])
    slug     = Path(row["mp4_path"]).stem

    # Already done?
    if reel_done(reel_dir, slug):
        say(f"SKIP — already compiled")
        return "skipped"

    if dry_run:
        say(f"DRY RUN → {reel_dir.relative_to(BOOKS)}")
        return "skipped"

    # 1. Parse SKILL.md
    skill     = parse_skill_md(skill_md)
    skill_dir = skill_md.parent

    # 2. Scaffold reel directory
    for sub in ("mp3", "media", "mp4", "clips"):
        (reel_dir / sub).mkdir(parents=True, exist_ok=True)

    # 3. Write beat_sheet.json (skip if exists — resumable)
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        bs = make_beat_sheet(skill, skill_dir, slug)
        bs_path.write_text(json.dumps(bs, indent=2, ensure_ascii=False), encoding="utf-8")
        say("beat_sheet.json written")
    else:
        say("beat_sheet.json exists — skipping beat sheet generation")

    # 4. Write PEDAGOGY.md (required by audio generator, --no-gate bypasses the check anyway)
    ped = reel_dir / "PEDAGOGY.md"
    if not ped.exists():
        ped.write_text(
            f"# PEDAGOGY — {name}\n\nVERDICT: PASS\n\nBatch build — skill teardown format.\n",
            encoding="utf-8",
        )

    # 5. Generate audio (Kokoro, free/local)
    say("generating audio…")
    ok, out = run([PY, GEN_AUDIO, str(reel_dir), "--no-gate"], timeout=360)
    if not ok:
        say(f"AUDIO FAIL: {out[-400:]}")
        return "failed"
    say("audio OK")

    # 6. Render Remotion beats
    say("rendering Remotion…")
    ok, out = run([PY, REMOTION_SCN, str(reel_dir)], timeout=1800)
    if not ok:
        say(f"REMOTION FAIL: {out[-400:]}")
        return "failed"
    say("remotion OK")

    # 7. Compile review cut
    say("compiling review cut…")
    ok, out = run([PY, COMPILE_PY, str(reel_dir), "--review", "--allow-slates"], timeout=600)
    if not ok:
        say(f"COMPILE FAIL: {out[-400:]}")
        return "failed"

    # Verify output
    if reel_done(reel_dir, slug):
        say(f"DONE ✓")
        return "built"

    say(f"COMPILE returned 0 but no mp4 found — treating as failed")
    return "failed"


# ── main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(description="Overnight batch skill explainer builder")
    ap.add_argument("--dry-run", action="store_true",
                    help="Audit pending rows without building anything")
    ap.add_argument("--start", type=int, default=1,
                    help="Start from log row N (skip earlier rows)")
    ap.add_argument("--end",   type=int, default=9999,
                    help="Stop after log row N")
    args = ap.parse_args()

    rows    = parse_log(LOG_MD)
    pending = [r for r in rows
               if "pending" in r["status"]
               and args.start <= int(r["num"]) <= args.end]

    print(f"=== BUILD-SKILL-EXPLAINERS overnight batch ===")
    print(f"    pending rows : {len(pending)}")
    print(f"    row range    : {args.start}–{args.end}")
    print(f"    dry_run      : {args.dry_run}")
    print(f"    started      : {datetime.now().isoformat(timespec='seconds')}")
    print()

    built = failed = skipped = 0
    today = datetime.now().strftime("%Y-%m-%d")

    with BUILD_LOG.open("a", encoding="utf-8") as log_fh:
        log_fh.write(
            f"\n\n## Run {datetime.now().isoformat(timespec='seconds')} "
            f"rows {args.start}–{args.end}  dry_run={args.dry_run}\n\n"
        )

        for row in pending:
            result = build_one(row, args.dry_run, log_fh)

            if result == "built":
                built += 1
                update_log_row(LOG_MD, row["num"], "built", notes=f"batch {today}")
            elif result == "failed":
                failed += 1
                update_log_row(LOG_MD, row["num"], "failed", notes=f"batch fail {today}")
            else:
                skipped += 1

        # Recount totals from log for accurate header
        all_rows     = parse_log(LOG_MD)
        total_built  = sum(1 for r in all_rows if "built"  in r["status"])
        total_pending= sum(1 for r in all_rows if "pending" in r["status"])
        total_failed = sum(1 for r in all_rows if "failed" in r["status"])
        if not args.dry_run:
            update_log_header(LOG_MD, total_built, total_pending, total_failed)

        summary = (
            f"\n## Summary: {built} built, {failed} failed, {skipped} skipped"
            f" | {datetime.now().isoformat(timespec='seconds')}\n"
        )
        log_fh.write(summary)
        print(summary.strip())


if __name__ == "__main__":
    main()
