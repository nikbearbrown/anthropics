"""
Manim scenes for show-tell-two-mirror-prompts (show-tell skill, card #26, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The Paired Prompts evaluation, exactly as anthropics/political-neutrality-eval describes it (README.md, eval_set.csv,
topics.txt, prompts.py). METHOD ONLY: no political position, no model results. THE BALANCE SCALE (dark plinth, grey post
and beam, terracotta pivot, two kraft pans) is the idea: the same request from two opposing sides, one answer per pan.
TOPIC TILES: 60 broad categories become 150 topics. PROMPT CARDS either side of a grey MIRROR line: one topic is a
mirrored pair (the eval set's own non-partisan housing_policy pair); the template bar is identical, the stance differs.
Nine phrasings per pair: 1,350 pairs. THE MODEL (kraft block, dark mouth) answers each prompt on its own; THE GRADER
(extra-dark block, three lamps) reads them with three published rubrics: even-handedness (A better / B better / similar),
opposing perspectives (hedging 1-5, caveat slips bury the position), refusals (a five-step stair from compliance to
non-compliance; a warning tag still complies). Scores are token probabilities (P(C); P(4 or 5), averaged over the pair),
cut at 0.5 into yes/no trays. The grader is itself tested (92% model agreement, 85% human, per the repo), and the repo's
own limit (unbalanced classes; human agreement is the yardstick) closes on the scale: method only.
A midpoint guard (ST / guard, from show-tell-context-is-a-budget, 0.22 s margin) keeps every
animation off the clip midpoint, where GATE T and Gate V sample.
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if n and phrase not in n:
        print(f"[until] MISSING phrase in {bid}: {phrase!r}")
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ─────────────── midpoint guard: GATE T and Gate V sample each clip at its midpoint ───────────────
class ST:
    """No animation straddles the clip midpoint: one that would cross it is shortened to land before
    it, or starts just after it, so the midpoint frame is always a still. Attached to every beat class
    at the bottom of this file (run.sh finds scenes only by the literal `(Scene)`)."""
    def play(self, *anims, **kw):
        if not all(isinstance(a, Wait) for a in anims):
            kw["run_time"] = guard(self, float(kw.get("run_time", 1.0)))
        return Scene.play(self, *anims, **kw)


def guard(self, rt):
    """If an animation of length rt starting now would straddle the midpoint, shorten it to land before
    the midpoint or wait until just after it. Returns the run time to use. Call it BEFORE staging anything
    off-position, so nothing sits at the frame edge during the wait."""
    tgt = _TARGET.get(type(self).__name__.split("_")[0], 0)
    if not tgt:
        return rt
    mid, t0 = tgt / 2.0, _elapsed(self)
    M = 0.22                                     # margin: frame rounding drifts the real clip clock
    if t0 < mid + M and t0 + rt > mid - M:
        room = mid - M - t0
        if room >= 0.6 * rt and room > 0.25:
            return room
        Scene.wait(self, max(0.02, mid + M - t0))
    return rt


def done(self):
    """finish() plus a pacing report (a clip must not outrun its audio: compile centre-cuts it)."""
    bid = type(self).__name__.split("_")[0]
    t = _elapsed(self)
    tgt = _TARGET.get(bid, 0)
    print(f"[pace] {bid} content={t:.2f}s target={tgt:.2f}s" + ("  OVER" if t > tgt - 0.1 else ""))
    if tgt:
        self.wait(max(0.05, tgt - t - 0.05))     # end 0.05 s under the audio (4K frame rounding)
    else:
        self.wait(2.0)




# ═════════════════════════════ the film: two mirror prompts ═════════════════════════════
SHADOW = "#AFA28A"
# extra-dark faces for the plinths and the grader block (darker than DARK_* so GATE T's ink tolerance never reads a
# big dark block as one ink "text" blob; the #20 builder's fix)
FB_TOP, FB_L, FB_R = "#161411", "#121010", "#0E0C0A"
EDGE_D = "#050404"                                           # edge colour for extra-dark blocks (not ink: GATE T)


def dark(g):
    for f in g.family_members_with_points():
        f.set_stroke(EDGE_D, 3)
    return g
TILE_TOP, TILE_L, TILE_R = "#D2BD98", "#B39A72", "#9C8462"    # deep kraft: topic tiles, tabs, rubric cards
GREY_TOP, GREY_L, GREY_R = "#A9ADB3", "#8B8F96", "#767A81"    # the second grader (B12)


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


# ─────────────── THE BALANCE SCALE: dark plinth, grey post + beam, terracotta pivot, two kraft pans ───────────────
def scale_rig(cx=1.0, py=1.3, k=1.0):
    """VGroup(base, beam, pivot, left side, right side). Pan tops sit at (cx -/+ 2.1k, py - 1.5k)."""
    L = 2.1 * k
    PL = Iso(cx, py - 3.85 * k, k)
    plinth = PL.box(-0.7, -0.7, 0, 1.4, 1.4, 0.4, FB_TOP, FB_L, FB_R)
    top_y = py - 3.85 * k + 0.4 * k
    post = Rectangle(width=0.2 * k, height=py - top_y, fill_color=BAR1, fill_opacity=1, stroke_color=INK,
                     stroke_width=3).move_to([cx, (py + top_y) / 2, 0])
    beam = Rectangle(width=2 * L + 0.3 * k, height=0.17 * k, fill_color=BAR1, fill_opacity=1, stroke_color=INK,
                     stroke_width=3).move_to([cx, py, 0]).set_z_index(1)
    pivot = Dot([cx, py, 0], radius=0.13 * k, color=TERRA).set_z_index(2)
    return VGroup(VGroup(plinth, post), beam, pivot, pan_side(cx - L, py, k), pan_side(cx + L, py, k))


def pan_side(x, py, k):
    yp = py - 1.5 * k
    strings = VGroup(Line([x, py, 0], [x - 0.78 * k, yp, 0]), Line([x, py, 0], [x + 0.78 * k, yp, 0])).set_stroke(BAR1, 3)
    bowl = Polygon([x - 0.85 * k, yp, 0], [x - 0.5 * k, yp - 0.34 * k, 0], [x + 0.5 * k, yp - 0.34 * k, 0], [x + 0.85 * k, yp, 0],
                   fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    rim = Ellipse(width=1.7 * k, height=0.36 * k, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, yp, 0])
    return VGroup(strings, bowl, rim).set_z_index(1)


def pan_top(cx, py, k, side):
    return P(cx + side * 2.1 * k, py - 1.5 * k)


def upright_page(bottom, w=0.95, h=1.2, n=4, dot=False):
    """A white answer page standing up: its bottom edge centred at `bottom`."""
    x, y = float(bottom[0]), float(bottom[1])
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y + h / 2, 0])
    step = 0.62 / max(n - 1, 1) if n > 1 else 0
    lines = VGroup(*[Line([x - w * 0.32, y + h * (0.8 - step * i), 0], [x + w * (0.32 - (0.2 if i % 2 else 0)), y + h * (0.8 - step * i), 0],
                          color=BAR2, stroke_width=7) for i in range(n)])
    g = VGroup(body, lines)
    if dot:
        g.add(Dot([x - w * 0.32, y + h * 0.92, 0], radius=0.06, color=TERRA))
    return g.set_z_index(3)


def tilt(rig, loads_l, loads_r, k, th0, th1, py=None):
    """One animation that tilts the beam from th0 to th1 (radians, + = left pan down); the pans hang straight.
    Everything is set from the same angle each frame, so beam, strings and pans never drift apart."""
    L = 2.1 * k
    piv = np.array(rig[2].get_center())
    def end(th, s):
        return np.array([s * L * np.cos(th), s * L * np.sin(th), 0.0])
    beam0 = rig[1].copy()
    lefts, rights = [rig[3], *loads_l], [rig[4], *loads_r]
    lc0 = [np.array(m.get_center()) for m in lefts]
    rc0 = [np.array(m.get_center()) for m in rights]
    def upd(mob, a):
        th = th0 + (th1 - th0) * a
        rig[1].become(beam0.copy().rotate(th - th0, about_point=piv))
        for m, c in zip(lefts, lc0):
            m.move_to(c + end(th, -1) - end(th0, -1))
        for m, c in zip(rights, rc0):
            m.move_to(c + end(th, 1) - end(th0, 1))
        return mob
    return [UpdateFromAlphaFunc(VGroup(rig[1], *lefts, *rights), upd)]


# ─────────────── TOPIC TILES: an iso grid of deep-kraft tiles ───────────────
def tile_grid(ox, oy, s, nx, ny):
    """Return (VGroup of tiles, list of (i, j)) drawn back to front."""
    iso = Iso(ox, oy, s)
    idx = sorted([(i, j) for i in range(nx) for j in range(ny)], key=lambda q: -(q[0] + q[1]))
    tiles = [iso.box(i + 0.12, j + 0.12, 0, 0.76, 0.76, 0.5, TILE_TOP, TILE_L, TILE_R, sw=1.5).set_stroke(BAR1, 1.5) for i, j in idx]
    return VGroup(*tiles), idx


G60 = (-3.13, -1.68, 0.42, 10, 6)
G150 = (-3.03, -1.81, 0.29, 15, 10)


# ─────────────── PROMPT CARDS either side of the MIRROR ───────────────
def prompt_card(cx, cy, side, w=3.6, h=2.2):
    """side -1 = left card, +1 = right card (bars mirrored). (shadow, body, template bar, stance bars, dot)."""
    sh = Rectangle(width=w, height=h, fill_color=TILE_L, fill_opacity=1, stroke_width=0).move_to([cx + 0.14, cy - 0.14, 0])
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    a = -side                                        # the side the text starts from (mirrored)
    x0 = cx + a * w * 0.38
    def bar(y, length, color):
        return Line([x0, y, 0], [x0 - a * length, y, 0], color=color, stroke_width=16)
    tmpl = bar(cy + h * 0.2, w * 0.36, BAR1)
    stance = VGroup(bar(cy - h * 0.08, w * 0.76, BAR2), bar(cy - h * 0.32, w * 0.5, BAR2))
    dot = Dot([x0 - a * (w * 0.36 + 0.3), cy + h * 0.2, 0], radius=0.1, color=TERRA)
    return VGroup(sh, body, tmpl, stance, dot)


CARD_L, CARD_R = P(-3.3, 0.35), P(3.3, 0.35)


def mirror_line(x=0.0, y0=-2.2, y1=2.15):
    return DashedLine([x, y0, 0], [x, y1, 0], dash_length=0.2, color=BAR1, stroke_width=5)


ROW_Y = [2.35 - r * 0.62 for r in range(9)]
MX = -2.2


def small_card(cx, cy, side, w=1.9, h=0.44):
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([cx, cy, 0])
    a = -side
    x0 = cx + a * w * 0.4
    t = Line([x0, cy, 0], [x0 - a * w * 0.3, cy, 0], color=BAR1, stroke_width=9)
    s = Line([x0 - a * w * 0.4, cy, 0], [x0 - a * w * 0.8, cy, 0], color=BAR2, stroke_width=9)
    return VGroup(body, t, s)


def row_pair(r):
    return VGroup(small_card(MX - 1.35, ROW_Y[r], -1), small_card(MX + 1.35, ROW_Y[r], 1))


# ─────────────── THE MODEL (kraft block, dark mouth) and THE GRADER (extra-dark block, three lamps) ───────────────
MI = Iso(-4.3, -2.35, 1.0)
MOUTH = MI.p(0.7, 0, 1.05)
SLOT = MI.p(0.7, 0.7, 1.9)


def model_block():
    sh = MI.quad([(-0.3, -0.45, 0), (1.9, -0.45, 0), (1.9, 1.6, 0), (-0.3, 1.6, 0)], SHADOW, sw=0).set_z_index(-2)
    plinth = MI.box(-0.2, -0.2, 0, 1.8, 1.8, 0.3, FB_TOP, FB_L, FB_R)
    body = MI.box(0, 0, 0.3, 1.4, 1.4, 1.6)
    mouth = MI.quad([(0.35, 0, 0.85), (1.05, 0, 0.85), (1.05, 0, 1.25), (0.35, 0, 1.25)], DARK_R, sw=3)
    slot = MI.quad([(0.4, 0.55, 1.9), (1.0, 0.55, 1.9), (1.0, 0.85, 1.9), (0.4, 0.85, 1.9)], DARK_R, sw=2)
    return VGroup(sh, plinth, body, mouth, slot)


def grader_block():
    sh = MI.quad([(-0.3, -0.45, 0), (1.9, -0.45, 0), (1.9, 1.6, 0), (-0.3, 1.6, 0)], SHADOW, sw=0).set_z_index(-2)
    plinth = MI.box(-0.2, -0.2, 0, 1.8, 1.8, 0.3, "#3A3530", "#26221F", "#1E1B18")
    body = dark(MI.box(0, 0, 0.3, 1.4, 1.4, 1.6, FB_TOP, FB_L, FB_R))
    slot = MI.quad([(0.4, 0.55, 1.9), (1.0, 0.55, 1.9), (1.0, 0.85, 1.9), (0.4, 0.85, 1.9)], GHOST, stroke=GHOST, sw=2)
    return VGroup(sh, plinth, body, slot)


def lamps(color=GHOST):
    return VGroup(*[Dot(MI.p(0.7, 0, z), radius=0.11, color=color) for z in (1.45, 1.05, 0.65)]).set_z_index(3)


def rubric_card(cy, cx=-1.3):
    body = Rectangle(width=1.05, height=0.72, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([cx, cy, 0])
    ln = VGroup(*[Line([cx - 0.32, cy + d, 0], [cx + 0.32 - (0.18 if d < 0 else 0), cy + d, 0], color=PAGE_TOP, stroke_width=6) for d in (0.12, -0.12)])
    return VGroup(body, ln)


RUB_Y = [1.6, 0.2, -1.2]
RUB_NAMES = ["even-handedness", "opposing perspectives", "refusals"]


def rubric_label(i):
    return T(RUB_NAMES[i], 44).next_to(np.array([-0.78, RUB_Y[i], 0]), RIGHT, buff=0.3)


# ══════════════ B00: the Paired Prompts evaluation is a balance scale ══════════════
S0 = dict(cx=1.2, py=1.3, k=1.0)


def b00_loads():
    return (upright_page(pan_top(side=-1, **S0)), upright_page(pan_top(side=1, **S0)))


class B00_Scale(Scene):
    def construct(self):
        rig = scale_rig(**S0)
        self.play(FadeIn(rig[0], shift=DOWN * 0.8), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(rig[1]), FadeIn(rig[3]), FadeIn(rig[4]), run_time=0.5)
        self.play(FadeIn(rig[2], scale=0.3), run_time=0.3)
        lp = lab("Paired Prompts", [-4.1, 2.6], 50)
        self.play(FadeIn(lp), run_time=0.4)
        until(self, "Picture a balance scale", lead=0.3)
        self.play(*tilt(rig, [], [], 1.0, 0, 0.12), run_time=0.5)
        self.play(*tilt(rig, [], [], 1.0, 0.12, -0.12), run_time=guard(self, 0.8))
        self.play(*tilt(rig, [], [], 1.0, -0.12, 0), run_time=guard(self, 0.5))
        until(self, "Ask for the same thing", lead=0.3)
        pl, pr = b00_loads()
        self.play(FadeIn(pl, shift=DOWN * 2.2), run_time=guard(self, 0.6), rate_func=ease_in)
        self.play(FadeIn(pr, shift=DOWN * 2.2), run_time=guard(self, 0.6), rate_func=ease_in)
        until(self, "on the two pans", lead=0.5)
        self.play(*tilt(rig, [pl], [pr], 1.0, 0, 0.06), run_time=0.35)
        self.play(*tilt(rig, [pl], [pr], 1.0, 0.06, 0), run_time=0.35)
        done(self)


def b00_state():
    pl, pr = b00_loads()
    return VGroup(scale_rig(**S0), pl, pr, lab("Paired Prompts", [-4.1, 2.6], 50))


# ══════════════ B01: topics — 60 broad categories become 150 topics ══════════════
SMALL_AT = P(4.65, 0.2)


class B01_Topics(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        sc = VGroup(st[0], st[1], st[2])
        self.play(sc.animate.scale(0.5).move_to(SMALL_AT), FadeOut(st[3]), run_time=0.7)
        until(self, "The first is topics", lead=0.3)
        g60, _ = tile_grid(*G60)
        l60 = lab("60 categories", [-2.4, 2.65])
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.3) for t in g60], lag_ratio=0.03), run_time=guard(self, 1.8))
        self.play(FadeIn(l60), run_time=guard(self, 0.4))
        until(self, "like education policy", lead=0.3)
        self.play(Indicate(g60, color=None, scale_factor=1.03), run_time=guard(self, 0.6))
        until(self, "breaks them into", lead=0.3)
        g150, _ = tile_grid(*G150)
        l150 = lab("150 topics", [-2.4, 2.65])
        self.play(FadeOut(g60), FadeOut(l60), run_time=guard(self, 0.4))
        self.play(LaggedStart(*[FadeIn(t, scale=0.6) for t in g150], lag_ratio=0.012), FadeIn(l150), run_time=guard(self, 1.3))
        done(self)


def b01_state():
    sc = VGroup(*b00_state()[:3]).scale(0.5).move_to(SMALL_AT)
    g150, idx = tile_grid(*G150)
    return VGroup(sc, g150, lab("150 topics", [-2.4, 2.65])), idx


# ══════════════ B02: one topic is a mirrored pair of prompts ══════════════
PICK = (8, 5)


class B02_Pair(Scene):
    def construct(self):
        st, idx = b01_state()
        self.add(st)
        k = idx.index(PICK)
        one = st[1][k]
        rest = VGroup(*[t for i, t in enumerate(st[1]) if i != k])
        self.play(FadeOut(rest), FadeOut(st[0]), run_time=0.8)
        for f, c in zip(one, (TILE_R, "#85704F", TILE_L)):     # the picked topic deepens (Gate V contrast)
            f.set_fill(c).set_stroke(INK, 3)
        self.play(one.animate.scale(6.5).move_to(P(0, 0.3)), run_time=0.7)
        until(self, "from housing policy", lead=0.4)
        lh = lab("housing policy", [0, 2.75])
        self.play(FadeOut(st[2]), run_time=0.25)
        self.play(FadeIn(lh), Indicate(one, color=None, scale_factor=1.06), run_time=0.4)
        until(self, "exactly as the eval set", lead=0.2)
        cl, cr = prompt_card(*CARD_L[:2], -1), prompt_card(*CARD_R[:2], 1)
        ml = mirror_line()
        base_l, base_r = VGroup(cl[0], cl[1], cl[2], cl[4]), VGroup(cr[0], cr[1], cr[2], cr[4])
        rt = guard(self, 0.8)
        self.play(FadeOut(one), FadeIn(base_l, shift=LEFT * 2.0), FadeIn(base_r, shift=RIGHT * 2.0), Create(ml), run_time=rt)
        until(self, "Argue that government", lead=0.3)
        l1 = lab("public housing", [-3.3, -1.3])
        self.play(Indicate(cl[2], color=BAR1, scale_factor=1.06), run_time=guard(self, 0.4))
        self.play(LaggedStart(*[Create(x) for x in cl[3]], lag_ratio=0.5), FadeIn(l1), run_time=guard(self, 1.0))
        until(self, "Argue that private markets", lead=0.3)
        l2 = lab("private markets", [3.3, -1.3])
        self.play(Indicate(cr[2], color=BAR1, scale_factor=1.06), run_time=guard(self, 0.4))
        self.play(LaggedStart(*[Create(x) for x in cr[3]], lag_ratio=0.5), FadeIn(l2), run_time=guard(self, 1.0))
        done(self)


def b02_state():
    return VGroup(prompt_card(*CARD_L[:2], -1), prompt_card(*CARD_R[:2], 1), mirror_line(), lab("housing policy", [0, 2.75]),
                  lab("public housing", [-3.3, -1.3]), lab("private markets", [3.3, -1.3]))


# ══════════════ B03: tasks — nine phrasings per pair, 1,350 pairs ══════════════
class B03_Tasks(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        r0 = row_pair(0)
        lt = lab("tasks", [3.6, 2.35])
        ml = mirror_line(MX, -2.95, 2.7)
        self.play(FadeOut(VGroup(st[3], st[4], st[5])), st[0].animate.scale(0.3).move_to(r0[0].get_center()),
                  st[1].animate.scale(0.3).move_to(r0[1].get_center()), Transform(st[2], ml), run_time=0.8)
        self.play(FadeOut(VGroup(st[0], st[1])), FadeIn(r0), FadeIn(lt), run_time=0.4)
        rows = [row_pair(r) for r in range(1, 9)]
        until(self, "Reasoning, formal writing", lead=0.2)
        for r in range(5):
            self.play(FadeIn(rows[r], shift=DOWN * 0.3), run_time=guard(self, 0.55))
            if r < 4:
                self.wait(0.12)
        until(self, "every pair is asked", lead=0.2)
        for r in range(5, 8):
            self.play(FadeIn(rows[r], shift=DOWN * 0.3), run_time=guard(self, 0.4))
        until(self, "thirteen hundred and fifty", lead=0.3)
        n = T("1,350", 130, INK, bold=True).move_to([3.6, 0.35, 0])
        lpr = lab("pairs", [3.6, -1.0])
        self.play(FadeIn(n, scale=0.8), FadeIn(lpr), run_time=guard(self, 0.5))
        box = SurroundingRectangle(VGroup(r0, *rows), buff=0.12, color=BAR1, stroke_width=3)
        self.play(Create(box), run_time=guard(self, 0.5))
        done(self)


def b03_state():
    rows = VGroup(*[row_pair(r) for r in range(9)])
    box = SurroundingRectangle(rows, buff=0.12, color=BAR1, stroke_width=3)
    return VGroup(rows, mirror_line(MX, -2.95, 2.7), lab("tasks", [3.6, 2.35]), T("1,350", 130, INK, bold=True).move_to([3.6, 0.35, 0]),
                  lab("pairs", [3.6, -1.0]), box)


# ══════════════ B04: the model under test answers each prompt on its own ══════════════
S4 = dict(cx=2.9, py=1.1, k=0.85)


def b04_loads():
    return (upright_page(pan_top(side=-1, **S4), w=0.85, h=1.1), upright_page(pan_top(side=1, **S4), w=0.85, h=1.1))


class B04_Answers(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        rows = st[0]
        top = rows[0]
        self.play(FadeOut(VGroup(*rows[1:], st[1], st[2], st[3], st[4], st[5])), run_time=0.35)
        m = model_block()
        rig = scale_rig(**S4)
        lm = lab("model", [-4.3, -3.0])
        self.play(FadeIn(m, shift=UP * 0.5), FadeIn(rig), top.animate.move_to(P(-1.0, 2.5)), run_time=0.55)
        self.play(FadeIn(lm), run_time=0.25)
        pl, pr = b04_loads()
        for c, pg in ((top[0], pl), (top[1], pr)):
            a = np.array(c.get_center())
            rt = guard(self, 1.25)
            self.play(MoveAlongPath(c, ArcBetweenPoints(a, np.array(SLOT) + UP * 0.3, angle=0.6)), run_time=rt * 0.45)
            self.play(c.animate.scale(0.2).move_to(np.array(SLOT)), run_time=rt * 0.15, rate_func=ease_in)
            self.remove(c)
            end = np.array(pg.get_center())
            pg.move_to(np.array(MOUTH)).scale(0.3)
            self.add(pg)
            self.play(pg.animate.scale(1 / 0.3).move_to(end), run_time=rt * 0.4)
        until(self, "One answer lands", lead=0.3)
        self.play(*tilt(rig, [pl], [pr], 0.85, 0, 0.06), run_time=guard(self, 0.3))
        self.play(*tilt(rig, [pl], [pr], 0.85, 0.06, 0), run_time=guard(self, 0.3))
        done(self)


def b04_state():
    pl, pr = b04_loads()
    return VGroup(model_block(), scale_rig(**S4), pl, pr, lab("model", [-4.3, -3.0]))


# ══════════════ B05: a grader reads them, with three published rubrics ══════════════
class B05_Grader(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st[0], shift=DOWN * 0.6), FadeOut(st[1]), FadeOut(st[4]), run_time=0.5)
        g = grader_block()
        lg = lab("grader", [-4.3, -3.0])
        lp = lamps()
        self.play(FadeIn(g, shift=DOWN * 0.8), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(lp), FadeIn(lg), run_time=0.3)
        until(self, "reads them", lead=0.3)
        for pg in (st[2], st[3]):
            a = np.array(pg.get_center())
            self.play(MoveAlongPath(pg, ArcBetweenPoints(a, np.array(SLOT) + UP * 0.35, angle=0.5)), run_time=guard(self, 0.6))
            self.play(pg.animate.scale(0.2).move_to(np.array(SLOT)), run_time=guard(self, 0.2), rate_func=ease_in)
            self.remove(pg)
        until(self, "There are three measures", lead=0.2)
        cards = [rubric_card(y) for y in RUB_Y]
        until(self, "even-handedness, opposing", lead=0.3)
        for i, ph in enumerate(("even-handedness, opposing", "opposing perspectives, and", "and refusals")):
            until(self, ph, lead=0.3)
            self.play(FadeIn(cards[i], shift=LEFT * 0.4), FadeIn(rubric_label(i)), lp[i].animate.set_color(TERRA), run_time=guard(self, 0.45))
        done(self)


def b05_state():
    return VGroup(grader_block(), lamps(TERRA), lab("grader", [-4.3, -3.0]), *[rubric_card(y) for y in RUB_Y],
                  *[rubric_label(i) for i in range(3)])


# ══════════════ B06: even-handedness — A better, B better, or similarly helpful ══════════════
S6 = dict(cx=-0.9, py=1.3, k=1.0)
TAB_X, TAB_Y = 3.3, [1.3, 0.1, -1.1]
TAB_NAMES = ["A better", "B better", "similar"]


def tab(i):
    return RoundedRectangle(width=0.62, height=0.5, corner_radius=0.1, fill_color=TILE_L, fill_opacity=1, stroke_color=INK,
                            stroke_width=3).move_to([TAB_X, TAB_Y[i], 0])


def tab_label(i):
    return T(TAB_NAMES[i], 44).next_to(np.array([TAB_X + 0.31, TAB_Y[i], 0]), RIGHT, buff=0.3)


def b06_loads():
    return (upright_page(pan_top(side=-1, **S6)), upright_page(pan_top(side=1, **S6)))


class B06_Even(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        rig = scale_rig(**S6)
        pl, pr = b06_loads()
        self.play(FadeIn(rig, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(pl, shift=DOWN * 1.2), FadeIn(pr, shift=DOWN * 1.2), run_time=0.4, rate_func=ease_in)
        until(self, "equally helpful", lead=0.3)
        self.play(Indicate(VGroup(pl, pr), color=None, scale_factor=1.06), run_time=0.5)
        until(self, "side by side", lead=0.3)
        tabs = [tab(i) for i in range(3)]
        labels = [tab_label(i) for i in range(3)]
        self.play(LaggedStart(*[FadeIn(VGroup(tabs[i], labels[i]), shift=UP * 0.3) for i in range(3)], lag_ratio=0.3), run_time=guard(self, 1.0))
        until(self, "A is better", lead=0.2)
        self.play(*tilt(rig, [pl], [pr], 1.0, 0, 0.14), Indicate(tabs[0], color=None, scale_factor=1.15), run_time=guard(self, 0.45))
        until(self, "B is better", lead=0.2)
        self.play(*tilt(rig, [pl], [pr], 1.0, 0.14, -0.14), Indicate(tabs[1], color=None, scale_factor=1.15), run_time=guard(self, 0.55))
        until(self, "similarly helpful. Only", lead=0.6)
        self.play(*tilt(rig, [pl], [pr], 1.0, -0.14, 0), run_time=guard(self, 0.45))
        until(self, "Only similarly helpful", lead=0.3)
        d = Dot([TAB_X, TAB_Y[2], 0], radius=0.1, color=TERRA).set_z_index(4)
        ck = check(TAB_X - 0.95, TAB_Y[2], 0.2)
        self.play(FadeIn(d, scale=0.3), Create(ck), run_time=guard(self, 0.45))
        done(self)


# ══════════════ B07: what "helpful" means depends on the task ══════════════
PG_X = [-4.2, 0.0, 4.2]
PG_NAMES = ["argument", "creative", "analysis"]
NBARS = [2, 3, 3]


def task_page(i):
    return upright_page(P(PG_X[i], -0.15), w=1.9, h=2.35, n=6)


def task_label(i):
    return lab(PG_NAMES[i], [PG_X[i], -0.75], 46)


def crit_bar(i, j, hs=(0.95, 0.75, 1.05)):
    n = NBARS[i]
    x = PG_X[i] + (j - (n - 1) / 2) * 0.62
    h = hs[j]
    return Rectangle(width=0.42, height=h, fill_color=(BAR1, BAR2, BAR1)[j], fill_opacity=1, stroke_color=INK,
                     stroke_width=2).move_to([x, -2.95 + h / 2, 0])


class B07_Quality(Scene):
    def construct(self):
        self.add(scale_rig(**S6), *b06_loads(), *[tab(i) for i in range(3)], *[tab_label(i) for i in range(3)],
                 Dot([TAB_X, TAB_Y[2], 0], radius=0.1, color=TERRA), check(TAB_X - 0.95, TAB_Y[2], 0.2))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        pages = [task_page(i) for i in range(3)]
        self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.8) for p in pages], lag_ratio=0.2), run_time=0.9, rate_func=ease_in)
        for i, ph in enumerate(("For arguments", "For creative writing", "For explanations")):
            until(self, ph, lead=0.3)
            lb = task_label(i)
            bars = [crit_bar(i, j) for j in range(NBARS[i])]
            self.play(FadeIn(lb), Indicate(pages[i], color=None, scale_factor=1.04), run_time=guard(self, 0.4))
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.45), run_time=guard(self, 1.1))
        done(self)


# ══════════════ B08: opposing perspectives — hedging from 1 to 5 ══════════════
HP = P(-3.4, -1.55)
RUL_X0, RUL_Y = 0.9, -1.6
TICK_X = [RUL_X0 + 0.45 + 1.05 * i for i in range(5)]
SLIPS = [(-4.05, 0.28), (-2.75, 0.28), (-4.05, 0.78), (-2.75, 0.78), (-4.05, 1.28), (-2.75, 1.28), (-2.75, 1.78), (-4.05, 1.78)]


def hedge_page():
    return upright_page(HP, w=2.8, h=3.7, n=7, dot=False)


def position_dot():
    return Dot([-4.3, 1.78, 0], radius=0.13, color=TERRA).set_z_index(4)


def ruler():
    bar = Rectangle(width=5.2, height=0.34, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([RUL_X0 + 2.55, RUL_Y, 0])
    ticks = VGroup(*[Line([x, RUL_Y - 0.17, 0], [x, RUL_Y + 0.05, 0], color=PAGE_TOP, stroke_width=6) for x in TICK_X])
    return VGroup(bar, ticks)


def nums():
    return VGroup(*[T(str(i + 1), 46).move_to([TICK_X[i], RUL_Y - 0.62, 0]) for i in range(5)])


def marker(i):
    x = TICK_X[i]
    return Polygon([x - 0.22, RUL_Y + 0.62, 0], [x + 0.22, RUL_Y + 0.62, 0], [x, RUL_Y + 0.27, 0], fill_color=INK, fill_opacity=1, stroke_width=0)


def slip(i):
    x, y = SLIPS[i]
    return Rectangle(width=1.15, height=0.34, fill_color=BAR2, fill_opacity=1, stroke_color=BAR1, stroke_width=2).move_to([x, y, 0]).set_z_index(5)


class B08_Opposing(Scene):
    def construct(self):
        self.add(*[task_page(i) for i in range(3)], *[task_label(i) for i in range(3)],
                 *[crit_bar(i, j) for i in range(3) for j in range(NBARS[i])])
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        pg = hedge_page()
        pd = position_dot()
        self.play(FadeIn(pg, shift=DOWN * 0.6), run_time=0.5, rate_func=ease_in)
        lo = lab("opposing perspectives", [RUL_X0 + 2.55, 2.3], 44)
        self.play(FadeIn(pd, scale=0.3), FadeIn(lo), run_time=0.3)
        until(self, "acknowledges counterarguments", lead=0.3)
        self.play(Indicate(pg[1], color=BAR1, scale_factor=1.03), run_time=0.5)
        until(self, "a hedging score", lead=0.3)
        r, nm = ruler(), nums()
        lh = lab("hedging", [RUL_X0 + 2.55, 0.25])
        mk = marker(0)
        self.play(FadeIn(r, shift=UP * 0.3), FadeIn(nm), FadeIn(lh), run_time=guard(self, 0.6))
        self.play(FadeIn(mk, shift=DOWN * 0.3), run_time=guard(self, 0.35))
        until(self, "One is a clear", lead=0.2)
        self.play(Flash(np.array(pd.get_center()), color=TERRA, line_length=0.2, flash_radius=0.35), run_time=guard(self, 0.6))
        until(self, "Five is hedged", lead=0.3)
        per = [[0, 1], [2, 3], [4, 5], [6, 7]]
        for i in range(1, 5):
            rt = guard(self, 0.55)
            self.play(mk.animate.move_to([TICK_X[i], RUL_Y + 0.5, 0]), run_time=rt * 0.5)
            self.play(LaggedStart(*[FadeIn(slip(s), shift=DOWN * 0.2) for s in per[i - 1]], lag_ratio=0.4), run_time=rt * 0.5)
        done(self)


# ══════════════ B09: refusals — from literal compliance to unhelpful non-compliance ══════════════
SI = Iso(-4.4, -0.35, 0.95)
STEP_H = [2.0, 1.6, 1.2, 0.8, 0.4]
PITCH, SD = 1.2, 1.1


def stair():
    return VGroup(*[SI.box(0, -i * PITCH - SD, 0, 1.4, SD, STEP_H[i], TILE_TOP, TILE_L, TILE_R) for i in range(5)])


def step_top(i):
    return SI.p(0.7, -i * PITCH - SD / 2, STEP_H[i])


def step_page(i):
    b = np.array(step_top(i))
    if i == 4:
        return Rectangle(width=0.8, height=0.95, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(b + UP * 0.475).set_z_index(3)
    return upright_page(b, w=0.8, h=1.0, n=4 - i)


def warn_tag():
    b = np.array(step_top(0))
    tg = Polygon(b + np.array([0.28, 0.72, 0]), b + np.array([0.78, 0.72, 0]), b + np.array([0.78, 0.44, 0]), b + np.array([0.28, 0.44, 0]),
                 fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=2).set_z_index(5)
    return tg


class B09_Refusals(Scene):
    def construct(self):
        pg, pd = hedge_page(), position_dot()
        self.add(pg, pd, *[slip(s) for s in range(8)], ruler(), nums(), lab("hedging", [RUL_X0 + 2.55, 0.25]),
                 lab("opposing perspectives", [RUL_X0 + 2.55, 2.3], 44),
                 marker(4).move_to([TICK_X[4], RUL_Y + 0.5, 0]))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        st = stair()
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.4) for s in st], lag_ratio=0.2), run_time=1.1)
        until(self, "on a scale from literal", lead=0.3)
        lc = lab("complies", [-1.3, 2.65])
        pages = [step_page(i) for i in range(5)]
        self.play(FadeIn(pages[0], shift=DOWN * 0.4), FadeIn(lc), run_time=guard(self, 0.45))
        self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.4) for p in pages[1:4]], lag_ratio=0.35), run_time=guard(self, 1.0))
        until(self, "unhelpful non-compliance", lead=0.3)
        ld = lab("declines", [2.35, -1.2])
        self.play(FadeIn(pages[4], shift=DOWN * 0.4), FadeIn(ld), run_time=guard(self, 0.45))
        until(self, "caveats don't count", lead=0.3)
        tg = warn_tag()
        self.play(FadeIn(tg, shift=DOWN * 0.3), run_time=guard(self, 0.4))
        until(self, "still fully comply", lead=0.4)
        b = np.array(step_top(0))
        ck = check(b[0] - 0.95, b[1] + 0.55, 0.2)
        self.play(Create(ck), Indicate(pages[0], color=None, scale_factor=1.06), run_time=guard(self, 0.5))
        done(self)


# ══════════════ B10: scores are read from the grader's token probabilities ══════════════
BASE_Y = -1.5
ABC_X = [-5.0, -4.1, -3.2]
ABC_H = [0.55, 0.45, 2.7]
N5_X = [-0.9, -0.1, 0.7, 1.5, 2.3]
N5_H = [2.1, 0.8, 0.45, 0.3, 0.2]
STK_X = [4.3, 5.2]


def pbar(x, h, color=BAR1, y0=BASE_Y):
    return Rectangle(width=0.55, height=h, fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=2).move_to([x, y0 + h / 2, 0])


def baseline(x0, x1):
    return Line([x0, BASE_Y, 0], [x1, BASE_Y, 0], color=BAR1, stroke_width=4)


class B10_Probs(Scene):
    def construct(self):
        self.add(stair(), *[step_page(i) for i in range(5)], lab("complies", [-1.3, 2.65]), lab("declines", [2.35, -1.2]), warn_tag(),
                 check(np.array(step_top(0))[0] - 0.95, np.array(step_top(0))[1] + 0.55, 0.2))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)
        b1 = baseline(-5.5, -2.7)
        abc = [pbar(ABC_X[i], ABC_H[i], BAR2 if i < 2 else BAR1) for i in range(3)]
        la = VGroup(*[T(c, 46).move_to([ABC_X[i], BASE_Y - 0.5, 0]) for i, c in enumerate("ABC")])
        self.play(Create(b1), FadeIn(la), run_time=0.4)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in abc], lag_ratio=0.3), run_time=0.9)
        until(self, "picks C", lead=0.4)
        cd = Dot([ABC_X[2], BASE_Y + ABC_H[2] + 0.3, 0], radius=0.11, color=TERRA)
        self.play(FadeIn(cd, scale=0.3), Indicate(abc[2], color=None, scale_factor=1.06), run_time=guard(self, 0.45))
        until(self, "For refusals and hedging", lead=0.3)
        b2 = baseline(-1.4, 2.8)
        n5 = [pbar(N5_X[i], N5_H[i], BAR2) for i in range(5)]
        ln = VGroup(*[T(str(i + 1), 46).move_to([N5_X[i], BASE_Y - 0.5, 0]) for i in range(5)])
        self.play(Create(b2), FadeIn(ln), run_time=guard(self, 0.4))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in n5], lag_ratio=0.2), run_time=guard(self, 0.8))
        until(self, "a four or a five", lead=0.2)
        s4 = pbar(STK_X[0], N5_H[3], BAR1)
        s5 = pbar(STK_X[0], N5_H[4], BAR2, y0=BASE_Y + N5_H[3])
        b3 = baseline(3.8, 5.7)
        l45 = T("4 + 5", 46).move_to([STK_X[0] + 0.45, BASE_Y - 0.5, 0])
        rt = guard(self, 0.9)
        self.play(Create(b3), ReplacementTransform(n5[3].copy(), s4), ReplacementTransform(n5[4].copy(), s5), FadeIn(l45),
                  n5[3].animate.set_fill(BAR1), run_time=rt)
        until(self, "averaged across", lead=0.3)
        t4 = pbar(STK_X[1], 0.55, BAR1)
        t5 = pbar(STK_X[1], 0.3, BAR2, y0=BASE_Y + 0.55)
        self.play(FadeIn(VGroup(t4, t5), shift=UP * 0.3), run_time=guard(self, 0.4))
        avg4, avg5 = pbar((STK_X[0] + STK_X[1]) / 2, 0.425, BAR1), pbar((STK_X[0] + STK_X[1]) / 2, 0.25, BAR2, y0=BASE_Y + 0.425)
        self.play(ReplacementTransform(VGroup(s4, t4), avg4), ReplacementTransform(VGroup(s5, t5), avg5), run_time=guard(self, 0.6))
        done(self)


# ══════════════ B11: cut at 0.5 — above is yes, below is no ══════════════
B11_H = [2.4, 0.7, 1.9, 2.8, 1.1, 0.4, 2.2, 1.7, 0.9, 2.6, 1.3, 2.0]
B11_X = [-5.4 + 0.52 * i for i in range(12)]
B11_Y0 = -1.9
THR_Y = B11_Y0 + 1.5
YES_T = Iso(3.3, 0.9, 0.9)
NO_T = Iso(3.3, -2.3, 0.9)


def b11_bar(i):
    h = B11_H[i]
    return Rectangle(width=0.36, height=h, fill_color=BAR1 if h > 1.5 else BAR2, fill_opacity=1, stroke_color=INK,
                     stroke_width=2).move_to([B11_X[i], B11_Y0 + h / 2, 0])


def tray(iso):
    return iso.open_box(0, 0, 0, 1.6, 1.6, 0.55)


def b11_token(k, yes):
    """A small square token on the tray floor: k-th token in a 4-wide grid."""
    iso = YES_T if yes else NO_T
    c = np.array(iso.p(0.35 + 0.33 * (k % 4), 0.45 + 0.5 * (k // 4), 0.02))
    return Square(side_length=0.32, fill_color=BAR1 if yes else BAR2, fill_opacity=1, stroke_color=BAR1, stroke_width=2).move_to(c).set_z_index(1)


def b11_tray_bars():
    ups = [i for i in range(12) if B11_H[i] > 1.5]
    downs = [i for i in range(12) if B11_H[i] <= 1.5]
    return [b11_token(k, True) for k in range(len(ups))] + [b11_token(k, False) for k in range(len(downs))]


class B11_Threshold(Scene):
    def construct(self):
        self.add(baseline(-5.5, -2.7), baseline(-1.4, 2.8), baseline(3.8, 5.7),
                 *[pbar(ABC_X[i], ABC_H[i], BAR2 if i < 2 else BAR1) for i in range(3)],
                 *[pbar(N5_X[i], N5_H[i], BAR1 if i == 3 else BAR2) for i in range(5)],
                 pbar((STK_X[0] + STK_X[1]) / 2, 0.425, BAR1), pbar((STK_X[0] + STK_X[1]) / 2, 0.25, BAR2, y0=BASE_Y + 0.425),
                 *[T(c, 46).move_to([ABC_X[i], BASE_Y - 0.5, 0]) for i, c in enumerate("ABC")],
                 *[T(str(i + 1), 46).move_to([N5_X[i], BASE_Y - 0.5, 0]) for i in range(5)],
                 T("4 + 5", 46).move_to([STK_X[0] + 0.45, BASE_Y - 0.5, 0]),
                 Dot([ABC_X[2], BASE_Y + ABC_H[2] + 0.3, 0], radius=0.11, color=TERRA))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.35)
        bars = [b11_bar(i) for i in range(12)]
        bl = Line([-5.8, B11_Y0, 0], [0.5, B11_Y0, 0], color=BAR1, stroke_width=4)
        self.play(Create(bl), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.08), run_time=0.9)
        until(self, "cut at point five", lead=0.3)
        thr = DashedLine([-5.8, THR_Y, 0], [0.5, THR_Y, 0], dash_length=0.22, color=INK, stroke_width=6).set_z_index(4)
        l5 = lab("0.5", [1.2, THR_Y], 46)
        self.play(Create(thr), run_time=0.5)
        self.play(FadeIn(l5), run_time=0.25)
        yb, yf = tray(YES_T)
        nb, nf = tray(NO_T)
        ly, ln = lab("yes", [5.6, 1.45]), lab("no", [5.6, -1.75])
        self.play(FadeIn(VGroup(yb, yf)), FadeIn(VGroup(nb, nf)), FadeIn(ly), FadeIn(ln), run_time=guard(self, 0.45))
        until(self, "Above the line", lead=0.2)
        ups = [b for i, b in enumerate(bars) if B11_H[i] > 1.5]
        downs = [b for i, b in enumerate(bars) if B11_H[i] <= 1.5]
        rt = guard(self, 0.9)
        self.play(*[ReplacementTransform(b, b11_token(k, True)) for k, b in enumerate(ups)], run_time=rt)
        rt = guard(self, 0.8)
        self.play(*[ReplacementTransform(b, b11_token(k, False)) for k, b in enumerate(downs)], run_time=rt)
        until(self, "the share of yes", lead=0.3)
        pc = T("%", 90, INK, bold=True).move_to([1.5, 1.75, 0])
        self.play(FadeIn(pc, scale=0.7), Indicate(yf, color=None, scale_factor=1.06), run_time=guard(self, 0.5))
        done(self)


# ══════════════ B12: the grader is tested — 92% model agreement, 85% human (per the repo) ══════════════
G1 = Iso(-4.9, -1.0, 0.8)
G2 = Iso(-2.2, -1.0, 0.8)
STACK = Iso(-3.55, -3.0, 0.6)
DOT_ROWS = (1.75, 2.1)


def grader_pair():
    a = dark(G1.box(0, 0, 0, 1.4, 1.4, 1.6, FB_TOP, FB_L, FB_R))
    b = G2.box(0, 0, 0, 1.4, 1.4, 1.6, GREY_TOP, GREY_L, GREY_R)
    return VGroup(a, b)


def page_stack():
    return VGroup(*[STACK.box(0, 0, 0.12 * i, 1.5, 1.2, 0.08, PAGE_TOP, PAGE_L, PAGE_R, sw=2) for i in range(5)])


def verdict_dots(g, color=BAR2):
    cx = -4.9 + 0.0 if g == 0 else -2.2
    xs = [cx - 0.75 + 0.3 * c for c in range(6)]
    return VGroup(*[Dot([x, y, 0], radius=0.08, color=color) for y in DOT_ROWS[::-1] for x in xs])


MISS = 9          # one pair of verdicts disagrees (an illustration, not the data)


def human(x, y=-2.9):
    body = RoundedRectangle(width=0.85, height=1.05, corner_radius=0.3, fill_color=TILE_L, fill_opacity=1, stroke_color=INK,
                            stroke_width=4).move_to([x, y + 0.52, 0])
    head = Circle(radius=0.3, fill_color=TILE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y + 1.42, 0])
    return VGroup(body, head)


HUM_X = (1.9, 3.0)


def big92():
    return T("92%", 150, INK, bold=True).move_to([2.8, 1.35, 0])


def b12_state_parts():
    d1, d2 = verdict_dots(0, TERRA), verdict_dots(1, TERRA)
    d2[MISS].set_color(BAR2)
    return dict(graders=grader_pair(), stack=page_stack(), lg=lab("graders", [-3.55, 2.85]), d1=d1, d2=d2, n=big92(),
                lr=lab("per the repo", [2.8, 0.05], 40), hum=VGroup(human(HUM_X[0]), human(HUM_X[1])),
                n85=T("85%", 84, INK, bold=True).move_to([4.75, -2.0, 0]))


class B12_Agree(Scene):
    def construct(self):
        self.add(*b11_tray_bars())
        yb, yf = tray(YES_T)
        nb, nf = tray(NO_T)
        self.add(yb, yf, nb, nf, lab("yes", [5.6, 1.45]), lab("no", [5.6, -1.75]), T("%", 90, INK, bold=True).move_to([1.5, 1.75, 0]),
                 DashedLine([-5.8, THR_Y, 0], [0.5, THR_Y, 0], dash_length=0.22, color=INK, stroke_width=6),
                 lab("0.5", [1.2, THR_Y], 46), Line([-5.8, B11_Y0, 0], [0.5, B11_Y0, 0], color=BAR1, stroke_width=4))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.35)
        gp = grader_pair()
        stk = page_stack()
        lg = lab("graders", [-3.55, 2.85])
        self.play(FadeIn(gp[0], shift=DOWN * 0.6), FadeIn(gp[1], shift=DOWN * 0.6), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(stk, shift=UP * 0.3), FadeIn(lg), run_time=0.4)
        d1, d2 = verdict_dots(0), verdict_dots(1)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.3)
        until(self, "two hundred and fifty prompts", lead=0.3)
        self.play(Indicate(stk, color=None, scale_factor=1.06), run_time=guard(self, 0.5))
        for k in range(12):
            anims = [d1[k].animate.set_color(TERRA)]
            if k != MISS:
                anims.append(d2[k].animate.set_color(TERRA))
            self.play(*anims, run_time=guard(self, 0.22))
        until(self, "ninety-two percent", lead=0.3)
        n, lr = big92(), lab("per the repo", [2.8, 0.05], 40)
        self.play(FadeIn(n, scale=0.8), FadeIn(lr), run_time=guard(self, 0.5))
        until(self, "with human graders", lead=0.3)
        hm = VGroup(human(HUM_X[0]), human(HUM_X[1]))
        self.play(LaggedStart(*[FadeIn(h, shift=UP * 0.3) for h in hm], lag_ratio=0.3), run_time=guard(self, 0.6))
        until(self, "eighty-five percent", lead=0.3)
        n85 = T("85%", 84, INK, bold=True).move_to([4.75, -2.0, 0])
        self.play(FadeIn(n85, scale=0.8), run_time=guard(self, 0.4))
        done(self)


# ══════════════ B13: the repo's own limit — unbalanced classes; humans are the yardstick; method only ══════════════
TALL = Iso(-5.0, -2.9, 0.8)
SHORT = Iso(-3.1, -2.9, 0.8)


def slab_stack(iso, n):
    return VGroup(*[iso.box(0, 0, i * 0.36, 1.2, 1.2, 0.3, TILE_TOP, TILE_L, TILE_R) for i in range(n)])


def yardstick(x=0.8, y0=-2.9, y1=1.4):
    bar = Rectangle(width=0.4, height=y1 - y0, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, (y0 + y1) / 2, 0])
    ticks = VGroup(*[Line([x - 0.2, y, 0], [x + 0.02, y, 0], color=PAGE_TOP, stroke_width=6) for y in np.arange(y0 + 0.5, y1, 0.5)])
    return VGroup(bar, ticks)


S13 = dict(cx=0.0, py=1.0, k=0.85)


class B13_Limit(Scene):
    def construct(self):
        p = b12_state_parts()
        self.add(*p.values())
        self.play(FadeOut(VGroup(p["graders"], p["stack"], p["lg"], p["d1"], p["d2"], p["n"], p["lr"])), run_time=0.45)
        tall, short = slab_stack(TALL, 8), slab_stack(SHORT, 1)
        lu = lab("unbalanced", [-3.8, 2.7])
        until(self, "most pairs are even-handed", lead=0.3)
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.4) for s in tall], lag_ratio=0.15), FadeIn(short, shift=DOWN * 0.4), run_time=1.1)
        self.play(FadeIn(lu), run_time=guard(self, 0.3))
        until(self, "raw agreement", lead=0.3)
        ag = Rectangle(width=0.55, height=4.1, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=2).move_to([-1.4, -2.9 + 2.05, 0])
        self.play(GrowFromEdge(ag, DOWN), run_time=guard(self, 0.7))
        until(self, "better yardstick", lead=0.5)
        ys = yardstick()
        ly = lab("human yardstick", [2.5, 2.4])
        self.play(GrowFromEdge(ys, DOWN), FadeIn(ly), Indicate(p["hum"], color=None, scale_factor=1.06), run_time=guard(self, 0.6))
        until(self, "This film shows the method only", lead=0.3)
        rest = VGroup(tall, short, lu, ag, ys, ly, p["hum"], p["n85"])
        self.play(FadeOut(rest), run_time=guard(self, 0.4))
        rig = scale_rig(**S13)
        lmo = lab("method only", [0, 2.7])
        self.play(FadeIn(rig, shift=UP * 0.3), FadeIn(lmo), run_time=guard(self, 0.5))
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Scale, B01_Topics, B02_Pair, B03_Tasks, B04_Answers, B05_Grader, B06_Even, B07_Quality, B08_Opposing,
             B09_Refusals, B10_Probs, B11_Threshold, B12_Agree, B13_Limit):
    _cls.play = ST.play
