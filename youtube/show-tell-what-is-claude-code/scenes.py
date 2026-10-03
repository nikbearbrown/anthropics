"""
Manim scenes for show-tell-what-is-claude-code (show-tell skill; Bear's order of 2026-09-27).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The one idea: Claude Code is not a smarter autocomplete; it is an agent you hand a whole task to.
It plans, reads your code, runs commands and tests, edits files and keeps going; you direct and review.
Sources: claude.com/product/claude-code (SOURCE-PASTE.md) and the live docs overview (sources/).
Cast (one small cast, whole film): YOU (a grey figure, left), the AGENT (a dark block with a
terracotta spark, 'Claude Code'), the TASK ticket above it, the CODEBASE (a kraft tray of code pages,
lower right), the TEST LAMP, the PR card; for the page's worked example, the PAY button, the GATEWAY
(a dark block), charge slips and their idempotency-key tags, and coins.
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





# ═════════════════════════════ the film: what is Claude Code ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
CONN = "#9C8462"          # deep kraft for cables, paths and arrows (outside GATE T's ink mask)
TILE = "#B39A72"          # deep kraft
PATHC = "#A8927A"         # light kraft for lines drawn ON pages inside the tray (luminance > 130, so GATE T does not read them as text)
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (outside GATE T's ink tolerance)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


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


def xmark(c, s=0.2, w=8):
    c = P3(c)
    return VGroup(Line(c + np.array([-s, -s, 0]), c + np.array([s, s, 0]), color=INK, stroke_width=w),
                  Line(c + np.array([-s, s, 0]), c + np.array([s, -s, 0]), color=INK, stroke_width=w)).set_z_index(8)


# ─── YOU: a grey figure at the left ───
YX, YY = -5.0, -1.35


def figure():
    body = RoundedRectangle(width=1.2, height=1.1, corner_radius=0.5, fill_color=BAR1, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to(P3((YX, YY)))
    head = Circle(radius=0.32, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((YX, YY + 0.95)))
    return VGroup(body, head).set_z_index(2)


def you_label():
    return lbl("you", (YX, YY - 0.98), 40)


# ─── the AGENT: Claude Code, a dark block with a terracotta spark ───
AG = rig_at(-1.6, -1.75, 0.8, 1.6, 1.6)
AGH = 1.0
AG_TOP = np.array(AG.p(1.6, 1.6, AGH))         # top vertex of the block
AG_SPARK = np.array(AG.p(0.8, 0.8, AGH))
AG_RIGHT = np.array(AG.p(1.6, 0.4, 0.6))        # a point on the right front face


def agent():
    body = AG.box(0, 0, 0, 1.6, 1.6, AGH, DK_TOP, DK_L, DK_R)
    ports = VGroup(*[AG.box(1.6 * f, -0.12, 0.3, 0.26, 0.12, 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.22, 0.6)])
    spark = Dot(AG_SPARK, radius=0.11, color=TERRA)
    return VGroup(body, ports, spark).set_z_index(1)


def agent_label():
    return lbl("Claude Code", (-1.6, -2.85), 40)


# ─── the TASK ticket ───
TK = (-1.6, 0.55)
TK_YOU = (-4.3, 0.8)


def ticket(c=TK):
    c = P3(c)
    base = rrect(1.5, 0.95, c, PAGE_TOP, INK, 4)
    title = gbar(c[0] - 0.5, c[0] + 0.45, c[1] + 0.2, BAR1, 10)
    l1 = gbar(c[0] - 0.5, c[0] + 0.55, c[1] - 0.05, BAR2, 7)
    l2 = gbar(c[0] - 0.5, c[0] + 0.25, c[1] - 0.27, BAR2, 7)
    dot = Dot(c + np.array([-0.58, 0.2, 0]), radius=0.07, color=TERRA)
    return VGroup(base, title, l1, l2, dot).set_z_index(4)


PLAN_C = (-1.6, 0.9)
PLAN_ROWS = [0.2, -0.12, -0.44]


def plan_card():
    c = P3(PLAN_C)
    base = rrect(1.7, 1.55, c, PAGE_TOP, INK, 4)
    dot = Dot(c + np.array([-0.6, 0.5, 0]), radius=0.07, color=TERRA)
    head = gbar(c[0] - 0.42, c[0] + 0.55, c[1] + 0.5, BAR1, 10)
    rows = VGroup()
    for k, y in enumerate(PLAN_ROWS):
        bx = Square(side_length=0.2, fill_color=GHOST, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(c + np.array([-0.55, y, 0]))
        ln = gbar(c[0] - 0.3, c[0] - 0.3 + (0.85, 0.65, 0.75)[k], c[1] + y, BAR2, 7)
        rows.add(VGroup(bx, ln))
    return VGroup(base, dot, head, rows).set_z_index(4)


def plan_tick(k):
    c = P3(PLAN_C)
    return check(c[0] - 0.55, c[1] + PLAN_ROWS[k], 0.1, INK, 5).set_z_index(6)


# ─── the CODEBASE: a kraft tray of code pages, lower right ───
CBW, CBD, CBH = 3.0, 1.5, 0.32
CB = rig_at(2.75, -2.05, 0.62, CBW, CBD)
PGW, PGD = 0.5, 1.05


def cb_page(i):
    return CB.page(0.2 + 0.68 * i, 0.22, 0.03, PGW, PGD).set_z_index(1)


def cb_page_c(i):
    return np.array(CB.p(0.2 + 0.68 * i + PGW / 2, 0.22 + PGD / 2, 0.09))


def tray():
    back, front = CB.open_box(0, 0, 0, CBW, CBD, CBH)
    pages = VGroup(*[cb_page(i) for i in range(4)])
    return VGroup(back, pages, front)


# ─── the TEST LAMP ───
LX, LY = 0.55, -1.0


def lamp(lit=False):
    plinth = Rectangle(width=0.5, height=0.16, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(P3((LX, -2.45)))
    post = Rectangle(width=0.14, height=1.2, fill_color=DK_R, fill_opacity=1, stroke_width=0).move_to(P3((LX, -1.85)))
    bulb = Circle(radius=0.27, fill_color=TERRA if lit else GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((LX, LY)))
    return VGroup(plinth, post, bulb).set_z_index(2)


MARK_C = (1.12, -1.0)


# ─── helpers: lens, cursor, slips, keys, coins ───
def lens(c):
    c = P3(c)
    ring = Circle(radius=0.36, stroke_color=INK, stroke_width=7, fill_color=PAGE_TOP, fill_opacity=1).move_to(c)
    glint = Arc(radius=0.22, start_angle=PI * 0.6, angle=PI * 0.5, arc_center=c, color=BAR2, stroke_width=6)
    d = np.array([0.707, -0.707, 0])
    handle = Line(c + d * 0.36, c + d * 0.72, color=INK, stroke_width=12)
    return VGroup(ring, glint, handle).set_z_index(12)


def term(c, w=1.4, h=0.95):
    c = P3(c)
    body = RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(c)
    x0 = c[0] - w / 2 + 0.22
    chev = VGroup(Line(c + np.array([x0 - c[0], 0.14, 0]), c + np.array([x0 - c[0] + 0.14, 0.0, 0]), color=GHOST, stroke_width=7),
                  Line(c + np.array([x0 - c[0] + 0.14, 0.0, 0]), c + np.array([x0 - c[0], -0.14, 0]), color=GHOST, stroke_width=7))
    cur = Rectangle(width=0.16, height=0.26, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(c + np.array([x0 - c[0] + 0.4, 0.0, 0]))
    return VGroup(body, chev).set_z_index(3), cur.set_z_index(4)


def slip(c, s=1.0):
    c = P3(c)
    b = rrect(0.9 * s, 0.5 * s, c, PAGE_TOP, INK, 3, r=0.05)
    l1 = gbar(c[0] - 0.28 * s, c[0] + 0.28 * s, c[1], BAR1, 6)
    return VGroup(b, l1).set_z_index(6)


def key(c, s=1.0, teeth=1, fill=TILE):
    c = P3(c)
    ring = Circle(radius=0.15 * s, stroke_color=INK, stroke_width=7, fill_color=fill, fill_opacity=1).move_to(c)
    shaft = Line(c + np.array([0.15 * s, 0, 0]), c + np.array([0.62 * s, 0, 0]), color=INK, stroke_width=8)
    t = VGroup(*[Line(c + np.array([x * s, 0, 0]), c + np.array([x * s, -0.14 * s, 0]), color=INK, stroke_width=8)
                 for x in ((0.55,) if teeth == 1 else (0.42, 0.56))])
    return VGroup(ring, shaft, t).set_z_index(7)


def coin(c):
    c = P3(c)
    return VGroup(Circle(radius=0.26, fill_color=TILE, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=5).move_to(c),
                  Circle(radius=0.14, stroke_color=BOX_L, stroke_width=5).move_to(c)).set_z_index(5)


# ─── the page's example: PAY button and the GATEWAY ───
PAY_C = (0.7, 1.35)


def pay_button(grey=False):
    return RoundedRectangle(width=1.4, height=0.6, corner_radius=0.3, fill_color=BAR3 if grey else BOX_TOP, fill_opacity=1,
                            stroke_color=BAR1 if grey else INK, stroke_width=4).move_to(P3(PAY_C)).set_z_index(3)


GW = rig_at(4.6, 0.75, 0.7, 1.3, 1.3)
GW_IN = np.array(GW.p(0, 0.65, 0.45)) + np.array([-0.1, 0, 0])
GW_OUT = np.array(GW.p(0.65, 0, 0.1))


def gateway():
    body = GW.box(0, 0, 0, 1.3, 1.3, 0.9, DK_TOP, DK_L, DK_R)
    slot = GW.quad([(0, 0.3, 0.38), (0, 1.0, 0.38), (0, 1.0, 0.54), (0, 0.3, 0.54)], GHOST, stroke=CONN, sw=2)
    return VGroup(body, slot).set_z_index(1)


SL_A, SL_B = (2.3, 1.75), (2.3, 0.85)
KEY_DX = 0.7
COIN_A, COIN_B = (4.3, -0.4), (4.95, -0.4)
COIN_FIX = (5.4, -0.4)


def diff_card(c=(2.2, -0.3)):
    c = P3(c)
    b = rrect(1.7, 0.9, c, PAGE_TOP, INK, 4)
    l1 = gbar(c[0] - 0.55, c[0] + 0.5, c[1] + 0.15, BAR1, 8)
    l2 = gbar(c[0] - 0.55, c[0] + 0.2, c[1] - 0.15, BAR2, 7)
    return VGroup(b, l1, l2).set_z_index(6)


# ─── the big codebase (B07) ───
MBW, MBD, MBH = 4.6, 1.6, 0.3
MB = rig_at(2.3, 1.05, 0.62, MBW, MBD)


def big_tray():
    back, front = MB.open_box(0, 0, 0, MBW, MBD, MBH)
    pages = VGroup(*[MB.page(0.2 + 0.72 * i, 0.25, 0.03, 0.5, 1.1).set_z_index(1) for i in range(6)])
    return VGroup(back, pages, front), pages


def mb_c(i):
    return np.array(MB.p(0.2 + 0.72 * i + 0.25, 0.25 + 0.55, 0.09))


# ─── the PR card ───
PR_C = (4.9, 0.4)


def pr_card():
    c = P3(PR_C)
    b = rrect(1.7, 0.95, c, BOX_TOP, INK, 4)
    l1 = gbar(c[0] - 0.55, c[0] + 0.5, c[1] + 0.15, BAR1, 8)
    l2 = gbar(c[0] - 0.55, c[0] + 0.2, c[1] - 0.15, BAR2, 7)
    return VGroup(b, l1, l2).set_z_index(3)


# ─── the doors (B10) ───
DOOR_Y = 2.05
DOOR_X = [-4.6, -2.8, -1.0, 0.8, 2.6, 4.4]


def door(i):
    x, y = DOOR_X[i], DOOR_Y
    c = P3((x, y))
    if i == 0:      # terminal
        g, cur = term((x, y), 1.1, 0.75)
        return VGroup(g, cur)
    if i == 1:      # editor: window with a side bar
        b = rrect(1.1, 0.75, c, PAGE_TOP, INK, 4)
        side = Rectangle(width=0.22, height=0.62, fill_color=BAR3, fill_opacity=1, stroke_width=0).move_to(c + np.array([-0.38, 0, 0]))
        ls = VGroup(*[gbar(x - 0.15, x + dx, y + dy, BAR2, 6) for dx, dy in ((0.35, 0.18), (0.2, 0.0), (0.4, -0.18))])
        return VGroup(b, side, ls).set_z_index(3)
    if i == 2:      # desktop app: a monitor on a stand
        b = rrect(1.1, 0.68, c + np.array([0, 0.08, 0]), PAGE_TOP, INK, 4)
        stand = Rectangle(width=0.14, height=0.16, fill_color=TILE, fill_opacity=1, stroke_width=0).move_to(c + np.array([0, -0.34, 0]))
        foot = Rectangle(width=0.5, height=0.08, fill_color=TILE, fill_opacity=1, stroke_width=0).move_to(c + np.array([0, -0.43, 0]))
        spark = Dot(c + np.array([0, 0.08, 0]), radius=0.08, color=TERRA)
        return VGroup(b, stand, foot, spark).set_z_index(3)
    if i == 3:      # web: a browser window, grey top band
        b = rrect(1.1, 0.75, c, PAGE_TOP, INK, 4)
        band = Rectangle(width=1.0, height=0.14, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(c + np.array([0, 0.24, 0]))
        ls = VGroup(*[gbar(x - 0.35, x + dx, y + dy, BAR2, 6) for dx, dy in ((0.35, 0.0), (0.15, -0.18))])
        return VGroup(b, band, ls).set_z_index(3)
    if i == 4:      # phone
        b = RoundedRectangle(width=0.48, height=0.8, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1,
                             stroke_color=INK, stroke_width=4).move_to(c)
        spk = gbar(x - 0.08, x + 0.08, y + 0.28, BAR1, 5)
        ls = VGroup(*[gbar(x - 0.13, x + 0.13, y + dy, BAR2, 5) for dy in (0.05, -0.1)])
        return VGroup(b, spk, ls).set_z_index(3)
    # chat bubble (Slack)
    b = rrect(1.1, 0.62, c + np.array([0, 0.06, 0]), BOX_TOP, INK, 4, r=0.16)
    tail = Polygon(P3((x - 0.3, y - 0.24)), P3((x - 0.05, y - 0.24)), P3((x - 0.35, y - 0.42)),
                   fill_color=BOX_TOP, fill_opacity=1, stroke_width=0)
    dots = VGroup(*[Dot(P3((x + dx, y + 0.06)), radius=0.06, color=BAR1) for dx in (-0.25, 0, 0.25)])
    return VGroup(b, tail, dots).set_z_index(3)


def cable(i):
    a = P3((-1.6 + 0.09 * (i - 2.5), 0.02))
    b = P3((DOOR_X[i], DOOR_Y - 0.5))
    return Line(a, b, color=CONN, stroke_width=6).set_z_index(0)


# ─── B12: commands, the barrier, the terminal ───
CMD_Y = 2.05
TERM12_C = (4.95, CMD_Y)
BAR_X = 2.35


def cmd(x, risky=False):
    c = P3((x, CMD_Y))
    if risky:
        b = RoundedRectangle(width=0.62, height=0.36, corner_radius=0.06, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(c)
        return VGroup(b, Dot(c, radius=0.07, color=TERRA)).set_z_index(6)
    return rrect(0.62, 0.36, c, BOX_TOP, INK, 3, r=0.06).set_z_index(6)


ARM_DOWN, ARM_UP = CMD_Y - 0.75, CMD_Y - 0.1


def barrier(up=False):
    """(arm, sleeve): a kraft arm in a dark sleeve below the path; raised, it crosses the path."""
    arm = Rectangle(width=0.2, height=1.0, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    arm.move_to(P3((BAR_X, ARM_UP if up else ARM_DOWN)))
    sleeve = Rectangle(width=0.42, height=0.7, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(P3((BAR_X, CMD_Y - 0.9)))
    return arm.set_z_index(5), sleeve.set_z_index(6)


# ─── B13: plan tags ───
def tag(c):
    x, y = c
    t = Polygon(P3((x - 0.35, y + 0.19)), P3((x + 0.4, y + 0.19)), P3((x + 0.4, y - 0.19)), P3((x - 0.35, y - 0.19)), P3((x - 0.55, y)),
                fill_color=TILE, fill_opacity=1, stroke_color=INK, stroke_width=4)
    hole = Dot(P3((x - 0.32, y)), radius=0.05, color=INK)
    return VGroup(t, hole).set_z_index(5)


TAG_PRO, TAG_MAX = (-3.35, 1.55), (-3.35, 0.75)


# ─── state at the start of each beat (continuity) ───
def state(k):
    """Everything on stage at the START of beat Bk, without labels."""
    d = {"you": figure(), "agent": agent()}
    if k >= 1:
        d["ticket"] = ticket()
    if k >= 2:
        d["tray"] = tray()
    if k == 2:
        d["lens"] = lens(cb_page_c(0) + np.array([0.0, 0.25, 0]))
        d["edit"] = VGroup(rrect(1.2, 1.3, (3.0, 0.75), PAGE_TOP, INK, 4),
                           *[gbar(2.6, 2.6 + w, 0.75 + dy, BAR2 if n < 3 else BAR1, 7) for n, (w, dy) in
                             enumerate(((0.75, 0.35), (0.55, 0.12), (0.7, -0.11), (0.6, -0.34)))]).set_z_index(4)
        g, cur = term((5.2, 0.75))
        d["term"] = VGroup(g, cur)
    if k == 3:
        d["ticket"] = VGroup(plan_card(), *[plan_tick(i) for i in range(3)])
    if k in (4, 5, 6, 7):
        d["pay"] = pay_button(grey=(k == 7))
        d["gw"] = gateway()
    if k == 4:
        d["coins"] = VGroup(coin(COIN_A), coin(COIN_B))
    if k >= 5:
        d["lamp"] = lamp(lit=(k in (5, 9, 10, 11, 12, 13)))
    if k == 6:
        d["coins"] = VGroup(coin(COIN_A), coin(COIN_B))
    if k == 7:
        d["coins"] = coin(COIN_FIX)
        d["diff"] = diff_card()
    if k == 8:
        bt, _pg = big_tray()
        d["big"] = bt
        d["map"] = map_diagram()
    if k == 9:
        d["pr"] = pr_card()
    if k == 10:
        d["mark"] = check(MARK_C[0], MARK_C[1], 0.2).set_z_index(8)
    if k == 11:
        d.pop("ticket")
        d["doors"] = VGroup(*[door(i) for i in range(6)])
        d["cables"] = VGroup(*[cable(i) for i in range(6)])
    if k == 12:
        d["diff"] = diff_card(TK_YOU)
        d["rmark"] = check(TK_YOU[0] + 1.15, TK_YOU[1], 0.2).set_z_index(8)
    if k == 13:
        g, cur = term(TERM12_C)
        d["term"] = VGroup(g, cur)
        arm, base = barrier(up=True)
        d["barrier"] = VGroup(arm, base)
        d["risky"] = cmd(BAR_X - 0.62, True)
    return d


ORDER = ["cables", "big", "map", "tray", "lamp", "you", "agent", "ticket", "pay", "gw", "coins", "diff", "pr",
         "lens", "edit", "term", "doors", "mark", "rmark", "barrier", "risky"]


def add_state(self, d):
    for kk in ORDER:
        if kk in d:
            self.add(d[kk])


MAP_EDGES = [(0, 1), (1, 3), (0, 2), (3, 4), (4, 5), (2, 4)]
MAP_NODES = [(4.55, 2.25), (5.2, 2.25), (4.55, 1.45), (5.85, 2.25), (5.85, 1.45), (5.2, 1.45)]   # page i -> node i


def map_node(i):
    return Dot(P3(MAP_NODES[i]), radius=0.13, color=BAR1).set_z_index(4)


def map_edge(a, b):
    return Line(P3(MAP_NODES[a]), P3(MAP_NODES[b]), color=PATHC, stroke_width=6).set_z_index(3)


def map_diagram():
    """The map Claude builds, drawn BESIDE the codebase: lines drawn over the pages break the pages
    off the tray's ink outline and GATE T reads them as stacked labels (2026-09-27 pre-check)."""
    return VGroup(*[map_edge(a, b) for a, b in MAP_EDGES], *[map_node(i) for i in range(6)])


# ══════════════ B00: the hand-off ══════════════
class B00_Handoff(Scene):
    def construct(self):
        you, ag = figure(), agent()
        ly, la = you_label(), agent_label()
        rt = guard(self, 0.8)
        self.play(FadeIn(you, shift=UP * 0.3), FadeIn(ag, shift=DOWN * 0.3), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeIn(ly), FadeIn(la), run_time=rt)
        until(self, "Hand Claude a bug fix", lead=0.3)
        tk = ticket(TK_YOU)
        lt = lbl("task", (TK_YOU[0], TK_YOU[1] + 0.85), 40)
        rt = guard(self, 0.5)
        self.play(FadeIn(tk[0], shift=UP * 0.2), FadeIn(tk[4]), FadeIn(lt), run_time=rt)
        for i, ph in enumerate(("a bug fix", "a test", "a multi-day migration")):
            until(self, ph, lead=0.15)
            rt = guard(self, 0.35)
            self.play(Create(tk[1 + i]), run_time=rt)
        until(self, "Then steer and review", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(you, color=None, scale_factor=1.08), run_time=rt)
        until(self, "hand it over", lead=0.5)
        rt = guard(self, 1.0)
        self.play(MoveAlongPath(tk, ArcBetweenPoints(P3(TK_YOU), P3(TK), angle=-PI / 4)), FadeOut(lt), run_time=rt)
        until(self, "Claude Code does the work", lead=0.2)
        ring = Circle(radius=0.3, stroke_color=GHOST, stroke_width=6).move_to(AG_SPARK).set_z_index(2)
        rt = guard(self, 0.6)
        self.play(Indicate(ag[2], color=None, scale_factor=1.8), GrowFromCenter(ring), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(ring), run_time=rt)
        done(self)


# ══════════════ B01: reads, edits, runs ══════════════
class B01_Hands(Scene):
    def construct(self):
        d = state(1)
        add_state(self, d)
        old = VGroup(you_label(), agent_label())
        self.add(old)
        tr = tray()
        rt = guard(self, 0.8)
        self.play(FadeOut(old), FadeIn(tr, shift=LEFT * 0.4), run_time=rt)
        until(self, "It reads your codebase", lead=0.3)
        ln = lens(cb_page_c(0) + np.array([-0.4, 0.9, 0]))
        lr = lbl("reads", (0.85, -0.95), 40)
        rt = guard(self, 0.5)
        self.play(FadeIn(ln), FadeIn(lr), run_time=rt)
        rt = guard(self, 0.6)
        self.play(ln.animate.move_to(cb_page_c(0) + np.array([0.0, 0.25, 0])), run_time=rt)
        until(self, "It edits files", lead=0.3)
        page = rrect(1.2, 1.3, (3.0, 0.75), PAGE_TOP, INK, 4).set_z_index(4)
        ls = VGroup(*[gbar(2.6, 2.6 + w, 0.75 + dy, BAR2, 7) for w, dy in ((0.75, 0.35), (0.55, 0.12), (0.7, -0.11))]).set_z_index(4)
        le = lbl("edits", (3.0, 1.75), 40)
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(page, ls), shift=UP * 0.4), FadeIn(le), run_time=rt)
        newl = gbar(2.6, 3.2, 0.41, BAR1, 7).set_z_index(5)
        rt = guard(self, 0.5)
        self.play(Create(newl), run_time=rt)
        edit = VGroup(page, ls, newl)
        until(self, "And it runs commands", lead=0.3)
        g, cur = term((5.2, 0.75))
        lu = lbl("runs", (5.2, 1.6), 40)
        rt = guard(self, 0.6)
        self.play(FadeIn(g, shift=UP * 0.3), FadeIn(lu), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        until(self, "like your tests", lead=0.2)
        rt = guard(self, 0.4)
        self.play(cur.animate.set_opacity(0.2), run_time=rt)
        rt = guard(self, 0.3)
        self.play(cur.animate.set_opacity(1), run_time=rt)
        until(self, "This takes the steps itself", lead=0.3)
        rt = guard(self, 0.9)
        self.play(LaggedStart(Indicate(ln, color=None, scale_factor=1.15), Indicate(edit, color=None, scale_factor=1.06),
                              Indicate(g, color=None, scale_factor=1.06), lag_ratio=0.35), run_time=rt)
        done(self)


# ══════════════ B02: a plan and questions ══════════════
def b01_labels():
    return VGroup(lbl("reads", (0.85, -0.95), 40), lbl("edits", (3.0, 1.75), 40), lbl("runs", (5.2, 1.6), 40))


class B02_Plan(Scene):
    def construct(self):
        d = state(2)
        add_state(self, d)
        old = b01_labels()
        self.add(old)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(old, d["lens"], d["edit"], d["term"])), run_time=rt)
        pc = plan_card()
        lp = lbl("plan", (0.05, PLAN_C[1]), 40)
        rt = guard(self, 0.7)
        self.play(FadeOut(d["ticket"]), FadeIn(pc, shift=UP * 0.15), FadeIn(lp), run_time=rt)
        until(self, "asks clarifying questions", lead=0.3)
        q = T("?", 60).move_to(P3((-3.15, -0.45))).set_z_index(9)
        rt = guard(self, 0.3)
        self.play(FadeIn(q), run_time=rt)
        rt = guard(self, 0.7)
        self.play(q.animate.move_to(P3((YX + 0.9, YY + 1.55))), run_time=rt)
        until(self, "and handles work", lead=0.2)
        rt = guard(self, 0.3)
        self.play(FadeOut(q), Indicate(d["you"], color=None, scale_factor=1.06), run_time=rt)
        for k in range(3):
            rt = guard(self, 0.4)
            self.play(Create(plan_tick(k)), run_time=rt)
        done(self)


# ══════════════ B03: the page's example, the bug ══════════════
def b03_labels():
    return VGroup(lbl("pay", (PAY_C[0], PAY_C[1] + 0.68), 40), lbl("gateway", (4.6, 2.35), 40))


class B03_Bug(Scene):
    def construct(self):
        d = state(3)
        add_state(self, d)
        old = lbl("plan", (0.05, PLAN_C[1]), 40)
        self.add(old)
        tk = ticket(TK_YOU)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(old, d["ticket"])), FadeIn(tk, shift=UP * 0.2), run_time=rt)
        until(self, "The request reads", lead=0.3)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(tk, ArcBetweenPoints(P3(TK_YOU), P3(TK), angle=-PI / 4)), run_time=rt)
        pb, gw = pay_button(), gateway()
        ls = b03_labels()
        rt = guard(self, 0.7)
        self.play(FadeIn(pb, shift=UP * 0.2), FadeIn(gw, shift=DOWN * 0.2), FadeIn(ls), run_time=rt)
        until(self, "double click", lead=0.3)
        cur = cursor(PAY_C[0] + 0.25, PAY_C[1] - 0.55).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        slips = []
        for i in range(2):
            rt = guard(self, 0.2)
            self.play(Indicate(pb, color=None, scale_factor=0.92), run_time=rt)
            s = slip(PAY_C, 0.8)
            slips.append(s)
            rt = guard(self, 0.5)
            self.play(MoveAlongPath(s, ArcBetweenPoints(P3(PAY_C), GW_IN, angle=-PI / 5)), run_time=rt)
            drop(self, s)
        until(self, "Can you find and fix it", lead=0.4)
        ca, cb = coin(COIN_A), coin(COIN_B)
        rt = guard(self, 0.6)
        self.play(FadeOut(cur), FadeIn(ca, shift=DOWN * 0.4), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeIn(cb, shift=DOWN * 0.4), run_time=rt)
        done(self)


# ══════════════ B04: it looks, then reproduces ══════════════
def b04_labels():
    return VGroup(lbl("3 files", (2.75, -0.55), 40), lbl("test charge", (LX, -0.3), 40))


class B04_Look(Scene):
    def construct(self):
        d = state(4)
        add_state(self, d)
        old = b03_labels()
        self.add(old)
        ln = lens(cb_page_c(0) + np.array([-0.3, 0.9, 0]))
        l3 = lbl("3 files", (2.75, -0.55), 40)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(old, d["coins"])), FadeIn(ln), FadeIn(l3), run_time=rt)
        until(self, "it reads three files", lead=0.3)
        ticks = VGroup()
        for i in range(3):
            rt = guard(self, 0.45)
            self.play(ln.animate.move_to(cb_page_c(i) + np.array([0.0, 0.25, 0])), run_time=rt)
            ck = check(cb_page_c(i)[0] + 0.05, cb_page_c(i)[1] + 0.95, 0.13, INK, 6).set_z_index(9)
            ticks.add(ck)
            rt = guard(self, 0.25)
            self.play(Create(ck), run_time=rt)
        until(self, "searches the checkout flow", lead=0.2)
        rt = guard(self, 0.6)
        self.play(ln.animate.move_to(cb_page_c(3) + np.array([0.0, 0.25, 0])), run_time=rt)
        until(self, "Then it reproduces", lead=0.3)
        lp = lamp(False)
        lt = lbl("test charge", (LX, -0.3), 40)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(ln, ticks)), FadeIn(lp, shift=UP * 0.3), FadeIn(lt), run_time=rt)
        until(self, "Two clicks", lead=0.2)
        for i in range(2):
            s = slip(PAY_C, 0.8)
            rt = guard(self, 0.55)
            self.play(MoveAlongPath(s, ArcBetweenPoints(P3(PAY_C), GW_IN, angle=-PI / 5)), run_time=rt)
            drop(self, s)
        until(self, "fire two charge requests", lead=0.2)
        rt = guard(self, 0.5)
        self.play(lp[2].animate.set_fill(TERRA), Indicate(d["gw"], color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B05: the root cause ══════════════
def b05_labels():
    return VGroup(lbl("key", (SL_A[0] + KEY_DX + 0.25, SL_A[1] + 0.62), 40), lbl("per call", (SL_B[0], SL_B[1] - 0.68), 40))


class B05_Cause(Scene):
    def construct(self):
        d = state(5)
        add_state(self, d)
        old = b04_labels()
        self.add(old)
        sa, sb = slip(SL_A, 1.0), slip(SL_B, 1.0)
        rt = guard(self, 0.7)
        self.play(FadeOut(old), d["lamp"][2].animate.set_fill(GHOST), FadeIn(sa, shift=RIGHT * 0.3), FadeIn(sb, shift=RIGHT * 0.3), run_time=rt)
        until(self, "carries an idempotency key", lead=0.3)
        ka = key((SL_A[0] + KEY_DX, SL_A[1]), 1.0, 1, TILE)
        ls = b05_labels()
        rt = guard(self, 0.6)
        self.play(FadeIn(ka, shift=DOWN * 0.2), FadeIn(ls[0]), run_time=rt)
        until(self, "spot a repeat", lead=0.2)
        rt = guard(self, 0.4)
        self.play(Indicate(ka, color=None, scale_factor=1.2), run_time=rt)
        until(self, "makes a new key on every call", lead=0.3)
        kb = key((SL_B[0] + KEY_DX, SL_B[1]), 1.0, 2, GHOST)
        rt = guard(self, 0.6)
        self.play(FadeIn(kb, shift=DOWN * 0.2), FadeIn(ls[1]), run_time=rt)
        until(self, "Two clicks, two different keys", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ka, color=None, scale_factor=1.2), Indicate(kb, color=None, scale_factor=1.2), run_time=rt)
        until(self, "So the gateway sees", lead=0.3)
        ga, gb = VGroup(sa, ka), VGroup(sb, kb)
        rt = guard(self, 0.45)
        self.play(ga.animate.scale(0.6).move_to(GW_IN), run_time=rt, rate_func=ease_in)
        drop(self, ga)
        ca, cb = coin(COIN_A), coin(COIN_B)
        rt = guard(self, 0.35)
        self.play(FadeIn(ca, shift=DOWN * 0.4), run_time=rt)
        rt = guard(self, 0.45)
        self.play(gb.animate.scale(0.6).move_to(GW_IN), run_time=rt, rate_func=ease_in)
        drop(self, gb)
        rt = guard(self, 0.35)
        self.play(FadeIn(cb, shift=DOWN * 0.4), run_time=rt)
        done(self)


# ══════════════ B06: the fix ══════════════
def b06_labels():
    return VGroup(lbl("one key", (SL_A[0] + KEY_DX + 0.3, SL_A[1] + 0.62), 40),
                  lbl("charges.ts", (2.2, 0.5), 40), lbl("+9 −3", (3.95, -0.3), 40))


class B06_Fix(Scene):
    def construct(self):
        d = state(6)
        add_state(self, d)
        old = b05_labels()
        self.add(old)
        sa, sb = slip(SL_A, 1.0), slip(SL_B, 1.0)
        ka = key((SL_A[0] + KEY_DX, SL_A[1]), 1.0, 1, TILE)
        kb = key((SL_B[0] + KEY_DX, SL_B[1]), 1.0, 2, GHOST)
        ls = b06_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old, d["coins"])), FadeIn(VGroup(sa, sb, ka, kb), shift=RIGHT * 0.3), FadeIn(ls[0]), run_time=rt)
        until(self, "the second click carries the same key", lead=0.3)
        kc = ka.copy()
        rt = guard(self, 0.4)
        self.play(FadeOut(kb, shift=RIGHT * 0.3), run_time=rt)
        rt = guard(self, 0.7)
        self.play(MoveAlongPath(kc, ArcBetweenPoints(np.array(ka.get_center()), np.array(ka.get_center()) + np.array([0, SL_B[1] - SL_A[1], 0]), angle=-PI / 2)), run_time=rt)
        until(self, "the gateway charges once", lead=0.4)
        ga, gb = VGroup(sa, ka), VGroup(sb, kc)
        rt = guard(self, 0.6)
        self.play(ga.animate.scale(0.6).move_to(GW_IN), run_time=rt, rate_func=ease_in)
        drop(self, ga)
        ca = coin(COIN_FIX)
        rt = guard(self, 0.4)
        self.play(FadeIn(ca, shift=DOWN * 0.4), run_time=rt)
        home = np.array(gb.get_center())
        rt = guard(self, 0.5)
        self.play(gb.animate.move_to(GW_IN + np.array([-0.35, -0.05, 0])), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.5)
        self.play(gb.animate.move_to(home + np.array([-0.4, 0, 0])), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeOut(gb), run_time=rt)
        until(self, "disables the button", lead=0.3)
        grey = pay_button(grey=True)
        rt = guard(self, 0.6)
        self.play(FadeOut(d["pay"]), FadeIn(grey), run_time=rt)
        until(self, "One file changed", lead=0.3)
        df = diff_card()
        rt = guard(self, 0.7)
        self.play(FadeIn(df, shift=UP * 0.5), FadeIn(ls[1]), run_time=rt)
        until(self, "nine lines added", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[2]), run_time=rt)
        done(self)


# ══════════════ B07: agentic search maps a new codebase ══════════════
def b07_labels():
    return VGroup(lbl("agentic search", (2.3, 2.85), 40), lbl("map", (5.2, 0.75), 40))


class B07_Map(Scene):
    def construct(self):
        d = state(7)
        add_state(self, d)
        old = b06_labels()
        self.add(old)
        bt, pages = big_tray()
        rt = guard(self, 0.9)
        self.play(FadeOut(VGroup(old, d["pay"], d["gw"], d["coins"], d["diff"])), run_time=rt)
        rt = guard(self, 0.8)
        self.play(FadeIn(bt, shift=DOWN * 0.4), run_time=rt)
        until(self, "Ask it to explain the project", lead=0.3)
        ln = lens(mb_c(0) + np.array([-0.2, 0.7, 0]))
        ls = b07_labels()
        rt = guard(self, 0.4)
        self.play(FadeIn(ln), FadeIn(ls[1]), run_time=rt)
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(map_node(0)), run_time=rt)
        seen = {0}
        for a, b in MAP_EDGES:
            anims = [ln.animate.move_to(mb_c(b) + np.array([0.0, 0.2, 0])), Create(map_edge(a, b))]
            if b not in seen:
                anims.append(GrowFromCenter(map_node(b)))
            rt = guard(self, 0.4)
            self.play(*anims, run_time=rt)
            seen.add(b)
        until(self, "The page calls this agentic search", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[0]), FadeOut(ln), run_time=rt)
        until(self, "so you don't hand pick", lead=0.3)
        ghost = DashedVMobject(ArcBetweenPoints(P3((YX + 0.5, YY + 1.5)), mb_c(0) + np.array([-0.4, 0.1, 0]), angle=-PI / 4)
                               .set_stroke(BAR2, 6), num_dashes=24).set_z_index(2)
        rt = guard(self, 0.6)
        self.play(Create(ghost), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeOut(ghost), run_time=rt)
        done(self)


# ══════════════ B08: issue to pull request ══════════════
def b08_labels():
    return VGroup(lbl("issue", (TK[0], TK[1] + 0.85), 40), lbl("tests", (LX, -0.3), 40), lbl("pull request", (PR_C[0], PR_C[1] + 0.85), 40))


class B08_IssueToPR(Scene):
    def construct(self):
        d = state(8)
        add_state(self, d)
        old = b07_labels()
        self.add(old)
        ls = b08_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old, d["big"], d["map"])), run_time=rt)
        until(self, "So one task can run", lead=0.3)
        dot = Dot(P3(TK) + np.array([0.9, 0.0, 0]), radius=0.1, color=TERRA).set_z_index(10)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[0]), GrowFromCenter(dot), run_time=rt)
        until(self, "write the code", lead=0.3)
        pg = cb_page_c(1) + np.array([0, 0.25, 0])
        rt = guard(self, 0.6)
        self.play(MoveAlongPath(dot, ArcBetweenPoints(np.array(dot.get_center()), pg, angle=-PI / 4)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Indicate(d["tray"][1][1], color=None, scale_factor=1.15), run_time=rt)
        until(self, "run the tests", lead=0.3)
        rt = guard(self, 0.5)
        self.play(MoveAlongPath(dot, ArcBetweenPoints(pg, P3((LX, LY)), angle=PI / 4)), FadeIn(ls[1]), run_time=rt)
        rt = guard(self, 0.3)
        self.play(d["lamp"][2].animate.set_fill(TERRA), run_time=rt)
        until(self, "open a pull request", lead=0.3)
        pr = pr_card()
        rt = guard(self, 0.7)
        self.play(FadeOut(dot), FadeIn(pr, shift=UP * 0.4), FadeIn(ls[2]), run_time=rt)
        done(self)


# ══════════════ B09: long runs keep going ══════════════
def b09_labels():
    return VGroup(lbl("imports", (2.75, -0.55), 40), lbl("tests", (LX, -0.3), 40))


class B09_LongRun(Scene):
    def construct(self):
        d = state(9)
        add_state(self, d)
        old = b08_labels()
        self.add(old)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(old[0], old[2], d["pr"])), d["lamp"][2].animate.set_fill(GHOST), run_time=rt)
        until(self, "It follows imports", lead=0.3)
        li = b09_labels()[0]
        dot = Dot(cb_page_c(0) + np.array([0, 0.3, 0]), radius=0.1, color=TERRA).set_z_index(10)
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(dot), FadeIn(li), run_time=rt)
        for i in range(1, 4):   # the import chain: page to page, nothing left drawn on the pages
            a, b = np.array(dot.get_center()), cb_page_c(i) + np.array([0, 0.3, 0])
            rt = guard(self, 0.4)
            self.play(MoveAlongPath(dot, ArcBetweenPoints(a, b, angle=-PI / 2)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeOut(dot), run_time=rt)
        until(self, "runs your tests", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Indicate(d["lamp"][2], color=None, scale_factor=1.2), run_time=rt)
        until(self, "when something breaks", lead=0.2)
        xm = xmark(MARK_C)
        rt = guard(self, 0.4)
        self.play(Create(xm), run_time=rt)
        until(self, "It fixes the failure", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(d["tray"][1][2], color=None, scale_factor=1.2), run_time=rt)
        until(self, "runs them again", lead=0.3)
        ck = check(MARK_C[0], MARK_C[1], 0.2).set_z_index(8)
        rt = guard(self, 0.4)
        self.play(FadeOut(xm), d["lamp"][2].animate.set_fill(TERRA), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(ck), run_time=rt)
        done(self)


# ══════════════ B10: one agent, many doors ══════════════
def b10_labels():
    return VGroup(lbl("terminal", (DOOR_X[0], DOOR_Y + 0.8), 40), lbl("editor", (DOOR_X[1], DOOR_Y + 0.8), 40),
                  lbl("Slack", (DOOR_X[5], DOOR_Y + 0.8), 40))


class B10_Doors(Scene):
    def construct(self):
        d = state(10)
        add_state(self, d)
        old = b09_labels()
        self.add(old)
        ls = b10_labels()
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(old, d["mark"], d["ticket"])), run_time=rt)
        groups = [("The docs list the terminal", (0,)), ("your editor", (1,)), ("the desktop app", (2,)), ("and the web", (3,)),
                  ("the same Claude Code engine", ()), ("The page adds the phone app", (4,)), ("And in Slack", (5,))]
        for ph, idx in groups:
            if not idx:
                until(self, ph, lead=0.3)
                rt = guard(self, 0.5)
                self.play(Indicate(d["agent"][2], color=None, scale_factor=1.8), run_time=rt)
                continue
            until(self, ph, lead=0.2)
            anims = []
            for i in idx:
                anims += [Create(cable(i)), FadeIn(door(i), shift=DOWN * 0.2)]
                if i in (0, 1):
                    anims.append(FadeIn(ls[i]))
                if i == 5:
                    anims.append(FadeIn(ls[2]))
            rt = guard(self, 0.5)
            self.play(*anims, run_time=rt)
        done(self)


# ══════════════ B11: your part — decide, answer, review ══════════════
def b11_labels():
    return VGroup(you_label(), lbl("review", (TK_YOU[0], TK_YOU[1] + 0.85), 40),
                  lbl("per Notion's co-founder", (-1.4, 2.55), 38))


class B11_Review(Scene):
    def construct(self):
        d = state(11)
        add_state(self, d)
        old = b10_labels()
        self.add(old)
        ls = b11_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old, d["doors"], d["cables"])), FadeIn(ls[0]), run_time=rt)
        until(self, "You decide what needs doing", lead=0.3)
        tk = ticket(TK_YOU)
        rt = guard(self, 0.4)
        self.play(FadeIn(tk, shift=UP * 0.2), run_time=rt)
        rt = guard(self, 0.8)
        self.play(MoveAlongPath(tk, ArcBetweenPoints(P3(TK_YOU), P3(TK), angle=-PI / 4)), run_time=rt)
        until(self, "you answer its questions", lead=0.3)
        q = T("?", 60).move_to(P3((-3.15, -0.45))).set_z_index(9)
        rt = guard(self, 0.3)
        self.play(FadeIn(q), run_time=rt)
        rt = guard(self, 0.6)
        self.play(q.animate.move_to(P3((YX + 0.9, YY + 1.55))), run_time=rt)
        until(self, "you review the change", lead=0.3)
        df = diff_card(AG_SPARK + np.array([0.0, 0.2, 0]))
        rt = guard(self, 0.3)
        self.play(FadeOut(q), FadeIn(df), run_time=rt)
        rt = guard(self, 0.8)
        self.play(MoveAlongPath(df, ArcBetweenPoints(np.array(df.get_center()), P3(TK_YOU), angle=PI / 4)), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[1]), run_time=rt)
        until(self, "before you keep it", lead=0.2)
        ck = check(TK_YOU[0] + 1.15, TK_YOU[1], 0.2).set_z_index(8)
        rt = guard(self, 0.4)
        self.play(Create(ck), run_time=rt)
        until(self, "Notion's co-founder", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[2]), run_time=rt)
        until(self, "Claude Code builds it", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(d["agent"][2], color=None, scale_factor=1.8), run_time=rt)
        done(self)


# ══════════════ B12: manual mode asks you; auto mode checks for you ══════════════
def b12_labels():
    return VGroup(lbl("auto mode", (0.25, CMD_Y + 0.75), 40), lbl("risky", (BAR_X - 1.1, CMD_Y - 0.6), 40),
                  lbl("manual", (0.25, CMD_Y + 0.75), 40))


def stop_x():
    return BAR_X - 0.62


class B12_Auto(Scene):
    def construct(self):
        d = state(12)
        add_state(self, d)
        old = b11_labels()
        self.add(old)
        g, cur = term(TERM12_C)
        arm, sleeve = barrier(up=False)
        ls = b12_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old[1], old[2], d["diff"], d["rmark"])), FadeIn(VGroup(g, cur), shift=LEFT * 0.3),
                  FadeIn(VGroup(arm, sleeve), shift=UP * 0.2), run_time=rt)
        x0 = -0.35
        until(self, "The docs describe manual mode", lead=0.3)
        c1 = cmd(x0)
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[2]), FadeIn(c1, scale=0.6), run_time=rt)
        rt = guard(self, 0.4)
        self.play(arm.animate.move_to(P3((BAR_X, ARM_UP))), run_time=rt)
        rt = guard(self, 0.6)
        self.play(c1.animate.move_to(P3((stop_x(), CMD_Y))), run_time=rt)
        until(self, "stops and asks you", lead=0.2)
        q = T("?", 60).move_to(P3((stop_x() - 0.7, CMD_Y - 0.55))).set_z_index(9)
        rt = guard(self, 0.25)
        self.play(FadeIn(q), run_time=rt)
        rt = guard(self, 0.7)
        self.play(q.animate.move_to(P3((YX + 0.9, YY + 1.55))), run_time=rt)
        until(self, "or runs commands", lead=0.2)
        ok = check(YX + 0.9, YY + 1.5, 0.2).set_z_index(9)
        rt = guard(self, 0.4)
        self.play(FadeOut(q), Create(ok), run_time=rt)
        rt = guard(self, 0.4)
        self.play(arm.animate.move_to(P3((BAR_X, ARM_DOWN))), run_time=rt)
        rt = guard(self, 0.5)
        self.play(c1.animate.move_to(P3((TERM12_C[0] - 1.1, CMD_Y))), run_time=rt)
        rt = guard(self, 0.25)
        self.play(FadeOut(c1), FadeOut(ok), run_time=rt)
        until(self, "And auto mode", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeOut(ls[2]), FadeIn(ls[0]), run_time=rt)
        for n in range(2):
            c = cmd(x0)
            rt = guard(self, 0.25)
            self.play(FadeIn(c, scale=0.6), run_time=rt)
            rt = guard(self, 0.6)
            self.play(c.animate.move_to(P3((TERM12_C[0] - 1.1, CMD_Y))), run_time=rt)
            rt = guard(self, 0.2)
            self.play(FadeOut(c), run_time=rt)
        until(self, "while still catching risky commands", lead=0.4)
        rc = cmd(x0, True)
        rt = guard(self, 0.25)
        self.play(FadeIn(rc, scale=0.6), run_time=rt)
        rt = guard(self, 0.4)
        self.play(arm.animate.move_to(P3((BAR_X, ARM_UP))), run_time=rt)
        rt = guard(self, 0.5)
        self.play(rc.animate.move_to(P3((stop_x(), CMD_Y))), FadeIn(ls[1]), run_time=rt)
        done(self)


# ══════════════ B13: how to start ══════════════
def b13_labels():
    return VGroup(lbl("Pro", (TAG_PRO[0] - 1.25, TAG_PRO[1]), 40), lbl("Max", (TAG_MAX[0] - 1.25, TAG_MAX[1]), 40),
                  lbl("install", (1.9, 2.55), 40))


class B13_Start(Scene):
    def construct(self):
        d = state(13)
        add_state(self, d)
        old = VGroup(you_label(), b12_labels()[:2])
        self.add(old)
        ls = b13_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old, d["term"], d["barrier"], d["risky"], d["lamp"])), run_time=rt)
        until(self, "Claude Code is included", lead=0.3)
        tp, tm = tag(TAG_PRO), tag(TAG_MAX)
        rt = guard(self, 0.5)
        self.play(FadeIn(tp, shift=DOWN * 0.4), FadeIn(ls[0]), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeIn(tm, shift=DOWN * 0.4), FadeIn(ls[1]), run_time=rt)
        until(self, "Team and Enterprise", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(tp, tm), color=None, scale_factor=1.08), run_time=rt)
        until(self, "one line in the terminal", lead=0.4)
        g, cur = term((1.9, 1.55), 2.2, 1.0)
        rt = guard(self, 0.5)
        self.play(FadeIn(g, shift=UP * 0.2), FadeIn(cur), FadeIn(ls[2]), run_time=rt)
        line = gbar(1.4, 2.75, 1.55, BAR3, 9).set_z_index(5)
        rt = guard(self, 0.8)
        self.play(Create(line), cur.animate.shift(RIGHT * 1.45), run_time=rt)
        until(self, "Then type claude", lead=0.3)
        link = Line(P3((-0.2, -1.3)), cb_page_c(0) + np.array([-0.55, 0.1, 0]), color=CONN, stroke_width=7).set_z_index(3)
        rt = guard(self, 0.6)
        self.play(Create(link), run_time=rt)
        rt = guard(self, 0.5)
        self.play(Indicate(d["agent"][2], color=None, scale_factor=1.8), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Handoff, B01_Hands, B02_Plan, B03_Bug, B04_Look, B05_Cause, B06_Fix, B07_Map, B08_IssueToPR,
             B09_LongRun, B10_Doors, B11_Review, B12_Auto, B13_Start):
    _cls.play = ST.play
