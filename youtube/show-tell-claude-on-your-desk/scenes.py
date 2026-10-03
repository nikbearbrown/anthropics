"""
Manim scenes for show-tell-claude-on-your-desk (show-tell skill, card #6).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

anthropics/claude-desktop-buddy, drawn on a desk: the Claude app on a laptop, a tiny ESP32 device
beside it, the opt-in Bluetooth link, the snapshot and its recent lines, the desk pet that sleeps
and wakes, a permission prompt mirrored onto the device and approved from it, encrypted pairing,
and REFERENCE.md as a blueprint anyone can build from.
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





# ═════════════════════════════ the film: Claude on your desk ═════════════════════════════
# Cast: a kraft DESK; a kraft LAPTOP whose screen is a pale Claude window carried by a dark title bar;
# a small upright kraft DEVICE (the ESP32 stick) outlined in dark kraft (#917A55: small ink-outlined
# objects fuse under GATE T), with a dark screen, a front button, a side button and a light on top;
# the Bluetooth ARC (dashed and grey until paired, then solid ink with terracotta end dots); white
# PACKETS (snapshots) that ride the arc; the pet's face, drawn in light lines on the dark screen;
# a PROMPT card; a grey radio DONGLE; a PADLOCK; the BLUEPRINT sheet (REFERENCE.md) with two
# other makers' boards. Everything drawn on a screen plane is mapped with plane() so it lies flat on
# that face. Screen content is DIM / light, never ink, so GATE T reads only the labels as type.
DEV_EDGE = "#917A55"      # dark kraft outline for small objects (outside GATE T's ink tolerance)
SHADOW = "#BFB4A0"
KRAFT_SIDE = "#E8DCC6"
SCREEN = "#1E1B18"        # the device's dark screen
LIGHT = "#F3E9D8"         # light lines on the dark screen (the pet, the transcript)

# world geometry (desk units)
DW, DD, DZ, DT = 7.0, 2.8, 1.0, 0.2
TOP = DZ + DT
LX, LY, LW, LD, LB = 0.6, 0.5, 3.0, 1.9, 0.14      # laptop base
LT, LH = 0.12, 2.0                                   # lid thickness, lid height
LSY = LY + LD - LT                                   # the lid's screen face lies in the plane y = LSY
DX, DY, DWD, DDD, DH = 5.3, 0.7, 0.8, 0.42, 1.6     # the device


def edge(g, color=DEV_EDGE, w=3):
    for f in g:
        f.set_stroke(color, w)
    return g


def plane(mob, iso, x0, y, z0):
    """Lay a flat 2D shape (designed around ORIGIN, in desk units: right = +x, up = +z) onto the
    face plane y = const, anchored at desk point (x0, y, z0)."""
    s = iso.s
    mob.apply_matrix(np.array([[C30 * s, 0.0, 0.0], [0.5 * s, s, 0.0], [0.0, 0.0, 1.0]]), about_point=ORIGIN)
    mob.shift(iso.p(x0, y, z0))
    return mob


# ── the desk ──
def desk(iso):
    sh = iso.quad([(0.3, -0.45, 0), (DW + 0.4, -0.45, 0), (DW + 0.4, DD - 0.2, 0), (0.3, DD - 0.2, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    L = 0.24
    legs_back = VGroup(iso.box(0.15, DD - 0.4, 0, L, L, DZ, KRAFT_SIDE, BOX_L, BOX_R, sw=3),
                       iso.box(DW - 0.4, DD - 0.4, 0, L, L, DZ, KRAFT_SIDE, BOX_L, BOX_R, sw=3))
    legs_front = VGroup(iso.box(0.15, 0.15, 0, L, L, DZ, KRAFT_SIDE, BOX_L, BOX_R, sw=3),
                        iso.box(DW - 0.4, 0.15, 0, L, L, DZ, KRAFT_SIDE, BOX_L, BOX_R, sw=3))
    top = iso.box(0, 0, DZ, DW, DD, DT)
    return VGroup(sh, legs_back, legs_front, top)


# ── the laptop ──
def sp(iso, u, v):
    """A point on the laptop's screen: u across (0..1), v up (0..1)."""
    return iso.p(LX + 0.15 + u * (LW - 0.3), LSY - 0.01, TOP + LB + 0.15 + v * (LH - 0.27))


def squad(iso, u0, v0, u1, v1, fill, stroke=None, sw=0):
    pts = [sp(iso, u0, v0), sp(iso, u1, v0), sp(iso, u1, v1), sp(iso, u0, v1)]
    return Polygon(*pts, fill_color=fill, fill_opacity=1, stroke_color=stroke or fill, stroke_width=sw)


def sline(iso, u0, u1, v, color=DIM, w=5):
    return Line(sp(iso, u0, v), sp(iso, u1, v), color=color, stroke_width=w)


def laptop(iso):
    """[0] base, [1] keyboard well, [2] lid, [3] screen, [4] title bar, [5] spark."""
    base = iso.box(LX, LY, TOP, LW, LD, LB)
    kb = iso.quad([(LX + 0.3, LY + 0.25, TOP + LB), (LX + LW - 0.3, LY + 0.25, TOP + LB),
                   (LX + LW - 0.3, LY + LD - 0.5, TOP + LB), (LX + 0.3, LY + LD - 0.5, TOP + LB)], BOX_IN1, stroke=DIM, sw=2)
    lid = iso.box(LX, LSY, TOP + LB, LW, LT, LH)
    screen = squad(iso, 0, 0, 1, 1, CARD)
    bar = squad(iso, 0, 0.85, 1, 1, DARK_TOP)
    spark = Dot(sp(iso, 0.06, 0.925), radius=0.07 * iso.s, color=TERRA)
    return VGroup(base, kb, lid, screen, bar, spark)


def lap_pt(iso):
    """Where the arc leaves the laptop: just above the lid's top right corner."""
    return iso.p(LX + LW, LSY + LT / 2, TOP + LB + LH) + UP * 0.2


# ── the device ──
def dp(iso, u, v):
    """A point on the device's screen."""
    return iso.p(DX + 0.1 + u * (DWD - 0.2), DY - 0.01, TOP + 0.45 + v * (DH - 0.57))


PET_C = (DX + DWD / 2, TOP + 0.45 + 0.74 * (DH - 0.57))   # the pet's centre on the screen plane (x, z)


def pet(iso, mood="asleep"):
    """The pet, drawn in light lines on the dark screen: [0] body, [1] eyes."""
    body = VGroup(Circle(radius=0.2, stroke_color=LIGHT, stroke_width=5),
                  Line([-0.13, -0.26, 0], [-0.07, -0.18, 0], color=LIGHT, stroke_width=5),
                  Line([0.13, -0.26, 0], [0.07, -0.18, 0], color=LIGHT, stroke_width=5))
    body = plane(body, iso, PET_C[0], DY - 0.02, PET_C[1])
    return VGroup(body, eyes(iso, mood))


def eyes(iso, mood):
    if mood == "asleep":
        g = VGroup(Line([-0.12, 0.02, 0], [-0.03, 0.02, 0], color=LIGHT, stroke_width=5),
                   Line([0.03, 0.02, 0], [0.12, 0.02, 0], color=LIGHT, stroke_width=5))
    elif mood == "impatient":
        g = VGroup(Circle(radius=0.042, stroke_width=0, fill_color=LIGHT, fill_opacity=1).move_to([-0.075, 0.0, 0]),
                   Circle(radius=0.042, stroke_width=0, fill_color=LIGHT, fill_opacity=1).move_to([0.075, 0.0, 0]),
                   Line([-0.13, 0.1, 0], [-0.04, 0.07, 0], color=LIGHT, stroke_width=5),
                   Line([0.13, 0.1, 0], [0.04, 0.07, 0], color=LIGHT, stroke_width=5))
    elif mood == "happy":
        g = VGroup(Arc(radius=0.045, start_angle=0, angle=PI, stroke_color=LIGHT, stroke_width=5).move_to([-0.075, 0.03, 0]),
                   Arc(radius=0.045, start_angle=0, angle=PI, stroke_color=LIGHT, stroke_width=5).move_to([0.075, 0.03, 0]))
    else:   # awake
        g = VGroup(Circle(radius=0.03, stroke_width=0, fill_color=LIGHT, fill_opacity=1).move_to([-0.075, 0.02, 0]),
                   Circle(radius=0.03, stroke_width=0, fill_color=LIGHT, fill_opacity=1).move_to([0.075, 0.02, 0]))
    return plane(g, iso, PET_C[0], DY - 0.02, PET_C[1])


def dev_lines(iso, n=3, first=0.36, step=0.1):
    """Recent transcript lines on the device's screen (light on dark), newest at the top. They stop well short of
    the screen edges: lines that nearly cut the dark screen leave small dark islands GATE T reads as low-contrast type."""
    lens = (0.8, 0.55, 0.7, 0.45)
    return VGroup(*[Line(dp(iso, 0.22, first - i * step), dp(iso, 0.22 + lens[i % 4] * 0.68, first - i * step),
                         color=LIGHT, stroke_width=5) for i in range(n)])


def device(iso, mood="asleep"):
    """[0] shadow, [1] body, [2] screen, [3] front button (A), [4] side button (B), [5] light, [6] pet."""
    sh = iso.quad([(DX + 0.1, DY - 0.3, TOP), (DX + DWD + 0.35, DY - 0.3, TOP), (DX + DWD + 0.35, DY + DDD, TOP),
                   (DX + 0.1, DY + DDD, TOP)], SHADOW, sw=0)
    sh.set_z_index(-0.5)
    body = edge(iso.box(DX, DY, TOP, DWD, DDD, DH), DEV_EDGE, 3)
    scr = Polygon(dp(iso, 0, 0), dp(iso, 1, 0), dp(iso, 1, 1), dp(iso, 0, 1), fill_color=SCREEN, fill_opacity=1, stroke_width=0)
    a = edge(iso.box(DX + 0.24, DY - 0.06, TOP + 0.12, 0.32, 0.06, 0.2, BOX_TOP, BOX_IN1, BOX_IN2), DEV_EDGE, 2)
    b = edge(iso.box(DX - 0.06, DY + 0.1, TOP + 0.95, 0.06, 0.22, 0.3, BOX_TOP, BOX_IN1, BOX_IN2), DEV_EDGE, 2)
    led = Dot(iso.p(DX + DWD * 0.72, DY + DDD / 2, TOP + DH), radius=max(0.05, 0.075 * iso.s), color=GHOST)
    led.set_z_index(1)
    return VGroup(sh, body, scr, a, b, led, pet(iso, mood))


def dev_pt(iso):
    """Where the arc lands on the device: just above its top."""
    return iso.p(DX + DWD * 0.35, DY + DDD / 2, TOP + DH) + UP * 0.24


# ── the link ──
def link(a, b, angle=-1.2, solid=True):
    arc = ArcBetweenPoints(a, b, angle=angle)
    if solid:
        arc.set_stroke(INK, 6)
        return arc
    return DashedVMobject(arc.set_stroke(DIM, 4), num_dashes=22)


def ends(a, b, color=TERRA):
    return VGroup(Dot(a, radius=0.08, color=color), Dot(b, radius=0.08, color=color)).set_z_index(3)


def packet(w=0.62, h=0.42, n=2):
    """A snapshot: a small white card, DIM outline and DIM lines (no ink: not type)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.06, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
    lines = VGroup(*[Line([-w * 0.3, h * (0.15 - 0.3 * i), 0], [w * (0.3 - 0.15 * i), h * (0.15 - 0.3 * i), 0], color=DIM, stroke_width=4)
                     for i in range(n)])
    return VGroup(card, lines).set_z_index(6)


def ride(self, path, rt=0.9, pk=None, back=False):
    """A packet rides the arc (reverse when back=True), then leaves."""
    rt = guard(self, rt)
    pk = pk or packet()
    p = path.copy()
    ease = rate_functions.ease_in_out_sine
    pk.move_to(p.get_end() if back else p.get_start())
    self.add(pk)
    self.play(MoveAlongPath(pk, p), run_time=rt, rate_func=(lambda t: 1 - ease(t)) if back else ease)
    self.remove(pk)
    return pk


def tag(word, at, size=36):
    """A white tag with one ink word (no outline: text inside an outline trips GATE T)."""
    t = T(word, size, INK, bold=True)
    bg = RoundedRectangle(width=t.width + 0.5, height=t.height + 0.36, corner_radius=0.1, fill_color="#FFFFFF",
                          fill_opacity=1, stroke_width=0)
    g = VGroup(bg, t.move_to(bg.get_center()))
    g.move_to(at).set_z_index(7)
    return g


def heart_spots():
    top = DEVC.p(DX + DWD, DY, TOP + DH)
    return [top + np.array([0.55, 0.15, 0]), top + np.array([1.0, 0.55, 0]), top + np.array([0.6, 0.95, 0])]


def heart(c, r=0.16):
    pts = [np.array([16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t), 0]) * r / 16
           for t in np.linspace(0, TAU, 40, endpoint=False)]
    return Polygon(*pts, fill_color=TERRA, fill_opacity=1, stroke_width=0).move_to(c).set_z_index(6)


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def fit(builder, s, cx, cy):
    """A rig of scale s that puts builder(rig)'s bounding-box centre at (cx, cy)."""
    c = builder(Iso(0, 0, s)).get_center()
    return Iso(cx - c[0], cy - c[1], s)


# rigs: WIDE (the desk, B00-B01); LAPC + DEVC (the close two-shot, B02-B07)
# fixed numbers (from fit(): desk+laptop+device centred at (0.15, -0.75); laptop at (-3.95, -0.25); device at (3.35, -0.35)),
# written out so Gate A's stub, whose get_center() differs, sees the real coordinates
WIDE = Iso(-1.5994, -3.284, 0.8)
LAPC = Iso(-4.4566, -3.8905, 0.9)
DEVC = Iso(-3.0798, -8.5728, 1.55)
MINI = Iso(2.4281, -1.1891, 0.62)      # the example device, small, top right (B07)
ARC_W = dict(angle=-1.9)
ARC_C = dict(angle=-0.75)


def wide_arc(solid):
    return link(lap_pt(WIDE), dev_pt(WIDE), solid=solid, **ARC_W)


def close_arc():
    return link(lap_pt(LAPC), dev_pt(DEVC), **ARC_C)


# on-screen furniture of B01 (laptop screen, WIDE rig)
def toggle(iso, on):
    pill = squad(iso, 0.08, 0.5, 0.3, 0.64, DARK_TOP if on else GHOST)
    knob = Dot(sp(iso, 0.25 if on else 0.13, 0.57), radius=0.085 * iso.s / 0.72 * 0.72, color=TERRA if on else "#FFFFFF")
    knob.set_z_index(2)
    return VGroup(pill, knob)


def buddy_panel(iso):
    """The Hardware Buddy window: a white panel with a DIM outline, a dark Connect button."""
    panel = squad(iso, 0.42, 0.1, 0.95, 0.76, "#FFFFFF", DIM, 2)
    btn = squad(iso, 0.52, 0.2, 0.84, 0.34, DARK_TOP)
    rows = VGroup(sline(iso, 0.5, 0.86, 0.62, GHOST, 5), sline(iso, 0.5, 0.74, 0.5, GHOST, 5))
    return VGroup(panel, rows, btn)


def lab_wide(word):
    t = T(word, 42)
    if word == "device":
        return t.move_to(WIDE.p(DX + DWD, DY, TOP + DH * 0.8)).align_to(WIDE.p(DX + DWD, DY, 0) + RIGHT * 0.55, LEFT)
    if word == "developer mode":
        return T(word, 40).move_to([-4.35, 2.3, 0])
    return t.move_to(sp(WIDE, 0, 0.55)).align_to(WIDE.p(LX, LY + LD, 0) + LEFT * 0.35, RIGHT)


# ─────────────── B00: the desk ───────────────
class B00_Desk(Scene):
    def construct(self):
        d = desk(WIDE)
        d.shift(DOWN * 5)
        self.add(d)
        self.play(d.animate.shift(UP * 5), run_time=0.9)
        until(self, "A laptop runs", lead=0.4)
        lp = laptop(WIDE)
        base, lidg = VGroup(lp[0], lp[1]), VGroup(lp[2], lp[3], lp[4], lp[5])
        base.shift(UP * 2.5)
        self.add(base)
        self.play(base.animate.shift(DOWN * 2.5), run_time=0.5, rate_func=ease_in)
        self.play(GrowFromEdge(lidg, DOWN), run_time=0.5)
        self.play(FadeIn(lab_wide("Claude")), run_time=0.3)
        until(self, "Beside it sits", lead=0.4)
        dv = device(WIDE)
        dv.shift(UP * 3)
        self.add(dv)
        self.play(dv.animate.shift(DOWN * 3), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(lab_wide("device")), Indicate(VGroup(*dv[1:]), color=None, scale_factor=1.06), run_time=0.4)
        until(self, "Cowork and Claude Code", lead=0.3)
        sess = VGroup(squad(WIDE, 0.06, 0.12, 0.46, 0.74, "#FFFFFF", DIM, 2), squad(WIDE, 0.54, 0.12, 0.94, 0.74, "#FFFFFF", DIM, 2),
                      sline(WIDE, 0.12, 0.38, 0.6), sline(WIDE, 0.12, 0.3, 0.46), sline(WIDE, 0.6, 0.86, 0.6), sline(WIDE, 0.6, 0.78, 0.46))
        self.play(LaggedStart(*[FadeIn(m) for m in sess], lag_ratio=0.15), run_time=0.6)
        until(self, "over Bluetooth", lead=0.7)
        arc = wide_arc(False)
        self.play(Create(arc), FadeIn(ends(lap_pt(WIDE), dev_pt(WIDE), GHOST)), run_time=0.6)
        self.play(FadeIn(T("Bluetooth", 42).move_to(arc.get_top() + UP * 0.4)), run_time=0.3)
        done(self)


def b00_end():
    arc = wide_arc(False)
    labs = VGroup(lab_wide("Claude"), lab_wide("device"), T("Bluetooth", 42).move_to(arc.get_top() + UP * 0.4))
    sess = VGroup(squad(WIDE, 0.06, 0.12, 0.46, 0.74, "#FFFFFF", DIM, 2), squad(WIDE, 0.54, 0.12, 0.94, 0.74, "#FFFFFF", DIM, 2),
                  sline(WIDE, 0.12, 0.38, 0.6), sline(WIDE, 0.12, 0.3, 0.46), sline(WIDE, 0.6, 0.86, 0.6), sline(WIDE, 0.6, 0.78, 0.46))
    return desk(WIDE), laptop(WIDE), device(WIDE), arc, ends(lap_pt(WIDE), dev_pt(WIDE), GHOST), labs, sess


# ─────────────── B01: off by default; you opt in ───────────────
class B01_OptIn(Scene):
    def construct(self):
        d, lp, dv, arc, dots, labs, sess = b00_end()
        self.add(d, lp, dv, arc, dots, labs, sess)
        until(self, "off by default", lead=0.2)
        self.play(FadeOut(labs[2]), FadeOut(labs[0]), FadeOut(sess), arc.animate.set_stroke(GHOST), run_time=0.5)
        until(self, "Turn on developer mode", lead=0.3)
        tg = toggle(WIDE, False)
        self.play(FadeIn(tg), FadeIn(lab_wide("developer mode")), run_time=0.35)
        on = toggle(WIDE, True)
        self.play(tg[1].animate.move_to(on[1].get_center()).set_color(TERRA), tg[0].animate.set_fill(DARK_TOP), run_time=0.45)
        until(self, "open Hardware Buddy", lead=0.3)
        bp = buddy_panel(WIDE)
        self.play(FadeIn(bp, scale=0.9), run_time=0.4)
        until(self, "click connect", lead=0.5)
        btn_c = bp[2].get_center()
        cur = cursor(btn_c[0] + 1.3, btn_c[1] - 0.9, 0.4).set_z_index(8)
        self.play(FadeIn(cur), run_time=0.25)
        self.play(cur.animate.move_to(btn_c + np.array([0.15, -0.15, 0])), run_time=0.45)
        self.play(Indicate(bp[2], color=None, scale_factor=0.9), run_time=0.3)
        until(self, "pick your device", lead=0.3)
        solid = wide_arc(True)
        live = ends(lap_pt(WIDE), dev_pt(WIDE))
        rt = guard(self, 0.7)
        self.play(Indicate(VGroup(*dv[1:]), color=None, scale_factor=1.06), FadeOut(arc), FadeOut(dots), Create(solid), FadeIn(live), run_time=rt)
        until(self, "reconnects by itself", lead=0.3)
        self.play(FadeOut(cur), Indicate(live, color=None, scale_factor=1.5), run_time=0.5)
        self.play(Indicate(live, color=None, scale_factor=1.5), run_time=0.5)
        done(self)


def b01_end():
    d, lp, dv = desk(WIDE), laptop(WIDE), device(WIDE)
    on = toggle(WIDE, True)
    bp = buddy_panel(WIDE)
    return d, lp, dv, wide_arc(True), ends(lap_pt(WIDE), dev_pt(WIDE)), VGroup(lab_wide("device"), lab_wide("developer mode")), VGroup(on, bp)


# ─────────────── B02: the snapshot and the recent lines ───────────────
def lab_close(word):
    pos = {"snapshot": [0.2, 0.25, 0], "messages": [5.25, -0.35, 0], "ESP32": [5.35, 0.75, 0], "asleep": [5.35, -0.05, 0],
           "awake": [5.35, -0.05, 0], "Bash": [-3.95, -2.75, 0], "prompt": [0.2, 0.25, 0], "approve": [1.3, -1.75, 0],
           "deny": [1.35, -0.2, 0], "dongle": [1.95, -2.85, 0], "pass key": [5.2, 1.05, 0], "encrypted": [0.2, 3.0, 0]}
    return T(word, 40 if word == "messages" else 42).move_to(pos[word])


class B02_Snapshot(Scene):
    def construct(self):
        d, lp, dv, arc, dots, labs, furn = b01_end()
        self.add(d, lp, dv, arc, dots, labs, furn)
        carc = close_arc()
        cdots = ends(lap_pt(LAPC), dev_pt(DEVC))
        self.play(FadeOut(d), FadeOut(labs), FadeOut(furn), FadeOut(dv[0]), to_rig(lp, WIDE, LAPC), to_rig(VGroup(*dv[1:]), WIDE, DEVC),
                  Transform(arc, carc), Transform(dots, cdots), run_time=0.9)
        sh = device(DEVC)[0]
        self.play(FadeIn(sh), FadeIn(lab_close("snapshot")), run_time=0.3)
        until(self, "sends a snapshot", lead=0.1)
        ride(self, carc, 0.9)
        self.play(Indicate(dv[2], color=None, scale_factor=1.04), run_time=0.3)
        until(self, "every ten seconds", lead=0.2)
        ride(self, carc, 0.8)
        until(self, "how many sessions", lead=0.2)
        sess = VGroup(*[squad(LAPC, 0.06 + i * 0.31, 0.12, 0.33 + i * 0.31, 0.7, "#FFFFFF", DIM, 2) for i in range(3)])
        wdot = Dot(sp(LAPC, 0.8, 0.6), radius=0.08, color=TERRA).set_z_index(2)
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[FadeIn(s) for s in sess], lag_ratio=0.3), run_time=rt)
        self.play(FadeIn(wdot), run_time=0.25)
        until(self, "recent transcript lines", lead=0.3)
        tl = VGroup(*[sline(LAPC, 0.1 + i * 0.31, 0.28 + i * 0.31, 0.42) for i in range(3)])
        self.play(LaggedStart(*[Create(l) for l in tl], lag_ratio=0.2), run_time=0.4)
        ride(self, carc, 0.8)
        dl = dev_lines(DEVC, 3)
        self.play(LaggedStart(*[Create(l) for l in dl], lag_ratio=0.25), FadeIn(lab_close("messages")), run_time=0.5)
        until(self, "The tiny screen scrolls", lead=0.3)
        new = dev_lines(DEVC, 1)[0].copy()
        step = dp(DEVC, 0, 0.26) - dp(DEVC, 0, 0.36)
        new.shift(-step)
        new.set_opacity(0)
        self.add(new)
        self.play(new.animate.shift(step).set_opacity(1), dl[0].animate.shift(step), dl[1].animate.shift(step),
                  dl[2].animate.shift(step).set_opacity(0), run_time=0.5)
        done(self)


def close_base(mood="asleep", sessions=True, lines=True):
    """The close two-shot as B02 leaves it."""
    lp, dv = laptop(LAPC), device(DEVC, mood)
    g = VGroup(lp, dv, close_arc(), ends(lap_pt(LAPC), dev_pt(DEVC)))
    extra = VGroup()
    if sessions:
        extra.add(*[squad(LAPC, 0.06 + i * 0.31, 0.12, 0.33 + i * 0.31, 0.7, "#FFFFFF", DIM, 2) for i in range(3)])
        extra.add(*[sline(LAPC, 0.1 + i * 0.31, 0.28 + i * 0.31, 0.42) for i in range(3)])
    if lines:
        extra.add(dev_lines(DEVC, 3))
    return g, extra


# ─────────────── B03: the pet sleeps, then wakes ───────────────
class B03_PetWakes(Scene):
    def construct(self):
        g, extra = close_base("asleep")
        wdot = Dot(sp(LAPC, 0.8, 0.6), radius=0.08, color=TERRA).set_z_index(2)
        self.add(g, extra, wdot, lab_close("snapshot"), lab_close("messages"))
        dv = g[1]
        self.play(FadeOut(VGroup(*[m for m in self.mobjects if isinstance(m, Text)])), FadeOut(wdot), run_time=0.3)
        until(self, "a desk pet", lead=0.3)
        self.play(FadeIn(lab_close("ESP32")), Indicate(VGroup(*dv[1:]), color=None, scale_factor=1.04), run_time=0.5)
        until(self, "It sleeps", lead=0.4)
        slab = lab_close("asleep")
        rt = guard(self, 0.4)
        self.play(FadeIn(slab), dv[6].animate.scale(1.07), run_time=rt)
        self.play(dv[6].animate.scale(1 / 1.07), run_time=0.5)
        until(self, "Start a session", lead=0.35)
        ns = squad(LAPC, 0.22, 0.2, 0.78, 0.78, "#FFFFFF", DIM, 2.5).set_z_index(2)
        nl = VGroup(sline(LAPC, 0.3, 0.66, 0.62), sline(LAPC, 0.3, 0.55, 0.48)).set_z_index(3)
        self.play(FadeIn(ns, scale=0.85), FadeIn(nl), run_time=0.3)
        ride(self, g[2], 0.6)
        until(self, "it wakes up", lead=0.15)
        aw = eyes(DEVC, "awake")
        self.play(FadeOut(dv[6][1]), FadeIn(aw), FadeOut(slab), FadeIn(lab_close("awake")), run_time=0.3)
        done(self)


def b03_end():
    g, extra = close_base("awake")
    ns = VGroup(squad(LAPC, 0.22, 0.2, 0.78, 0.78, "#FFFFFF", DIM, 2.5).set_z_index(2),
                VGroup(sline(LAPC, 0.3, 0.66, 0.62), sline(LAPC, 0.3, 0.55, 0.48)).set_z_index(3))
    return g, extra, ns


# ─────────────── B04: a permission prompt, mirrored ───────────────
def prompt_card(iso):
    """The permission prompt in the Claude window: white card, DIM outline, two DIM lines, a dark approve key."""
    card = squad(iso, 0.14, 0.14, 0.86, 0.8, "#FFFFFF", DIM, 3).set_z_index(4)
    ln = VGroup(sline(iso, 0.22, 0.7, 0.66), sline(iso, 0.22, 0.52, 0.53)).set_z_index(5)
    key = squad(iso, 0.52, 0.22, 0.8, 0.36, DARK_TOP).set_z_index(5)
    return VGroup(card, ln, key)


def dev_prompt(iso):
    """The prompt on the device's screen: a light block with two DIM lines."""
    blk = Polygon(dp(iso, 0.06, 0.0), dp(iso, 0.94, 0.0), dp(iso, 0.94, 0.44), dp(iso, 0.06, 0.44),
                  fill_color=LIGHT, fill_opacity=1, stroke_width=0).set_z_index(2)
    ln = VGroup(Line(dp(iso, 0.16, 0.32), dp(iso, 0.8, 0.32), color=DIM, stroke_width=5),
                Line(dp(iso, 0.16, 0.18), dp(iso, 0.6, 0.18), color=DIM, stroke_width=5)).set_z_index(3)
    return VGroup(blk, ln)


class B04_Prompt(Scene):
    def construct(self):
        g, extra, ns = b03_end()
        self.add(g, extra, ns, lab_close("ESP32"), lab_close("awake"))
        lp, dv, arc = g[0], g[1], g[2]
        self.play(FadeOut(VGroup(*[m for m in self.mobjects if isinstance(m, Text)])), run_time=0.3)
        until(self, "run a Bash command", lead=0.4)
        pc = prompt_card(LAPC)
        self.play(FadeOut(ns), FadeIn(pc, scale=0.85), run_time=0.4)
        self.play(FadeIn(lab_close("Bash")), run_time=0.3)
        until(self, "The snapshot carries a prompt", lead=0.3)
        pk = packet(0.9, 0.62, 3)
        half = arc.copy().pointwise_become_partial(arc, 0, 0.5)
        pk.move_to(half.get_start())
        rt = guard(self, 0.8)
        self.add(pk)
        self.play(MoveAlongPath(pk, half), run_time=rt, rate_func=rate_functions.ease_out_sine)
        self.play(pk.animate.scale(1.5), FadeIn(lab_close("prompt")), run_time=0.35)
        until(self, "It shows up on the device", lead=0.4)
        rest = arc.copy().pointwise_become_partial(arc, 0.5, 1)
        rt = guard(self, 0.8)
        self.play(pk.animate.scale(1 / 1.5), run_time=0.2)
        self.play(MoveAlongPath(pk, rest), run_time=rt, rate_func=rate_functions.ease_in_sine)
        self.remove(pk)
        dpm = dev_prompt(DEVC)
        self.play(FadeOut(extra[-1]), FadeIn(dpm), run_time=0.3)
        until(self, "the pet gets impatient", lead=0.3)
        imp = eyes(DEVC, "impatient")
        self.play(FadeOut(dv[6][1]), FadeIn(imp), run_time=0.25)
        self.play(Wiggle(VGroup(dv[6][0], imp), scale_value=1.05, rotation_angle=0.03 * TAU), run_time=0.6)
        until(self, "Its light blinks", lead=0.2)
        led = dv[5]
        for c in (TERRA, GHOST, TERRA):
            self.play(led.animate.set_color(c).scale(1.4 if c == TERRA else 1 / 1.4), run_time=0.18)
        done(self)


def b04_end():
    g, extra = close_base("impatient", lines=False)
    g[1][5].set_color(TERRA).scale(1.4)
    return g, extra, prompt_card(LAPC), dev_prompt(DEVC)


# ─────────────── B05: approve from the device ───────────────
class B05_Approve(Scene):
    def construct(self):
        g, extra, pc, dpm = b04_end()
        self.add(g, extra, pc, dpm, lab_close("Bash"), lab_close("prompt"))
        lp, dv, arc = g[0], g[1], g[2]
        self.play(FadeOut(VGroup(*[m for m in self.mobjects if isinstance(m, Text)])), run_time=0.3)
        until(self, "Press the front button", lead=0.2)
        a = dv[3]
        push = DEVC.v(0, 0.05, 0)
        self.play(a.animate.shift(push), FadeIn(lab_close("approve")), run_time=0.25)
        self.play(a.animate.shift(-push), run_time=0.2)
        until(self, "sends back one line", lead=0.3)
        ride(self, arc, 1.0, back=True)
        once = tag("once", [-0.9, 0.2, 0])
        self.play(FadeIn(once, shift=DOWN * 0.3), run_time=0.3)
        until(self, "Once approves", lead=0.3)
        ck = check(*sp(LAPC, 0.33, 0.3)[:2], 0.2, INK, 8).set_z_index(6)
        self.play(Create(ck), dv[5].animate.set_color(GHOST).scale(1 / 1.4), FadeOut(dpm), FadeIn(dev_lines(DEVC, 3)), run_time=0.45)
        until(self, "The other button", lead=0.3)
        self.play(Indicate(dv[4], color=None, scale_factor=1.6), FadeIn(lab_close("deny")), run_time=0.5)
        until(self, "Approve quickly", lead=0.2)
        hp = eyes(DEVC, "happy")
        self.play(FadeOut(dv[6][1]), FadeIn(hp), run_time=0.25)
        hs = [heart(p + DOWN * 0.5, 0.17) for p in heart_spots()]
        self.play(LaggedStart(*[FadeIn(h, shift=UP * 0.6) for h in hs], lag_ratio=0.3), run_time=0.7)
        done(self)


# ─────────────── B06: encrypted pairing ───────────────
def dongle(c):
    """A cheap radio dongle: a small grey stick, dark-kraft outline, a metal tip."""
    iso = Iso(c[0], c[1], 0.9)
    body = edge(iso.box(0, 0, 0, 1.0, 0.36, 0.22, BAR3, BAR2, BAR1), DEV_EDGE, 2.5)
    tip = edge(iso.box(1.0, 0.05, 0.03, 0.3, 0.26, 0.16, "#FFFFFF", GHOST, BAR3), DEV_EDGE, 2)
    return VGroup(body, tip)


def padlock(c, s=1.0):
    body = RoundedRectangle(width=0.62 * s, height=0.5 * s, corner_radius=0.06 * s, fill_color=BOX_L, fill_opacity=1,
                            stroke_color=DEV_EDGE, stroke_width=4).move_to(c)
    shackle = Arc(radius=0.2 * s, start_angle=0, angle=PI, stroke_color=DEV_EDGE, stroke_width=9).move_to(c + UP * 0.33 * s)
    key = Dot(c + DOWN * 0.03 * s, radius=0.06 * s, color=DARK_TOP)
    return VGroup(shackle, body, key).set_z_index(8)


PASSKEY = "482 913"


class B06_Pairing(Scene):
    def construct(self):
        g, extra = close_base("happy")
        pc = prompt_card(LAPC)
        ck = check(*sp(LAPC, 0.33, 0.3)[:2], 0.2, INK, 8).set_z_index(6)
        hs = VGroup(*[heart(p, 0.17) for p in heart_spots()])
        once = tag("once", [-0.9, 0.2, 0])
        self.add(g, extra, pc, ck, hs, once, lab_close("approve"), lab_close("deny"))
        lp, dv, arc = g[0], g[1], g[2]
        self.play(FadeOut(VGroup(*[m for m in self.mobjects if isinstance(m, Text)])), FadeOut(hs), FadeOut(once), FadeOut(ck), FadeOut(pc),
                  run_time=0.4)
        self.play(FadeOut(dv[6][1]), FadeIn(eyes(DEVC, "awake")), run_time=0.2)
        until(self, "transcript snippets", lead=0.3)
        ride(self, arc, 0.8)
        ride(self, arc, 0.8, back=True)
        until(self, "with a cheap dongle", lead=0.4)
        dg = dongle(np.array([0.3, -2.6, 0]))
        rt = guard(self, 0.5)
        dg.shift(DOWN * 2)
        self.add(dg)
        self.play(dg.animate.shift(UP * 2), run_time=rt)
        tap = DashedLine(dg.get_top() + UP * 0.2, [0.95, 0.75, 0], color=DIM, stroke_width=4, dash_length=0.12)
        dlab = lab_close("dongle")
        self.play(Create(tap), FadeIn(dlab), run_time=0.4)
        ride(self, arc, 0.7)
        until(self, "six-digit pass key", lead=0.4)
        pk_dev = tag(PASSKEY, [5.2, 1.7, 0], 40)
        src = pk_dev.copy().scale(0.2).move_to(dp(DEVC, 0.5, 0.25))
        self.play(FadeOut(extra[-1]), TransformFromCopy(src, pk_dev), run_time=0.45)
        plab = lab_close("pass key")
        self.play(FadeIn(plab), run_time=0.3)
        until(self, "you type it into the app", lead=0.3)
        pk_app = pk_dev.copy()
        field = squad(LAPC, 0.15, 0.3, 0.85, 0.62, "#FFFFFF", DIM, 3).set_z_index(3)
        fl = sline(LAPC, 0.25, 0.75, 0.46, DIM, 6).set_z_index(4)
        self.play(FadeIn(field), FadeIn(fl), run_time=0.25)
        self.play(pk_app.animate.move_to([-0.55, 0.3, 0]), run_time=0.6)
        until(self, "encrypted from then on", lead=0.4)
        apex = arc.point_from_proportion(0.5)
        lk = padlock(apex + DOWN * 0.02, 1.0)
        self.play(FadeOut(tap), FadeOut(plab), FadeOut(dlab), FadeOut(pk_dev), FadeOut(pk_app), FadeIn(lk, scale=1.4),
                  dg.animate.shift(DOWN * 0.3).set_opacity(0.0), run_time=0.5)
        self.remove(dg)
        self.play(FadeIn(lab_close("encrypted")), lk[0].animate.shift(DOWN * 0.08), run_time=0.3)
        done(self)


# ─────────────── B07: the blueprint; build your own ───────────────
SHEET = Iso(2.0, -3.05, 0.86)
SW_, SD_ = 4.3, 3.0


def sheet():
    """REFERENCE.md as a blueprint sheet lying on the floor: white, DIM outline, ghost grid, a dark title strip."""
    pg = SHEET.quad([(0, 0, 0), (SW_, 0, 0), (SW_, SD_, 0), (0, SD_, 0)], "#FFFFFF", stroke=DIM, sw=3)
    grid = VGroup(*[Line(SHEET.p(x, 0.15, 0.001), SHEET.p(x, SD_ - 0.15, 0.001), color=GHOST, stroke_width=3) for x in np.arange(0.6, SW_, 0.6)],
                  *[Line(SHEET.p(0.15, y, 0.001), SHEET.p(SW_ - 0.15, y, 0.001), color=GHOST, stroke_width=3) for y in np.arange(0.6, SD_, 0.6)])
    strip = SHEET.quad([(0.25, 0.2, 0.002), (1.55, 0.2, 0.002), (1.55, 0.55, 0.002), (0.25, 0.55, 0.002)], DARK_TOP, sw=0)
    return VGroup(pg, grid, strip)


def board(x0, y0, w=1.3, d=0.95, chips=1):
    """A maker's board on the sheet: kraft slab, dark-kraft outline, one or two grey chips (dark chips side by side fuse under GATE T)."""
    slab = edge(SHEET.box(x0, y0, 0.01, w, d, 0.14), DEV_EDGE, 3)
    cs = VGroup(*[edge(SHEET.box(x0 + 0.25 + i * 0.55, y0 + 0.3, 0.15, 0.36, 0.36, 0.12, BAR2, BAR1, BAR1), DEV_EDGE, 2)
                  for i in range(chips)])
    return VGroup(slab, cs)


def board_pt(b):
    return b.get_top() + UP * 0.28


class B07_Blueprint(Scene):
    def construct(self):
        g, extra = close_base("awake", sessions=False, lines=False)
        lk = padlock(g[2].point_from_proportion(0.5) + DOWN * 0.1, 1.0)
        elab = lab_close("encrypted")
        self.add(g, lk, elab)
        lp, dv, arc, dots = g
        until(self, "any of this code", lead=0.4)
        self.play(FadeOut(lk), FadeOut(elab), FadeOut(arc), FadeOut(dots), FadeOut(dv[0]),
                  to_rig(VGroup(*dv[1:]), DEVC, MINI), run_time=0.8)
        until(self, "REFERENCE dot md", lead=0.3)
        sh = sheet()
        self.play(GrowFromEdge(sh[0], LEFT), run_time=0.5)
        self.play(Create(sh[1]), FadeIn(sh[2]), FadeIn(T("REFERENCE.md", 42).move_to([-0.85, -2.9, 0])), run_time=0.5)
        until(self, "advertise the Nordic", lead=0.3)
        b1 = board(0.7, 1.4, 1.4, 1.0, 1)
        b1.shift(DOWN * 1.2)
        self.add(b1)
        self.play(b1.animate.shift(UP * 1.2), run_time=0.5, rate_func=ease_in)
        a1 = link(lap_pt(LAPC), board_pt(b1), angle=-0.7)
        e1 = ends(lap_pt(LAPC), board_pt(b1))
        self.play(Create(a1), FadeIn(e1), run_time=0.6)
        until(self, "one line of JSON", lead=0.4)
        ride(self, a1, 0.7, packet(0.7, 0.3, 1))
        ride(self, a1, 0.7, packet(0.7, 0.3, 1), back=True)
        until(self, "An Arduino", lead=0.3)
        b2 = board(2.7, 0.5, 1.2, 0.9, 2)
        b2.shift(DOWN * 1.2)
        self.add(b2)
        self.play(b2.animate.shift(UP * 1.2), run_time=0.5, rate_func=ease_in)
        a2 = link(lap_pt(LAPC), board_pt(b2), angle=-0.6)
        e2 = ends(lap_pt(LAPC), board_pt(b2))
        self.play(Create(a2), FadeIn(e2), run_time=0.6)
        until(self, "the best contribution", lead=0.3)
        root = dv[1].get_bottom() + DOWN * 0.25
        fk = VGroup(*[Line(root, b.get_right() + np.array([0.25, 0.1, 0]), color=DEV_EDGE, stroke_width=6) for b in (b1, b2)])
        fdot = Dot(root, radius=0.08, color=TERRA).set_z_index(3)
        self.play(Create(fk), FadeIn(fdot), run_time=0.6)
        self.play(FadeIn(T("fork", 42).move_to(root + np.array([0.7, 0.0, 0]))), run_time=0.3)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Desk, B01_OptIn, B02_Snapshot, B03_PetWakes, B04_Prompt, B05_Approve, B06_Pairing, B07_Blueprint):
    _cls.play = ST.play
