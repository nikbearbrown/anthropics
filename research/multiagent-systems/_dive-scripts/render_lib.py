"""
Shared 4K figure-animation harness for the multiagent-systems deep dive.

Design constitution: books/brutalist-art/runtime/design/DESIGN.md
  palette   : teardown (white ground, warm-near-black ink, ONE accent = crimson)
  multi-series charts: Okabe-Ito categorical set (>=3 series rule)
  type floor: 14pt @1080 baseline == 37px on the 4K master
              at dpi=100 / figsize 38.4x21.6, 37px == 26.6pt -> nothing below 27pt.

Every clip is born at native 3840x2160 (show-more law: no upscaled births).
Silent by design — narration is added by the reel, not baked into the pantry asset.
"""
import subprocess, math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

W, H, FPS, DPI = 3840, 2160, 30, 100
FIGSIZE = (W / DPI, H / DPI)

# --- teardown palette -------------------------------------------------------
GROUND   = "#FFFFFF"
INK      = "#2A1A0E"
CRIMSON  = "#C8102E"          # the ONE accent — the mark under scrutiny
SLATE    = "#545454"
HAIRLINE = "#D4D4D4"
WASH     = "#F6D8DC"          # crimson @ ~14% — the editor's-pen sweep

# --- Okabe-Ito categorical (DESIGN.md data-viz law: 3+ series) --------------
# #F0E442 (yellow) is skipped: it fails legibility on a white ground.
# Deviation logged in the dive manifest.
OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]
MODEL_COLOR = {
    "Sonnet 4.6":     OKABE[2],   # sky blue
    "Sonnet 5":       OKABE[4],   # blue
    "Opus 4.6":       OKABE[3],   # bluish green
    "Opus 4.8":       OKABE[0],   # black
    "Mythos Preview": OKABE[1],   # orange
    "Mythos 5":       OKABE[5],   # vermillion
}

def _pick(*names, fallback="DejaVu Sans"):
    have = {f.name for f in font_manager.fontManager.ttflist}
    for n in names:
        if n in have:
            return n
    return fallback

DISPLAY = _pick("Montserrat")                       # titles, labels
SERIF   = _pick("EB Garamond", "EBGaramond")        # skeptic's-read caption
MONO    = _pick("PT Mono", "Liberation Mono")       # data numbers only

# type scale — all >= 27pt (the 4K floor)
FS_TITLE, FS_SUB, FS_AXIS, FS_TICK, FS_LEG, FS_ANN, FS_CAP = 66, 38, 36, 31, 31, 33, 36

plt.rcParams.update({
    "figure.facecolor": GROUND, "axes.facecolor": GROUND,
    "text.color": INK, "axes.labelcolor": INK,
    "xtick.color": SLATE, "ytick.color": SLATE,
    "axes.edgecolor": HAIRLINE, "font.family": DISPLAY,
    "axes.linewidth": 2.0, "xtick.major.width": 2.0, "ytick.major.width": 2.0,
    "xtick.major.size": 9, "ytick.major.size": 9,
})


def ease(t):
    """smoothstep 0..1"""
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def seg(frame, start_s, dur_s):
    """eased 0..1 progress of a phase starting at start_s lasting dur_s"""
    return ease((frame / FPS - start_s) / dur_s) if dur_s > 0 else 1.0


def fade_in(ax_or_fig_artists, a):
    for art in ax_or_fig_artists:
        art.set_alpha(a)


class Clip:
    """Pipes matplotlib frames straight into ffmpeg at native 4K."""

    def __init__(self, out_path, seconds):
        self.out = out_path
        self.n = int(seconds * FPS)
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        self.proc = subprocess.Popen(
            ["ffmpeg", "-y", "-loglevel", "error",
             "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS),
             "-i", "-", "-an",
             "-c:v", "libx264", "-preset", "medium", "-crf", "16",
             "-pix_fmt", "yuv420p", "-movflags", "+faststart", out_path],
            stdin=subprocess.PIPE)

    def push(self, fig):
        fig.canvas.draw()
        self.proc.stdin.write(np.asarray(fig.canvas.buffer_rgba()).tobytes())

    def close(self):
        self.proc.stdin.close()
        self.proc.wait()


def stagger(prog, i, n, lead=0.55):
    """Eased per-row reveal that is GUARANTEED to reach alpha 1.0 at prog==1."""
    return ease(prog * (1 + lead * (n - 1)) - i * lead)


def caption(fig, text, prog=1.0, y=0.055):
    """The skeptic's-read caption: serif, crimson rule, bottom of frame."""
    if prog <= 0:
        return
    fig.text(0.055, y, text, fontsize=FS_CAP, family=SERIF, style="italic",
             color=INK, alpha=prog, va="bottom", ha="left", wrap=True)
    fig.patches.append(plt.Rectangle(
        (0.048, y - 0.004), 0.004, 0.075 * prog, transform=fig.transFigure,
        facecolor=CRIMSON, edgecolor="none", alpha=prog, zorder=5))


def chip(fig, text, x=0.055, y=0.935, prog=1.0):
    """LabelChip — Montserrat tracked caps, white on the crimson block."""
    if prog <= 0:
        return
    fig.text(x, y, text.upper(), fontsize=FS_SUB, family=DISPLAY, weight="medium",
             color="white", alpha=prog, va="center", ha="left",
             bbox=dict(boxstyle="square,pad=0.45", facecolor=CRIMSON,
                       edgecolor="none", alpha=prog))


def titleblock(fig, title, sub=None, prog=1.0):
    if prog <= 0:
        return
    fig.text(0.055, 0.885, title, fontsize=FS_TITLE, family=DISPLAY, weight="bold",
             color=INK, alpha=prog, va="top", ha="left")
    if sub:
        fig.text(0.055, 0.828, sub, fontsize=FS_SUB, family=DISPLAY,
                 color=SLATE, alpha=prog, va="top", ha="left")


def stamp(fig, text="SOURCE: ANTHROPIC FRONTIER RED TEAM, AUG 2026 — VALUES READ FROM PUBLISHED FIGURE"):
    fig.text(0.955, 0.012, text, fontsize=27, family=MONO, color="#E2E0DD",
             va="bottom", ha="right")
