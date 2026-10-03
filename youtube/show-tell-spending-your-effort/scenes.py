"""
Manim scenes for show-tell-spending-your-effort (show-tell skill, card #9).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Thariq Shihipar's "Spending your effort" (claude.dev, Sep 25, 2026), drawn around one hero
object: a kraft effort DIAL lying on the stage in isometric (a knob on a round base, five
ticks: low, medium, high, xhigh, max). Every round thing in the film (dial, clocks) is the
same iso-circle ellipse. Terracotta only for the pointer's tip dot, the active-level marker
dot, server lights and a crate's light; every label is ink.
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



# ═════════════════════════════ the film: the effort dial ═════════════════════════════
# Cast: the kraft effort DIAL (knob on a round base, five ticks, ink pointer with a terracotta tip, a
# terracotta marker dot beside the active level's ink label); a dark SERVER stack (compute); iso CLOCK
# pucks; grey VERIFICATION / JUDGEMENT columns; the kraft FILTER box (html-js-filter); five TRY tiles;
# four step icons; one use icon per level; the four LOOP pills and the /effort chip.
SHADOW = "#BFB4A0"
KRAFT_SIDE = "#E8DCC6"
DIAL_EDGE = "#917A55"                 # outline of small dials (see dial())
DIAL_SHADOW = "#AFA28A"               # the dial's floor shadow, a step deeper than SHADOW (Gate V contrast on the hero dial)
LEVELS = ["low", "medium", "high", "xhigh", "max"]
ANG = {"low": 225.0, "medium": 157.5, "high": 90.0, "xhigh": 22.5, "max": -45.0}
EA, EB = 1.2247449, 0.7071068          # an iso circle of radius r projects to an ellipse EA*r wide, EB*r tall


def ep(c, r, a, dz=0.0):
    """Screen point at dial-angle a (degrees; 90 = away from the viewer) on an iso circle of radius r, lifted dz."""
    t = np.radians(a)
    return np.array([c[0] + EA * r * np.cos(t), c[1] + EB * r * np.sin(t) + dz, 0.0])


def iso_ellipse(c, r, dz, fill, sw=4, stroke=INK):
    return Polygon(*[ep(c, r, a, dz) for a in np.linspace(0, 360, 49)[:-1]], fill_color=fill, fill_opacity=1,
                   stroke_color=stroke, stroke_width=sw)


def cyl(c, r, z0, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4, stroke=INK):
    """An upright iso cylinder: left band, right band, the front outline, then the top face."""
    def band(a0, a1, fill):
        pts = [ep(c, r, a, z0) for a in np.linspace(a0, a1, 13)] + [ep(c, r, a, z0 + h) for a in np.linspace(a1, a0, 13)]
        return Polygon(*pts, fill_color=fill, fill_opacity=1, stroke_width=0)
    edge = VMobject(stroke_color=stroke, stroke_width=sw).set_points_as_corners(
        [ep(c, r, 180, z0 + h)] + [ep(c, r, a, z0) for a in np.linspace(180, 360, 25)] + [ep(c, r, 360, z0 + h)])
    return VGroup(band(180, 270, left), band(270, 360, right), edge, iso_ellipse(c, r, z0 + h, top, sw, stroke))


def pointer(c, R, a):
    """The knob's pointer: an ink line from the hub, a terracotta tip dot."""
    dz = 0.34 * R
    ln = Line(ep(c, 0.0, a, dz), ep(c, 0.5 * R, a, dz), color=INK, stroke_width=max(4.0, 5.5 * R))
    hub = Dot(ep(c, 0.0, a, dz), radius=max(0.04, 0.06 * R), color=INK)
    tip = Dot(ep(c, 0.5 * R, a, dz), radius=max(0.05, 0.07 * R), color=TERRA)
    g = VGroup(ln, hub, tip)
    g.set_z_index(3)
    return g


def place_lab(t, c, R, lvl, fac=1.8):
    a = ANG[lvl]
    p = ep(c, fac * R, a)
    cs = np.cos(np.radians(a))
    if cs > 0.3:
        t.move_to(p, aligned_edge=LEFT)
    elif cs < -0.3:
        t.move_to(p, aligned_edge=RIGHT)
    else:
        t.move_to(p + UP * (t.height / 2 + 0.08))
    return t


def marker_pt(lab):
    return lab.get_left() + LEFT * 0.28


def dial(c, R, level="medium", labels=True, lab=34, marker=True):
    """VGroup(body, labels, marker). body = (shadow, ticks, base, knob, pointer)."""
    c = np.array([c[0], c[1], 0.0])
    hb, hk, rk = 0.14 * R, 0.2 * R, 0.62 * R
    sh = iso_ellipse(c + np.array([0.14 * R, -0.12 * R, 0]), 1.06 * R, 0, DIAL_SHADOW, sw=0)
    sh.set_z_index(-1)
    # A small dial's ink outline + ticks fuse into one "text-run" blob that encloses the pointer (GATE T §8.6b
    # false overlap), so dials under R = 1 are outlined in DIAL_EDGE, a dark kraft that GATE T does not read as ink.
    edge = INK if R >= 1.0 else DIAL_EDGE
    ticks = VGroup(*[Line(ep(c, 1.08 * R, ANG[l]), ep(c, 1.5 * R, ANG[l]), color=edge, stroke_width=7) for l in LEVELS])
    base = cyl(c, R, 0, hb, BOX_L, BOX_IN1, BOX_IN2, stroke=edge)          # deeper kraft: Gate V contrast (B00 measured 0.29)
    knob = cyl(c, rk, hb, hk, BOX_TOP, BOX_R, BOX_IN1, stroke=edge)
    body = VGroup(sh, ticks, base, knob, pointer(c, R, ANG[level]))
    labs = VGroup(*[place_lab(T(l, lab), c, R, l) for l in LEVELS]) if labels else VGroup()
    mk = Dot(marker_pt(labs[LEVELS.index(level)]), radius=0.085, color=TERRA) if (labels and marker) else VGroup()
    g = VGroup(body, labs, mk)
    g.dc, g.dR, g.dth, g.dmk = c, R, ANG[level], bool(labels and marker)
    return g


def turn(self, D, level, rt=0.7, *extra):
    """Turn the knob to `level` (the pointer sweeps along the scale); the marker dot follows."""
    a0, a1 = D.dth, ANG[level]
    c, R = D.dc, D.dR
    ptr = D[0][4]

    def upd(m, a):
        m.become(pointer(c, R, a0 + (a1 - a0) * a))
    anims = [UpdateFromAlphaFunc(ptr, upd)]
    if D.dmk:
        anims.append(D[2].animate.move_to(marker_pt(D[1][LEVELS.index(level)])))
    self.play(*anims, *extra, run_time=rt)
    D.dth = a1


def morph(self, D, c, R, level, labels=True, lab=34, marker=True, rt=0.8, extra=()):
    """Move/scale the dial to a new place and size (same structure, so the body transforms cleanly)."""
    N = dial(c, R, level, labels, lab, marker)
    anims = [ReplacementTransform(D[0], N[0])]
    if len(D[1]) and len(N[1]):
        anims.append(ReplacementTransform(D[1], N[1]))
    elif len(D[1]):
        anims.append(FadeOut(D[1]))
    elif len(N[1]):
        anims.append(FadeIn(N[1]))
    if D.dmk and N.dmk:
        anims.append(ReplacementTransform(D[2], N[2]))
    elif D.dmk:
        anims.append(FadeOut(D[2]))
    elif N.dmk:
        anims.append(FadeIn(N[2]))
    self.play(*anims, *extra, run_time=rt)
    for m in (N[0], N[1], N[2]):
        self.remove(m)
    self.remove(D)
    self.add(N)
    return N


def fpage(center, s=0.6, w=1.4, d=1.1, z=0.0, dot=False):
    """A flat white page (DIM outline, two ghost lines) whose centre lands at `center`."""
    rig = Iso(0, 0, s)
    o = np.array(center) - rig.v(w / 2, d / 2, z)
    rig = Iso(o[0], o[1], s)
    slab = rig.box(0, 0, z, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    for f in slab:
        f.set_stroke(DIM, 2)
    zt = z + 0.06
    lines = VGroup(*[Line(rig.p(0.2, d * f, zt), rig.p(w - 0.2, d * f, zt), color=GHOST, stroke_width=4) for f in (0.35, 0.65)])
    g = VGroup(slab, lines)
    if dot:
        g.add(Dot(rig.p(0.22, d * 0.85, zt), radius=0.06, color=TERRA))
    g.rig = rig
    return g


def cross(x, y, s=0.17, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def tag(word, at, size=36, bold=False):
    """A white pill with one ink word (no outline: text inside an outline trips GATE T)."""
    t = T(word, size, INK, bold=bold)
    bg = RoundedRectangle(width=t.width + 0.6, height=t.height + 0.42, corner_radius=(t.height + 0.42) / 2,
                          fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
    g = VGroup(bg, t.move_to(bg.get_center()))
    g.move_to(at)
    return g


# ── clocks: an iso puck with a white face, a grey wedge for time spent, an ink hand ──
def wedge(c, r, sweep):
    dz = 0.18 * r
    sweep = max(2.0, min(360.0, sweep))
    pts = [ep(c, 0, 0, dz)] + [ep(c, 0.74 * r, 90 - s_, dz) for s_ in np.linspace(0, sweep, 41)]
    w = Polygon(*pts, fill_color=BAR2, fill_opacity=1, stroke_width=0)
    hand = Line(ep(c, 0, 0, dz), ep(c, 0.74 * r, 90 - sweep, dz), color=INK, stroke_width=6)
    return VGroup(w, hand)


def clock(c, r, sweep=2.0):
    """VGroup(puck, quarter dots, wedge+hand, pin)."""
    c = np.array([c[0], c[1], 0.0])
    dz = 0.18 * r
    sh = iso_ellipse(c + np.array([0.12 * r, -0.1 * r, 0]), 1.05 * r, 0, SHADOW, sw=0)
    sh.set_z_index(-1)
    puck = VGroup(sh, cyl(c, r, 0, dz, CARD, BOX_L, BOX_R))
    dots = VGroup(*[Dot(ep(c, 0.88 * r, a, dz), radius=max(0.04, 0.05 * r), color=BAR1) for a in (90, 0, -90, 180)])
    pin = Dot(ep(c, 0, 0, dz), radius=max(0.05, 0.06 * r), color=INK)
    g = VGroup(puck, dots, wedge(c, r, sweep), pin)
    g.cc, g.cr, g.sw_ = c, r, sweep
    return g


def sweep_to(C, deg):
    """An animation: clock C's wedge and hand sweep to `deg` degrees of the face."""
    a0 = C.sw_

    def upd(m, a):
        m.become(wedge(C.cc, C.cr, a0 + (deg - a0) * a))
    C.sw_ = deg
    return UpdateFromAlphaFunc(C[2], upd)


# ─────────────── B00: the dial ───────────────
HC, HR = (0.0, -0.6), 1.8          # the hero dial
LC, LR = (-1.9, -0.9), 1.15        # the dial stepped left, labels on


class B00_Dial(Scene):
    def construct(self):
        D = dial(HC, HR, "low", lab=36)
        D.dmk = False
        sh, ticks, base, knob, ptr = D[0]
        rig = VGroup(base, knob, ptr)
        rig.shift(DOWN * 4.5)
        self.add(rig)
        self.play(rig.animate.shift(UP * 4.5), run_time=0.8)
        self.play(FadeIn(sh), run_time=0.3)
        until(self, "Five settings", lead=0.35)
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.15), run_time=0.5)
        for l, ph in zip(LEVELS, ["low, medium", "medium, high", "high, x high", "x high, and", "and max"]):
            until(self, ph, lead=0.15)
            if l == "low":
                self.play(FadeIn(D[1][0], shift=UP * 0.1), run_time=0.25)
            else:
                turn(self, D, l, 0.3, FadeIn(D[1][LEVELS.index(l)], shift=UP * 0.1))
        until(self, "starts at medium", lead=0.3)
        mk = Dot(marker_pt(D[1][1]), radius=0.085, color=TERRA)
        turn(self, D, "medium", 0.8)
        self.play(FadeIn(mk, scale=0.4), run_time=0.3)
        until(self, "Most other models", lead=0.2)
        hi = Dot(marker_pt(D[1][2]), radius=0.085, color=DIM)
        self.play(FadeIn(hi, scale=0.4), Indicate(D[1][2], color=INK, scale_factor=1.12), run_time=0.5)
        done(self)


# ─────────────── B01: what is effort? compute ───────────────
SV = Iso(3.9, -2.4, 0.9)


def b00_end():
    D = dial(HC, HR, "medium", lab=36)
    hi = Dot(marker_pt(D[1][2]), radius=0.085, color=DIM)
    return D, hi


def server_rig(lit=False):
    stack, lights = SV.server(0, 0, 0, w=1.5, d=1.5, slab=0.42, n=4)
    if lit:
        lights.set_color(TERRA)
    return VGroup(stack, lights)


def cable(D):
    # kept clear of the dial and the server by a gap, so it never joins either into one GATE T blob
    a_ = ep(D.dc, D.dR, 0, 0.07 * D.dR) + RIGHT * 0.3
    t_ = SV.p(0, 0.75, 0.9)
    k = (2.45 - a_[0]) / (t_[0] - a_[0])          # stop at x = 2.45, clear of the server's dark faces (x >= 2.73)
    return Line(a_, a_ + (t_ - a_) * k, color=INK, stroke_width=5)


def compute_lab():
    return T("compute", 38).move_to([3.9, 1.3, 0])


class B01_Compute(Scene):
    def construct(self):
        D, hi = b00_end()
        self.add(D, hi)
        self.play(FadeOut(hi), run_time=0.3)
        D = morph(self, D, LC, LR, "medium", rt=0.8)
        until(self, "Thariq", lead=0.4)
        srv = server_rig()
        rt = guard(self, 0.7)
        srv.shift(RIGHT * 5)
        self.add(srv)
        self.play(srv.animate.shift(LEFT * 5), run_time=rt)
        self.play(FadeIn(compute_lab()), Create(cable(D)), run_time=0.5)
        until(self, "how much compute", lead=0.3)
        turn(self, D, "max", 1.4, LaggedStart(*[l.animate.set_color(TERRA) for l in srv[1]], lag_ratio=0.35))
        done(self)


# ─────────────── B02: two clocks ───────────────
SC, SR = (0.0, 2.0), 0.72        # the small dial, top centre
CLK1, CLK2, CRAD = (-3.3, -1.0), (3.3, -1.0), 1.15


def clock_labs():
    return VGroup(T("1 hour", 40).move_to([CLK1[0], -2.55, 0]), T("12 hours", 40).move_to([CLK2[0], -2.55, 0]))


def iterate_arc():
    a = Arc(radius=0.9, start_angle=-PI / 3, angle=5 * PI / 3, arc_center=np.array([-3.3, 1.15, 0]), color=INK, stroke_width=5)
    a.add_tip(tip_length=0.22, tip_width=0.22)
    return a


def big_stack(n=5):
    return VGroup(*[fpage([3.3, 0.55 + 0.14 * k, 0], s=0.6) for k in range(n)])


class B02_Clocks(Scene):
    def construct(self):
        D = dial(LC, LR, "max")
        srv = server_rig(lit=True)
        rest = VGroup(srv, cable(D), compute_lab())
        self.add(D, rest)
        self.play(FadeOut(rest, shift=RIGHT * 0.5), run_time=0.4)
        D = morph(self, D, SC, SR, "max", labels=False, rt=0.7)
        c1, c2 = clock(CLK1, CRAD), clock(CLK2, CRAD)
        labs = clock_labs()
        self.play(FadeIn(c1, shift=UP * 0.3), FadeIn(c2, shift=UP * 0.3), FadeIn(labs), run_time=0.5)
        until(self, "Given one hour", lead=0.3)
        turn(self, D, "low", 0.7, sweep_to(c1, 30))
        until(self, "the best version", lead=0.3)
        pg = fpage([-3.3, 1.15, 0], s=0.6)
        pg.shift(UP * 3)
        self.add(pg)
        self.play(pg.animate.shift(DOWN * 3), run_time=0.45, rate_func=ease_in)
        until(self, "expect to iterate", lead=0.3)
        self.play(Create(iterate_arc()), run_time=0.6)
        until(self, "Given twelve hours", lead=0.3)
        turn(self, D, "max", 1.2, sweep_to(c2, 360))
        until(self, "try very hard", lead=0.4)
        st = big_stack()
        for p_ in st:
            p_.shift(UP * 3.5)
        self.add(st)
        self.play(LaggedStart(*[p_.animate.shift(DOWN * 3.5) for p_ in st], lag_ratio=0.25), run_time=1.0)
        done(self)


# ─────────────── B03: verification and judgement ───────────────
CJ = Iso(2.8, -2.6, 0.8)


def slab(col, k):
    x0, y0 = [(0.0, 0.0), (1.7, -1.7)][col]
    tone = (BAR1, BAR2, BAR3)[k % 3]
    return CJ.box(x0, y0, k * 0.42, 1.1, 1.1, 0.34, tone, tone, tone, sw=3)


def cj_labs():
    return VGroup(T("verification", 36).move_to([2.8, -3.0, 0]), T("judgement", 36).move_to([5.16, -3.0, 0]))


def b02_end():
    D = dial(SC, SR, "max", labels=False)
    c1, c2 = clock(CLK1, CRAD, 30), clock(CLK2, CRAD, 360)
    return D, VGroup(c1, c2, clock_labs(), fpage([-3.3, 1.15, 0], s=0.6), iterate_arc(), big_stack())


class B03_CheckJudge(Scene):
    def construct(self):
        D, rest = b02_end()
        self.add(D, rest)
        self.play(FadeOut(rest, shift=DOWN * 0.4), run_time=0.45)
        D = morph(self, D, LC, LR, "low", rt=0.8)
        s0 = VGroup(slab(0, 0), slab(1, 0))
        self.play(GrowFromEdge(s0, DOWN), FadeIn(cj_labs()), run_time=0.5)
        until(self, "Claude always tries", lead=0.2)
        self.play(Indicate(s0, color=None, scale_factor=1.05), run_time=0.5)
        until(self, "higher effort", lead=0.3)
        for k, l in enumerate(LEVELS[1:], start=1):
            s = VGroup(slab(0, k), slab(1, k))
            rt = guard(self, 0.45)
            s.shift(UP * 2.5)
            self.add(s)
            turn(self, D, l, rt, s.animate.shift(DOWN * 2.5))
        done(self)


# ─────────────── B04: html-js-filter at low ───────────────
FB = Iso(3.4, -3.0, 0.8)
LOWC = dict(dial=(-5.1, 1.45), lab=(-3.45, 1.6), clock=(-2.0, 1.45), tiles_x=-5.9, num=(-1.55, 0.2))
HIC = dict(dial=(1.0, 1.45), lab=(2.85, 1.6), clock=(4.6, 1.45), tiles_x=0.4, num=(5.0, 0.2))
TILE_Y = 0.2


def fbox():
    sh = FB.quad([(0.25, -0.35, 0), (2.35, -0.35, 0), (2.35, 1.8, 0), (0.25, 1.8, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    body = FB.box(0, 0, 0, 2.0, 2.0, 1.6)
    slot = FB.quad([(0.55, 0.7, 1.6), (1.45, 0.7, 1.6), (1.45, 1.3, 1.6), (0.55, 1.3, 1.6)], DARK_TOP, sw=3)
    return VGroup(sh, body, slot)


def filter_lab():
    return T("html-js-filter", 38).move_to([1.35, 0.45, 0])


def slot_pt():
    return FB.p(1.0, 1.0, 1.6)


def script_page(center):
    """A page carrying a dark script block."""
    pg = fpage(center, s=0.55, w=1.3, d=1.0)
    blk = pg.rig.box(0.45, 0.3, 0.06, 0.45, 0.45, 0.35, DARK_TOP, DARK_L, DARK_R, sw=2)
    return VGroup(pg, blk)


def stripped():
    blk = Iso(5.15, 0.75, 0.55).box(0, 0, 0, 0.45, 0.45, 0.35, DARK_TOP, DARK_L, DARK_R, sw=2)
    X = cross(*(blk.get_center()[:2]), 0.42, INK, 8)
    return blk, X


def column(C, level, oks, sweep):
    """(dial, label, marker, clock, tiles, marks, number) for one run column."""
    d = dial(C["dial"], 0.58, level, labels=False)
    lab = T(level, 38).move_to([C["lab"][0], C["lab"][1], 0])
    mk = Dot(lab.get_right() + RIGHT * 0.28, radius=0.085, color=TERRA)
    clk = clock(C["clock"], 0.45, sweep)
    x0, s_, gap = C["tiles_x"], 0.52, 0.18
    tl = VGroup(*[Square(side_length=s_, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
                  .move_to([x0 + s_ / 2 + i * (s_ + gap), TILE_Y, 0]) for i in range(5)])
    mks = VGroup(*[(check(t.get_center()[0] - 0.03, t.get_center()[1] + 0.02, 0.12, INK, 6) if ok
                    else cross(t.get_center()[0], t.get_center()[1], 0.13, INK, 6)) for t, ok in zip(tl, oks)])
    num = T(f"{sum(oks)}/5", 64 if sum(oks) < 5 else 84, bold=True).move_to([C["num"][0], C["num"][1], 0])
    return d, lab, mk, clk, tl, mks, num


def test_page():
    pg = fpage([-3.9, -1.5, 0], s=0.6, w=1.3, d=1.0)
    ck = check(-3.75, -1.3, 0.14, INK, 6)
    ck.set_z_index(5)
    return VGroup(pg, ck)


def attribution():
    return T("per Anthropic's runs", 32).move_to([-3.9, -2.95, 0])


class B04_LowRun(Scene):
    def construct(self):
        D = dial(LC, LR, "max")
        cols = VGroup(*[slab(c, k) for k in range(5) for c in (0, 1)])
        self.add(D, cols, cj_labs())
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
        bx = fbox()
        bx.shift(RIGHT * 6)
        self.add(bx)
        self.play(bx.animate.shift(LEFT * 6), run_time=0.7)
        self.play(FadeIn(filter_lab()), run_time=0.35)
        until(self, "strips every way", lead=0.5)
        sp = script_page([5.4, 2.5, 0]).set_z_index(6)
        rt = guard(self, 0.8)
        self.add(sp)
        self.play(MoveAlongPath(sp, ArcBetweenPoints(sp.get_center(), slot_pt() + UP * 0.3, angle=-TAU / 8)), run_time=rt)
        self.play(sp.animate.scale(0.2).move_to(slot_pt()), run_time=0.3)
        self.remove(sp)
        blk, X = stripped()
        blk_start = blk.copy().scale(0.3).move_to(slot_pt())
        self.play(TransformFromCopy(blk_start, blk), run_time=0.5)
        self.play(Create(X), run_time=0.35)
        until(self, "In Anthropic's runs", lead=0.3)
        self.play(FadeIn(attribution()), run_time=0.3)
        until(self, "Fable five point one", lead=0.3)
        d, lab, mk, clk, tl, mks, num = column(LOWC, "low", [True, False, False, False, False], 2.0)
        self.play(FadeIn(VGroup(d, clk), shift=UP * 0.3), FadeIn(lab), FadeIn(mk, scale=0.4), run_time=0.5)
        until(self, "passed one of five", lead=0.3)
        self.play(FadeIn(tl), run_time=0.3)
        self.play(LaggedStart(*[Create(m) for m in mks], lag_ratio=0.2), FadeIn(num), run_time=0.7)
        until(self, "about two minutes", lead=0.3)
        self.play(sweep_to(clk, 12), run_time=0.4)
        until(self, "one pass", lead=0.3)
        pg = fpage([5.4, 2.5, 0], s=0.55, w=1.3, d=1.0).set_z_index(6)
        self.add(pg)
        self.play(MoveAlongPath(pg, ArcBetweenPoints(pg.get_center(), slot_pt() + UP * 0.3, angle=-TAU / 8)), run_time=0.5)
        self.play(pg.animate.scale(0.2).move_to(slot_pt()), run_time=0.2)
        self.remove(pg)
        until(self, "hand-written test page", lead=0.3)
        tp = test_page()
        tp.shift(UP * 0.5)
        self.play(FadeIn(tp, shift=DOWN * 0.5), run_time=0.35)
        done(self)


# ─────────────── B05: html-js-filter at xhigh ───────────────
STEP_XY = [(0.75, -1.2), (4.15, -1.2), (0.75, -2.5), (4.15, -2.5)]
STEP_LABS = ["self-review", "parser", "XSS suite", "fuzzer"]


def step_icon(i):
    x, y = STEP_XY[i]
    if i == 0:      # its own draft, ringed
        pg = Rectangle(width=0.62, height=0.78, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5).move_to([x - 0.05, y + 0.02, 0])
        ln = VGroup(*[Line([x - 0.26, y + 0.2 - 0.18 * k, 0], [x + 0.14, y + 0.2 - 0.18 * k, 0], color=GHOST, stroke_width=4) for k in range(3)])
        ring = Circle(radius=0.24, color=INK, stroke_width=6).move_to([x + 0.2, y - 0.2, 0])
        return VGroup(pg, ln, ring)
    if i == 1:      # the parser's source: a dark block
        return Iso(x - 0.05, y - 0.35, 0.42).mcp(0, 0, 0, 1.2, 1.2, 0.8)
    if i == 2:      # a test suite: stacked pages + a check
        pgs = VGroup(*[Rectangle(width=0.62, height=0.74, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
                       .move_to([x - 0.14 + 0.1 * k, y - 0.08 + 0.1 * k, 0]) for k in range(3)])
        return VGroup(pgs, check(x + 0.02, y + 0.1, 0.13, INK, 6))
    cubes = VGroup()  # a fuzzer: a spray of random kraft cubes
    for dx, dy in [(-0.35, 0.22), (-0.05, -0.2), (0.25, 0.26), (0.4, -0.15), (-0.3, -0.3), (0.08, 0.05)]:
        cubes.add(Iso(x + dx, y + dy - 0.1, 0.22).box(0, 0, 0, 0.6, 0.6, 0.6, sw=2))
    return cubes


def step_lab(i):
    x, y = STEP_XY[i]
    t = T(STEP_LABS[i], 34)
    return t.move_to([x + 0.62, y, 0], aligned_edge=LEFT)


def low_column_end():
    d, lab, mk, clk, tl, mks, num = column(LOWC, "low", [True, False, False, False, False], 12.0)
    return VGroup(d, lab, mk, clk, tl, mks, num, test_page(), attribution())


class B05_XhighRun(Scene):
    def construct(self):
        low = low_column_end()
        bx, fl = fbox(), filter_lab()
        blk, X = stripped()
        self.add(low, bx, fl, blk, X)
        self.play(FadeOut(VGroup(bx, fl, blk, X), shift=RIGHT * 0.6), run_time=0.5)
        d, lab, mk, clk, tl, mks, num = column(HIC, "xhigh", [True] * 5, 12.0)
        top = VGroup(d, clk)
        top.shift(RIGHT * 3)
        self.add(top)
        self.play(top.animate.shift(LEFT * 3), FadeIn(lab), FadeIn(mk, scale=0.4), run_time=0.6)
        until(self, "passed five of five", lead=0.3)
        self.play(FadeIn(tl), run_time=0.3)
        self.play(LaggedStart(*[Create(m) for m in mks], lag_ratio=0.2), FadeIn(num, scale=0.8), run_time=0.8)
        until(self, "thirty-three minutes", lead=0.4)
        self.play(sweep_to(clk, 198), run_time=1.1)
        for i, ph in enumerate(["It reviewed", "read the installed", "ran a standard", "wrote a random"]):
            until(self, ph, lead=0.2)
            ic = step_icon(i).set_z_index(4)
            rt = guard(self, 0.45)
            ic.shift(UP * 0.6)
            self.add(ic)
            self.play(ic.animate.shift(DOWN * 0.6), FadeIn(step_lab(i)), run_time=rt, rate_func=ease_in)
        done(self)


# ─────────────── B06 / B07: one use per level ───────────────
IC = np.array([4.1, -0.6, 0])      # the use icon's centre
ULAB_Y = -2.45


def use_lab(word):
    return T(word, 38).move_to([IC[0], ULAB_Y, 0])


def sketch_page():
    pg = fpage(IC + UP * 0.1, s=0.8, w=2.4, d=1.8)
    r = pg.rig
    pts = [r.p(0.4, 0.5, 0.07), r.p(0.8, 1.3, 0.07), r.p(1.15, 0.6, 0.07), r.p(1.5, 1.4, 0.07), r.p(1.8, 0.7, 0.07), r.p(2.1, 1.2, 0.07)]
    sq = VMobject(stroke_color=INK, stroke_width=6).set_points_smoothly(pts)
    sq.set_z_index(3)
    return pg, sq


CRT = Iso(4.1, -2.1, 0.7)


def crate():
    back, front = CRT.open_box(0, 0, 0, 2.0, 2.0, 1.2)
    sh = CRT.quad([(0.25, -0.35, 0), (2.35, -0.35, 0), (2.35, 1.8, 0), (0.25, 1.8, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return VGroup(sh, back, front)


def crate_parts():
    blk = CRT.mcp(0.3, 0.9, 0.0, 0.8, 0.8, 0.55)
    blk.set_z_index(1)
    pg = CRT.box(1.1, 0.3, 0.0, 0.7, 0.9, 0.5, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    for f in pg:
        f.set_stroke(DIM, 2)
    pg.set_z_index(1)
    return VGroup(blk, pg)


def bug_scene():
    pg = fpage(IC + UP * 0.1, s=0.8, w=2.4, d=1.8)
    bx, by = IC[0] - 0.2, IC[1] + 0.1
    legs = VGroup()
    for k in (-1, 0, 1):
        for sgn in (-1, 1):
            legs.add(Line([bx + 0.18 * k, by, 0], [bx + 0.18 * k + 0.12 * k, by + sgn * 0.36, 0], color=INK, stroke_width=4))
    body = Ellipse(width=0.62, height=0.42, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([bx, by, 0])
    head = Circle(radius=0.13, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([bx + 0.4, by, 0])
    ant = VGroup(Line([bx + 0.48, by + 0.06, 0], [bx + 0.66, by + 0.24, 0], color=INK, stroke_width=4),
                 Line([bx + 0.48, by - 0.06, 0], [bx + 0.66, by - 0.24, 0], color=INK, stroke_width=4))
    bug = VGroup(legs, body, head, ant)
    bug.set_z_index(3)
    return pg, bug


def lens():
    ring = Circle(radius=0.62, color=INK, stroke_width=9)
    handle = Polygon([0.42, -0.42, 0], [1.05, -1.05, 0], [0.92, -1.18, 0], [0.29, -0.55, 0], fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4)
    g = VGroup(handle, ring)
    g.set_z_index(4)
    return g


BL = Iso(3.68, -1.56, 0.6)
LOOP_PATH = [(0.35, 0.35), (3.65, 0.35), (3.65, 2.05), (0.35, 2.05)]


def loop_belt():
    outer = BL.quad([(0, 0, 0), (4, 0, 0), (4, 2.4, 0), (0, 2.4, 0)], BOX_L, stroke=INK, sw=3)
    inner = BL.quad([(0.8, 0.8, 0), (3.2, 0.8, 0), (3.2, 1.6, 0), (0.8, 1.6, 0)], STAGE, stroke=INK, sw=3)
    return VGroup(outer, inner)


def rover():
    c = BL.box(-0.05, -0.05, 0.02, 0.8, 0.8, 0.7)
    light = Dot(BL.p(0.35, -0.05, 0.42), radius=0.08, color=TERRA)
    g = VGroup(c, light)
    g.set_z_index(3)
    return g


def rover_path():
    lift = rover().get_center() - BL.p(0.35, 0.35, 0)
    pts = [BL.p(x, y, 0) + lift for x, y in LOOP_PATH + [LOOP_PATH[0]]]
    return VMobject().set_points_as_corners(pts)


class B06_LowMedium(Scene):
    def construct(self):
        low = low_column_end()
        d, lab, mk, clk, tl, mks, num = column(HIC, "xhigh", [True] * 5, 198.0)
        icons = VGroup(*[VGroup(step_icon(i), step_lab(i)) for i in range(4)])
        self.add(low, d, lab, mk, clk, tl, mks, num, icons)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
        D = dial(LC, LR, "medium")
        D.shift(LEFT * 5)
        self.add(D)
        self.play(D.animate.shift(RIGHT * 5), run_time=0.6)
        until(self, "Low for quick", lead=0.3)
        turn(self, D, "low", 0.6)
        until(self, "brainstorming", lead=0.4)
        pg, sq = sketch_page()
        l1 = use_lab("sketches")
        pg.shift(UP * 3)
        self.add(pg)
        self.play(pg.animate.shift(DOWN * 3), FadeIn(l1), run_time=0.45, rate_func=ease_in)
        self.play(Create(sq), run_time=0.7)
        until(self, "Medium for most", lead=0.3)
        cr = crate()
        l2 = use_lab("new features")
        rt = guard(self, 0.7)
        cr.shift(UP * 4)
        self.add(cr)
        turn(self, D, "medium", rt, FadeOut(VGroup(pg, sq), shift=RIGHT * 0.8), FadeOut(l1), FadeIn(l2),
             cr.animate.shift(DOWN * 4))
        until(self, "like new features", lead=0.4)
        parts = crate_parts()
        parts.shift(UP * 3)
        self.add(parts)
        self.play(LaggedStart(*[p_.animate.shift(DOWN * 3) for p_ in parts], lag_ratio=0.3), run_time=0.6, rate_func=ease_in)
        done(self)


class B07_HighMax(Scene):
    def construct(self):
        D = dial(LC, LR, "medium")
        cr, parts, l2 = crate(), crate_parts(), use_lab("new features")
        self.add(D, cr, parts, l2)
        pg, bug = bug_scene()
        l3 = use_lab("bug fixes")
        pg_bug = VGroup(pg, bug)
        pg_bug.shift(UP * 4)
        self.add(pg_bug)
        turn(self, D, "high", 0.6, FadeOut(VGroup(cr, parts), shift=RIGHT * 0.8), FadeOut(l2), FadeIn(l3),
             pg_bug.animate.shift(DOWN * 4))
        ln = lens().move_to(IC + np.array([2.0, 0.9, 0]))
        self.play(FadeIn(ln, shift=LEFT * 0.4), run_time=0.4)
        until(self, "like fixing a bug", lead=0.4)
        self.play(ln.animate.move_to(np.array([IC[0] - 0.1, IC[1] + 0.1, 0]) + np.array([0.33, -0.37, 0])), run_time=0.7)
        self.play(Indicate(bug, color=None, scale_factor=1.15), run_time=0.4)
        until(self, "Max when", lead=0.3)
        belt = loop_belt()
        rv = rover()
        l4 = use_lab("on its own")
        rt = guard(self, 0.7)
        belt.shift(UP * 4)
        rv.shift(UP * 4)
        self.add(belt, rv)
        turn(self, D, "max", rt, FadeOut(VGroup(pg_bug, ln), shift=RIGHT * 0.8), FadeOut(l3), FadeIn(l4),
             belt.animate.shift(DOWN * 4), rv.animate.shift(DOWN * 4))
        until(self, "fully on its own", lead=0.3)
        self.play(MoveAlongPath(rv, rover_path()), run_time=2.2, rate_func=linear)
        done(self)


# ─────────────── B08: the loop, and /effort ───────────────
MC, MR = (0.0, -0.15), 0.8
PILLS = [("interview", (-3.7, 2.1)), ("build on low", (3.7, 2.1)), ("review", (3.7, -1.9)), ("verify on high", (-3.7, -1.9))]


def pills():
    return VGroup(*[tag(w, [x, y, 0], 38) for w, (x, y) in PILLS])


def loop_arrows(P):
    a = []
    a.append(Arrow(P[0].get_right() + RIGHT * 0.3, P[1].get_left() + LEFT * 0.3, buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.06))
    a.append(Arrow(P[1].get_bottom() + DOWN * 0.3, P[2].get_top() + UP * 0.3, buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.08))
    a.append(Arrow(P[2].get_left() + LEFT * 0.3, P[3].get_right() + RIGHT * 0.3, buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.06))
    a.append(Arrow(P[3].get_top() + UP * 0.3, P[0].get_bottom() + DOWN * 0.3, buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.08))
    return VGroup(*a)


def pill_dot(P, i):
    """The active step's terracotta dot sits on the outer side of its pill (clear of the arrows)."""
    return P[i].get_right() + RIGHT * 0.32 if i in (1, 2) else P[i].get_left() + LEFT * 0.32


class B08_Loop(Scene):
    def construct(self):
        D = dial(LC, LR, "max")
        belt, rv, l4 = loop_belt(), rover(), use_lab("on its own")
        self.add(D, belt, rv, l4)
        self.play(FadeOut(VGroup(belt, rv, l4), shift=RIGHT * 0.6), run_time=0.4)
        D = morph(self, D, MC, MR, "low", labels=False, rt=0.7)
        P = pills()
        A = loop_arrows(P)
        self.play(LaggedStart(*[FadeIn(p_, scale=0.9) for p_ in P], lag_ratio=0.2), run_time=0.6)
        self.play(LaggedStart(*[GrowArrow(a_) for a_ in A], lag_ratio=0.2), run_time=0.6)
        until(self, "Have Claude interview", lead=0.3)
        dot = Dot(pill_dot(P, 0), radius=0.1, color=TERRA)
        self.play(FadeIn(dot, scale=0.4), Indicate(P[0], color=None, scale_factor=1.06), run_time=0.4)
        until(self, "Build it on low", lead=0.3)
        self.play(dot.animate.move_to(pill_dot(P, 1)), run_time=0.4)
        until(self, "Review it", lead=0.3)
        self.play(dot.animate.move_to(pill_dot(P, 2)), run_time=0.4)
        until(self, "Then verify", lead=0.3)
        turn(self, D, "high", 0.6, dot.animate.move_to(pill_dot(P, 3)))
        until(self, "slash effort", lead=0.4)
        ch = tag("/effort", [0, -2.8, 0], 40, bold=True)
        ch.shift(DOWN * 1.5)
        self.add(ch)
        self.play(ch.animate.shift(UP * 1.5), run_time=0.4)
        cu = cursor(1.6, -2.3)
        cu.set_z_index(8)
        self.play(FadeIn(cu), run_time=0.2)
        self.play(cu.animate.move_to(ch.get_right() + np.array([0.15, -0.2, 0])), run_time=0.45)
        self.play(Indicate(ch, color=None, scale_factor=1.08), run_time=0.3)
        turn(self, D, "low", 0.35)
        turn(self, D, "high", 0.35)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Dial, B01_Compute, B02_Clocks, B03_CheckJudge, B04_LowRun, B05_XhighRun, B06_LowMedium, B07_HighMax, B08_Loop):
    _cls.play = ST.play
