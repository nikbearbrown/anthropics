"""
Manim scenes for show-tell-half-price-if-you-can-wait (show-tell skill, card #17, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The Message Batches API, from anthropics/claude-cookbooks/misc/batch_processing.ipynb, checked against the raw
live docs page (platform.claude.com/docs/en/build-with-claude/batch-processing.md, 2026-09-27): a pile of white
ENVELOPES (requests) goes one at a time into the kraft CLAUDE box while a CLOCK sweeps (the loop); the same
envelopes sit on one TRAY and get kraft SEALS with ink numerals (custom_id); the tray drops through the slot, a
batch-ID ticket pops out and a dark STATUS board rises (grey lamp = in_progress); four LANES carry the requests
independently and finish out of order (2, 0, 3, 1); your code's TERMINAL polls until the lamp turns terracotta
(ended); kraft ANSWER cards come back in any order and are matched under their envelopes by seal; checks mark
succeeded, a cross marks errored, and only that envelope goes back in; two price BARS and a hero 50%.
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







# ═════════════════════════════ the film: half price if you can wait ═════════════════════════════
# Cast: white ENVELOPES lying flat (a request; a V flap on top), later sealed with a kraft SEAL carrying an ink
# numeral (its custom_id); the big kraft CLAUDE box (dark slot on top, dark mouth on its left face, terracotta spark);
# a kraft TERMINAL (your code); a CLOCK; a dark STATUS board with one lamp (grey = in_progress, terracotta = ended);
# four LANES; kraft ANSWER cards with the same seals; ink checks and one ink cross; two price BARS and a hero 50%.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage
SEAL = BOX_L


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


# ─── ENVELOPES and ANSWERS ───
EW, ED = 1.4, 0.95
ES = 0.95                                  # the standard envelope scale


def seal(k, c):
    c = P3(c)
    return VGroup(RoundedRectangle(width=0.62, height=0.5, corner_radius=0.16, fill_color=SEAL, fill_opacity=1, stroke_width=0).move_to(c),
                  T(str(k), 38, INK, bold=True).move_to(c)).set_z_index(6)


def env_seal_pt(iso):
    return iso.p(EW / 2, ED * 0.42, 0.06)


def envelope(cx, cy, k=None, s=ES, under=False):
    iso = rig_at(cx, cy, s, EW, ED)
    slab = iso.box(0, 0, 0, EW, ED, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    if under:
        for f in slab:
            f.set_stroke(DEV_EDGE, 2)
    tip = env_seal_pt(iso)
    c0, c1 = iso.p(0.1, ED - 0.06, 0.06), iso.p(EW - 0.06, ED - 0.1, 0.06)
    flap = VGroup(Line(c0, c0 + (tip - c0) * 0.55, color=BAR2, stroke_width=5),
                  Line(c1 + (tip - c1) * 0.55, c1, color=BAR2, stroke_width=5))      # stops short of the seal (layout audit)
    g = VGroup(slab, flap)
    if k is not None:
        g.add(seal(k, tip))
    return g


def answer(cx, cy, k=None, s=ES):
    iso = rig_at(cx, cy, s, EW, ED)
    slab = iso.box(0, 0, 0, EW, ED, 0.1, BOX_TOP, BOX_L, BOX_R, sw=4)
    zt = 0.1
    bars = VGroup(iso.quad([(0.2, 0.62, zt), (1.2, 0.62, zt), (1.2, 0.74, zt), (0.2, 0.74, zt)], BAR2, sw=0),
                  iso.quad([(0.2, 0.36, zt), (0.9, 0.36, zt), (0.9, 0.48, zt), (0.2, 0.48, zt)], BAR2, sw=0))
    g = VGroup(slab, bars)
    if k is not None:
        g.add(seal(k, iso.p(1.05, 0.3, zt) + LEFT * 0.05))
    return g


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

    def top(self):
        return self.iso.p(CW, CD, CH)


def box_to(mob, A, B):
    """Animate a box built on CBox A to CBox B (linear projection: scale + shift)."""
    return mob.animate.scale(B.s / A.s, about_point=A.iso.p(0, 0, 0)).shift(B.iso.p(0, 0, 0) - A.iso.p(0, 0, 0))


# ─── STATUS board (dark, one lamp) ───
BDW, BDD, BDH = 0.3, 1.4, 1.45


def board(c):
    i = rig_at(c[0], c[1], 0.8, BDW, BDD)
    b = i.box(0, 0, 0, BDW, BDD, BDH, DARK_TOP, DARK_L, DARK_R)
    lamp = Circle(radius=0.19, fill_color=GHOST, fill_opacity=1, stroke_color=GHOST, stroke_width=2).move_to(i.p(0, BDD / 2, BDH * 0.55))
    return VGroup(b, lamp)


# ─── TERMINAL (your code) ───
TW, TD, TH = 1.3, 1.1, 1.0


def terminal(cx, cy, s=0.9):
    i = rig_at(cx, cy, s, TW, TD)
    body = i.box(0, 0, 0, TW, TD, TH)
    scr = i.quad([(0, 0.15, 0.22), (0, 0.95, 0.22), (0, 0.95, 0.86), (0, 0.15, 0.86)], DARK_TOP, sw=0)
    cur = Dot(i.p(0, 0.35, 0.42), radius=0.07, color=TERRA)
    return VGroup(body, scr, cur), i.p(0, 0.55, TH)


# ─── CLOCK ───
def clock(c, r=1.0):
    c = P3(c)
    face = Circle(radius=r, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=7).move_to(c)
    mn = Line(c, c + UP * r * 0.72, color=INK, stroke_width=9)
    hr = Line(c, c + (RIGHT * 0.42 + UP * 0.12) * r, color=INK, stroke_width=12)
    hub = Dot(c, radius=0.1 * r, color=TERRA).set_z_index(3)
    return VGroup(face, hr, mn, hub)


def spin(ck, turns=1.0):
    return Rotate(ck[2], angle=-TAU * turns, about_point=np.array(ck[0].get_center()))


def slip():
    card = RoundedRectangle(width=0.8, height=0.52, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1,
                            stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.24, 0.07, 0], [0.26, 0.07, 0], color=BAR1, stroke_width=6),
                Line([-0.24, -0.09, 0], [0.12, -0.09, 0], color=BAR1, stroke_width=6))
    return VGroup(card, ln).set_z_index(10)


def cross(x, y, s=0.22, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w))


# ══════════════ B00: the loop, one at a time ══════════════
BX0 = CBox(3.3, -1.35, 0.95)
PILE = (-4.4, -1.95)
PILE_N = 4
ANS0 = [(-1.85, -2.3), (0.35, -2.3)]
CK0 = (-4.4, 1.75)


def pile(n=PILE_N):
    return VGroup(*[envelope(PILE[0], PILE[1] + 0.2 * k, under=(k < n - 1)) for k in range(n)])


def l_claude(c=(3.3, 1.6)):
    return lbl("Claude", c)


def l_requests():
    return lbl("requests", (-4.4, -0.3))


def l_oneatatime():
    return lbl("one at a time", (-1.6, 1.75))


def b00_state():
    return VGroup(BX0.mob(), pile(PILE_N - 2), clock(CK0), VGroup(*[answer(*a) for a in ANS0]),
                  l_claude(), l_requests(), l_oneatatime())


class B00_Loop(Scene):
    def construct(self):
        box = BX0.mob()
        pl = pile()
        ck = clock(CK0)
        self.add(box, pl)
        self.play(FadeIn(ck), FadeIn(l_claude()), FadeIn(l_requests()), run_time=0.5)
        self.play(FadeIn(l_oneatatime()), run_time=0.3)
        for n, (phrase, wphrase) in enumerate((("Send one request", "wait for its answer"), ("then send the next", "a thousand waits"))):
            until(self, phrase, lead=0.2)
            e = pl[PILE_N - 1 - n]
            dest = BX0.slot() + UP * 0.55
            rt = guard(self, 1.2)
            self.play(MoveAlongPath(e, ArcBetweenPoints(np.array(e.get_center()), dest, angle=-0.7)), run_time=rt * 0.75)
            self.play(e.animate.scale(0.25).move_to(BX0.slot()), run_time=rt * 0.25, rate_func=ease_in)
            self.remove(e)
            until(self, wphrase, lead=0.2)
            rt = guard(self, 1.0)
            self.play(spin(ck), run_time=rt)
            a = answer(*ANS0[n])
            a0 = a.copy().scale(0.3).move_to(BX0.mouth())
            rt = guard(self, 0.7)
            self.play(Transform(a0, a), run_time=rt)
        until(self, "billed at the standard price", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(box[3], color=None, scale_factor=1.6), run_time=rt)
        done(self)


# ══════════════ B01: one list, a tag on each ══════════════
TRW, TRD, TRH = 6.4, 1.45, 0.3
TR1 = rig_at(-2.1, -0.85, 0.9, TRW, TRD)
EX = [0.15 + 1.55 * k for k in range(4)]


def tray(iso=TR1):
    back, front = iso.open_box(0, 0, 0, TRW, TRD, TRH)
    return back, front


def tray_env_center(iso, k):
    """screen centre of envelope k lying on the tray floor."""
    return (iso.p(EX[k], 0.25, 0.02) + iso.p(EX[k] + EW, 0.25 + ED, 0.02)) / 2 + np.array([0, 0, 0])


def tray_envs(iso=TR1, sealed=False):
    g = VGroup()
    for k in range(4):
        c = tray_env_center(iso, k)
        e = envelope(c[0], c[1] - 0.03, k if sealed else None, s=iso.s)
        e.set_z_index(1)
        g.add(e)
    return g


def l_batch():
    return lbl("batch", (-4.7, 0.45))


def l_customid():
    return lbl("custom_id", (0.4, -2.8))


def b01_state():
    back, front = tray()
    return VGroup(BX0.mob(), l_claude(), back, tray_envs(sealed=True), front, l_batch(), l_customid())


class B01_Batch(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[1], st[2], st[3], st[5], st[6])), run_time=0.5)
        until(self, "A batch is the same requests", lead=0.3)
        back, front = tray()
        envs = tray_envs()
        rt = guard(self, 0.5)
        self.play(FadeIn(VGroup(back, front), shift=DOWN * 0.6), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.8) for e in envs], lag_ratio=0.3), FadeIn(l_batch()), run_time=rt, rate_func=ease_in)
        until(self, "plus a custom ID", lead=0.2)
        seals = VGroup(*[seal(k, env_seal_pt(rig_at(*tray_env_center(TR1, k)[:2] - np.array([0, 0.03]), TR1.s, EW, ED))) for k in range(4)])
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(sl, shift=DOWN * 0.5) for sl in seals], lag_ratio=0.35), FadeIn(l_customid()), run_time=rt)
        until(self, "like question zero", lead=0.1)
        rt = guard(self, 0.4)
        self.play(Indicate(seals[0], color=None, scale_factor=1.3), run_time=rt)
        until(self, "question one", lead=0.1)
        rt = guard(self, 0.4)
        self.play(Indicate(seals[1], color=None, scale_factor=1.3), run_time=rt)
        until(self, "how you find its answer", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(seals, color=None, scale_factor=1.2), run_time=rt)
        done(self)


# ══════════════ B02: submit in one call ══════════════
TICKET = (-3.0, 1.3)
BD2 = (0.3, -1.45)


def ticket():
    return slip().scale(1.25).move_to(P3(TICKET))


def l_batchid():
    return lbl("batch ID", (-3.0, 0.5))


def l_inprog(c=BD2):
    return lbl("in_progress", (c[0], c[1] + 2.05))


def l_ended(c=BD2):
    return lbl("ended", (c[0], c[1] + 2.05))


def b02_state():
    return VGroup(BX0.mob(), l_claude(), ticket(), l_batchid(), board(BD2), l_inprog())


class B02_Submit(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        box = st[0]
        load = VGroup(st[2], st[3], st[4])
        self.play(FadeOut(VGroup(st[5], st[6])), run_time=0.3)
        rt = guard(self, 0.9)
        self.play(load.animate.scale(0.42).move_to(BX0.slot() + UP * 1.0 + LEFT * 2.4), run_time=rt)
        until(self, "goes in at once", lead=0.3)
        rt = guard(self, 0.4)
        self.play(load.animate.scale(0.25).move_to(BX0.slot()), run_time=rt, rate_func=ease_in)
        self.remove(load)
        rt = guard(self, 0.4)
        self.play(Indicate(box[1], color=None, scale_factor=1.15), run_time=rt)
        until(self, "you get back a batch ID", lead=0.2)
        tk = slip().scale(0.4).move_to(BX0.slot())
        self.add(tk)
        rt = guard(self, 0.6)
        self.play(tk.animate.scale(1.25 / 0.4).move_to(P3(TICKET)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_batchid()), run_time=rt)
        until(self, "with its status", lead=0.2)
        bd = board(BD2)
        rt = guard(self, 0.5)
        self.play(GrowFromEdge(bd, DOWN), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_inprog()), run_time=rt)
        done(self)


# ══════════════ B03: asynchronous, each on its own ══════════════
BX3 = CBox(-4.75, -0.55, 0.55)
LANE_Y = [1.5, 0.35, -0.8, -1.95]
LX0, LX1 = -2.55, 4.15
LAMP_X = 4.75
E3 = 0.7
FIN = [2.2, 3.4, 1.3, 2.8]                      # finish times: 2, 0, 3, 1


def lanes():
    g = VGroup()
    for y in LANE_Y:
        top = Polygon([LX0, y - 0.36, 0], [LX1, y - 0.36, 0], [LX1, y + 0.36, 0], [LX0, y + 0.36, 0],
                      fill_color=PAD, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2)
        lip = Polygon([LX0, y - 0.36, 0], [LX1, y - 0.36, 0], [LX1, y - 0.5, 0], [LX0, y - 0.5, 0],
                      fill_color=BOX_R, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2)
        g.add(VGroup(top, lip).set_z_index(-2))
    return g


def lamps(on=()):
    return VGroup(*[Circle(radius=0.17, fill_color=TERRA if k in on else GHOST, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2)
                    .move_to([LAMP_X, y, 0]) for k, y in enumerate(LANE_Y)])


def lane_env(k, at_end=False):
    x = (LX1 - 0.85) if at_end else (LX0 + 0.85)
    return envelope(x, LANE_Y[k] + 0.08, k, s=E3)


def l_hour():
    return lbl("most: under 1 hour", (-0.3, 2.75))


def l_24():
    return lbl("24 h limit", (3.4, 2.75))


def b03_state():
    return VGroup(BX3.mob(), lbl("Claude", (-4.75, 1.3)), lanes(), lamps(on=(0, 1, 2, 3)),
                  VGroup(*[lane_env(k, True) for k in range(4)]), l_hour(), l_24())


class B03_Async(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        box, lc = st[0], st[1]
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5])), run_time=0.35)
        rt = guard(self, 0.7)
        self.play(box_to(box, BX0, BX3), lc.animate.move_to([-4.75, 1.3, 0]), run_time=rt)
        until(self, "runs asynchronously", lead=0.4)
        ln, lp = lanes(), lamps()
        rt = guard(self, 0.5)
        self.play(FadeIn(ln), FadeIn(lp), run_time=rt)
        envs = VGroup(*[lane_env(k) for k in range(4)])
        srcs = [e.copy().scale(0.3).move_to(BX3.mouth()) for e in envs]
        rt = guard(self, 0.6)
        self.play(*[Transform(s_, e) for s_, e in zip(srcs, envs)], run_time=rt)
        until(self, "handled on its own", lead=0.3)
        starts = [np.array(e.get_center()) for e in envs]
        dx = (LX1 - LX0) - 1.7
        T_ = max(FIN)
        rt = guard(self, T_)
        lit = set()

        def upd(g, a):
            t = a * T_
            for k in range(4):
                f = min(1.0, t / FIN[k])
                srcs[k].move_to(starts[k] + RIGHT * dx * f)
                if f >= 1.0 and k not in lit:
                    lit.add(k)
                    lp[k].set_fill(TERRA)
            return g
        self.play(UpdateFromAlphaFunc(VGroup(*srcs), upd), run_time=rt, rate_func=linear)
        for k in range(4):
            lp[k].set_fill(TERRA)
        until(self, "most batches finish", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_hour()), run_time=rt)
        until(self, "twenty four hours", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_24()), Indicate(lp, color=None, scale_factor=1.3), run_time=rt)
        done(self)


# ══════════════ B04: your code polls ══════════════
BX4 = CBox(3.6, -1.35, 0.8)
TERM4 = (-4.3, -1.35)
CK4 = (-1.9, 1.85)
BD4 = (0.9, -1.4)


def l_yourcode():
    return lbl("your code", (-4.3, 0.2))


def b04_state():
    term, _ = terminal(*TERM4)
    bd = board(BD4)
    bd[1].set_fill(TERRA)
    return VGroup(BX4.mob(), l_claude((3.6, 1.35)), term, l_yourcode(), clock(CK4, 0.9), bd, l_ended(BD4))


class B04_Poll(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        box, lc = st[0], st[1]
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5], st[6])), run_time=0.35)
        rt = guard(self, 0.6)
        self.play(box_to(box, BX3, BX4), lc.animate.move_to([3.6, 1.35, 0]), run_time=rt)
        term, tport = terminal(*TERM4)
        bd = board(BD4)
        ck = clock(CK4, 0.9)
        lab = [l_inprog(BD4)]
        rt = guard(self, 0.5)
        self.play(FadeIn(term, shift=DOWN * 0.5), GrowFromEdge(bd, DOWN), FadeIn(ck), FadeIn(l_yourcode()), FadeIn(lab[0]), run_time=rt)
        lamp_pt = np.array(bd[1].get_center())

        def poll(final=False):
            s_ = slip().move_to(tport + UP * 0.3)
            self.add(s_)
            rt_ = guard(self, 1.1)
            self.play(MoveAlongPath(s_, ArcBetweenPoints(tport + UP * 0.3, lamp_pt + LEFT * 0.7 + UP * 0.3, angle=-0.6)), run_time=rt_ * 0.5)
            if final:
                self.play(bd[1].animate.set_fill(TERRA), FadeOut(lab[0]), FadeIn(l_ended(BD4)), run_time=0.35)
            self.play(MoveAlongPath(s_, ArcBetweenPoints(lamp_pt + LEFT * 0.7 + UP * 0.3, tport + UP * 0.3, angle=-0.6)), run_time=rt_ * 0.5)
            self.remove(s_)
        until(self, "your code polls", lead=0.3)
        poll()
        until(self, "asks for the batch's status", lead=0.3)
        rt = guard(self, 0.6)
        self.play(spin(ck, 0.5), run_time=rt)
        poll()
        until(self, "until every request has finished", lead=0.2)
        rt = guard(self, 0.9)
        self.play(spin(ck), run_time=rt)
        until(self, "Then it flips to ended", lead=0.5)
        poll(final=True)
        until(self, "results are ready", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(box, color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B05: any order, matched by custom_id ══════════════
BX5 = CBox(-4.95, -1.65, 0.55)
XS = [-2.0, 0.3, 2.6, 4.9]
YTOP, YBOT = 1.55, -1.25
ORDER = [2, 0, 3, 1]                            # the answer that lands in slot i


def l_req5():
    return lbl("requests", (-4.95, 1.6))


def l_results():
    return lbl("results", (1.45, -2.65))


def l_bycid():
    return lbl("by custom_id", (1.45, 0.2))


def b05_state():
    return VGroup(BX5.mob(), VGroup(*[envelope(XS[k], YTOP, k) for k in range(4)]),
                  VGroup(*[answer(XS[k], YBOT, k) for k in range(4)]), l_req5(), l_results(), l_bycid())


class B05_Match(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        box = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 7)])), run_time=0.35)
        rt = guard(self, 0.6)
        envs = VGroup(*[envelope(XS[k], YTOP, k) for k in range(4)])
        self.play(box_to(box, BX4, BX5), LaggedStart(*[FadeIn(e, shift=DOWN * 0.6) for e in envs], lag_ratio=0.2), FadeIn(l_req5()), run_time=rt)
        until(self, "come back as one list", lead=0.4)
        ans = [None] * 4
        anims = []
        for i, k in enumerate(ORDER):
            a = answer(XS[i], YBOT, k)
            a0 = a.copy().scale(0.3).move_to(BX5.mouth())
            ans[k] = a0
            anims.append(Transform(a0, a))
        rt = guard(self, 1.6)
        self.play(LaggedStart(*anims, lag_ratio=0.3), FadeIn(l_results()), run_time=rt)
        until(self, "in any order", lead=0.1)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*ans), color=None, scale_factor=1.06), run_time=rt)
        until(self, "Match by custom ID", lead=0.3)
        mv = []
        for i, k in enumerate(ORDER):
            if i != k:
                a, b = np.array(ans[k].get_center()), np.array([XS[k], YBOT, 0])
                mv.append(MoveAlongPath(ans[k], ArcBetweenPoints(a, b, angle=0.5 if b[0] > a[0] else -0.5)))
        rt = guard(self, 1.0)
        self.play(*mv, run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_bycid()), run_time=rt)
        until(self, "the request tagged two", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(envs[2], ans[2]), color=None, scale_factor=1.08), run_time=rt)
        done(self)


# ══════════════ B06: succeeded, errored, send the failed one again ══════════════
def mark_pt(k):
    return (XS[k] + 0.8, YBOT + 0.95)


def l_ok():
    return lbl("succeeded", (XS[3], YBOT - 1.35))


def l_err():
    return lbl("errored", (XS[1], YBOT - 1.35))


def b06_state():
    return VGroup(BX5.mob(), VGroup(*[envelope(XS[k], YTOP, k) for k in (0, 2, 3)]),
                  VGroup(*[answer(XS[k], YBOT, k) for k in (0, 2, 3)]), l_req5(),
                  VGroup(*[check(*mark_pt(k), 0.22) for k in (0, 2, 3)]), cross(*mark_pt(1)), l_ok(), l_err())


class B06_Results(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        box, envs, ans = st[0], st[1], st[2]
        self.play(FadeOut(st[4]), FadeOut(st[5]), run_time=0.3)
        until(self, "Most say succeeded", lead=0.2)
        cks = [check(*mark_pt(k), 0.22) for k in (0, 2, 3)]
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[Create(c) for c in cks], lag_ratio=0.3), FadeIn(l_ok()), run_time=rt)
        until(self, "One might say errored", lead=0.2)
        cx = cross(*mark_pt(1))
        rt = guard(self, 0.5)
        self.play(Create(cx), FadeIn(l_err()), run_time=rt)
        until(self, "aren't billed", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(cx, color=None, scale_factor=1.3), run_time=rt)
        until(self, "send just the failed ones", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeOut(ans[1]), run_time=rt)
        e = envs[1]
        dest = BX5.slot() + UP * 0.5
        rt = guard(self, 1.1)
        self.play(MoveAlongPath(e, ArcBetweenPoints(np.array(e.get_center()), dest, angle=0.6)), run_time=rt * 0.75)
        self.play(e.animate.scale(0.3).move_to(BX5.slot()), run_time=rt * 0.25, rate_func=ease_in)
        self.remove(e)
        done(self)


# ══════════════ B07: half price ══════════════
BASE = -2.25
SEG, GAP = 0.52, 0.08
BXS = (-3.4, -1.0)


def segs(x, n):
    return VGroup(*[Rectangle(width=1.35, height=SEG, fill_color=(BAR1, BAR2)[i % 2], fill_opacity=1, stroke_width=0)
                    .move_to([x, BASE + GAP + (SEG + GAP) * i + SEG / 2, 0]) for i in range(n)])


def l_std():
    return lbl("standard", (BXS[0], BASE - 0.45))


def l_bat():
    return lbl("batch", (BXS[1], BASE - 0.45))


def hero():
    return T("50%", 150, INK, bold=True).move_to([3.3, 1.35, 0])


def l_docs():
    return lbl("per Anthropic's docs", (3.3, 0.1), 38)


CK7 = (3.3, -1.55)


def floor7():
    return Line([-4.6, BASE, 0], [0.3, BASE, 0], color=DEV_EDGE, stroke_width=4)


class B07_Half(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        fl = floor7()
        sa = segs(BXS[0], 8)
        rt = guard(self, 1.0)
        self.play(Create(fl), LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in sa], lag_ratio=0.25), FadeIn(l_std()), run_time=rt)
        until(self, "Anthropic's docs say", lead=0.3)
        sb = segs(BXS[1], 8)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in sb], lag_ratio=0.25), FadeIn(l_bat()), run_time=rt)
        until(self, "fifty percent", lead=0.3)
        rt = guard(self, 0.6)
        self.play(*[x.animate.shift(RIGHT * 1.2 + UP * 0.4).set_opacity(0) for x in sb[4:]], run_time=rt)
        self.remove(*sb[4:])
        rt = guard(self, 0.4)
        self.play(FadeIn(hero(), scale=1.2), FadeIn(l_docs()), run_time=rt)
        until(self, "The trade is time", lead=0.2)
        ck = clock(CK7, 1.0)
        rt = guard(self, 0.5)
        self.play(FadeIn(ck, shift=UP * 0.4), run_time=rt)
        rt = guard(self, 1.2)
        self.play(spin(ck), run_time=rt)
        until(self, "twenty nine days", lead=0.2)
        rt = guard(self, 1.0)
        self.play(spin(ck, 0.5), run_time=rt)
        until(self, "they cost half", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*sb[:4]), color=None, scale_factor=1.06), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Loop, B01_Batch, B02_Submit, B03_Async, B04_Poll, B05_Match, B06_Results, B07_Half):
    _cls.play = ST.play
