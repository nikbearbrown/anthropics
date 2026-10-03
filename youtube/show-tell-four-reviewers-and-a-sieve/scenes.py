"""
Manim scenes for show-tell-four-reviewers-and-a-sieve (show-tell skill, card #31, Batch 2).
Titled "Five Reviewers and a Sieve": the plugin's command file launches five reviewers (the README summary says four).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The code-review plugin (anthropics/claude-plugins-official/plugins/code-review/, commands/code-review.md,
read raw from GitHub main on 2026-09-27): /code-review on a pull request -> 1 a Haiku agent checks eligibility
-> 2 a Haiku agent lists CLAUDE.md paths -> 3 a Haiku agent summarises -> 4 five parallel Sonnet reviewers
(CLAUDE.md rules, obvious bugs, git blame/history, earlier PRs' comments, code comments) -> 5 one Haiku
scorer per issue, 0-100, on a verbatim rubric -> 6 "Filter out any issues with a score less than 80"
-> 7 the eligibility check again -> 8 one brief comment via gh, each issue linked with the full SHA.
Cast (not the security-review film's PR crate on a belt, not #29's issue board): a kraft TABLE with the
pull request (a stack of white pages), five kraft REVIEWERS behind it, a checker and four tick boxes, the
CLAUDE.md list card, a row of finding SLIPS, a confidence RULER, the SIEVE (a mesh trough set at the
ruler's 80) over a BIN, and the PR COMMENT card that ends up on the table.
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







# ═════════════════════════════ the film: five reviewers and a sieve ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
CONN = "#9C8462"          # deep kraft for threads and cables (outside GATE T's ink mask)
TILE = "#B39A72"          # deep kraft
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (outside GATE T's ink tolerance)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=38):
    return T(s, size).move_to(P3(c)).set_z_index(20)


def llbl(s, x0, y, size=38):
    """A label left-aligned at x0."""
    t = T(s, size)
    return t.move_to(P3((x0 + t.width / 2.0, y))).set_z_index(20)


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.08):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def gbar(x0, x1, y, color=BAR1, w=6):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def drop(self, *mobs):
    for m in mobs:
        self.remove(*m.get_family())


# ─── the TABLE and the PULL REQUEST (a stack of white pages) ───
TW, TD, LEG, SLAB = 4.0, 2.4, 0.9, 0.18
TB = rig_at(-3.9, -0.35, 0.62, TW, TD)
ZT = LEG + SLAB


def table():
    legs = VGroup(*[TB.box(x, y, 0, 0.26, 0.26, LEG, DK_TOP, DK_L, DK_R, sw=0) for (x, y) in ((TW - 0.3, 0.04), (0.04, 0.04), (0.04, TD - 0.3))])
    top = TB.box(0, 0, LEG, TW, TD, SLAB)
    return VGroup(legs, top).set_z_index(1)


SX, SY, SW_, SD_ = 1.35, 0.55, 1.2, 1.35


def pr_stack():
    pages = VGroup(*[TB.page(SX, SY, ZT + i * 0.1, SW_, SD_) for i in range(3)])
    for pg in pages[:-1]:
        pg[2].set_opacity(0)          # only the top page shows its dot
    return pages.set_z_index(3)


STACK_C = np.array(TB.p(SX + SW_ / 2, SY + SD_ / 2, ZT + 0.3))


def summary_card():
    x0, y0 = SX + SW_ + 0.35, 0.7
    slab = TB.box(x0, y0, ZT, 0.75, 0.95, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = ZT + 0.05
    ls = VGroup(*[Line(TB.p(x0 + 0.15, y0 + 0.95 * f, zt), TB.p(x0 + 0.6, y0 + 0.95 * f, zt), color=BAR1, stroke_width=5) for f in (0.35, 0.65)])
    return VGroup(slab, ls).set_z_index(3)


# ─── the five REVIEWERS (behind the table) ───
RX = [-5.4, -4.65, -3.9, -3.15, -2.4]
RFOOT = 1.2


def reviewer(x, body=BOX_R):
    b = RoundedRectangle(width=0.5, height=0.66, corner_radius=0.22, fill_color=body, fill_opacity=1, stroke_color=INK,
                         stroke_width=4).move_to(P3((x, RFOOT + 0.33)))
    h = Circle(radius=0.19, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((x, RFOOT + 0.88)))
    return VGroup(b, h).set_z_index(0)


def reviewers():
    return VGroup(*[reviewer(x) for x in RX])


def head(i):
    return np.array([RX[i], RFOOT + 0.88, 0.0])


def rev_label(i, s):
    return lbl(s, (RX[i], 2.72), 38)


def spark(i):
    """The active reviewer's lamp: a terracotta dot on its chest."""
    return Dot(P3((RX[i], RFOOT + 0.36)), radius=0.08, color=TERRA).set_z_index(2)


def gaze(i):
    return Line(head(i) + np.array([0, -0.2, 0]), STACK_C + np.array([0, 0.05, 0]), color=BAR2, stroke_width=6).set_z_index(2)


# ─── the FINDING SLIPS (a row, top right) and their scores ───
SLOT_X = [1.0 + 0.85 * i for i in range(6)]
SLOT_Y = 2.35
SCORES = [90, 100, 75, 25, 50, 0]
SOURCE = [0, 1, 1, 2, 3, 4]           # which reviewer found each issue


def slip(c):
    c = P3(c)
    b = rrect(0.72, 0.44, c, PAGE_TOP, BAR1, 3, r=0.05)
    l1 = gbar(c[0] - 0.22, c[0] + 0.22, c[1] + 0.06, BAR1, 6)
    l2 = gbar(c[0] - 0.22, c[0] + 0.06, c[1] - 0.09, BAR2, 5)
    return VGroup(b, l1, l2).set_z_index(6)


def slot_slip(i):
    return slip((SLOT_X[i], SLOT_Y))


def score_num(i, y=None):
    return T(str(SCORES[i]), 36).move_to(P3((SLOT_X[i], (SLOT_Y + 0.6) if y is None else y))).set_z_index(20)


def scorer(i):
    return Circle(radius=0.17, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(
        P3((SLOT_X[i], SLOT_Y + 0.6))).set_z_index(7)


# ─── the RULER (confidence 0..100) ───
RUX, RY0, RK = -0.85, -2.6, 0.046


def ry(v):
    return RY0 + RK * v


def ruler_bar():
    return Rectangle(width=0.2, height=RK * 100 + 0.2, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(
        P3((RUX, ry(50)))).set_z_index(4)


def tick(v):
    return Line(P3((RUX - 0.1, ry(v))), P3((RUX + 0.22, ry(v))), color=INK, stroke_width=6).set_z_index(5)


def tick_num(v):
    return llbl(str(v), RUX + 0.36, ry(v), 34)


RUNGS = [0, 25, 50, 75, 100]


def ruler_full():
    return VGroup(ruler_bar(), *[tick(v) for v in RUNGS], *[tick_num(v) for v in RUNGS])


def cut_dot():
    return Dot(P3((RUX, ry(80))), radius=0.1, color=TERRA).set_z_index(6)


# ─── the SIEVE (a mesh trough set at 80) and the BIN under it ───
MX0, MX1 = 0.55, 5.45
MY = ry(80)                            # mesh top


def sieve():
    band = Rectangle(width=MX1 - MX0, height=0.26, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(
        P3(((MX0 + MX1) / 2, MY - 0.13)))
    hatch = VGroup(*[Line(P3((x, MY - 0.24)), P3((x, MY - 0.02)), color=BAR1, stroke_width=4)
                     for x in np.arange(MX0 + 0.2, MX1 - 0.1, 0.22)])
    posts = VGroup(*[Rectangle(width=0.18, height=MY - 0.26 - (-1.45), fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(
        P3((x, (MY - 0.26 + (-1.45)) / 2))) for x in (MX0 + 0.12, MX1 - 0.12)])
    return VGroup(posts, band, hatch).set_z_index(4)


BX0, BX1, BTOP, BBOT = 0.9, 5.1, -1.45, -2.95


def bin_back():
    return Rectangle(width=BX1 - BX0 - 0.2, height=0.25, fill_color=BOX_IN2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(
        P3(((BX0 + BX1) / 2 + 0.1, BTOP + 0.1))).set_z_index(3)


def bin_front():
    return Rectangle(width=BX1 - BX0, height=BTOP - BBOT, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(
        P3(((BX0 + BX1) / 2, (BTOP + BBOT) / 2))).set_z_index(8)


def sieve_group():
    return VGroup(bin_back(), sieve(), bin_front())


def eighty():
    return T("80", 52).move_to(P3((5.93, MY - 0.1))).set_z_index(20)


ON_MESH_Y = MY + 0.24


# ─── the GATE (the eligibility check), bottom strip ───
GCX = -3.6
GBX = [-3.05, -2.65, -2.25, -1.85]
GBY = -2.5


def checker():
    b = RoundedRectangle(width=0.4, height=0.52, corner_radius=0.17, fill_color=BAR2, fill_opacity=1, stroke_color=INK,
                         stroke_width=4).move_to(P3((GCX, -2.72)))
    h = Circle(radius=0.15, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((GCX, -2.28)))
    return VGroup(b, h).set_z_index(3)


def gboxes():
    return VGroup(*[Square(side_length=0.3, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((x, GBY)))
                    for x in GBX]).set_z_index(3)


def gticks():
    return VGroup(*[check(x, GBY, 0.1, INK, 5) for x in GBX]).set_z_index(4)


def gpass():
    return check(-1.35, GBY - 0.02, 0.2, TERRA, 9).set_z_index(4)


def gate_label(s="eligible?"):
    return lbl(s, (-2.45, -1.85), 38)


# ─── the CLAUDE.md list card, bottom left ───
LC = (-5.05, -2.45)


def list_card():
    c = P3(LC)
    b = rrect(1.65, 1.0, c, PAGE_TOP, INK, 4, r=0.06)
    rows = VGroup()
    for k, y in enumerate((0.26, 0.0, -0.26)):
        ic = Rectangle(width=0.14, height=0.18, fill_color=BOX_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(
            c + np.array([-0.58, y, 0]))
        ln = gbar(c[0] - 0.4, c[0] + (0.55, 0.3, 0.45)[k], c[1] + y, BAR1, 6)
        rows.add(VGroup(ic, ln))
    return VGroup(b, rows).set_z_index(3)


# ─── the PR COMMENT card ───
CC = (3.95, 2.55)


def comment_card():
    c = P3(CC)
    b = rrect(2.7, 1.1, c, PAGE_TOP, BAR1, 3, r=0.08)
    head_ = gbar(c[0] - 1.1, c[0] - 0.2, c[1] + 0.34, BAR1, 8)
    return VGroup(b, head_).set_z_index(6)


ROW_Y = [2.6, 2.2]


def crow(k):
    """A comment row: the issue line and its link line."""
    y = ROW_Y[k]
    return VGroup(gbar(CC[0] - 1.1, CC[0] + 0.5, y, BAR1, 6), gbar(CC[0] - 1.1, CC[0] + 1.0, y - 0.17, BAR3, 5)).set_z_index(7)


def cnum(k):
    return T(str(k + 1), 34).move_to(P3((CC[0] - 1.65, ROW_Y[k] - 0.08))).set_z_index(20)


def posted_card():
    """The comment, posted: a small card beside the table's front-right corner."""
    return comment_card().scale(0.4).move_to(P3((-1.6, -0.5))).set_z_index(4)


# ─── state at the START of each beat (continuity) ───
def state(k):
    d = {}
    if k >= 1:
        d["table"], d["stack"] = table(), pr_stack()
    if k >= 2:
        d["checker"], d["gboxes"], d["gticks"], d["gpass"] = checker(), gboxes(), gticks(), gpass()
    if k >= 3:
        d["list"] = list_card()
    if k >= 4:
        d["summary"] = summary_card()
    if k >= 5:
        d["revs"] = reviewers()
    n = {6: 1, 7: 3, 8: 4, 9: 5, 10: 6}
    ns = 6 if k >= 10 else n.get(k, 0)
    if k < 13:
        d["slips"] = VGroup(*[slot_slip(i) for i in range(ns)])
        if k >= 11:
            d["nums"] = VGroup(*[score_num(i) for i in range(6)])
    else:
        if k < 16:
            d["slips"] = VGroup(*[slip((SLOT_X[i], ON_MESH_Y)) for i in range(2)])
            d["nums"] = VGroup(*[score_num(i, ON_MESH_Y + 0.6) for i in range(2)])
    if k >= 12:
        d["ruler"] = ruler_full()
    if k >= 13:
        d["sieve"], d["dot"], d["eighty"] = sieve_group(), cut_dot(), eighty()
    if k >= 16:
        d["posted"] = posted_card()
    return d


ORDER = ["revs", "table", "stack", "summary", "posted", "checker", "gboxes", "gticks", "gpass", "list", "ruler", "dot",
         "sieve", "eighty", "slips", "nums"]


def add_state(self, d):
    for kk in ORDER:
        if kk in d:
            self.add(d[kk])


def world(self, k):
    d = state(k)
    add_state(self, d)
    return d


def fade_old(self, old, *more, rt=0.5):
    rt = guard(self, rt)
    self.play(FadeOut(old), *more, run_time=rt)


# ══════════════ B00: the table and the pull request ══════════════
def b00_labels():
    return VGroup(lbl("pull request", (-3.9, -1.9), 40), lbl("/code-review", (-3.9, -2.65), 40))


class B00_Table(Scene):
    def construct(self):
        tb = table()
        rt = guard(self, 0.8)
        self.play(FadeIn(tb, shift=UP * 0.4), run_time=rt)
        sh = Ellipse(width=3.2, height=0.5, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(P3((-3.9, -1.2))).set_z_index(0)
        rt = guard(self, 0.4)
        self.play(FadeIn(sh), run_time=rt)
        st = pr_stack()
        ls = b00_labels()
        start = st.copy().shift(LEFT * 2.2 + UP * 0.2)
        rt = guard(self, 0.3)
        self.play(FadeIn(start), run_time=rt)
        rt = guard(self, 0.8)
        self.play(start.animate.move_to(st.get_center()), run_time=rt)
        drop(self, start)
        self.add(st)
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        until(self, "It adds one command", lead=0.0)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[1], shift=UP * 0.2), run_time=rt)
        until(self, "It uses the GitHub command line tool", lead=0.2)
        cur = cursor(-1.0, -2.1).set_z_index(21)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.7)
        self.play(cur.animate.move_to(STACK_C + np.array([0.25, -0.2, 0])), run_time=rt)
        until(self, "and to post back to it", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Indicate(st, color=None, scale_factor=1.08), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeOut(cur), FadeOut(sh), run_time=rt)
        done(self)


# ══════════════ B01: step one, eligible? ══════════════
class B01_Eligible(Scene):
    def construct(self):
        d = world(self, 1)
        old = b00_labels()
        self.add(old)
        ch, bx = checker(), gboxes()
        gl = gate_label()
        rt = guard(self, 0.6)
        self.play(FadeOut(old), FadeIn(ch, shift=UP * 0.3), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeIn(bx), FadeIn(gl), run_time=rt)
        th = gticks()
        until(self, "If it's closed", lead=0.2)
        for k, ph in enumerate(("closed", "a draft", "automated", "already has a review")):
            until(self, ph, lead=0.15)
            rt = guard(self, 0.35)
            self.play(Create(th[k]), run_time=rt)
        until(self, "the command stops right there", lead=0.4)
        gp = gpass()
        rt = guard(self, 0.5)
        self.play(Create(gp), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(d["stack"], color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B02: step two, the CLAUDE.md paths ══════════════
def b02_labels():
    return VGroup(lbl("CLAUDE.md", (-4.65, -1.62), 36))


class B02_Paths(Scene):
    def construct(self):
        d = world(self, 2)
        old = gate_label()
        self.add(old)
        lc = list_card()
        ls = b02_labels()
        rt = guard(self, 0.6)
        self.play(FadeOut(old), FadeIn(lc[0], shift=UP * 0.3), FadeIn(ls[0]), run_time=rt)
        until(self, "the one at the root", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(lc[1][0], shift=RIGHT * 0.2), run_time=rt)
        until(self, "and any in the folders", lead=0.2)
        rt = guard(self, 0.6)
        self.play(FadeIn(lc[1][1], shift=RIGHT * 0.2), FadeIn(lc[1][2], shift=RIGHT * 0.2), run_time=rt)
        until(self, "It returns their paths", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*[r[1] for r in lc[1]]), color=None, scale_factor=1.1), run_time=rt)
        until(self, "not their contents", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*[r[0] for r in lc[1]]), color=None, scale_factor=1.3), run_time=rt)
        done(self)


# ══════════════ B03: step three, the summary ══════════════
def b03_labels():
    return VGroup(lbl("summary", (-1.6, -0.8), 38))


class B03_Summary(Scene):
    def construct(self):
        d = world(self, 3)
        old = b02_labels()
        self.add(old)
        rt = guard(self, 0.4)
        self.play(FadeOut(old), Indicate(d["stack"], color=None, scale_factor=1.06), run_time=rt)
        sc = summary_card()
        start = sc.copy().move_to(STACK_C)
        rt = guard(self, 0.3)
        self.play(FadeIn(start), run_time=rt)
        rt = guard(self, 0.8)
        self.play(start.animate.move_to(sc.get_center()), run_time=rt)
        drop(self, start)
        self.add(sc)
        ls = b03_labels()
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        done(self)


# ══════════════ B04: five reviewers, in parallel ══════════════
def b04_labels():
    return VGroup(lbl("five reviewers", (-3.9, 2.72), 40))


class B04_Five(Scene):
    def construct(self):
        d = world(self, 4)
        old = b03_labels()
        self.add(old)
        rt = guard(self, 0.4)
        self.play(FadeOut(old), run_time=rt)
        until(self, "Five Sonnet agents", lead=0.2)
        rv = reviewers()
        rt = guard(self, 0.6)
        self.play(*[GrowFromEdge(r, DOWN) for r in rv], run_time=rt)
        ls = b04_labels()
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        until(self, "each one reviews the change", lead=0.2)
        gz = VGroup(*[gaze(i) for i in range(5)])
        rt = guard(self, 0.7)
        self.play(*[Create(g) for g in gz], run_time=rt)
        until(self, "Each returns a list of issues", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(d["stack"], color=None, scale_factor=1.06), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeOut(gz), run_time=rt)
        done(self)


# ══════════════ B05–B09: one reviewer each ══════════════
def reviewer_beat(self, k, i, name, cue_find, n_new, extra=None, cue_extra=None):
    """Reviewer i lights, looks at the pull request, and sends n_new slips to the row."""
    d = world(self, k)
    olds = {5: b04_labels(), 6: VGroup(rev_label(0, "rules")), 7: VGroup(rev_label(1, "bugs")),
            8: VGroup(rev_label(2, "git history")), 9: VGroup(rev_label(3, "old PRs"))}
    old = olds[k]
    self.add(old)
    sp = spark(i)
    lab = rev_label(i, name)
    rt = guard(self, 0.5)
    self.play(FadeOut(old), GrowFromCenter(sp), d["revs"][i][0].animate.set_fill(TILE), FadeIn(lab), run_time=rt)
    gz = gaze(i)
    rt = guard(self, 0.5)
    self.play(Create(gz), run_time=rt)
    if extra is not None:
        until(self, cue_extra, lead=0.2)
        extra(self, d)
    until(self, cue_find, lead=0.3)
    have = len(d["slips"])
    for j in range(n_new):
        s = slot_slip(have + j)
        start = s.copy().scale(0.6).move_to(head(i) + np.array([0.2, 0.1, 0]))
        rt = guard(self, 0.2)
        self.play(FadeIn(start), run_time=rt)
        rt = guard(self, 0.6)
        self.play(start.animate.scale(1 / 0.6).move_to(s.get_center()), run_time=rt)
        drop(self, start)
        self.add(s)
    return d, sp, gz


def reviewer_end(self, d, i, sp, gz, *more):
    rt = guard(self, 0.5)
    self.play(FadeOut(sp), FadeOut(gz), d["revs"][i][0].animate.set_fill(BOX_R), *[FadeOut(m) for m in more], run_time=rt)
    done(self)


class B05_Rules(Scene):
    def construct(self):
        def ex(self, d):
            th = Line(np.array(d["list"].get_top()) + np.array([0, 0.02, 0]), np.array([RX[0] - 0.1, RFOOT + 0.02, 0]), color=CONN, stroke_width=6).set_z_index(2)
            self.th = th
            rt = guard(self, 0.6)
            self.play(Create(th), Indicate(d["list"], color=None, scale_factor=1.06), run_time=rt)
        d, sp, gz = reviewer_beat(self, 5, 0, "rules", "not every rule applies", 1, ex, "against the Claude dot M D rules")
        reviewer_end(self, d, 0, sp, gz, self.th)


def lens(c):
    c = P3(c)
    ring = Circle(radius=0.3, stroke_color=INK, stroke_width=7, fill_color=PAGE_TOP, fill_opacity=1).move_to(c)
    glint = Arc(radius=0.18, start_angle=PI * 0.6, angle=PI * 0.5, arc_center=c, color=BAR2, stroke_width=6)
    dv = np.array([0.707, -0.707, 0])
    handle = Line(c + dv * 0.3, c + dv * 0.62, color=INK, stroke_width=12)
    return VGroup(ring, glint, handle).set_z_index(12)


class B06_Bugs(Scene):
    def construct(self):
        def ex(self, d):
            ln = lens(STACK_C + np.array([-0.6, 0.15, 0]))
            self.ln = ln
            rt = guard(self, 0.4)
            self.play(FadeIn(ln), run_time=rt)
            rt = guard(self, 1.0)
            self.play(ln.animate.shift(RIGHT * 1.1), run_time=rt)
        d, sp, gz = reviewer_beat(self, 6, 1, "bugs", "Large bugs only", 2, ex, "does a shallow scan")
        reviewer_end(self, d, 1, sp, gz, self.ln)


def history_line():
    """A short commit line lying on the table, left of the pull request."""
    x = 0.35
    ln = Line(TB.p(x, 0.3, ZT), TB.p(x, 2.1, ZT), color=BAR1, stroke_width=8).set_z_index(3)
    dots = VGroup(*[Dot(TB.p(x, y, ZT), radius=0.09, color=BAR1).set_z_index(4) for y in (0.5, 1.1, 1.7)])
    return ln, dots


class B07_History(Scene):
    def construct(self):
        def ex(self, d):
            ln, dots = history_line()
            self.hl = VGroup(ln, dots)
            rt = guard(self, 0.6)
            self.play(Create(ln), run_time=rt)
            rt = guard(self, 0.6)
            self.play(LaggedStart(*[GrowFromCenter(x) for x in dots], lag_ratio=0.3), run_time=rt)
        d, sp, gz = reviewer_beat(self, 7, 2, "git history", "in light of that history", 1, ex, "git blame and history")
        reviewer_end(self, d, 2, sp, gz, self.hl)


def old_prs():
    """Two older pull requests: small kraft pages lying on the table, left of the stack."""
    return VGroup(*[TB.box(0.3 + 0.15 * j, 0.5 + 0.5 * j, ZT + 0.05 * j, 0.75, 0.95, 0.05, BOX_TOP, BOX_L, BOX_R, sw=2) for j in range(2)]).set_z_index(3)


class B08_OldPRs(Scene):
    def construct(self):
        def ex(self, d):
            op = old_prs()
            self.op = op
            rt = guard(self, 0.6)
            self.play(FadeIn(op, shift=RIGHT * 0.4), run_time=rt)
        d, sp, gz = reviewer_beat(self, 8, 3, "old PRs", "checks whether the comments", 1, ex, "earlier pull requests")
        reviewer_end(self, d, 3, sp, gz, self.op)


def bubble(c):
    c = P3(c)
    b = RoundedRectangle(width=0.9, height=0.55, corner_radius=0.2, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    tail = Polygon(c + np.array([-0.22, -0.26, 0]), c + np.array([-0.02, -0.26, 0]), c + np.array([-0.32, -0.5, 0]),
                   fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ls = VGroup(gbar(c[0] - 0.28, c[0] + 0.28, c[1] + 0.07, BAR1, 6), gbar(c[0] - 0.28, c[0] + 0.1, c[1] - 0.09, BAR2, 5))
    return VGroup(tail, b, ls).set_z_index(12)


class B09_Comments(Scene):
    def construct(self):
        def ex(self, d):
            bb = bubble(STACK_C + np.array([-1.35, 0.35, 0]))
            self.bb = bb
            rt = guard(self, 0.6)
            self.play(GrowFromCenter(bb), run_time=rt)
        d, sp, gz = reviewer_beat(self, 9, 4, "code comments", "follows what those comments say", 1, ex, "the code comments")
        reviewer_end(self, d, 4, sp, gz, self.bb)


# ══════════════ B10: step five, one scorer per issue ══════════════
def b10_labels():
    return VGroup(llbl("confidence", SLOT_X[5] + 0.5 - T("confidence", 38).width, 1.55, 38))


class B10_Score(Scene):
    def construct(self):
        d = world(self, 10)
        old = VGroup(rev_label(4, "code comments"))
        self.add(old)
        rt = guard(self, 0.4)
        self.play(FadeOut(old), run_time=rt)
        until(self, "Each one gets its own Haiku agent", lead=0.2)
        sc = VGroup(*[scorer(i) for i in range(6)])
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in sc], lag_ratio=0.12), run_time=rt)
        ls = b10_labels()
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        until(self, "from zero to a hundred", lead=0.5)
        nums = VGroup(*[score_num(i) for i in range(6)])
        rt = guard(self, 0.7)
        self.play(*[FadeOut(s, scale=0.4) for s in sc], *[FadeIn(n, scale=0.6) for n in nums], run_time=rt)
        until(self, "For a rules issue", lead=0.2)
        th = Line(np.array(d["list"].get_right()) + np.array([0.05, 0.2, 0]), np.array(d["slips"][0].get_bottom()) + np.array([-0.1, -0.05, 0]),
                  color=CONN, stroke_width=6).set_z_index(2)
        rt = guard(self, 0.7)
        self.play(Create(th), run_time=rt)
        until(self, "really calls it out", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Indicate(VGroup(d["slips"][0], nums[0]), color=None, scale_factor=1.12), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(th), run_time=rt)
        done(self)


# ══════════════ B11: the scale, word for word ══════════════
class B11_Scale(Scene):
    def construct(self):
        d = world(self, 11)
        old = b10_labels()
        self.add(old)
        bar = ruler_bar()
        rt = guard(self, 0.6)
        self.play(FadeOut(old), GrowFromEdge(bar, DOWN), run_time=rt)
        cues = {0: "Zero:", 25: "Twenty five", 50: "Fifty", 75: "Seventy five", 100: "A hundred"}
        mk = Triangle(fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3).scale(0.13).rotate(-PI / 2).move_to(
            P3((RUX - 0.32, ry(0)))).set_z_index(6)
        for v in RUNGS:
            until(self, cues[v], lead=0.2)
            anims = [Create(tick(v)), FadeIn(tick_num(v))]
            if v == 0:
                anims.append(FadeIn(mk))
            else:
                anims.append(mk.animate.move_to(P3((RUX - 0.32, ry(v)))))
            rt = guard(self, 0.5)
            self.play(*anims, run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(mk), run_time=rt)
        done(self)


# ══════════════ B12: the sieve at 80 ══════════════
class B12_Sieve(Scene):
    def construct(self):
        d = world(self, 12)
        dot = cut_dot()
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(dot), run_time=rt)
        sg = sieve_group()
        e8 = eighty()
        rt = guard(self, 0.8)
        self.play(FadeIn(sg, shift=UP * 0.3), FadeIn(e8), run_time=rt)
        until(self, "is filtered out", lead=0.6)
        grp = [VGroup(d["slips"][i], d["nums"][i]) for i in range(6)]
        rt = guard(self, 0.8)
        self.play(*[g.animate.shift(DOWN * (SLOT_Y - ON_MESH_Y)) for g in grp], run_time=rt, rate_func=ease_in)
        for i in (3, 5, 4):
            rt = guard(self, 0.5)
            self.play(grp[i][0].animate.move_to(P3((SLOT_X[i], -2.3))), FadeOut(grp[i][1]), run_time=rt, rate_func=ease_in)
            drop(self, grp[i])
        until(self, "still falls through", lead=0.5)
        rt = guard(self, 0.4)
        self.play(Indicate(grp[2][1], color=None, scale_factor=1.25), run_time=rt)
        rt = guard(self, 0.6)
        self.play(grp[2][0].animate.move_to(P3((SLOT_X[2], -2.3))), FadeOut(grp[2][1]), run_time=rt, rate_func=ease_in)
        drop(self, grp[2])
        until(self, "stays on the mesh", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(grp[0], grp[1]), color=None, scale_factor=1.12), run_time=rt)
        done(self)


# ══════════════ B13: what scores low ══════════════
def b13_labels():
    return VGroup(lbl("pre-existing", (2.3, 0.4), 38), lbl("nitpicks", (4.15, -0.6), 38), lbl("linter's job", (2.0, -0.6), 38))


class B13_Noise(Scene):
    def construct(self):
        d = world(self, 13)
        rt = guard(self, 0.4)
        self.play(Indicate(d["slips"], color=None, scale_factor=1.08), run_time=rt)
        ls = b13_labels()
        cues = ("pre-existing issues", "nitpicks a senior", "anything a linter")
        xs = (4.1, 5.0, 3.25)
        for k in range(3):
            until(self, cues[k], lead=0.3)
            g = slip((xs[k], ON_MESH_Y)).set_opacity(0.55)
            rt = guard(self, 0.3)
            self.play(FadeIn(g), run_time=rt)
            rt = guard(self, 0.6)
            self.play(g.animate.move_to(P3((xs[k], -2.3))), FadeIn(ls[k]), run_time=rt, rate_func=ease_in)
            drop(self, g)
        until(self, "on lines the pull request didn't change", lead=0.2)
        g = slip((2.3, ON_MESH_Y)).set_opacity(0.55)
        rt = guard(self, 0.3)
        self.play(FadeIn(g), run_time=rt)
        rt = guard(self, 0.6)
        self.play(g.animate.move_to(P3((2.3, -2.3))), run_time=rt, rate_func=ease_in)
        drop(self, g)
        done(self)


# ══════════════ B14: step seven, the second look ══════════════
class B14_Recheck(Scene):
    def construct(self):
        d = world(self, 14)
        old = b13_labels()
        self.add(old)
        rt = guard(self, 0.5)
        self.play(FadeOut(old), Indicate(d["slips"], color=None, scale_factor=1.08), run_time=rt)
        until(self, "If something does", lead=0.3)
        gl = gate_label("still eligible?")
        rt = guard(self, 0.5)
        self.play(FadeOut(d["gticks"]), FadeOut(d["gpass"]), FadeIn(gl), run_time=rt)
        th = gticks()
        until(self, "repeats the first check", lead=0.3)
        for k in range(4):
            rt = guard(self, 0.3)
            self.play(Create(th[k]), run_time=rt)
        until(self, "closed or reviewed", lead=0.2)
        gp = gpass()
        rt = guard(self, 0.5)
        self.play(Create(gp), run_time=rt)
        done(self)


# ══════════════ B15: step eight, the comment ══════════════
def b15_labels():
    return VGroup(lbl("PR comment", (3.95, 1.72), 38))


class B15_Comment(Scene):
    def construct(self):
        d = world(self, 15)
        old = gate_label("still eligible?")
        self.add(old)
        cc = comment_card()
        ls = b15_labels()
        rt = guard(self, 0.6)
        self.play(FadeOut(old), FadeIn(cc, shift=DOWN * 0.3), FadeIn(ls[0]), run_time=rt)
        rows = VGroup(crow(0), crow(1))
        nums = VGroup(cnum(0), cnum(1))
        for k in range(2):
            s = d["slips"][k]
            rt = guard(self, 0.7)
            self.play(s.animate.scale(0.5).move_to(rows[k][0].get_center()), *([FadeOut(d["nums"])] if k == 0 else []), run_time=rt)
            drop(self, s)
            rt = guard(self, 0.4)
            self.play(FadeIn(rows[k][0]), FadeIn(nums[k]), run_time=rt)
        until(self, "cites each issue with a link", lead=0.3)
        rt = guard(self, 0.7)
        self.play(Create(rows[0][1]), Create(rows[1][1]), run_time=rt)
        until(self, "using the full commit hash", lead=0.3)
        allc = VGroup(cc, rows, nums)
        pc = posted_card()
        rt = guard(self, 0.9)
        self.play(FadeOut(ls[0]), allc.animate.scale(0.4).move_to(pc.get_center()), run_time=rt)
        drop(self, allc)
        self.add(pc)
        rt = guard(self, 0.3)
        self.play(Indicate(pc, color=None, scale_factor=1.2), run_time=rt)
        done(self)


# ══════════════ B16: two files, and where the 80 lives ══════════════
def fpage(c):
    c = P3(c)
    b = Rectangle(width=1.0, height=1.25, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    ls = VGroup(*[gbar(c[0] - 0.3, c[0] + 0.3 - 0.12 * (k % 2), c[1] + 0.35 - 0.24 * k, BAR2, 6) for k in range(4)])
    return VGroup(b, ls).set_z_index(6)


class B16_TwoFiles(Scene):
    def construct(self):
        d = world(self, 16)
        p1, p2 = fpage((1.2, 2.45)), fpage((4.35, 2.45))
        l1, l2 = lbl("README", (1.2, 1.58), 38), lbl("command file", (4.35, 1.58), 38)
        n1, n2 = T("4", 60).move_to(P3((2.05, 2.45))).set_z_index(20), T("5", 60).move_to(P3((5.2, 2.45))).set_z_index(20)
        rt = guard(self, 0.6)
        self.play(FadeIn(p1, shift=DOWN * 0.3), FadeIn(l1), run_time=rt)
        until(self, "describes four reviewers", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(n1, scale=0.6), run_time=rt)
        until(self, "The command file", lead=0.3)
        rt = guard(self, 0.6)
        self.play(FadeIn(p2, shift=DOWN * 0.3), FadeIn(l2), run_time=rt)
        until(self, "launches five", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(n2, scale=0.6), run_time=rt)
        until(self, "where the eighty lives", lead=0.3)
        cur = cursor(4.6, 0.3).set_z_index(21)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.7)
        self.play(cur.animate.move_to(np.array(d["eighty"].get_center()) + np.array([-0.1, -0.38, 0])), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(d["eighty"], color=None, scale_factor=1.08), Indicate(d["dot"], color=None, scale_factor=1.5), run_time=rt)
        until(self, "change the threshold there", lead=0.3)
        rt = guard(self, 0.6)
        self.play(cur.animate.move_to(np.array(p2.get_center()) + np.array([0.2, -0.2, 0])), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(p2, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Table, B01_Eligible, B02_Paths, B03_Summary, B04_Five, B05_Rules, B06_Bugs, B07_History, B08_OldPRs,
             B09_Comments, B10_Score, B11_Scale, B12_Sieve, B13_Noise, B14_Recheck, B15_Comment, B16_TwoFiles):
    _cls.play = ST.play
