#!/usr/bin/env python3
"""Copy Claude/Anthropic-matching videos from across books/ into the 13
category folders under anthropics/youtube/, WITHOUT mp3/mp4 (and other A/V).
Non-destructive: skips any target slug that already exists. Logs everything."""
import json, os, subprocess, glob, sys

YT   = os.path.dirname(os.path.abspath(__file__))          # .../anthropics/youtube
BOOKS= os.path.abspath(os.path.join(YT, "..", ".."))        # .../books
CATS = {"behind-the-model","claude-agent-skills","claude-basics","claude-code",
        "claude-cowork","claude-for-education","claude-mcp-connectors","claude-news",
        "claude-plugins","claude-prompting","claude-research","claude-skills","claude-youtube"}

# Books whose every video is cleanly one category (book-titled)
CLEAN = {
 "claude-code-for-students":"claude-code",
 "claude-code-for-teachers":"claude-code",
 "claude-cowork":"claude-cowork",
 "claude-for-education-a-practitioners-guide":"claude-for-education",
 "claude-prompt-engineering":"claude-prompting",
}
# Mixed books: classify each video by its beat_sheet metadata
MIXED = ["claude","claude-agentic-ai","conducting-ai","validating-output-from-ai-systems"]
# Explicitly skipped source trees (non-Claude or toolkit working dir)
SKIP_BOOKS = {"brutalist-art","brutalist","brutalist_art","codex-for-students",
              "codex-for-teachers","github-copilot-cli-for-students",
              "github-copilot-cli-for-teachers"}

EXCLUDES = ["*.mp3","*.mp4","*.mov","*.wav","*.m4a","*.webm","*.aac","__pycache__",
            "node_modules",".git",".DS_Store"]

def classify(meta_text):
    t = meta_text.lower()
    rules = [
      ("claude-news",   ["release note","changelog","announc"," news","migration guide","opus 4","what's new"]),
      ("claude-mcp-connectors", ["mcp","connector","model context protocol"]),
      ("claude-plugins",["plugin","marketplace"]),
      ("claude-agent-skills", ["skill.md","agent skill","skill design","skill-creator"]),
      ("claude-skills", ["skill"]),
      ("claude-prompting", ["prompt","few-shot","chain-of-thought","precognition","xml tag","role-prompt","hallucinat"]),
      ("claude-code",  ["claude code","claude-code","subagent","cli","coding","commit","codebase","terminal","repository"]),
      ("claude-research", ["deep research","research agent","evidence synthesis","citation"]),
      ("claude-for-education", ["student","teacher","curriculum","classroom","education","medhavy"]),
      ("claude-cowork", ["cowork","knowledge work","connector","workflow","agentic loop","handoff","task packet"]),
      ("behind-the-model", ["constitution","alignment","eval","interpretab","reward","sycophan","deceiv",
                            "oversight","verification","verify","safety","supervision","model card","superposition",
                            "faithful","legitimacy","corrigib","power-seeking","error","omission","irony","oracle"]),
    ]
    for cat, kws in rules:
        if any(k in t for k in kws):
            return cat
    return None

def rsync(src, dst):
    cmd = ["rsync","-a","--ignore-existing"] + sum([["--exclude",e] for e in EXCLUDES],[]) + [src+"/", dst+"/"]
    subprocess.run(cmd, check=False)

copied, skipped_exist, unmatched, errors = [], [], [], []

def handle(video_dir, cat):
    slug = os.path.basename(video_dir)
    dst = os.path.join(YT, cat, slug)
    if os.path.exists(dst):
        skipped_exist.append(f"{cat}/{slug}"); return
    try:
        os.makedirs(dst, exist_ok=True)
        rsync(video_dir, dst)
        copied.append(f"{cat}/{slug}")
    except Exception as e:
        errors.append(f"{slug}: {e}")

# Clean book-level
for book, cat in CLEAN.items():
    for bs in glob.glob(os.path.join(BOOKS, book, "youtube", "*", "beat_sheet.json")):
        handle(os.path.dirname(bs), cat)

# Mixed: per-video classification
for book in MIXED:
    for bs in glob.glob(os.path.join(BOOKS, book, "youtube", "*", "beat_sheet.json")):
        vdir = os.path.dirname(bs)
        try:
            m = json.load(open(bs)).get("metadata", {})
            blob = " ".join(str(m.get(k,"")) for k in ("slug","title","subtitle","topic","one_idea","source"))
        except Exception:
            blob = os.path.basename(vdir)
        cat = classify(blob)
        if cat is None:
            unmatched.append(f"{book}/{os.path.basename(vdir)}")
        else:
            handle(vdir, cat)

log = os.path.join(YT, "_COPY-REPORT.md")
with open(log, "w") as f:
    f.write("# Copy report — matching videos consolidated into category folders\n\n")
    f.write(f"Copied: {len(copied)} · Skipped (already existed): {len(skipped_exist)} · "
            f"Unmatched (skipped): {len(unmatched)} · Errors: {len(errors)}\n\n")
    f.write("Excluded from every copy: mp3, mp4, mov, wav, m4a, webm, __pycache__.\n")
    f.write("Skipped source trees: brutalist-art (toolkit reels), codex-*, github-copilot-* (non-Claude).\n\n")
    for title, lst in [("COPIED",copied),("SKIPPED (target existed)",skipped_exist),
                       ("UNMATCHED (left in place)",unmatched),("ERRORS",errors)]:
        f.write(f"## {title} ({len(lst)})\n\n")
        for x in sorted(lst): f.write(f"- {x}\n")
        f.write("\n")
print("DONE copied=%d skipped_exist=%d unmatched=%d errors=%d" %
      (len(copied),len(skipped_exist),len(unmatched),len(errors)))
