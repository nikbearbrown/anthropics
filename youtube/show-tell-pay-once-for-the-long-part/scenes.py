"""
Manim scenes for show-tell-pay-once-for-the-long-part (show-tell skill, batch 2, card #11).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Prompt caching, from Anthropic's cookbook notebook (claude-cookbooks/misc/prompt_caching.ipynb):
the novel and a question ride a belt into Claude (a dark reader); with no cache every token is read
(a scan line crawls, a time meter fills); cache_control sets a bookmark and the first call writes a copy
to the cache (a shelf); the same request again comes off the shelf (the meter barely moves); in a
conversation the bookmark moves forward on its own; the price columns (normal / write / read); two
rules (an exact start; a five-minute hourglass); and explicit bookmarks placed by hand (up to four).
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










# ═════════════════════════════ the film: pay once for the long part ═════════════════════════════
# Cast: a pale BELT (the request) running into a dark READER station (Claude, one light); the novel as a
# thick BOOK block (dark cover, white page edges); questions and answers as standing CARDS (question: a
# terracotta dot; answer: a grey dot); the cache breakpoint as a terracotta BOOKMARK ribbon standing behind
# the last card; the cache as a kraft SHELF (upper left) holding a smaller copy of the prompt; a segmented
# TIME METER (lower right); a terracotta reading BEAM from Claude's light (reading from scratch); an
# HOURGLASS (the cache lifetime); three kinds of PRICE column (normal / write / read) on a kraft slab.
DEV_EDGE = "#917A55"      # dark kraft outline for SMALL objects only (grey 117 < GATE T's 120)
SHADOW = "#AFA28A"
BELT = "#E6DFD3"

W = Iso(-4.6, -2.65, 0.6)          # the wide rig: belt, book, reader
BL, BWD = 10.6, 1.8               # belt length (x) and width (y)
BK = (0.7, 0.25, 3.8, 1.3, 0.8)   # book: x0, y0, length, depth, height
Q1X = 5.1                         # the question card's plane
BMX = 5.6                         # the bookmark's plane (just behind the last card)
RX = 10.6                         # the reader station's front face
SH = Iso(-5.05, 0.7, 0.4)        # the shelf rig (the cache): same drawing, two-thirds size
K = 0.4 / 0.6


def belt(iso=W, x0=0.0, x1=BL, w=BWD, th=0.3):
    top = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, w, 0), (x0, w, 0)], BELT, stroke=DIM, sw=2)
    side = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, 0, -th), (x0, 0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)   # ink edges break into
    end = iso.quad([(x0, 0, 0), (x0, w, 0), (x0, w, -th), (x0, 0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)    # "text" blobs under GATE T
    mid = DashedLine(iso.p(x0 + 0.3, w / 2, 0), iso.p(x1 - 0.3, w / 2, 0), color=GHOST, stroke_width=3, dash_length=0.12)  # GHOST: DIM dashes read as type under GATE T
    g = VGroup(side, end, top, mid)
    g.set_z_index(-1)
    return g


def zx(x):
    """Painter's order along the belt: smaller x is nearer the viewer, so it draws on top."""
    return 4.0 - 0.2 * x


def book(iso=W, x0=BK[0], y0=BK[1], L=BK[2], D=BK[3], H=BK[4], z0=0.02):
    """The novel: a thick block, dark cover on top, white page edges on the two visible sides."""
    x1, y1, z1 = x0 + L, y0 + D, z0 + H
    body = iso.box(x0, y0, z0, L, D, H, DARK_TOP, PAGE_L, PAGE_R)
    band = VGroup(iso.quad([(x0, y0, z1 - 0.12), (x0, y1, z1 - 0.12), (x0, y1, z1), (x0, y0, z1)], DARK_L, sw=2),
                  iso.quad([(x0, y0, z1 - 0.12), (x1, y0, z1 - 0.12), (x1, y0, z1), (x0, y0, z1)], DARK_R, sw=2))
    edges = VGroup()
    for f in (0.25, 0.45, 0.65):
        z = z0 + (H - 0.12) * f
        edges.add(Line(iso.p(x0 + 0.1, y0, z), iso.p(x1 - 0.1, y0, z), color=BAR3, stroke_width=3))
        edges.add(Line(iso.p(x0, y0 + 0.08, z), iso.p(x0, y1 - 0.08, z), color=BAR3, stroke_width=3))
    return VGroup(body, edges, band).set_z_index(zx(x0 + L) + 0.05)


def card(iso, xc, question=True, y0=0.2, y1=1.6, z0=0.02, z1=1.5, z=None):
    """A message standing on its edge in the plane x = xc. Question: terracotta dot; answer: grey dot."""
    body = iso.quad([(xc, y0, z0), (xc, y1, z0), (xc, y1, z1), (xc, y0, z1)], PAGE_TOP, stroke=DIM, sw=2.5)
    lines = VGroup(*[Line(iso.p(xc, y0 + 0.2, z1 - f), iso.p(xc, y1 - 0.2 - 0.3 * (k % 2), z1 - f), color=BAR2, stroke_width=4)
                     for k, f in enumerate((0.45, 0.72))])
    dot = Dot(iso.p(xc, y1 - 0.25, z1 - 0.2), radius=max(0.05, 0.11 * iso.s), color=TERRA if question else BAR1)
    return VGroup(body, lines, dot).set_z_index(zx(xc) if z is None else z)


def bookmark(iso, xb, yc=0.9, w=0.7, z0=0.02, z1=2.05, z=None):
    """The cache breakpoint: a terracotta ribbon standing in the plane x = xb, notched at the top."""
    pts = [(xb, yc - w / 2, z0), (xb, yc + w / 2, z0), (xb, yc + w / 2, z1), (xb, yc, z1 - 0.3), (xb, yc - w / 2, z1)]
    return Polygon(*[iso.p(*q) for q in pts], fill_color=TERRA, fill_opacity=1, stroke_color=TERRA, stroke_width=1).set_z_index(zx(xb) if z is None else z)


def reader(iso=W, x=RX):
    """Claude: a dark station at the belt's end with a darker intake mouth and a light on top."""
    body = iso.box(x, -0.3, 0, 2.0, BWD + 0.6, 2.3, DARK_TOP, DARK_L, DARK_R)
    mouth = iso.quad([(x, 0.15, 0.02), (x, BWD - 0.15, 0.02), (x, BWD - 0.15, 1.35), (x, 0.15, 1.35)], "#4A443D", stroke=DARK_L, sw=2)
    light = Dot(iso.p(x + 0.6, BWD / 2, 2.3), radius=0.12, color=GHOST)
    body.set_z_index(6); mouth.set_z_index(6.5); light.set_z_index(7)
    return VGroup(body, mouth), light


def claude_label():
    return T("Claude", 42).move_to([3.3, 2.5, 0])


def prompt(iso=W, cards=((Q1X, True),), bm=BMX):
    """book + message cards + (optional) bookmark, drawn in `iso`."""
    g = VGroup(book(iso))
    for xc, q in cards:
        g.add(card(iso, xc, q))
    if bm is not None:
        g.add(bookmark(iso, bm))
    return g


def shelf():
    """The cache: a kraft plank with two brackets, upper left."""
    plank = SH.box(0.2, -0.3, -0.3, 9.4, 2.2, 0.3, BOX_TOP, BOX_L, BOX_R)
    br = VGroup(*[SH.quad([(x, -0.3, -0.3), (x + 1.1, -0.3, -0.3), (x, -0.3, -1.5)], BOX_R, sw=3) for x in (1.2, 6.8)])
    g = VGroup(br, plank)
    g.set_z_index(1)
    return g


def _shelf_point(pt):
    # a screen point of the belt rig -> the same local point in the shelf rig
    return np.array([SH.ox + (pt[0] - W.ox) * K, SH.oy + (pt[1] - W.oy) * K + 0.02 * SH.s, 0.0])


def fly_to_shelf(mob):
    """A copy of `mob` that can be animated up to the shelf (move and scale, never Transform)."""
    return mob.copy(), _shelf_point(np.array(mob.get_center()))


def read_beam(self, light, x0, x1, rt, *extra, z=0.84):
    """Reading from scratch: a terracotta beam from Claude's light to a spot that crawls along the prompt.
    The crawl AND its fade-out are guarded as one span, so the beam is never on screen at the clip midpoint."""
    FADE = 0.25
    tot = guard(self, rt + FADE)
    spot = Dot(W.p(x0, BWD / 2, z), radius=0.09, color=TERRA).set_z_index(9)
    beam = always_redraw(lambda: Line(np.array(light.get_center()), np.array(spot.get_center()), color=TERRA, stroke_width=5).set_z_index(8))
    self.add(beam, spot)
    Scene.play(self, spot.animate.move_to(W.p(x1, BWD / 2, z)), *extra, run_time=max(0.3, tot - FADE), rate_func=linear)
    beam.clear_updaters()
    Scene.play(self, FadeOut(beam), FadeOut(spot), run_time=FADE)


MET_X, MET_Y0, SEG_H, SEG_G, SEG_W = 5.3, -3.05, 0.36, 0.1, 1.25


def meter():
    segs = VGroup(*[RoundedRectangle(width=SEG_W, height=SEG_H, corner_radius=0.06, fill_color=CARD, fill_opacity=1,
                                     stroke_color=DIM, stroke_width=3).move_to([MET_X, MET_Y0 + SEG_H / 2 + k * (SEG_H + SEG_G), 0])
                  for k in range(10)])
    base = RoundedRectangle(width=SEG_W + 0.5, height=0.22, corner_radius=0.08, fill_color=BOX_R, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to([MET_X, MET_Y0 - 0.2, 0])
    return VGroup(base, segs)


def fill(m, n):
    return [m[1][k].animate.set_fill(BAR1) for k in range(n)]


def value(s):
    return T(s, 44).move_to([MET_X, 1.95, 0])


def wide_base(lit=True):
    b = belt()
    body, light = reader()
    if lit:
        light.set_color(TERRA)
    return b, body, light


def answer_slip():
    c = np.array([3.35, 0.75, 0])
    body = RoundedRectangle(width=1.3, height=0.72, corner_radius=0.1, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    ln = Line(c + np.array([-0.4, 0.05, 0]), c + np.array([0.4, 0.05, 0]), color=BAR1, stroke_width=6)
    return VGroup(body, ln).set_z_index(8)


# ─────────────── B00: the novel and the question go to Claude together ───────────────
class B00_Book(Scene):
    def construct(self):
        b = belt()
        self.play(FadeIn(b[0:3]), Create(b[3]), run_time=0.8)
        until(self, "a whole novel", lead=0.5)
        bk = book()
        sh = W.quad([(BK[0] - 0.15, BK[1] - 0.2, 0.01), (BK[0] + BK[2] + 0.25, BK[1] - 0.2, 0.01),
                     (BK[0] + BK[2] + 0.25, BK[1] + BK[3], 0.01), (BK[0] - 0.15, BK[1] + BK[3], 0.01)], SHADOW, sw=0).set_z_index(0)
        rt = guard(self, 0.6)
        bk.shift(UP * 4.5)
        self.add(bk)
        self.play(bk.animate.shift(DOWN * 4.5), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(sh), Indicate(bk, color=None, scale_factor=1.03), run_time=0.4)
        until(self, "about a hundred", lead=0.4)
        self.play(FadeIn(T("~187k tokens", 42).move_to([-1.0, -2.1, 0])), run_time=0.35)
        until(self, "one short question", lead=0.3)
        q = card(W, Q1X)
        rt = guard(self, 0.5)
        q.shift(UP * 4)
        self.add(q)
        self.play(q.animate.shift(DOWN * 4), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(T("question", 42).move_to([-3.7, 0.95, 0])), run_time=0.3)
        until(self, "go to Claude together", lead=0.4)
        body, light = reader()
        rt = guard(self, 0.6)
        body.shift(UP * 5); light.shift(UP * 5)
        self.add(body, light)
        self.play(VGroup(body, light).animate.shift(DOWN * 5), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(claude_label()), run_time=0.3)
        until(self, "in one request", lead=0.3)
        self.play(light.animate.set_color(TERRA), Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3),
                  VGroup(bk, q).animate.shift(W.v(0.35, 0, 0)), sh.animate.shift(W.v(0.35, 0, 0)), run_time=0.6)
        done(self)


# ─────────────── B01: no caching: every token read, every call ───────────────
class B01_Slow(Scene):
    def construct(self):
        b, body, light = wide_base()
        pr = VGroup(book(), card(W, Q1X)).shift(W.v(0.35, 0, 0))
        self.add(b, body, light, pr, claude_label())
        until(self, "every one of those tokens", lead=0.5)
        m = meter()
        rt = guard(self, 0.5)
        self.play(FadeIn(m, shift=UP * 0.2), run_time=rt)
        read_beam(self, light, 1.2, Q1X + 0.35, 2.9, LaggedStart(*fill(m, 10), lag_ratio=0.9))
        self.play(FadeIn(value("4.89 s")), run_time=0.3)
        until(self, "just to answer", lead=0.4)
        a = answer_slip()
        rt = guard(self, 0.5)
        self.play(FadeIn(a, shift=RIGHT * 0.4), Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=rt)
        until(self, "the book's title", lead=0.2)
        self.play(Indicate(a, color=None, scale_factor=1.08), run_time=0.4)
        done(self)


# ─────────────── B02: one field, cache_control: the bookmark; the first call writes the cache ───────────────
def cache_label():
    return T("cache", 42).move_to([-5.5, -0.15, 0])


class B02_Write(Scene):
    def construct(self):
        b, body, light = wide_base()
        pr = VGroup(book(), card(W, Q1X)).shift(W.v(0.35, 0, 0))
        m = meter()
        for k in range(10):
            m[1][k].set_fill(BAR1)
        old = value("4.89 s")
        self.add(b, body, light, pr, m, old)
        until(self, "add one field", lead=0.3)
        self.play(*[m[1][k].animate.set_fill(CARD) for k in range(10)], FadeOut(old), run_time=0.5)
        until(self, "cache control", lead=0.5)
        bm = bookmark(W, BMX + 0.35)
        rt = guard(self, 0.5)
        bm.shift(UP * 4)
        self.add(bm)
        self.play(bm.animate.shift(DOWN * 4), run_time=rt, rate_func=ease_in)
        cc = T("cache_control", 40).move_to([-2.6, 1.3, 0])
        self.play(FadeIn(cc), run_time=0.3)
        until(self, "still reads everything", lead=0.5)
        read_beam(self, light, 1.2, BMX + 0.35, 2.2, LaggedStart(*fill(m, 9), lag_ratio=0.9))
        until(self, "to the cache", lead=0.8)
        sf = shelf()
        rt = guard(self, 0.5)
        self.play(FadeIn(sf, shift=DOWN * 0.3), FadeOut(cc), run_time=rt)
        cp, dst = fly_to_shelf(VGroup(pr, bm))
        rt = guard(self, 0.8)
        self.play(cp.animate.scale(K).move_to(dst), run_time=rt)
        self.play(FadeIn(cache_label()), run_time=0.3)
        until(self, "Four point two eight", lead=0.3)
        self.play(FadeIn(value("4.28 s")), run_time=0.3)
        done(self)


def shelf_copy(cards=((Q1X, True),), bm=BMX, dx=0.35):
    """The prompt as it sits on the shelf (built on the belt, then moved and scaled, as fly_to_shelf does)."""
    g = prompt(W, cards, bm).shift(W.v(dx, 0, 0))
    g.scale(K).move_to(_shelf_point(np.array(g.get_center())))
    return g


def shelf_arc(sc, light):
    return DashedVMobject(ArcBetweenPoints(np.array(sc.get_right()) + RIGHT * 0.15, np.array(light.get_center()) + LEFT * 0.25, angle=-0.9)
                          .set_stroke(DIM, 5), num_dashes=18).set_z_index(9)


# ─────────────── B03: the same request again: off the shelf ───────────────
class B03_Hit(Scene):
    def construct(self):
        b, body, light = wide_base()
        sf = shelf()
        sc = shelf_copy()
        m = meter()
        for k in range(9):
            m[1][k].set_fill(BAR1)
        old = value("4.28 s")
        self.add(b, body, light, sf, sc, m, old, cache_label())
        until(self, "Send the exact same request", lead=0.2)
        self.play(*[m[1][k].animate.set_fill(CARD) for k in range(10)], FadeOut(old), run_time=0.4)
        pr = VGroup(book(), card(W, Q1X), bookmark(W, BMX)).shift(W.v(0.35, 0, 0))
        rt = guard(self, 0.8)
        pr.shift(W.v(-5.5, 0, 0) + LEFT * 0.5)
        self.add(pr)
        self.play(pr.animate.shift(W.v(5.5, 0, 0) + RIGHT * 0.5), run_time=rt)
        until(self, "Its start matches", lead=0.4)
        a = np.array(sc[0].get_bottom()) + np.array([0.0, 0.02, 0])
        z = np.array(pr[0].get_top()) + np.array([0.0, 0.05, 0])
        link = DashedLine(a, z, color=INK, stroke_width=5, dash_length=0.14).set_z_index(9)
        rt = guard(self, 0.6)
        self.play(Create(link), run_time=rt)
        mid = (a + z) / 2
        ck = check(mid[0] + 0.45, mid[1], 0.2, INK, 7).set_z_index(9)
        self.play(Create(ck), run_time=0.3)
        until(self, "comes off the shelf", lead=0.3)
        arc = shelf_arc(sc, light)
        rt = guard(self, 0.6)
        self.play(Create(arc), Indicate(sc, color=None, scale_factor=1.05), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), *fill(m, 3), run_time=rt)
        until(self, "One point four eight", lead=0.3)
        self.play(FadeOut(arc), FadeIn(value("1.48 s")), run_time=0.3)
        until(self, "three point three times", lead=0.3)
        hero = T("3.3×", 72).move_to([3.3, -1.3, 0])
        rt = guard(self, 0.4)
        self.play(FadeIn(hero, scale=1.2), run_time=rt)
        done(self)


# ─────────────── B04: a conversation: the bookmark moves forward on its own ───────────────
QX = [Q1X, 5.8, 6.5, 7.2, 7.9]          # Q1, A1, Q2, A2, Q3
BMS = [BMX, 6.95, 8.35]                 # the bookmark after turn 1, 2, 3


class B04_Turns(Scene):
    def construct(self):
        b, body, light = wide_base()
        sf = shelf()
        sc = shelf_copy(dx=0.0)
        pr = VGroup(book(), card(W, Q1X))
        bm = bookmark(W, BMX)
        self.add(b, body, light, sf, sc, cache_label(), pr, bm)
        until(self, "in a conversation", lead=0.3)
        self.play(FadeIn(T("conversation", 42).move_to([-0.55, -1.9, 0])), run_time=0.35)
        shelf_bm = sc[-1]

        def turn(i):
            a, q = card(W, QX[2 * i - 1], False), card(W, QX[2 * i], True)
            rt = guard(self, 0.6)
            for c in (a, q):
                c.shift(UP * 4)
            self.add(a, q)
            self.play(LaggedStart(a.animate.shift(DOWN * 4), q.animate.shift(DOWN * 4), lag_ratio=0.35), run_time=rt, rate_func=ease_in)
            return a, q

        def hop(x_from, x_to):
            p0 = np.array(bm.get_center())
            rt = guard(self, 0.6)
            bm.set_z_index(zx(x_to))
            self.play(MoveAlongPath(bm, ArcBetweenPoints(p0, p0 + W.v(x_to - x_from, 0, 0), angle=-1.2)), run_time=rt)

        def shelve(cards, x_from, x_to):
            moves = []
            for c in cards:
                cp, dst = fly_to_shelf(c)
                moves.append(cp.animate.scale(K).move_to(dst))
            rt = guard(self, 0.6)
            shelf_bm.set_z_index(zx(x_to))
            self.play(*moves, shelf_bm.animate.shift(SH.v(x_to - x_from, 0, 0)), run_time=rt)

        a1, q2 = turn(1)
        until(self, "the bookmark moves forward", lead=0.3)
        hop(BMS[0], BMS[1])
        until(self, "come from the cache", lead=0.4)
        arc = shelf_arc(sc, light)
        rt = guard(self, 0.6)
        self.play(Create(arc), Indicate(sc, color=None, scale_factor=1.05), run_time=rt)
        until(self, "only the new turn", lead=0.4)
        read_beam(self, light, QX[1], QX[2], 0.7, z=1.0)
        self.play(FadeOut(arc), run_time=0.2)
        shelve((a1, q2), BMS[0], BMS[1])
        until(self, "After turn one", lead=0.4)
        a2, q3 = turn(2)
        hop(BMS[1], BMS[2])
        until(self, "nearly all input", lead=0.3)
        shelve((a2, q3), BMS[1], BMS[2])
        rt = guard(self, 0.4)
        self.play(Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=rt)
        done(self)


# ─────────────── B05: the bill has the same shape ───────────────
P = Iso(-2.4, -2.3, 0.75)
COL = 1.3


def column(x, h, z0=0.0, faces=(BAR3, BAR2, BAR1)):
    return P.box(x, 0.3, z0, COL, COL, h, *faces)


def slab():
    s = P.box(-0.3, -0.4, -0.3, 9.5, 2.4, 0.3, BOX_TOP, BOX_L, BOX_R)
    s.set_z_index(-1)
    return s


def grow(col, x):
    """Grow a column up from its floor point."""
    return GrowFromPoint(col, P.p(x + COL / 2, 0.3 + COL / 2, 0))


class B05_Price(Scene):
    def construct(self):
        s = slab()
        self.play(FadeIn(s), run_time=0.5)
        until(self, "same shape", lead=0.3)
        nx, wx, rx = 0.4, 2.3, (4.4, 5.9, 7.4)
        normal = column(nx, 3.0)
        rt = guard(self, 0.6)
        self.play(grow(normal, nx), run_time=rt)
        self.play(FadeIn(T("normal", 42).move_to([-4.2, -0.5, 0])), run_time=0.3)
        until(self, "a quarter more", lead=0.5)
        wcol = column(wx, 3.0)
        extra = column(wx, 0.75, 3.1, faces=(BAR2, BAR1, "#6F7278"))
        level = DashedLine(P.p(nx, 0.3, 3.0), P.p(wx + COL + 0.3, 0.3, 3.0), color=INK, stroke_width=4, dash_length=0.12).set_z_index(5)
        rt = guard(self, 0.7)
        self.play(grow(wcol, wx), Create(level), run_time=rt)
        self.play(FadeIn(extra, shift=DOWN * 0.3), run_time=0.35)
        self.play(FadeIn(T("write", 42).move_to([0.7, 2.25, 0])), run_time=0.3)
        until(self, "Reading from it", lead=0.4)
        reads = [column(x, 0.3) for x in rx]
        dots = [Dot(P.p(x + COL / 2, 0.3 + COL / 2, 0.3), radius=0.1, color=TERRA).set_z_index(6) for x in rx]
        rt = guard(self, 0.5)
        self.play(grow(reads[0], rx[0]), run_time=rt)
        self.play(GrowFromCenter(dots[0]), FadeIn(T("read", 42).move_to([1.05, -1.55, 0])), run_time=0.35)
        until(self, "the notebook's headline", lead=0.4)
        rt = guard(self, 0.4)
        self.play(Indicate(extra, color=None, scale_factor=1.05), run_time=rt)
        until(self, "for repeated work", lead=0.6)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[AnimationGroup(grow(c, x), GrowFromCenter(d)) for c, x, d in zip(reads[1:], rx[1:], dots[1:])], lag_ratio=0.5),
                  run_time=rt)
        done(self)


# ─────────────── B06: two rules: an exact start, and a five-minute clock ───────────────
HG = np.array([4.9, -0.4, 0])     # the hourglass centre


def hourglass():
    c = HG
    hw, hh = 0.95, 1.5
    top = RoundedRectangle(width=2 * hw + 0.5, height=0.28, corner_radius=0.08, fill_color=BOX_R, fill_opacity=1,
                           stroke_color=INK, stroke_width=4).move_to(c + UP * (hh + 0.14))
    bot = top.copy().move_to(c + DOWN * (hh + 0.14))
    glass = VGroup(Polygon(c + np.array([-hw, hh, 0]), c + np.array([hw, hh, 0]), c + np.array([0.09, 0.05, 0]), c + np.array([-0.09, 0.05, 0]),
                           fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4),
                   Polygon(c + np.array([-hw, -hh, 0]), c + np.array([hw, -hh, 0]), c + np.array([0.09, -0.05, 0]), c + np.array([-0.09, -0.05, 0]),
                           fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4))
    neck = c + np.array([0, 0.09, 0])
    sand_top = Polygon(c + np.array([-hw * 0.8, hh * 0.8, 0]), c + np.array([hw * 0.8, hh * 0.8, 0]), neck,
                       fill_color=BAR1, fill_opacity=1, stroke_width=0)
    floor_pt = c + np.array([0, -hh + 0.05, 0])
    pile = Polygon(c + np.array([-hw * 0.8, -hh + 0.05, 0]), c + np.array([hw * 0.8, -hh + 0.05, 0]), c + np.array([0, -hh * 0.25, 0]),
                   fill_color=BAR1, fill_opacity=1, stroke_width=0)
    pile.scale(0.06, about_point=floor_pt)
    return VGroup(glass, sand_top, pile, top, bot), neck, floor_pt


def cross(x, y, s=0.22, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w)).set_z_index(9)


class B06_Rules(Scene):
    def construct(self):
        b, body, light = wide_base()
        sf = shelf()
        sc = shelf_copy(dx=0.0)
        self.add(b, body, light, sf, sc)
        until(self, "The start must match", lead=0.4)
        ts = VGroup(W.quad([(0.3, 0.45, 0.02), (0.3, 1.35, 0.02), (0.3, 1.35, 1.3), (0.3, 0.45, 1.3)], BOX_TOP, stroke=DEV_EDGE, sw=3),
                    Line(W.p(0.3, 0.65, 0.85), W.p(0.3, 1.15, 0.85), color=DEV_EDGE, stroke_width=4),
                    Line(W.p(0.3, 0.65, 0.55), W.p(0.3, 1.0, 0.55), color=DEV_EDGE, stroke_width=4)).set_z_index(4)
        pr = VGroup(ts, prompt(W))
        rt = guard(self, 0.8)
        pr.shift(W.v(-5.5, 0, 0) + LEFT * 0.5)
        self.add(pr)
        self.play(pr.animate.shift(W.v(5.5, 0, 0) + RIGHT * 0.5), run_time=rt)
        self.play(FadeIn(T("timestamp", 42).move_to([-2.9, -3.1, 0])), run_time=0.3)
        until(self, "every call is a miss", lead=0.6)
        a = _shelf_point(W.p(0.75, 0.9, 0.02)) + np.array([0.0, -0.3, 0])
        xm = W.p(0.3, 0.9, 1.3) + np.array([0.0, 0.75, 0])
        link = DashedLine(a, xm + UP * 0.35, color=INK, stroke_width=5, dash_length=0.14).set_z_index(9)
        rt = guard(self, 0.5)
        self.play(Create(link), run_time=rt)
        self.play(Create(cross(xm[0], xm[1])), FadeIn(T("miss", 42).move_to([xm[0] - 0.85, xm[1] - 0.02, 0])), run_time=0.35)
        until(self, "a fresh write", lead=0.4)
        read_beam(self, light, 0.3, BMX, 1.2)
        until(self, "five minutes by default", lead=0.6)
        hg, neck, floor_pt = hourglass()
        rt = guard(self, 0.5)
        self.play(FadeIn(hg, shift=UP * 0.3), run_time=rt)
        self.play(FadeIn(T("5 min", 42).move_to([HG[0], HG[1] - 2.2, 0])), run_time=0.3)
        rt = guard(self, 1.6)
        self.play(hg[1].animate.scale(0.35, about_point=neck), hg[2].animate.scale(12, about_point=floor_pt), run_time=rt, rate_func=linear)
        until(self, "every hit resets the clock", lead=0.4)
        rt = guard(self, 0.4)
        self.play(Flash(light.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), Indicate(sc, color=None, scale_factor=1.05), run_time=rt)
        self.play(hg.animate.stretch(-1, 1, about_point=HG), run_time=0.6)   # flip in place; a Rotate swept the plates across the label
        done(self)


# ─────────────── B07: explicit breakpoints: place the bookmarks yourself ───────────────
C = Iso(-4.2, -2.4, 0.9)
CQ = [4.3, 5.2, 6.1]                     # Q1, A1, Q2
SLOTS = [3.95, 4.75, 5.65, 6.55]         # after the book, after Q1, after A1, after Q2


class B07_Explicit(Scene):
    def construct(self):
        b = belt(C, -0.3, 8.8)
        bk = book(C, 0.3, 0.25, 3.3, 1.3, 0.8)
        cs = VGroup(card(C, CQ[0]), card(C, CQ[1], False), card(C, CQ[2]))
        self.add(b, bk, cs)
        self.play(FadeIn(T("system prompt", 42).move_to([-1.6, -2.55, 0])), run_time=0.4)
        until(self, "place the bookmarks yourself", lead=0.5)
        rest1, rest2 = np.array([2.7, -1.5, 0]), np.array([3.7, -1.5, 0])
        bm1, bm2 = bookmark(C, SLOTS[0], z1=2.5), bookmark(C, SLOTS[3], z1=2.5)
        home1, home2 = np.array(bm1.get_center()), np.array(bm2.get_center())
        bm1.move_to(rest1); bm2.move_to(rest2)
        cur = cursor(4.9, -2.6, 0.5).set_z_index(10)
        rt = guard(self, 0.5)
        self.play(FadeIn(bm1), FadeIn(bm2), FadeIn(cur, shift=UP * 0.3), run_time=rt)
        until(self, "puts one after the book", lead=0.3)
        rt = guard(self, 0.4)
        self.play(cur.animate.move_to(rest1 + np.array([0.15, -0.2, 0])), run_time=rt)
        rt = guard(self, 0.8)
        self.play(VGroup(bm1, cur).animate.shift(home1 - rest1), run_time=rt)
        until(self, "one on the newest question", lead=0.5)
        rt = guard(self, 0.4)
        self.play(cur.animate.move_to(rest2 + np.array([0.15, -0.2, 0])), run_time=rt)
        rt = guard(self, 0.7)
        self.play(VGroup(bm2, cur).animate.shift(home2 - rest2), run_time=rt)
        until(self, "up to four", lead=0.4)
        ghosts = VGroup(*[DashedVMobject(bookmark(C, SLOTS[k], z1=2.5).set_fill(opacity=0).set_stroke(INK, 4), num_dashes=18).set_z_index(zx(SLOTS[k]))
                          for k in (1, 2)])
        rt = guard(self, 0.5)
        self.play(Create(ghosts), cur.animate.shift(RIGHT * 1.5 + DOWN * 0.8), run_time=rt)
        self.play(FadeIn(T("up to 4", 42).move_to([1.6, 3.05, 0])), run_time=0.3)
        until(self, "start with automatic", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeOut(cur), Indicate(bm2, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Book, B01_Slow, B02_Write, B03_Hit, B04_Turns, B05_Price, B06_Rules, B07_Explicit):
    _cls.play = ST.play
