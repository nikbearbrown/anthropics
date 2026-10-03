"""
Manim scenes for show-tell-one-plugin-per-service (show-tell skill, card #7).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

anthropics/claude-tag-plugins, drawn as a wall of sockets: the team's workspace, @Claude (Claude Tag)
as a chat bubble, a crate of eighteen plugs, two plugged in (Asana, BigQuery) and reached by cords,
the inside of a plug (manifest, skill, references, scripts, and no key: the runtime brings it),
settings that add up from org to workspace to channel, read everywhere and write in one channel,
the data-viz helper turning a table into a chart, and the troubleshoot tester checking what loaded.
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





# ═════════════════════════════ the film: one plugin per service ═════════════════════════════
# Cast: a kraft WALL (the team's workspace) whose front face carries a 4 x 2 grid of SOCKETS (dark-kraft
# outlines: small ink-outlined objects fuse under GATE T), each with a light above it; kraft PLUGS that
# stick out of the wall toward the viewer; a kraft CRATE of eighteen small plugs (two grey helpers);
# the @Claude chat BUBBLE (white, DIM outline, terracotta spark) with session cards fanned behind it;
# dark-kraft CORDS from the bubble to the plugs; white request PACKETS; the opened plug (an open box)
# with a manifest tag, a SKILL page, a reference stack, a script tile and a KEY that comes from the
# RUNTIME (a dark server stack), not from the plug; the wall in three SECTIONS (org, workspace, channel);
# grey READ plugs and a dark WRITE plug; a TABLE card that becomes a CHART card; the TESTER handheld.
DEV_EDGE = "#917A55"      # dark kraft outline for small objects (outside GATE T's ink tolerance)
SHADOW = "#AFA28A"      # deep enough that the floor shadows carry Gate V contrast
PLUG_F = BOX_L            # a plug's front face (lighter than the wall face, so it reads as sticking out)
WALL_F = BOX_FLOOR          # the wall's socket face: mid kraft, for Gate V contrast
CORD = DEV_EDGE

# ── the WIDE rig: the wall of sockets ──
W = Iso(-5.6, -2.3, 0.9)
WW, WD, WH = 6.0, 0.4, 2.4
COLS = (0.9, 2.3, 3.7, 5.1)
ROWS = (1.65, 0.65)                  # top row first
ASANA, BQ, JIRA = (0, 0), (2, 0), (1, 0)   # (col, row) of the named sockets
OUT = 0.55                            # how far a plug sticks out of the wall


def edge(g, color=DEV_EDGE, w=3):
    for f in g:
        f.set_stroke(color, w)
    return g


def wall(iso=W):
    sh = iso.quad([(0.2, -0.6, 0), (WW + 0.35, -0.6, 0), (WW + 0.35, WD, 0), (0.2, WD, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return VGroup(sh, iso.box(0, 0, 0, WW, WD, WH, BOX_TOP, BOX_R, WALL_F))


def sock_xz(c, r):
    return COLS[c], ROWS[r]


def socket(c, r, iso=W):
    """[0] face, [1] slots, [2] light."""
    x, z = sock_xz(c, r)
    y = -0.005
    face = iso.quad([(x - 0.4, y, z - 0.3), (x + 0.4, y, z - 0.3), (x + 0.4, y, z + 0.3), (x - 0.4, y, z + 0.3)],
                    BOX_IN2, stroke=DEV_EDGE, sw=3)
    slots = VGroup(*[iso.quad([(x + dx - 0.035, y - 0.001, z - 0.12), (x + dx + 0.035, y - 0.001, z - 0.12),
                               (x + dx + 0.035, y - 0.001, z + 0.12), (x + dx - 0.035, y - 0.001, z + 0.12)], DEV_EDGE, sw=0)
                     for dx in (-0.15, 0.15)])
    light = Dot(iso.p(x, y, z + 0.42), radius=0.075, color=GHOST).set_z_index(1)
    face.set_z_index(0.2); slots.set_z_index(0.5)     # slots stay above the face even after the face is animated
    return VGroup(face, slots, light)


def sockets(iso=W):
    return VGroup(*[socket(c, r, iso) for r in range(2) for c in range(4)])


def sidx(c, r):
    return r * 4 + c


def plug(c, r, iso=W, kind="kraft"):
    """A plug seated in socket (c, r): a small box sticking out of the wall toward the viewer."""
    x, z = sock_xz(c, r)
    faces = {"kraft": (BOX_TOP, BOX_R, PLUG_F), "read": (BAR3, BAR2, BAR3), "write": (BAR2, BAR1, BAR1)}[kind]
    b = edge(iso.box(x - 0.3, -OUT, z - 0.24, 0.6, OUT, 0.48, *faces), DEV_EDGE, 3)
    b.set_z_index(3)
    return b


def plug_front(c, r, iso=W):
    x, z = sock_xz(c, r)
    return iso.p(x, -OUT, z)


def above_edge(t, pt, gap=0.3):
    """Sit text t above an iso x-edge point pt, clear of the edge (it rises 0.577 per unit to the right)."""
    return t.move_to(pt + UP * (gap + 0.2887 * t.width + t.height / 2))


def soft_page(iso, x0, y0, z0, w=1.1, d=1.4):
    pg = iso.page(x0, y0, z0, w, d)
    for f in pg[0]:
        f.set_stroke(DIM, 2)
    return pg


def label_above(word, c, iso=W, size=40):
    return above_edge(T(word, size), iso.p(COLS[c], WD, WH))


def wall_label():
    return above_edge(T("workspace", 42), W.p(1.3, WD, WH))


# ── the @Claude bubble ──
BUB_C = np.array([3.3, 1.75, 0])


def bubble(c=BUB_C):
    """[0] session cards behind, [1] bubble body, [2] tail, [3] spark, [4] typing dots."""
    body = RoundedRectangle(width=2.3, height=1.3, corner_radius=0.3, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    tail = Polygon(c + np.array([-0.75, -0.62, 0]), c + np.array([-0.3, -0.62, 0]), c + np.array([-0.95, -1.05, 0]),
                   fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
    tail_edge = VGroup(Line(c + np.array([-0.75, -0.65, 0]), c + np.array([-0.95, -1.05, 0]), color=DIM, stroke_width=3),
                       Line(c + np.array([-0.95, -1.05, 0]), c + np.array([-0.3, -0.65, 0]), color=DIM, stroke_width=3))
    spark = Dot(c + np.array([-0.72, 0.22, 0]), radius=0.13, color=TERRA)
    dots = VGroup(*[Dot(c + np.array([-0.15 + i * 0.36, -0.12, 0]), radius=0.09, color=BAR1) for i in range(3)])
    cards = VGroup(*[RoundedRectangle(width=2.0, height=1.1, corner_radius=0.2, fill_color=BOX_R, fill_opacity=1,
                                      stroke_color=DEV_EDGE, stroke_width=3).move_to(c + np.array([0.28 * (i + 1), 0.22 * (i + 1), 0]))
                     for i in (1, 0)])
    cards.set_z_index(0); body.set_z_index(1); tail.set_z_index(1.1); tail_edge.set_z_index(1.2)
    spark.set_z_index(2); dots.set_z_index(2)
    g = VGroup(cards, VGroup(body, tail, tail_edge), spark, dots)
    return g


def bub_port(c=BUB_C):
    """Where cords meet the bubble: its lower-left rim."""
    return c + np.array([-1.18, -0.2, 0])


def cord(c, r, bc=BUB_C):
    a = plug_front(c, r)
    b = bub_port(bc)
    return CubicBezier(a, a + np.array([0.5, -2.4, 0]), b + np.array([-2.2, -2.2, 0]), b).set_stroke(CORD, 7).set_z_index(4)


def cord_end(bc=BUB_C):
    return Dot(bub_port(bc), radius=0.09, color=TERRA).set_z_index(4)


def packet(w=0.5, h=0.34, n=2):
    card = RoundedRectangle(width=w, height=h, corner_radius=0.05, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
    lines = VGroup(*[Line([-w * 0.3, h * (0.15 - 0.3 * i), 0], [w * (0.3 - 0.15 * i), h * (0.15 - 0.3 * i), 0], color=DIM, stroke_width=4)
                     for i in range(n)])
    return VGroup(card, lines).set_z_index(6)


def ride(self, path, rt=0.8, back=False):
    rt = guard(self, rt)
    pk = packet()
    p = path.copy()
    ease = rate_functions.ease_in_out_sine
    pk.move_to(p.get_end() if back else p.get_start())
    self.add(pk)
    self.play(MoveAlongPath(pk, p), run_time=rt, rate_func=(lambda t: 1 - ease(t)) if back else ease)
    self.remove(pk)


# ── the crate of plugs ──
CR = Iso(1.9, -3.1, 0.8)
CW, CD, CH = 3.0, 1.9, 0.4


def crate_slot(i, j):
    return 0.15 + i * 0.47, 0.2 + j * 0.55


HELPERS = ((5, 0), (5, 1))
PICKS = {"asana": (0, 2), "bq": (1, 2)}


def mini(i, j, helper=False):
    x, y = crate_slot(i, j)
    faces = (BAR3, BAR2, BAR1) if helper else (BOX_TOP, BOX_R, PLUG_F)
    b = edge(CR.box(x, y, 0, 0.34, 0.34, 0.5, *faces), DEV_EDGE, 2.5)
    b.set_z_index(1)
    return b


def crate_plugs():
    """18 small plugs, drawn back to front; returns (group, dict (i, j) -> plug)."""
    d = {}
    order = sorted([(i, j) for i in range(6) for j in range(3)], key=lambda ij: -(sum(crate_slot(*ij))))
    for ij in order:
        d[ij] = mini(*ij, helper=ij in HELPERS)
    return VGroup(*[d[ij] for ij in order]), d


def crate():
    back, front = CR.open_box(0, 0, 0, CW, CD, CH)
    sh = CR.quad([(-0.2, -0.3, 0), (CW + 0.3, -0.3, 0), (CW + 0.3, CD, 0), (-0.2, CD, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return VGroup(sh, back), front


def lift_pos(ij):
    x, y = crate_slot(*ij)
    return CR.p(x + 0.17, y + 0.17, 0.25) + UP * 1.0


# ─────────────── B00: the wall of sockets, and @Claude ───────────────
class B00_Wall(Scene):
    def construct(self):
        wl = wall()
        wl.shift(DOWN * 6)
        self.add(wl)
        self.play(wl.animate.shift(UP * 6), run_time=0.9)
        self.play(FadeIn(wall_label()), run_time=0.3)
        until(self, "wall of sockets", lead=0.2)
        ss = sockets()
        self.play(LaggedStart(*[FadeIn(s, scale=0.7) for s in ss], lag_ratio=0.12), run_time=1.0)
        until(self, "one for each service", lead=0.2)
        self.play(LaggedStart(*[s[2].animate.set_color(TERRA) for s in ss], lag_ratio=0.1), run_time=0.7)
        self.play(*[s[2].animate.set_color(GHOST) for s in ss], run_time=0.4)
        until(self, "here's Claude Tag", lead=0.4)
        bb = bubble()
        rt = guard(self, 0.5)
        body = VGroup(bb[1], bb[2], bb[3])
        body.shift(UP * 3.5)
        self.add(body)
        self.play(body.animate.shift(DOWN * 3.5), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(T("@Claude", 42).move_to(BUB_C + np.array([0.55, -1.2, 0]))), run_time=0.3)
        until(self, "tag it in a chat thread", lead=0.3)
        self.play(FadeIn(bb[3]), run_time=0.3)
        self.play(LaggedStart(*[d.animate.shift(UP * 0.12) for d in bb[3]], lag_ratio=0.3), run_time=0.45)
        self.play(*[d.animate.shift(DOWN * 0.12) for d in bb[3]], run_time=0.3)
        until(self, "remote Claude Code sessions", lead=0.3)
        self.play(LaggedStart(*[FadeIn(c, shift=DL * 0.25) for c in bb[0]], lag_ratio=0.4), run_time=0.7)
        done(self)


def wide_base():
    """The wall, its sockets and the bubble, as B00 leaves them; labels separately."""
    labs = VGroup(wall_label(), T("@Claude", 42).move_to(BUB_C + np.array([0.55, -1.2, 0])))
    return wall(), sockets(), bubble(), labs


# ─────────────── B01: eighteen plugs in a crate ───────────────
class B01_Crate(Scene):
    def construct(self):
        wl, ss, bb, labs = wide_base()
        self.add(wl, ss, bb, labs)
        self.play(FadeOut(labs[0]), run_time=0.3)
        until(self, "lists eighteen plugins", lead=0.5)
        back, front = crate()
        cr = VGroup(back, front)
        cr.shift(DOWN * 3)
        self.add(cr)
        self.play(cr.animate.shift(UP * 3), run_time=0.5)
        grp, d = crate_plugs()
        for m in grp:
            m.shift(UP * 2.2)
        self.add(grp)
        rt = guard(self, 1.6)
        self.play(LaggedStart(*[m.animate.shift(DOWN * 2.2) for m in grp], lag_ratio=0.12), run_time=rt)
        num = T("18", 110, bold=True).move_to([5.25, -1.45, 0])
        self.play(FadeIn(num, shift=UP * 0.3), FadeIn(T("plugins", 42).move_to([5.25, -2.5, 0])), run_time=0.4)
        until(self, "Sixteen are services", lead=0.3)
        svc = [d[ij] for ij in d if ij not in HELPERS]
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[m.animate.shift(UP * 0.12) for m in svc], lag_ratio=0.08), run_time=rt)
        self.play(*[m.animate.shift(DOWN * 0.12) for m in svc], run_time=0.3)
        until(self, "The other two are helpers", lead=0.3)
        hp = VGroup(d[HELPERS[0]], d[HELPERS[1]])
        self.play(hp.animate.shift(UP * 0.45), FadeIn(T("helpers", 40).move_to([5.25, -0.35, 0])), run_time=0.45)
        self.play(hp.animate.shift(DOWN * 0.45), run_time=0.35)
        until(self, "install the services you use", lead=0.3)
        pk = d[PICKS["asana"]]
        self.play(pk.animate.move_to(lift_pos(PICKS["asana"])), run_time=0.6)
        done(self)


def b01_end():
    wl, ss, bb, labs = wide_base()
    back, front = crate()
    grp, d = crate_plugs()
    d[PICKS["asana"]].move_to(lift_pos(PICKS["asana"]))
    extra = VGroup(T("18", 110, bold=True).move_to([5.25, -1.45, 0]), T("plugins", 42).move_to([5.25, -2.5, 0]),
                   T("helpers", 40).move_to([5.25, -0.35, 0]))
    return wl, ss, bb, labs[1], VGroup(back, front), grp, d, extra


def seat(self, mob, c, r, rt=0.8):
    """Fly a small crate plug to the wall and push it into socket (c, r); returns the seated plug."""
    target = plug(c, r)
    pre = target.get_center() + W.v(0, -0.7, 0)
    rt = guard(self, rt + 0.35)
    self.play(Transform(mob, target.copy().move_to(pre)), run_time=rt - 0.35)
    self.play(mob.animate.move_to(target.get_center()), run_time=0.35)
    return mob


# ─────────────── B02: two plugs go in ───────────────
class B02_PlugIn(Scene):
    def construct(self):
        wl, ss, bb, clab, cr, grp, d, extra = b01_end()
        self.add(wl, ss, bb, clab, cr, grp, extra)
        self.play(FadeOut(extra), run_time=0.3)
        until(self, "its own plugin", lead=0.3)
        self.play(Indicate(d[PICKS["asana"]], color=None, scale_factor=1.3), run_time=0.6)
        until(self, "exactly the services it uses", lead=0.3)
        self.play(LaggedStart(*[Indicate(s[0], color=None, scale_factor=1.12) for s in ss], lag_ratio=0.1), run_time=1.0)
        until(self, "works in Asana", lead=0.5)
        a = seat(self, d[PICKS["asana"]], *ASANA)
        self.play(ss[sidx(*ASANA)][2].animate.set_color(TERRA), FadeIn(label_above("Asana", ASANA[0])), run_time=0.3)
        until(self, "keeps its data", lead=0.3)
        b = d[PICKS["bq"]]
        self.play(b.animate.move_to(lift_pos(PICKS["bq"])), run_time=0.4)
        seat(self, b, *BQ)
        self.play(ss[sidx(*BQ)][2].animate.set_color(TERRA), FadeIn(label_above("BigQuery", BQ[0])), run_time=0.3)
        until(self, "Two plugs go in", lead=0.1)
        rest = VGroup(*[m for m in grp if m is not a and m is not b])
        rt = guard(self, 0.6)
        self.play(VGroup(cr, rest).animate.shift(DOWN * 4.5), run_time=rt)
        self.remove(cr, rest)
        until(self, "Every other socket", lead=0.3)
        empty = [ss[i] for i in range(8) if i not in (sidx(*ASANA), sidx(*BQ))]
        rt = guard(self, 0.5)
        self.play(*[s[0].animate.set_fill(BOX_IN1) for s in empty], run_time=rt)
        done(self)


def plugged_base():
    """The wall with Asana and BigQuery plugged in (lights on), the bubble, labels."""
    wl, ss, bb, labs = wide_base()
    for c, r in (ASANA, BQ):
        ss[sidx(c, r)][2].set_color(TERRA)
    for i in range(8):
        if i not in (sidx(*ASANA), sidx(*BQ)):
            ss[i][0].set_fill(BOX_IN1)
    pl = VGroup(plug(*ASANA), plug(*BQ))
    return wl, ss, bb, labs[1], pl, VGroup(label_above("Asana", ASANA[0]), label_above("BigQuery", BQ[0]))


# ─────────────── B03: @Claude reaches exactly those two ───────────────
class B03_Reach(Scene):
    def construct(self):
        wl, ss, bb, clab, pl, slabs = plugged_base()
        self.add(wl, ss, bb, clab, pl, slabs)
        until(self, "tag Claude in a thread", lead=0.2)
        self.play(LaggedStart(*[d.animate.shift(UP * 0.12) for d in bb[3]], lag_ratio=0.3), run_time=0.45)
        self.play(*[d.animate.shift(DOWN * 0.12) for d in bb[3]], run_time=0.3)
        until(self, "reach those two", lead=0.4)
        c1, c2 = cord(*ASANA), cord(*BQ)
        self.play(Create(c1), Create(c2), FadeIn(cord_end()), run_time=0.8)
        until(self, "Asana tasks", lead=0.3)
        ride(self, c1, 0.8, back=True)
        until(self, "S Q L in Big Query", lead=0.3)
        ride(self, c2, 0.8, back=True)
        until(self, "Each skill activates", lead=0.3)
        pages = VGroup(*[Iso(*(plug_front(c, r)[:2] + np.array([0.35, 0.25])), 0.45).page(0, 0, 0, 1.0, 1.2) for c, r in (ASANA, BQ)])
        for pg in pages:
            for f in pg[0]:
                f.set_stroke(DIM, 2)
        for pg in pages:
            pg.set_z_index(5)
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[FadeIn(pg, shift=UP * 0.3) for pg in pages], lag_ratio=0.4), run_time=rt)
        until(self, "Ask about Jira", lead=0.3)
        jl = label_above("Jira", JIRA[0])
        tgt = plug_front(*JIRA)
        start = bub_port()
        stop = start + (tgt - start) * 0.55
        dash = DashedLine(start, stop, color=DIM, stroke_width=5, dash_length=0.14)
        self.play(FadeIn(jl), Create(dash), run_time=0.6)
        self.play(Indicate(ss[sidx(*JIRA)][0], color=None, scale_factor=1.15), run_time=0.5)
        self.play(FadeOut(dash), run_time=0.4)
        done(self)


# ─────────────── B04: inside a plug ───────────────
C = Iso(-2.9, -2.5, 1.05)          # the opened plug, close
PB = (0.0, 0.0, 0.0, 2.4, 2.0, 1.0)   # x0, y0, z0, w, d, h of the opened plug box
SRV = Iso(-5.4, 0.9, 0.7)         # the runtime: a dark server stack, far left


def key_shape(c, s=1.0, dashed=False):
    """A key lying on its side: a ring bow, a shaft, two teeth. Kraft with a dark-kraft outline."""
    bow = Circle(radius=0.26 * s, fill_color=BOX_L, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=4).move_to(c + LEFT * 0.55 * s)
    hole = Circle(radius=0.09 * s, fill_color=STAGE, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=3).move_to(c + LEFT * 0.55 * s)
    shaft = Rectangle(width=0.9 * s, height=0.14 * s, fill_color=BOX_L, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=4).move_to(c + RIGHT * 0.12 * s)
    t1 = Rectangle(width=0.12 * s, height=0.22 * s, fill_color=BOX_L, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=4).move_to(c + np.array([0.38, -0.16, 0]) * s)
    t2 = Rectangle(width=0.12 * s, height=0.16 * s, fill_color=BOX_L, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=4).move_to(c + np.array([0.18, -0.13, 0]) * s)
    g = VGroup(t1, t2, shaft, bow, hole)
    if dashed:
        return VGroup(*[DashedVMobject(m.copy().set_fill(opacity=0).set_stroke(DIM, 4), num_dashes=10) for m in (shaft, bow)])
    return g


def manifest_tag(c):
    """plugin.json as a shipping tag: white card, DIM outline, two DIM lines, a terracotta eyelet."""
    card = RoundedRectangle(width=1.3, height=0.8, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    ln = VGroup(Line(c + np.array([-0.35, 0.05, 0]), c + np.array([0.45, 0.05, 0]), color=DIM, stroke_width=5),
                Line(c + np.array([-0.35, -0.17, 0]), c + np.array([0.25, -0.17, 0]), color=DIM, stroke_width=5))
    eye = Dot(c + np.array([-0.47, 0.22, 0]), radius=0.07, color=TERRA)
    return VGroup(card, ln, eye).set_z_index(5)


def script_tile(c):
    """A small grey block with a prompt chevron (DIM): the scripts/ helpers."""
    iso = Iso(c[0], c[1], 0.8)
    body = edge(iso.box(0, 0, 0, 0.9, 0.9, 0.35, BAR3, BAR2, BAR1), DEV_EDGE, 3)
    chev = VGroup(Line(iso.p(0.2, 0.55, 0.351), iso.p(0.35, 0.45, 0.351), color=CARD, stroke_width=5),
                  Line(iso.p(0.35, 0.45, 0.351), iso.p(0.2, 0.3, 0.351), color=CARD, stroke_width=5))
    return VGroup(body, chev).set_z_index(5)


PARTS_AT = {"tag": np.array([0.9, 2.1, 0]), "page": np.array([2.7, 1.0, 0]), "stack": np.array([4.6, 1.6, 0]),
            "script": np.array([5.1, -1.1, 0])}


class B04_Inside(Scene):
    def construct(self):
        x0, y0, z0, w, d, h = PB
        closed = edge(C.box(x0, y0, z0, w, d, h, BOX_TOP, BOX_IN2, BOX_FLOOR), DEV_EDGE, 4)
        sh = C.quad([(x0 - 0.2, y0 - 0.4, 0), (x0 + w + 0.4, y0 - 0.4, 0), (x0 + w + 0.4, y0 + d, 0), (x0 - 0.2, y0 + d, 0)], SHADOW, sw=0)
        sh.set_z_index(-1)
        back, front = C.open_box(x0, y0, z0, w, d, h)
        edge(back, DEV_EDGE, 5); edge(front, DEV_EDGE, 5)
        front[0].set_fill(BOX_IN2); front[1].set_fill(BOX_FLOOR)
        back[1].set_fill(BOX_IN2); back[2].set_fill(BOX_FLOOR)     # darker inside: Gate V contrast
        self.add(sh, back, front, closed)
        until(self, "Open one plug", lead=0.1)
        lid = closed[2]
        self.remove(closed)
        self.add(lid)
        self.play(lid.animate.shift(UP * 1.2 + LEFT * 0.6).rotate(0.35), run_time=0.45)
        self.play(FadeOut(lid, shift=UP * 0.3), run_time=0.3)
        mouth = C.p(x0 + w / 2, y0 + d / 2, h)
        until(self, "a manifest", lead=0.3)
        tg = manifest_tag(PARTS_AT["tag"])
        self.play(TransformFromCopy(tg.copy().scale(0.3).move_to(mouth), tg), run_time=0.6)
        self.play(FadeIn(T("plugin.json", 40).next_to(tg, UP, buff=0.3)), run_time=0.3)
        until(self, "A skill", lead=0.3)
        pg = soft_page(Iso(*(PARTS_AT["page"][:2] + np.array([-0.4, -0.7])), 0.95), 0, 0, 0, 1.1, 1.4)
        pg.set_z_index(5)
        rt = guard(self, 0.6)
        self.play(TransformFromCopy(pg.copy().scale(0.3).move_to(mouth), pg), run_time=rt)
        self.play(FadeIn(T("SKILL.md", 40).next_to(pg, DOWN, buff=0.3)), run_time=0.3)
        until(self, "A catalog of endpoints", lead=0.3)
        base = PARTS_AT["stack"][:2] + np.array([-0.4, -0.7])
        stk = VGroup(*[soft_page(Iso(base[0], base[1] + 0.16 * k, 0.8), 0, 0, 0, 1.1, 1.4) for k in range(3)])
        stk.set_z_index(5)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[TransformFromCopy(p.copy().scale(0.3).move_to(mouth), p) for p in stk], lag_ratio=0.25), run_time=rt)
        until(self, "small scripts", lead=0.3)
        sc = script_tile(PARTS_AT["script"] + np.array([-0.2, -0.3, 0]))
        rt = guard(self, 0.5)
        self.play(TransformFromCopy(sc.copy().scale(0.3).move_to(mouth), sc), run_time=rt)
        until(self, "won't find is a key", lead=0.3)
        ghost_key = key_shape(C.p(x0 + w / 2, y0 + d / 2, 0.02), 1.0, dashed=True).set_z_index(1)
        self.play(Create(ghost_key), run_time=0.5)
        until(self, "The runtime injects", lead=0.4)
        stack, lights = SRV.server(0, 0, 0, 1.3, 1.3, 0.38, 3)
        srv = VGroup(stack, lights)
        srv.shift(LEFT * 3)
        self.add(srv)
        self.play(srv.animate.shift(RIGHT * 3), FadeIn(T("runtime", 40).move_to([-5.4, 3.0, 0])), run_time=0.5)
        self.play(*[l.animate.set_color(TERRA) for l in lights], run_time=0.3)
        ky = key_shape(np.array([-5.1, 0.2, 0]), 1.3).set_z_index(7)
        pk = packet(1.0, 0.66, 3).move_to([1.2, -2.8, 0])
        self.play(FadeIn(ky, shift=RIGHT * 0.4), FadeIn(pk), run_time=0.35)
        self.play(MoveAlongPath(ky, ArcBetweenPoints(ky.get_center(), pk.get_center() + LEFT * 1.25, angle=0.9)), run_time=0.6)
        self.play(VGroup(ky, pk).animate.shift(RIGHT * 2.2), run_time=0.5)
        done(self)


# ─────────────── B05: layers add up ───────────────
L = Iso(-3.7, -2.5, 0.78)
SEC_X = (0.0, 3.6, 7.2)            # the three sections' x0
SEC_W, SEC_H, SEC_D = 3.0, 1.4, 0.3
SEC_SOCK = (0.6, 1.5, 2.4)          # socket x offsets within a section
SEC_Z = 0.7
SEC_NAMES = ("org", "workspace", "channel")


def section(k):
    x0 = SEC_X[k]
    sh = L.quad([(x0 + 0.15, -0.55, 0), (x0 + SEC_W + 0.3, -0.55, 0), (x0 + SEC_W + 0.3, SEC_D, 0), (x0 + 0.15, SEC_D, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    body = L.box(x0, 0, 0, SEC_W, SEC_D, SEC_H, BOX_TOP, BOX_R, WALL_F)
    socks = VGroup()
    for sx in SEC_SOCK:
        x, z, y = x0 + sx, SEC_Z, -0.005
        face = L.quad([(x - 0.33, y, z - 0.26), (x + 0.33, y, z - 0.26), (x + 0.33, y, z + 0.26), (x - 0.33, y, z + 0.26)],
                      BOX_IN2, stroke=DEV_EDGE, sw=3)
        slots = VGroup(*[L.quad([(x + dx - 0.03, y - 0.001, z - 0.1), (x + dx + 0.03, y - 0.001, z - 0.1),
                                 (x + dx + 0.03, y - 0.001, z + 0.1), (x + dx - 0.03, y - 0.001, z + 0.1)], DEV_EDGE, sw=0)
                         for dx in (-0.13, 0.13)])
        socks.add(VGroup(face, slots))
    return VGroup(sh, body, socks)


def sec_plug(k, s, kind="kraft"):
    x = SEC_X[k] + SEC_SOCK[s]
    faces = {"kraft": (BOX_TOP, BOX_R, PLUG_F), "read": (BAR3, BAR2, BAR3), "write": (BAR2, BAR1, BAR1)}[kind]
    b = edge(L.box(x - 0.26, -0.5, SEC_Z - 0.21, 0.52, 0.5, 0.42, *faces), DEV_EDGE, 3)
    b.set_z_index(3)
    if kind == "write":
        b.add(Dot(L.p(x, -0.5, SEC_Z), radius=0.07, color=TERRA).set_z_index(4))
    return b


def sec_label(k, size=40):
    x = SEC_X[k] + SEC_W / 2
    return above_edge(T(SEC_NAMES[k], size), L.p(x, SEC_D, SEC_H))


def chain_arrow(k):
    """A short ink chevron between section k and k+1, on the floor line (a direction, not type)."""
    a = L.p(SEC_X[k] + SEC_W + 0.12, -0.2, SEC_H * 0.5)
    b = L.p(SEC_X[k + 1] - 0.12, -0.2, SEC_H * 0.5)
    return Arrow(a, b, buff=0.05, color=DEV_EDGE, stroke_width=6, max_tip_length_to_length_ratio=0.35)


class B05_Layers(Scene):
    def construct(self):
        secs = VGroup(*[section(k) for k in range(3)])
        until(self, "come in layers", lead=0.4)
        for k in range(3):
            secs[k].shift(DOWN * 5)
        self.add(secs)
        self.play(LaggedStart(*[secs[k].animate.shift(UP * 5) for k in range(3)], lag_ratio=0.25), run_time=0.9)
        until(self, "the organization", lead=0.2)
        self.play(FadeIn(sec_label(0)), run_time=0.3)
        until(self, "a workspace", lead=0.2)
        self.play(FadeIn(sec_label(1)), FadeIn(chain_arrow(0)), run_time=0.3)
        until(self, "then a channel", lead=0.2)
        self.play(FadeIn(sec_label(2)), FadeIn(chain_arrow(1)), run_time=0.3)
        until(self, "Plugins add up", lead=0.3)
        p0 = sec_plug(0, 0)
        pre = p0.get_center() + L.v(0, -0.8, 0)
        p0.move_to(pre)
        rt = guard(self, 0.7)
        self.add(p0)
        self.play(p0.animate.move_to(sec_plug(0, 0).get_center()), run_time=0.35)
        copies = [sec_plug(1, 0), sec_plug(2, 0)]
        movers = [p0.copy() for _ in copies]
        self.add(*movers)
        self.play(*[MoveAlongPath(m, ArcBetweenPoints(p0.get_center(), c.get_center(), angle=-0.8)) for m, c in zip(movers, copies)],
                  run_time=rt)
        until(self, "can plug in more", lead=0.3)
        own = sec_plug(2, 2)
        tgt = own.get_center()
        own.move_to(tgt + L.v(0, -0.8, 0))
        self.add(own)
        rt = guard(self, 0.45)
        self.play(own.animate.move_to(tgt), run_time=rt)
        until(self, "can't unplug", lead=0.3)
        inh = movers[1]
        cur = cursor(*(inh.get_center()[:2] + np.array([0.9, -0.9])), 0.42).set_z_index(9)
        self.play(FadeIn(cur), run_time=0.2)
        self.play(cur.animate.move_to(inh.get_center() + np.array([0.12, -0.2, 0])), run_time=0.35)
        pull = L.v(0, -0.45, 0)
        self.play(inh.animate.shift(pull), cur.animate.shift(pull), run_time=0.3)
        self.play(inh.animate.shift(-pull), cur.animate.shift(-pull), run_time=0.3, rate_func=rate_functions.ease_out_bounce)
        until(self, "at the top reaches", lead=0.3)
        self.play(FadeOut(cur), *[Indicate(m, color=None, scale_factor=1.25) for m in [p0] + movers], run_time=0.6)
        done(self)


def layers_base():
    secs = VGroup(*[section(k) for k in range(3)])
    labs = VGroup(*[sec_label(k) for k in range(3)])
    arrows = VGroup(chain_arrow(0), chain_arrow(1))
    plugs = VGroup(sec_plug(0, 0), sec_plug(1, 0), sec_plug(2, 0), sec_plug(2, 2))
    return secs, labs, arrows, plugs


# ─────────────── B06: read everywhere, write in one channel ───────────────
def radius_ring(k, s):
    """A dashed DIM iso ring on the floor around section k's socket s (the blast radius)."""
    x = SEC_X[k] + SEC_SOCK[s]
    c = L.p(x, -0.6, 0)
    e = Ellipse(width=1.2 * L.s * 1.2247 * 2, height=1.2 * L.s * 0.7071 * 2).move_to(c)
    return DashedVMobject(e.set_stroke(DIM, 5), num_dashes=28).set_z_index(2)


class B06_ReadWrite(Scene):
    def construct(self):
        secs, labs, arrows, plugs = layers_base()
        self.add(secs, labs, arrows, plugs)
        until(self, "For GitHub", lead=0.2)
        self.play(*[p.animate.shift(L.v(0, -0.6, 0)).set_opacity(0) for p in plugs], run_time=0.5)
        self.remove(plugs)
        until(self, "a read-only profile", lead=0.3)
        r0 = sec_plug(0, 1, "read")
        tgt = r0.get_center()
        r0.move_to(tgt + L.v(0, -0.8, 0))
        self.add(r0)
        self.play(r0.animate.move_to(tgt), run_time=0.35)
        rl = T("read", 40).move_to(L.p(SEC_X[0] + SEC_SOCK[1], -0.5, 0) + np.array([0.2, -0.75, 0]))
        self.play(FadeIn(rl), run_time=0.25)
        until(self, "bound everywhere", lead=0.3)
        rc = [sec_plug(1, 1, "read"), sec_plug(2, 1, "read")]
        mv = [r0.copy() for _ in rc]
        self.add(*mv)
        rt = guard(self, 0.7)
        self.play(*[MoveAlongPath(m, ArcBetweenPoints(r0.get_center(), c.get_center(), angle=-0.8)) for m, c in zip(mv, rc)], run_time=rt)
        until(self, "a write profile", lead=0.3)
        wp = sec_plug(2, 2, "write")
        tgt = wp.get_center()
        wp.move_to(tgt + L.v(0, -0.9, 0))
        self.add(wp)
        rt = guard(self, 0.4)
        self.play(wp.animate.move_to(tgt), run_time=rt)
        self.play(FadeIn(T("write", 40).move_to(L.p(SEC_X[2] + SEC_SOCK[2], -0.5, 0) + np.array([1.75, -0.55, 0]))), run_time=0.25)
        until(self, "push or merge", lead=0.3)
        self.play(Indicate(secs[2][1], color=None, scale_factor=1.04), run_time=0.5)
        until(self, "limits the blast radius", lead=0.4)
        ring = radius_ring(2, 2)
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(ring), run_time=rt)
        until(self, "Plug in what you use", lead=0.3)
        empties = []
        for k in range(3):
            for s in range(3):
                if (k, s) not in ((0, 1), (1, 1), (2, 1), (2, 2)):
                    empties.append(secs[k][2][s][0])
        rt = guard(self, 0.5)
        self.play(*[e.animate.set_fill(BOX_IN1) for e in empties], run_time=rt)
        done(self)


# ─────────────── B07: a table becomes a chart ───────────────
def card(c, w, h):
    """A white card with a dark title bar (the bar carries Gate V contrast)."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    bar = Rectangle(width=w - 0.06, height=0.32, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (h / 2 - 0.19))
    return VGroup(body, bar)


TAB_C, CHT_C = np.array([-4.1, 0.55, 0]), np.array([3.7, 0.55, 0])


def table_card(c=TAB_C):
    cd = card(c, 3.0, 2.6)
    rows = VGroup()
    for i in range(5):
        y = c[1] + 0.7 - i * 0.42
        rows.add(Line([c[0] - 1.25, y, 0], [c[0] + 1.25, y, 0], color=GHOST, stroke_width=3))
        for j, (a, b) in enumerate(((-1.15, -0.45), (-0.25, 0.3), (0.5, 1.05))):
            rows.add(Line([c[0] + a, y - 0.2, 0], [c[0] + b * (0.7 + 0.3 * ((i + j) % 2)), y - 0.2, 0], color=DIM, stroke_width=5))
    return VGroup(cd, rows)


def chart_card(c=CHT_C):
    cd = card(c, 3.4, 2.6)
    base = c[1] - 1.0
    hs = (0.55, 0.9, 0.75, 1.35, 1.65)
    cols = (BAR1, BAR2, BAR1, BAR2, BAR1)
    bars = VGroup(*[Rectangle(width=0.4, height=hh, fill_color=cc, fill_opacity=1, stroke_width=0)
                    .move_to([c[0] - 1.1 + i * 0.55, base + hh / 2, 0]) for i, (hh, cc) in enumerate(zip(hs, cols))])
    axis = Line([c[0] - 1.45, base, 0], [c[0] + 1.45, base, 0], color=DIM, stroke_width=4)
    pts = [np.array([c[0] - 1.1 + i * 0.55, base + hh + 0.12, 0]) for i, hh in enumerate(hs)]
    line = VMobject().set_points_as_corners(pts).set_stroke(INK, 6)
    dot = Dot(pts[-1], radius=0.1, color=TERRA).set_z_index(4)
    return cd, bars, axis, line, dot


def file_card(c, kind):
    body = RoundedRectangle(width=0.9, height=1.1, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    if kind == "png":
        mark = Polygon(c + np.array([-0.3, -0.3, 0]), c + np.array([-0.05, 0.1, 0]), c + np.array([0.1, -0.1, 0]),
                       c + np.array([0.3, 0.15, 0]), c + np.array([0.3, -0.3, 0]), fill_color=BAR2, fill_opacity=1, stroke_width=0)
    elif kind == "svg":
        mark = CubicBezier(c + np.array([-0.3, -0.25, 0]), c + np.array([-0.1, 0.4, 0]), c + np.array([0.1, -0.4, 0]),
                           c + np.array([0.3, 0.25, 0])).set_stroke(BAR1, 5)
    else:
        mark = VGroup(Line(c + np.array([-0.1, 0.2, 0]), c + np.array([-0.28, 0, 0]), color=BAR1, stroke_width=5),
                      Line(c + np.array([-0.28, 0, 0]), c + np.array([-0.1, -0.2, 0]), color=BAR1, stroke_width=5),
                      Line(c + np.array([0.1, 0.2, 0]), c + np.array([0.28, 0, 0]), color=BAR1, stroke_width=5),
                      Line(c + np.array([0.28, 0, 0]), c + np.array([0.1, -0.2, 0]), color=BAR1, stroke_width=5))
    return VGroup(body, mark).set_z_index(3)


VZ = Iso(-0.2, -0.9, 1.0)     # the data-viz plug, centre


class B07_Chart(Scene):
    def construct(self):
        bqp = edge(Iso(-5.6, -2.6, 1.0).box(0, 0, 0, 0.8, 0.7, 0.6, BOX_TOP, BOX_L, PLUG_F), DEV_EDGE, 3)
        vz = edge(VZ.box(0, 0, 0, 1.0, 0.9, 0.75, BAR3, BAR2, BAR1), DEV_EDGE, 3)
        vz_light = Dot(VZ.p(0.5, 0.45, 0.76), radius=0.1, color=GHOST).set_z_index(4)
        self.add(bqp)
        until(self, "the two helpers", lead=0.3)
        vz.shift(DOWN * 4); vz_light.shift(DOWN * 4)
        self.add(vz, vz_light)
        self.play(VGroup(vz, vz_light).animate.shift(UP * 4), run_time=0.5)
        until(self, "a table", lead=0.4)
        tb = table_card()
        self.play(TransformFromCopy(tb.copy().scale(0.2).move_to(bqp.get_center()), tb), run_time=0.6)
        self.play(FadeIn(T("table", 42).next_to(tb, DOWN, buff=0.35)), run_time=0.3)
        until(self, "rows from Big Query", lead=0.3)
        self.play(Indicate(tb[1], color=None, scale_factor=1.05), run_time=0.5)
        until(self, "it composes", lead=0.4)
        cp = tb.copy()
        rt = guard(self, 0.7)
        self.add(cp)
        self.play(cp.animate.scale(0.25).move_to(VZ.p(0.5, 0.45, 0.9)), vz_light.animate.set_color(TERRA), run_time=rt)
        self.remove(cp)
        cd, bars, axis, line, dot = chart_card()
        self.play(FadeIn(cd, shift=LEFT * 0.4), Create(axis), run_time=0.4)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2), run_time=0.8)
        self.play(Create(line), run_time=0.5)
        self.play(FadeIn(dot, scale=1.6), FadeIn(T("chart", 42).next_to(cd, DOWN, buff=0.35)), run_time=0.3)
        until(self, "a P N G", lead=0.2)
        fc = [file_card(CHT_C + np.array([-1.2 + 1.2 * i, -2.75, 0]), k) for i, k in enumerate(("png", "svg", "html"))]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(f, shift=DOWN * 0.3) for f in fc], lag_ratio=0.45), run_time=rt)
        done(self)


# ─────────────── B08: the tester checks what loaded ───────────────
TS = Iso(0.9, -3.1, 0.9)       # the tester


def tester():
    """[0] shadow, [1] body, [2] screen, [3] probe tip."""
    sh = TS.quad([(0.0, -0.3, 0), (1.5, -0.3, 0), (1.5, 0.6, 0), (0.0, 0.6, 0)], SHADOW, sw=0)
    body = edge(TS.box(0, 0, 0, 1.2, 0.45, 1.9, BOX_TOP, BOX_IN2, BOX_FLOOR), DEV_EDGE, 3)
    scr = TS.quad([(0.15, -0.005, 0.8), (1.05, -0.005, 0.8), (1.05, -0.005, 1.7), (0.15, -0.005, 1.7)], "#FFFFFF", stroke=DIM, sw=2)
    tip = Dot(TS.p(1.2, 0.2, 1.9) + UP * 0.2, radius=0.1, color=DARK_TOP).set_z_index(6)
    return VGroup(sh, body, scr, tip)


def probe(tip_pt):
    return Line(TS.p(0.9, 0.2, 1.9), tip_pt, color=CORD, stroke_width=6).set_z_index(5)


def row_check(k):
    """A check on the tester's screen, row k (0 top)."""
    c = TS.p(0.6, -0.01, 1.45 - 0.42 * k)
    return check(c[0], c[1], 0.13, INK, 6).set_z_index(7)


class B08_Tester(Scene):
    def construct(self):
        wl, ss, bb, clab, pl, slabs = plugged_base()
        c1, c2 = cord(*ASANA), cord(*BQ)
        ce = cord_end()
        self.add(wl, ss, bb, clab, pl, slabs, c1, c2, ce)
        until(self, "is troubleshoot", lead=0.4)
        ts = tester()
        ts.shift(DOWN * 4)
        self.add(ts)
        self.play(ts.animate.shift(UP * 4), run_time=0.5)
        until(self, "Config changes", lead=0.3)
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(ce), bb.animate.shift(RIGHT * 0.25).set_opacity(0.0), FadeOut(clab), run_time=0.5)
        self.remove(bb)
        until(self, "fresh Slack thread", lead=0.4)
        nb = bubble()
        body = VGroup(nb[1], nb[2], nb[3])
        body.shift(UP * 3.5)
        rt = guard(self, 0.5)
        self.add(body)
        self.play(body.animate.shift(DOWN * 3.5), run_time=rt, rate_func=ease_in)
        c1b, c2b = cord(*ASANA), cord(*BQ)
        self.play(Create(c1b), Create(c2b), FadeIn(cord_end()), FadeIn(nb[0]), run_time=0.5)
        until(self, "run debug plugins", lead=0.3)
        tl = T("debug-plugins", 40).move_to([4.0, -2.45, 0])
        rt = guard(self, 0.4)
        self.play(FadeIn(tl), ts[2].animate.set_fill(CARD), run_time=rt)
        until(self, "which plugins actually loaded", lead=0.6)
        tip = ts[3]
        pr = probe(tip.get_center())
        self.add(pr)
        for k, (c, r) in enumerate((ASANA, BQ)):
            dest = plug_front(c, r) + np.array([0.12, -0.12, 0])
            rt = guard(self, 0.6)
            self.play(tip.animate.move_to(dest), Transform(pr, probe(dest)), run_time=rt)
            self.play(Indicate(ss[sidx(c, r)][2], color=None, scale_factor=1.8), Create(row_check(k)), run_time=0.4)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Wall, B01_Crate, B02_PlugIn, B03_Reach, B04_Inside, B05_Layers, B06_ReadWrite, B07_Chart, B08_Tester):
    _cls.play = ST.play
