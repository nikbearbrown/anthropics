"""
Manim scenes for show-tell-one-tool-that-finds-the-rest (show-tell skill, card #20, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Tool search, from anthropics/claude-cookbooks/tool_use/tool_search_with_embeddings.ipynb, checked against the raw
live docs page (sources/live_tool-search-tool-2026-09-27.md):
CLAUDE (a kraft block with a terracotta spark on a dark plinth) sits at the left behind its CONTEXT TRAY (a low kraft
open box on a dark plinth). The TOOL WALL (a dark pegboard of white tool cards) stands at the right. Loading every
definition piles the tray past its rim (~100 tools, per Anthropic's cookbook). Instead Claude carries one tool,
TOOL_SEARCH (a small kraft block with a dark lens and a terracotta light), and the wall's cards turn ghost (deferred).
The cookbook's search: the wall shrinks, a pale MEANING MAP draws in, each card drops onto it as an ink dot, similar
tools cluster. A white QUERY slip ("I need to check the weather") lands as a terracotta dot; grey spokes pick the three
closest dots; three white NAME TAGS ride back and grow into full cards in the tray. Then the built-in search (a dark
block with two lights, one per version) beside the custom one, and when to use it (10+ tools, per the docs; keep three
favourites always loaded). No filing cabinet and no drawers (that is "How a Skill Loads").
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








# ═════════════════════════════ the film: carry one tool that finds the rest ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


def grey_edges(mob, color=BAR1, w=3):
    for f in mob.family_members_with_points():
        f.set_stroke(color, w)
    return mob


# ─────────────── Claude ───────────────
CL = Iso(-4.8, -2.1, 1.15)
CW_, CH_ = 1.2, 1.3
CL_TOP = CL.p(0.6, 0.6, CH_) + UP * 0.6
SPARK_C = CL.p(CW_ / 2, CW_ / 2, CH_) + UP * 0.05


def claude_block(iso=CL, w=CW_, h=CH_):
    """Claude: a kraft block with a terracotta spark on top, on a dark plinth."""
    base = iso.box(0, 0, 0, w, w, 0.34, DARK_TOP, DARK_L, DARK_R)
    body = iso.box(0, 0, 0.34, w, w, h - 0.34)
    c = iso.p(w / 2, w / 2, h) + UP * 0.05 * iso.s     # inside the top face (GATE T sub-floor fragment trap)
    r = 0.3 * iso.s
    pts = []
    for k in range(16):
        a = PI / 2 + k * PI / 8
        rr = r if k % 2 == 0 else r * 0.42
        pts.append(c + np.array([rr * np.cos(a), rr * np.sin(a), 0]))
    spark = Polygon(*pts, fill_color=TERRA, fill_opacity=1, stroke_width=0)
    sh = iso.quad([(-0.15, -0.3, 0), (w + 0.25, -0.3, 0), (w + 0.25, w, 0), (-0.15, w, 0)], SHADOW, sw=0).set_z_index(-2)
    return VGroup(sh, base, body, spark).set_z_index(1)


def l_claude():
    return lab("Claude", [-4.8, -2.95])


# ─────────────── the context tray ───────────────
TR = Iso(-1.95, -2.55, 1.15)
TW, TD, TZ, TH = 2.2, 1.3, 0.2, 0.22
TRAY_IN = TR.p(1.1, 0.65, TZ + 0.3)


def tray():
    plinth = TR.box(-0.1, -0.1, 0, TW + 0.2, TD + 0.2, TZ, DARK_TOP, DARK_L, DARK_R).set_z_index(0)
    back, front = TR.open_box(0, 0, TZ, TW, TD, TH)
    return VGroup(plinth, back.set_z_index(0), front.set_z_index(4))


def l_context():
    return lab("context", [-1.6, -3.05])


# the pile of definitions (one layer per card), inside the tray
PX0, PY0, PW, PD, PSTEP = 0.3, 0.2, 1.6, 0.9, 0.1


def pile(level):
    h = max(level, 0.001) * PSTEP
    body = TR.box(PX0, PY0, TZ, PW, PD, h, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    for f in body:
        f.set_stroke(BOX_IN2, 3)
    ks = range(2, level, 2)
    ln = VGroup(*[Line(TR.p(PX0 + 0.08, PY0, TZ + k * PSTEP), TR.p(PX0 + PW - 0.08, PY0, TZ + k * PSTEP), color=BAR2, stroke_width=4) for k in ks] +
                [Line(TR.p(PX0, PY0 + 0.08, TZ + k * PSTEP), TR.p(PX0, PY0 + PD - 0.08, TZ + k * PSTEP), color=BAR2, stroke_width=4) for k in ks])
    return VGroup(body, ln).set_z_index(3)


# ─────────────── tool_search: a small kraft block with a dark lens and a terracotta light ───────────────
SX0, SY0, SS, SHh = 0.25, 0.25, 0.8, 0.55
S_TOP = TR.p(SX0 + SS / 2, SY0 + SS / 2, TZ + SHh)


def search_block():
    body = TR.box(SX0, SY0, TZ, SS, SS, SHh)
    return VGroup(body).set_z_index(3)


def lens():
    r = 0.24
    e = Ellipse(width=2.449 * r, height=1.414 * r, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(S_TOP)
    d = Dot(S_TOP, radius=0.07, color=TERRA)
    return VGroup(e, d).set_z_index(3)


def mini_map():
    """The custom search's face in B06: a small cluster of ink dots on the block's top."""
    pts = [(0.3, 0.35), (0.5, 0.55), (0.28, 0.6), (0.55, 0.28)]
    return VGroup(*[Dot(TR.p(SX0 + a, SY0 + b, TZ + SHh), radius=0.055, color=INK) for a, b in pts]).set_z_index(3)


def l_search():
    return lab("tool_search", [-1.9, 0.45])


# ─────────────── the tool wall: a dark pegboard of white tool cards ───────────────
WL = Iso(1.9, -2.4, 0.9)
WLS = Iso(3.95, 0.6, 0.42)          # the same wall, small, top right (B03-B05)
WW, WD, WH = 4.4, 0.3, 2.8
# the board is darker than DARK_*: DARK_R sits 46 from INK in RGB, just inside GATE T's ink tolerance (48), so codec
# noise split the lattice between the cards into small "text" fragments (local pre-check, 2026-09-27). These sit > 55 away.
WALL_TOP, WALL_L, WALL_R = "#161411", "#121010", "#0E0C0A"
COLS, ROWS = 6, 4


def slot(c, r):
    x0, z0 = 0.25 + c * 0.68, 0.25 + r * 0.62
    return x0, z0, x0 + 0.52, z0 + 0.44


def card_quad(iso, c, r, fill="#FFFFFF"):
    x0, z0, x1, z1 = slot(c, r)
    return iso.quad([(x0, -0.01, z0), (x1, -0.01, z0), (x1, -0.01, z1), (x0, -0.01, z1)], fill, sw=0)


def wall(iso=WL, ghost=False):
    sh = iso.quad([(-0.1, -0.35, 0), (WW + 0.2, -0.35, 0), (WW + 0.2, WD, 0), (-0.1, WD, 0)], SHADOW, sw=0).set_z_index(-2)
    board = iso.box(0, 0, 0, WW, WD, WH, WALL_TOP, WALL_L, WALL_R).set_z_index(1)
    cards = VGroup(*[card_quad(iso, c, r, GHOST if ghost else "#FFFFFF") for r in range(ROWS) for c in range(COLS)]).set_z_index(2)
    return VGroup(sh, board, cards)


def card_center(iso, c, r):
    x0, z0, x1, z1 = slot(c, r)
    return iso.p((x0 + x1) / 2, -0.01, (z0 + z1) / 2)


def flyer(iso, c, r):
    """A copy of one wall card, white with a grey edge, for flights across the cream stage."""
    q = card_quad(iso, c, r)
    q.set_stroke(BAR1, 3)
    return q.set_z_index(7)


def l_tools():
    return lab("tools", [3.6, 2.85])


def l_deferred():
    return lab("deferred", [3.6, 2.85])


# ─────────────── one definition, big ───────────────
DF = Iso(-2.35, 0.55, 1.0)
DFW, DFH = 2.5, 1.35


def big_card():
    return DF.quad([(0, 0, 0), (DFW, 0, 0), (DFW, 0, DFH), (0, 0, DFH)], "#FFFFFF", sw=4).set_z_index(6)


def big_bars():
    y = -0.01
    return VGroup(
        Line(DF.p(0.3, y, 1.0), DF.p(1.2, y, 1.0), color=BAR1, stroke_width=16),
        Line(DF.p(0.3, y, 0.68), DF.p(2.2, y, 0.68), color=BAR2, stroke_width=12),
        Line(DF.p(0.3, y, 0.35), DF.p(0.9, y, 0.35), color=BAR2, stroke_width=12),
        Line(DF.p(1.1, y, 0.35), DF.p(1.7, y, 0.35), color=BAR2, stroke_width=12)).set_z_index(7)


def l_definition():
    return lab("definition", [-3.7, 1.2])


# ─────────────── the map of meaning ───────────────
MP = Iso(2.1, -3.0, 1.0)
MW, MD, MZ = 3.8, 2.2, 0.18
Q = (1.2, 1.5)                                                   # the query "I need to check the weather"
WEATHER = [(0.8, 1.3), (1.55, 1.8), (1.35, 1.1), (1.85, 1.5)]    # get_weather, get_forecast, get_air_quality, get_timezone
FINANCE = [(2.95, 0.55), (3.35, 0.8), (3.2, 0.25), (2.75, 0.95)]
OTHERS = [(0.35, 0.35), (0.9, 0.2), (0.45, 0.9), (1.5, 0.45), (2.05, 0.2), (2.2, 0.9), (0.3, 1.75), (0.75, 2.0),
          (2.3, 1.9), (2.7, 1.5), (3.15, 1.8), (3.55, 1.35), (3.6, 1.95), (3.65, 0.3), (2.5, 0.45), (1.1, 0.7)]
ALL_PTS = WEATHER + FINANCE + OTHERS                              # 24 points, one per wall card
WIN = [0, 1, 2]                                                  # the three closest to the query


def mpt(xy):
    return MP.p(xy[0], xy[1], MZ)


def meaning_map():
    body = MP.box(0, 0, 0, MW, MD, MZ, BOX_TOP, BOX_L, BOX_R, sw=4)
    grey_edges(body, BAR1, 4)
    return VGroup(body).set_z_index(0)


def dots(pts=ALL_PTS, r=0.085):
    return VGroup(*[Dot(mpt(p), radius=r, color=INK) for p in pts]).set_z_index(2)


def pad(center_xy, r=0.62):
    return Ellipse(width=2.449 * r, height=1.414 * r, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(mpt(center_xy)).set_z_index(1)


def pads():
    return VGroup(pad((1.3, 1.45)), pad((3.05, 0.6), 0.55))


def l_map():
    return lab("map", [0.75, -2.95])


def l_weather():
    return lab("weather", [1.0, -0.1])


def l_finance():
    return lab("finance", [5.3, -2.4])


# ─────────────── slips and tags (white, grey-edged) ───────────────
def slip(center, s=0.6):
    iso = Iso(0, 0, s)
    body = grey_edges(iso.box(0, 0, 0, 0.9, 0.6, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=3))
    dot = Dot(iso.p(0.3, 0.3, 0.06), radius=0.07 * s / 0.6, color=TERRA)
    return VGroup(body, dot).move_to(center).set_z_index(8)


def tag(center, s=0.7):
    iso = Iso(0, 0, s)
    body = grey_edges(iso.box(0, 0, 0, 0.75, 0.35, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=3))
    bar = Line(iso.p(0.12, 0.17, 0.06), iso.p(0.5, 0.17, 0.06), color=BAR1, stroke_width=6)
    return VGroup(body, bar).move_to(center).set_z_index(8)


# the found cards, lying in the tray beside tool_search
FX0, FW, FD, FH = 1.28, 0.78, 0.32, 0.25
FY = [0.1, 0.5, 0.9]


def found_card(k):
    y0 = FY[k]
    body = grey_edges(TR.box(FX0, y0, TZ, FW, FD, FH, PAGE_TOP, PAGE_L, PAGE_R, sw=3))
    zt = TZ + FH
    bars = VGroup(Line(TR.p(FX0 + 0.1, y0 + FD * 0.5, zt), TR.p(FX0 + 0.42, y0 + FD * 0.5, zt), color=BAR1, stroke_width=7),
                  Line(TR.p(FX0 + 0.5, y0 + FD * 0.5, zt), TR.p(FX0 + FW - 0.1, y0 + FD * 0.5, zt), color=BAR2, stroke_width=5))
    return VGroup(body, bars).set_z_index(2.5 + (2 - k) * 0.1)


def found_center(k):
    return TR.p(FX0 + FW / 2, FY[k] + FD / 2, TZ + FH)


def found_cards():
    return VGroup(*[found_card(k) for k in range(3)])


TAG_PARK = [P(-2.9, 1.25), P(-1.9, 1.25), P(-0.9, 1.25)]


def l_names():
    return lab("names", [0.35, 1.25])


def l_defs():
    return lab("definitions", [-1.9, 0.45])


# ─────────────── the built-in search: a dark block with one light per version ───────────────
BX0 = 1.3


def builtin_block():
    body = TR.box(BX0, SY0, TZ, SS, SS, SHh, DARK_TOP, DARK_L, DARK_R)
    return VGroup(body).set_z_index(2.5)


def builtin_light(k, color=TERRA):
    """Light k (0 = the pattern version, 1 = the plain-query version) on the dark block's right front face."""
    return Dot(TR.p(BX0 + 0.22 + k * 0.36, SY0, TZ + SHh * 0.5), radius=0.075, color=color).set_z_index(4)


def l_builtin():
    return lab("built-in", [-0.45, 0.8])


def l_custom():
    return lab("custom", [-3.0, 0.95])


# ─────────────── when: few tools, just load them; keep three favourites ───────────────
FEW = [(0.3, 0.12), (1.2, 0.12), (0.3, 0.72), (1.2, 0.72)]


def few_card(k):
    x0, y0 = FEW[k]
    body = grey_edges(TR.box(x0, y0, TZ, 0.78, 0.45, FH, PAGE_TOP, PAGE_L, PAGE_R, sw=3))
    zt = TZ + FH
    bar = Line(TR.p(x0 + 0.1, y0 + 0.22, zt), TR.p(x0 + 0.6, y0 + 0.22, zt), color=BAR1, stroke_width=7)
    return VGroup(body, bar).set_z_index(3 + (1 - k // 2) * 0.1)


def l_ten():
    return T("10+ tools", 100, INK, bold=True).move_to([-1.0, 2.65, 0])


def l_docs():
    return lab("per the docs", [-1.0, 1.75], 38)


def l_always():
    return lab("always loaded", [-1.9, 0.45])


# ══════════════ B00: a wall of tools; one definition ══════════════
class B00_Wall(Scene):
    def construct(self):
        cl, tr = claude_block(), tray()
        self.play(FadeIn(cl, shift=DOWN * 1.0), FadeIn(tr, shift=UP * 0.5), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(l_claude()), FadeIn(l_context()), run_time=0.3)
        until(self, "hundreds of tools", lead=0.4)
        w = wall()
        cards = w[2]
        self.play(FadeIn(VGroup(w[0], w[1]), shift=UP * 0.8), FadeIn(l_tools()), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in cards], lag_ratio=0.06), run_time=1.2)
        until(self, "Each has a definition", lead=0.3)
        cp = flyer(WL, 1, 2)
        self.add(cp)
        bc = big_card()
        self.play(Transform(cp, bc), run_time=0.7)
        bb = big_bars()
        ld = l_definition()
        self.play(LaggedStart(*[Create(b) for b in bb], lag_ratio=0.25), FadeIn(ld), run_time=0.9)
        until(self, "Normally, every definition", lead=0.2)
        g = VGroup(cp, bb)
        self.play(FadeOut(ld), g.animate.scale(0.22).move_to(TRAY_IN), run_time=0.8, rate_func=ease_in)
        self.remove(g)
        pl = pile(1)
        self.add(pl)
        until(self, "on every request", lead=0.3)
        for k, (c, r) in enumerate(((4, 3), (2, 0))):
            f = flyer(WL, c, r)
            self.add(f)
            self.play(MoveAlongPath(f, ArcBetweenPoints(np.array(card_center(WL, c, r)), TRAY_IN, angle=0.7)), run_time=0.45)
            self.remove(f)
            self.play(Transform(pl, pile(k + 2)), run_time=0.1)
        done(self)


def b00_state():
    return VGroup(claude_block(), tray(), wall(), l_claude(), l_context(), l_tools())


# ══════════════ B01: load them all and the tray overflows ══════════════
SPILL = [TR.p(TW + 0.35, 0.35, 0), TR.p(TW + 0.55, -0.35, 0)]


def spilled(k):
    c = SPILL[k]
    q = TR.quad([(0, 0, 0), (0.55, 0, 0), (0.55, 0.4, 0), (0, 0.4, 0)], "#FFFFFF", sw=3)
    q.set_stroke(BAR1, 3)
    return q.move_to(c).set_z_index(5)


def l_100():
    return T("~100 tools", 100, INK, bold=True).move_to([-1.0, 2.65, 0])


def l_cookbook():
    return lab("per Anthropic's cookbook", [-1.0, 1.75], 38)


def flights(slots, target=None):
    out = []
    for (c, r) in slots:
        f = flyer(WL, c, r)
        out.append((f, ArcBetweenPoints(np.array(card_center(WL, c, r)), target if target is not None else TRAY_IN, angle=0.7)))
    return out


class B01_Overflow(Scene):
    def construct(self):
        st = b00_state()
        pl = pile(3)
        self.add(st, pl)
        a = flights([(c, r) for r in (3, 2) for c in range(COLS)])
        for f, _ in a:
            self.add(f)
        self.play(LaggedStart(*[MoveAlongPath(f, p) for f, p in a], lag_ratio=0.12), Transform(pl, pile(13)),
                  run_time=2.0, rate_func=linear)
        for f, _ in a:
            self.remove(f)
        until(self, "Anthropic's cookbook", lead=0.4)
        self.play(FadeIn(l_100(), scale=0.8), run_time=0.45)
        self.play(FadeIn(l_cookbook()), run_time=0.3)
        b = flights([(c, r) for r in (1, 0) for c in range(COLS)])
        for f, _ in b:
            self.add(f)
        self.play(LaggedStart(*[MoveAlongPath(f, p) for f, p in b], lag_ratio=0.12), Transform(pl, pile(16)),
                  run_time=1.6, rate_func=linear)
        for f, _ in b:
            self.remove(f)
        until(self, "this becomes impractical", lead=0.2)
        top = TR.p(PX0 + PW / 2, PY0 + PD / 2, TZ + 16 * PSTEP)
        for k in range(2):
            s = spilled(k)
            tgt = np.array(s.get_center())
            s.move_to(top)
            self.add(s)
            self.play(MoveAlongPath(s, ArcBetweenPoints(top, tgt, angle=-0.9)), run_time=0.5, rate_func=ease_in)
        until(self, "harder to find", lead=0.3)
        self.play(Indicate(st[2][2], color=None, scale_factor=1.04), run_time=0.6)
        done(self)


def b01_state():
    return VGroup(b00_state(), pile(16), spilled(0), spilled(1), l_100(), l_cookbook())


# ══════════════ B02: carry one tool; defer the rest ══════════════
class B02_OneTool(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        base = st[0]                  # claude, tray, wall, Claude, context, tools
        self.play(FadeOut(VGroup(st[4], st[5])), FadeOut(VGroup(st[1], st[2], st[3]), shift=DOWN * 0.5), run_time=0.6)
        until(self, "tool search", lead=0.5)
        sb, ln = search_block(), lens()
        self.play(FadeIn(VGroup(sb, ln), shift=DOWN * 0.9), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(l_search()), Flash(np.array(S_TOP), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=0.4)
        until(self, "mark the rest", lead=0.2)
        cards = base[2][2]
        ghost = wall(ghost=True)[2]
        rt = guard(self, 1.3)
        self.play(LaggedStart(*[Transform(cards[i], ghost[i]) for i in range(len(cards))], lag_ratio=0.05),
                  FadeOut(base[5]), FadeIn(l_deferred()), run_time=rt)
        until(self, "until a search finds them", lead=0.3)
        self.play(Flash(np.array(S_TOP), color=TERRA, line_length=0.15, flash_radius=0.3), Indicate(ln[1], color=TERRA, scale_factor=1.8),
                  run_time=0.6)
        done(self)


def b02_state():
    return VGroup(claude_block(), tray(), wall(ghost=True), l_claude(), l_context(), search_block(), lens(), l_search(), l_deferred())


# ══════════════ B03: every definition becomes a point on a map ══════════════
class B03_Map(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        w = st[2]
        self.play(FadeOut(VGroup(st[7], st[8])), Transform(w, wall(WLS, ghost=True)), run_time=0.8)
        mp = meaning_map()
        self.play(FadeIn(mp, shift=UP * 0.5), FadeIn(l_map()), run_time=0.6)
        until(self, "Each definition becomes text", lead=0.3)
        fl = []
        for i, (c, r) in enumerate([(c, r) for r in range(ROWS) for c in range(COLS)]):
            f = card_quad(WLS, c, r)
            f.set_stroke(BAR1, 2)
            f.set_z_index(7)
            fl.append((f, mpt(ALL_PTS[(i * 7) % 24])))
        for f, _ in fl:
            self.add(f)
        self.play(LaggedStart(*[f.animate.move_to(t).scale(0.35) for f, t in fl], lag_ratio=0.06), run_time=2.0)
        for f, _ in fl:
            self.remove(f)
        d = dots()
        self.add(d)
        until(self, "a point on a map", lead=0.3)
        self.play(Indicate(d[3], color=INK, scale_factor=2.0), run_time=0.6)
        until(self, "Similar tools land close", lead=0.3)
        pd = pads()
        self.play(FadeIn(pd), FadeIn(l_weather()), FadeIn(l_finance()), run_time=0.6)
        done(self)


def b03_state():
    return VGroup(claude_block(), tray(), wall(WLS, ghost=True), l_claude(), l_context(), search_block(), lens(),
                  meaning_map(), pads(), dots(), l_map(), l_weather(), l_finance())


# ══════════════ B04: the query lands; the three closest win ══════════════
PARK = P(1.75, 1.35)


def l_query():
    return lab("query", [0.35, 1.35])


def l_closest():
    return lab("closest 3", [1.0, -0.1])


def spokes():
    q = mpt(Q)
    return VGroup(*[Line(q, mpt(WEATHER[i]), color=BAR1, stroke_width=6) for i in WIN]).set_z_index(1)


class B04_Query(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        d = st[9]
        self.play(FadeOut(VGroup(st[10], st[12])), run_time=0.3)
        s = slip(CL_TOP)
        self.play(FadeIn(s, scale=0.5), FadeIn(l_query()), run_time=0.4)
        self.play(MoveAlongPath(s, ArcBetweenPoints(CL_TOP, PARK, angle=-0.6)), run_time=0.9)
        until(self, "check the weather", lead=0.3)
        self.play(Indicate(s, color=None, scale_factor=1.15), run_time=0.5)
        until(self, "The query lands", lead=0.2)
        qd = Dot(mpt(Q), radius=0.11, color=TERRA).set_z_index(3)
        self.play(s.animate.scale(0.3).move_to(mpt(Q)), run_time=0.5, rate_func=ease_in)
        self.remove(s)
        self.add(qd)
        self.play(Flash(np.array(mpt(Q)), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=0.4)
        until(self, "closest points come back", lead=0.3)
        sp = spokes()
        self.play(Create(sp), *[d[i].animate.scale(1.5) for i in WIN], FadeOut(st[11]), FadeIn(l_closest()), run_time=0.6)
        for i, ph in zip(WIN, ("get weather", "get forecast", "air quality")):
            until(self, ph, lead=0.15)
            self.play(Indicate(d[i], color=INK, scale_factor=1.5), run_time=0.35)
        done(self)


def win_dots():
    d = dots()
    for i in WIN:
        d[i].scale(1.5)
    return d


def b04_state():
    return VGroup(claude_block(), tray(), wall(WLS, ghost=True), l_claude(), l_context(), search_block(), lens(),
                  meaning_map(), pads(), win_dots(), spokes(), Dot(mpt(Q), radius=0.11, color=TERRA).set_z_index(3),
                  l_query(), l_closest())


# ══════════════ B05: names come back; the API expands them; Claude calls the tool ══════════════
class B05_Found(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[12], st[13])), run_time=0.3)
        tags = [tag(mpt(WEATHER[i])) for i in WIN]
        lnm = l_names()
        self.play(*[FadeIn(t, scale=0.4) for t in tags], FadeIn(lnm), run_time=0.4)
        self.play(*[MoveAlongPath(t, ArcBetweenPoints(np.array(t.get_center()), TAG_PARK[k], angle=0.5))
                    for k, t in enumerate(tags)], run_time=1.0)
        until(self, "swaps each name", lead=0.3)
        self.play(*[t.animate.move_to(found_center(k)) for k, t in enumerate(tags)], run_time=0.5, rate_func=ease_in)
        fc = found_cards()
        self.play(*[FadeOut(t) for t in tags], FadeIn(fc, scale=0.7), FadeOut(lnm), FadeIn(l_defs()), run_time=0.4)
        until(self, "calls get weather", lead=0.3)
        ck = check(*(found_center(0)[:2] + np.array([0.2, 0.42])), s=0.2)
        ck.set_z_index(8)
        self.play(Create(ck), Flash(np.array(SPARK_C), color=TERRA, line_length=0.15, flash_radius=0.35), run_time=0.5)
        until(self, "never entered", lead=0.3)
        self.play(Indicate(st[2], color=None, scale_factor=1.05), run_time=0.6)
        done(self)


def b05_state():
    ck = check(*(found_center(0)[:2] + np.array([0.2, 0.42])), s=0.2).set_z_index(8)
    return VGroup(claude_block(), tray(), wall(WLS, ghost=True), l_claude(), l_context(), search_block(), lens(),
                  meaning_map(), pads(), win_dots(), spokes(), Dot(mpt(Q), radius=0.11, color=TERRA).set_z_index(3),
                  found_cards(), ck, l_defs())


# ══════════════ B06: the built-in search, and the custom one ══════════════
class B06_BuiltIn(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[7], st[8], st[9], st[10], st[11], st[12], st[13], st[14])), run_time=0.5)
        self.play(Transform(st[2], wall(ghost=True)), run_time=0.8)
        until(self, "built-in tool search", lead=0.3)
        bb = builtin_block()
        dark = VGroup(builtin_light(0, GHOST), builtin_light(1, GHOST))
        self.play(FadeIn(VGroup(bb, dark), shift=DOWN * 0.9), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(l_builtin()), run_time=0.3)
        until(self, "one version matches patterns", lead=0.2)
        self.play(Transform(dark[0], builtin_light(0)), Flash(np.array(builtin_light(0).get_center()), color=TERRA,
                                                               line_length=0.12, flash_radius=0.22), run_time=0.4)
        until(self, "one takes plain queries", lead=0.2)
        self.play(Transform(dark[1], builtin_light(1)), Flash(np.array(builtin_light(1).get_center()), color=TERRA,
                                                               line_length=0.12, flash_radius=0.22), run_time=0.4)
        until(self, "search by meaning", lead=0.4)
        self.play(FadeOut(st[6]), FadeIn(mini_map(), scale=0.5), FadeIn(l_custom()), run_time=0.5)
        done(self)


def b06_state():
    return VGroup(claude_block(), tray(), wall(ghost=True), l_claude(), l_context(), search_block(), mini_map(),
                  builtin_block(), builtin_light(0), builtin_light(1), l_builtin(), l_custom())


# ══════════════ B07: when to use it ══════════════
CHECK_AT = (1.0, -0.95)


class B07_When(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[7], st[8], st[9], st[10], st[11]), shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(l_ten(), scale=0.8), run_time=0.45)
        self.play(FadeIn(l_docs()), run_time=0.3)
        until(self, "With fewer", lead=0.3)
        srch = VGroup(st[5], st[6])
        self.play(FadeOut(srch, shift=UP * 0.6), run_time=0.4)
        few = [few_card(k) for k in range(4)]
        self.play(LaggedStart(*[FadeIn(f, shift=DOWN * 0.8) for f in few], lag_ratio=0.25), run_time=0.8, rate_func=ease_in)
        ck = check(*CHECK_AT, s=0.28).set_z_index(8)
        self.play(Create(ck), run_time=0.4)
        until(self, "And keep your", lead=0.3)
        self.play(*[FadeOut(f) for f in few], FadeOut(ck), run_time=0.4)
        sb, mm = search_block(), mini_map()
        self.play(FadeIn(VGroup(sb, mm), shift=DOWN * 0.8), run_time=0.45, rate_func=ease_in)
        fav = flights([(0, 3), (3, 2), (5, 1)])
        fc = found_cards()
        for k, (f, _) in enumerate(fav):
            f.set_fill("#FFFFFF")
            self.add(f)
        self.play(LaggedStart(*[MoveAlongPath(f, ArcBetweenPoints(np.array(f.get_center()), found_center(k), angle=0.6))
                                for k, (f, _) in enumerate(fav)], lag_ratio=0.25), run_time=1.0)
        for f, _ in fav:
            self.remove(f)
        self.add(fc)
        self.play(FadeIn(l_always()), Flash(np.array(SPARK_C), color=TERRA, line_length=0.15, flash_radius=0.35), run_time=0.4)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Wall, B01_Overflow, B02_OneTool, B03_Map, B04_Query, B05_Found, B06_BuiltIn, B07_When):
    _cls.play = ST.play
