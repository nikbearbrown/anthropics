"""
Manim scenes for show-tell-zoom-in (show-tell skill, card #32, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The zoom tool from anthropics/claude-cookbooks multimodal/crop_tool.ipynb (LIVE version, rewritten
2026-07-23): Claude sees an image once, in 28x28-pixel patches, and an image over the model's budget is
scaled down -> your code keeps the full-resolution original and resizes a copy to exactly the size Claude
sees -> a tool named zoom with pixel inputs x1, y1, x2, y2 (origin top-left) -> Claude calls it on a
region -> your code maps the box onto the original, crops there, scales the crop up to the budget and
returns it as a JPEG with one text line -> Claude may zoom again, tighter, then answers -> a loop (capped
at 20 rounds by the runner) -> the same pattern on any small detail -> more than double the accuracy on a
public benchmark (per the cookbook), paid for in tokens and time.
Cast: the CHART (one data model drawn at any zoom: grey series, Widget A grey, Widget E deep kraft), the
PATCH grid, the ORIGINAL and the COPY, CLAUDE (a dark block with a terracotta spark) with its ZOOM tag,
YOUR CODE (a kraft box on a dark plinth), the zoom FRAME, the magnified TILE, the LOOP arcs, a scanned
FORM, two bars and a stack of token slabs.
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







# ═════════════════════════════ the film: Zoom In ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
CONN = "#9C8462"          # deep kraft: connectors, and the Widget-E line
TILE = "#B39A72"          # deep kraft
SHADOW = "#9A8D76"        # paper-cut offset under cards
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (outside GATE T's ink tolerance)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=40):
    return T(s, size).move_to(P3(c)).set_z_index(20)


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.08):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def gbar(x0, x1, y, color=BAR1, w=6):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def leader(a, b):
    return Line(P3(a), P3(b), color=CONN, stroke_width=5).set_z_index(15)


def drop(self, *mobs):
    for m in mobs:
        self.remove(*m.get_family())


# ─── the chart: one data model, drawn at any zoom ───
def base(u):
    return 0.5 + 0.12 * np.sin(5 * u + 0.3)


SERIES = [  # (function, colour, weight)
    (lambda u: 0.86 + 0.06 * np.sin(7 * u + 1.0), BAR2, 1.0),
    (lambda u: 0.20 + 0.08 * np.sin(6 * u + 2.2), BAR2, 1.0),
    (lambda u: 0.64 + 0.09 * np.sin(4.3 * u + 4.0), BAR2, 1.0),
    (lambda u: base(u) - 0.15 * (0.84 - u), BAR1, 1.3),     # Widget A (grey)
    (lambda u: base(u) + 0.15 * (0.84 - u), CONN, 1.3),     # Widget E (deep kraft)
]
FA, FE = SERIES[3][0], SERIES[4][0]
SPOT_U = 0.8                                  # "month 48" of 60
REG1 = (0.74, 0.86, 0.33, 0.45)               # first zoom box (data coords)
REG2 = (0.78, 0.82, 0.37, 0.41)               # second, tighter zoom box


def chart(cx, cy, w, h, reg=(0.0, 1.0, 0.0, 1.0), lw=4.0, marker=False, month=False, plinth=False, sw=4, stroke=INK):
    """A chart card showing data region reg=(u0,u1,v0,v1). Returns (group, XY) where XY maps data -> screen."""
    u0, u1, v0, v1 = reg
    x0, y0 = cx - w / 2.0, cy - h / 2.0
    ins = 0.06

    def XY(u, v):
        return np.array([x0 + (u - u0) / (u1 - u0) * w, y0 + (v - v0) / (v1 - v0) * h, 0.0])

    g = VGroup()
    sh = Rectangle(width=w, height=h, fill_color=SHADOW, fill_opacity=1, stroke_width=0).move_to(P3((cx + 0.1, cy - 0.1)))
    g.add(sh)
    if plinth:
        g.add(Rectangle(width=w + 0.3, height=0.16, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(P3((cx + 0.05, y0 - 0.2))))
    card = rrect(w, h, (cx, cy), PAGE_TOP, stroke, sw, r=0.06)
    g.add(card)
    grid = VGroup()
    for k in range(1, 10):
        u = k / 10.0
        if u0 < u < u1 and not (month and abs(u - SPOT_U) < 1e-6):
            grid.add(Line(XY(u, v0) + UP * ins, XY(u, v1) + DOWN * ins, color=GHOST, stroke_width=2))
    for k in range(1, 5):
        v = k / 5.0
        if v0 < v < v1:
            grid.add(Line(XY(u0, v) + RIGHT * ins, XY(u1, v) + LEFT * ins, color=GHOST, stroke_width=2))
    g.add(grid)
    if month:
        g.add(DashedLine(XY(SPOT_U, v0) + UP * ins, XY(SPOT_U, v1) + DOWN * ins, color=BAR2, stroke_width=5, dash_length=0.12))
    curves = VGroup()
    ylo, yhi = y0 + ins * 1.5, y0 + h - ins * 1.5
    for f, col, wt in SERIES:
        us = np.linspace(u0, u1, 220)
        run = []
        runs = []
        for u in us:
            p = XY(u, f(u))
            if ylo <= p[1] <= yhi and x0 + ins <= p[0] <= x0 + w - ins:
                run.append(p)
            else:
                if len(run) > 1:
                    runs.append(run)
                run = []
        if len(run) > 1:
            runs.append(run)
        for r_ in runs:
            curves.add(VMobject(stroke_color=col, stroke_width=lw * wt).set_points_as_corners(r_))
    g.add(curves)
    if marker:   # the tiny annotation at the top series' peak: a dot and a tiny "text" bar
        up = (np.pi / 2 - 1.0) / 7.0
        pk = XY(up, SERIES[0][0](up))
        g.add(Dot(pk, radius=0.04, color=BAR1))
        g.add(Line(pk + np.array([0.07, 0.07, 0]), pk + np.array([0.37, 0.07, 0]), color=BAR1, stroke_width=3))
    return g.set_z_index(1), XY


def region_box(XY, reg, color=CONN, sw=7):
    u0, u1, v0, v1 = reg
    a, b = XY(u0, v0), XY(u1, v1)
    return Rectangle(width=b[0] - a[0], height=b[1] - a[1], stroke_color=color, stroke_width=sw, fill_opacity=0).move_to((a + b) / 2).set_z_index(8)


def patch_grid(cx, cy, w, h, p=0.32, color=BAR2):
    x0, y0 = cx - w / 2.0 + 0.06, cy - h / 2.0 + 0.06
    x1, y1 = cx + w / 2.0 - 0.06, cy + h / 2.0 - 0.06
    g = VGroup()
    x = x0 + p
    while x < x1 - 0.02:
        g.add(Line([x, y0, 0], [x, y1, 0], color=color, stroke_width=2.5))
        x += p
    y = y0 + p
    while y < y1 - 0.02:
        g.add(Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=2.5))
        y += p
    return g.set_z_index(6)


# ─── fixed layout ───
BIG = (-1.3, 0.05, 7.6, 4.4)          # B00/B01 chart
ORIG = (-3.55, -1.55, 5.0, 2.9)       # the full-resolution original
COPY = (-3.9, 1.75, 3.4, 1.97)        # the resized copy Claude sees
TILE_C, TW, TH = (0.95, 0.35), 3.4, 2.0


def big_chart():
    return chart(*BIG, lw=5, marker=True, plinth=True)


def orig_chart():
    return chart(*ORIG, lw=4.5, marker=True, plinth=True)


def copy_chart():
    return chart(*COPY, lw=3.5, marker=True, sw=4)


def tile1(scale=1.0, c=TILE_C):
    return chart(c[0], c[1], TW * scale, TH * scale, REG1, lw=9 if scale > 0.5 else 3, month=scale > 0.5, sw=4,
                 stroke=INK if scale > 0.5 else BAR1)


# ─── Claude and your code ───
CL_C = (4.8, 1.3)
CD_C = (4.8, -2.1)


def claude_block(c=CL_C):
    A = rig_at(c[0], c[1], 0.8, 1.4, 1.4)
    body = A.box(0, 0, 0, 1.4, 1.4, 0.8, DK_TOP, DK_L, DK_R)
    spark = Dot(A.p(0.7, 0.7, 0.8), radius=0.1, color=TERRA)
    return VGroup(body, spark).set_z_index(3)


def code_box(c=CD_C):
    A = rig_at(c[0], c[1], 0.7, 1.6, 1.2)
    plinth = A.box(-0.15, -0.15, -0.3, 1.9, 1.5, 0.3, DK_TOP, DK_L, DK_R)
    body = A.box(0, 0, 0, 1.6, 1.2, 0.9)
    slot = A.quad([(0.35, 0, 0.3), (1.25, 0, 0.3), (1.25, 0, 0.6), (0.35, 0, 0.6)], DK_L, stroke=DEV_EDGE, sw=3)
    return VGroup(plinth, body, slot).set_z_index(3)


def zoom_tag(c=CL_C):
    tag = rrect(0.9, 0.42, (c[0] - 1.55, c[1] + 0.35), DK_L, DK_L, 0, r=0.12)
    plug = Line(P3((c[0] - 1.1, c[1] + 0.35)), P3((c[0] - 0.85, c[1] + 0.35)), color=CONN, stroke_width=8)
    return VGroup(plug, tag).set_z_index(4)


def slip(c, w=1.1, h=0.6):
    b = rrect(w, h, c, PAGE_TOP, BAR1, 3, r=0.06)
    l1 = gbar(c[0] - w * 0.35, c[0] + w * 0.3, c[1] + h * 0.15, BAR1, 7)
    l2 = gbar(c[0] - w * 0.35, c[0] + w * 0.05, c[1] - h * 0.18, BAR2, 6)
    return VGroup(b, l1, l2).set_z_index(10)


def call_card(c):
    """A small card carrying a zoom box (the tool call)."""
    b = rrect(0.95, 0.62, c, PAGE_TOP, BAR1, 3, r=0.06)
    fr = Rectangle(width=0.42, height=0.26, stroke_color=DEV_EDGE, stroke_width=5).move_to(P3(c) + np.array([0.12, -0.02, 0]))
    dt = Dot(P3(c) + np.array([-0.28, 0.12, 0]), radius=0.05, color=TERRA)
    return VGroup(b, fr, dt).set_z_index(10)


def workbench(k):
    """Everything on stage at the START of beat Bk, k in 3..8 (without labels)."""
    d = {}
    d["orig"], d["oXY"] = orig_chart()
    d["copy"], d["cXY"] = copy_chart()
    d["code"] = code_box()
    if k >= 4:
        d["claude"] = claude_block()
        d["tag"] = zoom_tag()
    if k >= 5:
        d["cframe"] = region_box(d["cXY"], REG1)
    if k >= 6:
        d["oframe"] = region_box(d["oXY"], REG1)
        d["tile"], d["tXY"] = tile1(0.158)
    if k >= 7:
        d["tile"], d["tXY"] = tile1(1.0)
    return d


def add_all(self, d, keys):
    for k in keys:
        if k in d:
            self.add(d[k])


# ═════════════════════════════ beats ═════════════════════════════
class B00_Chart(Scene):
    def construct(self):
        ch, XY = big_chart()
        card = VGroup(ch[0], ch[1], ch[2], ch[3])            # shadow, plinth, card, grid
        curves = ch[4]
        mark = VGroup(ch[5], ch[6])
        self.play(FadeIn(card, shift=UP * 0.3), run_time=0.8)
        l0 = lbl("dense chart", (1.3, 2.72), 40)
        self.play(FadeIn(l0), run_time=0.4)
        others = VGroup(*[c for c in curves if c.get_stroke_color().to_hex().upper() == BAR2.upper()])
        ae = VGroup(*[c for c in curves if c.get_stroke_color().to_hex().upper() != BAR2.upper()])
        self.play(Create(others), run_time=1.6)
        until(self, "Claude sees an image once")
        self.play(Create(ae), run_time=1.2)
        until(self, "a small label")
        self.play(FadeIn(mark), run_time=0.5)
        pk = mark[0].get_center()
        l1 = lbl("tiny label", (pk[0] + 0.75, 2.72), 40)
        self.play(FadeIn(l1), run_time=0.5)
        until(self, "two lines that nearly touch")
        sp = XY(SPOT_U, FE(SPOT_U))
        dot = Dot(sp, radius=0.09, color=TERRA).set_z_index(9)
        self.play(GrowFromCenter(dot), run_time=0.5)
        l2 = lbl("nearly touch", (4.3, sp[1] + 1.0), 40)
        ld2 = leader((sp[0] + 0.15, sp[1] + 0.1), (l2.get_left()[0] - 0.3, sp[1] + 1.0))
        self.play(Create(ld2), FadeIn(l2), run_time=0.6)
        until(self, "no amount of prompting")
        self.play(Indicate(dot, color=None, scale_factor=1.6), run_time=0.8)
        done(self)


class B01_Patches(Scene):
    def construct(self):
        ch, XY = big_chart()
        self.add(ch)
        sp = XY(SPOT_U, FE(SPOT_U))
        dot = Dot(sp, radius=0.09, color=TERRA).set_z_index(9)
        self.add(dot)
        until(self, "It reads an image in patches")
        cx, cy, w, h = BIG
        pg = patch_grid(cx, cy, w, h, 0.32)
        self.play(Create(pg), run_time=1.4)
        l1 = lbl("patches", (4.3, 1.9), 40)
        ld1 = leader((cx + w / 2 - 0.4, 1.9), (l1.get_left()[0] - 0.3, 1.9))
        self.play(FadeIn(l1), Create(ld1), run_time=0.5)
        until(self, "Each patch is one visual token")
        # the one patch that holds both lines
        x0, y0 = cx - w / 2 + 0.06, cy - h / 2 + 0.06
        px = x0 + np.floor((sp[0] - x0) / 0.32) * 0.32 + 0.16
        py = y0 + np.floor((sp[1] - y0) / 0.32) * 0.32 + 0.16
        one = Square(side_length=0.32, stroke_color=INK, stroke_width=7).move_to([px, py, 0]).set_z_index(10)
        self.play(Create(one), run_time=0.6)
        l2 = lbl("one patch", (4.3, py - 0.9), 40)
        ld2 = leader((px + 0.25, py - 0.1), (l2.get_left()[0] - 0.3, py - 0.9))
        self.play(FadeIn(l2), Create(ld2), run_time=0.5)
        until(self, "An image over the budget is scaled down")
        self.play(FadeOut(pg), FadeOut(one), FadeOut(ld1), FadeOut(ld2), FadeOut(l1), FadeOut(l2), run_time=0.5)
        grp = VGroup(ch, dot)
        self.play(grp.animate.scale(0.5).move_to(P3((-1.3, 0.3))), run_time=1.2)
        sw_, sh_ = w * 0.5, h * 0.5
        cc_ = np.array(ch[2].get_center())
        pg2 = patch_grid(float(cc_[0]), float(cc_[1]), sw_, sh_, 0.32)
        self.play(Create(pg2), run_time=0.8)
        l3 = lbl("scaled down", (3.6, 0.3), 40)
        self.play(FadeIn(l3), run_time=0.5)
        until(self, "the small details shrink")
        self.play(Indicate(dot, color=None, scale_factor=1.6), run_time=0.8)
        done(self)


class B02_Resize(Scene):
    def construct(self):
        # start: B01's end (small chart + patch grid), then the workbench forms
        ch, XY = big_chart()
        dot = Dot(XY(SPOT_U, FE(SPOT_U)), radius=0.09, color=TERRA).set_z_index(9)
        grp = VGroup(ch, dot).scale(0.5).move_to(P3((-1.3, 0.3)))
        cx, cy, w, h = BIG
        cc_ = np.array(ch[2].get_center())
        pg2 = patch_grid(float(cc_[0]), float(cc_[1]), w * 0.5, h * 0.5, 0.32)
        self.add(grp, pg2)
        self.play(FadeOut(grp), FadeOut(pg2), run_time=0.6)
        code = code_box()
        self.play(FadeIn(code, shift=DOWN * 0.4), run_time=0.7)
        lc = lbl("your code", (2.55, -2.75), 40)
        self.play(FadeIn(lc), run_time=0.4)
        until(self, "Keep the full-resolution original")
        orig, oXY = orig_chart()
        self.play(FadeIn(orig, shift=RIGHT * 0.4), run_time=0.8)
        lo = lbl("original", (0.35, -0.6), 40)
        self.play(FadeIn(lo), run_time=0.4)
        until(self, "Then resize a copy")
        cp, cXY = copy_chart()
        ghost, _ = chart(*ORIG, lw=4.5, marker=True, plinth=False)
        ghost.set_z_index(5)
        self.add(ghost)
        self.play(ghost.animate.scale(COPY[2] / ORIG[2]).move_to(np.array(cp.get_center())), run_time=1.2)
        self.remove(ghost)
        self.add(cp)
        lk = lbl("copy", (-1.3, 2.4), 40)
        self.play(FadeIn(lk), run_time=0.4)
        until(self, "That copy is what you send")
        chk = check(-1.95, 1.55, 0.2, INK, 8).set_z_index(12)
        self.play(Create(chk), run_time=0.5)
        until(self, "Now any pixel Claude names")
        pa = Dot(cXY(0.3, 0.5), radius=0.07, color=TERRA).set_z_index(12)
        pb = Dot(oXY(0.3, 0.5), radius=0.07, color=TERRA).set_z_index(12)
        link = DashedLine(pa.get_center(), pb.get_center(), color=CONN, stroke_width=5, dash_length=0.12).set_z_index(11)
        self.play(GrowFromCenter(pa), run_time=0.4)
        self.play(Create(link), GrowFromCenter(pb), run_time=0.7)
        done(self)


class B03_Tool(Scene):
    def construct(self):
        d = workbench(3)
        add_all(self, d, ["orig", "copy", "code"])
        cl = claude_block()
        self.play(FadeIn(cl, shift=DOWN * 0.5), run_time=0.7)
        lcl = lbl("Claude", (CL_C[0], CL_C[1] - 0.95), 40)
        self.play(FadeIn(lcl), run_time=0.4)
        tag = zoom_tag()
        self.play(FadeIn(tag, shift=RIGHT * 0.3), run_time=0.5)
        lz = lbl("zoom", (CL_C[0] - 1.55, CL_C[1] + 1.0), 40)
        self.play(FadeIn(lz), run_time=0.4)
        until(self, "It takes four numbers")
        cXY = d["cXY"]
        cx, cy, cw, chh = COPY
        o = Dot(P3((cx - cw / 2, cy + chh / 2)), radius=0.09, color=TERRA).set_z_index(12)
        lo = lbl("0, 0", (cx - cw / 2 + 0.35, cy + chh / 2 + 0.33), 38)
        self.play(GrowFromCenter(o), FadeIn(lo), run_time=0.6)
        fr = region_box(cXY, REG1)
        self.play(Create(fr), run_time=0.8)
        tl, br = fr.get_corner(UL), fr.get_corner(DR)
        c1 = Dot(tl, radius=0.07, color=TERRA).set_z_index(12)
        c2 = Dot(br, radius=0.07, color=TERRA).set_z_index(12)
        l1 = lbl("x1, y1", (-0.6, 2.35), 40)
        d1 = leader((tl[0] + 0.12, tl[1] + 0.1), (l1.get_left()[0] - 0.3, 2.35))
        self.play(GrowFromCenter(c1), Create(d1), FadeIn(l1), run_time=0.6)
        until(self, "Those are the left, top, right and bottom")
        l2 = lbl("x2, y2", (-0.6, 0.75), 40)
        d2 = leader((br[0] + 0.12, br[1] - 0.08), (l2.get_left()[0] - 0.3, 0.75))
        self.play(GrowFromCenter(c2), Create(d2), FadeIn(l2), run_time=0.6)
        until(self, "An earlier version")
        l3 = lbl("0 to 1", (1.9, -0.55), 40)
        self.play(FadeIn(l3), run_time=0.5)
        until(self, "Claude works best with pixel")
        self.play(FadeOut(l3, shift=DOWN * 0.2), run_time=0.5)
        until(self, "so the current one uses pixels")
        l4 = lbl("pixels", (1.9, -0.55), 40)
        ck = check(1.05, -0.5, 0.2, INK, 8).set_z_index(12)
        self.play(FadeIn(l4), Create(ck), run_time=0.6)
        done(self)


class B04_Ask(Scene):
    def construct(self):
        d = workbench(4)
        add_all(self, d, ["orig", "copy", "code", "claude", "tag"])
        q = slip((1.2, 2.55))
        self.play(FadeIn(q, shift=RIGHT * 0.6), run_time=0.7)
        lq = lbl("A or E?", (1.2, 1.8), 40)
        self.play(FadeIn(lq), run_time=0.4)
        until(self, "In the full view")
        cXY = d["cXY"]
        sp = cXY(SPOT_U, FE(SPOT_U))
        dot = Dot(sp, radius=0.08, color=TERRA).set_z_index(12)
        self.play(GrowFromCenter(dot), run_time=0.4)
        self.play(Indicate(dot, color=None, scale_factor=1.7), run_time=0.7)
        until(self, "So instead of answering")
        self.play(q.animate.scale(0.5).move_to(P3((CL_C[0], CL_C[1] + 0.5))), FadeOut(lq), run_time=0.8)
        self.remove(q)
        fr = region_box(cXY, REG1)
        self.play(Create(fr), run_time=0.6)
        until(self, "Claude calls zoom")
        cc = call_card((CL_C[0], CL_C[1] - 0.2))
        self.play(FadeIn(cc), run_time=0.3)
        self.play(cc.animate.move_to(P3((CD_C[0], CD_C[1] + 1.45))), run_time=0.9)
        lcc = lbl("zoom call", (3.0, -0.35), 40)
        self.play(FadeIn(lcc), run_time=0.4)
        done(self)


class B05_Crop(Scene):
    def construct(self):
        d = workbench(5)
        add_all(self, d, ["orig", "copy", "code", "claude", "tag", "cframe"])
        cc = call_card((CD_C[0], CD_C[1] + 1.45))
        self.add(cc)
        self.play(cc.animate.scale(0.6).move_to(P3((CD_C[0], CD_C[1] + 0.35))), run_time=0.6)
        self.play(FadeOut(cc), run_time=0.3)
        until(self, "It maps the box")
        echo = d["cframe"].copy().set_z_index(12)
        self.add(echo)
        of = region_box(d["oXY"], REG1)
        self.play(echo.animate.move_to(of.get_center()).stretch_to_fit_width(of.width).stretch_to_fit_height(of.height), run_time=1.2)
        self.remove(echo)
        self.add(of)
        ls = lbl("same box", (0.35, -1.9), 40)
        ldr = leader((of.get_right()[0] + 0.12, of.get_center()[1]), (ls.get_left()[0] - 0.3, -1.9))
        self.play(Create(ldr), FadeIn(ls), run_time=0.6)
        until(self, "and cuts the region out of the original")
        small, _ = tile1(0.158, tuple(of.get_center()[:2]))
        small.set_z_index(14)
        self.add(small)
        self.play(small.animate.move_to(P3(TILE_C)), FadeOut(ldr), FadeOut(ls), run_time=1.0)
        lc = lbl("crop", (TILE_C[0] + 1.1, TILE_C[1]), 40)
        self.play(FadeIn(lc), run_time=0.4)
        until(self, "So the crop keeps every pixel")
        self.play(Indicate(of, color=None, scale_factor=1.15), run_time=0.7)
        done(self)


class B06_Magnify(Scene):
    def construct(self):
        d = workbench(6)
        add_all(self, d, ["orig", "copy", "code", "claude", "tag", "cframe", "oframe", "tile"])
        small = d["tile"]
        big, tXY = tile1(1.0)
        self.play(small.animate.scale(TW / (TW * 0.158)).move_to(big.get_center()), run_time=1.3)
        self.remove(small)
        self.add(big)
        lm = lbl("magnified", (TILE_C[0], TILE_C[1] + TH / 2 + 0.45), 40)
        self.play(FadeIn(lm), run_time=0.4)
        until(self, "so each detail covers more patches")
        pg = patch_grid(TILE_C[0], TILE_C[1], TW, TH, 0.32)
        self.play(Create(pg), run_time=1.2)
        until(self, "It sends that back")
        self.play(FadeOut(pg), run_time=0.4)
        strip = VGroup(rrect(2.2, 0.36, (TILE_C[0], TILE_C[1] - TH / 2 - 0.45), PAGE_TOP, BAR1, 3, r=0.06),
                       gbar(TILE_C[0] - 0.85, TILE_C[0] + 0.6, TILE_C[1] - TH / 2 - 0.45, BAR1, 7)).set_z_index(10)
        self.play(FadeIn(strip, shift=UP * 0.2), run_time=0.5)
        lj = lbl("JPEG", (TILE_C[0] + 1.95, TILE_C[1] - TH / 2 - 0.45), 40)
        self.play(FadeIn(lj), run_time=0.4)
        until(self, "JPEG, because every result")
        pkt_t, _ = tile1(0.3, (TILE_C[0], TILE_C[1]))
        pkt = VGroup(pkt_t, strip.copy().scale(0.35).next_to(pkt_t, DOWN, buff=0.05)).set_z_index(16)
        self.add(pkt)
        self.play(pkt.animate.scale(0.6).move_to(P3((CL_C[0] - 0.05, CL_C[1] + 0.95))), run_time=1.0)
        self.play(FadeOut(pkt), run_time=0.4)
        until(self, "and a few big PNG crops")
        self.play(Indicate(strip, color=None, scale_factor=1.08), run_time=0.6)
        done(self)


class B07_Again(Scene):
    def construct(self):
        d = workbench(7)
        add_all(self, d, ["orig", "copy", "code", "claude", "tag", "cframe", "oframe", "tile"])
        t1 = d["tile"]
        L1 = (-3.9, 0.45)
        self.play(FadeOut(d["orig"]), FadeOut(d["copy"]), FadeOut(d["cframe"]), FadeOut(d["oframe"]), run_time=0.5)
        self.play(t1.animate.shift(P3(L1) - P3(TILE_C)), run_time=0.8)
        _, t1XY = tile1(1.0, L1)
        until(self, "it zooms again, tighter")
        fr2 = region_box(t1XY, REG2)
        self.play(Create(fr2), run_time=0.6)
        C2, W2, H2 = (1.5, 0.3), 3.6, 2.1
        t2, t2XY = chart(C2[0], C2[1], W2, H2, REG2, lw=10, month=True, sw=4)
        s = t2.copy().scale(fr2.width / W2).move_to(fr2.get_center()).set_z_index(14)
        self.add(s)
        self.play(s.animate.scale(W2 / fr2.width).move_to(t2.get_center()), run_time=1.1)
        self.remove(s)
        self.add(t2)
        lz2 = lbl("zoom 2", (C2[0], C2[1] + H2 / 2 + 0.45), 40)
        self.play(FadeIn(lz2), run_time=0.4)
        until(self, "then answered")
        yE = t2XY(REG2[0], FE(REG2[0]))[1]
        yA = t2XY(REG2[0], FA(REG2[0]))[1]
        le = lbl("E", (C2[0] - W2 / 2 - 0.4, yE), 44)
        la = lbl("A", (C2[0] - W2 / 2 - 0.4, yA), 44)
        self.play(FadeIn(le), FadeIn(la), run_time=0.5)
        ck = check(C2[0] - W2 / 2 - 1.05, yE - 0.02, 0.2, INK, 8).set_z_index(12)
        self.play(Create(ck), run_time=0.5)
        until(self, "Asked the same question without the tool")
        ln = lbl("no tool: A", (-3.6, -1.55), 40)
        self.play(FadeIn(ln), run_time=0.5)
        xa = VGroup(Line(P3((-2.2, -1.75)), P3((-1.8, -1.35)), color=INK, stroke_width=8),
                    Line(P3((-2.2, -1.35)), P3((-1.8, -1.75)), color=INK, stroke_width=8)).set_z_index(12)
        self.play(Create(xa), run_time=0.5)
        done(self)


def pedestal():
    """A kraft counter pedestal on a dark plinth; the round cap stands on it as a big number."""
    A = rig_at(-3.9, -2.35, 0.7, 1.4, 1.4)
    return VGroup(A.box(-0.15, -0.15, -0.3, 1.7, 1.7, 0.3, DK_TOP, DK_L, DK_R), A.box(0, 0, 0, 1.4, 1.4, 0.5)).set_z_index(3)


LC_C = (0.9, 1.45)     # the loop: Claude up, your code down (B08)
LD_C = (0.9, -2.05)


class B08_Loop(Scene):
    def construct(self):
        d = workbench(7)
        add_all(self, d, ["code", "claude", "tag"])
        t1, _ = tile1(1.0, (-3.9, 0.45))
        t2, _ = chart(1.5, 0.3, 3.6, 2.1, REG2, lw=10, month=True, sw=4)
        self.add(t1, t2)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)
        top = VGroup(d["claude"], d["tag"])
        self.play(top.animate.shift(P3(LC_C) - P3(CL_C)), d["code"].animate.shift(P3(LD_C) - P3(CD_C)), run_time=1.0)
        lcl = lbl("Claude", (LC_C[0] + 2.1, LC_C[1] + 0.25), 40)
        lcd = lbl("your code", (LD_C[0] + 2.6, LD_C[1] + 0.05), 40)
        self.play(FadeIn(lcl), FadeIn(lcd), run_time=0.4)
        until(self, "Claude asks")
        a = P3((LC_C[0] - 1.05, LC_C[1] - 0.2))
        b = P3((LD_C[0] - 1.05, LD_C[1] + 0.55))
        arc1 = ArcBetweenPoints(a, b, angle=PI / 2.2, color=CONN, stroke_width=8).set_z_index(2)
        arc2 = ArcBetweenPoints(b + np.array([2.1, 0, 0]), a + np.array([2.1, 0, 0]), angle=PI / 2.2, color=CONN, stroke_width=8).set_z_index(2)
        self.play(Create(arc1), run_time=0.7)
        lask = lbl("ask", (arc1.get_left()[0] - 0.55, (a[1] + b[1]) / 2), 40)
        self.play(FadeIn(lask), run_time=0.3)
        until(self, "your code crops and returns")
        self.play(Create(arc2), run_time=0.7)
        lcrop = lbl("crop", (arc2.get_right()[0] + 0.6, (a[1] + b[1]) / 2), 40)
        self.play(FadeIn(lcrop), run_time=0.3)
        until(self, "and Claude looks again")
        rd = Dot(a, radius=0.1, color=TERRA).set_z_index(12)
        self.add(rd)
        for _ in range(2):
            self.play(MoveAlongPath(rd, arc1), run_time=0.45)
            self.play(MoveAlongPath(rd, arc2), run_time=0.45)
        until(self, "The loop ends when Claude answers")
        ans = slip((LC_C[0], LC_C[1] + 0.6), 1.0, 0.55)
        self.add(ans)
        self.play(ans.animate.move_to(P3((5.2, 2.75))), run_time=0.8)
        lans = lbl("answer", (5.2, 2.05), 40)
        self.play(FadeIn(lans), run_time=0.3)
        until(self, "also stops after twenty rounds")
        plate = pedestal()
        num = lbl("20", (-3.9, -0.95), 72).set_z_index(22)
        self.play(FadeIn(plate, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(num), run_time=0.3)
        lmax = lbl("max rounds", (-3.9, -0.05), 40)
        self.play(FadeIn(lmax), run_time=0.3)
        done(self)


FORM_C, FW, FH = (-3.4, -0.1), 3.0, 4.0
FIELD = (-2.55, -1.65, 0.62, 0.3)       # tiny field on the form: cx, cy, w, h


def form_card():
    g = VGroup(Rectangle(width=FW, height=FH, fill_color=SHADOW, fill_opacity=1, stroke_width=0).move_to(P3((FORM_C[0] + 0.1, FORM_C[1] - 0.1))),
               Rectangle(width=FW + 0.3, height=0.16, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(P3((FORM_C[0] + 0.05, FORM_C[1] - FH / 2 - 0.2))),
               rrect(FW, FH, FORM_C, PAGE_TOP, INK, 4, r=0.06))
    rows = VGroup()
    for i in range(9):
        y = FORM_C[1] + FH / 2 - 0.45 - i * 0.33
        rows.add(gbar(FORM_C[0] - FW / 2 + 0.3, FORM_C[0] + FW / 2 - 0.3 - (0.6 if i % 3 == 2 else 0.0), y, BAR2 if i % 2 else BAR1, 5))
    g.add(rows)
    fx, fy, fw, fh = FIELD
    g.add(Rectangle(width=fw, height=fh, stroke_color=BAR1, stroke_width=3).move_to(P3((fx, fy))))
    g.add(Line(P3((fx - fw * 0.35, fy - fh * 0.1)), P3((fx + fw * 0.3, fy + fh * 0.12)), color=BAR1, stroke_width=2.5))
    return g.set_z_index(1)


def field_tile(c, w=3.6, h=1.75):
    g = VGroup(Rectangle(width=w, height=h, fill_color=SHADOW, fill_opacity=1, stroke_width=0).move_to(P3((c[0] + 0.1, c[1] - 0.1))),
               rrect(w, h, c, PAGE_TOP, INK, 4, r=0.06))
    bw, bh = w * 0.62, h * 0.55
    g.add(Rectangle(width=bw, height=bh, stroke_color=BAR1, stroke_width=8).move_to(P3(c)))
    wave = VMobject(stroke_color=CONN, stroke_width=10).set_points_smoothly(
        [P3((c[0] - bw * 0.36 + k * bw * 0.12, c[1] + (0.12 if k % 2 else -0.14) * bh * 1.2)) for k in range(7)])
    g.add(wave)
    return g.set_z_index(4)


class B09_Anywhere(Scene):
    def construct(self):
        d = workbench(7)
        top = VGroup(d["claude"], d["tag"]).shift(P3(LC_C) - P3(CL_C))
        code = d["code"].shift(P3(LD_C) - P3(CD_C))
        a = P3((LC_C[0] - 1.05, LC_C[1] - 0.2))
        b = P3((LD_C[0] - 1.05, LD_C[1] + 0.55))
        arc1 = ArcBetweenPoints(a, b, angle=PI / 2.2, color=CONN, stroke_width=8).set_z_index(2)
        arc2 = ArcBetweenPoints(b + np.array([2.1, 0, 0]), a + np.array([2.1, 0, 0]), angle=PI / 2.2, color=CONN, stroke_width=8).set_z_index(2)
        ans = slip((5.2, 2.75), 1.0, 0.55)
        plate = pedestal()
        num = lbl("20", (-3.9, -0.95), 72).set_z_index(22)
        rest = VGroup(top, code, arc1, arc2, ans, plate, num)
        self.add(rest)
        self.play(FadeOut(rest), run_time=0.6)
        f = form_card()
        self.play(FadeIn(f, shift=UP * 0.4), run_time=0.8)
        lf = lbl("scanned form", (FORM_C[0], FORM_C[1] + FH / 2 + 0.45), 40)
        self.play(FadeIn(lf), run_time=0.4)
        until(self, "wherever the detail is small")
        fx, fy, fw, fh = FIELD
        fr = Rectangle(width=fw + 0.24, height=fh + 0.2, stroke_color=CONN, stroke_width=7).move_to(P3((fx, fy))).set_z_index(8)
        self.play(Create(fr), run_time=0.6)
        TC = (2.4, -0.1)
        tl = field_tile(TC)
        s = tl.copy().scale(fr.width / 3.6).move_to(fr.get_center()).set_z_index(14)
        self.add(s)
        self.play(s.animate.scale(3.6 / fr.width).move_to(tl.get_center()), run_time=1.0)
        self.remove(s)
        self.add(tl)
        lt = lbl("same move", (TC[0], TC[1] + 1.35), 40)
        self.play(FadeIn(lt), run_time=0.4)
        until(self, "and scans of paper forms")
        self.play(Indicate(fr, color=None, scale_factor=1.2), run_time=0.6)
        done(self)


class B10_Payoff(Scene):
    def construct(self):
        f = form_card()
        tl = field_tile((2.4, -0.1))
        fx, fy, fw, fh = FIELD
        fr = Rectangle(width=fw + 0.24, height=fh + 0.2, stroke_color=CONN, stroke_width=7).move_to(P3((fx, fy))).set_z_index(8)
        self.add(f, tl, fr)
        self.play(FadeOut(VGroup(f, tl, fr)), run_time=0.6)
        base_y = -2.1
        ground = Line(P3((-5.2, base_y)), P3((0.4, base_y)), color=INK, stroke_width=6).set_z_index(2)
        self.play(Create(ground), run_time=0.5)
        until(self, "more than doubled accuracy")
        b1 = Rectangle(width=1.3, height=1.1, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((-3.8, base_y + 0.55))).set_z_index(3)
        b2 = Rectangle(width=1.3, height=2.9, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((-1.2, base_y + 1.45))).set_z_index(3)
        l1 = lbl("no tool", (-3.8, base_y - 0.45), 40)
        l2 = lbl("zoom tool", (-1.2, base_y - 0.45), 40)
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.9)
        lh = lbl("more than 2×", (-1.2, base_y + 3.35), 44)
        self.play(FadeIn(lh), run_time=0.4)
        lp = lbl("per the cookbook", (-2.5, 2.05), 36)
        self.play(FadeIn(lp), run_time=0.4)
        until(self, "Each zoom is another round trip")
        S = rig_at(3.2, -2.0, 0.8, 1.6, 1.6)
        slabs = VGroup()
        for i in range(5):
            slabs.add(S.box(0, 0, i * 0.42, 1.6, 1.6, 0.36).set_z_index(3 + i))
        plin = S.box(-0.15, -0.15, -0.3, 1.9, 1.9, 0.3, DK_TOP, DK_L, DK_R).set_z_index(2)
        self.play(FadeIn(plin), run_time=0.3)
        for i in range(3):
            self.play(FadeIn(slabs[i], shift=DOWN * 0.4), run_time=0.35)
        lt = lbl("tokens", (5.3, -0.2), 40)
        self.play(FadeIn(lt), run_time=0.3)
        until(self, "You trade tokens and time")
        for i in range(3, 5):
            self.play(FadeIn(slabs[i], shift=DOWN * 0.4), run_time=0.35)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Chart, B01_Patches, B02_Resize, B03_Tool, B04_Ask, B05_Crop, B06_Magnify, B07_Again, B08_Loop, B09_Anywhere, B10_Payoff):
    _cls.play = ST.play
