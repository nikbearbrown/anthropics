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


def _trim(text: str, n: int) -> str:
    """Cut to <= n chars on a WORD boundary.

    A raw text[:n] slice cut mid-word and the truncation was audible in the
    narration — every skill video said "the way a profes" out loud. Never slice
    a string that will be spoken or shown; trim it here.
    """
    text = (text or "").strip()
    if len(text) <= n:
        return text
    cut = text[:n]
    sp = cut.rfind(" ")
    if sp > n * 0.5:           # a space near the end — cut there
        cut = cut[:sp]
    return cut.rstrip(" ,;:—-") + "…"

def _title(name: str) -> str:
    return " ".join(w.capitalize() for w in name.replace("-", " ").split())


# ── SKILL.md parsing ────────────────────────────────────────────────────────────

def parse_skill_md(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    r: dict = {
        "name": "",
        "description": "",
        "steps": [],
        "notes": [],
        "capabilities": [],
        "constraints": [],
        "referenced_files": [],
        "code_signals": [],
        "sections": [],
    }

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

    # ── Steps ───────────────────────────────────────────────────────────────
    # The old parser looked for a section titled literally "## Steps". ZERO of
    # the 734 SKILL.md files in this tree have one — they use "## Step 1: ...",
    # or "## Instructions" / "## Workflow". So `steps` was ALWAYS empty and every
    # one of the ~83 skill videos took the generic fallback branch, which is why
    # they all said "the pipeline is in the Steps section" and named nothing.

    # (a) the real pattern: sibling headings "## Step 1: Decide what belongs..."
    for m in re.finditer(r"^#{2,3}\s*Step\s+(\d+)\s*(.+?)\s*$\n(.*?)(?=^#{2,3}\s|\Z)",
                         text, re.MULTILINE | re.DOTALL):
        title = _clean(m.group(2)).lstrip(":.)-–—  ").strip()
        body  = re.sub(r"```.*?```", "", m.group(3), flags=re.DOTALL)
        r["steps"].append({"title": title, "body": _trim(_clean(body), 120)})

    # (b) a numbered list under any procedure-ish heading
    if not r["steps"]:
        sm = re.search(
            r"^#{2,3}\s*(?:Steps|Instructions|Workflow|Process|Procedure|Usage|"
            r"How it works|How to use|Quick ?start)\s*\n(.*?)(?=^#{2,3}\s|\Z)",
            text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        if sm:
            steps_text = sm.group(1)
            for m in re.finditer(
                r"^\d+\.\s+\*\*([^*\n]+)\*\*[.:]?\s*(.*?)(?=^\d+\.|\Z)",
                steps_text, re.MULTILINE | re.DOTALL
            ):
                body = re.sub(r"```.*?```", "", m.group(2), flags=re.DOTALL)
                r["steps"].append({"title": _clean(m.group(1)),
                                   "body": _trim(_clean(body), 120)})
            if not r["steps"]:
                for line in steps_text.splitlines():
                    m2 = re.match(r"^\d+\.\s+(.+)", line.strip())
                    if m2:
                        r["steps"].append({"title": _trim(_clean(m2.group(1)), 80),
                                           "body": ""})
            # Many skills write the procedure as bullets, not a numbered list.
            if not r["steps"]:
                for line in steps_text.splitlines():
                    m3 = re.match(r"^[-*]\s+(?:\*\*)?([^*\n]{4,90})", line.strip())
                    if m3:
                        r["steps"].append({"title": _trim(_clean(m3.group(1)), 80),
                                           "body": ""})
                r["steps"] = r["steps"][:6]

    # ── Notes / the design tell ─────────────────────────────────────────────
    # Same failure: "## Notes" is rare. The constraint that makes a skill THIS
    # skill usually lives under a working-style or rules heading.
    nm = re.search(
        r"^#{2,3}\s*(?:Notes|Working style|Answer format|Output format|"
        r"Constraints|Rules|Guidelines|Limitations|Caveats|Important)\s*\n"
        r"(.*?)(?=^#{2,3}\s|\Z)",
        text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if nm:
        for m in re.finditer(r"^[-*]\s+(.+?)(?=^[-*]|\Z)", nm.group(1),
                              re.MULTILINE | re.DOTALL):
            r["notes"].append(_trim(_clean(m.group(1)), 200))
        if not r["notes"]:
            para = _clean(nm.group(1))
            if para:
                r["notes"].append(_trim(para, 200))

    # Deeper detail extraction. The reel should be able to explain any skill
    # from the actual SKILL.md, not just say "there is a pipeline."
    r["sections"] = [
        _clean(h).strip()
        for h in re.findall(r"^#{2,3}\s+(.+?)\s*$", text, re.MULTILINE)
    ][:10]

    detail_sections = (
        "Key concepts", "Capabilities", "What it does", "Use cases", "Supports",
        "Tools", "Libraries", "Command-Line Tools", "Python Libraries",
        "Component Organization", "Directory Structure", "Review Dimensions",
        "How It Works", "Output", "Deliverables",
    )
    for heading in detail_sections:
        sm = re.search(
            rf"^(?:#{{2,3}}\s*{re.escape(heading)}|\*\*{re.escape(heading)}:\*\*)\s*\n"
            r"(.*?)(?=^#{2,3}\s|^\*\*[^\n]+:\*\*\s*$|\Z)",
            text, re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if sm:
            block = sm.group(1)
            for m in re.finditer(r"^[-*]\s+(.+)", block, re.MULTILINE):
                item = _trim(_clean(m.group(1)), 150)
                if item and item not in r["capabilities"]:
                    r["capabilities"].append(item)
            for m in re.finditer(r"^#{3,4}\s+(.+)", block, re.MULTILINE):
                item = _trim(_clean(m.group(1)), 120)
                if item and item not in r["capabilities"]:
                    r["capabilities"].append(item)
            for m in re.finditer(r"^\*\*([^*\n]{3,80})\*\*:?(?:\s+(.+))?", block, re.MULTILINE):
                label = _clean(m.group(1))
                tail = _clean(m.group(2) or "")
                item = _trim(f"{label}: {tail}" if tail else label, 150)
                if item and item not in r["capabilities"]:
                    r["capabilities"].append(item)
        if len(r["capabilities"]) >= 8:
            break

    if not r["capabilities"] and r.get("description"):
        desc_bits = re.split(r",\s+|;\s+|\.\s+", _clean(r["description"]))
        for bit in desc_bits:
            bit = bit.strip()
            if 12 <= len(bit) <= 150 and bit.lower() not in ("this includes", "use this skill"):
                r["capabilities"].append(_trim(bit, 140))
            if len(r["capabilities"]) >= 5:
                break

    rule_sections = (
        "Critical rules", "Important", "Path rules", "Constraints", "Rules",
        "Limitations", "Caveats", "Warnings", "Security", "Safety",
    )
    for heading in rule_sections:
        sm = re.search(
            rf"^(?:#{{2,4}}\s*{re.escape(heading)}|\*\*{re.escape(heading)}:\*\*)\s*\n"
            r"(.*?)(?=^#{2,4}\s|^\*\*[^\n]+:\*\*\s*$|\Z)",
            text, re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if sm:
            for m in re.finditer(r"^(?:[-*]|\d+\.)\s+(.+)", sm.group(1), re.MULTILINE):
                item = _trim(_clean(m.group(1)), 170)
                if item and item not in r["constraints"]:
                    r["constraints"].append(item)

    for m in re.finditer(r"(?im)^.*\b(?:MUST|NEVER|required|do not|cannot|only)\b.*$", text):
        item = _trim(_clean(m.group(0)).strip("-* 0123456789. "), 170)
        if item and item not in r["constraints"]:
            r["constraints"].append(item)
        if len(r["constraints"]) >= 8:
            break

    code_langs = [lang.strip() for lang in re.findall(r"```([^\n`]*)", text) if lang.strip()]
    for lang in code_langs:
        sig = f"code block: {lang}"
        if sig not in r["code_signals"]:
            r["code_signals"].append(sig)
    for token in re.findall(r"`([^`\n]{2,80})`", text):
        if any(ch in token for ch in "/.$_-") or token.endswith((".py", ".md", ".json", ".sh", ".ts", ".js", ".yaml", ".yml")):
            clean = _clean(token)
            if clean not in r["referenced_files"]:
                r["referenced_files"].append(clean)

    for item in sorted(path.parent.iterdir(), key=lambda p: p.name.lower()):
        if item.name.startswith(".") or item.name == "SKILL.md":
            continue
        label = item.name + ("/" if item.is_dir() else "")
        if label not in r["referenced_files"]:
            r["referenced_files"].append(label)

    r["capabilities"] = r["capabilities"][:8]
    r["constraints"] = r["constraints"][:8]
    r["referenced_files"] = r["referenced_files"][:10]
    r["code_signals"] = r["code_signals"][:6]

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
    cap = f" Its concrete surface area includes {_trim('; '.join(s.get('capabilities', [])[:3]), 180)}." if s.get("capabilities") else ""
    return (
        f"Hola — this is Liam, in for Bear. "
        f"The skill is {s['name']}. {desc}.{cap} "
        f"A SKILL.md tells Claude exactly how. Let me show you what's in it."
    )

def _b01_narr(s: dict) -> str:
    refs = s.get("referenced_files", [])
    ref_sentence = ""
    if refs:
        ref_sentence = f" It also points at {', '.join(refs[:3])}, so the skill is more than one paragraph of advice."
    return (
        f"A skill is a folder Claude reads before it works. "
        f"This one is {s['name']}. "
        f"The SKILL.md contains the full instruction set — plain language, no hidden logic."
        f"{ref_sentence} Claude reads it, then acts. The file is the program."
    )

def _b02_narr(s: dict) -> str:
    steps = s["steps"]
    n = len(steps)
    if not steps:
        # NOT every skill is a pipeline. Many SKILL.md files are reference and
        # lookup skills. Say what is actually true, then name the actual surface.
        what = _trim(_clean(s.get("description", "")), 150)
        caps = s.get("capabilities", [])
        if caps:
            return (
                f"{s['name']} is not a simple numbered pipeline. It is a reference "
                f"Claude reads and applies. The concrete pieces are: "
                f"{'; '.join(caps[:4])}. The instruction set IS the behaviour."
            )
        if what:
            return (
                f"{s['name']} is not a pipeline — it is a reference Claude reads "
                f"and applies. {what} There are no numbered steps to walk; the "
                f"instruction set IS the behaviour."
            )
        return (
            f"{s['name']} has no numbered procedure. It is a reference Claude "
            f"reads and applies — the instruction set IS the behaviour."
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
    constraints = s.get("constraints", [])
    if constraints:
        return (
            f"Here is the design tell. {constraints[0]}. "
            f"That is the constraint in {s['name']} — not decoration, but a rule "
            f"that changes how Claude is supposed to act."
        )
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
        f"Claude's job: {_trim(desc, 100)}. "
        f"What it gets right: repeatable results. "
        f"What it bites: anything outside the spec."
    )

def _b04_narr(s: dict) -> str:
    refs = s.get("referenced_files", [])
    signals = s.get("code_signals", [])
    parts = []
    if refs:
        parts.append(f"supporting material: {', '.join(refs[:4])}")
    if signals:
        parts.append(f"implementation signals: {', '.join(signals[:3])}")
    if s.get("sections"):
        parts.append(f"sections: {', '.join(s['sections'][:4])}")
    if not parts:
        parts.append("the whole source is the frontmatter description plus the body instructions")
    return (
        f"The detail layer matters. In {s['name']}, "
        f"{'; '.join(parts)}. "
        f"That is what keeps the explanation tied to the actual skill, not a generic Claude demo."
    )

def _bvdt_narr(s: dict) -> str:
    desc = _trim(_clean(s["description"]), 80) if s["description"] else s["name"]
    return (
        f"{s['name']} makes Claude execute one task reliably. "
        f"The SKILL.md is the spec — {desc}. "
        f"Same input, same output, every run. Know the limit: only what the file says."
    )

def _bhtf_narr(s: dict) -> str:
    short = _trim(_clean(s["description"]), 80).rstrip("…").lower().rstrip(".") if s["description"] else f"use {s['name']}"
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
            {"label": _trim(st["title"], 30), "desc": _trim(st["body"] or "", 60), "accent": i == 0}
            for i, st in enumerate(steps[:4])
        ]
    else:
        phases = [
            {"label": "Read SKILL.md", "desc": "load the instruction set", "accent": True},
            {"label": "Execute",       "desc": "run each step in order",    "accent": False},
            {"label": "Return output", "desc": "deliver the result",        "accent": False},
        ]

    # Mechanism body (SkillTeardownMechanism)
    if skill.get("constraints"):
        mech_body = _clean(skill["constraints"][0])
    elif skill["notes"]:
        mech_body = _clean(skill["notes"][0])
    else:
        mech_body = _trim(_clean(skill["description"]), 200)
    detail_body = _trim("; ".join(
        (skill.get("capabilities") or [])[:3]
        + (skill.get("referenced_files") or [])[:3]
        + (skill.get("code_signals") or [])[:2]
    ), 220)

    # Verdict lines
    desc = _clean(skill["description"])
    verdict_lines = [
        f"Skill: {name} — Claude reads SKILL.md before acting",
        (_trim(desc, 90) if desc else f"Executes the {name} workflow reliably"),
    ]
    if steps:
        verdict_lines.append(
            f"{len(steps)}-step pipeline: {' → '.join(st['title'] for st in steps[:3])}"
        )
    elif skill.get("capabilities"):
        verdict_lines.append(f"Capabilities: {'; '.join(skill['capabilities'][:3])}")
    if skill.get("constraints"):
        verdict_lines.append(f"Constraint: {_trim(skill['constraints'][0], 90)}")
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
            _trim(desc, 80) if desc else f"Claude skill: {name}",
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
            f"I want to {_trim(_clean(skill['description']), 70).rstrip('…').lower().rstrip('.') if skill['description'] else f'use {name}'}. "
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
            "body":     _trim(mech_body, 200),
            "sparkLine": "This is the part worth knowing.",
        }, 28),
        _beat("B04", "detail layer",          _b04_narr(skill),  "SkillTeardownMechanism", {
            "eyebrow":  "SKILL · DETAIL LAYER",
            "heading":  "What the source actually names.",
            "body":     detail_body or _trim(_clean(skill["description"]), 200),
            "sparkLine": "Ground the reel in the file.",
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
            "source_detail": {
                "capabilities": skill.get("capabilities", []),
                "constraints": skill.get("constraints", []),
                "referenced_files": skill.get("referenced_files", []),
                "code_signals": skill.get("code_signals", []),
                "sections": skill.get("sections", []),
            },
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

def build_one(row: dict, dry_run: bool, force_sheet: bool, log_fh) -> str:
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

    # Already done? --force-sheet means intentionally regenerate the script layer.
    if reel_done(reel_dir, slug) and not force_sheet:
        say(f"SKIP — already compiled")
        return "skipped"
    if reel_done(reel_dir, slug) and force_sheet:
        say("already compiled — forcing deeper sheet/audio/render refresh")

    if dry_run:
        say(f"DRY RUN → {reel_dir.relative_to(BOOKS)}")
        return "skipped"

    # 1. Parse SKILL.md
    skill     = parse_skill_md(skill_md)
    skill_dir = skill_md.parent

    # 2. Scaffold reel directory
    for sub in ("mp3", "media", "mp4", "clips"):
        (reel_dir / sub).mkdir(parents=True, exist_ok=True)

    # 3. Write beat_sheet.json (skip if exists unless --force-sheet)
    bs_path = reel_dir / "beat_sheet.json"
    if force_sheet and bs_path.exists():
        backup = reel_dir / f"beat_sheet.pre-detail-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        backup.write_text(bs_path.read_text(encoding="utf-8"), encoding="utf-8")
        bs = make_beat_sheet(skill, skill_dir, slug)
        bs_path.write_text(json.dumps(bs, indent=2, ensure_ascii=False), encoding="utf-8")
        say(f"beat_sheet.json rewritten with deeper detail; backup: {backup.name}")
    elif not bs_path.exists():
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
    ap.add_argument("--force-sheet", action="store_true",
                    help="Rewrite existing beat_sheet.json files with the deeper source-detail template")
    args = ap.parse_args()

    rows    = parse_log(LOG_MD)
    target_rows = [r for r in rows
                   if args.start <= int(r["num"]) <= args.end
                   and ("pending" in r["status"] or args.force_sheet)]

    print(f"=== BUILD-SKILL-EXPLAINERS overnight batch ===")
    print(f"    target rows  : {len(target_rows)}")
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

        for row in target_rows:
            result = build_one(row, args.dry_run, args.force_sheet, log_fh)

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
