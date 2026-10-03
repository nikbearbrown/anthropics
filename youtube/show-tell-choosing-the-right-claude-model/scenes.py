"""
Manim scenes for show-tell-choosing-the-right-claude-model (show-tell skill; Bear's order of 2026-09-27).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The one idea: there is no single best Claude model; you match the model to the job, and you make
that call, one task at a time. Source: Anthropic's "Choosing the right Claude model" guide
(six screenshots, SOURCE-SCREENSHOTS.md) and the live developer docs page (sources/).
Cast (one small cast, whole film): YOU (a grey figure, left); FOUR kraft FILE FOLDERS standing in a
row (Haiku, Sonnet, Opus, Fable), told apart by the names beneath them and their staggered tabs,
never by colour (the screenshots' sage and lilac are off-palette); TASK SLIPS that get filed; ONE
terracotta SPARK on the tab of the folder being chosen, which travels folder to folder; and, per beat,
where the task comes from (a long email, a study, a chain of steps) and the pointer.
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






# ═════════════════════════════ the film: choosing the right Claude model ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
CONN = "#9C8462"          # deep kraft for arrows and connectors (outside GATE T's ink mask)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def lbl(s, c, size=40):
    return T(s, size).move_to(P3(c))


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.08):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def gbar(x0, x1, y, color=BAR1, w=6):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def drop(self, *mobs):
    for m in mobs:
        self.remove(*m.get_family())


# ─── YOU: a grey figure at the left ───
YX, YY = -5.15, -1.3


def figure():
    body = RoundedRectangle(width=1.2, height=1.1, corner_radius=0.5, fill_color=BAR1, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to(P3((YX, YY)))
    head = Circle(radius=0.32, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((YX, YY + 0.95)))
    return VGroup(body, head).set_z_index(2)


def you_label():
    return lbl("you", (YX, YY - 0.98), 40)


# ─── the FOUR FOLDERS: kraft file folders standing in a row, tabs staggered ───
NAMES = ["Haiku", "Sonnet", "Opus", "Fable"]
FS = 1.1                          # iso scale
FW, FD, FH, FHF = 1.7, 0.16, 2.0, 1.75   # width (along x), gap between leaves, back-leaf height, front-leaf height
TW, TH = 0.6, 0.36                # tab width and height
TX = [0.06, 0.36, 0.66, 0.96]      # tab offsets: one step further along per folder, like a real file drawer
FOY = -2.25                       # every folder stands on the same floor line
FOX = [-3.0, -0.6, 1.8, 4.2]     # rig origins, left to right: Haiku, Sonnet, Opus, Fable
FOX_ONE = 0.6                     # B00: the one "best" folder stands alone at the centre


def rig(i, ox=None):
    return Iso(FOX[i] if ox is None else ox, FOY, FS)


def folder(i, ox=None):
    """(shadow, back leaf with its tab, side strip, front leaf). Contents go between back (z1) and front (z3)."""
    R = rig(i, ox)
    tx = TX[i]
    shadow = R.quad([(-0.08, -0.12, 0), (FW + 0.12, -0.12, 0), (FW + 0.12, FD + 0.3, 0), (-0.08, FD + 0.3, 0)], GHOST, sw=0)
    back = Polygon(*[R.p(*q) for q in [(0, FD, 0), (FW, FD, 0), (FW, FD, FH), (tx + TW + 0.06, FD, FH), (tx + TW, FD, FH + TH),
                                        (tx + 0.04, FD, FH + TH), (tx - 0.02, FD, FH), (0, FD, FH)]],
                   fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4)
    side = R.quad([(0, 0, 0), (0, FD, 0), (0, FD, FHF), (0, 0, FHF)], BOX_IN1, sw=3)
    front = R.quad([(0, 0, 0), (FW, 0, 0), (FW, 0, FHF), (0, 0, FHF)], BOX_R, sw=4)
    shadow.set_z_index(0); back.set_z_index(1); side.set_z_index(3); front.set_z_index(3)
    return VGroup(shadow, back, side, front)


def tab_c(i, ox=None):
    return np.array(rig(i, ox).p(TX[i] + TW / 2 + 0.01, FD, FH + TH * 0.5))


def slot_top(i):
    """Screen point just above the folder's opening, between the leaves."""
    return np.array(rig(i).p(FW / 2, FD / 2, FH)) + np.array([0, 0.75, 0])


def inside(i):
    """Screen point where a filed slip sits hidden behind the front leaf."""
    return np.array(rig(i).p(FW / 2, FD / 2, 0)) + np.array([0, 0.95, 0])


def name_c(i, ox=None):
    o = FOX[i] if ox is None else ox
    return (o + 0.81, FOY - 0.7)


def name_label(i):
    """Names hang from one top line, so a descender ('Opus') doesn't lift its label out of the row."""
    t = lbl(NAMES[i], name_c(i), 40)
    return t.shift(UP * (name_c(i)[1] + 0.17 - float(np.array(t.get_top())[1])))


def names():
    return VGroup(*[name_label(i) for i in range(4)])


def spark(i):
    return Dot(tab_c(i), radius=0.1, color=TERRA).set_z_index(5)


# ─── task slips ───
def slip(c, s=1.0):
    c = P3(c)
    s = s * 1.15
    b = rrect(0.8 * s, 0.48 * s, c, PAGE_TOP, INK, 3, r=0.05)
    l1 = gbar(c[0] - 0.25 * s, c[0] + 0.25 * s, c[1] + 0.05 * s, BAR1, 6)
    l2 = gbar(c[0] - 0.25 * s, c[0] + 0.08 * s, c[1] - 0.1 * s, BAR2, 5)
    return VGroup(b, l1, l2).set_z_index(6)


ROW_Y = 2.5
ROW = [(-4.4, ROW_Y), (-3.2, ROW_Y), (-2.0, ROW_Y)]     # slips waiting above the figure, lined up in a row


def file_into(self, s, src, i, rt=0.8):
    """Arc a slip from screen point src to just above folder i, then drop it in behind the front leaf."""
    top = slot_top(i)
    self.play(MoveAlongPath(s, ArcBetweenPoints(P3(src), top, angle=-PI / 4)), run_time=guard(self, rt))
    s.set_z_index(2)
    self.play(s.animate.move_to(inside(i)), run_time=guard(self, 0.35))
    drop(self, s)


def move_spark_anim(sp, a, b):
    """The one terracotta spark hops from folder a's tab to folder b's tab (arcing up, over the row)."""
    return MoveAlongPath(sp, ArcBetweenPoints(tab_c(a), tab_c(b), angle=-PI / 3 if b > a else PI / 3))


def move_spark(self, sp, a, b, rt=0.6):
    self.play(move_spark_anim(sp, a, b), run_time=guard(self, rt))


def cursor_at(c, s=0.55):
    x, y = c
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).set_z_index(12)


def lens(c):
    c = P3(c)
    ring = Circle(radius=0.36, stroke_color=INK, stroke_width=7, fill_color=PAGE_TOP, fill_opacity=1).move_to(c)
    glint = Arc(radius=0.22, start_angle=PI * 0.6, angle=PI * 0.5, arc_center=c, color=BAR2, stroke_width=6)
    d = np.array([0.707, -0.707, 0])
    handle = Line(c + d * 0.36, c + d * 0.72, color=INK, stroke_width=12)
    return VGroup(ring, glint, handle).set_z_index(12)


# ─── B02: the long email ───
EM_C = (-3.3, 2.3)


def email():
    c = P3(EM_C)
    b = rrect(1.5, 1.75, c, PAGE_TOP, INK, 4)
    flap = VGroup(Line(c + np.array([-0.72, 0.85, 0]), c + np.array([0, 0.45, 0]), color=BAR1, stroke_width=5),
                  Line(c + np.array([0, 0.45, 0]), c + np.array([0.72, 0.85, 0]), color=BAR1, stroke_width=5))
    ls = VGroup(*[gbar(c[0] - 0.5, c[0] - 0.5 + w, c[1] + dy, BAR2, 6)
                  for w, dy in ((1.0, 0.18), (0.8, 0.0), (0.95, -0.18), (0.6, -0.36), (0.9, -0.54), (0.7, -0.72))])
    return VGroup(b, flap, ls).set_z_index(4)


DATE_C = (-3.3, 2.0)          # where the one-date slip lifts from (over the email's lines)
DATE_UP = (-1.3, 2.5)         # where it waits, beside the email


# ─── B04: the study (a thick stack of pages) ───
ST_R = Iso(-3.55, 1.55, 0.66)


def study():
    return VGroup(*[ST_R.box(0, 0, 0.2 * k, 1.5, 1.1, 0.18, PAGE_TOP, PAGE_L, PAGE_R, sw=3) for k in range(4)]).set_z_index(4)


STUDY_TOP = np.array(ST_R.p(0.75, 0.55, 0.78))
STUDY_C = (-3.55, 2.3)


# ─── B05: the chain of connected steps ───
CH_Y = 2.55
CH_X = [-3.9, -2.7, -1.5, -0.3, 0.9]


def step_tile(k):
    return Square(side_length=0.55, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((CH_X[k], CH_Y))).set_z_index(5)


def link(k):
    return Line(P3((CH_X[k] + 0.32, CH_Y)), P3((CH_X[k + 1] - 0.32, CH_Y)), color=CONN, stroke_width=7).set_z_index(4)


# ─── B07: step arrows above the tabs ───
STEP_UP_L, STEP_DN_L = (-1.45, 2.55), (1.25, 2.55)


def step_arrow(a, b):
    pa = tab_c(a) + np.array([0.15 if b > a else -0.15, 0.55, 0])
    pb = tab_c(b) + np.array([-0.15 if b > a else 0.15, 0.55, 0])
    return CurvedArrow(pa, pb, angle=-PI / 3 if b > a else PI / 3, color=CONN, stroke_width=9, tip_length=0.26).set_z_index(4)


# ══════════════ B00: one best model ══════════════
class B00_OneBest(Scene):
    def construct(self):
        you, ly = figure(), you_label()
        f = folder(3, FOX_ONE)
        lb = lbl("best?", name_c(3, FOX_ONE), 40)
        self.play(FadeIn(you, shift=UP * 0.3), FadeIn(ly), run_time=guard(self, 0.6))
        self.play(FadeIn(f, shift=DOWN * 0.3), FadeIn(lb), run_time=guard(self, 0.6))
        slips = [slip(c) for c in ROW]
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.2) for s in slips], lag_ratio=0.3), run_time=guard(self, 0.7))
        R = Iso(FOX_ONE, FOY, FS)
        top = np.array(R.p(FW / 2, FD / 2, FH)) + np.array([0, 0.75, 0])
        ins = np.array(R.p(FW / 2, FD / 2, 0)) + np.array([0, 0.95, 0])
        for k, ph in enumerate(("The quick question", "The everyday draft", "The hard problem")):
            until(self, ph, lead=0.15)
            self.play(MoveAlongPath(slips[k], ArcBetweenPoints(P3(ROW[k]), top, angle=-PI / 4)), run_time=guard(self, 0.7))
            slips[k].set_z_index(2)
            self.play(slips[k].animate.move_to(ins), run_time=guard(self, 0.3))
            drop(self, slips[k])
        until(self, "the picture the guide replaces", lead=0.2)
        self.play(Indicate(f, color=None, scale_factor=1.06), run_time=guard(self, 0.6))
        done(self)


# ══════════════ B01: four folders ══════════════
class B01_FourFolders(Scene):
    def construct(self):
        you, ly = figure(), you_label()
        f = folder(3, FOX_ONE)
        lb = lbl("best?", name_c(3, FOX_ONE), 40)
        self.add(you, ly, f, lb)
        self.play(FadeOut(lb), run_time=guard(self, 0.4))
        self.play(f.animate.shift(RIGHT * (FOX[3] - FOX_ONE)), run_time=guard(self, 0.8))
        for i, ph in enumerate(("Haiku, for", "Sonnet, for", "Opus, for")):
            until(self, ph, lead=0.35)
            nf = folder(i)
            self.play(FadeIn(nf, shift=RIGHT * 0.5), FadeIn(name_label(i)), run_time=guard(self, 0.5))
        until(self, "And Fable", lead=0.2)
        self.play(FadeIn(name_label(3)), Indicate(f, color=None, scale_factor=1.05), run_time=guard(self, 0.5))
        done(self)


def base(self, spark_on=None):
    """Everything on stage between beats: you, the four folders, their names (and the spark, if any)."""
    you, ly = figure(), you_label()
    fs = VGroup(*[folder(i) for i in range(4)])
    nm = names()
    self.add(fs, you, ly, nm)
    sp = None
    if spark_on is not None:
        sp = spark(spark_on)
        self.add(sp)
    return you, fs, nm, sp


# ══════════════ B02: Haiku ══════════════
class B02_Haiku(Scene):
    def construct(self):
        you, fs, nm, _ = base(self)
        until(self, "most efficient model", lead=0.3)
        sp = spark(0)
        ring = Circle(radius=0.26, stroke_color=GHOST, stroke_width=6).move_to(tab_c(0)).set_z_index(4)
        self.play(GrowFromCenter(sp), GrowFromCenter(ring), Indicate(fs[0], color=None, scale_factor=1.05), run_time=guard(self, 0.6))
        self.play(FadeOut(ring), run_time=guard(self, 0.3))
        until(self, "Straightforward questions", lead=0.2)
        em = email()
        le = lbl("email", (EM_C[0] - 1.55, EM_C[1]), 40)
        self.play(FadeIn(em, shift=DOWN * 0.3), FadeIn(le), run_time=guard(self, 0.6))
        until(self, "pulling specific info", lead=0.2)
        ln = lens((EM_C[0] + 0.9, EM_C[1] + 0.9))
        self.play(FadeIn(ln), run_time=guard(self, 0.3))
        self.play(ln.animate.move_to(P3((EM_C[0] + 0.2, EM_C[1] - 0.1))), run_time=guard(self, 0.6))
        until(self, "Say you need one date", lead=0.2)
        ds = slip(DATE_C, 0.8)
        ld = lbl("one date", (DATE_UP[0] + 1.55, DATE_UP[1]), 40)
        self.play(FadeOut(ln), FadeIn(ds), run_time=guard(self, 0.3))
        self.play(ds.animate.move_to(P3(DATE_UP)), FadeIn(ld), run_time=guard(self, 0.5))
        until(self, "That's a Haiku job", lead=0.9)
        self.play(FadeOut(ld), run_time=guard(self, 0.2))
        file_into(self, ds, DATE_UP, 0, 0.6)
        self.play(Indicate(sp, color=None, scale_factor=1.6), run_time=guard(self, 0.3))
        done(self)


# ══════════════ B03: Sonnet ══════════════
class B03_Sonnet(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 0)
        old = VGroup(email(), lbl("email", (EM_C[0] - 1.55, EM_C[1]), 40))
        self.add(old)
        self.play(FadeOut(old), run_time=guard(self, 0.5))
        until(self, "Sonnet, the guide says", lead=0.1)
        move_spark(self, sp, 0, 1, 0.6)
        self.play(Indicate(fs[1], color=None, scale_factor=1.05), run_time=guard(self, 0.5))
        until(self, "Writing and creating", lead=0.2)
        slips = [slip(c) for c in ROW]
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.2) for s in slips], lag_ratio=0.3), run_time=guard(self, 0.8))
        for k, ph in enumerate(("Drafting a blog post", "Fixing an ordinary bug", "Sorting through survey")):
            until(self, ph, lead=0.15)
            file_into(self, slips[k], ROW[k], 1, 0.7)
        self.play(Indicate(sp, color=None, scale_factor=1.8), run_time=guard(self, 0.4))
        done(self)


# ══════════════ B04: Opus ══════════════
class B04_Opus(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 1)
        until(self, "Opus. The guide", lead=0.5)
        move_spark(self, sp, 1, 2, 0.6)
        self.play(Indicate(fs[2], color=None, scale_factor=1.05), run_time=guard(self, 0.5))
        until(self, "Complex research", lead=0.2)
        stdy = study()
        self.play(FadeIn(stdy, shift=DOWN * 0.3), run_time=guard(self, 0.6))
        until(self, "the methods of a study", lead=0.3)
        ls = lbl("a study", (-1.45, 2.4), 40)
        ln = lens(STUDY_TOP + np.array([-0.6, 0.35, 0]))
        self.play(FadeIn(ls), FadeIn(ln), run_time=guard(self, 0.4))
        self.play(ln.animate.move_to(STUDY_TOP + np.array([0.5, 0.2, 0])), run_time=guard(self, 0.7))
        until(self, "whether its conclusion holds", lead=0.3)
        self.play(FadeOut(ln), FadeOut(ls), run_time=guard(self, 0.3))
        dst = slot_top(2)
        self.play(stdy.animate.scale(0.45).move_to(dst), run_time=guard(self, 0.7))
        stdy.set_z_index(2)
        self.play(stdy.animate.move_to(inside(2)), run_time=guard(self, 0.3))
        drop(self, stdy)
        self.play(Indicate(sp, color=None, scale_factor=1.8), run_time=guard(self, 0.4))
        done(self)


# ══════════════ B05: Fable ══════════════
class B05_Fable(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 2)
        until(self, "Fable. The guide", lead=0.4)
        move_spark(self, sp, 2, 3, 0.6)
        self.play(Indicate(fs[3], color=None, scale_factor=1.05), run_time=guard(self, 0.5))
        until(self, "takes planning", lead=0.3)
        tiles = [step_tile(k) for k in range(5)]
        links = [link(k) for k in range(4)]
        self.play(FadeIn(tiles[0], shift=UP * 0.2), run_time=guard(self, 0.35))
        for k in range(4):
            self.play(Create(links[k]), FadeIn(tiles[k + 1], shift=RIGHT * 0.2), run_time=guard(self, 0.3))
        until(self, "Long-horizon tasks", lead=0.2)
        lm = lbl("many steps", (CH_X[4] + 1.65, CH_Y), 40)
        self.play(FadeIn(lm), run_time=guard(self, 0.4))
        until(self, "Dense source material", lead=0.2)
        stk = VGroup(*[Square(side_length=0.5, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=3)
                       .move_to(P3((CH_X[0] - 0.06 * j, CH_Y - 0.72 + 0.06 * j))) for j in range(3)]).set_z_index(5)
        self.play(FadeIn(stk, shift=DOWN * 0.2), run_time=guard(self, 0.4))
        until(self, "Building something from a rough idea", lead=0.3)
        chain = VGroup(*tiles, *links, stk)
        self.play(FadeOut(lm), run_time=guard(self, 0.25))
        self.play(chain.animate.scale(0.25).move_to(slot_top(3)), run_time=guard(self, 0.8))
        chain.set_z_index(2)
        self.play(chain.animate.move_to(inside(3)), run_time=guard(self, 0.3))
        drop(self, chain)
        self.play(Indicate(sp, color=None, scale_factor=1.8), run_time=guard(self, 0.4))
        done(self)


# ══════════════ B06: problems Opus struggled with ══════════════
class B06_Struggled(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 3)
        until(self, "problems that Opus", lead=0.4)
        s = slip(inside(2)).set_z_index(2)
        self.play(FadeIn(s), run_time=guard(self, 0.2))          # appears hidden behind Opus's front leaf
        up = slot_top(2) + np.array([0, 0.7, 0])
        self.play(s.animate.move_to(up), run_time=guard(self, 0.5))
        s.set_z_index(6)
        q = T("?", 60).move_to(up + np.array([0.9, 0.15, 0])).set_z_index(9)
        self.play(FadeIn(q), run_time=guard(self, 0.3))
        for dx in (0.12, -0.24, 0.24, -0.12):
            self.play(s.animate.shift(RIGHT * dx), run_time=guard(self, 0.1))
        until(self, "When a hard problem beats Opus", lead=0.2)
        self.play(FadeOut(q), run_time=guard(self, 0.3))
        until(self, "the guide points you", lead=0.2)
        top = slot_top(3)
        self.play(MoveAlongPath(s, ArcBetweenPoints(up, top, angle=-PI / 3)), run_time=guard(self, 0.7))
        s.set_z_index(2)
        self.play(s.animate.move_to(inside(3)), run_time=guard(self, 0.3))
        drop(self, s)
        ring = Circle(radius=0.3, stroke_color=GHOST, stroke_width=6).move_to(tab_c(3)).set_z_index(4)
        self.play(GrowFromCenter(ring), Indicate(sp, color=None, scale_factor=1.6), run_time=guard(self, 0.35))
        self.play(FadeOut(ring), run_time=guard(self, 0.2))   # a new shape late in the beat (Gate A: shapes must change)
        done(self)


# ══════════════ B07: step up, step down ══════════════
class B07_StepUpDown(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 3)
        until(self, "Start from the job", lead=0.3)
        s = slip(ROW[1])
        self.play(FadeIn(s, shift=UP * 0.2), Indicate(you, color=None, scale_factor=1.06), run_time=guard(self, 0.5))
        until(self, "Start with an efficient model", lead=0.2)
        move_spark(self, sp, 3, 0, 0.6)
        file_into(self, s, ROW[1], 0, 0.7)
        until(self, "upgrade only if", lead=0.2)
        s = slip(inside(0)).set_z_index(2)
        self.add(s)
        self.play(s.animate.move_to(slot_top(0)), run_time=guard(self, 0.4))
        s.set_z_index(6)
        a1 = step_arrow(0, 1)
        l1 = lbl("step up", STEP_UP_L, 40)
        self.play(Create(a1), FadeIn(l1), run_time=guard(self, 0.5))
        self.play(MoveAlongPath(s, ArcBetweenPoints(slot_top(0), slot_top(1), angle=-PI / 3)), move_spark_anim(sp, 0, 1), run_time=guard(self, 0.6))
        s.set_z_index(2)
        self.play(s.animate.move_to(inside(1)), run_time=guard(self, 0.3))
        drop(self, s)
        until(self, "Or start with the strongest", lead=0.2)
        s = slip(ROW[1])
        self.play(FadeIn(s, shift=UP * 0.2), run_time=guard(self, 0.35))
        self.play(MoveAlongPath(s, ArcBetweenPoints(P3(ROW[1]), slot_top(2), angle=-PI / 4)), move_spark_anim(sp, 1, 2), run_time=guard(self, 0.7))
        until(self, "and move down over time", lead=0.6)
        a2 = step_arrow(2, 1)
        l2 = lbl("step down", STEP_DN_L, 40)
        self.play(Create(a2), FadeIn(l2), run_time=guard(self, 0.45))
        self.play(MoveAlongPath(s, ArcBetweenPoints(slot_top(2), slot_top(1), angle=PI / 3)), move_spark_anim(sp, 2, 1), run_time=guard(self, 0.6))
        s.set_z_index(2)
        self.play(s.animate.move_to(inside(1)), run_time=guard(self, 0.3))
        drop(self, s)
        done(self)


# ══════════════ B08: you choose ══════════════
class B08_YouChoose(Scene):
    def construct(self):
        you, fs, nm, sp = base(self, 1)
        old = VGroup(step_arrow(0, 1), step_arrow(2, 1), lbl("step up", STEP_UP_L, 40), lbl("step down", STEP_DN_L, 40))
        self.add(old)
        cur = cursor_at((5.4, 2.6))
        self.play(FadeOut(old), FadeIn(cur), run_time=guard(self, 0.4))
        tgt = tab_c(2) + np.array([0.08, -0.02, 0])
        self.play(cur.animate.move_to(tgt + np.array([0.17, -0.2, 0])), run_time=guard(self, 0.8))
        self.play(Indicate(cur, color=None, scale_factor=0.85), move_spark_anim(sp, 1, 2), run_time=guard(self, 0.5))
        until(self, "one task at a time", lead=0.3)
        s = slip(ROW[1])
        self.play(FadeIn(s, shift=UP * 0.2), run_time=guard(self, 0.3))
        self.play(FadeOut(cur), run_time=guard(self, 0.2))
        file_into(self, s, ROW[1], 2, 0.7)
        until(self, "There's the right one", lead=0.2)
        self.play(Indicate(you, color=None, scale_factor=1.08), Indicate(sp, color=None, scale_factor=1.8), run_time=guard(self, 0.6))
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_OneBest, B01_FourFolders, B02_Haiku, B03_Sonnet, B04_Opus, B05_Fable, B06_Struggled,
             B07_StepUpDown, B08_YouChoose):
    _cls.play = ST.play
