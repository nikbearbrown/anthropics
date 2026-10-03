"""
Manim scenes for show-tell-screenshot-point-click (show-tell skill, card #21, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Computer use, from anthropics/claude-quickstarts/computer-use-demo/ (README, loop.py, tools/computer.py),
computer-use-best-practices/README.md and the raw live docs page (computer-use-tool.md, 2026-09-27): a kraft
CRATE (the Docker container) with a flat MONITOR standing in it (grey bezel, cream screen, grey title bar,
a window, a button with a terracotta dot); YOUR CODE, a kraft terminal inside the crate (the demo's agent loop
runs in the container); a grey CABLE out to the kraft CLAUDE box (dark slot, dark mouth, terracotta spark);
the SCREENSHOT, a small framed copy of the screen; the ACTION slip; a grey TARGET ring with a terracotta dot;
the kit cursor; a rail of screenshots and a grey token bar; terracotta tape on the crate; a login card;
four allowlist sites; a planted note; a gate, your signal board and a confirm pill.
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







# ═════════════════════════════ the film: screenshot, point, click ═════════════════════════════
# Cast: the kraft CRATE (the Docker container) with a flat MONITOR standing in it; YOUR CODE, a kraft terminal in
# the crate; a grey CABLE to the kraft CLAUDE box (dark slot on top, dark mouth on its left face, terracotta spark);
# the SCREENSHOT (a small framed copy of the screen); the ACTION slip; a grey TARGET ring with a terracotta dot.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


def cross(x, y, s=0.22, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w))


def slip(s=1.0, dot=False):
    body = RoundedRectangle(width=0.8, height=0.52, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.24, 0.07, 0], [0.26, 0.07, 0], color=BAR1, stroke_width=6),
                Line([-0.24, -0.09, 0], [0.12, -0.09, 0], color=BAR1, stroke_width=6))
    g = VGroup(body, ln)
    if dot:
        ln.shift(RIGHT * 0.08)
        g.add(Dot([-0.27, 0.0, 0], radius=0.07, color=TERRA))
    return g.scale(s).set_z_index(10)


# ─── the CLAUDE box ───
CW, CD, CH = 2.4, 2.0, 1.6


class CBox:
    def __init__(self, cx, cy, s):
        self.iso = rig_at(cx, cy, s, CW, CD)
        self.cx, self.cy, self.s = cx, cy, s

    def mob(self):
        i = self.iso
        body = i.box(0, 0, 0, CW, CD, CH)
        slot = i.quad([(0.5, 0.82, CH), (1.9, 0.82, CH), (1.9, 1.18, CH), (0.5, 1.18, CH)], DARK_TOP, sw=0)
        mouth = i.quad([(0, 0.45, 0.12), (0, 1.55, 0.12), (0, 1.55, 0.72), (0, 0.45, 0.72)], DARK_L, sw=0)
        spark = Dot(i.p(CW * 0.55, 0, CH * 0.6), radius=0.15 * self.s / 0.8, color=TERRA)
        return VGroup(body, slot, mouth, spark)

    def slot(self):
        return self.iso.p(1.2, 1.0, CH)

    def mouth(self):
        return self.iso.p(0, 1.0, 0.42)


def box_to(mob, A, B):
    """Animate a box built on CBox A to CBox B (linear projection: scale + shift)."""
    return mob.animate.scale(B.s / A.s, about_point=A.iso.p(0, 0, 0)).shift(B.iso.p(0, 0, 0) - A.iso.p(0, 0, 0))


# ─── YOUR CODE: a kraft terminal; YOU: a dark signal board ───
TW, TD, TH = 1.3, 1.1, 1.0


def terminal(cx, cy, s=0.9):
    i = rig_at(cx, cy, s, TW, TD)
    body = i.box(0, 0, 0, TW, TD, TH)
    scr = i.quad([(0, 0.15, 0.22), (0, 0.95, 0.22), (0, 0.95, 0.86), (0, 0.15, 0.86)], DARK_TOP, sw=0)
    cur = Dot(i.p(0, 0.35, 0.42), radius=0.07, color=TERRA)
    return VGroup(body, scr, cur).set_z_index(1.5), i


BDW, BDD, BDH = 0.3, 1.4, 1.45


def board(c, on=False):
    i = rig_at(c[0], c[1], 0.8, BDW, BDD)
    b = i.box(0, 0, 0, BDW, BDD, BDH, DARK_TOP, DARK_L, DARK_R)
    lamp = Circle(radius=0.19, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=GHOST, stroke_width=2).move_to(i.p(0, BDD / 2, BDH * 0.55))
    return VGroup(b, lamp)


# ─── the CRATE (container), the MONITOR (desktop) standing in it ───
CRW, CRD, CRH = 6.2, 2.0, 0.95
CR = rig_at(-2.5, -1.3, 0.72, CRW, CRD)
MC = np.array([-3.45, 1.3, 0.0])            # monitor (bezel) centre
MW, MH = 3.4, 2.3                           # bezel
SW, SH = 3.12, 1.97                         # screen (w / h = 1.58)
SCC = MC + np.array([0.0, 0.03, 0.0])       # screen centre
BTN = (0.74, 0.64)                          # the button, in screen fractions from the top left (u, v)
TERM_C = CR.p(5.7, 1.0, 0)


def crate():
    back, front = CR.open_box(0, 0, 0, CRW, CRD, CRH)
    return back, front


def U(c, w, h, u, v):
    c = P3(c)
    return np.array([c[0] + (u - 0.5) * w, c[1] + (0.5 - v) * h, 0.0])


def content(c, w, h, opened=False, note=False, pressed=False):
    """The desktop: title bar, a window with lines, a button (terracotta dot); optional new window and planted note."""
    k = w / SW
    sw = max(1.5, 3.5 * k)
    bg = Rectangle(width=w, height=h, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to(P3(c))
    bar = Rectangle(width=w, height=h * 0.13, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to(U(c, w, h, 0.5, 0.065))
    dots = VGroup(*[Dot(U(c, w, h, 0.05 + 0.04 * i, 0.065), radius=0.045 * k, color=GHOST) for i in range(3)])
    wa = Rectangle(width=0.46 * w, height=0.64 * h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=sw).move_to(U(c, w, h, 0.3, 0.54))
    wl = VGroup(*[Line(U(c, w, h, 0.12, v), U(c, w, h, 0.48 if n % 2 == 0 else 0.4, v), color=BAR3, stroke_width=max(2, 7 * k))
                  for n, v in enumerate((0.36, 0.48, 0.6, 0.72))])
    pill_ = RoundedRectangle(width=0.26 * w, height=0.15 * h, corner_radius=0.07 * h, fill_color=BAR3 if pressed else PAGE_TOP, fill_opacity=1,
                             stroke_color=BAR1, stroke_width=sw).move_to(U(c, w, h, *BTN))
    bdot = Dot(U(c, w, h, BTN[0] - 0.08, BTN[1]), radius=0.05 * k, color=TERRA)
    bl = Line(U(c, w, h, BTN[0] - 0.03, BTN[1]), U(c, w, h, BTN[0] + 0.08, BTN[1]), color=BAR1, stroke_width=max(2, 6 * k))
    g = VGroup(bg, bar, dots, VGroup(wa, wl), VGroup(pill_, bdot, bl))
    if opened:
        g.add(newwin(c, w, h))
    if note:
        g.add(planted(c, w, h))
    return g


def newwin(c, w, h):
    k = w / SW
    wb = Rectangle(width=0.34 * w, height=0.3 * h, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=max(1.5, 3.5 * k)).move_to(U(c, w, h, 0.77, 0.33))
    wl = VGroup(*[Line(U(c, w, h, 0.64, v), U(c, w, h, 0.9, v), color=PAGE_TOP, stroke_width=max(2, 7 * k)) for v in (0.28, 0.38)])
    return VGroup(wb, wl)


def planted(c, w, h):
    """A note planted on the web page (kraft, no ink: it sits inside a framed screenshot later)."""
    k = w / SW
    nt = Rectangle(width=0.2 * w, height=0.24 * h, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to(U(c, w, h, 0.3, 0.58))
    nl = VGroup(*[Line(U(c, w, h, 0.23, v), U(c, w, h, 0.37, v), color=DEV_EDGE, stroke_width=max(2, 6 * k)) for v in (0.53, 0.63)])
    return VGroup(nt, nl)


def monitor(opened=False, note=False, pressed=False):
    bezel = RoundedRectangle(width=MW, height=MH, corner_radius=0.14, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to(MC)
    neck = Rectangle(width=0.5, height=2.0, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to(MC + DOWN * (MH / 2 + 0.9))
    g = VGroup(neck, bezel, content(SCC, SW, SH, opened, note, pressed))
    g.set_z_index(1)
    return g


def screen_pt(u, v):
    return U(SCC, SW, SH, u, v)


def photo(c, w, opened=False, note=False, pressed=False):
    """A screenshot: a framed copy of the screen, w wide."""
    h = w * SH / SW
    fr = RoundedRectangle(width=w + 0.14, height=h + 0.14, corner_radius=0.06, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(c))
    return VGroup(fr, content(c, w, h, opened, note, pressed)).set_z_index(9)


def flash():
    return Rectangle(width=SW, height=SH, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0).move_to(SCC).set_z_index(3)


def target(c, r=0.2):
    c = P3(c)
    return VGroup(Circle(radius=r, stroke_color=BAR1, stroke_width=7, fill_opacity=0).move_to(c),
                  Dot(c, radius=0.075, color=TERRA)).set_z_index(12)


# ─── the loop stage: crate + monitor + your code + cable + Claude ───
BXL = CBox(4.3, -1.0, 0.8)
PS = 1.15                                   # small screenshot width
PBC = np.array([1.2, 1.6, 0.0])           # big screenshot centre
PB = 2.9                                    # big screenshot width
PBH = PB * SH / SW


def term_mob():
    return terminal(TERM_C[0], TERM_C[1], 0.8)


def port():
    _, i = term_mob()
    return i.p(TW * 0.75, 0, TH * 0.55)


def mouth_end():
    return BXL.mouth() + LEFT * 0.12


def cable():
    return Line(port(), mouth_end(), color=BAR1, stroke_width=9).set_z_index(3)


def on_cable(t):
    a, b = port(), mouth_end()
    return a + (b - a) * t


def lift_pt():
    return port() + UP * 1.35 + LEFT * 0.2


def l_container():
    return lbl("container", (-4.9, -3.05), 40)


def l_code():
    return lbl("your code", (0.75, -1.55))


def l_claude(c=(4.3, -2.6)):
    return lbl("Claude", c)


def stage(opened=False, note=False, pressed=False, tape=False, with_claude=True, with_cable=True):
    back, front = crate()
    g = VGroup(back, front, monitor(opened, note, pressed), term_mob()[0])
    if tape:
        g.add(crate_tape())
    if with_cable:
        g.add(cable())
    if with_claude:
        g.add(BXL.mob())
    return g


def crate_tape():
    """A grey strap round both front walls of the crate with one terracotta seal: sealed. (A slanted terracotta
    band reads as accent text under GATE T, so the strap is DIM and the seal is a single spark-sized dot.)"""
    z0, z1 = CRH * 0.36, CRH * 0.64
    return VGroup(CR.quad([(0, 0, z0), (CRW, 0, z0), (CRW, 0, z1), (0, 0, z1)], DIM, sw=0),
                  CR.quad([(0, 0, z0), (0, CRD, z0), (0, CRD, z1), (0, 0, z1)], DIM, sw=0),
                  Dot(CR.p(CRW * 0.32, 0, CRH * 0.5), radius=0.15, color=TERRA)).set_z_index(2.5)


# ══════════════ B00: a desktop in a container ══════════════
def b00_state():
    st = stage()
    return VGroup(st, l_container(), l_code(), l_claude())


class B00_Crate(Scene):
    def construct(self):
        back, front = crate()
        rt = guard(self, 0.7)
        self.play(FadeIn(VGroup(back, front), shift=DOWN * 0.4), FadeIn(l_container()), run_time=rt)
        until(self, "runs a whole Linux desktop", lead=0.3)
        mon = monitor()
        neck, bezel, cont = mon[0], mon[1], mon[2]
        rt = guard(self, 0.8)
        self.play(FadeIn(VGroup(neck, bezel), shift=UP * 0.7), run_time=rt)
        rt = guard(self, 0.9)
        self.play(FadeIn(cont[0]), LaggedStart(*[FadeIn(p) for p in cont[1:]], lag_ratio=0.3), run_time=rt)
        until(self, "Claude never connects", lead=0.3)
        box = BXL.mob()
        rt = guard(self, 0.7)
        self.play(FadeIn(box, shift=DOWN * 0.4), FadeIn(l_claude()), run_time=rt)
        until(self, "Your code sits in between", lead=0.3)
        term, _ = term_mob()
        rt = guard(self, 0.6)
        self.play(FadeIn(term, shift=DOWN * 0.4), FadeIn(l_code()), run_time=rt)
        rt = guard(self, 0.7)
        self.play(Create(cable()), run_time=rt)
        until(self, "the live docs now say", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(box[3], color=None, scale_factor=1.6), run_time=rt)
        done(self)


# ══════════════ B01: step one, the screenshot ══════════════
def l_shot():
    return lbl("screenshot", (lift_pt()[0] + 0.45, lift_pt()[1] + 0.85))


def l_task():
    return lbl("task", (lift_pt()[0], lift_pt()[1] + 0.85))


class B01_Snap(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        stg = st[0]
        box = stg[5]
        tk = slip(0.9).move_to(lift_pt())
        lt = l_task()
        rt = guard(self, 0.5)
        self.play(FadeOut(VGroup(st[1], st[2])), FadeIn(tk, shift=DOWN * 0.3), FadeIn(lt), run_time=rt)
        rt = guard(self, 0.9)
        self.play(tk.animate.move_to(BXL.slot() + UP * 0.9), run_time=rt * 0.7)
        self.play(tk.animate.scale(0.25).move_to(BXL.slot()), run_time=rt * 0.3, rate_func=ease_in)
        self.remove(tk)
        until(self, "Claude asks to see the screen", lead=0.2)
        rq = slip(0.7).move_to(BXL.mouth()).scale(0.3)
        self.add(rq)
        rt = guard(self, 0.8)
        self.play(rq.animate.scale(1 / 0.3).move_to(on_cable(0.3) + UP * 0.05), run_time=rt * 0.6)
        self.play(rq.animate.scale(0.3).move_to(port() + UP * 0.1), run_time=rt * 0.4, rate_func=ease_in)
        self.remove(rq)
        until(self, "your code takes a screenshot", lead=0.2)
        fl = flash()
        rt = guard(self, 0.4)
        self.play(FadeIn(fl), run_time=rt * 0.35)
        self.play(FadeOut(fl), run_time=rt * 0.65)
        ph = photo(SCC, SW)
        self.add(ph)
        ls = l_shot()
        rt = guard(self, 0.6)
        self.play(ph.animate.scale(PS / SW).move_to(lift_pt()), FadeOut(lt), FadeIn(ls), run_time=rt)
        until(self, "sends it back", lead=0.7)
        rt = guard(self, 0.7)
        self.play(ph.animate.move_to(BXL.slot() + UP * 0.9), run_time=rt * 0.7)
        self.play(ph.animate.scale(0.25).move_to(BXL.slot()), run_time=rt * 0.3, rate_func=ease_in)
        self.remove(ph)
        rt = guard(self, 0.25)
        self.play(Indicate(box[3], color=None, scale_factor=1.6), FadeOut(ls), run_time=rt)
        done(self)


# ══════════════ B02: Claude points ══════════════
def big_target_pt():
    return U(PBC, PB, PBH, *BTN)


def guides():
    t = big_target_pt()
    top = PBC[1] + PBH / 2
    left = PBC[0] - PB / 2
    return VGroup(Line([t[0], top, 0], [t[0], t[1] + 0.24, 0], color=BAR1, stroke_width=6),
                  Line([left, t[1], 0], [t[0] - 0.24, t[1], 0], color=BAR1, stroke_width=6)).set_z_index(11)


def origin_dot():
    return Dot(U(PBC, PB, PBH, 0.035, 0.065) + RIGHT * 0.02, radius=0.08, color=TERRA).set_z_index(12)


def l_xy():
    t = big_target_pt()
    return lbl("x, y", (PBC[0] + PB / 2 + 0.75, t[1]))


SLIP_PARK = 0.45


def l_left():
    p = on_cable(SLIP_PARK)
    return lbl("left click", (p[0], p[1] - 0.8))


def b02_state():
    return VGroup(stage(), l_claude(), photo(PBC, PB), target(big_target_pt()), guides(), origin_dot(), l_xy(),
                  slip(1.0).move_to(on_cable(SLIP_PARK) + UP * 0.05), l_left())


class B02_Point(Scene):
    def construct(self):
        self.add(stage(), l_claude())
        big = photo(PBC, PB)
        src = big.copy().scale(0.12).move_to(BXL.slot())
        rt = guard(self, 0.8)
        self.play(Transform(src, big), run_time=rt)
        until(self, "a left click", lead=0.2)
        tg = target(big_target_pt())
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(tg), run_time=rt)
        until(self, "an x, y spot", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_xy()), run_time=rt)
        until(self, "counted in pixels", lead=0.2)
        gd = guides()
        rt = guard(self, 0.9)
        self.play(GrowFromCenter(origin_dot()), run_time=rt * 0.3)
        self.play(Create(gd[0]), Create(gd[1]), run_time=rt * 0.7)
        until(self, "It can't click anything", lead=0.3)
        sl = slip(1.0).move_to(BXL.mouth())
        sl.scale(0.3)
        self.add(sl)
        rt = guard(self, 0.9)
        self.play(sl.animate.scale(1 / 0.3).move_to(on_cable(SLIP_PARK) + UP * 0.05), FadeIn(l_left()), run_time=rt)
        done(self)


# ══════════════ B03: your code clicks ══════════════
def l_scale():
    return lbl("scale up", (-4.4, 2.95))


def l_click():
    return lbl("click", (-2.1, 2.95))


def cursor_at(p):
    return cursor(p[0], p[1]).set_z_index(13)


def b03_state():
    return VGroup(stage(opened=True, pressed=True), l_claude(), target(screen_pt(*BTN)), cursor_at(screen_pt(*BTN) + np.array([0.05, -0.05, 0])),
                  l_scale(), l_click())


class B03_Click(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        stg = st[0]
        big, tg, gd, od, lxy, sl, ll = st[2], st[3], st[4], st[5], st[6], st[7], st[8]
        rt = guard(self, 0.6)
        self.play(sl.animate.move_to(port() + UP * 0.1), FadeOut(ll), run_time=rt * 0.7)
        self.play(sl.animate.scale(0.2), run_time=rt * 0.3, rate_func=ease_in)
        self.remove(sl)
        until(self, "If it shrank the screenshot", lead=0.3)
        rt = guard(self, 0.3)
        self.play(FadeOut(VGroup(gd, od, lxy)), run_time=rt)
        until(self, "scales the spot back up", lead=0.3)
        grp = VGroup(big, tg[0])
        k = SW / PB
        rt = guard(self, 1.2)
        self.play(grp.animate.scale(k).move_to(SCC), tg[1].animate.move_to(screen_pt(*BTN)),
                  FadeIn(l_scale()), run_time=rt)
        rt = guard(self, 0.5)
        tgn = target(screen_pt(*BTN))
        self.play(FadeOut(big), Transform(tg, tgn), run_time=rt)
        until(self, "moves the mouse", lead=0.3)
        cur = cursor_at(screen_pt(0.2, 0.9))
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.7)
        self.play(cur.animate.shift(screen_pt(*BTN) + np.array([0.05, -0.05, 0]) - screen_pt(0.2, 0.9)), run_time=rt)
        until(self, "and clicks", lead=0.55)
        mon = stg[2]
        pill_ = mon[2][4][0]
        rt = guard(self, 0.25)
        self.play(Indicate(tg, color=None, scale_factor=1.5), pill_.animate.set_fill(BAR3), run_time=rt)
        nw = newwin(SCC, SW, SH).set_z_index(1)
        rt = guard(self, 0.35)
        self.play(GrowFromCenter(nw), FadeIn(l_click()), run_time=rt)
        done(self)


# ══════════════ B04: round it goes ══════════════
LOOP_C = np.array([1.2, 1.25, 0.0])
LOOP_R = 0.72


def loop_ring(col=INK):
    a0, sweep = PI / 2 + 0.35, -(2 * PI - 0.7)
    arc = Arc(radius=LOOP_R, start_angle=a0, angle=sweep, arc_center=LOOP_C, color=col, stroke_width=9)
    a1 = a0 + sweep
    e = LOOP_C + LOOP_R * np.array([np.cos(a1), np.sin(a1), 0])
    tdir = np.array([np.sin(a1), -np.cos(a1), 0])        # clockwise tangent
    nrm = np.array([np.cos(a1), np.sin(a1), 0])
    tip = Polygon(e + tdir * 0.26, e - nrm * 0.17, e + nrm * 0.17, fill_color=col, fill_opacity=1, stroke_width=0)
    s = LOOP_C + LOOP_R * np.array([np.cos(a0), np.sin(a0), 0])
    dot = Dot(s, radius=0.1, color=TERRA if col == INK else GHOST)
    return VGroup(arc, tip, dot).set_z_index(8)


def answer_card(c):
    c = P3(c)
    body = RoundedRectangle(width=1.4, height=0.95, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=5).move_to(c)
    ln = VGroup(*[Line([c[0] - 0.45, c[1] + y, 0], [c[0] + (0.45 if n % 2 == 0 else 0.2), c[1] + y, 0], color=BAR2, stroke_width=9)
                  for n, y in enumerate((0.2, 0.0, -0.2))])
    return VGroup(body, ln).set_z_index(10)


ANS_C = (4.3, 2.35)


def l_loop():
    return lbl("loop", (LOOP_C[0], LOOP_C[1] + LOOP_R + 0.55))


def l_done():
    return lbl("done", (2.85, 2.35))


def b04_state():
    return VGroup(stage(opened=True, pressed=True), l_claude(), loop_ring(GHOST), answer_card(ANS_C), check(5.45, 2.35, 0.22), l_done())


class B04_Loop(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        rt = guard(self, 0.4)
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5])), run_time=rt)
        fl = flash()
        rt = guard(self, 0.4)
        self.play(FadeIn(fl), run_time=rt * 0.35)
        self.play(FadeOut(fl), run_time=rt * 0.65)
        ph = photo(SCC, SW, opened=True, pressed=True)
        self.add(ph)
        rt = guard(self, 0.5)
        self.play(ph.animate.scale(PS / SW).move_to(lift_pt()), run_time=rt)
        rt = guard(self, 0.9)
        self.play(ph.animate.move_to(BXL.slot() + UP * 0.9), run_time=rt * 0.7)
        self.play(ph.animate.scale(0.25).move_to(BXL.slot()), run_time=rt * 0.3, rate_func=ease_in)
        self.remove(ph)
        until(self, "It picks the next action", lead=0.2)
        sl = slip(1.0).move_to(BXL.mouth()).scale(0.3)
        self.add(sl)
        rt = guard(self, 0.8)
        self.play(sl.animate.scale(1 / 0.3).move_to(on_cable(0.25) + UP * 0.05), run_time=rt)
        until(self, "round it goes", lead=0.3)
        ring = loop_ring()
        rt = guard(self, 0.6)
        ll = l_loop()
        self.play(Create(ring[0]), FadeIn(ring[1]), FadeIn(ring[2]), FadeIn(ll), sl.animate.move_to(port() + UP * 0.1), run_time=rt)
        self.remove(sl)
        rt = guard(self, 1.2)
        self.play(Rotate(ring, angle=-2 * PI, about_point=LOOP_C), run_time=rt)
        until(self, "The loop ends", lead=0.2)
        card = answer_card(ANS_C)
        c0 = card.copy().scale(0.25).move_to(BXL.slot())
        rt = guard(self, 0.8)
        self.play(Transform(c0, card), FadeOut(ll), run_time=rt)
        until(self, "instead of asking", lead=0.2)
        rt = guard(self, 0.6)
        self.play(ring.animate.set_color(GHOST), Create(check(5.45, 2.35, 0.22)), FadeIn(l_done()), run_time=rt)
        done(self)


# ══════════════ B05: screenshots pile up ══════════════
BX5 = CBox(4.55, -0.35, 0.7)
RY = 0.55
RX = [-5.1 + 1.2 * i for i in range(7)]
PW5 = 0.98
BAR_Y = -1.35
BAR_X0 = -5.75
UNIT = 0.86


def rail():
    return Rectangle(width=8.3, height=0.2, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([RX[0] + 3.6 - 0.1, RY - 0.52, 0])


def tok_bar(n):
    w = max(0.05, UNIT * n)
    return Rectangle(width=w, height=0.36, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([BAR_X0 + w / 2, BAR_Y, 0])


def shot5(i, opened=True):
    return photo((RX[i], RY), PW5, opened=opened, pressed=opened)


def l_shots():
    return lbl("screenshots", (-4.2, 1.55))


def l_tok():
    return lbl("tokens", (-4.9, -2.2))


def l_three():
    return lbl("last three", (-3.9, 1.55))


def b05_state():
    return VGroup(BX5.mob(), l_claude((4.55, -2.2)), rail(), VGroup(*[shot5(i) for i in range(4)]), tok_bar(4), l_tok(), l_three(),
                  check(RX[3] + 1.0, RY, 0.22))


class B05_Shelf(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        box, lc = st[0][5], st[1]
        rt = guard(self, 0.5)
        self.play(FadeOut(VGroup(*[st[0][i] for i in range(5)])), FadeOut(VGroup(st[2], st[3], st[4], st[5])), run_time=rt)
        rt = guard(self, 0.7)
        lsh = l_shots()
        self.play(box_to(box, BXL, BX5), lc.animate.move_to([4.55, -2.2, 0]), FadeIn(rail()), FadeIn(lsh), FadeIn(l_tok()), run_time=rt)
        shots = [shot5(i) for i in range(7)]
        bar = tok_bar(0.06)
        self.add(bar)
        for i in range(5):
            rt = guard(self, 0.45)
            self.play(FadeIn(shots[i], shift=DOWN * 0.7), Transform(bar, tok_bar(i + 1)), run_time=rt, rate_func=ease_in if i else smooth)
        until(self, "each one costs tokens", lead=0.2)
        for i in (5, 6):
            rt = guard(self, 0.45)
            self.play(FadeIn(shots[i], shift=DOWN * 0.7), Transform(bar, tok_bar(i + 1)), run_time=rt)
        until(self, "keeping the last three", lead=0.2)
        rt = guard(self, 0.5)
        self.play(*[Indicate(shots[i], color=None, scale_factor=1.08) for i in (4, 5, 6)], run_time=rt)
        until(self, "pruning older ones in batches", lead=0.2)
        old = VGroup(*shots[:4])
        rt = guard(self, 0.8)
        self.play(old.animate.shift(DOWN * 1.2).set_opacity(0), Transform(bar, tok_bar(3)), run_time=rt)
        self.remove(old)
        rt = guard(self, 0.6)
        self.play(*[shots[4 + j].animate.move_to([RX[j], RY, 0]) for j in range(3)], FadeOut(lsh), FadeIn(l_three()), run_time=rt)
        until(self, "not every turn", lead=0.2)
        new = shot5(3)
        rt = guard(self, 0.5)
        self.play(FadeIn(new, shift=DOWN * 0.7), Transform(bar, tok_bar(4)), run_time=rt)
        until(self, "the prompt cache keeps working", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Create(check(RX[3] + 1.0, RY, 0.22)), run_time=rt)
        until(self, "let the API clear", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(box[3], color=None, scale_factor=1.6), run_time=rt)
        done(self)


# ══════════════ B06: the sandbox warning ══════════════
LOGIN_C = np.array([1.35, -2.25, 0.0])
SITES = [np.array([4.9, y, 0.0]) for y in (2.1, 0.95, -0.2, -1.35)]
ALLOW = (0, 2)
EXIT = np.array([-0.35, 0.75, 0.0])


def login_card(c):
    c = P3(c)
    body = RoundedRectangle(width=1.7, height=1.1, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    f1 = RoundedRectangle(width=1.2, height=0.2, corner_radius=0.05, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=2).move_to(c + UP * 0.2)
    f2 = VGroup(*[Dot(c + np.array([-0.45 + 0.18 * k, -0.2, 0]), radius=0.05, color=BAR1) for k in range(6)])
    return VGroup(body, f1, f2).set_z_index(10)


def site(c):
    i = rig_at(c[0], c[1], 0.42, 1.2, 1.2)
    return i.box(0, 0, 0, 1.2, 1.2, 0.9)


def site_line(k):
    return Line(EXIT, SITES[k] + LEFT * 0.62, color=BAR1, stroke_width=7).set_z_index(0)


def l_vm():
    return lbl("dedicated VM", (-4.72, -3.08), 38)


def l_nolog():
    return lbl("no logins", (LOGIN_C[0] + 2.1, LOGIN_C[1]))


def l_allow():
    return lbl("allowlist", (3.2, 2.85))


def b06_state():
    return VGroup(stage(tape=True, with_claude=False, with_cable=False), l_vm(), login_card(LOGIN_C), cross(LOGIN_C[0] - 1.3, LOGIN_C[1], 0.25), l_nolog(),
                  VGroup(*[site(c) for c in SITES]), VGroup(*[site_line(k) for k in ALLOW]),
                  VGroup(*[check(SITES[k][0] + 0.85, SITES[k][1] - 0.05, 0.18) for k in ALLOW]),
                  VGroup(*[cross(SITES[k][0] + 0.85, SITES[k][1] - 0.05, 0.17) for k in range(4) if k not in ALLOW]), l_allow())


class B06_Sandbox(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        rt = guard(self, 0.6)
        self.play(FadeOut(st), run_time=rt)
        stg = stage(with_claude=False, with_cable=False)
        rt = guard(self, 0.7)
        self.play(FadeIn(stg, shift=UP * 0.3), run_time=rt)
        until(self, "Use a dedicated virtual machine", lead=0.2)
        tp = crate_tape()
        rt = guard(self, 0.6)
        self.play(GrowFromEdge(tp, LEFT), FadeIn(l_vm()), run_time=rt)
        until(self, "with minimal privileges", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(tp, color=None, scale_factor=1.04), run_time=rt)
        until(self, "Avoid giving the model", lead=0.2)
        lc = login_card(LOGIN_C + RIGHT * 2.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(lc, shift=LEFT * 0.4), run_time=rt)
        rt = guard(self, 0.7)
        self.play(lc.animate.move_to(LOGIN_C), run_time=rt)
        until(self, "account login information", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Create(cross(LOGIN_C[0] - 1.3, LOGIN_C[1], 0.25)), FadeIn(l_nolog()), run_time=rt)
        until(self, "limit internet access", lead=0.3)
        sites = VGroup(*[site(c) for c in SITES])
        lines = [site_line(k) for k in range(4)]
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(s_, shift=DOWN * 0.3) for s_ in sites], lag_ratio=0.2), run_time=rt)
        rt = guard(self, 0.7)
        self.play(*[Create(l_) for l_ in lines], run_time=rt)
        until(self, "an allowlist of domains", lead=0.3)
        rt = guard(self, 0.8)
        self.play(*[FadeOut(lines[k]) for k in range(4) if k not in ALLOW],
                  *[Create(check(SITES[k][0] + 0.85, SITES[k][1] - 0.05, 0.18)) for k in ALLOW],
                  *[Create(cross(SITES[k][0] + 0.85, SITES[k][1] - 0.05, 0.17)) for k in range(4) if k not in ALLOW],
                  FadeIn(l_allow()), run_time=rt)
        done(self)


# ══════════════ B07: the screen talks back ══════════════
def note_big_pt():
    return U(PBC, PB, PBH, 0.3, 0.58)


def l_inject():
    return lbl("prompt injection", (PBC[0] - 0.2, PBC[1] + PBH / 2 + 0.45))


def flag(c):
    c = P3(c)
    pole = Line(c + DOWN * 0.45, c + UP * 0.45, color=INK, stroke_width=7)
    fl = Polygon(c + UP * 0.45, c + UP * 0.05, c + np.array([0.55, 0.25, 0]), fill_color=TERRA, fill_opacity=1, stroke_width=0)
    return VGroup(pole, fl).set_z_index(13)


FLAG_C = (PBC[0] + PB / 2 + 0.5, PBC[1] + 0.55)


def l_scan():
    return lbl("scan", (FLAG_C[0] + 0.85, FLAG_C[1] - 0.05))


def b07_state():
    return VGroup(stage(note=True, tape=True), l_claude(), photo(PBC, PB, note=True), target(note_big_pt()),
                  Line(note_big_pt(), big_target_pt(), color=BAR1, stroke_width=6).set_z_index(11), l_inject(), flag(FLAG_C), l_scan())


class B07_Inject(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        rt = guard(self, 0.5)
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 10)])), run_time=rt)
        box = BXL.mob()
        cb = cable()
        rt = guard(self, 0.6)
        self.play(FadeIn(box, shift=DOWN * 0.3), FadeIn(l_claude()), Create(cb), run_time=rt)
        until(self, "the screen can talk back", lead=0.3)
        nt = planted(SCC, SW, SH).set_z_index(1)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(nt), run_time=rt)
        until(self, "Instructions on a web page", lead=0.3)
        fl = flash()
        rt = guard(self, 0.35)
        self.play(FadeIn(fl), run_time=rt * 0.35)
        self.play(FadeOut(fl), run_time=rt * 0.65)
        ph = photo(SCC, SW, note=True)
        self.add(ph)
        rt = guard(self, 1.0)
        self.play(ph.animate.scale(PS / SW).move_to(lift_pt()), run_time=rt * 0.4)
        self.play(ph.animate.move_to(BXL.slot() + UP * 0.9), run_time=rt * 0.4)
        self.play(ph.animate.scale(0.25).move_to(BXL.slot()), run_time=rt * 0.2, rate_func=ease_in)
        self.remove(ph)
        big = photo(PBC, PB, note=True)
        src = big.copy().scale(0.12).move_to(BXL.slot())
        rt = guard(self, 0.6)
        self.play(Transform(src, big), run_time=rt)
        tg = target(big_target_pt())
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(tg), run_time=rt)
        until(self, "might override yours", lead=0.3)
        pull = Line(note_big_pt(), big_target_pt(), color=BAR1, stroke_width=6).set_z_index(11)
        rt = guard(self, 0.4)
        self.play(Create(pull), run_time=rt)
        rt = guard(self, 0.6)
        self.play(tg.animate.move_to(note_big_pt()), run_time=rt)
        until(self, "That's prompt injection", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_inject()), run_time=rt)
        until(self, "scans screenshots for it", lead=0.3)
        top, bot = PBC[1] + PBH / 2, PBC[1] - PBH / 2
        scan = Line([PBC[0] - PB / 2 - 0.1, top, 0], [PBC[0] + PB / 2 + 0.1, top, 0], color=TERRA, stroke_width=8).set_z_index(14)
        rt = guard(self, 1.0)
        self.play(FadeIn(scan), run_time=rt * 0.15)
        self.play(scan.animate.move_to([PBC[0], bot, 0]), run_time=rt * 0.7)
        self.play(FadeOut(scan), run_time=rt * 0.15)
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(flag(FLAG_C), DOWN), FadeIn(l_scan()), run_time=rt)
        until(self, "the precautions still matter", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(st[0][4], color=None, scale_factor=1.04), run_time=rt)
        done(self)


# ══════════════ B08: a human confirms ══════════════
GATE_T = 0.2
BD8 = (1.0, 1.35)
PILL_C = np.array([2.6, 1.95, 0.0])


def gate_parts():
    g = on_cable(GATE_T)
    post = Line(g + DOWN * 0.55, g + UP * 0.65, color=INK, stroke_width=9).set_z_index(6)
    arm = Rectangle(width=0.2, height=1.25, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to(g + RIGHT * 0.22 + UP * 0.05).set_z_index(6)
    return post, arm


def confirm_pill(on=False):
    p = RoundedRectangle(width=1.5, height=0.62, corner_radius=0.31, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=4).move_to(PILL_C)
    return VGroup(p, check(PILL_C[0] - 0.05, PILL_C[1], 0.16)).set_z_index(9)


def l_confirm():
    return lbl("you confirm", (PILL_C[0] + 0.3, PILL_C[1] + 0.85))


def l_each():
    return lbl("each action", (0.9, -2.05))


Q_T = [0.4, 0.64, 0.88]


class B08_Confirm(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        stg = st[0]
        rt = guard(self, 0.5)
        self.play(FadeOut(VGroup(*[st[i] for i in range(2, 8)])), FadeOut(stg[2][2][5]), run_time=rt)
        post, arm = gate_parts()
        bd = board(BD8)
        cp = confirm_pill()
        rt = guard(self, 0.7)
        self.play(FadeIn(bd, shift=DOWN * 0.3), FadeIn(cp), FadeIn(post), FadeIn(arm), FadeIn(l_confirm()), run_time=rt)
        until(self, "decisions with real-world", lead=0.3)
        slips = [slip(0.9, dot=True).move_to(BXL.mouth()).scale(0.3) for _ in range(3)]
        self.add(*slips)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[s_.animate.scale(1 / 0.3).move_to(on_cable(Q_T[k]) + UP * 0.05) for k, s_ in enumerate(slips)], lag_ratio=0.25), run_time=rt)
        c0 = PILL_C + np.array([0.9, -0.7, 0])
        cur = cursor_at(c0)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.3)
        self.play(cur.animate.shift(PILL_C + np.array([0.3, -0.05, 0]) - c0), run_time=rt)
        for k, phrase in enumerate(("accepting cookies", "paying", "agreeing to terms")):
            until(self, phrase, lead=0.2)
            s_ = slips[k]
            rt = guard(self, 0.8)
            self.play(Indicate(cur, color=None, scale_factor=0.85), bd[1].animate.set_fill(TERRA), arm.animate.shift(UP * 1.1), cp[0].animate.set_fill(BAR3), run_time=rt * 0.3)
            self.play(s_.animate.move_to(port() + UP * 0.1).scale(0.5), *[slips[m].animate.move_to(on_cable(Q_T[m - k - 1]) + UP * 0.05) for m in range(k + 1, 3)], run_time=rt * 0.45)
            self.remove(s_)
            self.play(bd[1].animate.set_fill(GHOST), arm.animate.shift(DOWN * 1.1), cp[0].animate.set_fill(PAGE_TOP), run_time=rt * 0.25)
        until(self, "several actions in one turn", lead=0.2)
        more = [slip(0.9, dot=True).move_to(BXL.mouth()).scale(0.3) for _ in range(2)]
        self.add(*more)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[s_.animate.scale(1 / 0.3).move_to(on_cable(Q_T[k]) + UP * 0.05) for k, s_ in enumerate(more)], lag_ratio=0.3),
                  FadeIn(l_each()), run_time=rt)
        until(self, "check before each one runs", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(bd[1], color=None, scale_factor=1.5), Indicate(more[0], color=None, scale_factor=1.12), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Crate, B01_Snap, B02_Point, B03_Click, B04_Loop, B05_Shelf, B06_Sandbox, B07_Inject, B08_Confirm):
    _cls.play = ST.play
