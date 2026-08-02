#!/usr/bin/env python3
"""is-done scanner — find videos that look COMPLETELY DONE.

A video folder is <...>/youtube/<slug>/ containing beat_sheet.json.
"Done" = a rendered master mp4 + every beat filled + no leftover slates +
no blocking MISSING line in BUILD-LOG.md. Read-only; prints a JSON report.

Usage: python3 scan_done.py [root]
Default root: /Users/bear/Documents/CoWork/bear-textbooks/books
"""
import json, os, re, subprocess, sys, shutil

DEFAULT_ROOT = "/Users/bear/Documents/CoWork/bear-textbooks/books"
PRUNE = {"node_modules", ".git", "_to_delete", "__pycache__", ".venv"}
HAVE_FFPROBE = shutil.which("ffprobe") is not None


def find_video_dirs(root):
    """Every dir holding a beat_sheet.json that sits somewhere under a
    `youtube/` path. Handles both <book>/youtube/<slug>/ and the nested
    <book>/youtube/<category>/<slug>/ layout. Nested beat-sheet dirs (e.g.
    a `short/` variant inside a video) are dropped — only the outermost is
    kept."""
    cands = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in PRUNE]
        if "beat_sheet.json" in filenames:
            parts = dirpath.split(os.sep)
            if "youtube" in parts and os.path.basename(dirpath) != "youtube":
                cands.append(dirpath)
    cands.sort()
    kept = []
    for c in cands:
        if any(c != k and c.startswith(k + os.sep) for k in cands):
            continue  # nested inside another video folder -> variant, skip
        kept.append(c)
    for vd in kept:
        yield vd


MIN_MASTER = 500_000  # bytes; smaller mp4s are stubs / LFS pointers, not renders
# Substrings that mark an mp4 as NOT the finished master (previz/variant/partial)
BAD_MP4 = ("slate", "previz", "preview", "silent", "review", "-qc", "proxy",
           "draft", "temp", "-short", "short-", "test")


def _ok_master_name(fn):
    low = fn.lower()
    if low.startswith("beat-"):
        return False
    return not any(b in low for b in BAD_MP4)


def find_master(vd, slug):
    """Return (path, bytes) of the finished master render, or (None, 0).
    Excludes slate/previz/silent/short/beat stubs and anything <0.5 MB."""
    named = [f"mp4/{slug}.mp4", f"{slug}-final.mp4", f"{slug}-cut.mp4",
             f"{slug}.mp4", f"mp4/{slug}-final.mp4", f"mp4/{slug}-cut.mp4"]
    for rel in named:
        p = os.path.join(vd, rel)
        if os.path.isfile(p) and _ok_master_name(os.path.basename(p)) \
                and os.path.getsize(p) > MIN_MASTER:
            return p, os.path.getsize(p)
    # fallback: largest acceptable mp4 (skip the short/ variant subtree)
    best, best_sz = None, 0
    for dp, dn, fn in os.walk(vd):
        dn[:] = [d for d in dn if d not in PRUNE]
        if os.path.basename(dp) == "short":
            dn[:] = []
            continue
        for f in fn:
            if f.lower().endswith(".mp4") and _ok_master_name(f):
                p = os.path.join(dp, f)
                try:
                    sz = os.path.getsize(p)
                except OSError:
                    continue
                if sz > best_sz:
                    best, best_sz = p, sz
    if best and best_sz > MIN_MASTER:
        return best, best_sz
    return None, 0


def beats_status(bs):
    """Return (filled, total, slates_open, ok, note)."""
    m = bs.get("metadata", {}) or {}
    build = m.get("build", {}) or {}
    filled, total = build.get("filled"), build.get("of")
    slates = build.get("slates") or []
    if filled is not None and total is not None:
        ok = (filled >= total) and not slates
        return filled, total, len(slates), ok, ("cut=%s" % build.get("cut", "?"))
    # No build block: infer from beats — reject if any slate/placeholder beat
    beats = bs.get("beats", []) or []
    total = len(beats)
    open_slates = 0
    for b in beats:
        scene = str(b.get("scene", "")).lower()
        stype = str((b.get("shot", {}) or {}).get("type", "")).lower()
        narr = str(b.get("narration", "")).lower()
        if "slate" in scene or stype == "slate" or "[slate]" in narr or "[todo]" in narr:
            open_slates += 1
    ok = total > 0 and open_slates == 0
    return (total - open_slates), total, open_slates, ok, "no build block"


def has_missing_blocker(vd):
    log = os.path.join(vd, "BUILD-LOG.md")
    if not os.path.isfile(log):
        return False
    try:
        with open(log, errors="ignore") as f:
            for line in f:
                if re.match(r"\s*MISSING:", line):
                    return True
    except OSError:
        pass
    return False


def captions(vd, slug):
    for name in (f"{slug}.srt",):
        if os.path.isfile(os.path.join(vd, name)):
            return name
    for f in os.listdir(vd):
        if f.lower().endswith(".srt"):
            return f
    return None


def description(vd, slug):
    for name in ("description.txt", f"{slug}-youtube.md", f"{slug}.youtube.md"):
        if os.path.isfile(os.path.join(vd, name)):
            return name
    return None


def duration_s(path):
    if not HAVE_FFPROBE or not path:
        return None
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=20)
        return round(float(out.stdout.strip()), 1)
    except Exception:
        return None


def book_and_category(vd, root):
    rel = os.path.relpath(vd, root)
    parts = rel.split(os.sep)
    book = parts[0] if parts else ""
    cat = ""
    if "youtube" in parts:
        i = parts.index("youtube")
        if i + 1 < len(parts) - 1:  # a category folder sits between youtube and slug
            cat = parts[i + 1]
    return book, cat


def scan(root):
    done, almost = [], []
    for vd in find_video_dirs(root):
        slug = os.path.basename(vd)
        try:
            bs = json.load(open(os.path.join(vd, "beat_sheet.json"), errors="ignore"))
        except Exception:
            bs = {}
        m = bs.get("metadata", {}) or {}
        cut = str((m.get("build", {}) or {}).get("cut", "")).lower()
        previz_cut = cut in {"slate", "review", "scaffold", "previz", "draft"}
        master, mbytes = find_master(vd, slug)
        filled, total, open_slates, beats_ok, bnote = beats_status(bs)
        blocker = has_missing_blocker(vd)
        cap = captions(vd, slug)
        desc = description(vd, slug)
        book, cat = book_and_category(vd, root)
        title = m.get("title") or slug

        reasons, missing = [], []
        if master: reasons.append(f"master {os.path.basename(master)} ({mbytes//1_000_000}MB)")
        else: missing.append("no master mp4")
        if beats_ok: reasons.append(f"beats {filled}/{total}, no open slates ({bnote})")
        else: missing.append(f"beats {filled}/{total}, {open_slates} open slate(s)")
        if blocker: missing.append("BUILD-LOG has MISSING:")
        if previz_cut: missing.append(f"cut={cut} (not a final/master cut)")
        elif cut in {"master", "final"}: reasons.append(f"cut={cut}")
        if cap: reasons.append("captions")
        if desc: reasons.append("description")

        is_done = bool(master) and beats_ok and not blocker and not previz_cut
        item = dict(
            slug=slug, path=vd, book=book, category=cat, title=title,
            one_idea=m.get("one_idea", ""), cut=cut, master=master,
            master_bytes=mbytes,
            duration_s=duration_s(master) if is_done else None,
            beats_filled=filled, beats_total=total,
            captions=bool(cap), description=bool(desc),
            reasons=reasons)
        if is_done:
            conf = 3 + (1 if cap else 0) + (1 if desc else 0) \
                + (1 if item["duration_s"] else 0) \
                + (1 if cut in {"master", "final"} else 0)
            item["confidence"] = conf
            done.append(item)
        else:
            item["missing"] = missing
            almost.append(item)

    done.sort(key=lambda x: (x["confidence"], x["master_bytes"]), reverse=True)
    # almost: closest first (fewest missing), master-having ones ahead
    almost.sort(key=lambda x: (len(x["missing"]), 0 if x["master"] else 1))
    return dict(
        root=root, ffprobe=HAVE_FFPROBE,
        counts=dict(done=len(done), almost=len(almost)),
        done=done, almost=almost)


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ROOT
    if not os.path.isdir(root):
        print(json.dumps({"error": f"root not found: {root}"}));  sys.exit(1)
    print(json.dumps(scan(root), indent=2))
