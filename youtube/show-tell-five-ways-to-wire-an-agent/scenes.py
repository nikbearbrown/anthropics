"""
Manim scenes for show-tell-five-ways-to-wire-an-agent (show-tell skill).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

One conveyor cast for the whole film (source: Anthropic, "Building effective agents"):
crate = the work, dark station = one LLM call, belt = a path written in code, gate = a
programmatic check. B06 takes the rails away (an agent); B07 is the advice (start simple).
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
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ the film: one conveyor cast ═════════════════════════════
# Cast, whole film: a kraft CRATE with terracotta tape (the work), dark STATIONS (one LLM call each,
# a light that turns terracotta when the call runs), pale BELTS (paths written in code), ink GATES.
BELT = "#E6DFD3"
PLATE = "#CDB894"


def _unit(v):
    v = np.array(v, dtype=float)
    return v / np.linalg.norm(v)


def strip(iso, a, b, w=1.1):
    """A flat belt from iso point a=(x,y) to b=(x,y), any direction, with a dashed centre line."""
    a = np.array(a, dtype=float); b = np.array(b, dtype=float)
    d = _unit(b - a); n = np.array([-d[1], d[0]]) * w / 2
    q = iso.quad([(*(a - n), 0), (*(b - n), 0), (*(b + n), 0), (*(a + n), 0)], BELT, stroke=DIM, sw=2)
    m = DashedLine(iso.p(*(a + d * 0.25), 0), iso.p(*(b - d * 0.25), 0), color=DIM, stroke_width=2, dash_length=0.12)
    return VGroup(q, m)


def station(iso, cx, cy, w=1.3, d=None, h=1.1):
    """A dark LLM station centred on (cx, cy); [1] is its light (ghost until the call runs)."""
    d = d or w
    body = iso.box(cx - w / 2, cy - d / 2, 0, w, d, h, DARK_TOP, DARK_L, DARK_R)
    light = Dot(iso.p(cx + w * 0.22, cy - d / 2, h * 0.62), radius=max(0.06, 0.11 * iso.s), color=GHOST)
    return VGroup(body, light)


def crate(iso, cx, cy, s=0.9, z=0.02):
    x0, y0, h = cx - s / 2, cy - s / 2, s * 0.8
    return VGroup(iso.box(x0, y0, z, s, s, h), iso.tape(x0, y0, z + h, s, s, drop=h * 0.25, t=s * 0.12))


def mark(iso, cx, cy, s, k, z=0.02):
    """k-th ink tick on a crate's right front face: the output of one more call."""
    h = s * 0.8
    return Dot(iso.p(cx - s / 2 + s * (0.22 + 0.24 * k), cy - s / 2, z + h * 0.45), radius=max(0.05, 0.075 * iso.s * 1.2), color=INK)


def title(n, name):
    num = T(n, 46, INK, bold=True).move_to([-5.75, 2.8, 0])
    nm = T(name, 42).next_to(num, RIGHT, buff=0.3)
    nm.align_to(num, DOWN)
    return VGroup(num, nm)


def cross(x, y, s=0.22, color=INK, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def gate(iso, x, y0, y1, h=1.8, sw=9):
    """An ink arch across a belt at x: (back post + beam, front post)."""
    back = VGroup(Line(iso.p(x, y1, 0), iso.p(x, y1, h), color=INK, stroke_width=sw),
                  Line(iso.p(x, y1, h), iso.p(x, y0, h), color=INK, stroke_width=sw))
    front = Line(iso.p(x, y0, 0), iso.p(x, y0, h), color=INK, stroke_width=sw)
    return back, front


def slide(mob, iso, dx, dy=0.0):
    return mob.animate.shift(iso.v(dx, dy, 0))


# ─────────────── B00 · the augmented LLM: one station with a kit ───────────────
class B00_Station(Scene):
    def construct(self):
        M = Iso(-3.0, -0.3, 1.0)
        belt = strip(M, (-3.3, -1.75), (1.4, -1.75), 1.2)
        st = station(M, 0, 0, 1.9, 1.9, 1.6)
        self.play(FadeIn(belt), FadeIn(st), run_time=0.6)
        until(self, "a model with a kit")
        anchor = M.p(0.85, -0.95, 1.25)
        dots = VGroup(*[Dot([1.35, y, 0], radius=0.07, color=GHOST) for y in (2.1, 0.45, -1.35)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.3), run_time=0.6)
        LX = 3.55
        # retrieval — a magnifier
        until(self, "Retrieval")
        mag = VGroup(Circle(radius=0.42, stroke_color=INK, stroke_width=10, fill_color=CARD, fill_opacity=1),
                     Line([0.3, -0.3, 0], [0.72, -0.72, 0], color=INK, stroke_width=16)).move_to([2.3, 2.05, 0])
        mag.shift(UP * 3); self.add(mag)
        self.play(mag.animate.shift(DOWN * 3), run_time=0.6, rate_func=ease_in)
        c1 = Line(anchor, [1.35, 2.1, 0], color=INK, stroke_width=4)
        self.play(Create(c1), dots[0].animate.set_color(TERRA),
                  FadeIn(T("retrieval", 38).move_to([LX, 2.1, 0], aligned_edge=LEFT)), run_time=0.5)
        # tools — the dark connector block
        until(self, "tools to act")
        blk = Iso(1.85, 0.05, 0.75).mcp(0, 0, 0)
        blk.shift(UP * 4); self.add(blk)
        self.play(blk.animate.shift(DOWN * 4), run_time=0.6, rate_func=ease_in)
        c2 = Line(anchor, [1.35, 0.45, 0], color=INK, stroke_width=4)
        self.play(Create(c2), dots[1].animate.set_color(TERRA),
                  FadeIn(T("tools", 38).move_to([LX, 0.45, 0], aligned_edge=LEFT)), run_time=0.5)
        # memory — a stack of pages
        until(self, "and memory")
        PI_ = Iso(1.85, -2.05, 0.75)
        pages = VGroup(*[PI_.page(0, 0, z, 1.1, 1.3) for z in (0.0, 0.14, 0.28)])
        pages.shift(UP * 4); self.add(pages)
        self.play(pages.animate.shift(DOWN * 4), run_time=0.6, rate_func=ease_in)
        c3 = Line(anchor, [1.35, -1.35, 0], color=INK, stroke_width=4)
        self.play(Create(c3), dots[2].animate.set_color(TERRA),
                  FadeIn(T("memory", 38).move_to([LX, -1.35, 0], aligned_edge=LEFT)), run_time=0.5)
        # the call runs: a crate rides in, the light comes on
        until(self, "Every pattern after this")
        cr = crate(M, -2.7, -1.75, 0.95); cr.set_z_index(2)
        self.add(cr)
        self.play(slide(cr, M, 2.7), run_time=1.0)
        self.play(st[1].animate.set_color(TERRA), Indicate(VGroup(mag, blk, pages), color=None, scale_factor=1.05), run_time=0.8)
        cr.add(mark(M, 0, -1.75, 0.95, 0))
        self.play(Indicate(cr[-1], scale_factor=1.6, color=INK), run_time=0.5)
        finish(self)


# ─────────────── B01 · prompt chaining: stations in a row, a gate between ───────────────
class B01_Chain(Scene):
    def construct(self):
        C = Iso(-4.5, -2.75, 0.66)
        head = title("1", "prompt chaining")
        belt = strip(C, (0, 0), (13.4, 0), 1.3)
        xs = [2.0, 8.4, 11.9]
        sts = [station(C, x, 2.2, 1.4, 1.4, 1.1) for x in xs]
        self.play(FadeIn(head), FadeIn(belt), *[FadeIn(s) for s in sts], run_time=0.7)
        gb, gf = gate(C, 4.6, -0.75, 0.75, 1.7)
        gb.set_z_index(0); gf.set_z_index(3)
        self.play(Create(gb), Create(gf), run_time=0.6)
        glab = T("gate", 38).move_to(C.p(4.6, -0.75, 0) + np.array([0.95, -0.5, 0]))
        self.play(FadeIn(glab), run_time=0.4)
        cr = crate(C, 0.4, 0, 1.0); cr.set_z_index(2)
        self.add(cr)
        pos = [0.4]

        def go(x, rt=0.8):
            self.play(slide(cr, C, x - pos[0]), run_time=rt)
            pos[0] = x

        def call(i):
            self.play(sts[i][1].animate.set_color(TERRA), run_time=0.25)
            m = mark(C, pos[0], 0, 1.0, i); cr.add(m)
            self.play(GrowFromCenter(m), sts[i][1].animate.set_color(GHOST), run_time=0.25)

        until(self, "Split the job")
        self.play(*[Indicate(s, color=None, scale_factor=1.06) for s in sts], run_time=0.7)
        until(self, "Each call works")
        go(xs[0]); call(0)
        until(self, "and a gate between")
        go(4.6 - 0.9, 0.6)
        ck = check(C.p(4.6, 0, 1.7)[0] - 0.15, C.p(4.6, 0, 1.7)[1] + 0.5, 0.22, TERRA, 8)
        self.play(Create(ck), gb.animate.set_color(TERRA), gf.animate.set_color(TERRA), run_time=0.5)
        go(xs[1], 0.6); call(1)
        until(self, "Outline, check")
        go(xs[2], 0.5); call(2)
        finish(self)


# ─────────────── B02 · routing: a track switch ───────────────
class B02_Route(Scene):
    def construct(self):
        R = Iso(-3.6, -2.75, 0.58)
        head = title("2", "routing")
        SW = (4.6, 0.0)
        lanes = [2.6, 0.0, -2.6]          # back (upper left) · middle · front (lower right)
        inbelt = strip(R, (-0.6, 0), (4.0, 0), 1.2)
        forks = VGroup(*[strip(R, (5.2, 0), (7.2, y), 1.1) for y in lanes])
        outs = VGroup(*[strip(R, (7.2, y), (9.8, y), 1.1) for y in lanes])
        sts = [station(R, 11.0, lanes[0], 1.4, 1.4, 1.2), station(R, 11.0, lanes[1], 1.4, 1.4, 1.2),
               station(R, 10.7, lanes[2], 0.8, 0.8, 0.6)]
        plate = R.quad([(SW[0] - 0.8, -0.8, 0), (SW[0] + 0.8, -0.8, 0), (SW[0] + 0.8, 0.8, 0), (SW[0] - 0.8, 0.8, 0)], PLATE, sw=3)
        self.play(FadeIn(head), FadeIn(inbelt), FadeIn(forks), FadeIn(outs), FadeIn(plate), *[FadeIn(s) for s in sts], run_time=0.8)
        hub = R.p(SW[0], SW[1], 0.05)

        def aim(y):
            v = R.p(7.2, y, 0) - hub
            return np.arctan2(v[1], v[0])

        lever = Line(hub, hub + 0.95 * np.array([np.cos(aim(0)), np.sin(aim(0)), 0]), color=INK, stroke_width=12)
        knob = Dot(hub, radius=0.13, color=INK)
        self.play(Create(lever), GrowFromCenter(knob), run_time=0.5)
        l1 = T("refunds", 38).move_to([-2.0, 1.95, 0])
        l2 = T("tech support", 38).move_to([4.0, 0.8, 0])
        state = {"a": aim(0)}

        def route(cr, y, s, rt=0.55):
            a = aim(y)
            self.play(Rotate(lever, a - state["a"], about_point=hub), run_time=0.25)
            state["a"] = a
            self.play(slide(cr, R, SW[0] + 0.2), run_time=rt)
            self.play(slide(cr, R, 7.2 - SW[0], y), run_time=rt)
            self.play(slide(cr, R, 9.8 - 7.2 - s / 2 - 0.1), run_time=rt)

        until(self, "Classify what comes in")
        c1 = crate(R, -0.2, 0, 1.0); c1.set_z_index(3); self.add(c1)
        self.play(Indicate(knob, color=TERRA, scale_factor=1.8), run_time=0.6)
        until(self, "send it down the line")
        route(c1, lanes[0], 1.0)
        until(self, "Refunds go one way")
        self.play(sts[0][1].animate.set_color(TERRA), FadeIn(l1), run_time=0.4)
        c2 = VGroup(R.box(-0.7, -0.5, 0.02, 1.0, 1.0, 0.8, DARK_TOP, DARK_L, DARK_R)); c2.set_z_index(3); self.add(c2)
        until(self, "tech support another")
        route(c2, lanes[1], 1.0, 0.4)
        self.play(sts[1][1].animate.set_color(TERRA), FadeIn(l2), run_time=0.4)
        until(self, "And easy questions")
        c3 = crate(R, -0.2, 0, 0.6); c3.set_z_index(3); self.add(c3)
        route(c3, lanes[2], 0.6, 0.35)
        self.play(sts[2][1].animate.set_color(TERRA), Indicate(sts[2], color=None, scale_factor=1.15), run_time=0.5)
        finish(self)


# ─────────────── B03 · parallelization: split belts that merge (sectioning, voting) ───────────────
class B03_Parallel(Scene):
    def construct(self):
        P = Iso(-3.4, -2.6, 0.6)
        head = title("3", "parallelization")
        lanes = [3.0, 0.0, -3.0]
        belts = VGroup(strip(P, (-0.5, 0), (3.0, 0), 1.1),
                       *[strip(P, (3.0, 0), (4.8, y), 1.0) for y in lanes],
                       *[strip(P, (4.8, y), (9.4, y), 1.0) for y in lanes],
                       *[strip(P, (9.4, y), (11.2, 0), 1.0) for y in lanes],
                       strip(P, (11.2, 0), (13.6, 0), 1.1))
        sts = [station(P, 7.1, y + 1.45, 1.0, 0.9, 0.9) for y in lanes]
        self.play(FadeIn(head), FadeIn(belts), *[FadeIn(s) for s in sts], run_time=0.8)
        lab_s = T("sectioning", 38)
        lab_v = T("voting", 38).next_to(lab_s, RIGHT, buff=0.8)
        VGroup(lab_s, lab_v).move_to([3.6, -2.55, 0])
        pip = Dot(lab_s.get_bottom() + DOWN * 0.25, radius=0.1, color=TERRA)

        def run(parts, rt=0.55):
            self.play(*[slide(p, P, 4.8 - 3.0, y) for p, y in zip(parts, lanes)], run_time=rt)
            self.play(*[slide(p, P, 7.1 - 4.8) for p in parts], run_time=rt)
            self.play(*[s[1].animate.set_color(TERRA) for s in sts], run_time=0.3)
            self.play(*[slide(p, P, 9.4 - 7.1) for p in parts], *[s[1].animate.set_color(GHOST) for s in sts], run_time=rt)

        until(self, "Split the belt")
        c = crate(P, 0.6, 0, 1.0); c.set_z_index(3); self.add(c)
        self.play(slide(c, P, 2.4), run_time=0.6)
        until(self, "Sectioning runs")
        self.play(FadeIn(lab_s), FadeIn(lab_v), GrowFromCenter(pip), run_time=0.4)
        # sectioning: the crate breaks into three DIFFERENT parts
        parts = [P.mcp(2.6, -0.4, 0.02, 0.8, 0.8, 0.5), P.page(2.6, -0.45, 0.05, 0.8, 0.9), crate(P, 3.0, 0, 0.7)]
        for p in parts:
            p.set_z_index(3)
        self.remove(c); self.add(*parts)
        run(parts, 0.45)
        self.play(*[slide(p, P, 11.2 - 9.4, -y) for p, y in zip(parts, lanes)], run_time=0.4)
        whole = crate(P, 11.3, 0, 1.0); whole.set_z_index(4)
        self.remove(*parts); self.add(whole)
        self.play(slide(whole, P, 1.8), run_time=0.35)
        # voting: the SAME task, three times, then compare
        until(self, "Voting runs")
        self.play(pip.animate.move_to(lab_v.get_bottom() + DOWN * 0.25), whole.animate.shift(RIGHT * 4), run_time=0.3)
        self.remove(whole)
        votes = [crate(P, 3.0, 0, 0.75) for _ in lanes]
        for v in votes:
            v.set_z_index(3)
        self.add(*votes)
        run(votes, 0.4)
        tops = [P.p(9.4, y, 1.25) + UP * 0.25 for y in lanes]
        marks = [check(tops[0][0], tops[0][1], 0.18, INK, 7), check(tops[1][0], tops[1][1], 0.18, INK, 7),
                 cross(tops[2][0], tops[2][1], 0.16, INK, 7)]
        self.play(*[Create(m) for m in marks], run_time=0.4)
        until(self, "compares the answers")
        self.play(slide(votes[0], P, 11.2 - 9.4, -3.0), slide(marks[0], P, 11.2 - 9.4, -3.0),
                  slide(votes[1], P, 11.2 - 9.4, 0), slide(marks[1], P, 11.2 - 9.4, 0), run_time=0.4)
        agreed = crate(P, 11.3, 0, 1.0); agreed.set_z_index(4)
        self.remove(votes[0], votes[1], marks[0], marks[1]); self.add(agreed)
        top = P.p(11.3, 0, 1.3)
        self.play(Create(check(top[0], top[1] + 0.3, 0.2, TERRA, 7)), run_time=0.3)
        finish(self)


# ─────────────── B04 · orchestrator-workers: a foreman hands out crates ───────────────
class B04_Foreman(Scene):
    def construct(self):
        F = Iso(-3.3, -0.9, 0.9)
        head = title("4", "orchestrator-workers")
        belt = strip(F, (-3.6, -1.8), (2.6, -1.8), 1.2)
        boss = station(F, 0, 0.2, 2.0, 2.0, 2.4)
        self.play(FadeIn(head), FadeIn(belt), FadeIn(boss), run_time=0.7)
        cr = crate(F, -3.0, -1.8, 1.0); cr.set_z_index(3); self.add(cr)
        until(self, "A central model reads")
        self.play(slide(cr, F, 3.0), run_time=0.8)
        self.play(boss[1].animate.set_color(TERRA), run_time=0.3)
        spots = [(0.9, 2.35), (2.8, 2.0), (4.3, 0.9), (4.8, -0.65), (4.2, -2.15)]
        hub = F.p(1.0, 0.2, 1.8)

        def worker(x, y):
            return station(Iso(x, y - 0.25, 0.55), 0, 0, 1.1, 1.1, 0.9)

        ws = [worker(*s) for s in spots]
        paths = [DashedLine(hub, np.array([x - 0.55, y + 0.25, 0]), color=INK, stroke_width=4, dash_length=0.14) for x, y in spots]
        until(self, "decides the subtasks")
        self.play(*[GrowFromCenter(w) for w in ws[:4]], run_time=0.5)
        self.play(*[Create(p) for p in paths[:4]], run_time=0.5)
        wl = T("workers", 38).move_to([5.1, 2.35, 0])
        self.play(FadeIn(wl), run_time=0.3)
        until(self, "hands them to worker")
        self.remove(cr)
        small = [crate(Iso(*hub[:2], 0.5), 0, 0, 0.8) for _ in range(4)]
        for s in small:
            s.set_z_index(4)
        self.add(*small)
        targets = [np.array([x + 0.1, y + 0.35, 0]) for x, y in spots[:4]]
        self.play(*[s.animate.move_to(t) for s, t in zip(small, targets)], run_time=0.8)
        self.play(*[w[1].animate.set_color(TERRA) for w in ws[:4]], run_time=0.3)
        until(self, "pulls their results together")
        self.play(*[s.animate.move_to(hub + np.array([-0.2, 0.3, 0])) for s in small], run_time=0.8)
        done = crate(F, 0.4, -1.8, 1.0); done.set_z_index(5)
        self.remove(*small)
        self.add(done)
        self.play(slide(done, F, 1.0), run_time=0.5)
        until(self, "Unlike parallelization")
        self.play(GrowFromCenter(ws[4]), Create(paths[4]), run_time=0.6)
        self.play(ws[4][1].animate.set_color(TERRA), run_time=0.3)
        finish(self)


# ─────────────── B05 · evaluator-optimizer: an inspector sends it back ───────────────
class B05_Inspector(Scene):
    def construct(self):
        E = Iso(-1.3, -2.45, 0.58)
        head = title("5", "evaluator-optimizer")
        fwd = strip(E, (0.3, 0), (7.3, 0), 1.1)
        back = strip(E, (7.3, 2.4), (0.3, 2.4), 1.1)
        endR = strip(E, (7.3, -0.55), (7.3, 2.95), 1.1)
        endL = strip(E, (0.3, -0.55), (0.3, 2.95), 1.1)
        maker = station(E, -1.1, 1.2, 1.6, 3.2, 1.4)
        booth = VGroup(E.box(7.8, -0.4, 0, 1.6, 3.2, 1.6),
                       E.quad([(7.8, 0.4, 0.7), (7.8, 2.2, 0.7), (7.8, 2.2, 1.25), (7.8, 0.4, 1.25)], DARK_L, sw=3))
        self.play(FadeIn(head), FadeIn(VGroup(endL, endR, back, fwd)), FadeIn(maker), FadeIn(booth), run_time=0.8)
        fb = T("feedback", 38).move_to([-1.5, 0.35, 0])
        cr = crate(E, 0.9, 0, 1.0); cr.set_z_index(3); self.add(cr)
        lamp = Dot(E.p(8.6, 1.2, 1.6), radius=0.12, color=GHOST); lamp.set_z_index(4)
        self.add(lamp)
        until(self, "One call makes the work")
        self.play(maker[1].animate.set_color(TERRA), run_time=0.3)
        n = [0]

        def forward(rt=0.8):
            self.play(slide(cr, E, 6.6 - 0.9), run_time=rt)

        def reject(rt=0.8):
            x, y = cr.get_top()[0], cr.get_top()[1] + 0.45
            X = cross(x, y, 0.2, INK, 8)
            self.play(Create(X), lamp.animate.set_color(INK), run_time=0.3)
            self.remove(X)
            self.play(slide(cr, E, 7.3 - 6.6, 2.4), lamp.animate.set_color(GHOST), run_time=0.3)
            self.play(slide(cr, E, 0.3 - 7.3), run_time=rt)
            self.play(slide(cr, E, 0.9 - 0.3, -2.4), run_time=0.25)
            m = mark(E, 0.9, 0, 1.0, n[0]); cr.add(m); n[0] += 1
            self.play(GrowFromCenter(m), Indicate(maker[1], color=TERRA), run_time=0.3)

        until(self, "Another judges it")
        forward()
        until(self, "sends it back")
        self.play(FadeIn(fb), run_time=0.3)
        reject(0.6)
        forward(0.5)
        until(self, "until it passes")
        x, y = cr.get_top()[0], cr.get_top()[1] + 0.5
        self.play(Create(check(x, y, 0.22, TERRA, 8)), lamp.animate.set_color(TERRA), run_time=0.4)
        finish(self)


# ─────────────── B06 · agents: the rails come off ───────────────
class B06_Agent(Scene):
    def construct(self):
        A = Iso(-3.6, -1.2, 0.72)
        rails = VGroup(strip(A, (-1.0, 0), (7.0, 0), 1.2), strip(A, (7.0, 0), (7.0, 4.0), 1.2))
        cr = crate(A, 0.2, 0, 1.0); cr.set_z_index(5)
        self.add(rails, cr)
        self.play(Indicate(rails, color=None, scale_factor=1.02), run_time=0.4)
        until(self, "take the rails away", lead=0.1)
        self.play(rails.animate.shift(DOWN * 7), run_time=0.9, rate_func=ease_in)
        self.remove(rails)
        head = T("agent", 44, bold=True).move_to([-5.3, 2.8, 0])
        spots = [(-0.6, 1.2), (3.7, 1.2), (1.6, -1.3), (4.9, -1.9)]
        tools = [station(Iso(x, y - 0.35, 0.6), 0, 0, 1.2, 1.2, 1.0) for x, y in spots]
        shadow = Iso(-3.6, -1.2, 0.72).quad([(-0.35, -0.4, 0), (0.85, -0.4, 0), (0.85, 0.5, 0), (-0.35, 0.5, 0)], "#BFB4A0", sw=0)
        shadow.set_z_index(-1)
        self.play(FadeIn(head), *[GrowFromCenter(t) for t in tools], FadeIn(shadow), run_time=0.7)
        # the step counter: a row of pips toward a stop post
        pips = VGroup(*[Circle(radius=0.13, stroke_color=INK, stroke_width=4, fill_color=CARD, fill_opacity=1).move_to([1.2 + i * 0.5, 2.85, 0])
                        for i in range(8)])
        self.play(FadeIn(pips), run_time=0.4)
        route = [0, 2, 1, 3]
        pos = cr.get_center()
        for i, k in enumerate(route):
            if i == 0:
                until(self, "picks its own route")
            elif i == 1:
                until(self, "checking real results")
            x, y = spots[k]
            dest = np.array([x - 1.35, y - 0.15, 0])
            arc = ArcBetweenPoints(pos, dest, angle=-PI / 3 if i % 2 == 0 else PI / 3)
            trail = DashedVMobject(arc.copy().set_stroke(INK, 4), num_dashes=16)
            self.play(Create(trail), MoveAlongPath(cr, arc), run_time=0.75)
            pos = dest
            self.play(tools[k][1].animate.set_color(TERRA), pips[i].animate.set_fill(INK), run_time=0.3)
        until(self, "stop condition")
        stop = Square(side_length=0.42, fill_color=INK, fill_opacity=1, stroke_width=0).rotate(PI / 4).move_to([5.3, 2.85, 0])
        self.play(GrowFromCenter(stop), run_time=0.4)
        until(self, "maximum number of steps")
        self.play(Indicate(pips, color=None, scale_factor=1.08), run_time=0.6)
        self.play(FadeIn(T("max steps", 36).move_to([0.85, 2.85, 0], aligned_edge=RIGHT)), run_time=0.4)
        finish(self)


# ─────────────── B07 · start simple: climb only when a measurement says so ───────────────
class B07_Simplest(Scene):
    def construct(self):
        S = Iso(-4.9, -2.85, 0.62)
        steps = []
        for i in range(6):
            h = 0.55 * (i + 1)
            blk = S.box(i * 1.9, 0, 0, 1.9, 2.2, h)
            blk.set_z_index(-i)
            steps.append(blk)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.3) for s in steps], lag_ratio=0.15), run_time=0.9)
        tops = [(i * 1.9 + 0.95, 1.1, 0.55 * (i + 1)) for i in range(6)]
        until(self, "Start with the simplest")
        st0 = station(Iso(*S.p(*tops[0])[:2], 0.62), 0.45, 0.55, 0.9, 0.9, 0.8)
        cr = crate(S, tops[0][0] - 0.45, tops[0][1] - 0.5, 0.7, tops[0][2]); cr.set_z_index(3)
        cr.shift(UP * 3); self.add(st0, cr)
        self.play(cr.animate.shift(DOWN * 3), run_time=0.6, rate_func=ease_in)
        here = T("start here", 38).move_to([-2.3, -2.85, 0])
        self.play(FadeIn(here), run_time=0.4)
        until(self, "is enough")
        self.play(st0[1].animate.set_color(TERRA), run_time=0.3)
        ck = check(S.p(*tops[0])[0] + 0.9, S.p(*tops[0])[1] + 0.9, 0.2, TERRA, 7)
        self.play(Create(ck), run_time=0.4)
        until(self, "costs time and money")
        coins = VGroup()
        for i in range(1, 6):
            x, y, z = tops[i]
            for k in range(i):
                c = S.box(x - 0.35, y - 0.35, z + k * 0.2, 0.7, 0.7, 0.16, BAR3, BAR2, BAR1, sw=2)
                coins.add(c)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in coins], lag_ratio=0.04), run_time=1.2)
        until(self, "only when you can measure")
        gx, gy = 5.0, -0.2
        frame = Rectangle(width=0.55, height=2.6, stroke_color=INK, stroke_width=5, fill_color=CARD, fill_opacity=1).move_to([gx, gy, 0])
        line = DashedLine([gx - 0.55, gy + 0.55, 0], [gx + 0.55, gy + 0.55, 0], color=INK, stroke_width=4, dash_length=0.1)
        self.play(FadeIn(frame), Create(line), FadeIn(T("measure", 38).move_to([gx, gy - 1.75, 0])), run_time=0.4)
        fill = Rectangle(width=0.43, height=0.01, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([gx, gy - 1.24, 0], aligned_edge=DOWN)
        self.add(fill)
        self.play(fill.animate.stretch_to_fit_height(1.9, about_edge=DOWN), run_time=0.8)
        self.play(Indicate(line, color=TERRA), run_time=0.3)
        d = np.array(S.p(*tops[1])) - np.array(S.p(*tops[0]))
        c0 = cr.get_center()
        self.play(MoveAlongPath(cr, ArcBetweenPoints(c0, c0 + d, angle=-PI / 3)), run_time=0.5)
        finish(self)
