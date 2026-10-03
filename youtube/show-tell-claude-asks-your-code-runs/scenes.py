"""
Manim scenes for show-tell-claude-asks-your-code-runs (show-tell skill, card #10, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Tool use, from anthropics/courses/tool_use (01 overview, 04 complete workflow) and the current docs:
Claude sits at a desk; your code is a machine at the far end of a belt. A question and tool cards arrive;
Claude writes a request slip (tool_use) and stops; the slip rides to your machine, which runs the function;
a result slip (tool_result) rides back and its id dot ties to the request's; Claude writes the answer.
Then: two slips, two machines, one message back; no slip at all when Claude already knows; and
Anthropic's own grey machine for its server tools, beside the rule that every tool you define, your code runs.
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









# ═════════════════════════════ the film: Claude asks, your code runs ═════════════════════════════
# Cast: Claude as a dark BLOCK on a kraft DESK (a light on its top face); your code as a dark MACHINE (the kit's
# server stack) at the far end of a pale BELT; TOOL CARDS (white cards: dark name bar, grey description lines, an
# outlined input field); request and result SLIPS lying flat on the belt (white; the terracotta dot is the id);
# an ANSWER card with an ink check; a SYSTEM PROMPT note; Anthropic's own grey machine behind the desk.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
BELT = "#E6DFD3"
GREY_TOP, GREY_L, GREY_R = "#C9C4BA", "#A9A398", "#96907F"   # Anthropic's machine: grey, not dark

W = Iso(-2.3, -2.5, 0.75)          # the one rig: desk (near), belt, machine (far)
BW = 1.5                          # belt width (y)
BX0, BX1 = 2.8, 9.0              # belt x range
DESK = (-1.0, -0.4, 0.0, 3.6, 2.4, 0.9)     # x0, y0, z0, w, d, h
DZ = 0.9                                      # desk top
BLOCK = (-0.8, 0.4, DZ, 1.2, 1.2, 0.8)       # Claude's block on the desk
MX, MY = 9.3, 0.05                            # machine 1 (your code)
M2X, M2Y = 5.2, -3.2                           # machine 2 (B06), in front of the belt
SLAB, NSL = 0.4, 3
SPOT_Q = (1.1, 1.0)                            # question card on the desk (x0, y0)
SPOT_R = (1.1, -0.2)                           # request slip kept on the desk (x0, y0)


def belt(iso=W, x0=BX0, x1=BX1, w=BW, th=0.25):
    top = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, w, 0), (x0, w, 0)], BELT, stroke=DIM, sw=2)
    side = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, 0, -th), (x0, 0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)
    end = iso.quad([(x0, 0, 0), (x0, w, 0), (x0, w, -th), (x0, 0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    mid = DashedLine(iso.p(x0 + 0.3, w / 2, 0), iso.p(x1 - 0.3, w / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
    g = VGroup(side, end, top, mid)
    g.set_z_index(-1)
    return g


def desk():
    """(shadow, desk, block, light). Kraft desk with ink outlines; Claude's dark block; the light on its top."""
    x0, y0, z0, w, d, h = DESK
    sh = W.quad([(x0 - 0.2, y0 - 0.45, 0), (x0 + w + 0.3, y0 - 0.45, 0), (x0 + w + 0.3, y0 + d, 0), (x0 - 0.2, y0 + d, 0)], SHADOW, sw=0)
    sh.set_z_index(-2)
    dk = W.box(x0, y0, z0, w, d, h, BOX_TOP, BOX_IN1, BOX_IN2)
    dk.set_z_index(0)
    bx, by, bz, bw, bd, bh = BLOCK
    blk = W.box(bx, by, bz, bw, bd, bh, DARK_TOP, DARK_L, DARK_R)
    blk.set_z_index(1)
    light = Dot(W.p(bx + bw / 2, by + bd / 2, bz + bh), radius=0.11, color=GHOST).set_z_index(2)
    return sh, dk, blk, light


def machine(y0=MY, x0=MX, faces=(DARK_TOP, DARK_L, DARK_R)):
    """(shadow, stack, lights). The kit's server stack; lights start ghost."""
    sh = W.quad([(x0 - 0.2, y0 - 0.4, 0), (x0 + 1.7, y0 - 0.4, 0), (x0 + 1.7, y0 + 1.4, 0), (x0 - 0.2, y0 + 1.4, 0)], SHADOW, sw=0)
    sh.set_z_index(-2)
    stack = VGroup(*[W.box(x0, y0, i * (SLAB + 0.04), 1.4, 1.4, SLAB, *faces) for i in range(NSL)])
    lights = VGroup(*[Dot(W.p(x0 + 0.3 + 0.35 * k, y0, i * (SLAB + 0.04) + SLAB / 2), radius=0.07, color=GHOST)
                      for i in range(NSL) for k in range(2)])
    stack.set_z_index(3); lights.set_z_index(4)
    return sh, stack, lights


def run_lights(lights):
    """New terracotta dots over the ghost lights (added shapes, one by one)."""
    return VGroup(*[Dot(l.get_center(), radius=0.07, color=TERRA).set_z_index(5) for l in lights])


def slip(x0, y0, z0=0.02, w=1.3, d=0.9, result=False):
    """A slip lying flat: white slab, DIM outline, three lines, a terracotta dot (the id) at its near-left corner."""
    slab = W.box(x0, y0, z0, w, d, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    for f in slab:
        f.set_stroke(DIM, 1.5)
    zt = z0 + 0.05
    col = BAR1 if result else BAR2
    lines = VGroup(*[Line(W.p(x0 + 0.45, y0 + d * f, zt), W.p(x0 + w - 0.15 - 0.25 * (k % 2), y0 + d * f, zt), color=col, stroke_width=4)
                     for k, f in enumerate((0.3, 0.55, 0.8))])
    dot = Dot(W.p(x0 + 0.22, y0 + d * 0.3, zt), radius=0.085, color=TERRA)
    return VGroup(slab, lines, dot)


def q_card():
    """The question card, flat on the desk at SPOT_Q: white, grey lines, no dot."""
    x0, y0 = SPOT_Q
    slab = W.box(x0, y0, DZ, 1.2, 0.85, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    for f in slab:
        f.set_stroke(DIM, 1.5)
    lines = VGroup(*[Line(W.p(x0 + 0.2, y0 + 0.85 * f, DZ + 0.05), W.p(x0 + 1.0 - 0.3 * (k % 2), y0 + 0.85 * f, DZ + 0.05),
                          color=BAR2, stroke_width=4) for k, f in enumerate((0.3, 0.6))])
    return VGroup(slab, lines).set_z_index(2)


def tool_card(c, s=1.0):
    """A tool card (2D): white card, a dark name bar, two grey description lines, an outlined input field."""
    c = np.array([float(c[0]), float(c[1]), 0.0])
    w, h = 1.5 * s, 1.9 * s
    body = RoundedRectangle(width=w, height=h, corner_radius=0.1 * s, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    bar = Rectangle(width=w - 0.3 * s, height=0.26 * s, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * 0.6 * s)
    desc = VGroup(*[Line(c + np.array([-0.55 * s, (0.15 - 0.25 * k) * s, 0]), c + np.array([(0.55 - 0.3 * k) * s, (0.15 - 0.25 * k) * s, 0]),
                         color=BAR2, stroke_width=5) for k in range(2)])
    field = Rectangle(width=1.1 * s, height=0.34 * s, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(c + DOWN * 0.55 * s)
    return VGroup(body, bar, desc, field)


def answer_card(c, s=1.0):
    c = np.array([float(c[0]), float(c[1]), 0.0])
    body = RoundedRectangle(width=2.3 * s, height=1.45 * s, corner_radius=0.12 * s, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    lines = VGroup(*[Line(c + np.array([-0.85 * s, (0.35 - 0.3 * k) * s, 0]), c + np.array([(0.85 - 0.35 * (k % 2)) * s, (0.35 - 0.3 * k) * s, 0]),
                          color=BAR1, stroke_width=6) for k in range(3)])
    return VGroup(body, lines)


def base(lit=True):
    """Belt, desk + Claude, machine 1, and the two cast labels, as B00 leaves them."""
    b = belt()
    sh, dk, blk, light = desk()
    if lit:
        light.set_color(TERRA)
    msh, stack, lights = machine()
    return b, VGroup(sh, dk, blk), light, VGroup(msh, stack), lights, claude_label(), code_label()


def claude_label():
    return T("Claude", 42).move_to([-5.1, -2.8, 0])


def code_label():
    return T("your code", 42).move_to([5.0, 0.45, 0])


def ride(slp, dx, dy=0.0):
    return slp.animate.shift(W.v(dx, dy, 0))


# ─────────────── end states, rebuilt so each beat opens on what the previous one left (continuity) ───────────────
def stop_tag():
    bar = Rectangle(width=0.32, height=0.32, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-5.5, 0.55, 0])
    return VGroup(bar, T("stop_reason: tool_use", 40).next_to(bar, RIGHT, buff=0.3))


def loop_arcs():
    a, m = W.p(1.5, 2.2, DZ + 0.3), W.p(MX - 0.3, 1.9, 1.5)
    out = ArcBetweenPoints(a, m, angle=-0.5).set_stroke(INK, 5)
    back = ArcBetweenPoints(W.p(MX - 0.6, -0.7, 0.2), W.p(2.6, -0.8, 0.2), angle=-0.35).set_stroke(INK, 5)
    tip_o = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.12).move_to(m).rotate(-0.6)
    tip_b = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.12).move_to(back.get_end()).rotate(2.0)
    return out, back, tip_o, tip_b


# ─────────────── B00: Claude at a desk; your code, a machine at the far end ───────────────
class B00_Desk(Scene):
    def construct(self):
        b = belt()
        self.play(FadeIn(b[0:3]), run_time=0.6)
        sh, dk, blk, light = desk()
        g = VGroup(dk, blk, light)
        g.shift(UP * 4)
        self.add(g)
        self.play(g.animate.shift(DOWN * 4), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(sh), FadeIn(claude_label()), run_time=0.35)
        until(self, "At the far end", lead=0.3)
        msh, stack, lights = machine()
        rt = guard(self, 0.9)
        self.play(FadeIn(msh), LaggedStart(*[GrowFromEdge(s, DOWN) for s in stack], lag_ratio=0.3), run_time=rt)
        self.add(lights)
        self.play(FadeIn(code_label()), run_time=0.3)
        until(self, "looking up a stock price", lead=0.3)
        on = run_lights(lights)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.15), run_time=rt)
        self.play(FadeOut(on), run_time=0.3)
        until(self, "connects the two", lead=0.6)
        rt = guard(self, 0.7)
        self.play(Create(b[3]), run_time=rt)
        self.play(light.animate.set_color(TERRA), Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=0.5)
        done(self)


# ─────────────── B01: a question and a stack of tool cards; the code stays home ───────────────
FAN = [(-4.6, 1.8), (-3.3, 2.0), (-2.0, 1.8)]
BIG_C, BIG_S = np.array([-3.7, 1.6, 0]), 1.3


class B01_Cards(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base()
        self.add(b, dk, light, mach, lights, cl, co)
        until(self, "you send a question", lead=0.3)
        q = q_card()
        q.shift(LEFT * 3)
        self.add(q)
        self.play(q.animate.shift(RIGHT * 3), run_time=0.5)
        ql = T("question", 42).move_to([-0.9, 0.3, 0])
        self.play(FadeIn(ql), run_time=0.3)
        until(self, "a stack of tool cards", lead=0.3)
        cards = [tool_card(c) for c in FAN]
        for k, c in enumerate(cards):
            c.shift(UP * 4)
        rt = guard(self, 0.7)
        self.add(*cards)
        self.play(LaggedStart(*[c.animate.shift(DOWN * 4) for c in cards], lag_ratio=0.15), run_time=rt)
        tl = T("tools", 42).move_to([0.0, 2.0, 0])
        self.play(FadeIn(tl), run_time=0.3)
        until(self, "Each card has a name", lead=0.4)
        big = tool_card(BIG_C, BIG_S)
        rt = guard(self, 0.6)
        self.play(FadeOut(tl), FadeOut(ql), FadeOut(cards[0]), FadeOut(cards[2]), ReplacementTransform(cards[1], big), run_time=rt)
        self.play(Indicate(big[1], color=None, scale_factor=1.12), run_time=0.4)
        until(self, "a description", lead=0.2)
        self.play(Indicate(big[2], color=None, scale_factor=1.12), run_time=0.4)
        until(self, "an input schema", lead=0.3)
        tick = Line(big[3].get_right() + RIGHT * 0.15, big[3].get_right() + RIGHT * 0.85, color=INK, stroke_width=5)
        sl = T("input schema", 42).next_to(tick, RIGHT, buff=0.35)
        rt = guard(self, 0.4)
        self.play(Create(tick), Indicate(big[3], color=None, scale_factor=1.1), run_time=rt)
        self.play(FadeIn(sl), run_time=0.3)
        until(self, "Claude sees the cards", lead=0.3)
        tgt = light.get_center()
        rt = guard(self, 0.7)
        self.play(FadeOut(tick), FadeOut(sl), big.animate.scale(0.18).move_to(tgt + UP * 0.2), run_time=rt)
        self.play(FadeOut(big), Flash(tgt, color=TERRA, line_length=0.18, flash_radius=0.3), run_time=0.35)
        until(self, "The code stays with you", lead=0.3)
        on = run_lights(lights)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.1), Indicate(mach[1], color=None, scale_factor=1.04), run_time=0.6)
        done(self)


# ─────────────── B02: Claude writes a request slip, then stops ───────────────
REQ_ON = 4.8                        # where the request slip waits on the belt (x0)


class B02_Ask(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base()
        q = q_card()
        self.add(b, dk, light, mach, lights, cl, co, q)
        until(self, "decides a tool would help", lead=0.3)
        self.play(Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), Indicate(q, color=None, scale_factor=1.05), run_time=0.5)
        until(self, "writes a request slip", lead=0.3)
        keep = slip(*SPOT_R, z0=DZ).set_z_index(2)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(keep), run_time=rt)
        s = slip(*SPOT_R, z0=DZ).set_z_index(2)
        self.add(s)
        rt = guard(self, 0.9)
        self.play(s.animate.move_to(slip(REQ_ON, 0.3).get_center()), run_time=rt)
        s.set_z_index(1)
        ul = T("tool_use", 42).move_to([1.05, -1.3, 0])
        self.play(FadeIn(ul), run_time=0.3)
        until(self, "Then it stops", lead=0.2)
        rt = guard(self, 0.4)
        self.play(light.animate.set_color(GHOST), run_time=rt)
        until(self, "The stop reason", lead=0.3)
        rt = guard(self, 0.4)
        tag = stop_tag()
        self.play(GrowFromCenter(tag[0]), FadeIn(tag[1]), run_time=rt)
        done(self)


# ─────────────── B03: your code reads the slip and runs the function ───────────────
class B03_Run(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base(lit=False)
        q = q_card()
        keep = slip(*SPOT_R, z0=DZ).set_z_index(2)
        s = slip(REQ_ON, 0.3).set_z_index(1)
        carry = VGroup(stop_tag(), T("tool_use", 42).move_to([1.05, -1.3, 0]))
        self.add(b, dk, light, mach, lights, cl, co, q, keep, s, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "your code reads the slip", lead=0.3)
        rt = guard(self, 1.2)
        self.play(ride(s, MX - 0.9 - REQ_ON), run_time=rt, rate_func=linear)
        self.play(ride(s, 0.95), run_time=0.4, rate_func=linear)
        self.remove(s)
        until(self, "runs the real function", lead=0.4)
        on = run_lights(lights)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.2), run_time=rt)
        rl = T("runs", 42).move_to([1.55, 2.6, 0])
        self.play(FadeIn(rl), run_time=0.3)
        until(self, "Claude doesn't run it", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(dk[2], color=None, scale_factor=1.04), run_time=rt)
        until(self, "Your code does", lead=0.3)
        self.play(Indicate(mach[1], color=None, scale_factor=1.05), run_time=0.5)
        done(self)


# ─────────────── B04: the result slip comes back, matched by its id ───────────────
RES_BACK = BX0 + 0.1                # where the result slip stops, at the belt's start


CO1, CO2 = np.array([1.35, -2.0, 0]), np.array([4.55, -2.0, 0])


def callout_card(c, dot_right=True, result=False):
    """A slip, close up (2D): white card, three lines, the terracotta id dot on the edge facing the other card."""
    body = RoundedRectangle(width=2.2, height=1.1, corner_radius=0.1, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    sx = -0.2 if dot_right else 0.2
    lines = VGroup(*[Line(c + np.array([sx - 0.75, 0.28 - 0.28 * k, 0]), c + np.array([sx + 0.75 - 0.3 * (k % 2), 0.28 - 0.28 * k, 0]),
                          color=BAR1 if result else BAR2, stroke_width=6) for k in range(3)])
    dot = Dot(c + np.array([0.85 if dot_right else -0.85, 0.0, 0]), radius=0.11, color=TERRA)
    return VGroup(body, lines, dot).set_z_index(5)


def id_callout():
    c1, c2 = callout_card(CO1, dot_right=True), callout_card(CO2, dot_right=False, result=True)
    l1 = T("tool_use", 38).move_to(CO1 + DOWN * 0.95)
    l2 = T("tool_result", 38).move_to(CO2 + DOWN * 0.95)
    a, z = np.array(c1[2].get_center()), np.array(c2[2].get_center())
    tie = DashedLine(a + RIGHT * 0.15, z + LEFT * 0.15, color=INK, stroke_width=6, dash_length=0.12).set_z_index(6)
    idl = T("id", 42).move_to((a + z) / 2 + UP * 0.6)
    return c1, c2, l1, l2, tie, idl


class B04_Result(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base(lit=False)
        q = q_card()
        keep = slip(*SPOT_R, z0=DZ).set_z_index(2)
        on = run_lights(lights)
        rl = T("runs", 42).move_to([1.55, 2.6, 0])
        self.add(b, dk, light, mach, lights, on, cl, co, q, keep, rl)
        until(self, "sends the output back", lead=0.3)
        r = slip(MX + 0.05, 0.3, result=True).set_z_index(1)
        self.add(r)
        rt = guard(self, 0.6)
        self.play(FadeOut(rl), FadeOut(on), ride(r, -1.5), run_time=rt, rate_func=linear)
        r.set_z_index(3)
        rt = guard(self, 1.6)
        self.play(ride(r, RES_BACK - (MX - 1.45)), run_time=rt, rate_func=linear)
        until(self, "a new user message", lead=0.3)
        self.play(Indicate(r, color=None, scale_factor=1.08), run_time=0.4)
        until(self, "It carries the ID", lead=0.5)
        # close-up callout in the open lower right: the request and the result, their id dots tied
        c1, c2, l1, l2, tie, idl = id_callout()
        a, z = np.array(c1[2].get_center()), np.array(c2[2].get_center())
        rt = guard(self, 0.6)
        self.play(GrowFromPoint(c1, keep.get_center()), GrowFromPoint(c2, r.get_center()), run_time=rt)
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.3)
        rt = guard(self, 0.5)
        self.play(Create(tie), run_time=rt)
        self.play(FadeIn(idl), run_time=0.3)
        until(self, "match them up", lead=0.3)
        self.play(Flash(a, color=TERRA, line_length=0.16, flash_radius=0.26), Flash(z, color=TERRA, line_length=0.16, flash_radius=0.26), run_time=0.5)
        done(self)


# ─────────────── B05: Claude writes the answer; the whole loop ───────────────
ANS_C = np.array([-2.6, 1.55, 0])


def answer_set(c, side):
    ans = answer_card(c)
    return ans, T("answer", 42).next_to(ans, side, buff=0.35)


def result_home():
    return slip(RES_BACK, 0.3, result=True).set_z_index(3)


class B05_Answer(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base(lit=False)
        q = q_card()
        keep = slip(*SPOT_R, z0=DZ).set_z_index(2)
        r = result_home()
        carry = VGroup(*id_callout())
        self.add(b, dk, light, mach, lights, cl, co, q, keep, r, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "has what it was missing", lead=0.3)
        self.play(light.animate.set_color(TERRA), Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=0.5)
        until(self, "writes the answer", lead=0.3)
        ans, al = answer_set(ANS_C, LEFT)
        start = light.get_center()
        rt = guard(self, 0.7)
        self.play(GrowFromPoint(ans, start), run_time=rt)
        ck = check(ANS_C[0] + 1.55, ANS_C[1] + 0.05, 0.22, INK, 8)
        self.play(FadeIn(al), Create(ck), run_time=0.4)
        until(self, "Ask, stop", lead=0.2)
        out, back, tip_o, tip_b = loop_arcs()
        rt = guard(self, 1.2)
        self.play(Create(out), Create(back), run_time=rt)
        self.play(FadeIn(tip_o), FadeIn(tip_b), run_time=0.25)
        until(self, "the whole loop", lead=0.3)
        self.play(Indicate(VGroup(out, back), color=None, scale_factor=1.03), run_time=0.5)
        done(self)


# ─────────────── B06: two calls in one response; both results in one message ───────────────
class B06_Two(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base()
        q = q_card()
        ans, al = answer_set(ANS_C, LEFT)
        carry = VGroup(ans, al, check(ANS_C[0] + 1.55, ANS_C[1] + 0.05, 0.22, INK, 8), *loop_arcs(),
                       slip(*SPOT_R, z0=DZ).set_z_index(2), result_home())
        self.add(b, dk, light, mach, lights, cl, co, q, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "need two lookups", lead=0.3)
        m2sh, m2, l2 = machine(M2Y, M2X)
        rt = guard(self, 0.7)
        self.play(FadeIn(m2sh), LaggedStart(*[GrowFromEdge(s, DOWN) for s in m2], lag_ratio=0.3), run_time=rt)
        self.add(l2)
        until(self, "ask for both in one response", lead=0.3)
        s1 = slip(*SPOT_R, z0=DZ, d=0.6).set_z_index(2)
        s2 = slip(SPOT_R[0], SPOT_R[1] + 0.7, z0=DZ, d=0.6).set_z_index(2)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(s1), GrowFromCenter(s2), run_time=rt)
        m1 = s1.copy(); m2s = s2.copy()
        self.add(m1, m2s)
        rt = guard(self, 0.8)
        self.play(m1.animate.move_to(slip(4.4, 0.1, d=0.6).get_center()), m2s.animate.move_to(slip(4.4, 0.8, d=0.6).get_center()), run_time=rt)
        tc = T("two calls", 42).move_to([1.15, -1.8, 0])
        self.play(FadeIn(tc), run_time=0.3)
        until(self, "Your code runs both", lead=0.4)
        rt = guard(self, 1.1)
        m1.set_z_index(1); m2s.set_z_index(1)
        self.play(ride(m1, MX + 0.4 - 4.4), ride(m2s, M2X + 0.1 - 4.4, -3.3), run_time=rt, rate_func=linear)
        self.remove(m1, m2s)
        on1, on2 = run_lights(lights), run_lights(l2)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in [*on1, *on2]], lag_ratio=0.06), run_time=0.6)
        until(self, "sends both results back", lead=0.6)
        tray_x = MX - 2.1
        tb, tf = W.open_box(tray_x, 0.05, 0.02, 1.8, 1.4, 0.25)
        for f in [*tb, *tf]:
            f.set_stroke(INK, 3)
        r1 = slip(tray_x + 0.25, 0.12, 0.08, w=1.3, d=0.55, result=True)
        r2 = slip(tray_x + 0.25, 0.78, 0.08, w=1.3, d=0.55, result=True)
        tray = VGroup(tb, r2, r1, tf)
        tb.set_z_index(1); r2.set_z_index(1); r1.set_z_index(1); tf.set_z_index(2)
        self.play(FadeOut(tc), FadeIn(tray), FadeOut(on1), FadeOut(on2), run_time=0.3)
        rt = guard(self, 0.9)
        self.play(tray.animate.shift(W.v(BX0 + 0.3 - tray_x, 0, 0)), run_time=rt, rate_func=linear)
        self.play(FadeIn(T("one message", 42).move_to(ONE_MSG)), run_time=0.3)
        until(self, "each with its ID", lead=0.4)
        ties = id_ties(s1, s2, r1, r2)
        self.play(Create(ties), run_time=0.45)
        done(self)


ONE_MSG = [1.0, -2.55, 0]


def id_ties(s1, s2, r1, r2):
    return VGroup(DashedLine(s1[2].get_center(), r1[2].get_center(), color=INK, stroke_width=6, dash_length=0.1),
                  DashedLine(s2[2].get_center(), r2[2].get_center(), color=INK, stroke_width=6, dash_length=0.1)).set_z_index(6)


def b06_end():
    m2sh, m2, l2 = machine(M2Y, M2X)
    s1 = slip(*SPOT_R, z0=DZ, d=0.6).set_z_index(2)
    s2 = slip(SPOT_R[0], SPOT_R[1] + 0.7, z0=DZ, d=0.6).set_z_index(2)
    tx = BX0 + 0.3
    tb, tf = W.open_box(tx, 0.05, 0.02, 1.8, 1.4, 0.25)
    for f in [*tb, *tf]:
        f.set_stroke(INK, 3)
    r1 = slip(tx + 0.25, 0.12, 0.08, w=1.3, d=0.55, result=True)
    r2 = slip(tx + 0.25, 0.78, 0.08, w=1.3, d=0.55, result=True)
    tb.set_z_index(1); r2.set_z_index(1); r1.set_z_index(1); tf.set_z_index(2)
    ties = id_ties(s1, s2, r1, r2)
    return VGroup(m2sh, m2, l2, s1, s2, tb, r2, r1, tf, ties, q_card(), T("one message", 42).move_to(ONE_MSG))


# ─────────────── B07: no tool needed; the system prompt steers ───────────────
NOTE_C = np.array([-4.4, 1.3, 0])
ANS7_C = np.array([-1.7, 1.6, 0])


def note_card():
    body = RoundedRectangle(width=2.0, height=1.6, corner_radius=0.1, fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(NOTE_C)
    bar = Rectangle(width=1.94, height=0.3, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(NOTE_C + UP * 0.63)
    lines = VGroup(*[Line(NOTE_C + np.array([-0.7, 0.2 - 0.3 * k, 0]), NOTE_C + np.array([0.75 - 0.3 * (k % 2), 0.2 - 0.3 * k, 0]),
                          color=BAR1, stroke_width=6) for k in range(3)])
    return VGroup(body, bar, lines)


class B07_Skip(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base(lit=False)
        self.add(b, dk, light, mach, lights, cl, co)
        carry = b06_end()
        self.add(carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "doesn't have to ask", lead=0.3)
        q = q_card()
        q.shift(LEFT * 3)
        self.add(q)
        self.play(q.animate.shift(RIGHT * 3), run_time=0.5)
        until(self, "already knows the answer", lead=0.3)
        self.play(light.animate.set_color(TERRA), Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=0.5)
        until(self, "it can just reply", lead=0.4)
        ans, al = answer_set(ANS7_C, RIGHT)
        rt = guard(self, 0.6)
        self.play(GrowFromPoint(ans, light.get_center()), run_time=rt)
        self.play(FadeIn(al), Indicate(b[2], color=None, scale_factor=1.01), run_time=0.4)
        until(self, "a line in your system prompt", lead=0.4)
        nc = note_card()
        nc.shift(LEFT * 3)
        rt = guard(self, 0.6)
        self.add(nc)
        self.play(nc.animate.shift(RIGHT * 3), run_time=rt)
        spl = T("system prompt", 42).move_to([NOTE_C[0], 2.5, 0])
        self.play(FadeIn(spl), run_time=0.3)
        until(self, "only call the tool when needed", lead=0.3)
        mark = Dot(NOTE_C + np.array([-0.85, -0.1, 0]), radius=0.09, color=TERRA)
        ul = Line(NOTE_C + np.array([-0.7, -0.22, 0]), NOTE_C + np.array([0.45, -0.22, 0]), color=INK, stroke_width=4)
        self.play(GrowFromCenter(mark), Create(ul), run_time=0.4)
        until(self, "steers how often it asks", lead=0.3)
        self.play(Indicate(nc, color=None, scale_factor=1.05), run_time=0.5)
        done(self)


# ─────────────── B08: Anthropic's own tools; every tool you define, your code runs ───────────────
AX, AY = 3.5, -3.3                   # Anthropic's machine, behind the desk


class B08_Server(Scene):
    def construct(self):
        b, dk, light, mach, lights, cl, co = base()
        self.add(b, dk, light, mach, lights, cl, co)
        nc = note_card()
        ans, al = answer_set(ANS7_C, RIGHT)
        carry = VGroup(nc, T("system prompt", 42).move_to([NOTE_C[0], 2.5, 0]), ans, al, q_card(),
                       Dot(NOTE_C + np.array([-0.85, -0.1, 0]), radius=0.09, color=TERRA),
                       Line(NOTE_C + np.array([-0.7, -0.22, 0]), NOTE_C + np.array([0.45, -0.22, 0]), color=INK, stroke_width=4))
        self.add(carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "Anthropic also runs", lead=0.3)
        ash, ast, al = machine(AY, AX, (GREY_TOP, GREY_L, GREY_R))
        for s in ast:
            for f in s:
                f.set_stroke(INK, 4)
        ast.set_z_index(3); al.set_z_index(4); ash.set_z_index(-2)
        rt = guard(self, 0.8)
        self.play(FadeIn(ash), LaggedStart(*[GrowFromEdge(s, DOWN) for s in ast], lag_ratio=0.3), run_time=rt)
        self.add(al)
        an = T("Anthropic", 42).move_to([4.6, -1.65, 0])
        self.play(FadeIn(an), run_time=0.3)
        until(self, "like web search", lead=0.4)
        s = slip(*SPOT_Q, z0=DZ).set_z_index(3)
        self.play(GrowFromCenter(s), run_time=0.3)
        dst = W.p(AX + 0.7, AY + 0.7, 1.5)
        rt = guard(self, 0.7)
        self.play(MoveAlongPath(s, ArcBetweenPoints(s.get_center(), dst, angle=-0.9)), run_time=rt)
        self.play(FadeOut(s), *[GrowFromCenter(d) for d in run_lights(al)], run_time=0.4)
        until(self, "come back without your code", lead=0.4)
        r = slip(*SPOT_Q, z0=DZ, result=True).set_z_index(3)
        home = r.get_center()
        r.move_to(dst)
        self.add(r)
        rt = guard(self, 0.7)
        self.play(MoveAlongPath(r, ArcBetweenPoints(dst, home, angle=0.9)), run_time=rt)
        self.play(Indicate(b[2], color=None, scale_factor=1.01), run_time=0.4)
        until(self, "every tool you define", lead=0.4)
        c = tool_card([-0.2, 1.4, 0], 0.7)
        rt = guard(self, 0.5)
        self.play(FadeIn(c, shift=DOWN * 0.3), run_time=rt)
        self.play(c.animate.scale(0.5).move_to(W.p(MX + 0.7, MY + 0.7, 1.55) + UP * 0.35), run_time=0.8)
        self.play(FadeOut(c), *[GrowFromCenter(d) for d in run_lights(lights)], run_time=0.4)
        until(self, "your code runs", lead=0.2)
        ck = check(5.0, -0.15, 0.22, INK, 8)
        self.play(Create(ck), run_time=0.35)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Desk, B01_Cards, B02_Ask, B03_Run, B04_Result, B05_Answer, B06_Two, B07_Skip, B08_Server):
    _cls.play = ST.play
