"""
Manim scenes for show-tell-legacy-code-in-order (show-tell skill, card #24, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Anthropic's code-modernization plugin (v1.0.0, read raw from GitHub main on 2026-09-27): the
order preflight -> assess -> map -> extract-rules -> review -> brief -> (uplift | transform |
reimagine) -> verify -> harden, and the README's six points where a person decides.
Cast: the legacy CABINET (a tall dark mainframe, two ghost tape reels, a terracotta lamp) standing
in the kraft LEGACY tray, with a kraft PADLOCK; the kraft ANALYSIS tray, where each step's page
lands flat; the kraft MODERNIZED tray, where the new kraft BOX lands; a HUD of six pips ("you
decide") that light terracotta one by one. Per beat: the question card, three lenses, the
circle-pack map, rule cards, the brief binder and its gate, three dark build doors, the comparator
and test lamps, the verdict card, the ranked findings and the patch.
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




# ═════════════════════════════ the film: legacy code, in order ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
TILE = "#B39A72"          # deep kraft (pale kraft fails Gate V contrast)
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (outside GATE T's ink tolerance)


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


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.08):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def gbar(x0, x1, y, color=BAR1, w=6):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def slip(c, s=1.0):
    """A small white slip with two grey lines: an input or an output."""
    c = P3(c)
    body = rrect(0.62 * s, 0.42 * s, c, PAGE_TOP, INK, 4, r=0.06)
    ln = VGroup(gbar(c[0] - 0.19 * s, c[0] + 0.19 * s, c[1] + 0.06 * s, BAR1, 5),
                gbar(c[0] - 0.19 * s, c[0] + 0.08 * s, c[1] - 0.08 * s, BAR1, 5))
    return VGroup(body, ln).set_z_index(10)


# ─── the LEGACY tray and the CABINET standing in it ───
LGW, LGD, LGH = 1.9, 1.7, 0.35
LG = rig_at(-4.45, -1.55, 0.75, LGW, LGD)
CX0, CY0, CWD, CDP, CHT = 0.35, 0.3, 1.2, 1.05, 2.6


def reel(yc, zc, r=0.2):
    pts = [LG.p(CX0, yc + r * np.cos(t), zc + r * np.sin(t)) for t in np.linspace(0, 2 * PI, 28, endpoint=False)]
    disc = Polygon(*pts, fill_color=GHOST, fill_opacity=1, stroke_width=0)
    return VGroup(disc)


def cabinet():
    """(group, lamp): a tall dark mainframe with two tape reels and a terracotta lamp (grey vents read as text under GATE T)."""
    body = LG.box(CX0, CY0, 0, CWD, CDP, CHT, DK_TOP, DK_L, DK_R)
    reels = VGroup(reel(CY0 + CDP * 0.27, CHT * 0.72), reel(CY0 + CDP * 0.73, CHT * 0.72))
    lamp = Dot(LG.p(CX0 + CWD * 0.72, CY0, CHT * 0.25), radius=0.1, color=TERRA)
    g = VGroup(body, reels, lamp).set_z_index(1)
    return g, lamp


def cab_pt(f, z):
    """A point on the cabinet's right (front) face: f along its width, z up."""
    return LG.p(CX0 + CWD * f, CY0, z)


CAB_TOP = LG.p(CX0 + CWD / 2, CY0 + CDP / 2, CHT)
CAB_IN = LG.p(CX0 + CWD * 0.85, CY0, CHT * 0.85)


def legacy():
    back, front = LG.open_box(0, 0, 0, LGW, LGD, LGH)
    cab, lamp = cabinet()
    return VGroup(back, cab, front), cab, lamp


def padlock():
    c = cab_pt(0.36, 1.35)
    body = rrect(0.5, 0.42, (c[0], c[1] - 0.05), BOX_L, INK, 4, r=0.06)
    shackle = Arc(radius=0.16, start_angle=0, angle=PI, arc_center=P3((c[0], c[1] + 0.16)), color=INK, stroke_width=9)
    hole = Dot(P3((c[0], c[1] - 0.05)), radius=0.05, color=INK)
    return VGroup(shackle, body, hole).set_z_index(3)


# ─── the ANALYSIS tray (pages land flat in it) and the MODERNIZED tray (the new box lands in it) ───
ATW, ATD, ATH = 3.4, 1.5, 0.35
AT = rig_at(0.0, -1.62, 0.7, ATW, ATD)
PGW, PGD = 0.5, 0.95


def atray():
    back, front = AT.open_box(0, 0, 0, ATW, ATD, ATH)
    return VGroup(back, front)


def apage(i):
    return AT.page(0.25 + 0.62 * i, 0.28, 0.03, PGW, PGD).set_z_index(1)


def apages(n):
    return VGroup(*[apage(i) for i in range(n)])


def slot_pt(i):
    return AT.p(0.25 + 0.62 * i + PGW / 2, 0.28 + PGD / 2, 0.06)


MTW, MTD, MTH = 2.2, 1.7, 0.35
MT = rig_at(4.45, -1.62, 0.7, MTW, MTD)
NBX = (0.5, 0.4, 0.03, 1.2, 0.9, 0.75)


def mtray():
    back, front = MT.open_box(0, 0, 0, MTW, MTD, MTH)
    return VGroup(back, front)


def newbox():
    """The modernized code: a kraft box on a thin dark plinth, with a terracotta spark."""
    x0, y0, z0, w, d, h = NBX
    plinth = MT.box(x0 - 0.05, y0 - 0.05, z0, w + 0.1, d + 0.1, 0.1, DK_TOP, DK_L, DK_R, sw=2)
    body = MT.box(x0, y0, z0 + 0.1, w, d, h)
    spark = Dot(MT.p(x0 + w * 0.3, y0, z0 + 0.1 + h * 0.55), radius=0.08, color=TERRA)
    return VGroup(plinth, body, spark).set_z_index(1)


NB_HOME = np.array(newbox().get_center())


def l_legacy():
    return lbl("legacy/", (-4.45, -2.95), 40)


def l_analysis():
    return lbl("analysis/", (0.0, -3.0), 40)


def l_modern():
    return lbl("modernized/", (4.45, -2.95), 40)


# ─── the HUD: six points where a person decides ───
PIPX = [3.55 + 0.46 * i for i in range(6)]
PIPY = 2.95


def pips(n):
    return VGroup(*[Dot(P3((PIPX[i], PIPY)), radius=0.13, color=TERRA if i < n else BAR2) for i in range(6)]).set_z_index(5)


def l_you():
    return lbl("you decide", (2.05, 2.95), 40)


def step_lbl(s):
    return lbl(s, (-4.45, 1.5), 44)


def world(pages=0, lit=None, box=True):
    """The persistent cast. Returns (group, parts)."""
    lg, cab, lamp = legacy()
    lk = padlock()
    at = atray()
    pg = apages(pages)
    mt = mtray()
    parts = {"legacy": lg, "cab": cab, "lamp": lamp, "lock": lk, "atray": at, "pages": pg, "mtray": mt}
    g = VGroup(lg, lk, at, pg, mt)
    if box:
        nb = newbox()
        parts["box"] = nb
        g.add(nb)
    if lit is not None:
        pp, ly = pips(lit), l_you()
        parts["pips"], parts["you"] = pp, ly
        g.add(pp, ly)
    return g, parts


def light(k, pp):
    """Animations that light pip k."""
    return [pp[k].animate.set_color(TERRA).scale(1.35)]


def unscale(k, pp):
    return [pp[k].animate.scale(1 / 1.35)]


def drop(self, *mobs):
    for m in mobs:
        self.remove(*m.get_family())


def land_page(self, mob, i, rt=0.9):
    """Fly mob into analysis slot i (shrinking), then swap it for the flat page."""
    rt = guard(self, rt)
    self.play(mob.animate.scale(0.22).move_to(slot_pt(i)), run_time=rt * 0.75, rate_func=ease_in)
    drop(self, mob)
    pg = apage(i)
    self.play(FadeIn(pg, scale=1.3), run_time=rt * 0.2)
    return pg


# ══════════════ B00: the three folders ══════════════
def b00_state():
    g, P = world(0, None, box=False)
    return VGroup(g, l_legacy(), l_analysis(), l_modern())


class B00_Folders(Scene):
    def construct(self):
        lg, cab, lamp = legacy()
        rt = guard(self, 0.8)
        self.play(FadeIn(lg, shift=DOWN * 0.5), FadeIn(l_legacy()), run_time=rt)
        until(self, "in order", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(lamp, color=None, scale_factor=1.8), run_time=rt)
        until(self, "stop and review", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(lamp, color=None, scale_factor=1.8), run_time=rt)
        until(self, "nothing edits it", lead=0.3)
        lk = padlock()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(lk), run_time=rt)
        until(self, "analysis, for what", lead=0.3)
        at = atray()
        rt = guard(self, 0.6)
        self.play(FadeIn(at, shift=UP * 0.4), FadeIn(l_analysis()), run_time=rt)
        until(self, "and modernized", lead=0.3)
        mt = mtray()
        rt = guard(self, 0.6)
        self.play(FadeIn(mt, shift=LEFT * 0.4), FadeIn(l_modern()), run_time=rt)
        done(self)


# ══════════════ B01: preflight ══════════════
QC = np.array([-1.2, 0.95, 0.0])
QROWS = [0.64, 0.32, 0.0, -0.32, -0.64]
QLEN = [1.3, 1.0, 1.2, 0.8, 1.05]


def qbox(k):
    return Square(side_length=0.2, fill_color=GHOST, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(QC + np.array([-0.82, QROWS[k], 0]))


def qcard():
    body = rrect(2.3, 1.85, QC, PAGE_TOP, INK, 4, r=0.1)
    rows = VGroup(*[VGroup(qbox(k), gbar(QC[0] - 0.55, QC[0] - 0.55 + QLEN[k], QC[1] + QROWS[k], BAR2, 7)) for k in range(5)])
    return VGroup(body, rows).set_z_index(6)


def qtick(k):
    return check(QC[0] - 0.82, QC[1] + QROWS[k] - 0.02, 0.1, INK, 5).set_z_index(7)


BUILD_CHK = (-2.95, 1.0)


def b01_state():
    g, P = world(1, 1, box=False)
    return VGroup(g, step_lbl("preflight"), check(*BUILD_CHK, 0.2)), P


class B01_Preflight(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        lp = step_lbl("preflight")
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(st[1], st[2], st[3])), FadeIn(lp), run_time=rt)
        until(self, "five questions", lead=0.3)
        qc = qcard()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(qc), run_time=rt)
        until(self, "like whether this", lead=0.3)
        cur = cursor(QC[0] + 1.4, QC[1] - 1.2).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        ticks = VGroup()
        for k, phrase in ((0, "the whole system"), (4, "off limits"), (1, "writes your answers"), (2, "down word"), (3, "for word")):
            until(self, phrase, lead=0.15)
            tp = QC + np.array([-0.82 + 0.05, QROWS[k] - 0.05, 0])
            t = qtick(k)
            rt = guard(self, 0.4)
            self.play(cur.animate.move_to(tp + np.array([0.12, -0.2, 0])), run_time=rt * 0.5)
            self.play(Create(t), run_time=rt * 0.4)
            ticks.add(t)
        until(self, "Meanwhile it proves", lead=0.2)
        cab = st[0][0][1]
        lamp = st[0][0][1][2]
        top, bot = cab_pt(0.5, CHT)[1] + 0.2, cab_pt(0.5, 0.2)[1]
        x0, x1 = cab.get_left()[0] - 0.12, cab.get_right()[0] + 0.12
        scan = Line([x0, top, 0], [x1, top, 0], color=DIM, stroke_width=9).set_z_index(4)
        rt = guard(self, 1.0)
        self.play(FadeIn(scan), FadeOut(cur), run_time=rt * 0.15)
        self.play(scan.animate.move_to([(x0 + x1) / 2, bot, 0]), run_time=rt * 0.6)
        self.play(FadeOut(scan), run_time=rt * 0.15)
        until(self, "looks for missing source", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(lamp, color=None, scale_factor=1.8), Create(check(*BUILD_CHK, 0.2)), run_time=rt)
        until(self, "Those answers", lead=0.3)
        card = VGroup(qc, ticks)
        land_page(self, card, 0, 0.9)
        until(self, "first of six points", lead=0.3)
        pp, ly = pips(0), l_you()
        rt = guard(self, 0.5)
        self.play(FadeIn(pp), FadeIn(ly), run_time=rt)
        rt = guard(self, 0.5)
        self.play(*light(0, pp), run_time=rt)
        rt = guard(self, 0.3)
        self.play(*unscale(0, pp), run_time=rt)
        until(self, "never decides them", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(pp[0], color=None, scale_factor=1.5), run_time=rt)
        done(self)


# ══════════════ B02: assess, then map ══════════════
LENS_AT = [(-3.35, 0.55), (-3.0, -0.25), (-3.45, -1.0)]


def lens(c):
    c = P3(c)
    ring = Circle(radius=0.36, stroke_color=INK, stroke_width=7, fill_color=PAGE_TOP, fill_opacity=1).move_to(c)
    glint = Arc(radius=0.22, start_angle=PI * 0.6, angle=PI * 0.5, arc_center=c, color=BAR2, stroke_width=6)
    d = np.array([0.707, -0.707, 0])
    handle = Line(c + d * 0.36, c + d * 0.72, color=INK, stroke_width=12)
    return VGroup(ring, glint, handle).set_z_index(6)


def assess_page():
    c = np.array([-2.6, 0.4, 0.0])
    body = rrect(0.9, 1.1, c, PAGE_TOP, INK, 4)
    bars = VGroup(*[Rectangle(width=0.14, height=h, fill_color=col, fill_opacity=1, stroke_width=0).move_to(c + np.array([-0.24 + 0.24 * k, -0.35 + h / 2, 0]))
                    for k, (h, col) in enumerate(((0.55, BAR1), (0.35, BAR2), (0.7, BAR1)))])
    return VGroup(body, bars).set_z_index(8)


PK0 = np.array([1.7, 0.75, 0.0])
PK = np.array([2.2, 1.1, 0.0])
MK = 0.85


def mp(x, y):
    return PK + (np.array([x, y, 0.0]) - PK0) * MK
DOMS = [((1.05, 1.2), 0.7), ((2.45, 1.1), 0.62), ((1.75, 0.0), 0.62)]
MODS = [(0.85, 1.4, 0.28), (1.3, 1.0, 0.2), (0.8, 0.85, 0.14), (2.3, 1.3, 0.25), (2.7, 0.95, 0.18),
        (1.55, 0.1, 0.26), (2.0, -0.15, 0.15), (1.85, 0.35, 0.1)]
EDGES = [(0, 3), (1, 5), (2, 5), (3, 4), (4, 6)]
FLOW = [0, 3, 4, 6]


def mod_c(k):
    return mp(MODS[k][0], MODS[k][1])


def edge(a, b):
    pa, pb = mod_c(a), mod_c(b)
    u = (pb - pa) / np.linalg.norm(pb - pa)
    return Line(pa + u * MODS[a][2] * MK, pb - u * MODS[b][2] * MK, color=BAR1, stroke_width=5).set_z_index(3)


def pack_parts():
    ring = Circle(radius=1.55 * MK, stroke_color=BAR1, stroke_width=5, fill_opacity=0).move_to(PK).set_z_index(2)
    doms = VGroup(*[Circle(radius=r * MK, stroke_color=BAR1, stroke_width=3, fill_color=GHOST, fill_opacity=1).move_to(mp(*c)) for c, r in DOMS]).set_z_index(2)
    mods = VGroup(*[Circle(radius=r * MK, stroke_color=DEV_EDGE, stroke_width=3, fill_color=TILE, fill_opacity=1).move_to(mod_c(k))
                    for k, (x, y, r) in enumerate(MODS)]).set_z_index(4)
    edges = VGroup(*[edge(a, b) for a, b in EDGES])
    entry = Circle(radius=MODS[0][2] * MK + 0.1, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to(mod_c(0)).set_z_index(4)
    return ring, doms, mods, edges, entry


def l_map():
    return lbl("map", (0.1, 2.1))


def l_flow():
    return lbl("flow", (4.25, 0.2))


def b02_state():
    g, P = world(2, 1, box=False)
    ring, doms, mods, edges, entry = pack_parts()
    dot = Dot(mod_c(FLOW[-1]), radius=0.1, color=TERRA).set_z_index(6)
    pack = VGroup(ring, doms, edges, mods, entry, dot)
    return VGroup(g, pack, l_map(), l_flow()), P, pack


class B02_AssessMap(Scene):
    def construct(self):
        st, P = b01_state()
        self.add(st)
        la = step_lbl("assess")
        rt = guard(self, 0.5)
        self.play(FadeOut(st[1]), FadeOut(st[2]), FadeIn(la), run_time=rt)
        until(self, "Three agents", lead=0.3)
        ls = VGroup(*[lens((x + 1.6, y)) for x, y in LENS_AT])
        rt = guard(self, 0.7)
        self.play(FadeIn(ls, shift=LEFT * 0.3), run_time=rt * 0.4)
        self.play(ls.animate.shift(LEFT * 1.6), run_time=rt * 0.5)
        until(self, "for structure", lead=0.2)
        rt = guard(self, 0.9)
        self.play(ls.animate.shift(UP * 0.35), run_time=rt * 0.45)
        self.play(ls.animate.shift(DOWN * 0.35), run_time=rt * 0.45)
        until(self, "recommends a pattern", lead=0.3)
        ap = assess_page()
        rt = guard(self, 0.5)
        self.play(FadeOut(ls), FadeIn(ap, shift=RIGHT * 0.3), run_time=rt)
        land_page(self, ap, 1, 0.8)
        until(self, "Step three: map", lead=0.2)
        rt = guard(self, 0.4)
        lm = l_map()
        self.play(FadeOut(la), FadeIn(lm), run_time=rt)
        until(self, "Calls, data", lead=0.2)
        ring, doms, mods, edges, entry = pack_parts()
        rt = guard(self, 1.0)
        self.play(Create(ring), LaggedStart(*[GrowFromCenter(d) for d in doms], lag_ratio=0.2), run_time=rt * 0.45)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in mods], lag_ratio=0.1), run_time=rt * 0.45)
        until(self, "entry points", lead=0.2)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.15), run_time=rt * 0.6)
        self.play(Create(entry), run_time=rt * 0.3)
        until(self, "business flows", lead=0.3)
        dot = Dot(mod_c(FLOW[0]), radius=0.1, color=TERRA).set_z_index(6)
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(dot), FadeIn(l_flow()), run_time=rt)
        for k in range(1, len(FLOW)):
            rt = guard(self, 0.45)
            self.play(dot.animate.move_to(mod_c(FLOW[k])), run_time=rt)
        done(self)


# ══════════════ B03: extract rules, then review ══════════════
RX = [-1.5, -0.35, 0.8, 1.95, 3.1]
RY = 1.75
RV = np.array([0.8, 0.95, 0.0])
PILLS = [(0.0, 0.25), (0.8, 0.25), (1.6, 0.25)]
THREAD_Z = [2.2, 1.9, 1.6, 1.3, 1.0]


def rcard(c, dot=False):
    c = P3(c)
    body = rrect(0.95, 0.7, c, PAGE_TOP, INK, 4)
    ln = VGroup(*[gbar(c[0] - 0.3, c[0] + (0.3 if k != 1 else 0.12), c[1] + y, BAR1, 6) for k, y in enumerate((0.17, 0.0, -0.17))])
    g = VGroup(body, ln)
    if dot:
        ln.shift(RIGHT * 0.06)
        g.add(Dot(c + np.array([-0.34, 0.17, 0]), radius=0.06, color=TERRA))
    return g.set_z_index(8)


def rcards():
    return VGroup(*[rcard((x, RY)) for x in RX])


def thread(k):
    end = cab_pt(0.88, THREAD_Z[k])
    return VGroup(Line(np.array([RX[k], RY - 0.35, 0]), end + np.array([0.12, 0.05, 0]), color=BAR1, stroke_width=4).set_z_index(5),
                  Dot(end, radius=0.06, color=BAR2).set_z_index(5))


def rchecks():
    return VGroup(*[check(x + 0.02, RY + 0.58, 0.14, INK, 6) for x in RX])


def rpill(k, icon):
    x, y = PILLS[k]
    p = rrect(0.66, 0.44, (x, y), PAGE_TOP, BAR1, 4, r=0.2)
    if icon == "ok":
        i = check(x - 0.02, y, 0.11, INK, 6)
    elif icon == "no":
        i = cross(x, y, 0.1, 6)
    else:
        i = Line([x - 0.13, y, 0], [x + 0.13, y, 0], color=INK, stroke_width=6)
    return VGroup(p, i).set_z_index(8)


def l_rules():
    return lbl("rule cards", (-3.3, 1.75))


def l_review():
    return lbl("review", (2.3, 0.95))


def b03_state():
    g, P = world(3, 2, box=False)
    cards = rcards()
    cards[2].become(rcard(RV, dot=True))
    ck = rchecks()
    ck[2].shift(RV - np.array([RX[2], RY, 0]))
    pills = VGroup(rpill(0, "ok"), rpill(1, "no"), rpill(2, "?"))
    pills[0][0].set_fill(BAR3)
    cur = cursor(PILLS[0][0] + 0.1, PILLS[0][1] - 0.1).set_z_index(12)
    return VGroup(g, cards, ck, pills, cur, l_rules(), l_review()), P, cards


class B03_Rules(Scene):
    def construct(self):
        st, P, pack = b02_state()
        self.add(st)
        rt = guard(self, 0.8)
        self.play(pack.animate.scale(0.12).move_to(slot_pt(2)), FadeOut(VGroup(st[2], st[3])), run_time=rt * 0.75, rate_func=ease_in)
        drop(self, pack)
        pg = apage(2)
        self.play(FadeIn(pg, scale=1.3), run_time=rt * 0.2)
        lr = l_rules()
        rt = guard(self, 0.4)
        self.play(FadeIn(lr), run_time=rt)
        until(self, "come out of the code", lead=0.3)
        cards = rcards()
        srcs = [c.copy().scale(0.25).move_to(CAB_IN) for c in cards]
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[Transform(s_, c) for s_, c in zip(srcs, cards)], lag_ratio=0.18), run_time=rt)
        drop(self, *srcs)
        self.add(cards)
        until(self, "citing its file", lead=0.3)
        th = VGroup(*[thread(k) for k in range(5)])
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(t) for t in th], lag_ratio=0.12), run_time=rt)
        until(self, "re-checked by a second agent", lead=0.3)
        ck = rchecks()
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[Create(c) for c in ck], lag_ratio=0.15), run_time=rt)
        until(self, "Rules that look wrong", lead=0.2)
        flag = Dot(np.array([RX[2] - 0.34, RY + 0.17, 0]), radius=0.06, color=TERRA).set_z_index(9)
        rt = guard(self, 0.4)
        self.play(FadeOut(th), cards[2][1].animate.shift(RIGHT * 0.06), GrowFromCenter(flag), run_time=rt)
        rt = guard(self, 0.6)
        moved = VGroup(cards[2], flag)
        self.play(moved.animate.move_to(RV + np.array([-0.0, 0.0, 0])), ck[2].animate.shift(RV - np.array([RX[2], RY, 0])), run_time=rt)
        until(self, "a person marks", lead=0.3)
        pills = VGroup(rpill(0, "ok"), rpill(1, "no"), rpill(2, "?"))
        cur = cursor(2.6, -0.9).set_z_index(12)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(p_, shift=UP * 0.2) for p_ in pills], lag_ratio=0.2), FadeIn(l_review()), FadeIn(cur), run_time=rt)
        until(self, "right, wrong", lead=0.2)
        rt = guard(self, 0.6)
        self.play(cur.animate.move_to(np.array([PILLS[0][0] + 0.1, PILLS[0][1] - 0.1, 0]) + np.array([0.13, -0.22, 0])), run_time=rt * 0.5)
        self.play(Indicate(cur, color=None, scale_factor=0.85), pills[0][0].animate.set_fill(BAR3), run_time=rt * 0.4)
        until(self, "decision two", lead=0.3)
        pp = P["pips"]
        rt = guard(self, 0.5)
        self.play(*light(1, pp), run_time=rt)
        rt = guard(self, 0.3)
        self.play(*unscale(1, pp), run_time=rt)
        done(self)


# ══════════════ B04: the brief, and the approval gate ══════════════
BI = rig_at(0.6, 0.25, 0.8, 1.5, 1.1)
STRIPS_X = 2.95
STRIPS_Y = [0.8, 0.2, -0.4]
GATE_X = 3.85
PILL_C = np.array([5.35, 0.3, 0.0])
P0_AT = [(-1.7, 0.95), (-1.7, 0.15)]
RY2 = 2.2


def binder():
    plinth = BI.box(-0.08, -0.08, 0, 1.66, 1.26, 0.12, DK_TOP, DK_L, DK_R, sw=2)
    body = BI.box(0, 0, 0.12, 1.5, 1.1, 0.4)
    spine = BI.quad([(0, 0.2, 0.2), (0, 0.9, 0.2), (0, 0.9, 0.44), (0, 0.2, 0.44)], BAR1, sw=0)
    return VGroup(plinth, body, spine).set_z_index(4)


BIN_TOP = BI.p(0.75, 0.55, 0.52)


def strip(k):
    y = STRIPS_Y[k]
    body = rrect(1.3, 0.42, (STRIPS_X, y), PAGE_TOP, INK, 4)
    w = (0.7, 0.9, 0.55)[k]
    bars = gbar(STRIPS_X - 0.45, STRIPS_X - 0.45 + w, y, BAR1, 8)
    return VGroup(body, bars).set_z_index(6)


def gate_parts():
    post = Line([GATE_X, -1.0, 0], [GATE_X, 1.0, 0], color=INK, stroke_width=9).set_z_index(6)
    arm = Rectangle(width=0.22, height=1.6, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([GATE_X + 0.24, 0.0, 0]).set_z_index(6)
    return post, arm


def approve_pill():
    p = rrect(1.3, 0.56, PILL_C, PAGE_TOP, BAR1, 4, r=0.28)
    return VGroup(p, check(PILL_C[0] - 0.05, PILL_C[1], 0.14, INK, 6)).set_z_index(8)


def l_brief():
    return lbl("brief", (0.6, 1.45))


def l_p0():
    return lbl("P0 rules", (-1.7, -0.55))


def l_approve():
    return lbl("approve", (5.35, 1.0))


def b04_state():
    g, P = world(3, 3, box=False)
    post, arm = gate_parts()
    arm.shift(UP * 1.4)
    pl = approve_pill()
    pl[0].set_fill(BAR3)
    p0 = VGroup(rcard(P0_AT[0], dot=True), rcard(P0_AT[1], dot=True))
    cur = cursor(PILL_C[0] + 0.15, PILL_C[1] - 0.1).set_z_index(12)
    return VGroup(g, binder(), VGroup(*[strip(k) for k in range(3)]), p0, VGroup(post, arm), pl, cur,
                  l_brief(), l_p0(), l_approve()), P


class B04_Brief(Scene):
    def construct(self):
        st, P, cards = b03_state()
        self.add(st)
        ck, pills, cur, lr, lrv = st[2], st[3], st[4], st[5], st[6]
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(ck, pills, cur, lr, lrv)), *[c.animate.scale(0.8).move_to(np.array([RX[k], RY2, 0])) for k, c in enumerate(cards)], run_time=rt)
        lb = l_brief()
        bn = binder()
        rt = guard(self, 0.6)
        self.play(FadeIn(bn, shift=UP * 0.3), FadeIn(lb), run_time=rt)
        until(self, "It reads what discovery", lead=0.3)
        flyers = [rrect(0.5, 0.62, slot_pt(i), PAGE_TOP, INK, 4).set_z_index(9) for i in range(3)]
        self.add(*flyers)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[f.animate.scale(0.4).move_to(BIN_TOP) for f in flyers], lag_ratio=0.25), run_time=rt, rate_func=ease_in)
        drop(self, *flyers)
        until(self, "phased plan", lead=0.3)
        ss = VGroup(*[strip(k) for k in range(3)])
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(s_, shift=RIGHT * 0.4) for s_ in ss], lag_ratio=0.25), run_time=rt)
        until(self, "the critical rules", lead=0.3)
        rt = guard(self, 0.9)
        self.play(FadeOut(VGroup(cards[1], cards[3], cards[4])),
                  Transform(cards[0], rcard(P0_AT[0], dot=True)), Transform(cards[2], rcard(P0_AT[1], dot=True)),
                  FadeIn(l_p0()), run_time=rt)
        until(self, "Then it stops", lead=0.2)
        post, arm = gate_parts()
        pl = approve_pill()
        rt = guard(self, 0.6)
        self.play(FadeIn(post), FadeIn(arm, shift=DOWN * 0.4), FadeIn(pl), FadeIn(l_approve()), run_time=rt)
        c0 = PILL_C + np.array([0.45, -0.9, 0])
        cur = cursor(*c0[:2]).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        until(self, "until you approve it", lead=0.2)
        rt = guard(self, 0.5)
        self.play(cur.animate.move_to(PILL_C + np.array([0.28, -0.32, 0])), run_time=rt)
        pp = P["pips"]
        rt = guard(self, 0.5)
        self.play(Indicate(cur, color=None, scale_factor=0.85), pl[0].animate.set_fill(BAR3), *light(2, pp), run_time=rt)
        rt = guard(self, 0.3)
        self.play(*unscale(2, pp), run_time=rt)
        until(self, "no objection", lead=0.2)
        rt = guard(self, 0.6)
        self.play(arm.animate.shift(UP * 1.4), run_time=rt)
        done(self)


# ══════════════ B05: three build doors ══════════════
DOORS = [-0.5, 1.9, 4.3]
DY = 0.0
DS, DW, DD, DH = 0.7, 0.6, 1.2, 1.8
BIN5 = np.array([-2.15, 0.6, 0.0])


def door(x):
    i = rig_at(x, DY, DS, DW, DD)
    body = i.box(0, 0, 0, DW, DD, DH, DK_TOP, DK_L, DK_R)
    way = i.quad([(0, 0.25, 0.05), (0, 0.95, 0.05), (0, 0.95, 1.05), (0, 0.25, 1.05)], DARK_TOP, sw=0)
    lamp = Circle(radius=0.13, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(i.p(0, DD / 2, 1.4))
    return VGroup(body, way, lamp).set_z_index(3), i.p(0, DD / 2, 0.55)


def l_door(k):
    return lbl(("uplift", "transform", "reimagine")[k], (DOORS[k], 2.0), 38)


def b05_state():
    g, P = world(3, 3, box=True)
    ds = VGroup(*[door(x)[0] for x in DOORS])
    for d in ds:
        d[2].set_fill(BAR1)
    ds[1][2].set_fill(TERRA)
    return VGroup(g, ds, l_door(0), l_door(1), l_door(2)), P, ds


class B05_Build(Scene):
    def construct(self):
        st, P = b04_state()
        self.add(st)
        bn = st[1]
        rt = guard(self, 0.8)
        self.play(FadeOut(VGroup(*[st[i] for i in range(2, 10)])), bn.animate.scale(0.7).move_to(BIN5), run_time=rt)
        until(self, "one of three methods", lead=0.3)
        ds = VGroup(*[door(x)[0] for x in DOORS])
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.4) for d in ds], lag_ratio=0.2), run_time=rt)
        for k, phrase in enumerate(("Uplift keeps", "Transform rewrites", "Reimagine rebuilds")):
            until(self, phrase, lead=0.2)
            rt = guard(self, 0.45)
            self.play(ds[k][2].animate.set_fill(BAR1), Indicate(ds[k][0], color=None, scale_factor=1.05), FadeIn(l_door(k)), run_time=rt)
            if k == 0:
                until(self, "Java eight", lead=0.1)
                rt = guard(self, 0.4)
                self.play(Indicate(ds[0][2], color=None, scale_factor=1.6), run_time=rt)
            if k == 1:
                until(self, "keeps running", lead=0.3)
                rt = guard(self, 0.5)
                self.play(Indicate(P["lamp"], color=None, scale_factor=1.8), run_time=rt)
        until(self, "Each one reads the brief", lead=0.2)
        mouth = door(DOORS[1])[1]
        rt = guard(self, 1.0)
        self.play(MoveAlongPath(bn, ArcBetweenPoints(np.array(BIN5), mouth + LEFT * 0.35, angle=-PI / 3)), run_time=rt * 0.6)
        self.play(bn.animate.scale(0.25).move_to(mouth), run_time=rt * 0.3, rate_func=ease_in)
        drop(self, bn)
        until(self, "entry criteria as gates", lead=0.3)
        rt = guard(self, 0.4)
        self.play(ds[1][2].animate.set_fill(TERRA), run_time=rt)
        nb = newbox()
        home = np.array(nb.get_center())
        nb.scale(0.3).move_to(mouth)
        self.add(nb)
        rt = guard(self, 0.9)
        self.play(nb.animate.scale(1 / 0.3).move_to(home), run_time=rt)
        done(self)


# ══════════════ B06: verify — same inputs, byte for byte ══════════════
NB_UP = np.array([2.6, 0.35, 0.0])
NB_K = 1.25
LAMPX = [1.9 + 0.45 * i for i in range(5)]
LAMPY = -0.8
CMP = np.array([-1.2, 1.0, 0.0])
TILEX = [-1.9 + 0.38 * i for i in range(10)]
TILEY = 2.15


def box_up():
    return newbox().scale(NB_K).move_to(NB_UP)


def lamps(color=TERRA):
    return VGroup(*[Dot(P3((x, LAMPY)), radius=0.12, color=color) for x in LAMPX]).set_z_index(5)


def comparator():
    body = rrect(1.3, 0.8, CMP, DIM, INK, 4, r=0.1)
    slots = VGroup(*[Line(CMP + np.array([-0.4, y, 0]), CMP + np.array([0.4, y, 0]), color=PAGE_TOP, stroke_width=7) for y in (0.14, -0.14)])
    return VGroup(body, slots).set_z_index(6)


def l_verify():
    return step_lbl("verify")


def l_compare():
    return lbl("compare", (CMP[0], CMP[1] - 0.8))


def l_inputs():
    return lbl("new inputs", (-3.3, 2.2))


def box_left():
    b = box_up()
    return np.array([b.get_left()[0] + 0.1, NB_UP[1] + 0.1, 0.0])


def box_top():
    b = box_up()
    return np.array([NB_UP[0], b.get_top()[1] - 0.25, 0.0])


def cab_right():
    return cab_pt(1.0, 1.6) + np.array([0.15, 0.0, 0])


def b06_state():
    g, P = world(3, 3, box=False)
    return VGroup(g, box_up(), lamps(), comparator(), check(CMP[0], CMP[1] + 0.75, 0.2), l_verify(), l_compare()), P


class B06_Verify(Scene):
    def construct(self):
        st, P, ds = b05_state()
        self.add(st)
        nb = P["box"]
        lv = l_verify()
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(ds, st[2], st[3], st[4])), FadeIn(lv), run_time=rt)
        rt = guard(self, 0.8)
        self.play(nb.animate.scale(NB_K).move_to(NB_UP), run_time=rt)
        until(self, "reruns the tests from clean", lead=0.3)
        lp = lamps(BAR2)
        rt = guard(self, 0.9)
        self.play(FadeIn(lp), run_time=rt * 0.3)
        self.play(LaggedStart(*[d.animate.set_color(TERRA) for d in lp], lag_ratio=0.2), run_time=rt * 0.6)
        until(self, "get the same inputs", lead=0.3)
        ina = slip((CAB_IN[0] + 1.3, CAB_IN[1] + 0.5))
        inb = slip((NB_UP[0], box_top()[1] + 1.2))
        rt = guard(self, 0.7)
        self.play(FadeIn(ina, shift=DOWN * 0.3), FadeIn(inb, shift=DOWN * 0.3), run_time=rt * 0.4)
        self.play(ina.animate.scale(0.3).move_to(CAB_IN), inb.animate.scale(0.3).move_to(box_top()), run_time=rt * 0.5, rate_func=ease_in)
        drop(self, ina, inb)
        cm = comparator()
        rt = guard(self, 0.4)
        self.play(FadeIn(cm), FadeIn(l_compare()), run_time=rt)
        until(self, "a script compares", lead=0.3)
        oa, ob = slip(cab_right(), 0.5), slip(box_left(), 0.5)
        self.add(oa, ob)
        rt = guard(self, 0.9)
        self.play(oa.animate.scale(2.0).move_to(CMP + np.array([-1.05, 0.0, 0])), ob.animate.scale(2.0).move_to(CMP + np.array([1.05, 0.0, 0])), run_time=rt * 0.55)
        self.play(oa.animate.scale(0.3).move_to(CMP), ob.animate.scale(0.3).move_to(CMP), run_time=rt * 0.35, rate_func=ease_in)
        drop(self, oa, ob)
        ok = check(CMP[0], CMP[1] + 0.75, 0.2)
        rt = guard(self, 0.4)
        self.play(Create(ok), Indicate(cm, color=None, scale_factor=1.06), run_time=rt)
        until(self, "at least ten inputs", lead=0.3)
        tiles = VGroup(*[Square(side_length=0.28, fill_color=TILE, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=3).move_to(P3((x, TILEY)))
                         for x in TILEX]).set_z_index(9)
        li = l_inputs()
        rt = guard(self, 0.8)
        self.play(FadeOut(ok), LaggedStart(*[FadeIn(t, shift=DOWN * 0.3) for t in tiles], lag_ratio=0.08), FadeIn(li), run_time=rt)
        until(self, "nobody used", lead=0.1)
        rt = guard(self, 0.6)
        self.play(*[t.animate.scale(0.4).move_to(CAB_IN if k < 5 else box_top()) for k, t in enumerate(tiles)], FadeOut(li), run_time=rt, rate_func=ease_in)
        drop(self, tiles)
        until(self, "compares again", lead=0.5)
        ok2 = check(CMP[0], CMP[1] + 0.75, 0.2)
        rt = guard(self, 0.4)
        self.play(Create(ok2), Indicate(cm, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B07: the canary, the verdict, the signature ══════════════
VC = np.array([-2.1, 1.05, 0.0])
VSLOT = [0.5, 0.0, -0.5]
SIG_Y = -0.2


def zig():
    b = box_up()
    x0, x1 = b.get_right()[0] - 0.95, b.get_right()[0] - 0.25
    y = NB_UP[1] - 0.05
    pts = [np.array([x0 + (x1 - x0) * t, y + (0.1 if k % 2 else -0.1), 0]) for k, t in enumerate(np.linspace(0, 1, 6))]
    z = VMobject(stroke_color=INK, stroke_width=6).set_points_as_corners(pts)
    return VGroup(z, Dot(pts[-1] + np.array([0.12, 0.0, 0]), radius=0.08, color=TERRA)).set_z_index(9)


def vcard():
    body = rrect(1.3, 1.7, VC, PAGE_TOP, INK, 4, r=0.1)
    slots = VGroup(*[rrect(0.85, 0.3, VC + np.array([0.08, y, 0]), BAR3, BAR1, 3, r=0.15) for y in VSLOT])
    return VGroup(body, slots).set_z_index(6)


def vdot():
    return Dot(VC + np.array([-0.45, VSLOT[0], 0]), radius=0.08, color=TERRA).set_z_index(8)


def sig():
    base = Line([VC[0] - 0.8, SIG_Y - 0.2, 0], [VC[0] + 0.8, SIG_Y - 0.2, 0], color=BAR1, stroke_width=4)
    f = ParametricFunction(lambda t: np.array([VC[0] - 0.65 + 1.3 * t, SIG_Y + 0.14 * np.sin(11 * t) + 0.06 * np.sin(27 * t), 0]),
                           t_range=[0, 1, 0.01], color=INK, stroke_width=6)
    return VGroup(base, f).set_z_index(7)


def l_canary():
    return lbl("canary", (4.3, 1.35))


def l_proven():
    return lbl("PROVEN", (0.05, VC[1] + VSLOT[0] + 0.02), 40)


def b07_state():
    g, P = world(3, 5, box=False)
    return VGroup(g, box_up(), lamps(), vcard(), vdot(), sig(), l_verify(), l_proven()), P


class B07_Verdict(Scene):
    def construct(self):
        st, P = b06_state()
        self.add(st)
        lp, cm, ok, lcmp = st[2], st[3], st[4], st[6]
        rt = guard(self, 0.5)
        self.play(FadeOut(VGroup(cm, ok, lcmp)), run_time=rt)
        until(self, "breaks one line", lead=0.3)
        zz = zig()
        lc = l_canary()
        rt = guard(self, 0.5)
        self.play(Create(zz[0]), GrowFromCenter(zz[1]), FadeIn(lc), run_time=rt)
        until(self, "turns red", lead=0.3)
        xs = VGroup(*[cross(x, LAMPY, 0.13, 6).set_z_index(6) for x in LAMPX])
        rt = guard(self, 0.6)
        self.play(FadeOut(lp), LaggedStart(*[Create(x) for x in xs], lag_ratio=0.15), run_time=rt)
        until(self, "pin the behaviour", lead=0.2)
        lp2 = lamps()
        rt = guard(self, 0.6)
        self.play(FadeOut(zz), FadeOut(xs), FadeOut(lc), FadeIn(lp2), run_time=rt)
        until(self, "one verdict", lead=0.3)
        vc = vcard()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(vc), run_time=rt)
        until(self, "proven, partly", lead=0.2)
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(vdot()), FadeIn(l_proven()), run_time=rt)
        until(self, "partly proven, or", lead=0.1)
        rt = guard(self, 0.35)
        self.play(Indicate(vc[1][1], color=None, scale_factor=1.12), run_time=rt)
        until(self, "not proven", lead=0.1)
        rt = guard(self, 0.35)
        self.play(Indicate(vc[1][2], color=None, scale_factor=1.12), run_time=rt)
        until(self, "can't run where you work", lead=0.3)
        lamp = P["lamp"]
        rt = guard(self, 0.5)
        self.play(lamp.animate.set_color(BAR2), run_time=rt)
        until(self, "best it can get", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(vc[1][1], color=None, scale_factor=1.15), run_time=rt)
        rt = guard(self, 0.4)
        self.play(lamp.animate.set_color(TERRA), run_time=rt)
        until(self, "A person accepts", lead=0.3)
        cur = cursor(VC[0] + 1.2, SIG_Y - 0.6).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        until(self, "signs the proof", lead=0.4)
        sg = sig()
        rt = guard(self, 0.8)
        self.play(Create(sg[0]), run_time=rt * 0.2)
        self.play(Create(sg[1]), cur.animate.move_to(np.array([VC[0] + 0.62, SIG_Y - 0.2, 0])), run_time=rt * 0.7)
        until(self, "decisions four and five", lead=0.3)
        pp = P["pips"]
        rt = guard(self, 0.5)
        self.play(FadeOut(cur), *light(3, pp), *light(4, pp), run_time=rt)
        rt = guard(self, 0.3)
        self.play(*unscale(3, pp), *unscale(4, pp), run_time=rt)
        done(self)


# ══════════════ B08: harden ══════════════
FLAGS = [(-2.75, 0.75), (-2.45, 0.1), (-2.85, -0.5)]
RANK_X0 = -2.35
RANK = [(1.0, 1.5, BAR1), (0.55, 1.05, BAR1), (0.1, 0.6, BAR2)]
PC = np.array([1.2, 0.75, 0.0])


def flag(c):
    c = P3(c)
    pole = Line(c + DOWN * 0.3, c + UP * 0.3, color=INK, stroke_width=6)
    pen = Polygon(c + UP * 0.3, c + UP * 0.02, c + np.array([0.38, 0.16, 0]), fill_color=TERRA, fill_opacity=1, stroke_width=0)
    return VGroup(pole, pen).set_z_index(7)


def rank_bars():
    return VGroup(*[Rectangle(width=w, height=0.28, fill_color=col, fill_opacity=1, stroke_width=0).move_to([RANK_X0 + w / 2, y, 0])
                    for y, w, col in RANK]).set_z_index(6)


def patch_card():
    body = rrect(1.2, 0.95, PC, PAGE_TOP, INK, 4, r=0.08)
    ln = VGroup(gbar(PC[0] - 0.38, PC[0] + 0.38, PC[1] + 0.2, BAR1, 6), gbar(PC[0] - 0.38, PC[0] + 0.2, PC[1], BAR2, 6),
                gbar(PC[0] - 0.38, PC[0] + 0.3, PC[1] - 0.2, BAR1, 6))
    return VGroup(body, ln).set_z_index(9)


def l_patch():
    return lbl("patch", (PC[0], PC[1] + 0.9))


def l_apply():
    return lbl("you apply", (-1.55, -0.55))


class B08_Harden(Scene):
    def construct(self):
        st, P = b07_state()
        self.add(st)
        nb = st[1]
        lh = step_lbl("harden")
        rt = guard(self, 0.8)
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5], st[6], st[7])), nb.animate.scale(1 / NB_K).move_to(NB_HOME), FadeIn(lh), run_time=rt)
        until(self, "a security scan", lead=0.3)
        cab = P["cab"]
        top, bot = cab_pt(0.5, CHT)[1] + 0.2, cab_pt(0.5, 0.2)[1]
        x0, x1 = cab.get_left()[0] - 0.12, cab.get_right()[0] + 0.12
        scan = Line([x0, top, 0], [x1, top, 0], color=TERRA, stroke_width=8).set_z_index(4)
        rt = guard(self, 1.0)
        self.play(FadeIn(scan), run_time=rt * 0.12)
        self.play(scan.animate.move_to([(x0 + x1) / 2, bot, 0]), run_time=rt * 0.65)
        self.play(FadeOut(scan), run_time=rt * 0.12)
        until(self, "ranks what it finds", lead=0.3)
        fl = VGroup(*[flag(c) for c in FLAGS])
        rt = guard(self, 0.4)
        self.play(LaggedStart(*[GrowFromEdge(f, DOWN) for f in fl], lag_ratio=0.2), run_time=rt)
        rb = rank_bars()
        rt = guard(self, 0.6)
        self.play(FadeOut(fl), LaggedStart(*[GrowFromEdge(b, LEFT) for b in rb], lag_ratio=0.2), run_time=rt)
        until(self, "drafts a patch", lead=0.3)
        pc = patch_card()
        rt = guard(self, 0.5)
        self.play(FadeIn(pc, shift=RIGHT * 0.3), FadeIn(l_patch()), Indicate(rb[0], color=None, scale_factor=1.05), run_time=rt)
        until(self, "has the patch reviewed", lead=0.3)
        rt = guard(self, 0.4)
        rv_ck = check(PC[0] + 0.9, PC[1], 0.2)
        self.play(Create(rv_ck), run_time=rt)
        until(self, "never edits your code", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(P["lock"], color=None, scale_factor=1.25), run_time=rt)
        until(self, "You apply the patch", lead=0.3)
        cur = cursor(PC[0] + 0.3, PC[1] - 0.2).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        dest = cab_pt(0.75, 1.9)
        rt = guard(self, 0.9)
        grp = VGroup(pc, cur)
        self.play(grp.animate.scale(0.45).move_to(dest + np.array([0.25, -0.1, 0])), FadeOut(rv_ck), FadeIn(l_apply()), run_time=rt)
        until(self, "decision six", lead=0.3)
        pp = P["pips"]
        rt = guard(self, 0.5)
        self.play(*light(5, pp), run_time=rt)
        rt = guard(self, 0.3)
        self.play(*unscale(5, pp), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Folders, B01_Preflight, B02_AssessMap, B03_Rules, B04_Brief, B05_Build, B06_Verify, B07_Verdict, B08_Harden):
    _cls.play = ST.play
