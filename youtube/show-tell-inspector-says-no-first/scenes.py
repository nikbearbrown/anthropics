"""
Manim scenes for show-tell-inspector-says-no-first (show-tell skill, card #5).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The quality loop of anthropics/cwc-long-running-agents, drawn as a workshop: a builder at a
bench, every part stamped FAIL until evidence is opened, an inspector in a closed booth
(fresh context), a handoff clipboard, the loop, the operator's stop file, and /goal.
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




# ═════════════════════════════ the film: a workshop with an inspector ═════════════════════════════
# Cast: a kraft WORKBENCH with the dark BUILDER station (the station of show-tell-five-ways-to-wire-an-agent);
# the kraft PART crate with a white stamp TAG (FAIL / PASS); the RESULTS BOARD (test-results.json); the
# HOOK arch over a short belt (show-tell-inside-a-plugin-folder's hook gate) with a drop BAR; a SCREENSHOT
# card (evidence, it shows the crack); a closed kraft INSPECTOR BOOTH behind a WALL (fresh context);
# a CLIPBOARD (PROGRESS.md) and a grey COMMIT stack (git log); the LOOP belts; an AGENT_STOP file and a
# STEER note; a small dark /goal booth.
SHADOW = "#BFB4A0"
KRAFT_SIDE = "#E8DCC6"
BENCH_W, BENCH_D, BENCH_Z = 3.4, 2.0, 1.1
TOPZ = BENCH_Z + 0.22
PX, PY, PS, PH = 2.05, 0.3, 0.95, 0.8           # the part crate on the bench
SX, SY, SW_, SD, SH_ = 0.3, 0.85, 1.2, 0.95, 1.05   # the builder station on the bench

BIG = Iso(-1.6, -2.55, 1.15)     # B00: the bench, centre stage
LB = Iso(-4.75, -1.55, 0.72)     # B01..B04: the bench, stepped left


def builder_lab():
    return T("builder", 42).move_to(BIG.p(SX, SY + SD, TOPZ + SH_ * 0.7) + LEFT * 1.4)


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def bench(iso):
    """Shadow, legs and the kraft top. Things on the bench stand at z = TOPZ."""
    sh = iso.quad([(0.25, -0.35, 0), (BENCH_W + 0.35, -0.35, 0), (BENCH_W + 0.35, BENCH_D - 0.2, 0), (0.25, BENCH_D - 0.2, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    L = 0.22
    legs_back = VGroup(iso.box(0.12, BENCH_D - 0.34, 0, L, L, BENCH_Z, KRAFT_SIDE, BOX_L, BOX_R, sw=3),
                       iso.box(BENCH_W - 0.34, BENCH_D - 0.34, 0, L, L, BENCH_Z, KRAFT_SIDE, BOX_L, BOX_R, sw=3))
    legs_front = VGroup(iso.box(0.12, 0.12, 0, L, L, BENCH_Z, KRAFT_SIDE, BOX_L, BOX_R, sw=3),
                        iso.box(BENCH_W - 0.34, 0.12, 0, L, L, BENCH_Z, KRAFT_SIDE, BOX_L, BOX_R, sw=3))
    top = iso.box(0, 0, BENCH_Z, BENCH_W, BENCH_D, 0.22)
    return VGroup(sh, legs_back, legs_front, top)


def builder(iso, on=True):
    """The dark builder station; [1] is its light."""
    body = iso.box(SX, SY, TOPZ, SW_, SD, SH_, DARK_TOP, DARK_L, DARK_R)
    light = Dot(iso.p(SX + SW_ * 0.72, SY, TOPZ + SH_ * 0.6), radius=max(0.06, 0.11 * iso.s), color=TERRA if on else GHOST)
    light.set_z_index(1)
    return VGroup(body, light)


def part(iso):
    return iso.box(PX, PY, TOPZ, PS, PS, PH)


def crack(iso):
    """An ink zigzag on the part's right front face (y = PY): the visible break."""
    pts = [(PX + 0.22, PY, TOPZ + PH - 0.04), (PX + 0.47, PY, TOPZ + 0.5), (PX + 0.34, PY, TOPZ + 0.36), (PX + 0.66, PY, TOPZ + 0.1)]
    c = VMobject(stroke_color=INK, stroke_width=6).set_points_as_corners([iso.p(*q) for q in pts])
    c.set_z_index(1)
    return c


def tag_at(iso):
    return iso.p(PX + PS / 2, PY + PS / 2, TOPZ + PH) + UP * (0.55 + 0.25 * iso.s)


def tag(word, at, size=34):
    """A white stamp tag with one ink word (no outline: text inside an outline trips GATE T)."""
    t = T(word, size, INK, bold=True)
    bg = RoundedRectangle(width=t.width + 0.5, height=t.height + 0.36, corner_radius=0.1, fill_color="#FFFFFF",
                          fill_opacity=1, stroke_width=0)
    g = VGroup(bg, t.move_to(bg.get_center()))
    g.move_to(at).set_z_index(6)
    return g


def shop(iso, word=None, cracked=True, on=True):
    """(bench, builder, part, crack, tag): the workshop bench as it stands."""
    g = VGroup(bench(iso), builder(iso, on), part(iso))
    g.add(crack(iso) if cracked else VGroup())
    g.add(tag(word, tag_at(iso)) if word else VGroup())
    return g


def swap_tag(self, g, word, rt=0.45):
    """Replace the part's tag (g[4]) with a new word: the old one lifts away, the new one drops on."""
    old = g[4]
    new = tag(word, old.get_center() if len(old) else tag_at(LB))
    new.shift(UP * 0.6)
    self.play(FadeOut(old, shift=UP * 0.5), FadeIn(new, shift=DOWN * 0.6), run_time=rt)
    g.remove(old)
    g.add(new)
    return new


# the results board: test-results.json, one row per feature
BC, BWD_, BHT = np.array([3.55, 0.55, 0]), 3.7, 2.9


def board(c=BC, w=BWD_, h=BHT):
    win = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to(c)
    bar = Rectangle(width=w, height=0.46, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (h / 2 - 0.23))
    dots = VGroup(*[Dot(c + np.array([-w / 2 + 0.33 + i * 0.28, h / 2 - 0.23, 0]), radius=0.065, color=GHOST) for i in range(3)])
    lines = VGroup(*[Line(row_pt(i, c, w, h) + RIGHT * 0.5, row_pt(i, c, w, h) + RIGHT * (w - 1.35), color=GHOST, stroke_width=10)
                     for i in range(3)])
    return VGroup(win, bar, dots, lines)


def row_pt(i, c=BC, w=BWD_, h=BHT):
    """Where row i's mark sits (the left end of its line)."""
    return np.array([c[0] - w / 2 + 0.55, c[1] + h / 2 - 1.05 - i * 0.72, 0])


def cross(x, y, s=0.17, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def mark(i, ok, c=BC):
    p = row_pt(i, c)
    m = check(p[0] - 0.05, p[1] + 0.03, 0.17, INK, 7) if ok else cross(p[0], p[1])
    m.set_z_index(5)
    return m


def board_lab(c=BC):
    return T("test-results.json", 38).move_to(c + DOWN * (BHT / 2 + 0.42))


def shot_card(w=1.5, h=1.1, cracked=True):
    """A screenshot (evidence): white card, DIM outline, dark title strip, a ghost line and the crack."""
    card = Rectangle(width=w, height=h, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
    strip_ = Rectangle(width=w, height=h * 0.2, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(card.get_top() + DOWN * h * 0.1)
    ln = Line([-w * 0.32, -h * 0.02, 0], [w * 0.1, -h * 0.02, 0], color=GHOST, stroke_width=6)
    g = VGroup(card, strip_, ln)
    if cracked:
        z = VMobject(stroke_color=INK, stroke_width=4).set_points_as_corners(
            [np.array(q) for q in ([w * 0.18, h * 0.22, 0], [w * 0.3, -h * 0.02, 0], [w * 0.22, -h * 0.1, 0], [w * 0.36, -h * 0.34, 0])])
        g.add(z)
    return g


def note_card(w=1.3, h=0.9, n=2):
    """A small white note (a prompt, findings, a slip): DIM outline, ink lines."""
    card = Rectangle(width=w, height=h, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
    lines = VGroup(*[Line([-w * 0.32, h * (0.18 - 0.3 * i), 0], [w * (0.32 - 0.2 * i), h * (0.18 - 0.3 * i), 0], color=INK, stroke_width=5)
                     for i in range(n)])
    return VGroup(card, lines)


# the hook: an ink arch over a short belt, with a drop bar that lifts
BELT = Iso(-2.15, -2.75, 0.6)
BLEN, BWID, GX = 7.2, 1.3, 3.6


def belt(iso=BELT, L=BLEN, w=BWID):
    q = iso.quad([(0, 0, 0), (L, 0, 0), (L, w, 0), (0, w, 0)], "#E6DFD3", stroke=DIM, sw=2)
    m = DashedLine(iso.p(0.3, w / 2, 0), iso.p(L - 0.3, w / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
    return VGroup(q, m)


def hook(iso=BELT, gx=GX, w=BWID, H=2.4):
    back = VGroup(Line(iso.p(gx, w + 0.1, 0), iso.p(gx, w + 0.1, H), color=INK, stroke_width=9),
                  Line(iso.p(gx, w + 0.1, H), iso.p(gx, -0.1, H), color=INK, stroke_width=9))
    front = Line(iso.p(gx, -0.1, 0), iso.p(gx, -0.1, H), color=INK, stroke_width=9)
    light = Dot(iso.p(gx, -0.1, H), radius=0.12, color=GHOST)
    bar = Line(iso.p(gx, w + 0.1, 0.75), iso.p(gx, -0.1, 0.75), color=INK, stroke_width=12)
    back.set_z_index(0); front.set_z_index(4); light.set_z_index(5); bar.set_z_index(4)
    return back, front, light, bar


def slip(iso=BELT, x=0.4):
    """A write slip riding the belt: a flat white card with an ink check on top."""
    s = iso.box(x, 0.3, 0.02, 1.1, 0.7, 0.1, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    for f in s:
        f.set_stroke(DIM, 2)
    c = check(*iso.p(x + 0.55, 0.65, 0.12)[:2], 0.13, INK, 5)
    g = VGroup(s, c)
    g.set_z_index(3)
    return g


# the inspector's booth and the wall (fresh context)
def booth(iso, x0=0.0, y0=0.0, w=1.9, d=1.9, h=2.7, lamp_on=False):
    """A closed kraft booth: a dark window high on the left face, a dark hatch low, a lamp on the right face ([3])."""
    body = iso.box(x0, y0, 0, w, d, h)
    win = iso.quad([(x0, y0 + 0.35, h * 0.56), (x0, y0 + d - 0.35, h * 0.56), (x0, y0 + d - 0.35, h * 0.84), (x0, y0 + 0.35, h * 0.84)], DARK_L, sw=3)
    hatch = iso.quad([(x0, y0 + 0.55, 0.3), (x0, y0 + d - 0.55, 0.3), (x0, y0 + d - 0.55, 0.95), (x0, y0 + 0.55, 0.95)], DARK_R, sw=3)
    lamp = Dot(iso.p(x0 + w * 0.5, y0, h * 0.72), radius=max(0.07, 0.12 * iso.s), color=TERRA if lamp_on else GHOST)
    lamp.set_z_index(1)
    sh = iso.quad([(x0 + 0.2, y0 - 0.3, 0), (x0 + w + 0.3, y0 - 0.3, 0), (x0 + w + 0.3, y0 + d - 0.2, 0), (x0 + 0.2, y0 + d - 0.2, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return VGroup(body, win, hatch, lamp, sh)


BO = Iso(2.6, -2.35, 0.78)       # the booth rig (B03, B04)
WL = Iso(-0.35, -2.55, 0.78)     # the wall rig


def wall(iso=WL):
    return iso.box(0, -0.2, 0, 0.22, 3.4, 3.4, BOX_TOP, BOX_L, BOX_R)


def hatch_pt():
    return BO.p(0, 0.95, 0.62)


def pencil(c):
    body = Polygon([-0.55, -0.1, 0], [0.35, -0.1, 0], [0.35, 0.1, 0], [-0.55, 0.1, 0], fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=3)
    tip = Polygon([0.35, -0.1, 0], [0.6, 0, 0], [0.35, 0.1, 0], fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3)
    g = VGroup(body, tip).rotate(PI / 6).move_to(c)
    return g


def thoughts(iso):
    """The builder's reasoning: three pages stacked on the bench behind the station."""
    return VGroup(*[dpage(iso, 0.2, 0.1, TOPZ + i * 0.1, 1.2, 0.6, dot=False) for i in range(3)])


def dpage(iso, x0, y0, z0, w=1.1, d=1.4, dot=True):
    """A flat white page with a DIM outline, three ghost lines, and an optional terracotta dot."""
    slab = iso.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    for f in slab:
        f.set_stroke(DIM, 2)
    zt = z0 + 0.06
    lines = VGroup(*[Line(iso.p(x0 + 0.15, y0 + d * f, zt), iso.p(x0 + w - 0.15, y0 + d * f, zt), color=GHOST, stroke_width=3)
                     for f in (0.3, 0.7)])
    g = VGroup(slab, lines)
    if dot:
        g.add(Dot(iso.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA))
    return g


# ─────────────── B00: the bench, and a builder that grades itself ───────────────
class B00_Bench(Scene):
    def construct(self):
        b, st = bench(BIG), builder(BIG, on=False)
        g = VGroup(b, st)
        g.shift(DOWN * 4.5)
        self.add(g)
        self.play(g.animate.shift(UP * 4.5), run_time=0.9)
        until(self, "a builder makes", lead=0.4)
        blab = builder_lab()
        self.play(st[1].animate.set_color(TERRA), FadeIn(blab), run_time=0.5)
        until(self, "one feature at a time", lead=0.4)
        pt = part(BIG)
        self.play(GrowFromEdge(pt, DOWN), run_time=0.6)
        self.play(Indicate(st, color=None, scale_factor=1.04), run_time=0.5)
        until(self, "after one unit test", lead=0.3)
        tk = check(*(BIG.p(PX + PS / 2, PY + PS / 2, TOPZ + PH)[:2] + np.array([0.0, 0.55])), 0.18, INK, 7)
        tk.set_z_index(6)
        self.play(Create(tk), run_time=0.35)
        until(self, "it marks the part", lead=0.3)
        tg = tag("PASS", tag_at(BIG)).shift(UP * 0.8)
        self.play(FadeOut(tk), tg.animate.shift(DOWN * 0.8), run_time=0.45, rate_func=ease_in)
        self.play(Indicate(tg, color=None, scale_factor=1.08), run_time=0.35)
        until(self, "visibly broken", lead=0.4)
        ck = crack(BIG)
        self.play(Create(ck), run_time=0.5)
        self.play(Indicate(pt, color=None, scale_factor=1.05), run_time=0.5)
        done(self)


# ─────────────── B01: flip the default: every row starts false ───────────────
class B01_DefaultFail(Scene):
    def construct(self):
        g = shop(BIG, "PASS")
        blab = builder_lab()
        self.add(g, blab)
        body = VGroup(*g[:4])
        self.play(to_rig(body, BIG, LB), g[4].animate.move_to(tag_at(LB)), FadeOut(blab), run_time=0.7)
        nt = note_card(1.2, 0.8).move_to([0.5, 2.3, 0]).set_z_index(7)
        self.play(FadeIn(nt, shift=LEFT * 0.4), run_time=0.4)
        self.play(nt.animate.scale(0.35).move_to(LB.p(SX + SW_ / 2, SY + SD / 2, TOPZ + SH_)), run_time=0.6)
        self.remove(nt)
        self.play(Indicate(g[4], color=None, scale_factor=1.1), run_time=0.45)
        until(self, "flips the default", lead=0.4)
        swap_tag(self, g, "FAIL")
        until(self, "Every feature is a row", lead=0.4)
        bd = board()
        rt = guard(self, 0.6)
        bd.shift(RIGHT * 7)
        self.add(bd)
        self.play(bd.animate.shift(LEFT * 7), run_time=rt)
        self.play(FadeIn(board_lab()), run_time=0.35)
        until(self, "every row starts false", lead=0.5)
        for i in range(3):
            self.play(Create(mark(i, False)), run_time=0.25)
        done(self)


# ─────────────── B02: the hook: no write without evidence ───────────────
class B02_EvidenceGate(Scene):
    def construct(self):
        g = shop(LB, "FAIL")
        bd = board()
        marks = VGroup(*[mark(i, False) for i in range(3)])
        blab = board_lab()
        self.add(g, bd, marks, blab)
        bl = belt()
        back, front, light, bar = hook()
        self.play(FadeIn(bl, shift=UP * 0.2), run_time=0.5)
        self.play(Create(back), Create(front), FadeIn(light), Create(bar), run_time=0.6)
        hlab = T("hook", 40).move_to(BELT.p(GX, -0.1, 2.4) + np.array([0.75, 0.3, 0]))
        self.play(FadeIn(hlab), run_time=0.3)
        until(self, "can't write to it", lead=0.5)
        s1 = slip(BELT, 0.2)
        rt = guard(self, 0.9)
        self.add(s1)
        self.play(s1.animate.shift(BELT.v(GX - 1.55, 0, 0)), run_time=rt, rate_func=rate_functions.ease_out_sine)
        self.play(Indicate(bar, color=INK, scale_factor=1.08), run_time=0.35)
        until(self, "opened evidence", lead=0.4)
        sc = shot_card(1.5, 1.1)
        start = LB.p(PX + PS / 2, PY, TOPZ + PH * 0.5)
        sc.scale(0.3).move_to(start).set_z_index(8)
        rt = guard(self, 0.7)
        self.add(sc)
        self.play(sc.animate.scale(1 / 0.3 * 1.3).move_to([0.55, 2.1, 0]), run_time=rt)
        elab = T("evidence", 40).move_to([-1.55, 2.1, 0])
        self.play(FadeIn(elab), run_time=0.3)
        until(self, "Each read unlocks", lead=0.3)
        self.play(light.animate.set_color(TERRA), bar.animate.shift(BELT.v(0, 0, 1.5)), run_time=0.4)
        self.play(s1.animate.shift(BELT.v(BLEN - GX + 0.2, 0, 0)), run_time=0.8, rate_func=linear)
        m0 = mark(0, True)
        self.play(FadeOut(s1), FadeOut(marks[0]), Create(m0), run_time=0.35)
        swap_tag(self, g, "PASS", rt=0.4)
        until(self, "fresh proof", lead=0.5)
        self.play(FadeOut(sc), FadeOut(elab), light.animate.set_color(GHOST), bar.animate.shift(BELT.v(0, 0, -1.5)), run_time=0.45)
        s2 = slip(BELT, 0.2)
        self.add(s2)
        self.play(s2.animate.shift(BELT.v(GX - 1.55, 0, 0)), run_time=0.6, rate_func=rate_functions.ease_out_sine)
        done(self)


# ─────────────── B03: the inspector's booth: a fresh context ───────────────
def b02_end():
    """B02's last frame, rebuilt (for the continuity start of B03)."""
    g = shop(LB, "PASS")
    bd = board()
    marks = VGroup(mark(0, True), mark(1, False), mark(2, False))
    back, front, light, bar = hook()
    s2 = slip(BELT, 0.2).shift(BELT.v(GX - 1.55, 0, 0))
    rest = VGroup(bd, marks, board_lab(), belt(), back, front, light, bar, s2, T("hook", 40).move_to(BELT.p(GX, -0.1, 2.4) + np.array([0.75, 0.3, 0])))
    return g, rest


class B03_Booth(Scene):
    def construct(self):
        g, rest = b02_end()
        self.add(g, rest)
        self.play(FadeOut(rest, shift=RIGHT * 0.4), run_time=0.5)
        th = thoughts(LB)
        th.set_z_index(1)
        self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.3) for p in th], lag_ratio=0.3), run_time=0.5)
        until(self, "from its own booth", lead=0.5)
        bt = booth(BO)
        bt.shift(RIGHT * 6)
        self.add(bt)
        self.play(bt.animate.shift(LEFT * 6), run_time=0.7)
        ilab = T("inspector", 42).move_to(BO.p(0.95, 0.95, 2.7) + UP * 1.2)
        self.play(FadeIn(ilab), run_time=0.3)
        until(self, "with a fresh context", lead=0.5)
        wl = wall()
        self.play(GrowFromEdge(wl, DOWN), run_time=0.6)
        flab = T("fresh context", 40).move_to([-0.55, -2.95, 0])
        self.play(FadeIn(flab), run_time=0.3)
        until(self, "It never saw the build", lead=0.3)
        self.play(th.animate.set_opacity(0.45), run_time=0.4)
        until(self, "It gets the spec", lead=0.5)
        hp = hatch_pt()
        items = [note_card(1.0, 1.25, 3), note_card(1.3, 0.9, 2), shot_card(1.4, 1.0)]
        spots = [np.array([-1.7 + 1.55 * i, 2.55, 0]) for i in range(3)]
        rt = guard(self, 1.6)
        for it, sp in zip(items, spots):
            it.move_to(sp).set_z_index(8)
            it.shift(UP * 2.5)
        self.add(*items)
        self.play(LaggedStart(*[it.animate.shift(DOWN * 2.5) for it in items], lag_ratio=0.2), run_time=rt * 0.45)
        self.play(LaggedStart(*[it.animate.scale(0.15).move_to(hp) for it in items], lag_ratio=0.25), run_time=rt * 0.55)
        self.remove(*items)
        self.play(Indicate(bt[2], color=None, scale_factor=1.2), run_time=0.35)
        until(self, "no Write or Edit", lead=0.5)
        pc = pencil([5.1, 0.5, 0])
        self.play(FadeIn(pc), run_time=0.3)
        X = cross(5.1, 0.5, 0.42, INK, 9)
        self.play(Create(X), run_time=0.4)
        done(self)


# ─────────────── B04: the inspector says NEEDS_WORK; findings ride back ───────────────
def b03_end():
    g = shop(LB, "PASS")
    th = thoughts(LB).set_opacity(0.45)
    bt, wl = booth(BO), wall()
    labs = VGroup(T("inspector", 42).move_to(BO.p(0.95, 0.95, 2.7) + UP * 1.2),
                  T("fresh context", 40).move_to([-0.55, -2.95, 0]))
    pc = VGroup(pencil([5.1, 0.5, 0]), cross(5.1, 0.5, 0.42, INK, 9))
    return g, th, bt, wl, labs, pc


class B04_NeedsWork(Scene):
    def construct(self):
        g, th, bt, wl, labs, pc = b03_end()
        self.add(g, th, bt, wl, labs, pc)
        self.play(FadeOut(pc), FadeOut(labs[1]), run_time=0.4)
        until(self, "plausibility is not", lead=0.4)
        sc = shot_card(1.9, 1.4).move_to([5.0, 2.3, 0]).set_z_index(8)
        start = sc.copy().scale(0.15).move_to(BO.p(0, 0.95, 2.0))
        self.play(TransformFromCopy(start, sc), run_time=0.6)
        ring = Circle(radius=0.42, color=INK, stroke_width=7).move_to(sc.get_center() + np.array([0.52, -0.05, 0])).set_z_index(9)
        self.play(Create(ring), run_time=0.5)
        until(self, "missing evidence means", lead=0.3)
        self.play(bt[3].animate.set_color(TERRA), run_time=0.35)
        until(self, "So it answers", lead=0.5)
        nw = tag("NEEDS_WORK", [4.4, -2.8, 0], size=32)
        rt = guard(self, 0.5)
        nw.shift(LEFT * 0.8)
        self.play(FadeOut(sc), FadeOut(ring), nw.animate.shift(RIGHT * 0.8), run_time=rt)
        until(self, "its findings become", lead=0.4)
        fd = note_card(1.2, 0.85, 2).move_to(BO.p(0, 0.95, 2.9) + UP * 0.2).set_z_index(9)
        flab = T("findings", 40).move_to(fd.get_center() + LEFT * 1.75 + UP * 0.45)
        self.play(FadeIn(fd, shift=UP * 0.3), FadeIn(flab), run_time=0.4)
        dest = LB.p(SX + SW_ / 2, SY + SD / 2, TOPZ + SH_) + UP * 0.35
        self.play(MoveAlongPath(fd, ArcBetweenPoints(fd.get_center(), dest, angle=TAU / 5)), run_time=1.1)
        self.play(fd.animate.scale(0.3).move_to(dest + DOWN * 0.3), g[1][1].animate.set_color(GHOST), FadeOut(flab), run_time=0.35)
        self.remove(fd)
        self.play(g[1][1].animate.set_color(TERRA), run_time=0.25)
        swap_tag(self, g, "FAIL", rt=0.4)
        done(self)


# ─────────────── B05: the handoff note and the commits ───────────────
HB = Iso(-3.6, -1.9, 0.9)        # B05: the bench, bigger, left of centre
GL = Iso(3.2, -2.45, 0.75)        # the git-log stack rig


def clip_board(c, w=1.6, h=2.1):
    board_ = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    paper = Rectangle(width=w - 0.36, height=h - 0.5, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to(c + DOWN * 0.1)
    clip = RoundedRectangle(width=w * 0.45, height=0.26, corner_radius=0.06, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (h / 2 - 0.05))
    return VGroup(board_, paper, clip)


def clip_lines(c, w=1.6, h=2.1):
    x0 = c[0] - w / 2 + 0.38
    return [Line([x0, y, 0], [x0 + (w - 0.76) * f, y, 0], color=INK, stroke_width=5)
            for y, f in zip([c[1] + 0.45, c[1] + 0.1, c[1] - 0.25, c[1] - 0.6], (0.9, 0.7, 0.85, 0.55))]


def commit(k):
    """k-th grey commit slab on the git-log stack (grey tones with gaps: packed dark blocks fuse under GATE T)."""
    tone = (BAR1, BAR2, BAR3)[k % 3]
    return GL.box(0, 0, k * 0.42, 1.5, 1.5, 0.34, tone, tone, tone, sw=3)


class B05_Handoff(Scene):
    def construct(self):
        g, th, bt, wl, labs, pc = b03_end()
        g2 = shop(LB, "FAIL")
        left = VGroup(g2, th)
        self.add(left, bt, wl, labs[0], tag("NEEDS_WORK", [4.4, -2.8, 0], size=32))
        self.play(*[FadeOut(m, shift=RIGHT * 0.5) for m in self.mobjects if m is not left], run_time=0.5)
        self.play(FadeOut(th), to_rig(VGroup(*g2[:4]), LB, HB), g2[4].animate.move_to(tag_at(HB)), run_time=0.7)
        until(self, "starts cold", lead=0.6)
        st = g2[1]
        self.play(st[1].animate.set_color(GHOST), run_time=0.3)
        fresh = builder(HB, on=True)
        fresh.shift(UP * 5)
        self.play(st.animate.shift(LEFT * 7), run_time=0.5)
        self.add(fresh)
        self.play(fresh.animate.shift(DOWN * 5), run_time=0.5, rate_func=ease_in)
        until(self, "own handoff note", lead=0.5)
        cc = np.array([1.2, 1.35, 0])
        cb = clip_board(cc).set_z_index(5)
        cb.shift(UP * 4)
        self.add(cb)
        self.play(cb.animate.shift(DOWN * 4), run_time=0.5, rate_func=ease_in)
        plab = T("PROGRESS.md", 40).move_to(cc + DOWN * 1.5)
        self.play(FadeIn(plab), run_time=0.3)
        lines = VGroup(*clip_lines(cc))
        lines.set_z_index(6)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.3), run_time=rt)
        until(self, "reads it first", lead=0.4)
        link = DashedLine(cc + LEFT * 0.85 + UP * 0.2, HB.p(SX + SW_, SY + SD / 2, TOPZ + SH_ * 0.8) + RIGHT * 0.1, color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(link), Indicate(VGroup(cb, lines), color=None, scale_factor=1.06), run_time=0.6)
        self.play(Indicate(fresh, color=None, scale_factor=1.04), run_time=0.4)
        until(self, "It commits as it goes", lead=0.4)
        glab = T("git log", 40).move_to(GL.p(0.75, 0, 0) + np.array([0.9, -0.55, 0]))
        c0 = commit(0); c0.shift(UP * 3); self.add(c0)
        self.play(FadeOut(link), c0.animate.shift(DOWN * 3), FadeIn(glab), run_time=0.5, rate_func=ease_in)
        c1 = commit(1); c1.shift(UP * 3); self.add(c1)
        self.play(c1.animate.shift(DOWN * 3), run_time=0.45, rate_func=ease_in)
        until(self, "when the session stops", lead=0.4)
        c2 = commit(2); c2.shift(UP * 3); self.add(c2)
        self.play(fresh[1].animate.set_color(GHOST), c2.animate.shift(DOWN * 3), run_time=0.5, rate_func=ease_in)
        done(self)


# ─────────────── B06: the loop ───────────────
LP = Iso(-5.2, -3.1, 0.55)      # the loop's bench (small, left)
LBO = Iso(2.55, -2.9, 0.62)      # the loop's booth
BC6 = np.array([-3.9, 1.95, 0])   # the board, top centre


def board_small(c=BC6):
    return board(c, 3.3, 2.5)


def mark6(i, ok):
    p = row_pt(i, BC6, 3.3, 2.5)
    m = check(p[0] - 0.05, p[1] + 0.03, 0.16, INK, 7) if ok else cross(p[0], p[1], 0.15)
    m.set_z_index(5)
    return m


def board6_lines():
    return VGroup(*[Line(row_pt(i, BC6, 3.3, 2.5) + RIGHT * 0.5, row_pt(i, BC6, 3.3, 2.5) + RIGHT * (3.3 - 1.35), color=GHOST, stroke_width=10)
                    for i in range(3)])


def board6():
    c, w, h = BC6, 3.3, 2.5
    win = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to(c)
    bar = Rectangle(width=w, height=0.42, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (h / 2 - 0.21))
    dots = VGroup(*[Dot(c + np.array([-w / 2 + 0.33 + i * 0.28, h / 2 - 0.21, 0]), radius=0.06, color=GHOST) for i in range(3)])
    return VGroup(win, bar, dots, board6_lines())


# loop belts: out along the front (bench -> booth), back along the rear
LOOP = Iso(-3.0, -3.05, 0.55)
LOUT, LW = 9.6, 1.1


def loop_belts():
    out = LOOP.quad([(0, 0, 0), (LOUT, 0, 0), (LOUT, LW, 0), (0, LW, 0)], "#E6DFD3", stroke=DIM, sw=2)
    m1 = DashedLine(LOOP.p(0.3, LW / 2, 0), LOOP.p(LOUT - 0.3, LW / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
    return VGroup(out, m1)


def loop_shop():
    """The loop layout: bench (left), belt, booth (right), board (top)."""
    return VGroup(shop(LP, None, cracked=False), loop_belts(), booth(LBO))


def rider(x):
    c = LOOP.box(x, 0.2, 0.02, 0.8, 0.7, 0.62)
    c.set_z_index(3)
    return c


class B06_Loop(Scene):
    def construct(self):
        # B05's end, then the loop layout
        g = shop(HB, "FAIL", cracked=True)
        g[1][1].set_color(GHOST)
        cc = np.array([1.2, 1.35, 0])
        last = VGroup(g, clip_board(cc), VGroup(*clip_lines(cc)), T("PROGRESS.md", 40).move_to(cc + DOWN * 1.5),
                      commit(0), commit(1), commit(2), T("git log", 40).move_to(GL.p(0.75, 0, 0) + np.array([0.9, -0.55, 0])))
        self.add(last)
        self.play(FadeOut(last), run_time=0.5)
        ls = loop_shop()
        bd = board6()
        marks = VGroup(*[mark6(i, False) for i in range(3)])
        self.play(FadeIn(ls[0], shift=RIGHT * 0.3), FadeIn(ls[1]), FadeIn(ls[2], shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(bd, shift=DOWN * 0.3), run_time=0.4)
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.3), run_time=0.5)
        blab = T("build", 40).move_to([-5.0, -0.3, 0])
        ilab = T("inspect", 40).move_to([4.6, -2.95, 0])
        self.play(FadeIn(blab), FadeIn(ilab), run_time=0.3)
        lamp = ls[2][3]

        def trip(i, ok, rt=1.4):
            rt = guard(self, rt)
            r = rider(0.2)
            self.add(r)
            self.play(r.animate.shift(LOOP.v(LOUT - 1.4, 0, 0)), run_time=rt * 0.5, rate_func=linear)
            self.play(lamp.animate.set_color(TERRA), FadeOut(r), run_time=rt * 0.15)
            if ok:
                self.play(FadeOut(marks[i]), Create(mark6(i, True)), lamp.animate.set_color(GHOST), run_time=rt * 0.35)
            else:
                fd = note_card(0.8, 0.55, 2).move_to(LBO.p(0.95, 0.95, 2.7) + UP * 0.4).set_z_index(8)
                dest = LP.p(SX + SW_ / 2, SY + SD / 2, TOPZ + SH_) + UP * 0.2
                self.add(fd)
                self.play(lamp.animate.set_color(GHOST), MoveAlongPath(fd, ArcBetweenPoints(fd.get_center(), dest, angle=TAU / 6)), run_time=rt * 0.3)
                self.remove(fd)
                self.play(Indicate(ls[0][1], color=None, scale_factor=1.06), run_time=rt * 0.05 + 0.1)

        until(self, "build, inspect", lead=0.2)
        trip(0, False, 1.2)
        trip(0, True, 1.2)
        until(self, "a cycle changes nothing", lead=0.4)
        trip(1, True, 1.2)
        until(self, "Let only its PASS", lead=0.6)
        link = DashedLine(LBO.p(0.95, 0.95, 2.8) + UP * 0.1, BC6 + np.array([1.75, -0.8, 0]), color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(link), run_time=0.4)
        self.play(FadeOut(marks[2]), Create(mark6(2, True)), run_time=0.35)
        done(self)


# ─────────────── B07: the operator: AGENT_STOP and STEER.md ───────────────
def file_card(c, w=1.25, h=1.55):
    """A file with a folded corner (DIM outline), two ghost lines."""
    f = 0.32
    body = Polygon([c[0] - w / 2, c[1] - h / 2, 0], [c[0] + w / 2, c[1] - h / 2, 0], [c[0] + w / 2, c[1] + h / 2 - f, 0],
                   [c[0] + w / 2 - f, c[1] + h / 2, 0], [c[0] - w / 2, c[1] + h / 2, 0],
                   fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=2.5)
    fold = Polygon([c[0] + w / 2 - f, c[1] + h / 2, 0], [c[0] + w / 2 - f, c[1] + h / 2 - f, 0], [c[0] + w / 2, c[1] + h / 2 - f, 0],
                   fill_color=GHOST, fill_opacity=1, stroke_color=DIM, stroke_width=2)
    dark = Rectangle(width=w - 0.4, height=0.28, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([c[0] - 0.05, c[1] + 0.05, 0])
    return VGroup(body, fold, dark)


class B07_Operator(Scene):
    def construct(self):
        ls = loop_shop()
        bd = board6()
        marks = VGroup(mark6(0, True), mark6(1, True), mark6(2, True))
        self.add(ls, bd, marks)
        self.play(FadeOut(bd), FadeOut(marks), run_time=0.4)
        lamp, light = ls[2][3], ls[0][1][1]
        r = rider(0.2)
        self.add(r)
        self.play(r.animate.shift(LOOP.v(3.2, 0, 0)), lamp.animate.set_color(TERRA), run_time=0.9, rate_func=linear)
        until(self, "a file called agent stop", lead=0.5)
        fc = file_card(np.array([0.2, 1.5, 0])).set_z_index(8)
        fc.shift(UP * 3.5)
        self.add(fc)
        self.play(fc.animate.shift(DOWN * 3.5), run_time=0.5, rate_func=ease_in)
        alab = T("AGENT_STOP", 40).move_to([0.2, 0.25, 0])
        self.play(FadeIn(alab), run_time=0.3)
        until(self, "every tool call halts", lead=0.3)
        self.play(lamp.animate.set_color(GHOST), light.animate.set_color(GHOST), run_time=0.4)
        until(self, "Write a note", lead=0.5)
        self.play(FadeOut(fc, shift=UP * 1.2), FadeOut(alab), light.animate.set_color(TERRA), run_time=0.5)
        nt = note_card(1.3, 0.9, 2).move_to([-1.3, 2.4, 0]).set_z_index(8)
        slab = T("STEER.md", 40).move_to([0.9, 2.4, 0])
        self.play(FadeIn(nt, shift=LEFT * 0.4), FadeIn(slab), run_time=0.4)
        until(self, "sees it once", lead=0.3)
        dest = LP.p(SX + SW_ / 2, SY + SD / 2, TOPZ + SH_)
        self.play(nt.animate.scale(0.3).move_to(dest), run_time=0.6)
        self.remove(nt)
        self.play(Indicate(ls[0][1], color=None, scale_factor=1.08), FadeOut(slab), run_time=0.4)
        self.play(r.animate.shift(LOOP.v(3.2, 0, 0)), lamp.animate.set_color(TERRA), run_time=0.8, rate_func=linear)
        done(self)


# ─────────────── B08: /goal, the built-in checker, and your own evaluator.md ───────────────
GB = Iso(-3.9, -1.0, 0.72)       # the /goal booth; its belt runs in front of it (same rig)
EB = Iso(3.0, -1.7, 0.72)        # your evaluator.md booth; its belt runs into the hatch (same rig)


def goal_booth():
    body = GB.box(0, 0, 0, 1.6, 1.6, 1.9, DARK_TOP, DARK_L, DARK_R)
    lamp = Dot(GB.p(0.8, 0, 1.4), radius=0.1, color=GHOST).set_z_index(1)
    sh = GB.quad([(0.2, -0.3, 0), (1.9, -0.3, 0), (1.9, 1.4, 0), (0.2, 1.4, 0)], SHADOW, sw=0).set_z_index(-1)
    return VGroup(sh, body, lamp)


def goal_belt():
    q = GB.quad([(-3.0, -1.7, 0), (4.0, -1.7, 0), (4.0, -0.6, 0), (-3.0, -0.6, 0)], "#E6DFD3", stroke=DIM, sw=2)
    m = DashedLine(GB.p(-2.7, -1.15, 0), GB.p(3.7, -1.15, 0), color=DIM, stroke_width=2, dash_length=0.12)
    g = VGroup(q, m)
    g.set_z_index(-0.5)
    return g


class B08_GoalVsYours(Scene):
    def construct(self):
        ls = loop_shop()
        self.add(ls)
        self.play(FadeOut(ls[0]), FadeOut(ls[1]), to_rig(ls[2], LBO, EB), run_time=0.7)
        gb = goal_booth()
        gb.shift(LEFT * 6)
        self.add(gb)
        self.play(gb.animate.shift(RIGHT * 6), run_time=0.6)
        glab = T("/goal", 44).move_to([-5.45, 2.55, 0])
        self.play(FadeIn(glab), run_time=0.3)
        until(self, "takes a condition", lead=0.5)
        cond = RoundedRectangle(width=2.9, height=0.62, corner_radius=0.31, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0).move_to([-3.0, 2.55, 0])
        cl = Line([-4.1, 2.55, 0], [-1.9, 2.55, 0], color=INK, stroke_width=6)
        self.play(FadeIn(cond, shift=DOWN * 0.2), run_time=0.3)
        self.play(Create(cl), run_time=0.5)
        until(self, "after every turn", lead=0.4)
        gbl = goal_belt()
        self.play(FadeIn(gbl), run_time=0.3)
        lamp = gb[2]

        def turn(rt=0.9):
            rt = guard(self, rt)
            c = GB.box(-2.6, -1.5, 0.02, 0.7, 0.7, 0.58)
            c.set_z_index(3)
            self.add(c)
            self.play(c.animate.shift(GB.v(3.3, 0, 0)), run_time=rt * 0.45, rate_func=linear)
            self.play(lamp.animate.set_color(TERRA), c.animate.shift(GB.v(1.2, 0, 0)), run_time=rt * 0.2, rate_func=linear)
            self.play(lamp.animate.set_color(GHOST), c.animate.shift(GB.v(1.5, 0, 0)), run_time=rt * 0.2, rate_func=linear)
            self.play(FadeOut(c), run_time=rt * 0.15)

        turn()
        turn()
        until(self, "until it's met", lead=0.4)
        turn(0.8)
        ck = check(-1.2, 2.6, 0.2, TERRA, 8)
        self.play(Create(ck), lamp.animate.set_color(TERRA), run_time=0.4)
        until(self, "Write your own", lead=0.4)
        bt = ls[2]
        elab = T("evaluator.md", 42).move_to(EB.p(0.95, 0.95, 2.7) + UP * 1.2)
        self.play(Indicate(bt, color=None, scale_factor=1.05), FadeIn(elab), run_time=0.6)
        until(self, "the evidence gate", lead=0.5)
        eb = VGroup(EB.quad([(-3.4, 0.2, 0), (0, 0.2, 0), (0, 1.3, 0), (-3.4, 1.3, 0)], "#E6DFD3", stroke=DIM, sw=2))
        eb.set_z_index(-0.5)
        back, front, gl, bar = hook(EB, -2.7, 1.3, 1.9)
        self.play(FadeIn(eb), Create(back), Create(front), FadeIn(gl), run_time=0.5)
        self.play(gl.animate.set_color(TERRA), run_time=0.3)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Bench, B01_DefaultFail, B02_EvidenceGate, B03_Booth, B04_NeedsWork, B05_Handoff, B06_Loop, B07_Operator, B08_GoalVsYours):
    _cls.play = ST.play
