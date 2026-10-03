"""
Manim scenes for show-tell-inside-a-plugin-folder (show-tell skill, card #4).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Direct sequel to show-tell-claude-plugin-portal: the same kraft plugin box, now unpacked.
A midpoint guard (ST / guard, from show-tell-context-is-a-budget) keeps every animation off
the clip midpoint, where GATE T and Gate V sample.
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


# ═════════════════════════════ the film: one plugin box, unpacked ═════════════════════════════
# Cast (same box as show-tell-claude-plugin-portal): the kraft PLUGIN BOX with terracotta tape; its
# SHIPPING LABEL on the right face (plugin.json); inside it a small kraft HELPER crate (sub-agent),
# a dark MCP block and a white page. Each part beat lifts one part out and shows what it does.
BW, BD, BH, LIDH = 3.0, 3.0, 1.9, 0.22
MAIN = Iso(0.0, -2.0, 0.78)          # the hero box, centre stage (B00, B01)
HOME = Iso(-4.3, -2.3, 0.5)          # the box, stepped left and smaller (B02 to B06)
SHADOW = "#BFB4A0"
KRAFT_SIDE = "#E8DCC6"


def floor_shadow(iso=MAIN):
    sh = iso.quad([(0.15, -0.35, 0), (BW + 0.35, -0.35, 0), (BW + 0.35, BD - 0.15, 0), (0.15, BD - 0.15, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return sh


def sealed(iso=MAIN):
    return VGroup(iso.box(0, 0, 0, BW, BD, BH), iso.tape(0, 0, BH, BW, BD))


def dpage(iso, x0, y0, z0, w=1.1, d=1.4, dot=True):
    """A flat white page with a DIM outline (an ink-outlined card inside an ink-outlined box reads as
    overlapping text under GATE T), three ghost lines, one terracotta dot."""
    slab = iso.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    for f in slab:
        f.set_stroke(DIM, 2)
    zt = z0 + 0.06
    lines = VGroup(*[Line(iso.p(x0 + 0.2, y0 + d * f, zt), iso.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                     for f in (0.3, 0.5, 0.7)])
    g = VGroup(slab, lines)
    if dot:
        g.add(Dot(iso.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA))
    return g


def crate(iso, x0, y0, z0, w=1.0, d=1.0, h=0.85, light=True):
    """The small kraft helper crate (a sub-agent): no tape (a short tape stripe reads as accent text)."""
    g = VGroup(iso.box(x0, y0, z0, w, d, h))
    if light:
        g.add(Dot(iso.p(x0 + w * 0.5, y0, z0 + h * 0.55), radius=0.05 + 0.07 * iso.s, color=TERRA))
    return g


def contents(iso):
    """What peeks out of the open box: a dark MCP block (back), the helper crate, a white page (front)."""
    blk = iso.mcp(1.7, 1.65, 1.3, 1.0, 1.0, 0.8)
    cr = crate(iso, 0.35, 1.5, 1.25, light=False)
    pg = dpage(iso, 1.35, 0.3, 1.97, 1.2, 1.0, dot=False)
    g = VGroup(blk, cr, pg)
    g.set_z_index(1)
    return g


def label_card(iso):
    """The shipping label on the right front face (plugin.json): white, DIM outline, three ghost lines."""
    y = -0.012
    card = iso.quad([(0.85, y, 0.45), (2.35, y, 0.45), (2.35, y, 1.45), (0.85, y, 1.45)], PAGE_TOP, stroke=DIM, sw=2.5)
    lines = VGroup(*[Line(iso.p(1.05, y, z), iso.p(2.15, y, z), color=GHOST, stroke_width=4) for z in (1.2, 0.95, 0.7)])
    g = VGroup(card, lines)
    g.set_z_index(3)
    return g


def open_box(iso=MAIN, with_card=True):
    """(shadow, back, contents, front, card): the unpacked-state plugin box."""
    back, front = iso.open_box(0, 0, 0, BW, BD, BH)
    parts = [floor_shadow(iso), back, contents(iso), front]
    if with_card:
        parts.append(label_card(iso))
    return VGroup(*parts)


def to_home(g):
    """Animate a MAIN-built group to the HOME rig (the iso projection is linear: scale + shift)."""
    k = HOME.s / MAIN.s
    return g.animate.scale(k, about_point=MAIN.p(0, 0, 0)).shift(HOME.p(0, 0, 0) - MAIN.p(0, 0, 0))


def home_box():
    return open_box(HOME)


def key_shape(s=1.0):
    ring = Circle(radius=0.17 * s, color=INK, stroke_width=7)
    shaft = Line([0.17 * s, 0, 0], [0.75 * s, 0, 0], color=INK, stroke_width=7)
    t1 = Line([0.55 * s, 0, 0], [0.55 * s, -0.17 * s, 0], color=INK, stroke_width=7)
    t2 = Line([0.7 * s, 0, 0], [0.7 * s, -0.13 * s, 0], color=INK, stroke_width=7)
    return VGroup(ring, shaft, t1, t2)


def window(cx, cy, w, h):
    """A Claude Code window: pale card carried by a dark title bar (Gate V)."""
    win = RoundedRectangle(width=w, height=h, corner_radius=0.22, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([cx, cy, 0])
    bar = Rectangle(width=w, height=0.5, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([cx, cy + h / 2 - 0.25, 0])
    dots = VGroup(*[Dot([cx - w / 2 + 0.35 + i * 0.3, cy + h / 2 - 0.25, 0], radius=0.07, color=GHOST) for i in range(3)])
    return VGroup(win, bar, dots)


# ─────────────── B00: the box, and it is a folder ───────────────
class B00_Folder(Scene):
    def construct(self):
        box = sealed(); box.shift(UP * 3.4)
        self.add(box)
        self.play(box.animate.shift(DOWN * 3.4), run_time=1.1, rate_func=rate_functions.ease_out_bounce)
        sh = floor_shadow()
        lab = T("plugin", 44).move_to([0, -2.7, 0])
        self.play(FadeIn(sh), FadeIn(lab, shift=UP * 0.2), run_time=0.5)
        until(self, "just a folder", lead=0.4)
        tab = MAIN.quad([(0.45, BD, BH + LIDH * 0), (1.75, BD, BH), (1.6, BD, BH + 0.8), (0.6, BD, BH + 0.8)], BOX_TOP)
        tab.set_z_index(-0.5)
        flab = T("folder", 40).move_to([-2.75, 2.0, 0])
        self.play(GrowFromEdge(tab, DOWN), FadeIn(flab), run_time=0.5)
        until(self, "Open it", lead=0.3)
        back, front = MAIN.open_box(0, 0, 0, BW, BD, BH)
        lid = VGroup(MAIN.box(0, 0, BH, BW, BD, LIDH), MAIN.tape(0, 0, BH + LIDH, BW, BD, drop=LIDH))
        tab2 = tab.copy().shift(MAIN.v(0, 0, LIDH))
        lidg = VGroup(tab2, lid); lidg.set_z_index(3)
        inside = contents(MAIN); inside.shift(MAIN.v(0, 0, -1.2))
        self.remove(box, tab)
        self.add(back, inside, front, lidg)
        self.play(lidg.animate.shift(UP * 2.3 + RIGHT * 1.2).scale(0.8), FadeOut(flab), run_time=0.8)
        self.play(lidg.animate.shift(UP * 2.0).set_opacity(0), run_time=0.4)
        self.remove(lidg)
        self.play(inside.animate.shift(MAIN.v(0, 0, 1.2)), run_time=0.8)
        done(self)


# ─────────────── B01: the shipping label is plugin.json ───────────────
class B01_Label(Scene):
    def construct(self):
        g = open_box(MAIN, with_card=False)
        lab = T("plugin", 44).move_to([0, -2.7, 0])
        self.add(g, lab)
        card = label_card(MAIN); card.shift(UP * 2.6)
        self.add(card)
        self.play(FadeOut(lab), card.animate.shift(DOWN * 2.6), run_time=0.7, rate_func=ease_in)
        self.play(Indicate(card, color=None, scale_factor=1.06), run_time=0.4)
        until(self, "a file called plugin", lead=0.4)
        cx, cy = 4.4, 0.35
        big = VGroup(Rectangle(width=2.8, height=1.8, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to([cx, cy, 0]))
        rows = [cy + 0.45, cy, cy - 0.45]
        big.set_z_index(4)
        start = card.get_center()
        big.scale(0.35).move_to(start)
        self.add(big)
        jl = T("plugin.json", 40).move_to([cx, cy + 1.75, 0])
        self.play(big.animate.scale(1 / 0.35).move_to([cx, cy, 0]), run_time=0.7)
        self.play(FadeIn(jl), run_time=0.4)
        until(self, "in a folder named", lead=0.3)
        folder = VGroup(
            Polygon([cx - 1.65, cy + 1.2, 0], [cx - 0.55, cy + 1.2, 0], [cx - 0.35, cy + 1.45, 0], [cx - 1.55, cy + 1.45, 0],
                    fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4),
            RoundedRectangle(width=3.3, height=2.4, corner_radius=0.12, fill_color=BOX_TOP, fill_opacity=1,
                             stroke_color=INK, stroke_width=4).move_to([cx, cy, 0]))
        folder.set_z_index(2)
        fl = T(".claude-plugin", 40).move_to([cx, cy - 1.65, 0])
        self.play(FadeIn(folder, scale=0.9), FadeIn(fl), run_time=0.5)
        until(self, "the plugin's name", lead=0.3)
        lines = []
        for i, (y, cue) in enumerate(zip(rows, ["the plugin's name", "a description", "sometimes a version"])):
            until(self, cue, lead=0.3)
            ln = Line([cx - 1.05, y, 0], [cx + (1.05 if i < 2 else 0.2), y, 0], color=GHOST, stroke_width=10)
            ln.set_z_index(5)
            self.play(Create(ln), run_time=0.4)
            lines.append(ln)
        until(self, "Only the name", lead=0.2)
        dot = Dot([cx - 1.05 - 0.28, rows[0], 0], radius=0.09, color=TERRA).set_z_index(5)
        self.play(lines[0].animate.set_color(INK).set_stroke(width=14), GrowFromCenter(dot), run_time=0.5)
        done(self)


# ─────────────── B02: slash commands, triggered by you ───────────────
class B02_Commands(Scene):
    def construct(self):
        g = open_box(MAIN)
        self.add(g)
        self.play(to_home(g), run_time=0.7)
        pg = dpage(HOME, 1.0, 0.8, 1.2, 1.2, 1.0, dot=False)
        pg.set_z_index(1)
        self.add(pg)
        tgt = pg.copy().scale(3.6).move_to([-1.35, 1.15, 0])
        clab = T("commands", 40).next_to(tgt, DOWN, buff=0.35)
        self.play(pg.animate.shift(HOME.v(0, 0, 1.4)), run_time=0.4)
        pg.set_z_index(4)
        self.play(pg.animate.scale(3.6).move_to([-1.35, 1.15, 0]), run_time=0.7)
        self.play(FadeIn(clab), run_time=0.3)
        win = window(3.45, -0.35, 4.9, 4.4)
        self.play(FadeIn(win, shift=LEFT * 0.3), run_time=0.6)
        bar = pill(3.45, -1.95, 4.3, 0.72, "#ECE6DC")
        self.play(FadeIn(bar), run_time=0.3)
        until(self, "Type slash commit", lead=0.3)
        cmd = T("/commit", 40).move_to([1.65, -1.95, 0], aligned_edge=LEFT)
        self.play(AddTextLetterByLetter(cmd), run_time=0.6)
        until(self, "Claude follows", lead=0.4)
        self.play(pg.animate.scale(0.3).move_to([3.45, 0.3, 0]), run_time=0.5)
        self.play(FadeOut(pg), run_time=0.2)
        for y in (0.9, 0.25, -0.4):
            row = VGroup(Line([2.35, y, 0], [5.2, y, 0], color=GHOST, stroke_width=8), check(1.85, y + 0.02, 0.16, INK, 6))
            self.play(Create(row), run_time=0.28)
        done(self)


# ─────────────── B03: a sub-agent takes a task and reports back ───────────────
HELP = Iso(-1.55, -2.0, 0.85)


class B03_SubAgent(Scene):
    def construct(self):
        self.add(home_box())
        stack = VGroup(*[dpage(Iso(3.95, -1.75, 1.05), 0, 0, i * 0.16, 1.5, 1.7, dot=False) for i in range(3)])
        tlab = T("task", 40).move_to([4.15, -2.6, 0])
        self.play(FadeIn(stack, shift=LEFT * 0.3), FadeIn(tlab), run_time=0.6)
        cr = crate(HELP, 0, 0, 0, 1.2, 1.2, 1.0)
        home_pos = cr.get_center()
        cr.scale(HOME.s / HELP.s).move_to(HOME.p(0.85, 2.0, 1.2))
        cr.set_z_index(1)
        self.add(cr)
        self.play(cr.animate.shift(HOME.v(0, 0, 2.0)), run_time=0.5)
        cr.set_z_index(4)
        self.play(cr.animate.scale(HELP.s / HOME.s).move_to(home_pos), run_time=0.7)
        slab = T("sub-agent", 40).next_to(cr, DOWN, buff=0.3)
        self.play(FadeIn(slab), run_time=0.3)
        until(self, "Claude hands one", lead=0.3)
        rt = guard(self, 0.9)
        rider = VGroup(cr, slab)
        away = home_pos + np.array([2.55, 0.0, 0])
        self.play(MoveAlongPath(rider, ArcBetweenPoints(rider.get_center(), rider.get_center() + (away - home_pos), angle=-TAU / 6)), run_time=rt)
        until(self, "It works through it", lead=0.3)
        for i in (2, 1, 0):
            self.play(stack[i].animate.move_to(cr.get_top() + np.array([0, -0.1, 0])).scale(0.4), run_time=0.3)
            self.remove(stack[i])
        self.play(FadeOut(tlab), run_time=0.2)
        rep = VGroup(Rectangle(width=0.8, height=0.55, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=DIM, stroke_width=2),
                     Line([-0.25, 0.08, 0], [0.25, 0.08, 0], color=INK, stroke_width=5),
                     Line([-0.25, -0.1, 0], [0.12, -0.1, 0], color=INK, stroke_width=5)).next_to(cr, UP, buff=0.05)
        rep.set_z_index(5)
        self.play(GrowFromCenter(rep), run_time=0.3)
        until(self, "then reports back", lead=0.4)
        rider.add(rep)
        self.play(MoveAlongPath(rider, ArcBetweenPoints(rider.get_center(), rider.get_center() - (away - home_pos), angle=-TAU / 6)), run_time=0.8)
        done(self)


# ─────────────── B04: skills, opened when the task matches ───────────────
class B04_Skills(Scene):
    def construct(self):
        self.add(home_box())
        spots = [np.array([-1.5, 1.3, 0]), np.array([1.3, 1.85, 0]), np.array([4.1, 1.3, 0])]
        pages = VGroup(*[dpage(HOME, 0.9 + 0.35 * i, 0.6, 1.3, 1.2, 1.0) for i in range(3)])
        pages.set_z_index(1)
        self.add(pages)
        self.play(pages.animate.shift(HOME.v(0, 0, 1.5)), run_time=0.5)
        pages.set_z_index(4)
        self.play(*[p.animate.scale(2.9).move_to(s) for p, s in zip(pages, spots)], run_time=0.9)
        slab = T("skills", 40).move_to([1.3, 0.25, 0])
        self.play(FadeIn(slab), run_time=0.3)
        until(self, "Claude reads each", lead=0.3)
        for p in pages:
            self.play(p[1][2].animate.set_color(INK), run_time=0.3)
        until(self, "opens one when", lead=0.6)
        task = VGroup(Rectangle(width=2.0, height=1.2, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=DIM, stroke_width=3),
                      Line([-0.65, 0.2, 0], [0.65, 0.2, 0], color=INK, stroke_width=6),
                      Line([-0.65, -0.15, 0], [0.3, -0.15, 0], color=INK, stroke_width=6)).move_to([4.7, -1.55, 0])
        tl = T("task", 40).move_to([4.7, -2.6, 0])
        task.shift(RIGHT * 3); self.add(task)
        self.play(task.animate.shift(LEFT * 3), FadeIn(tl), run_time=0.5)
        link = DashedLine(task.get_top() + np.array([-0.3, 0.05, 0]), pages[2].get_bottom() + np.array([0, -0.1, 0]),
                          color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(link), pages[2].animate.shift(UP * 0.3), pages[0].animate.set_opacity(0.4),
                  pages[1].animate.set_opacity(0.4), run_time=0.6)
        done(self)


# ─────────────── B05: hooks fire on events ───────────────
BELT = Iso(-2.1, -2.95, 0.62)
BL, BWD, GX = 12.0, 1.6, 7.0


class B05_Hooks(Scene):
    def construct(self):
        self.add(home_box())
        belt = BELT.quad([(0, 0, 0), (BL, 0, 0), (BL, BWD, 0), (0, BWD, 0)], "#E6DFD3", stroke=DIM, sw=2)
        mid = DashedLine(BELT.p(0.3, BWD / 2, 0), BELT.p(BL - 0.3, BWD / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
        backp = VGroup(Line(BELT.p(GX, BWD + 0.1, 0), BELT.p(GX, BWD + 0.1, 2.6), color=INK, stroke_width=9),
                       Line(BELT.p(GX, BWD + 0.1, 2.6), BELT.p(GX, -0.1, 2.6), color=INK, stroke_width=9))
        hook = Arc(radius=0.2, start_angle=PI, angle=PI, color=INK, stroke_width=7).move_to(BELT.p(GX, BWD / 2, 1.95))
        hk = VGroup(Line(BELT.p(GX, BWD / 2, 2.6), BELT.p(GX, BWD / 2, 2.1), color=INK, stroke_width=7), hook)
        frontp = Line(BELT.p(GX, -0.1, 0), BELT.p(GX, -0.1, 2.6), color=INK, stroke_width=9)
        light = Dot(BELT.p(GX, -0.1, 2.6), radius=0.12, color=GHOST)
        backp.set_z_index(0); hk.set_z_index(0); frontp.set_z_index(3); light.set_z_index(4)
        self.play(FadeIn(belt), Create(mid), run_time=0.6)
        self.play(Create(backp), Create(frontp), Create(hk), FadeIn(light), run_time=0.7)
        hlab = T("hook", 40).move_to(BELT.p(GX, -0.1, 2.6) + np.array([0.9, 0.35, 0]))
        self.play(FadeIn(hlab), run_time=0.3)
        S = Iso(4.2, -2.55, 0.62)
        stack, lights = S.server(0, 0, 0, 1.4, 1.4, 0.4, n=2)
        stack.set_z_index(1); lights.set_z_index(2)
        self.play(FadeIn(stack, shift=UP * 0.3), FadeIn(lights), run_time=0.5)
        clab = T("command", 40).next_to(stack, DOWN, buff=0.25)
        elab = T("on edit", 40).move_to([-1.0, -3.02, 0])
        self.play(FadeIn(clab), FadeIn(elab), run_time=0.3)

        def event(kind):
            if kind == "edit":
                m = VGroup(BELT.box(0.4, 0.3, 0.02, 1.2, 1.0, 0.14, PAGE_TOP, PAGE_L, PAGE_R, sw=2))
                for f in m[0]:
                    f.set_stroke(DIM, 2)
            else:
                m = BELT.box(0.5, 0.35, 0.02, 0.9, 0.9, 0.8, KRAFT_SIDE, BOX_L, BOX_R, sw=3)
            m.set_z_index(2)
            return m

        def ride(kind):
            rt = guard(self, 1.3)
            ev = event(kind)
            self.add(ev)
            self.play(ev.animate.shift(BELT.v(GX - 1.0, 0, 0)), run_time=rt * 0.55, rate_func=linear)
            self.play(light.animate.set_color(TERRA), *[l.animate.set_color(TERRA) for l in lights],
                      ev.animate.shift(BELT.v(0.6, 0, 0)), run_time=0.3, rate_func=linear)
            self.play(ev.animate.shift(BELT.v(BL - GX - 1.0, 0, 0)), light.animate.set_color(GHOST),
                      *[l.animate.set_color(GHOST) for l in lights], run_time=rt * 0.45, rate_func=linear)
            self.remove(ev)

        until(self, "when Claude edits", lead=0.5)
        ride("edit")
        until(self, "or finishes a turn", lead=0.3)
        ride("stop")
        until(self, "to check each edit", lead=0.8)
        ride("edit")
        until(self, "That's a real program", lead=0.2)
        self.play(*[l.animate.set_color(TERRA) for l in lights], Indicate(stack, color=None, scale_factor=1.05), run_time=0.7)
        done(self)


# ─────────────── B06: MCP servers reach outside ───────────────
BIG = Iso(-1.2, -1.75, 1.0)


class B06_MCP(Scene):
    def construct(self):
        self.add(home_box())
        blk = BIG.mcp(0, 0, 0, 1.7, 1.7, 0.9)
        final = blk.get_center()
        blk.scale(HOME.s / BIG.s).move_to(HOME.p(2.2, 2.15, 1.3))
        blk.set_z_index(1)
        self.add(blk)
        self.play(blk.animate.shift(HOME.v(0, 0, 1.6)), run_time=0.4)
        blk.set_z_index(4)
        self.play(blk.animate.scale(BIG.s / HOME.s).move_to(final), run_time=0.7)
        mlab = T("MCP", 40).move_to([final[0] - 0.1, -2.6, 0])
        self.play(FadeIn(mlab), run_time=0.3)
        until(self, "They plug Claude", lead=0.4)
        S = Iso(3.5, -1.5, 1.0)
        stack, lights = S.server(0, 0, 0, 1.5, 1.5, 0.46)
        rt = guard(self, 0.5)
        stack.shift(RIGHT * 5); self.add(stack)
        self.play(stack.animate.shift(LEFT * 5), run_time=rt)
        start = BIG.p(1.7 * 0.58 + 0.15, -0.18, 0.9 * 0.45)
        end = S.p(0, 0.75, 0.7)
        cable = CubicBezier(start, start + np.array([1.2, -1.3, 0]), end + np.array([-1.3, -1.1, 0]), end, color=INK, stroke_width=5)
        self.play(Create(cable), run_time=1.0)
        until(self, "they start when", lead=0.3)
        self.add(lights)
        self.play(*[l.animate.set_color(TERRA) for l in lights], run_time=0.5)
        until(self, "GitHub's plugin", lead=0.3)
        glab = T("GitHub", 40).move_to([S.p(0.75, 0.75, 0)[0], -2.6, 0])
        self.play(FadeIn(glab), run_time=0.4)
        until(self, "your access token", lead=0.5)
        key = key_shape(0.9).move_to(start)
        key.set_z_index(6)
        self.play(GrowFromCenter(key), run_time=0.3)
        self.play(MoveAlongPath(key, cable), run_time=1.0)
        done(self)


# ─────────────── B07: only the parts it needs ───────────────
L7 = Iso(-3.3, -2.25, 0.62)
R7 = Iso(2.7, -2.25, 0.62)
RIM7 = 1.3


class B07_OnlyWhatItNeeds(Scene):
    def construct(self):
        boxes = VGroup()
        backs, fronts = [], []
        for iso in (L7, R7):
            back, front = iso.open_box(0, 0, 0, BW, BD, RIM7)
            y = -0.012
            card = VGroup(iso.quad([(0.85, y, 0.25), (2.35, y, 0.25), (2.35, y, 1.05), (0.85, y, 1.05)], PAGE_TOP, stroke=DIM, sw=2.5),
                          *[Line(iso.p(1.05, y, z), iso.p(2.15, y, z), color=GHOST, stroke_width=4) for z in (0.85, 0.65, 0.45)])
            card.set_z_index(3)
            boxes.add(VGroup(floor_shadow(iso), back, front, card))
        self.play(FadeIn(boxes[0], shift=UP * 0.2), FadeIn(boxes[1], shift=UP * 0.2), run_time=0.7)
        la = T("commit-commands", 40).move_to([L7.p(1.5, 0, 0)[0] - 0.9, -2.85, 0])
        lb = T("github", 40).move_to([R7.p(1.5, 0, 0)[0] - 0.9, -2.85, 0])
        self.play(FadeIn(la), FadeIn(lb), run_time=0.4)
        until(self, "three slash commands", lead=0.5)
        cards = VGroup()
        for xc in (0.8, 1.5, 2.2):
            c = VGroup(L7.quad([(xc, 0.55, 0.1), (xc, 2.45, 0.1), (xc, 2.45, 1.95), (xc, 0.55, 1.95)], PAGE_TOP, stroke=DIM, sw=2.5),
                       Line(L7.p(xc, 1.25, 1.45), L7.p(xc, 1.75, 1.8), color=INK, stroke_width=6))
            c.set_z_index(1)
            cards.add(c)
        rt = guard(self, 1.0)
        for c in cards:
            c.shift(UP * 3.0)
        self.add(cards)
        self.play(LaggedStart(*[c.animate.shift(DOWN * 3.0) for c in cards], lag_ratio=0.25), run_time=rt, rate_func=ease_in)
        until(self, "GitHub's is a label", lead=0.4)
        m = R7.mcp(0.9, 0.9, 0.0, 1.3, 1.3, 1.75)
        m.set_z_index(1)
        m.shift(UP * 3.0); self.add(m)
        self.play(m.animate.shift(DOWN * 3.0), run_time=0.6, rate_func=ease_in)
        until(self, "Nothing else", lead=0.2)
        self.play(Indicate(VGroup(boxes[0], cards), color=None, scale_factor=1.04),
                  Indicate(VGroup(boxes[1], m), color=None, scale_factor=1.04), run_time=0.7)
        done(self)


# ─────────────── B08: the marketplace, and trust it first ───────────────
SHF = Iso(-4.15, -2.55, 0.52)
LEVELS = (0.0, 1.55, 3.1)
SHELF_L, SHELF_D = 8.2, 1.7


class B08_Marketplace(Scene):
    def construct(self):
        frame = VGroup()
        for z in LEVELS:
            frame.add(SHF.box(0, 0, z - 0.15, SHELF_L, SHELF_D, 0.15, BOX_TOP, BOX_L, BOX_R, sw=3))
        posts = VGroup(SHF.box(-0.2, 0, -0.15, 0.2, SHELF_D, 4.2, BOX_TOP, BOX_L, BOX_R, sw=3),
                       SHF.box(SHELF_L, 0, -0.15, 0.2, SHELF_D, 4.2, BOX_TOP, BOX_L, BOX_R, sw=3))
        self.play(FadeIn(frame), FadeIn(posts), run_time=0.6)
        minis = []
        for z in LEVELS:
            row = VGroup(*[SHF.box(0.35 + i * 1.3, 0.3, z, 1.0, 1.0, 0.9) for i in range(6)])
            minis.append(row)
        self.play(LaggedStart(*[FadeIn(r, shift=DOWN * 0.2) for r in minis], lag_ratio=0.3), run_time=0.9)
        mk = T("marketplace", 40).move_to([-1.7, -3.0, 0])
        self.play(FadeIn(mk), run_time=0.3)
        until(self, "two hundred fifty-five", lead=0.4)
        v = ValueTracker(0)
        num = always_redraw(lambda: T(f"{int(round(v.get_value()))}", 150, INK, bold=True).move_to([4.1, 1.5, 0]))
        self.add(num)
        self.play(v.animate.set_value(255), run_time=1.3)
        self.play(FadeIn(T("per marketplace.json", 32).move_to([4.1, 0.3, 0])), run_time=0.4)
        until(self, "But the catalog", lead=0.3)
        pick = minis[0][2]
        rt = guard(self, 1.1)
        self.play(pick.animate.shift(SHF.v(0, -2.2, 0)), run_time=rt * 0.4)
        pick.set_z_index(5)
        self.play(pick.animate.scale(1.7).move_to([3.4, -1.55, 0]), run_time=rt * 0.6)
        until(self, "make sure you trust", lead=0.2)
        lens = VGroup(Circle(radius=0.62, color=INK, stroke_width=9).set_fill(CARD, opacity=0.25),
                      Line([0.44, -0.44, 0], [1.05, -1.05, 0], color=INK, stroke_width=14))
        lens.move_to([5.5, -0.95, 0]).set_z_index(6)
        tl = T("trust it first", 40).move_to([3.5, -2.9, 0])
        self.play(FadeIn(lens), FadeIn(tl), run_time=0.4)
        self.play(lens.animate.move_to(pick.get_center() + np.array([0.35, -0.3, 0])), run_time=0.8)
        until(self, "doesn't control", lead=0.3)
        self.play(lens.animate.shift(LEFT * 0.7 + UP * 0.25), run_time=0.6)
        self.play(lens.animate.shift(RIGHT * 0.7 + DOWN * 0.25), run_time=0.6)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Folder, B01_Label, B02_Commands, B03_SubAgent, B04_Skills, B05_Hooks, B06_MCP, B07_OnlyWhatItNeeds, B08_Marketplace):
    _cls.play = ST.play
