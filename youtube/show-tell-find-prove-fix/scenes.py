"""
Manim scenes for show-tell-find-prove-fix (show-tell skill, card #12, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The find-and-fix loop, from anthropics/defending-code-reference-harness (docs/blog-post.md, docs/pipeline.md,
README.md, docs/patching.md): your code is a building; six steps, two of setup and four in a loop. A threat map
says what counts and what is trusted; the building goes into a sealed glass box with one line out, to the model
API; one agent splits the roof into areas and inspectors search them; a finding is a crash file that trips the
alarm three times out of three; a grader in a fresh box gets only the file; a judge merges duplicates on a table
and ranks the rest; a patch climbs a four-rung ladder and the lessons go back to the map; a human owns the fix;
and the count: 1,596 disclosed, 97 patched, per Anthropic.
Cast deliberately NOT the security-review film's pull-request belt.
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






# ═════════════════════════════ the film: find, prove, fix ═════════════════════════════
# Cast: your code as a kraft BUILDING (grey windows, a dark door); a THREAT MAP card at the left (the
# building's footprint, a grey trusted zone, terracotta door dots, a dashed boundary); a GLASS SANDBOX
# (an ink wireframe box) with a cut cable and one line to a dark 'model API' block; INSPECTORS (small dark
# pawns) and a grey RECON pawn; a CRASH FILE card; the roof ALARM and a wall CRACK; a second, smaller glass
# box for the GRADER; a kraft TRIAGE TABLE; a PATCH plate, a four-rung LADDER, and a kraft HUMAN figure.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
GREY_TOP, GREY_L, GREY_R = "#C9C4BA", "#A9A398", "#96907F"
WIN = DARK_L             # windows: dark, no outline (they carry the pale building's contrast for Gate V)

W = Iso(0.5, -2.1, 0.82)                  # the one rig: the building in its glass box
BX, BY, BW, BD, BH = 0.0, 0.0, 2.6, 2.2, 2.3
GX, GY, GW, GD, GH = -0.45, -0.45, 3.5, 3.1, 3.0     # the glass box
MAP_C = np.array([-4.35, 1.0, 0])
MAP_W, MAP_H = 3.0, 2.5


def building(iso=W, door_dot=False):
    """(shadow, body, windows, door). Kraft box, grey windows in rows on both front faces, a dark door."""
    sh = iso.quad([(BX - 0.25, BY - 0.5, 0), (BX + BW + 0.4, BY - 0.5, 0), (BX + BW + 0.4, BY + BD, 0), (BX - 0.25, BY + BD, 0)], SHADOW, sw=0)
    sh.set_z_index(-2)
    body = iso.box(BX, BY, 0, BW, BD, BH)
    wins = VGroup()
    for zr in (1.15, 1.75):
        for xc in (0.35, 1.05, 1.95):          # right face (y = BY): leave room for the door at x 1.3..1.75 low
            wins.add(iso.quad([(xc, BY, zr), (xc + 0.4, BY, zr), (xc + 0.4, BY, zr + 0.35), (xc, BY, zr + 0.35)], WIN, sw=0))
        for yc in (0.35, 1.25):                # left face (x = BX)
            wins.add(iso.quad([(BX, yc, zr), (BX, yc + 0.5, zr), (BX, yc + 0.5, zr + 0.35), (BX, yc, zr + 0.35)], WIN, sw=0))
    door = iso.quad([(1.1, BY, 0), (1.55, BY, 0), (1.55, BY, 0.8), (1.1, BY, 0.8)], DARK_R, sw=0)
    g = VGroup(sh, body, wins, door)
    return g


def glass(iso=W, x0=GX, y0=GY, w=GW, d=GD, h=GH, sw=4):
    """An ink wireframe glass box: back edges dashed grey, front edges ink, two white glints."""
    P = lambda x, y, z: iso.p(x, y, z)
    x1, y1, z1 = x0 + w, y0 + d, h
    back = VGroup(*[DashedLine(P(*a), P(*b), color=DIM, stroke_width=2, dash_length=0.12) for a, b in
                    [((x1, y1, 0), (x1, y0, 0)), ((x1, y1, 0), (x0, y1, 0)), ((x1, y1, 0), (x1, y1, z1))]])
    front = VGroup(*[Line(P(*a), P(*b), color=INK, stroke_width=sw) for a, b in [
        ((x0, y0, 0), (x1, y0, 0)), ((x0, y0, 0), (x0, y1, 0)), ((x0, y0, 0), (x0, y0, z1)),
        ((x1, y0, 0), (x1, y0, z1)), ((x0, y1, 0), (x0, y1, z1)),
        ((x0, y0, z1), (x1, y0, z1)), ((x0, y0, z1), (x0, y1, z1)), ((x1, y0, z1), (x1, y1, z1)), ((x0, y1, z1), (x1, y1, z1))]])
    glint = VGroup(Line(P(x0 + w * 0.62, y0, h * 0.62), P(x0 + w * 0.8, y0, h * 0.86), color="#FFFFFF", stroke_width=7),
                   Line(P(x0 + w * 0.7, y0, h * 0.5), P(x0 + w * 0.84, y0, h * 0.68), color="#FFFFFF", stroke_width=7))
    back.set_z_index(-1); front.set_z_index(5); glint.set_z_index(5)
    return VGroup(back, front, glint)


def threat_map(c=MAP_C):
    """The threat map card: CARD sheet (no outline), a dark header bar, the building's footprint as a rhombus."""
    c = np.array(c, dtype=float)
    sheet = RoundedRectangle(width=MAP_W, height=MAP_H, corner_radius=0.12, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to(c)
    bar = Rectangle(width=MAP_W, height=0.34, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (MAP_H / 2 - 0.17))
    return VGroup(sheet, bar)


def fp_pts(c=MAP_C):
    """Footprint rhombus corners on the map: front, right, back, left."""
    o = np.array(c, dtype=float) + DOWN * 0.2
    return [o + np.array([0, -0.72, 0]), o + np.array([1.12, 0, 0]), o + np.array([0, 0.72, 0]), o + np.array([-1.12, 0, 0])]


def footprint(c=MAP_C):
    f, r, b, l = fp_pts(c)
    return Polygon(f, r, b, l, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3)


def trusted_zone(c=MAP_C):
    """The back part of the footprint (behind the boundary): grey = trusted."""
    f, r, b, l = fp_pts(c)
    m1, m2 = (l + b) / 2 * 0.0 + l + (b - l) * 0.45, r + (b - r) * 0.45
    return Polygon(m1, b, m2, fill_color=BAR2, fill_opacity=1, stroke_width=0)


def boundary(c=MAP_C):
    f, r, b, l = fp_pts(c)
    m1, m2 = l + (b - l) * 0.45, r + (b - r) * 0.45
    return DashedLine(m1 + LEFT * 0.25, m2 + RIGHT * 0.25, color=INK, stroke_width=5, dash_length=0.12)


def map_doors(c=MAP_C):
    """Two entry doors on the footprint's front edges (terracotta dots)."""
    f, r, b, l = fp_pts(c)
    return VGroup(Dot(f + (l - f) * 0.5, radius=0.1, color=TERRA), Dot(f + (r - f) * 0.5, radius=0.1, color=TERRA))


def map_full(c=MAP_C):
    return VGroup(threat_map(c), footprint(c), trusted_zone(c), boundary(c), map_doors(c))


def door_dot(iso=W):
    return Dot(iso.p(1.33, BY, 0.95), radius=0.09, color=TERRA).set_z_index(3)


def label_code():
    return T("your code", 42).move_to([-3.3, -2.35, 0])


def label_map():
    return T("threat model", 42).move_to(MAP_C + DOWN * (MAP_H / 2 + 0.45))


# ─── the sandbox parts (B02) ───
WEB_C = np.array([5.35, 1.75, 0])
API_C = np.array([5.3, -1.15, 0])
CABLE_A = W.p(GX + GW, GY, 2.3)          # where the cable leaves the glass (its right front edge)
API_A = W.p(GX + GW, GY, 0.9)


def web():
    ring = Circle(radius=0.5, fill_color=BAR3, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(WEB_C)
    mer = VGroup(Ellipse(width=0.45, height=1.0, stroke_color=INK, stroke_width=3).move_to(WEB_C),
                 Line(WEB_C + LEFT * 0.5, WEB_C + RIGHT * 0.5, color=INK, stroke_width=3))
    return VGroup(ring, mer)


def cable():
    return Line(CABLE_A, WEB_C + LEFT * 0.55 + DOWN * 0.1, color=INK, stroke_width=6)


def cut_ends():
    a, z = CABLE_A, WEB_C + LEFT * 0.55 + DOWN * 0.1
    m1, m2 = a + (z - a) * 0.4, a + (z - a) * 0.6
    return VGroup(Line(a, m1 + DOWN * 0.45, color=INK, stroke_width=6), Line(z, m2 + DOWN * 0.45, color=INK, stroke_width=6))


def api_block():
    iso = Iso(API_C[0] - 0.05, API_C[1] - 0.45, 0.55)
    return iso.box(-0.5, -0.5, 0, 1.0, 1.0, 0.9, DARK_TOP, DARK_L, DARK_R)


def api_line():
    return Line(API_A, API_C + LEFT * 0.75 + UP * 0.05, color=INK, stroke_width=5)


def key_icon(c):
    c = np.array(c, dtype=float)
    ring = Circle(radius=0.3, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to(c)
    shaft = Rectangle(width=0.9, height=0.2, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + RIGHT * 0.72)
    tooth = Rectangle(width=0.16, height=0.28, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + RIGHT * 1.02 + DOWN * 0.2)
    return VGroup(ring, shaft, tooth)


KEY_C = np.array([1.75, -2.75, 0])


def cross(c, s=0.3, w=7):
    c = np.array(c, dtype=float)
    return VGroup(Line(c + np.array([-s, -s, 0]), c + np.array([s, s, 0]), color=INK, stroke_width=w),
                  Line(c + np.array([-s, s, 0]), c + np.array([s, -s, 0]), color=INK, stroke_width=w))


def snap_card():
    """A small photo of the box: white card, a mini footprint, a DIM outline."""
    c = np.array([-2.0, 2.55, 0])
    card = RoundedRectangle(width=1.0, height=0.9, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to(c)
    mini = Polygon(c + np.array([0, -0.25, 0]), c + np.array([0.35, -0.03, 0]), c + np.array([0, 0.19, 0]), c + np.array([-0.35, -0.03, 0]),
                   fill_color=BOX_TOP, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2)
    return VGroup(card, mini)


def sandbox_state():
    """What B02 leaves: glass, the API block and its line, the crossed key, the cut cable ends, the web, the snapshot."""
    return VGroup(glass(), api_block(), api_line(), web(), cut_ends(), snap_card(), key_icon(KEY_C), cross(KEY_C + RIGHT * 0.45, 0.42),
                  T("sandbox", 42).move_to([-2.75, -1.6, 0]), T("model API", 42).move_to(API_C + DOWN * 1.3 + LEFT * 0.35))


# ─── inspectors (B03) ───
ZONES = [(0.43, 1.1), (1.3, 1.1), (2.17, 1.1)]          # roof centres of the three areas (x, y)


def pawn(iso, x, y, z, faces=(DARK_TOP, DARK_L, DARK_R), s=1.0, edge=None):
    body = iso.box(x - 0.17 * s, y - 0.17 * s, z, 0.34 * s, 0.34 * s, 0.5 * s, *faces, sw=2)
    if edge:
        for f in body:
            f.set_stroke(edge, 2)
    head = Dot(iso.p(x, y, z + 0.5 * s) + UP * 0.2 * iso.s * s, radius=0.15 * iso.s * s, color=faces[0])
    return VGroup(body, head).set_z_index(4)


def roof_lines(iso=W):
    return VGroup(*[DashedLine(iso.p(xz, BY + 0.08, BH), iso.p(xz, BY + BD - 0.08, BH), color=INK, stroke_width=4, dash_length=0.1)
                    for xz in (0.87, 1.73)]).set_z_index(3)


def inspectors(iso=W):
    return VGroup(*[pawn(iso, x, y, BH) for x, y in ZONES])


def mini_map(c):
    c = np.array(c, dtype=float)
    sheet = Rectangle(width=0.42, height=0.34, fill_color=CARD, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2).move_to(c)
    bar = Rectangle(width=0.42, height=0.08, fill_color=BOX_R, fill_opacity=1, stroke_width=0).move_to(c + UP * 0.13)
    return VGroup(sheet, bar).set_z_index(6)


def mini_spot(i):
    x, y = ZONES[i]
    return W.p(x, y, BH) + np.array([0.36, 0.42, 0])


def inspect_state():
    return VGroup(roof_lines(), inspectors(), *[mini_map(mini_spot(i)) for i in range(3)])


def l_inspectors():
    return T("inspectors", 42).move_to([2.9, 2.75, 0])


# ─── crash (B04) ───
def alarm(iso=W, lit=False):
    post = iso.box(BW - 0.35, BD - 0.35, BH, 0.22, 0.22, 0.45, GREY_TOP, GREY_L, GREY_R, sw=2)
    light = Dot(iso.p(BW - 0.24, BD - 0.24, BH + 0.45) + UP * 0.08, radius=0.13, color=TERRA if lit else GHOST)
    return VGroup(post, light).set_z_index(3)


def crash_file(c, s=1.0):
    c = np.array(c, dtype=float)
    card = RoundedRectangle(width=0.62 * s, height=0.78 * s, corner_radius=0.06 * s, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    lines = VGroup(*[Line(c + np.array([-0.2 * s, (0.15 - 0.2 * k) * s, 0]), c + np.array([0.2 * s, (0.15 - 0.2 * k) * s, 0]),
                          color=BAR1, stroke_width=4) for k in range(2)])
    dot = Dot(c + np.array([0, -0.26 * s, 0]), radius=0.07 * s, color=TERRA)
    return VGroup(card, lines, dot).set_z_index(7)


def crack(iso=W):
    pts = [(2.05, BY, 0.95), (2.25, BY, 0.7), (2.12, BY, 0.5), (2.4, BY, 0.2)]
    c = VMobject(stroke_color=INK, stroke_width=7).set_points_as_corners([iso.p(*q) for q in pts])
    return c.set_z_index(3)


TICK_C = np.array([4.35, 2.2, 0])


def ticks():
    return VGroup(*[check(TICK_C[0] + 0.62 * k, TICK_C[1], 0.16, INK, 7) for k in range(3)])


def l_33():
    return T("3/3", 42).move_to(TICK_C + RIGHT * 0.62 + DOWN * 0.72)


def crash_state():
    return VGroup(alarm(lit=True), crack(), ticks(), l_33())


# ─── the grader (B05) ───
G = Iso(4.62, -2.55, 0.42)          # the grader's small box, right


def grader_box():
    return VGroup(building(G), glass(G, sw=3), pawn(G, 1.3, 1.1, BH, s=1.4), alarm(G))


# ─── triage (B06) ───
SM = Iso(3.1, 0.25, 0.4)            # the building, small, back right


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def small_building():
    return VGroup(building(SM), glass(SM, sw=3), alarm(SM, lit=True), crack(SM))


TB = Iso(-2.6, -2.75, 0.78)         # the triage table
TW, TD, TZ = 6.0, 2.8, 1.0


def table():
    sh = TB.quad([(0.1, -0.35, 0), (TW + 0.3, -0.35, 0), (TW + 0.3, TD - 0.2, 0), (0.1, TD - 0.2, 0)], SHADOW, sw=0).set_z_index(-2)
    L = 0.24
    legs = VGroup(*[TB.box(x, y, 0, L, L, TZ, BOX_TOP, BOX_L, BOX_R, sw=3) for x, y in
                    ((0.15, 0.15), (TW - 0.4, 0.15), (0.15, TD - 0.4), (TW - 0.4, TD - 0.4))])
    top = TB.box(0, 0, TZ, TW, TD, 0.2)
    return VGroup(sh, legs, top)


def tcard(x, y, z=TZ + 0.2):
    """A crash card lying on the table: white slab, DIM outline, two lines, a terracotta dot."""
    slab = TB.box(x, y, z, 1.1, 0.8, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    for f in slab:
        f.set_stroke(DIM, 1.5)
    zt = z + 0.06
    lines = VGroup(*[Line(TB.p(x + 0.4, y + 0.8 * f, zt), TB.p(x + 0.95, y + 0.8 * f, zt), color=BAR1, stroke_width=4) for f in (0.35, 0.65)])
    dot = Dot(TB.p(x + 0.2, y + 0.4, zt), radius=0.07, color=TERRA)
    return VGroup(slab, lines, dot).set_z_index(3)


def num_at(r):
    return TB.p(RANK[r][0] + 0.55, RANK[r][1] - 0.5, TZ + 0.2)


DROP = [(0.4, 1.7), (1.9, 1.6), (0.5, 0.3), (2.0, 0.25), (3.4, 1.0)]
RANK = [(1.6, 1.3), (3.0, 1.3), (4.4, 1.3)]


# ─── patch (B07) ───
def patch_plate(iso=W):
    q = iso.quad([(1.92, BY, 0.1), (2.52, BY, 0.1), (2.52, BY, 1.05), (1.92, BY, 1.05)], BOX_IN1, sw=4)
    return q.set_z_index(4)


LAD_X, LAD_Y0, LAD_Y1 = 4.35, -2.5, 1.3
RUNGS = [-1.75, -0.8, 0.15, 1.1]


def ladder():
    rails = VGroup(Line([LAD_X - 0.45, LAD_Y0, 0], [LAD_X - 0.45, LAD_Y1 + 0.3, 0], color=INK, stroke_width=6),
                   Line([LAD_X + 0.45, LAD_Y0, 0], [LAD_X + 0.45, LAD_Y1 + 0.3, 0], color=INK, stroke_width=6))
    rungs = VGroup(*[Line([LAD_X - 0.45, y, 0], [LAD_X + 0.45, y, 0], color=INK, stroke_width=6) for y in RUNGS])
    return VGroup(rails, rungs)


def rung_check(i):
    return check(LAD_X + 1.05, RUNGS[i] + 0.12, 0.17, INK, 7)


def human(iso=W, x=2.2, y=-1.6):
    body = iso.box(x, y, 0, 0.5, 0.5, 1.05, BOX_TOP, BOX_L, BOX_R, sw=4)
    head = Circle(radius=0.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(iso.p(x + 0.25, y + 0.25, 1.05) + UP * 0.3)
    return VGroup(body, head).set_z_index(6)


def l_patch():
    return T("patch", 42).move_to([1.35, -2.8, 0])


def l_human():
    return T("human", 42).move_to([3.2, -3.0, 0])


def back_arrow():
    a, z = W.p(0.2, BD, BH + 0.3) + UP * 0.2, MAP_C + UP * (MAP_H / 2 + 0.15) + RIGHT * 0.4
    arc = ArcBetweenPoints(a, z, angle=0.8).set_stroke(INK, 5)
    tip = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.14).move_to(z).rotate(-2.3)
    return VGroup(arc, tip)


def new_map_dot():
    return Dot(fp_pts()[1] + np.array([-0.35, 0.05, 0]), radius=0.1, color=TERRA)


# ─── B00: your code, a building; six steps, two setup, four in a loop ───
RING_C, RING_R = (1.3, 1.1), 2.35


def ring_pt(t, iso=W):
    return iso.p(RING_C[0] + RING_R * np.cos(t), RING_C[1] + RING_R * np.sin(t), 0)


def ring():
    pts = [ring_pt(t) for t in np.linspace(0, 2 * np.pi, 73)]
    r = VMobject(stroke_color=INK, stroke_width=5).set_points_smoothly(pts)
    return r.set_z_index(-1)


def tile(iso, x, y, fill=BOX_TOP):
    return iso.box(x, y, 0, 0.55, 0.55, 0.12, fill, BOX_L, BOX_R, sw=3).set_z_index(1)


TILE_ROW = [(-1.97 + 0.6 * k, 0.27 - 0.6 * k) for k in range(6)]  # six tiles in a row on the floor, in front
SETUP_AT = [(0.68, 6.88), (1.28, 7.48)]                              # two tiles set aside, left (setup)
LOOP_T = [np.pi * 0.82, np.pi * 1.1, np.pi * 1.42, np.pi * 1.7]    # four tiles on the ring's front arc


def loop_tile_xy(k):
    t = LOOP_T[k]
    return RING_C[0] + RING_R * np.cos(t) - 0.27, RING_C[1] + RING_R * np.sin(t) - 0.27


def b00_state():
    tiles = VGroup(*[tile(W, *SETUP_AT[k], GREY_TOP) for k in range(2)], *[tile(W, *loop_tile_xy(k)) for k in range(4)])
    return VGroup(ring(), tiles, T("setup", 42).move_to([-3.9, 0.15, 0]), T("loop", 42).move_to([3.65, -2.6, 0]))


class B00_Building(Scene):
    def construct(self):
        bld = building()
        body = VGroup(bld[1], bld[2], bld[3])
        body.shift(UP * 5)
        self.add(body)
        self.play(body.animate.shift(DOWN * 5), run_time=0.7, rate_func=ease_in)
        self.play(FadeIn(bld[0]), FadeIn(label_code()), run_time=0.35)
        until(self, "has six steps", lead=0.3)
        tiles = [tile(W, *xy) for xy in TILE_ROW]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[GrowFromCenter(t) for t in tiles], lag_ratio=0.2), run_time=rt)
        until(self, "Two are setup", lead=0.3)
        tgt = [tile(W, *SETUP_AT[k], GREY_TOP) for k in range(2)]
        rt = guard(self, 0.8)
        self.play(*[Transform(tiles[k], tgt[k]) for k in range(2)], run_time=rt)
        self.play(FadeIn(T("setup", 42).move_to([-3.9, 0.15, 0])), run_time=0.3)
        until(self, "Four run as a loop", lead=0.4)
        r = ring()
        rt = guard(self, 0.9)
        self.play(Create(r), *[tiles[2 + k].animate.move_to(tile(W, *loop_tile_xy(k)).get_center()) for k in range(4)], run_time=rt)
        self.play(FadeIn(T("loop", 42).move_to([3.65, -2.6, 0])), run_time=0.3)
        until(self, "find, prove", lead=0.2)
        rider = Dot(ring_pt(LOOP_T[0]), radius=0.13, color=TERRA).set_z_index(-1)
        self.add(rider)
        arc = VMobject().set_points_smoothly([ring_pt(t) for t in np.linspace(LOOP_T[0], LOOP_T[0] + 2 * np.pi, 73)])
        rt = guard(self, 1.4)
        self.play(MoveAlongPath(rider, arc), run_time=rt, rate_func=linear)
        done(self)


# ─── B01: the threat map ───
class B01_ThreatMap(Scene):
    def construct(self):
        bld = building()
        self.add(bld, label_code())
        carry = b00_state()
        self.add(carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "the threat model", lead=0.3)
        tm = threat_map()
        tm.shift(LEFT * 4)
        self.add(tm)
        rt = guard(self, 0.6)
        self.play(tm.animate.shift(RIGHT * 4), run_time=rt)
        fp = footprint()
        self.play(Create(fp), FadeIn(label_map()), run_time=0.5)
        until(self, "what you trust", lead=0.3)
        tz = trusted_zone()
        rt = guard(self, 0.5)
        self.play(FadeIn(tz), run_time=rt)
        tl = T("trusted", 42).move_to([-1.9, 1.75, 0])
        lead = Line(tl.get_left() + LEFT * 0.3, MAP_C + np.array([0.45, 0.25, 0]), color=INK, stroke_width=3)
        self.play(FadeIn(tl), Create(lead), run_time=0.35)
        until(self, "where outside input gets in", lead=0.3)
        md = map_doors()
        dd = door_dot()
        rt = guard(self, 0.5)
        self.play(*[GrowFromCenter(d) for d in md], GrowFromCenter(dd), run_time=rt)
        until(self, "a misread trust boundary", lead=0.3)
        bd = boundary()
        rt = guard(self, 0.6)
        self.play(Create(bd), run_time=rt)
        until(self, "false positives", lead=0.3)
        self.play(Indicate(bd, color=None, scale_factor=1.06), run_time=0.5)
        done(self)


def b01_state():
    tl = T("trusted", 42).move_to([-1.9, 1.75, 0])
    lead = Line(tl.get_left() + LEFT * 0.3, MAP_C + np.array([0.45, 0.25, 0]), color=INK, stroke_width=3)
    return VGroup(tl, lead)


# ─── B02: the sandbox ───
class B02_Sandbox(Scene):
    def construct(self):
        bld = building()
        mp = map_full()
        self.add(bld, label_code(), mp, label_map(), door_dot())
        carry = b01_state()
        self.add(carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "a sealed glass box", lead=0.4)
        gl = glass()
        gl.shift(UP * 5.5)
        self.add(gl)
        rt = guard(self, 0.7)
        self.play(gl.animate.shift(DOWN * 5.5), run_time=rt, rate_func=ease_in)
        lc_old = label_code()
        sb = T("sandbox", 42).move_to([-2.75, -1.6, 0])
        self.play(FadeIn(sb), run_time=0.3)
        until(self, "Network only during setup", lead=0.3)
        wb, cb = web(), cable()
        rt = guard(self, 0.6)
        self.play(FadeIn(wb), Create(cb), run_time=rt)
        until(self, "snapshot it", lead=0.3)
        sc = snap_card()
        rt = guard(self, 0.45)
        self.play(GrowFromPoint(sc, W.p(GX, GY + GD / 2, GH / 2)), run_time=rt)
        until(self, "cut the cable", lead=0.25)
        ce = cut_ends()
        rt = guard(self, 0.45)
        self.play(ReplacementTransform(cb, ce), run_time=rt)
        until(self, "leaving one line out", lead=0.3)
        ab, al = api_block(), api_line()
        ab.shift(DOWN * 4)
        self.add(ab)
        rt = guard(self, 0.6)
        self.play(ab.animate.shift(UP * 4), run_time=rt)
        self.play(Create(al), FadeIn(T("model API", 42).move_to(API_C + DOWN * 1.3 + LEFT * 0.35)), run_time=0.45)
        until(self, "No credentials inside", lead=0.3)
        k = key_icon(KEY_C)
        rt = guard(self, 0.35)
        self.play(FadeIn(k, shift=RIGHT * 0.3), run_time=rt)
        self.play(Create(cross(KEY_C + RIGHT * 0.45, 0.42)), run_time=0.35)
        done(self)


# ─── B03: recon, then inspectors in parallel ───
class B03_Inspectors(Scene):
    def construct(self):
        bld = building()
        mp = map_full()
        st = sandbox_state()
        keep = VGroup(st[0], st[1], st[2], st[8], st[9])          # glass, API block + line, labels
        drop = VGroup(st[3], st[4], st[5], st[6], st[7])          # web, cut ends, snapshot, key, cross
        self.add(bld, mp, label_map(), door_dot(), keep, drop, label_code())
        self.play(FadeOut(drop), run_time=0.4)
        until(self, "One agent splits", lead=0.3)
        rp = pawn(W, 0.1, 1.1, BH, (GREY_TOP, GREY_L, GREY_R), edge=INK)
        rt = guard(self, 0.35)
        self.play(FadeIn(rp, shift=DOWN * 0.4), run_time=rt)
        lines = roof_lines()
        rt = guard(self, 1.3)
        self.play(rp.animate.shift(W.v(2.3, 0, 0)), Create(lines, lag_ratio=0.5), run_time=rt, rate_func=linear)
        ar = T("areas", 42).move_to([4.25, 1.6, 0])
        self.play(FadeOut(rp), FadeIn(ar), run_time=0.35)
        until(self, "Inspectors search them", lead=0.3)
        ins = inspectors()
        for p in ins:
            p.shift(UP * 3.5)
        self.add(ins)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[p.animate.shift(DOWN * 3.5) for p in ins], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(l_inspectors()), run_time=0.3)
        until(self, "the threat model in hand", lead=0.3)
        mms = [mini_map(MAP_C + UP * 0.2) for _ in range(3)]
        self.add(*mms)
        rt = guard(self, 0.9)
        self.play(*[MoveAlongPath(m, ArcBetweenPoints(MAP_C + UP * 0.2, mini_spot(i), angle=-0.6)) for i, m in enumerate(mms)], run_time=rt)
        until(self, "short prompts", lead=0.3)
        self.play(*[Indicate(p, color=None, scale_factor=1.12) for p in ins], run_time=0.5)
        done(self)


def b03_labels():
    return VGroup(T("areas", 42).move_to([4.25, 1.6, 0]), l_inspectors())


def base_scene():
    """Building, map, door dot, the glass and API line with their labels (as B03 opens after its fades)."""
    st = sandbox_state()
    return VGroup(building(), map_full(), label_map(), door_dot(), st[0], st[1], st[2], st[8], st[9], label_code())


# ─── B04: an input file that crashes it, 3/3 ───
class B04_Crash(Scene):
    def construct(self):
        base = base_scene()
        ins = inspect_state()
        lab = b03_labels()
        self.add(base, ins, lab)
        self.play(FadeOut(lab), run_time=0.4)
        until(self, "memory bugs in C", lead=0.3)
        al = alarm()
        rt = guard(self, 0.4)
        self.play(FadeIn(al, shift=DOWN * 0.3), run_time=rt)
        until(self, "an input file", lead=0.4)
        start = W.p(*ZONES[2], BH) + np.array([0.55, 0.35, 0])
        cf = crash_file(start)
        rt = guard(self, 0.35)
        self.play(GrowFromCenter(cf), run_time=rt)
        cl = T("crash file", 42).move_to([4.0, 2.25, 0])
        self.play(FadeIn(cl), run_time=0.3)
        until(self, "crashes the program", lead=0.3)
        door = W.p(1.33, BY, 0.45)
        rt = guard(self, 0.8)
        self.play(FadeOut(cl), MoveAlongPath(cf, ArcBetweenPoints(start, door, angle=-0.8)), run_time=rt)
        self.play(cf.animate.scale(0.3).set_opacity(0), run_time=0.3)
        self.remove(cf)
        until(self, "three times out of three", lead=0.35)
        tk = ticks()
        for k in range(3):
            self.play(al[1].animate.set_color(TERRA), Create(tk[k]), run_time=0.25)
            self.play(al[1].animate.set_color(GHOST), run_time=0.15)
        self.play(FadeIn(l_33()), run_time=0.3)
        until(self, "raising the alarm", lead=0.3)
        ck = crack()
        self.play(al[1].animate.set_color(TERRA), Flash(al[1].get_center(), color=TERRA, line_length=0.2, flash_radius=0.35),
                  Create(ck), run_time=0.5)
        done(self)


# ─── B05: a second agent, in a fresh box; only the file crosses ───
class B05_Grader(Scene):
    def construct(self):
        base = base_scene()
        ins = inspect_state()
        cs = crash_state()
        self.add(base, ins, cs)
        apis = VGroup(base[5], base[6], base[8])                 # API block, line, label
        self.play(FadeOut(apis), FadeOut(cs[2]), FadeOut(cs[3]), run_time=0.4)
        until(self, "a second agent", lead=0.3)
        gb = grader_box()
        gb.shift(DOWN * 4.5)
        self.add(gb)
        rt = guard(self, 0.7)
        self.play(gb.animate.shift(UP * 4.5), run_time=rt)
        gl = T("grader", 42).move_to([5.3, 0.45, 0])
        self.play(FadeIn(gl), run_time=0.3)
        until(self, "Only the crash file", lead=0.3)
        pages = VGroup(*[crash_file(W.p(*ZONES[2], BH) + np.array([-0.05 + 0.08 * k, 0.75 + 0.08 * k, 0]), 0.8) for k in range(3)])
        for pg in pages:
            pg[2].set_color(BAR2)
        a = W.p(*ZONES[2], BH) + np.array([0.55, 0.35, 0])
        cf = crash_file(a)
        self.play(FadeIn(pages), GrowFromCenter(cf), run_time=0.35)
        z = G.p(1.8, 1.0, 1.2)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(cf, ArcBetweenPoints(a, z, angle=-0.7)), run_time=rt)
        self.play(cf.animate.scale(0.5), Indicate(pages, color=None, scale_factor=1.06), run_time=0.35)
        ol = T("only the file", 42).move_to([2.1, 2.85, 0])
        self.play(FadeIn(ol), run_time=0.3)
        until(self, "a verifier that must build", lead=0.3)
        glt = gb[3][1]
        self.play(glt.animate.set_color(TERRA), Flash(glt.get_center(), color=TERRA, line_length=0.16, flash_radius=0.3), run_time=0.45)
        ck = check(2.85, -3.0, 0.2, INK, 8)
        rt = guard(self, 0.35)
        self.play(Create(ck), run_time=rt)
        pa = T("per Anthropic", 36).move_to([4.85, -3.0, 0])
        self.play(FadeIn(pa), run_time=0.3)
        until(self, "a failed proof", lead=0.35)
        a2 = W.p(*ZONES[0], BH) + np.array([0.55, 0.35, 0])
        c2 = crash_file(a2)
        z2 = G.p(0.6, 1.0, 1.2)
        self.play(GrowFromCenter(c2), glt.animate.set_color(GHOST), FadeOut(ck), FadeOut(cf), run_time=0.3)
        rt = guard(self, 0.8)
        self.play(MoveAlongPath(c2, ArcBetweenPoints(a2, z2, angle=-0.55)), run_time=rt)
        q = T("?", 64, INK, bold=True).move_to([4.1, 0.35, 0])
        self.play(FadeIn(q), c2.animate.scale(0.5), run_time=0.35)
        done(self)


def b05_state():
    """What B05 leaves on stage (beyond the base without its API parts)."""
    c2 = crash_file(G.p(0.6, 1.0, 1.2)).scale(0.5)
    pages = VGroup(*[crash_file(W.p(*ZONES[2], BH) + np.array([-0.05 + 0.08 * k, 0.75 + 0.08 * k, 0]), 0.8) for k in range(3)])
    for pg in pages:
        pg[2].set_color(BAR2)
    return VGroup(grader_box(), c2, pages, T("grader", 42).move_to([5.3, 0.45, 0]), T("only the file", 42).move_to([2.1, 2.85, 0]),
                  T("per Anthropic", 36).move_to([4.85, -3.0, 0]), T("?", 64, INK, bold=True).move_to([4.1, 0.35, 0]))


def main_building():
    """The building in its glass with the map, door dot, inspectors, alarm (lit) and the crack: the B05/B06 stage."""
    st = sandbox_state()
    return VGroup(building(), glass(), door_dot(), inspect_state(), alarm(lit=True), crack())


# ─── B06: triage on a table ───
class B06_Triage(Scene):
    def construct(self):
        mb = main_building()
        mp = VGroup(map_full(), label_map())
        cl = label_code(); sb = T("sandbox", 42).move_to([-2.75, -1.6, 0])
        carry = b05_state()
        self.add(mb, mp, cl, sb, carry)
        self.play(FadeOut(carry), FadeOut(mp), FadeOut(cl), FadeOut(sb), run_time=0.4)
        mv = VGroup(mb[0], mb[1], mb[4], mb[5])
        self.play(FadeOut(mb[2]), FadeOut(mb[3]), to_rig(mv, W, SM), run_time=0.6)
        until(self, "Step five, triage", lead=0.3)
        tb = table()
        tb.shift(DOWN * 4)
        self.add(tb)
        rt = guard(self, 0.6)
        self.play(tb.animate.shift(UP * 4), run_time=rt)
        tl = T("triage", 42).move_to([-4.6, -2.75, 0])
        self.play(FadeIn(tl), run_time=0.3)
        until(self, "Many crashes", lead=0.4)
        cards = [tcard(*xy) for xy in DROP]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.7) for c in cards], lag_ratio=0.12), run_time=rt, rate_func=ease_in)
        until(self, "merges the duplicates", lead=0.3)
        rt = guard(self, 0.7)
        self.play(cards[1].animate.move_to(tcard(DROP[0][0], DROP[0][1], TZ + 0.3).get_center()),
                  cards[3].animate.move_to(tcard(DROP[2][0], DROP[2][1], TZ + 0.3).get_center()), run_time=rt)
        dl = T("duplicates", 42).move_to([-4.3, 0.6, 0])
        self.play(FadeIn(dl), run_time=0.3)
        until(self, "each bug is ranked", lead=0.3)
        stacks = [VGroup(cards[0], cards[1]), VGroup(cards[2], cards[3]), cards[4]]
        order = [2, 0, 1]
        rt = guard(self, 0.9)
        self.play(FadeOut(dl), *[stacks[o].animate.shift(TB.v(RANK[r][0] - DROP[[0, 2, 4][o]][0], RANK[r][1] - DROP[[0, 2, 4][o]][1], 0))
                                  for r, o in enumerate(order)], run_time=rt)
        nums = VGroup(*[T(str(r + 1), 44, INK, bold=True).move_to(num_at(r)) for r in range(3)])
        self.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.2), run_time=0.5)
        until(self, "how far would the damage spread", lead=0.3)
        self.play(Indicate(stacks[order[0]], color=None, scale_factor=1.08), run_time=0.5)
        done(self)


def b06_state():
    t = table()
    out = VGroup(t, T("triage", 42).move_to([-4.6, -2.75, 0]))
    for r, o in enumerate([2, 0, 1]):
        x, y = RANK[r]
        out.add(tcard(x, y))
        if o in (0, 1):
            out.add(tcard(x, y, TZ + 0.3))
        out.add(T(str(r + 1), 44, INK, bold=True).move_to(num_at(r)))
    return out


# ─── B07: the patch climbs the ladder; lessons feed the next round; a human owns it ───
class B07_Patch(Scene):
    def construct(self):
        small = small_building()
        carry = b06_state()
        self.add(small, carry)
        self.play(FadeOut(carry), run_time=0.4)
        self.play(to_rig(small, SM, W), run_time=0.6)
        mb = small
        until(self, "Step six, the fix", lead=0.3)
        pp = patch_plate()
        pp.shift(RIGHT * 2.5)
        self.add(pp)
        rt = guard(self, 0.5)
        self.play(pp.animate.shift(LEFT * 2.5), run_time=rt)
        self.play(mb[2][1].animate.set_color(GHOST), FadeIn(l_patch()), run_time=0.3)
        until(self, "climbs a ladder", lead=0.3)
        ld = ladder()
        rt = guard(self, 0.5)
        self.play(GrowFromEdge(ld, DOWN), run_time=rt)
        for i, ph in enumerate(["it builds", "the old crash stops", "the old tests pass", "a fresh agent attacks it"]):
            until(self, ph, lead=0.1)
            rt = guard(self, 0.3)
            self.play(Create(rung_check(i)), run_time=rt)
        until(self, "The lessons feed", lead=0.3)
        mp = map_full()
        rt = guard(self, 0.4)
        self.play(FadeIn(mp), run_time=rt)
        ba = back_arrow()
        self.play(Create(ba), run_time=0.5)
        self.play(GrowFromCenter(new_map_dot()), FadeIn(T("next round", 42).move_to([-4.35, -0.75, 0])), run_time=0.35)
        until(self, "not that the patch is safe", lead=0.3)
        self.play(Indicate(pp, color=None, scale_factor=1.15), run_time=0.45)
        until(self, "A human owns", lead=0.3)
        hm = human()
        hm.shift(DOWN * 4)
        self.add(hm)
        rt = guard(self, 0.5)
        self.play(hm.animate.shift(UP * 4), run_time=rt)
        self.play(FadeIn(l_human()), run_time=0.3)
        done(self)


# ─── B08: why now: 1,596 disclosed, 97 patched (per Anthropic) ───
ST_ISO = Iso(-1.6, -2.75, 0.8)
NSLAB = 16


def slab(iso, x, y, i, fill):
    return iso.box(x, y, i * 0.24, 1.4, 1.4, 0.18, fill, BOX_L, BOX_R, sw=2)


def stack_tall(n=NSLAB):
    return VGroup(*[slab(ST_ISO, 0, 0, i, (BAR1, BAR2, BAR3)[i % 3]) for i in range(n)])


def stack_short():
    return VGroup(slab(ST_ISO, 3.4, -1.6, 0, BAR1))


class B08_Count(Scene):
    def construct(self):
        mb = VGroup(building(), glass(), alarm(), crack(), patch_plate(), ladder(), *[rung_check(i) for i in range(4)], human(),
                    map_full(), back_arrow(), new_map_dot())
        carry = VGroup(l_patch(), T("next round", 42).move_to([-4.35, -0.75, 0]), l_human())
        self.add(mb, carry)
        self.play(FadeOut(mb), FadeOut(carry), run_time=0.45)
        until(self, "by May", lead=0.3)
        tall = stack_tall()
        v = ValueTracker(0)
        num = always_redraw(lambda: T(f"{int(round(v.get_value())):,}", 110, INK, bold=True).move_to([-1.6, 2.5, 0]))
        self.add(num)
        rt = guard(self, 2.2)
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.25) for s in tall], lag_ratio=0.12),
                  v.animate.set_value(1596), run_time=rt, rate_func=linear)
        self.play(FadeIn(T("disclosed", 42).move_to([-3.95, 0.3, 0])), FadeIn(T("per Anthropic", 36).move_to([1.7, 2.45, 0])),
                  run_time=0.35)
        until(self, "ninety-seven were patched", lead=0.3)
        sh = stack_short()
        n97 = T("97", 64, INK, bold=True).move_to(ST_ISO.p(4.1, -0.9, 0.3) + UP * 0.9)
        rt = guard(self, 0.5)
        self.play(FadeIn(sh, shift=DOWN * 0.3), FadeIn(n97), run_time=rt)
        self.play(FadeIn(T("patched", 42).move_to([4.05, -2.1, 0])), Create(check(2.95, -0.3, 0.2, INK, 8)), run_time=0.4)
        until(self, "Finding has outrun fixing", lead=0.3)
        self.play(Indicate(tall, color=None, scale_factor=1.03), run_time=0.6)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Building, B01_ThreatMap, B02_Sandbox, B03_Inspectors, B04_Crash, B05_Grader, B06_Triage, B07_Patch, B08_Count):
    _cls.play = ST.play
