"""
Manim scenes for show-tell-loop-that-wont-let-go (show-tell skill, card #13, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The Ralph Loop plugin, from anthropics/claude-plugins-official/plugins/ralph-loop/ (README.md, the commands,
hooks/stop-hook.sh, scripts/setup-ralph-loop.sh): one command pins the prompt above Claude's bench and writes a
state file (prompt, lap counter from 1, cap, promise); Claude works, the repo shelf fills, Claude heads for the
door; the Stop hook at the door reads the state file and Claude's last message, blocks the exit, adds one to the
counter and hands back the same prompt; laps repeat on the same prompt while the work persists; the loop ends on an
exact promise (the hook deletes the state file and the door opens) or at max iterations, done or not; with neither
it runs forever. The plugin's advice: always set the cap; use it for work a test can check; /cancel-ralph stops it.
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










# ═════════════════════════════ the film: the loop that won't let Claude leave ═════════════════════════════
# Cast: Claude as a kraft WORKER with a terracotta spark; a kraft BENCH (lower left); a PINBOARD with the
# PROMPT card (upper left); a kraft SHELF behind the bench (your repo) where upright file pages and grey commit
# cubes pile up; a kraft WALL with a bright DOORWAY (right); a kraft BOOTH with a light and a parking-gate ARM
# (the Stop hook); a STATE FILE card with a big ink lap numeral (top middle); a white promise TOKEN; a TEST BOARD.
SHADOW = "#AFA28A"
GREY_TOP, GREY_L, GREY_R = "#C9C4BA", "#A9A398", "#96907F"

W = Iso(-2.4, -2.6, 0.9)                 # the one rig: the workshop
HOME = (2.4, -0.6)                       # where Claude stands at the bench
GATE_X = 5.7                             # where Claude stops in front of the arm
DOOR_IN = 7.0                            # standing in the doorway
XD = 7.2                                 # the wall plane (x = XD)
PB_C = np.array([-4.6, 2.0, 0])          # pinboard centre (flat)
SF_C = np.array([0.3, 2.5, 0])           # state-file card centre (flat)
NUM_C = np.array([1.6, 2.45, 0])         # the lap numeral
TB_C = np.array([-5.0, -1.45, 0])        # test board (B07)


def lbl(s, at, size=42):
    return T(s, size).move_to(np.array([at[0], at[1], 0]))


L_CLAUDE = (1.25, -2.45)
L_CMD = (-4.7, -2.75)
L_PROMPT = (-4.6, 0.55)
L_REPO = (-3.9, 0.25)
L_STATE = (-1.35, 2.75)
L_LAP = (1.6, 1.6)
L_HOOK = (4.75, -1.65)


def bench():
    legs = VGroup(W.box(0.1, 0.3, 0, 0.22, 0.7, 0.8), W.box(1.68, 0.3, 0, 0.22, 0.7, 0.8))
    top = W.box(0, 0.2, 0.8, 2.0, 0.9, 0.22)
    tool = W.box(0.5, 0.45, 1.02, 0.7, 0.45, 0.16, GREY_TOP, GREY_L, GREY_R, sw=3)
    sh = W.quad([(-0.15, 0.05, 0), (2.25, 0.05, 0), (2.25, 1.15, 0), (-0.15, 1.15, 0)], SHADOW, sw=0).set_z_index(-2)
    return VGroup(sh, legs, top, tool)


def worker(x=HOME[0], y=HOME[1]):
    body = W.box(x - 0.3, y - 0.3, 0, 0.6, 0.6, 1.0)
    spark = Dot(W.p(x, y - 0.3, 0.62), radius=0.11, color=TERRA)
    head = Circle(radius=0.27, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(W.p(x, y, 1.0) + UP * 0.38)
    return VGroup(body, spark, head).set_z_index(8)


def walk(dx):
    return W.v(dx, 0, 0)


def pinboard():
    board = RoundedRectangle(width=2.3, height=1.8, corner_radius=0.1, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(PB_C)
    bar = Rectangle(width=2.1, height=0.24, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(PB_C + UP * 0.68)
    return VGroup(board, bar)


def prompt_card(c=PB_C, s=1.0):
    c = np.array(c, dtype=float)
    card = RoundedRectangle(width=1.6 * s, height=1.05 * s, corner_radius=0.06 * s, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to(c)
    lines = VGroup(*[Line(c + np.array([-0.55 * s, (0.18 - 0.26 * k) * s, 0]), c + np.array([(0.55 - 0.2 * (k == 2)) * s, (0.18 - 0.26 * k) * s, 0]),
                          color=BAR2, stroke_width=6 * s) for k in range(3)])
    pin = Dot(c + np.array([0, 0.4 * s, 0]), radius=0.08 * s, color=TERRA)
    return VGroup(card, lines, pin).set_z_index(3)


# ─── the shelf: your repo ───
SX = [2.8 + 0.44 * k for k in range(6)]


def shelf():
    return W.box(2.6, 1.8, 0, 2.8, 0.8, 0.9).set_z_index(0)


def file_page(k):
    return W.box(SX[k], 1.95, 0.9, 0.14, 0.5, 0.62, PAGE_TOP, PAGE_L, PAGE_R, sw=2.5).set_z_index(1)


def commit(k):
    return W.box(SX[k], 2.02, 0.9, 0.34, 0.34, 0.34, GREY_TOP, GREY_L, GREY_R, sw=3).set_z_index(1)


def item(k):
    return file_page(k) if k % 2 == 0 else commit(k)


# ─── the wall and doorway ───
def door():
    wl = W.quad([(XD, -2.0, 0), (XD, -1.3, 0), (XD, -1.3, 2.1), (XD, -2.0, 2.1)], BOX_L)
    wr = W.quad([(XD, 0.1, 0), (XD, 0.5, 0), (XD, 0.5, 2.1), (XD, 0.1, 2.1)], BOX_L)
    lin = W.quad([(XD, -1.3, 1.75), (XD, 0.1, 1.75), (XD, 0.1, 2.1), (XD, -1.3, 2.1)], BOX_L)
    opening = W.quad([(XD, -1.3, 0), (XD, 0.1, 0), (XD, 0.1, 1.75), (XD, -1.3, 1.75)], "#FFFFFF")
    top = W.quad([(XD, -2.0, 2.1), (XD + 0.3, -2.0, 2.1), (XD + 0.3, 0.5, 2.1), (XD, 0.5, 2.1)], BOX_TOP)
    end = W.quad([(XD, -2.0, 0), (XD + 0.3, -2.0, 0), (XD + 0.3, -2.0, 2.1), (XD, -2.0, 2.1)], BOX_R)
    sill = W.quad([(XD - 0.45, -1.3, 0), (XD, -1.3, 0), (XD, 0.1, 0), (XD - 0.45, 0.1, 0)], DARK_TOP, sw=0)
    return VGroup(opening, wl, wr, lin, top, end, sill).set_z_index(1)


# ─── the Stop hook: a booth and a gate arm ───
PIV = np.array([6.7, -2.3, 1.0])


def booth(lit=False):
    b = W.box(6.5, -2.75, 0, 0.45, 0.45, 1.2)
    light = Dot(W.p(6.72, -2.52, 1.2) + UP * 0.1, radius=0.13, color=TERRA if lit else GHOST)
    return VGroup(b, light).set_z_index(5)


def arm(a_deg):
    a = np.radians(a_deg)
    d = np.array([0.0, np.cos(a), np.sin(a)])
    n = np.array([0.0, -np.sin(a), np.cos(a)])
    L, t = 2.6, 0.16
    cs = [PIV - n * t, PIV + d * L - n * t, PIV + d * L + n * t, PIV + n * t]
    return Polygon(*[W.p(*c) for c in cs], fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4).set_z_index(4)


def swing(self, arm_mob, a0, a1, rt=0.5):
    rt = guard(self, rt)
    self.play(UpdateFromAlphaFunc(arm_mob, lambda m, al: m.become(arm(a0 + (a1 - a0) * al))), run_time=rt)


# ─── the state file ───
def state_card(n_lines=4):
    c = SF_C
    card = RoundedRectangle(width=1.05, height=1.2, corner_radius=0.06, fill_color="#FFFFFF", fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    bar = Rectangle(width=0.85, height=0.2, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * 0.42)
    card = VGroup(card, bar)
    lines = VGroup(*[Line(c + np.array([-0.32, 0.16 - 0.2 * k, 0]), c + np.array([0.32, 0.16 - 0.2 * k, 0]), color=BAR1, stroke_width=6)
                     for k in range(n_lines)])
    return VGroup(card, lines).set_z_index(3)


def numeral(n):
    return T(str(n), 96, INK, bold=True).move_to(NUM_C)


def set_num(self, old, n, rt=0.25):
    new = numeral(n)
    rt = guard(self, rt)
    self.play(FadeOut(old, shift=UP * 0.25), FadeIn(new, shift=UP * 0.25), run_time=rt)
    return new


def token(at):
    at = np.array(at, dtype=float)
    card = RoundedRectangle(width=0.8, height=0.55, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(at)
    dot = Dot(at, radius=0.1, color=TERRA)
    return VGroup(card, dot).set_z_index(9)


def head_pt(x, y=HOME[1]):
    return W.p(x, y, 1.0) + UP * 1.2


# ─── states carried between beats ───
def s_b00():
    return VGroup(bench(), pinboard(), prompt_card())


def s_b01():
    return VGroup(door(), state_card())


def s_b02_shelf(n=2):
    return VGroup(shelf(), *[item(k) for k in range(n)])


# ─── B00: one command; the task becomes the prompt, pinned above the bench ───
class B00_Command(Scene):
    def construct(self):
        b = bench()
        b.shift(UP * 5)
        self.add(b)
        self.play(b.animate.shift(DOWN * 5), run_time=0.7, rate_func=ease_in)
        w = worker()
        w.shift(LEFT * 3)
        self.add(w)
        self.play(w.animate.shift(RIGHT * 3), run_time=0.6)
        self.play(FadeIn(lbl("Claude", L_CLAUDE)), run_time=0.3)
        until(self, "You run one command", lead=0.3)
        cmd = lbl("/ralph-loop", L_CMD)
        rt = guard(self, 0.4)
        self.play(FadeIn(cmd, shift=RIGHT * 0.3), run_time=rt)
        until(self, "with your task in quotes", lead=0.3)
        pb = pinboard()
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(pb), run_time=rt)
        until(self, "That task becomes the prompt", lead=0.3)
        start = np.array([L_CMD[0], L_CMD[1] + 0.75, 0])
        pc = prompt_card(start, 0.35)
        self.play(GrowFromCenter(pc), run_time=0.3)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(pc, ArcBetweenPoints(start, PB_C, angle=-0.5)), run_time=rt)
        self.play(pc.animate.scale(1 / 0.35), run_time=0.35)
        self.play(FadeIn(lbl("prompt", L_PROMPT)), run_time=0.3)
        done(self)


# ─── B01: the state file ───
class B01_StateFile(Scene):
    def construct(self):
        self.add(s_b00(), worker(), lbl("prompt", L_PROMPT))
        carry = VGroup(lbl("Claude", L_CLAUDE), lbl("/ralph-loop", L_CMD))
        self.add(carry)
        self.play(FadeOut(carry), run_time=0.4)
        dr = door()
        dr.shift(RIGHT * 4)
        self.add(dr)
        self.play(dr.animate.shift(LEFT * 4), run_time=0.6)
        until(self, "a small state file", lead=0.3)
        sc = state_card(0)
        sc.shift(UP * 2.5)
        self.add(sc)
        rt = guard(self, 0.5)
        self.play(sc.animate.shift(DOWN * 2.5), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(lbl("state file", L_STATE)), run_time=0.3)
        ln = state_card()[1]
        until(self, "It holds the prompt", lead=0.2)
        self.play(Create(ln[0]), run_time=0.3)
        until(self, "a lap counter", lead=0.2)
        self.play(Create(ln[1]), run_time=0.3)
        nm = numeral(1)
        rt = guard(self, 0.35)
        self.play(GrowFromCenter(nm), run_time=rt)
        self.play(FadeIn(lbl("lap", L_LAP)), run_time=0.3)
        until(self, "your cap on laps", lead=0.2)
        self.play(Create(ln[2]), run_time=0.3)
        until(self, "your promise phrase", lead=0.2)
        self.play(Create(ln[3]), run_time=0.3)
        done(self)


# ─── B02: Claude works; the repo shelf fills; Claude heads for the door ───
class B02_Work(Scene):
    def construct(self):
        self.add(s_b00(), s_b01(), numeral(1), lbl("state file", L_STATE), lbl("lap", L_LAP))
        w = worker()
        self.add(w)
        pl = lbl("prompt", L_PROMPT)
        self.add(pl)
        self.play(FadeOut(pl), run_time=0.3)
        sh = shelf()
        sh.shift(UP * 4)
        self.add(sh)
        rt = guard(self, 0.5)
        self.play(sh.animate.shift(DOWN * 4), run_time=rt, rate_func=ease_in)
        until(self, "Files change", lead=0.2)
        its = [item(k) for k in range(2)]
        for it in its:
            it.shift(UP * 1.2)
        self.add(*its)
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[it.animate.shift(DOWN * 1.2) for it in its], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(lbl("your repo", L_REPO)), run_time=0.3)
        until(self, "heads for the door", lead=0.5)
        rt = guard(self, 1.1)
        self.play(w.animate.shift(walk(GATE_X - HOME[0])), run_time=rt)
        done(self)


def s_b02():
    return VGroup(s_b00(), s_b01(), s_b02_shelf(2))


# ─── B03: the Stop hook blocks the exit, adds one, hands back the same prompt ───
class B03_Hook(Scene):
    def construct(self):
        self.add(s_b02(), lbl("state file", L_STATE), lbl("lap", L_LAP))
        nm = numeral(1)
        self.add(nm)
        w = worker().shift(walk(GATE_X - HOME[0]))
        self.add(w)
        rp = lbl("your repo", L_REPO)
        self.add(rp)
        self.play(FadeOut(rp), run_time=0.3)
        bt = booth()
        am = arm(90)
        grp = VGroup(bt, am)
        grp.shift(DOWN * 4)
        self.add(grp)
        rt = guard(self, 0.5)
        self.play(grp.animate.shift(UP * 4), run_time=rt)
        self.play(FadeIn(lbl("Stop hook", L_HOOK)), run_time=0.3)
        until(self, "It reads the state file", lead=0.2)
        sc_ref = state_card()
        self.add(sc_ref)
        rt = guard(self, 0.5)
        self.play(Indicate(sc_ref, color=None, scale_factor=1.12), bt[1].animate.set_color(TERRA), run_time=rt)
        until(self, "it blocks the exit", lead=0.3)
        swing(self, am, 90, 0, 0.5)
        self.play(Flash(bt[1].get_center(), color=TERRA, line_length=0.18, flash_radius=0.32), run_time=0.4)
        until(self, "adds one to the counter", lead=0.2)
        nm = set_num(self, nm, 2)
        until(self, "hands back the same prompt", lead=0.3)
        a = bt[1].get_center() + UP * 0.3
        cp = prompt_card(a, 0.35)
        self.play(GrowFromCenter(cp), run_time=0.25)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(cp, ArcBetweenPoints(a, PB_C, angle=0.5)), run_time=rt)
        self.play(cp.animate.scale(1 / 0.35), run_time=0.3)
        rt = guard(self, 0.9)
        self.play(w.animate.shift(walk(HOME[0] - GATE_X)), bt[1].animate.set_color(GHOST), run_time=rt)
        done(self)


def s_b03():
    return VGroup(s_b02(), booth(), arm(0))


# ─── B04: laps; the prompt never changes, the work piles up ───
class B04_Laps(Scene):
    def construct(self):
        self.add(s_b03(), lbl("state file", L_STATE), lbl("lap", L_LAP), lbl("Stop hook", L_HOOK))
        nm = numeral(2)
        w = worker()
        self.add(nm, w)
        until(self, "The prompt never changes", lead=0.2)
        pin = prompt_card()
        self.add(pin)
        self.play(Indicate(pin, color=None, scale_factor=1.08), run_time=0.5)
        bt_light = booth()[1]
        self.add(bt_light)
        n = 2
        k = 2
        for lap in range(2):
            ph = ["Each lap", "and picks up where it left off"][lap]
            until(self, ph, lead=0.3)
            rt = guard(self, 0.7)
            self.play(w.animate.shift(walk(GATE_X - HOME[0])), run_time=rt)
            rt = guard(self, 0.25)
            self.play(bt_light.animate.set_color(TERRA), run_time=rt)
            n += 1
            nm = set_num(self, nm, n)
            rt = guard(self, 0.7)
            self.play(w.animate.shift(walk(HOME[0] - GATE_X)), bt_light.animate.set_color(GHOST), run_time=rt)
            its = [item(k), item(k + 1)]
            for it in its:
                it.shift(UP * 1.2)
            self.add(*its)
            rt = guard(self, 0.45)
            self.play(LaggedStart(*[it.animate.shift(DOWN * 1.2) for it in its], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
            k += 2
        until(self, "every lap is another full turn", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*[item(j) for j in range(6)]), color=None, scale_factor=1.04), run_time=rt)
        done(self)


def s_b04():
    return VGroup(s_b00(), s_b01(), s_b02_shelf(6), booth(), arm(0))


# ─── B05: the promise; the hook deletes the state file; the door opens ───
class B05_Promise(Scene):
    def construct(self):
        base = VGroup(s_b00(), door(), s_b02_shelf(6), booth())
        sc = state_card()
        nm = numeral(4)
        am = arm(0)
        w = worker()
        labs = VGroup(lbl("state file", L_STATE), lbl("lap", L_LAP))
        hk = lbl("Stop hook", L_HOOK)
        self.add(base, sc, nm, am, w, labs, hk)
        until(self, "Claude writes your promise phrase", lead=0.2)
        tk = token(head_pt(HOME[0]))
        rt = guard(self, 0.35)
        self.play(GrowFromCenter(tk), run_time=rt)
        pl = lbl("promise", (HOME[0] - 1.35, 0.2))
        pl.move_to(head_pt(HOME[0]) + RIGHT * 1.45)
        self.play(FadeIn(pl), run_time=0.3)
        until(self, "The hook sees it", lead=0.35)
        rt = guard(self, 0.8)
        self.play(FadeOut(pl), VGroup(w, tk).animate.shift(walk(GATE_X - HOME[0])), run_time=rt)
        lt = booth()[1]
        ck = check(W.p(6.72, -2.52, 1.2)[0] + 0.7, W.p(6.72, -2.52, 1.2)[1] + 0.35, 0.18, INK, 7)
        rt = guard(self, 0.35)
        self.play(Create(ck), run_time=rt)
        until(self, "deletes the state file", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeOut(sc), FadeOut(nm), FadeOut(labs), run_time=rt)
        until(self, "opens the door", lead=0.2)
        swing(self, am, 0, 90, 0.5)
        rt = guard(self, 0.8)
        self.play(VGroup(w, tk).animate.shift(walk(DOOR_IN - GATE_X)), run_time=rt)
        until(self, "only when it's completely true", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(tk, color=None, scale_factor=1.2), run_time=rt)
        done(self)


# ─── B06: the cap; done or not; with neither, forever ───
RING_C, RING_A, RING_B = ((HOME[0] + GATE_X) / 2 + 0.2, -0.6), 2.35, 0.95


def ring_pt(t):
    return W.p(RING_C[0] + RING_A * np.cos(t), RING_C[1] + RING_B * np.sin(t), 0)


def ring():
    return VMobject(stroke_color=INK, stroke_width=5).set_points_smoothly([ring_pt(t) for t in np.linspace(0, 2 * np.pi, 73)]).set_z_index(-1)


L_MAX = (1.6, 1.6)
L_FOREVER = (1.3, -2.85)


class B06_Cap(Scene):
    def construct(self):
        base = VGroup(s_b00(), door(), s_b02_shelf(6), booth())
        am = arm(90)
        w = worker().shift(walk(DOOR_IN - HOME[0]))
        tk = token(head_pt(DOOR_IN))
        hk = lbl("Stop hook", L_HOOK)
        ck = check(W.p(6.72, -2.52, 1.2)[0] + 0.7, W.p(6.72, -2.52, 1.2)[1] + 0.35, 0.18, INK, 7)
        self.add(base, am, w, tk, hk, ck)
        sc = state_card()
        nm = numeral(8)
        mx = lbl("max 10", L_MAX)
        self.play(FadeOut(tk), FadeOut(ck), w.animate.shift(walk(GATE_X - DOOR_IN)), run_time=0.45)
        self.play(FadeIn(sc), FadeIn(nm), FadeIn(mx), UpdateFromAlphaFunc(am, lambda m, al: m.become(arm(90 * (1 - al)))), run_time=0.45)
        until(self, "the counter reaches", lead=0.2)
        nm = set_num(self, nm, 9, 0.25)
        nm = set_num(self, nm, 10, 0.25)
        until(self, "The hook ends the loop", lead=0.3)
        swing(self, am, 0, 90, 0.4)
        rt = guard(self, 0.6)
        self.play(w.animate.shift(walk(DOOR_IN - GATE_X)), run_time=rt)
        until(self, "done or not", lead=0.2)
        q = T("?", 64, INK, bold=True).move_to([-1.0, 2.35, 0])
        rt = guard(self, 0.3)
        self.play(FadeIn(q), run_time=rt)
        until(self, "Set neither one", lead=0.2)
        r = ring()
        rt = guard(self, 0.7)
        self.play(Create(r), FadeOut(sc), FadeOut(nm), FadeOut(mx), w.animate.shift(walk(HOME[0] - DOOR_IN)),
                  UpdateFromAlphaFunc(am, lambda m, al: m.become(arm(90 * (1 - al)))), run_time=rt)
        rider = Dot(ring_pt(np.pi), radius=0.13, color=TERRA).set_z_index(-1)
        self.add(rider)
        self.play(FadeIn(lbl("forever", L_FOREVER)), run_time=0.3)
        arc = VMobject().set_points_smoothly([ring_pt(t) for t in np.linspace(np.pi, 3 * np.pi, 73)])
        rt = guard(self, 1.2)
        self.play(MoveAlongPath(rider, arc), run_time=rt, rate_func=linear)
        done(self)


# ─── B07: the plugin's advice; /cancel-ralph ───
def test_board():
    c = TB_C
    board = RoundedRectangle(width=1.7, height=1.9, corner_radius=0.08, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    rows = VGroup(*[RoundedRectangle(width=0.7, height=0.3, corner_radius=0.05, fill_color=BAR2, fill_opacity=1, stroke_width=0)
                    .move_to(c + np.array([-0.3, 0.55 - 0.55 * k, 0])) for k in range(3)])
    return VGroup(board, rows).set_z_index(3)


def test_check(k):
    return check(TB_C[0] + 0.42, TB_C[1] + 0.55 - 0.55 * k + 0.02, 0.15, INK, 7).set_z_index(4)


class B07_Advice(Scene):
    def construct(self):
        base = VGroup(s_b00(), door(), s_b02_shelf(6), booth())
        am = arm(0)
        w = worker()
        hk = lbl("Stop hook", L_HOOK)
        r = ring()
        rider = Dot(ring_pt(np.pi), radius=0.13, color=TERRA).set_z_index(-1)
        q = T("?", 64, INK, bold=True).move_to([-1.0, 2.35, 0])
        fv = lbl("forever", L_FOREVER)
        self.add(base, am, w, hk, r, rider, q, fv)
        self.play(FadeOut(r), FadeOut(rider), FadeOut(q), FadeOut(fv), run_time=0.4)
        sc = state_card()
        nm = numeral(10)
        mx = lbl("max 10", L_MAX)
        self.play(FadeIn(sc), FadeIn(nm), FadeIn(mx), run_time=0.5)
        until(self, "always set max iterations", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(nm, mx), color=None, scale_factor=1.12), run_time=rt)
        until(self, "The cap is your main safety net", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(am, color=None, scale_factor=1.06), run_time=rt)
        until(self, "work a test can check", lead=0.3)
        tb = test_board()
        tb.shift(DOWN * 4)
        self.add(tb)
        rt = guard(self, 0.5)
        self.play(tb.animate.shift(UP * 4), run_time=rt)
        self.play(FadeIn(lbl("tests", (TB_C[0], TB_C[1] - 1.4))), run_time=0.3)
        for k in range(3):
            rt = guard(self, 0.25)
            self.play(Create(test_check(k)), run_time=rt)
        until(self, "And to stop early", lead=0.1)
        x = VGroup(Line(SF_C + np.array([-0.45, -0.5, 0]), SF_C + np.array([0.45, 0.5, 0]), color=INK, stroke_width=8),
                   Line(SF_C + np.array([-0.45, 0.5, 0]), SF_C + np.array([0.45, -0.5, 0]), color=INK, stroke_width=8)).set_z_index(5)
        rt = guard(self, 0.35)
        self.play(Create(x), FadeOut(mx), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(VGroup(sc, x, nm)), run_time=rt)
        self.play(FadeIn(lbl("/cancel-ralph", (SF_C[0] + 0.5, SF_C[1]))),
                  UpdateFromAlphaFunc(am, lambda m, al: m.become(arm(90 * al))), run_time=0.45)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Command, B01_StateFile, B02_Work, B03_Hook, B04_Laps, B05_Promise, B06_Cap, B07_Advice):
    _cls.play = ST.play
