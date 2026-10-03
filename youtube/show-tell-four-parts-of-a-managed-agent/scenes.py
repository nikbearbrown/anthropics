"""
Manim scenes for show-tell-four-parts-of-a-managed-agent (show-tell skill, card #14, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The four core primitives of Claude Managed Agents (beta), from anthropics/launch-your-agent/cma-primitives.md,
checked against the live docs (platform.claude.com/docs/en/managed-agents/*, 2026-09-27): the AGENT is a white
blueprint card (model, prompt, tools, MCP, skills; a new card on each change = a new version); the ENVIRONMENT is an
open kraft crate (packages drop in; a fence with one gap to an allowed host); each SESSION is a closed crate on a pad
with a lamp (ghost = idle, terracotta = running), its own fresh copy; EVENTS are white cards riding a belt in
(user.message) and out (agent events); on idle a checkpoint photo is taken and a new message resumes it; sandbox
state lasts 30 days from creation (per Anthropic's docs), so outputs go to a tray.
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





# ═════════════════════════════ the film: four parts of a managed agent ═════════════════════════════
# Cast: the AGENT as a white BLUEPRINT card (a dark header band, ghost lines, five small part tiles); a new card on top
# for each version. The ENVIRONMENT as an open kraft CRATE (package cubes drop in) with a FENCE that has one gap, to a
# dark HOST block. Each SESSION as a closed kraft crate on a ghost pad with a grey lamp post (lamp ghost = idle,
# terracotta = running). EVENTS as white cards (terracotta dot) riding pale BELTS into and out of a session. A white
# CHECKPOINT photo card. A grey TIMELINE bar, a history stack, and a kraft OUTPUTS tray.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
BELT = "#E6DFD3"            # within Gate V's INK_DELTA of the stage, so it doesn't dilute the contrast average
PAD = "#E6E1D6"             # likewise
GREY_TOP, GREY_L, GREY_R = "#C9C4BA", "#A9A398", "#96907F"


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def pad(iso, x0, y0, w, d):
    q = iso.quad([(x0, y0, 0), (x0 + w, y0, 0), (x0 + w, y0 + d, 0), (x0, y0 + d, 0)], PAD, sw=0)
    return q.set_z_index(-3)


# ─── the AGENT: a blueprint card ───
BPW, BPD, BPH = 2.4, 1.8, 0.1
PART_TONES = [(DARK_TOP, DARK_L, DARK_R), (PAGE_TOP, PAGE_L, PAGE_R), (BOX_TOP, BOX_L, BOX_R),
              (GREY_TOP, GREY_L, GREY_R), (PAGE_TOP, PAGE_L, PAGE_R)]


def card_slab(iso, z=0.0):
    slab = iso.box(0, 0, z, BPW, BPD, BPH, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    zt = z + BPH
    band = iso.quad([(0.15, BPD - 0.45, zt), (BPW - 0.15, BPD - 0.45, zt), (BPW - 0.15, BPD - 0.15, zt), (0.15, BPD - 0.15, zt)],
                    BAR1, sw=0)     # grey, not dark: a dark band inside the ink card reads as overlapping text (GATE T bbox)
    lines = VGroup(*[Line(iso.p(0.25, y, zt), iso.p(BPW - 0.25, y, zt), color=GHOST, stroke_width=4) for y in (0.25, 1.1)])
    return VGroup(slab, band, lines)


def part(iso, k, z=BPH, tones=None):
    t = tones or PART_TONES[k]
    b = iso.box(0.2 + 0.44 * k, 0.5, z, 0.32, 0.32, 0.24, *t, sw=2)
    for f in b:
        f.set_stroke(DEV_EDGE, 2)
    return b


def blueprint(iso, z=0.0, tones=None):
    """(card, parts): the card and its five part tiles."""
    tones = tones or PART_TONES
    return VGroup(card_slab(iso, z), VGroup(*[part(iso, k, z + BPH, tones[k]) for k in range(5)]))


# ─── the ENVIRONMENT: an open kraft crate ───
CW, CD, CH = 2.0, 1.6, 1.1
PKG = [(0.25, 0.9, GREY_TOP, GREY_L, GREY_R), (1.1, 0.95, BOX_TOP, BOX_L, BOX_R), (0.3, 0.2, BOX_TOP, BOX_L, BOX_R),
       (1.15, 0.2, GREY_TOP, GREY_L, GREY_R)]


def crate(iso):
    """(shadow, back, front) of the open crate."""
    sh = iso.quad([(-0.2, -0.45, 0), (CW + 0.35, -0.45, 0), (CW + 0.35, CD, 0), (-0.2, CD, 0)], SHADOW, sw=0).set_z_index(-2)
    back, front = iso.open_box(0, 0, 0, CW, CD, CH)
    return VGroup(sh, back, front)


def pkg(iso, k):
    x, y, t, l, r = PKG[k]
    b = iso.box(x, y, 0.0, 0.6, 0.55, 0.55, t, l, r, sw=3)
    return b.set_z_index(1)


def env(iso, n=4):
    return VGroup(crate(iso), VGroup(*[pkg(iso, k) for k in range(n)]))


# ─── a SESSION: a closed crate on a pad, with a lamp post ───
SW_, SD_, SH_ = 1.6, 1.3, 1.0


def session(iso, lit=False):
    """(pad, box, post, lamp)."""
    pd = iso.quad([(-0.2, -0.45, 0), (SW_ + 0.35, -0.45, 0), (SW_ + 0.35, SD_, 0), (-0.2, SD_, 0)], SHADOW, sw=0).set_z_index(-3)
    bx = iso.box(0, 0, 0, SW_, SD_, SH_)
    bx.add(iso.quad([(0, 0.35, 0.1), (0, 0.95, 0.1), (0, 0.95, 0.5), (0, 0.35, 0.5)], DARK_R, sw=0),      # in-port (left face)
           iso.quad([(0.35, 0, 0.1), (0.95, 0, 0.1), (0.95, 0, 0.5), (0.35, 0, 0.5)], DARK_R, sw=0))      # out-port (right face)
    post = iso.box(SW_ - 0.45, SD_ - 0.45, SH_, 0.24, 0.24, 0.5, GREY_TOP, GREY_L, GREY_R, sw=2)
    lamp = Dot(iso.p(SW_ - 0.33, SD_ - 0.33, SH_ + 0.5) + UP * 0.09 * iso.s / 0.6, radius=0.14 * max(iso.s, 0.6) / 0.85,
               color=TERRA if lit else GHOST)
    bx.set_z_index(1); post.set_z_index(2); lamp.set_z_index(3)
    return VGroup(pd, bx, post, lamp)


def lamp_on(s, on=True):
    return s[3].animate.set_color(TERRA if on else GHOST)


# ─── EVENTS: belts and cards ───
def strip_x(iso, x0, x1, y0, y1, th=0.22):
    top = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], BELT, stroke=DEV_EDGE, sw=2)
    side = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y0, -th), (x0, y0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)
    end = iso.quad([(x0, y0, 0), (x0, y1, 0), (x0, y1, -th), (x0, y0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    ym = (y0 + y1) / 2
    mid = DashedLine(iso.p(x0 + 0.3, ym, 0), iso.p(x1 - 0.3, ym, 0), color=GHOST, stroke_width=3, dash_length=0.12)
    return VGroup(side, end, top, mid).set_z_index(-2)


def strip_y(iso, x0, x1, y0, y1, th=0.22):
    top = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], BELT, stroke=DEV_EDGE, sw=2)
    side = iso.quad([(x0, y0, 0), (x0, y1, 0), (x0, y1, -th), (x0, y0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    front = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y0, -th), (x0, y0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)
    xm = (x0 + x1) / 2
    mid = DashedLine(iso.p(xm, y0 + 0.3, 0), iso.p(xm, y1 - 0.3, 0), color=GHOST, stroke_width=3, dash_length=0.12)
    return VGroup(side, front, top, mid).set_z_index(-2)


def ecard(iso, x, y, z=0.02, fill=(PAGE_TOP, PAGE_L, PAGE_R), dot=True):
    """An event card lying on a belt: a white slab, DIM outline, one grey line, a terracotta dot."""
    slab = iso.box(x - 0.4, y - 0.3, z, 0.8, 0.6, 0.07, *fill, sw=2)
    for f in slab:
        f.set_stroke(DIM, 2)
    zt = z + 0.07
    ln = Line(iso.p(x - 0.05, y - 0.1, zt), iso.p(x + 0.3, y - 0.1, zt), color=BAR1, stroke_width=4)
    g = VGroup(slab, ln)
    if dot:
        g.add(Dot(iso.p(x - 0.22, y + 0.08, zt), radius=0.06 * max(iso.s, 0.6) / 0.8, color=TERRA))
    return g.set_z_index(4)


# ══════════════ B00: four parts on four pads ══════════════
AG0 = Iso(-4.55, -0.45, 0.72)
EN0 = Iso(-1.05, -0.8, 0.72)
SE0 = Iso(2.15, -0.65, 0.72)
EV_B0 = (0.35, 1.05, -3.3, -0.05)          # the belt on the session's rig: x range, y range (runs toward the viewer)


def b00_objs():
    ag = VGroup(pad(AG0, -0.3, -0.3, BPW + 0.6, BPD + 0.6), blueprint(AG0))
    en = VGroup(pad(EN0, -0.3, -0.3, CW + 0.6, CD + 0.6), env(EN0))
    se = session(SE0)
    ev = strip_y(SE0, EV_B0[0], EV_B0[1], EV_B0[2], EV_B0[3])
    return ag, en, se, ev


def l_beta():
    return VGroup(Dot([-0.75, 2.62, 0], radius=0.11, color=TERRA), T("beta", 44).move_to([0.05, 2.6, 0]))


ONCE_Y = -2.05


def once_mark():
    br = VGroup(Line([-5.9, ONCE_Y, 0], [0.45, ONCE_Y, 0], color=INK, stroke_width=5),
                Line([-5.9, ONCE_Y, 0], [-5.9, ONCE_Y + 0.3, 0], color=INK, stroke_width=5),
                Line([0.45, ONCE_Y, 0], [0.45, ONCE_Y + 0.3, 0], color=INK, stroke_width=5))
    return VGroup(br, T("once", 42).move_to([-2.72, ONCE_Y - 0.5, 0]))


def b00_state():
    ag, en, se, ev = b00_objs()
    return VGroup(ag, en, se, ev, l_beta(), once_mark())


class B00_FourParts(Scene):
    def construct(self):
        ag, en, se, ev = b00_objs()
        self.play(FadeIn(l_beta()), run_time=0.4)
        for obj, ph in ((ag, "The agent"), (en, "The environment"), (se, "The session"), (ev, "And events")):
            until(self, ph, lead=0.2)
            rt = guard(self, 0.5)
            self.play(FadeIn(obj, shift=DOWN * 1.2), run_time=rt, rate_func=ease_in)
        until(self, "the first two once", lead=0.3)
        om = once_mark()
        rt = guard(self, 0.5)
        self.play(Create(om[0]), FadeIn(om[1]), run_time=rt)
        until(self, "events are how", lead=0.3)
        a, z = EV_B0[0] + 0.35, (EV_B0[0] + EV_B0[1]) / 2
        c = ecard(SE0, z, EV_B0[2] + 0.5)
        self.add(c)
        rt = guard(self, 1.0)
        self.play(c.animate.shift(SE0.v(0, EV_B0[3] - EV_B0[2] - 0.8, 0)), run_time=rt, rate_func=linear)
        self.play(lamp_on(se), FadeOut(c), run_time=0.3)
        done(self)


# ══════════════ B01: the blueprint ══════════════
AG1 = Iso(-0.75, -1.55, 1.25)
V_LAB = np.array([3.45, 0.55, 0])
BACK = (0.55, 0.55, 0.0)                   # v1 slides back by this rig vector (straight up on screen)


def l_agent1():
    return T("agent", 42).move_to([-3.7, -1.75, 0])


def id_tag(iso=AG1):
    a = iso.p(BPW, 0.25, BPH)
    c = a + np.array([0.85, -0.85, 0])
    string = Line(a + np.array([0.08, -0.06, 0]), c + np.array([-0.2, 0.2, 0]), color=DIM, stroke_width=4)
    tag = RoundedRectangle(width=0.75, height=0.5, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1,
                           stroke_color=INK, stroke_width=4).move_to(c + np.array([0.12, -0.08, 0])).rotate(-0.5)
    hole = Dot(tag.get_center() + np.array([-0.2, 0.1, 0]), radius=0.06, color=TERRA)
    return VGroup(string, tag, hole).set_z_index(6)


NEW_TONES = [PART_TONES[0], PART_TONES[1], (GREY_TOP, GREY_L, GREY_R), PART_TONES[3], PART_TONES[4]]


class B01_Blueprint(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        ag = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3], st[4], st[5], ag[0])), run_time=0.45)
        bp = ag[1]
        parts = bp[1]
        self.play(to_rig(bp, AG0, AG1), FadeOut(parts), run_time=0.7)
        self.play(FadeIn(l_agent1()), run_time=0.3)
        bp.remove(parts)
        new_parts = VGroup(*[part(AG1, k) for k in range(5)])
        for k, ph in enumerate(["the model", "a system prompt", "tools", "MCP servers", "skills"]):
            until(self, ph, lead=0.15)
            p = new_parts[k]
            rt = guard(self, 0.35)
            self.play(FadeIn(p, shift=DOWN * 1.0), run_time=rt, rate_func=ease_in)
        until(self, "reuse it by its ID", lead=0.3)
        tg = id_tag()
        rt = guard(self, 0.45)
        self.play(GrowFromPoint(tg, AG1.p(BPW, 0.25, BPH)), run_time=rt)
        v1 = T("v1", 44, INK, bold=True).move_to(V_LAB)
        self.play(FadeIn(v1), run_time=0.3)
        until(self, "Change it", lead=0.2)
        old_tile = new_parts[2]
        rt = guard(self, 0.4)
        self.play(old_tile.animate.shift(UP * 0.5).set_opacity(0), run_time=rt)
        until(self, "you get a new version", lead=0.3)
        v1grp = VGroup(bp[0], *[new_parts[k] for k in (0, 1, 3, 4)], tg)
        rt = guard(self, 0.6)
        self.play(v1grp.animate.shift(AG1.v(*BACK)), run_time=rt)
        v2 = blueprint(AG1, tones=NEW_TONES)
        v2.set_z_index(5)
        for m in v2.get_family():
            m.set_z_index(5)
        until(self, "Version one becomes", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(v2, shift=DOWN * 1.2), FadeOut(v1), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(T("v2", 44, INK, bold=True).move_to(V_LAB)), run_time=0.3)
        until(self, "stays in the history", lead=0.3)
        rt = guard(self, 0.35)
        self.play(FadeIn(T("history", 42).move_to([2.45, 2.35, 0])), run_time=rt)
        done(self)


def b01_state():
    old = VGroup(card_slab(AG1), *[part(AG1, k) for k in (0, 1, 3, 4)], id_tag()).shift(AG1.v(*BACK))
    v2 = blueprint(AG1, tones=NEW_TONES)
    for m in v2.get_family():
        m.set_z_index(5)
    labs = VGroup(l_agent1(), T("v2", 44, INK, bold=True).move_to(V_LAB), T("history", 42).move_to([2.45, 2.35, 0]))
    return old, v2, labs


# ══════════════ B02: the environment ══════════════
AG2 = Iso(-5.15, 1.5, 0.45)
EN2 = Iso(-2.0, -2.3, 1.1)
FX = 3.6                                   # the fence runs along y at x = FX (on EN2)
FY0, FY1, GAP = -1.45, 2.05, (0.3, 1.1)
HOST = (5.0, 0.3)


def fence(iso=EN2):
    ys = [y for y in np.arange(FY0, FY1 + 0.01, 0.35) if not (GAP[0] - 0.05 < y < GAP[1] + 0.05)]
    posts = VGroup(*[Line(iso.p(FX, y, 0), iso.p(FX, y, 1.0), color=INK, stroke_width=6) for y in ys])
    rails = VGroup(*[Line(iso.p(FX, a, z), iso.p(FX, b, z), color=INK, stroke_width=5)
                     for z in (0.35, 0.8) for a, b in ((FY0, ys[[i for i, y in enumerate(ys) if y < GAP[0]][-1]]),
                                                       (ys[[i for i, y in enumerate(ys) if y > GAP[1]][0]], FY1))])
    return VGroup(posts, rails).set_z_index(3)


def host(iso=EN2):
    b = iso.box(HOST[0], HOST[1], 0, 0.7, 0.7, 0.6, DARK_TOP, DARK_L, DARK_R)
    return b.set_z_index(3)


def net_line(iso=EN2):
    a = iso.p(CW * 0.55, CD * 0.55, CH + 0.1)
    z = iso.p(HOST[0] - 0.3, HOST[1] + 0.35, 0.45)
    return DashedLine(a, z, color=INK, stroke_width=5, dash_length=0.14).set_z_index(4)


def l_env():
    return T("environment", 42).move_to([-3.85, -2.75, 0])


def l_host():
    return T("allowed host", 42).move_to([4.45, -1.75, 0])


class B02_Environment(Scene):
    def construct(self):
        old, v2, labs = b01_state()
        self.add(old, v2, labs)
        self.play(FadeOut(old), FadeOut(labs), run_time=0.4)
        self.play(to_rig(v2, AG1, AG2), run_time=0.6)
        until(self, "where sessions run", lead=0.3)
        cr = crate(EN2)
        cr.shift(LEFT * 9)
        self.add(cr)
        rt = guard(self, 0.7)
        self.play(cr.animate.shift(RIGHT * 9), run_time=rt)
        self.play(FadeIn(l_env()), run_time=0.3)
        until(self, "or a self-hosted one", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(cr, color=None, scale_factor=1.05), run_time=rt)
        until(self, "packages to install", lead=0.3)
        pk = [pkg(EN2, k) for k in range(4)]
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 1.2) for p in pk], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        until(self, "which hosts the network", lead=0.3)
        fc = fence()
        rt = guard(self, 0.6)
        self.play(Create(fc, lag_ratio=0.1), run_time=rt)
        hs = host()
        self.play(FadeIn(hs, shift=DOWN * 1.0), run_time=0.45, rate_func=ease_in)
        self.play(Create(net_line()), FadeIn(l_host()), run_time=0.5)
        done(self)


def b02_state():
    return VGroup(blueprint(AG2), env(EN2), fence(), host(), net_line(), l_env(), l_host())


# ══════════════ B03: sessions ══════════════
AG3 = Iso(-5.35, 1.35, 0.42)
EN3 = Iso(-4.75, -1.85, 0.52)
SE3 = [Iso(0.35, -1.25, 0.8), Iso(3.55, -2.45, 0.8)]


def thread(a, z):
    return DashedLine(a, z, color=INK, stroke_width=4, dash_length=0.12).set_z_index(-1)


def threads(k=0):
    s = SE3[k]
    tgt = s.p(-0.05, SD_ * 0.6, SH_ * 0.6)
    return VGroup(thread(AG3.p(BPW, BPD * 0.5, BPH) + RIGHT * 0.15, tgt + LEFT * 0.1 + UP * 0.1),
                  thread(EN3.p(CW, CD * 0.3, CH * 0.6) + RIGHT * 0.15, tgt + LEFT * 0.12 + DOWN * 0.1))


def l_session():
    return T("session", 42).move_to([0.0, 2.45, 0])


def l_idle():
    return T("idle", 42).move_to([5.25, 0.55, 0])


class B03_Session(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        bp, en = st[0], st[1]
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5], st[6])), run_time=0.4)
        self.play(to_rig(bp, AG2, AG3), to_rig(en, EN2, EN3), run_time=0.7)
        until(self, "A session is one run", lead=0.3)
        s0 = session(SE3[0])
        src = EN3.p(CW / 2, CD / 2, CH / 2)
        s0.scale(0.3).move_to(src).set_opacity(1)
        tgt0 = session(SE3[0])
        rt = guard(self, 0.8)
        self.play(Transform(s0, tgt0), run_time=rt)
        self.play(FadeIn(l_session()), run_time=0.3)
        until(self, "It names an agent", lead=0.3)
        th = threads(0)
        rt = guard(self, 0.7)
        self.play(Create(th[0]), Create(th[1]), run_time=rt)
        until(self, "Two sessions", lead=0.4)
        s1 = session(SE3[1])
        s1.scale(0.3).move_to(src)
        rt = guard(self, 0.8)
        self.play(Transform(s1, session(SE3[1])), FadeOut(th), run_time=rt)
        until(self, "no shared files", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(s0[1], s1[1]), color=None, scale_factor=1.06), run_time=rt)
        until(self, "it starts idle", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_idle()), Flash(s1[3].get_center(), color=DIM, line_length=0.18, flash_radius=0.3), run_time=rt)
        done(self)


def b03_state():
    return VGroup(blueprint(AG3), env(EN3), session(SE3[0]), session(SE3[1]), l_session(), l_idle())


# ══════════════ B04: events ══════════════
SE4 = Iso(0.45, -1.3, 1.15)
IN_B = (-2.9, -0.05, 0.3, 1.0)             # in-belt on SE4: x range, y range (runs along x into the left face)
OUT_B = (0.3, 1.0, -2.55, -0.05)           # out-belt on SE4: x range, y range (runs toward the viewer from the right face)


def in_belt():
    return strip_x(SE4, IN_B[0], IN_B[1], IN_B[2], IN_B[3])


def out_belt():
    return strip_y(SE4, OUT_B[0], OUT_B[1], OUT_B[2], OUT_B[3])


def in_card(fill=(PAGE_TOP, PAGE_L, PAGE_R), dot=True):
    return ecard(SE4, IN_B[0] + 0.55, (IN_B[2] + IN_B[3]) / 2, fill=fill, dot=dot)


IN_RIDE = SE4.v(IN_B[1] - IN_B[0] - 0.75, 0, 0)
OUT_Y0 = OUT_B[3] - 0.45


def out_card():
    return ecard(SE4, (OUT_B[0] + OUT_B[1]) / 2, OUT_Y0)


def l_user():
    return T("user.message", 42).move_to([-3.35, -1.2, 0])


def l_running():
    return T("running", 42).move_to([2.15, 2.6, 0])


def l_agentev():
    return T("agent events", 42).move_to([4.6, -1.35, 0])


class B04_Events(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        s0 = st[2]
        self.play(FadeOut(VGroup(st[0], st[1], st[3], st[4], st[5])), run_time=0.45)
        self.play(to_rig(s0, SE3[0], SE4), run_time=0.7)
        until(self, "how you talk to it", lead=0.3)
        ib = in_belt()
        rt = guard(self, 0.5)
        self.play(FadeIn(ib, shift=RIGHT * 0.4), run_time=rt)
        until(self, "You send a user", lead=0.3)
        c = in_card()
        rt = guard(self, 0.3)
        self.play(FadeIn(c), FadeIn(l_user()), run_time=rt)
        rt = guard(self, 1.0)
        self.play(c.animate.shift(IN_RIDE), run_time=rt, rate_func=linear)
        self.play(FadeOut(c), lamp_on(s0), run_time=0.3)
        until(self, "switches to running", lead=0.2)
        lr = l_running()
        rt = guard(self, 0.35)
        self.play(FadeIn(lr), Flash(s0[3].get_center(), color=TERRA, line_length=0.18, flash_radius=0.32), run_time=rt)
        until(self, "Tool calls", lead=0.4)
        ob = out_belt()
        rt = guard(self, 0.4)
        self.play(FadeIn(ob), run_time=rt)
        outs = [out_card() for _ in range(3)]
        rides = []
        for oc in outs:
            self.add(oc)
        rt = guard(self, 1.5)
        self.play(LaggedStart(*[oc.animate.shift(SE4.v(0, OUT_B[2] - OUT_Y0 + 0.45, 0)) for oc in outs], lag_ratio=0.3),
                  run_time=rt, rate_func=linear)
        self.play(FadeIn(l_agentev()), *[FadeOut(oc) for oc in outs[:2]], run_time=0.35)
        until(self, "another message steers", lead=0.3)
        c2 = in_card()
        self.add(c2)
        rt = guard(self, 0.8)
        self.play(c2.animate.shift(IN_RIDE), run_time=rt, rate_func=linear)
        self.play(FadeOut(c2), run_time=0.2)
        until(self, "an interrupt stops it", lead=0.35)
        c3 = in_card(fill=(BOX_TOP, BOX_L, BOX_R), dot=False)
        self.add(c3)
        rt = guard(self, 0.7)
        self.play(c3.animate.shift(IN_RIDE), run_time=rt, rate_func=linear)
        self.play(FadeOut(c3), lamp_on(s0, False), FadeOut(lr), run_time=0.3)
        done(self)


def last_out_card():
    return out_card().shift(SE4.v(0, OUT_B[2] - OUT_Y0 + 0.45, 0))


def b04_state():
    return VGroup(session(SE4), in_belt(), out_belt(), l_user(), l_agentev(), last_out_card())


# ══════════════ B05: idle, checkpoint, resume ══════════════
PH_C = np.array([-3.35, 1.55, 0])


def photo(c=PH_C, s=1.0):
    c = np.array(c, dtype=float)
    card = RoundedRectangle(width=1.5 * s, height=1.25 * s, corner_radius=0.08 * s, fill_color=PAGE_TOP, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to(c)
    mini = Iso(c[0] - 0.12 * s, c[1] - 0.42 * s, 0.34 * s)
    m = mini.box(0, 0, 0, SW_, SD_, SH_, sw=2)
    for f in m:
        f.set_stroke(DEV_EDGE, 2)
    return VGroup(card, m).set_z_index(7)


def l_idle5():
    return T("idle", 42).move_to([2.15, 2.6, 0])


def l_ckpt():
    return T("checkpoint", 42).move_to(PH_C + DOWN * 1.15)


class B05_Checkpoint(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        s0 = st[0]
        self.play(FadeOut(VGroup(st[3], st[4], st[5])), run_time=0.4)
        until(self, "When a turn ends", lead=0.3)
        li = l_idle5()
        rt = guard(self, 0.4)
        self.play(FadeIn(li), Flash(s0[3].get_center(), color=DIM, line_length=0.18, flash_radius=0.32), run_time=rt)
        until(self, "sandbox is checkpointed", lead=0.3)
        src = SE4.p(SW_ * 0.2, SD_ * 0.9, SH_)
        ph = photo()
        rt = guard(self, 0.6)
        self.play(Flash(src, color=DIM, line_length=0.3, flash_radius=0.5), GrowFromPoint(ph, src), run_time=rt)
        lc = l_ckpt()
        self.play(FadeIn(lc), run_time=0.3)
        until(self, "Send another user message", lead=0.3)
        c = in_card()
        self.add(c)
        rt = guard(self, 1.0)
        self.play(c.animate.shift(IN_RIDE), run_time=rt, rate_func=linear)
        self.play(FadeOut(c), run_time=0.2)
        until(self, "picks up from there", lead=0.3)
        rt = guard(self, 0.6)
        self.play(ph.animate.scale(0.25).move_to(SE4.p(SW_ * 0.5, SD_ * 0.5, SH_)).set_opacity(0.0), FadeOut(lc), run_time=rt)
        self.play(lamp_on(s0), FadeOut(li), FadeIn(l_running()), run_time=0.3)
        done(self)


def b05_state():
    return VGroup(session(SE4, lit=True), in_belt(), out_belt(), l_running())


# ══════════════ B06: thirty days ══════════════
SE6 = Iso(-4.55, -1.15, 0.62)
BAR_Y, BAR_X0, NSEG, SEGW = -0.25, -1.55, 10, 0.62
PH6 = np.array([-1.05, -1.55, 0])
TRAY = Iso(3.2, -2.9, 0.62)


def seg(i, fill):
    return Rectangle(width=SEGW - 0.1, height=0.42, fill_color=fill, fill_opacity=1, stroke_width=0).move_to(
        [BAR_X0 + SEGW * i + SEGW / 2, BAR_Y, 0])


def bar_ghost():
    return VGroup(*[seg(i, GHOST) for i in range(NSEG)]).set_z_index(-1)


def bar_fill(n=NSEG):
    return VGroup(*[seg(i, (BAR1, BAR2)[i % 2]) for i in range(n)])


def history_stack():
    iso = Iso(-5.4, 0.9, 0.5)
    cards = VGroup(*[iso.box(0, 0, 0.16 * k, 1.8, 1.2, 0.1, PAGE_TOP, PAGE_L, PAGE_R, sw=3) for k in range(4)])
    return cards


def l_history6():
    return T("history", 42).move_to([-4.15, 2.75, 0])


def l_30():
    return T("30 days", 96, INK, bold=True).move_to([1.55, 1.75, 0])


def l_docs():
    return T("per Anthropic's docs", 36).move_to([1.55, 0.65, 0])


def tray():
    back, front = TRAY.open_box(0, 0, 0, 2.2, 1.6, 0.6)
    return VGroup(back, front)


def l_outputs():
    return T("outputs", 42).move_to([5.3, -0.95, 0])


def s6_in_belt():
    return strip_x(SE6, -2.2, -0.05, 0.3, 1.0)


class B06_ThirtyDays(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        s0 = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3])), run_time=0.35)
        self.play(to_rig(s0, SE4, SE6), run_time=0.6)
        until(self, "conversation history stays", lead=0.3)
        hs = history_stack()
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.3) for c in hs], lag_ratio=0.2), run_time=rt)
        self.play(FadeIn(l_history6()), run_time=0.3)
        until(self, "The sandbox state lasts", lead=0.35)
        ph = photo(PH6, 0.8)
        gb = bar_ghost()
        rt = guard(self, 0.5)
        self.play(GrowFromPoint(ph, SE6.p(SW_ / 2, SD_ / 2, SH_)), FadeIn(gb), run_time=rt)
        self.play(FadeIn(l_30()), FadeIn(l_docs()), run_time=0.35)
        bf = bar_fill()
        until(self, "from when the sandbox", lead=0.3)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(b) for b in bf[:5]], lag_ratio=0.3), run_time=rt)
        until(self, "activity doesn't extend", lead=0.3)
        ib = s6_in_belt()
        c = ecard(SE6, -1.7, 0.65)
        self.add(ib, c)
        rt = guard(self, 0.9)
        self.play(c.animate.shift(SE6.v(1.35, 0, 0)), LaggedStart(*[FadeIn(b) for b in bf[5:]], lag_ratio=0.3), run_time=rt)
        self.play(FadeOut(c), ph.animate.set_opacity(0.15), run_time=0.35)
        until(self, "save what matters", lead=0.3)
        tr = tray()
        rt = guard(self, 0.4)
        self.play(FadeIn(tr), FadeIn(l_outputs()), run_time=rt)
        f = ecard(TRAY, 1.1, 0.8, z=0.05)
        f.set_z_index(1)
        self.play(FadeIn(f, shift=DOWN * 1.2), run_time=0.45, rate_func=ease_in)
        done(self)


def b06_state():
    f = ecard(TRAY, 1.1, 0.8, z=0.05)
    f.set_z_index(1)
    return VGroup(session(SE6, lit=True), history_stack(), l_history6(), photo(PH6, 0.8).set_opacity(0.15), bar_fill(),
                  l_30(), l_docs(), s6_in_belt(), tray(), f, l_outputs())


# ══════════════ B07: together ══════════════
AG7 = Iso(-5.5, 0.75, 0.48)
EN7 = Iso(-4.85, -2.45, 0.52)
SE7 = [Iso(-0.35, -2.55, 0.6), Iso(1.9, -1.35, 0.6), Iso(4.15, -0.15, 0.6)]
HUB = np.array([-2.2, -0.35, 0])


def l_one():
    return T("one agent", 42).move_to([-3.95, 2.75, 0])


def l_many():
    return T("many sessions", 42).move_to([1.3, 2.55, 0])


class B07_Together(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        s0 = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 11)])), run_time=0.45)
        bp, en = blueprint(AG7), env(EN7)
        until(self, "one agent and one environment", lead=0.3)
        rt = guard(self, 0.6)
        self.play(FadeIn(bp, shift=DOWN * 0.4), FadeIn(en, shift=DOWN * 0.4), to_rig(s0, SE6, SE7[0]), run_time=rt)
        self.play(FadeIn(l_one()), s0[3].animate.set_color(GHOST), run_time=0.3)
        until(self, "as many sessions", lead=0.3)
        ss = [s0]
        for k in (1, 2):
            s = session(SE7[k])
            s.scale(0.3).move_to(HUB)
            ss.append(s)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[Transform(ss[k], session(SE7[k])) for k in (1, 2)], lag_ratio=0.35), run_time=rt)
        self.play(FadeIn(l_many()), run_time=0.3)
        until(self, "driven by events", lead=0.3)
        cards = []
        paths = []
        for k in range(3):
            c = ecard(Iso(HUB[0], HUB[1], 0.6), 0, 0)
            cards.append(c)
            paths.append(ArcBetweenPoints(HUB, SE7[k].p(0.2, SD_ * 0.5, SH_ + 0.3), angle=-0.5))
        self.add(*cards)
        rt = guard(self, 1.0)
        self.play(*[MoveAlongPath(c, p) for c, p in zip(cards, paths)], run_time=rt)
        self.play(*[FadeOut(c) for c in cards], *[s[3].animate.set_color(TERRA) for s in ss], run_time=0.3)
        until(self, "You design the four parts", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(bp, en), color=None, scale_factor=1.06), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_FourParts, B01_Blueprint, B02_Environment, B03_Session, B04_Events, B05_Checkpoint, B06_ThirtyDays, B07_Together):
    _cls.play = ST.play
