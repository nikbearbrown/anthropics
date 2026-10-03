"""
Manim scenes for show-tell-one-lesson-three-tiers (show-tell skill, card #30, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The mechanism exactly as Anthropic's k12-lesson-differentiation skill states it (live upstream files, sources/): THE
LESSON (a white upright page) the teacher brings is split into THREE TRAYS (kraft open boxes: below, at, above grade
level) that share ONE CORE, drawn as THE ROD (a deep-kraft rail running out of the lesson through every tray and
every worksheet: same standard, same context, same core tasks). Out come four Word documents: THE PLAN (a larger page
with a grey band) and three WORKSHEETS (white pages standing in the trays), later tagged Group A / B / C. Grey
SCAFFOLD chips fade 2-1-0; the above tier's EXTENSION is a kraft block that rises; RULEBOOK binders on a dark shelf;
the Knowledge Graph connector is a dark MCP block; the SOURCE is a taped kraft box whose threads feed all four pages.
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




# ═════════════════════════════ the film: one lesson, three tiers ═════════════════════════════
SHADOW = "#9A8D76"                                           # darker than #28's: carries Gate V contrast on the kraft trays
# extra-dark faces for plinths and shelves (darker than DARK_* so GATE T's ink tolerance never reads a big dark block
# as one ink "text" blob; the #20 builder's fix)
FB_TOP, FB_L, FB_R = "#161411", "#121010", "#0E0C0A"
EDGE_D = "#050404"                                           # edge colour for extra-dark blocks (not ink: GATE T)
TILE_TOP, TILE_L, TILE_R = "#D2BD98", "#B39A72", "#9C8462"    # deep kraft: the rod, tags, the extension block
SMALL_EDGE = "#917A55"                                       # dark kraft outline for SMALL objects (GATE T §8.6b)
ROD_EDGE = TILE_R                                            # rod and threads edged in deep kraft, never ink


def dark(g):
    for f in g.family_members_with_points():
        f.set_stroke(EDGE_D, 3)
    return g


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float)).set_z_index(9)


def P(x, y):
    return np.array([x, y, 0.0])


# ─────────────── pages ───────────────
def page(cx, by, w, h, n=4, edge=INK, band=False, dot=True, z=1):
    """An upright white page, bottom edge centred at (cx, by): VGroup(shadow, body, lines, [band], [dot])."""
    sh = Rectangle(width=w, height=h, fill_color=TILE_L, fill_opacity=1, stroke_width=0).move_to([cx + 0.1, by + h / 2 - 0.1, 0])
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=edge, stroke_width=3).move_to([cx, by + h / 2, 0])
    g = VGroup(sh, body)
    top = by + h - (0.42 if band else 0.3)
    if band:
        g.add(Rectangle(width=w - 0.12, height=0.2, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([cx, by + h - 0.18, 0]))
    step = (h - 0.75) / max(n - 1, 1)
    lines = VGroup()
    for i in range(n):
        y = top - 0.12 - step * i
        lines.add(Line([cx - w * 0.32, y, 0], [cx + w * (0.32 - (0.18 if i % 2 else 0)), y, 0], color=BAR2, stroke_width=7))
    g.add(lines)
    if dot:
        g.add(Dot([cx - w * 0.34, by + h - 0.2 - (0.22 if band else 0), 0], radius=0.07, color=TERRA))
    return g.set_z_index(z)


# THE LESSON / THE PLAN sit at the left of the tray row; the rod runs out of them
LX, LBY = -5.0, -1.6


def lesson(cx=LX, by=LBY, w=1.4, h=2.0):
    return page(cx, by, w, h, n=4)


def plan(cx=LX, by=LBY):
    return page(cx, by, 1.5, 2.15, n=4, band=True)


# ─────────────── THE THREE TRAYS ───────────────
TW, TD, TDH = 1.9, 1.3, 0.75
TK, TBASE = 0.85, -2.0
TX = [-2.2, 1.1, 4.4]
ROD_Y = -0.3
LAB_Y = -2.62


def tray_iso(cx, base=TBASE, k=TK):
    return Iso(cx - (TW - TD) / 2 * C30 * k, base, k)


def tray(cx, base=TBASE, k=TK):
    """(back, front): shadow + floor + inner walls behind (z 0), front walls (z 2). Contents go between."""
    I = tray_iso(cx, base, k)
    sh = I.quad([(-0.12, -0.35, 0), (TW + 0.25, -0.35, 0), (TW + 0.25, TD, 0), (-0.12, TD, 0)], SHADOW, sw=0).set_z_index(-2)
    back, front = I.open_box(0, 0, 0, TW, TD, TDH)
    return VGroup(sh, back), front                 # keep the shadow at z -2 (a group set_z_index would lift it)


def floor_mid(cx, base=TBASE, k=TK):
    return tray_iso(cx, base, k).p(TW / 2, TD / 2, 0)


def sheet(cx, base=TBASE, k=TK, w=1.1, h=1.75):
    """A student worksheet standing in a tray (grey outline: it sits inside an ink-outlined container)."""
    f = floor_mid(cx, base, k)
    return page(float(f[0]), float(f[1]), w, h, n=4, edge=BAR1, dot=False, z=1)


def rod(x0=-5.85, x1=5.9, y=ROD_Y, h=0.26):
    return Rectangle(width=x1 - x0, height=h, fill_color=TILE_L, fill_opacity=1, stroke_color=ROD_EDGE,
                     stroke_width=4).move_to([(x0 + x1) / 2, y, 0]).set_z_index(1.5)


def rod_end(x1=5.9, y=ROD_Y):
    return Dot([x1 - 0.2, y, 0], radius=0.07, color=TERRA).set_z_index(1.6)


def all_trays():
    return [tray(x) for x in TX]


def tray_labels(names=("below", "at", "above")):
    return [lab(n, [x, LAB_Y]) for n, x in zip(names, TX)]


def support_pair(cx, base=TBASE, k=TK):
    """Two grey support blocks standing in a tray, left of the worksheet (a small step)."""
    I = tray_iso(cx, base, k)
    a = I.box(0.2, 0.75, 0, 0.38, 0.38, 1.25, BAR3, BAR2, BAR1, sw=3)
    b = I.box(0.2, 0.25, 0, 0.38, 0.38, 0.95, BAR3, BAR2, BAR1, sw=3)
    return VGroup(a, b).set_z_index(1.2)


def ext_block(cx, y=ROD_Y + 0.13, k=TK):
    """The above tier's extension: a deep-kraft block sitting on the rod, right of the worksheet."""
    I = Iso(cx + 0.95, y, 0.55 * k / 0.85)
    return VGroup(I.box(-0.4, -0.4, 0, 0.8, 0.8, 0.6, TILE_TOP, TILE_L, TILE_R, sw=3),
                  Dot(I.p(0.0, 0.0, 0.6), radius=0.06, color=TERRA)).set_z_index(1.7)


# ══════════════ B00: it starts from your lesson ══════════════
B0 = dict(cx=-2.1, by=-1.9, w=2.1, h=2.9)
GX = 2.3


def ghost_page(cx=GX, by=-1.9, w=2.1, h=2.9):
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, by, by + h
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    return VGroup(*[DashedLine([pts[i][0], pts[i][1], 0], [pts[(i + 1) % 4][0], pts[(i + 1) % 4][1], 0],
                               color=BAR1, stroke_width=5, dash_length=0.18) for i in range(4)])


def cross(cx, cy, s=0.75, w=12):
    return VGroup(Line([cx - s, cy - s, 0], [cx + s, cy + s, 0], color=INK, stroke_width=w),
                  Line([cx - s, cy + s, 0], [cx + s, cy - s, 0], color=INK, stroke_width=w)).set_z_index(3)


def floor_shadow(cx, y, w):
    return Ellipse(width=w, height=0.35, fill_color=SHADOW, fill_opacity=1, stroke_width=0).move_to([cx, y, 0]).set_z_index(-2)


class B00_Lesson(Scene):
    def construct(self):
        pg = page(**B0, n=5)
        sh = floor_shadow(B0["cx"], B0["by"] - 0.05, 2.6)
        self.play(FadeIn(pg, shift=DOWN * 0.8), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(sh, scale=0.5), run_time=0.3)
        until(self, "It starts from a lesson", lead=0.3)
        l1 = lab("your lesson", [B0["cx"], -2.55])
        self.play(FadeIn(l1), run_time=guard(self, 0.4))
        until(self, "You share it", lead=0.2)
        ck = check(B0["cx"] + 0.2, 1.6, s=0.28)
        self.play(Create(ck), run_time=guard(self, 0.4))
        until(self, "It doesn't write a new lesson", lead=0.3)
        gp = ghost_page()
        self.play(Create(gp), run_time=guard(self, 0.6))
        l2 = lab("new lesson", [GX, -2.55])
        self.play(FadeIn(l2), run_time=guard(self, 0.3))
        until(self, "A separate lesson creation", lead=0.4)
        self.play(Create(cross(GX, -0.45)), run_time=guard(self, 0.4))
        done(self)


def b00_state():
    return dict(pg=page(**B0, n=5), sh=floor_shadow(B0["cx"], B0["by"] - 0.05, 2.6), l1=lab("your lesson", [B0["cx"], -2.55]),
                ck=check(B0["cx"] + 0.2, 1.6, s=0.28), gp=ghost_page(), l2=lab("new lesson", [GX, -2.55]), x=cross(GX, -0.45))


# ══════════════ B01: one lesson, three tiers, one core ══════════════
class B01_Tiers(Scene):
    def construct(self):
        s = b00_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["gp"], s["l2"], s["x"], s["ck"], s["l1"], s["sh"])), run_time=0.4)
        self.play(ReplacementTransform(s["pg"], lesson()), run_time=0.6)
        trs = all_trays()
        labs = tray_labels()
        until(self, "into three tiers", lead=0.3)
        for (bk, fr), lb in zip(trs, labs):
            self.play(FadeIn(VGroup(bk, fr), shift=DOWN * 0.6), FadeIn(lb), run_time=guard(self, 0.4), rate_func=ease_in)
        until(self, "A core runs through", lead=0.3)
        r = rod()
        self.play(GrowFromEdge(r, LEFT), run_time=guard(self, 0.9))
        self.play(FadeIn(rod_end(), scale=0.3), run_time=guard(self, 0.2))
        until(self, "Only the supports change", lead=0.3)
        self.play(FadeIn(support_pair(TX[0]), shift=UP * 0.3), FadeIn(ext_block(TX[2]), shift=DOWN * 0.4),
                  run_time=guard(self, 0.5))
        done(self)


def row_state(sheets=False, supports=True, labels=("below", "at", "above"), left="lesson"):
    d = {}
    for i, (bk, fr) in enumerate(all_trays()):
        d[f"bk{i}"], d[f"fr{i}"] = bk, fr
    for i, lb in enumerate(tray_labels(labels)):
        d[f"lb{i}"] = lb
    d["rod"], d["end"] = rod(), rod_end()
    d["left"] = lesson() if left == "lesson" else plan()
    if supports:
        d["sup"], d["ext"] = support_pair(TX[0]), ext_block(TX[2])
    if sheets:
        for i, x in enumerate(TX):
            d[f"ws{i}"] = sheet(x)
    return d


# ══════════════ B02: four Word documents ══════════════
class B02_FourDocs(Scene):
    def construct(self):
        s = row_state()
        self.add(*s.values())
        ws = [sheet(x) for x in TX]
        self.play(*[GrowFromEdge(w, DOWN) for w in ws], run_time=0.6)
        until(self, "four editable Word documents", lead=0.3)
        lw = lab("worksheets", [TX[1], 1.02])
        self.play(FadeIn(lw), run_time=guard(self, 0.35))
        until(self, "one plan for you", lead=0.3)
        pl = plan()
        self.play(FadeOut(s["left"]), FadeIn(pl, shift=DOWN * 0.5), run_time=guard(self, 0.45), rate_func=ease_in)
        lp = lab("plan", [LX, 1.1])
        self.play(FadeIn(lp), run_time=guard(self, 0.3))
        done(self)


def b02_state():
    d = row_state(sheets=True, left="plan")
    d["lw"], d["lp"] = lab("worksheets", [TX[1], 1.02]), lab("plan", [LX, 1.1])
    return d


# ══════════════ B03: route: the subject's rulebook ══════════════
L3 = dict(cx=-4.4, by=-1.8, w=1.7, h=2.4)
SH_Y = -1.9                                  # shelf top line
BX = [0.2, 1.55, 2.9, 4.25]                  # binder centres


def shelf():
    slab = Rectangle(width=5.6, height=0.3, fill_color=FB_TOP, fill_opacity=1, stroke_color=EDGE_D, stroke_width=3
                     ).move_to([2.25, SH_Y - 0.1, 0])
    face = Rectangle(width=5.6, height=0.22, fill_color=FB_R, fill_opacity=1, stroke_color=EDGE_D, stroke_width=3
                     ).move_to([2.25, SH_Y - 0.36, 0])
    return VGroup(slab, face).set_z_index(0)


def binder(cx, y=SH_Y, k=0.8):
    """An upright kraft binder (iso box) with a grey spine ring; its base sits on the shelf."""
    I = Iso(cx, y + 0.22, k)
    body = I.box(-0.25, -0.55, 0, 0.5, 1.1, 1.9)
    ring = Circle(radius=0.1 * k, fill_color=GHOST, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(I.p(-0.25, 0.0, 1.35))
    return VGroup(body, ring).set_z_index(1)


def page_tab(cx, top, w=0.5):
    return Rectangle(width=w, height=0.32, fill_color=TILE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3
                     ).move_to([cx + 0.35, top + 0.1, 0]).set_z_index(0.5)


class B03_Subject(Scene):
    def construct(self):
        s = b02_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.45)
        lp = page(**L3, n=4)
        self.play(FadeIn(lp, shift=DOWN * 0.5), run_time=0.45, rate_func=ease_in)
        sf = shelf()
        bs = [binder(x) for x in BX]
        self.play(FadeIn(sf), *[FadeIn(b, shift=DOWN * 0.4) for b in bs], run_time=0.5, rate_func=ease_in)
        until(self, "It works out the subject", lead=0.3)
        l4 = lab("4 subjects", [2.25, 1.35])
        self.play(FadeIn(l4), run_time=guard(self, 0.35))
        until(self, "Then it reads", lead=0.3)
        guard(self, 1.2)
        tgt = P(-1.55, 0.0)
        self.play(bs[0].animate.shift(tgt - P(BX[0], 0) + DOWN * 0.35), run_time=guard(self, 0.6))
        self.play(FadeOut(l4), run_time=guard(self, 0.25))
        lm = lab("math rulebook", [-1.3, 1.95])
        top = L3["by"] + L3["h"]
        th = Line(P(-2.05, 0.25), P(L3["cx"] + L3["w"] / 2 + 0.05, 0.25), color=ROD_EDGE, stroke_width=7).set_z_index(0.5)
        self.play(FadeIn(lm), Create(th), run_time=guard(self, 0.45))
        until(self, "calls loading it mandatory", lead=0.3)
        self.play(FadeIn(page_tab(L3["cx"], top), shift=DOWN * 0.3), run_time=guard(self, 0.35))
        done(self)


def b03_state():
    top = L3["by"] + L3["h"]
    b0 = binder(BX[0]).shift(P(-1.55, 0.0) - P(BX[0], 0) + DOWN * 0.35)
    return dict(lp=page(**L3, n=4), sf=shelf(), b0=b0, b1=binder(BX[1]), b2=binder(BX[2]), b3=binder(BX[3]),
                lm=lab("math rulebook", [-1.3, 1.95]),
                th=Line(P(-2.05, 0.25), P(L3["cx"] + L3["w"] / 2 + 0.05, 0.25), color=ROD_EDGE, stroke_width=7).set_z_index(0.5),
                tab=page_tab(L3["cx"], top))


# ══════════════ B04: ground it in its standard ══════════════
KG = dict(ox=2.6, oy=-0.9, s=1.35)
PR = L3["cx"] + L3["w"] / 2                  # page right edge


def kg_block():
    I = Iso(**KG)
    return I.mcp(-0.65, -0.65, 0, 1.3, 1.3, 0.8).set_z_index(1)


def kg_cable():
    a = Iso(**KG).p(-0.65, 0.0, 0.4)
    return Line(P(PR + 0.05, float(a[1])), a, color=ROD_EDGE, stroke_width=9).set_z_index(0.5)


def std_tag(y=0.3):
    x0 = PR - 0.15
    return Polygon([x0, y + 0.3, 0], [x0 + 1.05, y + 0.3, 0], [x0 + 1.3, y, 0], [x0 + 1.05, y - 0.3, 0], [x0, y - 0.3, 0],
                   fill_color=TILE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).set_z_index(2)


def footer_line():
    y = L3["by"] + 0.22
    return Line([L3["cx"] - 0.6, y, 0], [L3["cx"] + 0.45, y, 0], color=BAR1, stroke_width=9).set_z_index(2)


class B04_Standards(Scene):
    def construct(self):
        s = b03_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["sf"], s["b0"], s["b1"], s["b2"], s["b3"], s["lm"], s["th"])), run_time=0.45)
        until(self, "grounds the lesson in its standard", lead=0.3)
        tg = std_tag()
        ls = lab("standard", [-2.3, 1.15])
        self.play(FadeIn(tg, shift=LEFT * 0.4), FadeIn(ls), run_time=0.45)
        until(self, "The Learning Commons", lead=0.3)
        kb = kg_block()
        self.play(FadeIn(kb, shift=DOWN * 0.6), run_time=guard(self, 0.5), rate_func=ease_in)
        lk = lab("Knowledge Graph", [2.6, 1.75])
        self.play(FadeIn(lk), run_time=guard(self, 0.35))
        until(self, "When it's connected", lead=0.3)
        self.play(Create(kg_cable()), run_time=guard(self, 0.6))
        until(self, "before drafting", lead=0.3)
        self.play(Create(check(PR + 1.75, 0.35, s=0.24)), run_time=guard(self, 0.35))
        until(self, "Without it", lead=0.3)
        self.play(Create(footer_line()), run_time=guard(self, 0.4))
        lf = lab("footer", [L3["cx"], -2.45])
        self.play(FadeIn(lf), run_time=guard(self, 0.3))
        done(self)


def b04_state():
    s = b03_state()
    return dict(lp=s["lp"], tab=s["tab"], tg=std_tag(), ls=lab("standard", [-2.3, 1.15]), kb=kg_block(),
                lk=lab("Knowledge Graph", [2.6, 1.75]), cb=kg_cable(), ck=check(PR + 1.75, 0.35, s=0.24),
                ft=footer_line(), lf=lab("footer", [L3["cx"], -2.45]))


# ══════════════ B05: where you teach ══════════════
def state_tag(x, y, fill):
    return Polygon([x, y + 0.34, 0], [x + 1.25, y + 0.34, 0], [x + 1.55, y, 0], [x + 1.25, y - 0.34, 0], [x, y - 0.34, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=3).set_z_index(2)


ST_X = 0.6


def pin(x, y):
    stem = Line([x, y, 0], [x, y + 0.5, 0], color=TILE_R, stroke_width=8).set_z_index(3)
    head = Dot([x, y + 0.55, 0], radius=0.15, color=TERRA).set_z_index(3)
    return VGroup(stem, head)


class B05_State(Scene):
    def construct(self):
        s = b04_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["kb"], s["lk"], s["cb"], s["ck"], s["lf"])), run_time=0.45)
        until(self, "Name your state", lead=0.3)
        t1 = state_tag(ST_X, 0.9, TILE_TOP)
        l1 = lab("your state", [ST_X + 3.2, 0.9])
        self.play(FadeIn(t1, shift=LEFT * 0.4), FadeIn(l1), run_time=guard(self, 0.45))
        self.play(FadeIn(pin(ST_X + 0.45, 0.72), shift=DOWN * 0.5), run_time=guard(self, 0.35), rate_func=ease_in)
        until(self, "Say nothing", lead=0.3)
        t2 = state_tag(ST_X, -0.9, BAR3)
        l2 = lab("national default", [ST_X + 3.6, -0.9])
        self.play(FadeIn(t2, shift=LEFT * 0.4), FadeIn(l2), run_time=guard(self, 0.45))
        c1 = Line(P(PR + 1.15, 0.3), P(ST_X, 0.9), color=ROD_EDGE, stroke_width=6).set_z_index(0.5)
        c2 = Line(P(PR + 1.15, 0.3), P(ST_X, -0.9), color=ROD_EDGE, stroke_width=6).set_z_index(0.5)
        self.play(Create(c1), Create(c2), run_time=guard(self, 0.4))
        until(self, "For social studies", lead=0.3)
        q = RoundedRectangle(width=1.0, height=0.7, corner_radius=0.15, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                             stroke_width=3).move_to(P(ST_X + 0.7, -2.3)).set_z_index(2)
        self.play(FadeIn(q, shift=UP * 0.4), run_time=guard(self, 0.35))
        self.play(FadeIn(lab("asks first", [ST_X + 3.0, -2.3])), run_time=guard(self, 0.3))
        done(self)


def b05_state():
    s = b04_state()
    return dict(lp=s["lp"], tab=s["tab"], tg=s["tg"], ls=s["ls"], ft=s["ft"],
                t1=state_tag(ST_X, 0.9, TILE_TOP), l1=lab("your state", [ST_X + 3.2, 0.9]), pn=pin(ST_X + 0.45, 0.72),
                t2=state_tag(ST_X, -0.9, BAR3), l2=lab("national default", [ST_X + 3.6, -0.9]),
                c1=Line(P(PR + 1.15, 0.3), P(ST_X, 0.9), color=ROD_EDGE, stroke_width=6).set_z_index(0.5),
                c2=Line(P(PR + 1.15, 0.3), P(ST_X, -0.9), color=ROD_EDGE, stroke_width=6).set_z_index(0.5),
                q=RoundedRectangle(width=1.0, height=0.7, corner_radius=0.15, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                                   stroke_width=3).move_to(P(ST_X + 0.7, -2.3)).set_z_index(2),
                lq=lab("asks first", [ST_X + 3.0, -2.3]))


# ══════════════ B06: what you said about your students ══════════════
NOTE = P(-3.4, 2.35)


def note_card(at=NOTE):
    body = Rectangle(width=1.5, height=0.95, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(at)
    lines = VGroup(*[Line(at + P(-0.5, 0.18 - 0.3 * i), at + P(0.5 - 0.25 * (i % 2), 0.18 - 0.3 * i), color=BAR2, stroke_width=7)
                     for i in range(2)])
    return VGroup(body, lines).set_z_index(3)


def vocab_chip(cx, base=TBASE, k=TK):
    """A small white support card standing in a tray, right of the worksheet spot (sentence supports + vocabulary)."""
    I = tray_iso(cx, base, k)
    return I.box(1.05, 0.8, 0, 0.7, 0.12, 1.6, PAGE_TOP, PAGE_L, PAGE_R, sw=3).set_z_index(1.1)


class B06_Needs(Scene):
    def construct(self):
        s = b05_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        r = row_state(supports=False)
        self.play(*[FadeIn(r[k], shift=DOWN * 0.4) for k in ("left", "bk0", "fr0", "bk1", "fr1", "bk2", "fr2")],
                  run_time=0.45, rate_func=ease_in)
        self.play(GrowFromEdge(r["rod"], LEFT), FadeIn(r["end"]), *[FadeIn(r[f"lb{i}"]) for i in range(3)], run_time=0.5)
        until(self, "what you've said about your students", lead=0.3)
        nc = note_card()
        ln = lab("learner needs", [-0.4, 2.35])
        self.play(FadeIn(nc, shift=RIGHT * 0.6), FadeIn(ln), run_time=guard(self, 0.45))
        until(self, "Those shape the tiers", lead=0.3)
        c0 = vocab_chip(TX[0])
        start = NOTE + P(0, -0.5)
        c0.move_to(start)
        self.play(FadeIn(c0, scale=0.5), run_time=guard(self, 0.2))
        dst = np.array(vocab_chip(TX[0]).get_center())
        self.play(MoveAlongPath(c0, ArcBetweenPoints(start, dst, angle=-0.8)), run_time=guard(self, 0.7))
        until(self, "every tier gets", lead=0.3)
        c1, c2 = vocab_chip(TX[1]), vocab_chip(TX[2])
        self.play(FadeIn(c1, shift=DOWN * 0.6), FadeIn(c2, shift=DOWN * 0.6), run_time=guard(self, 0.45), rate_func=ease_in)
        self.play(FadeIn(lab("all tiers", [TX[2], 1.25])), run_time=guard(self, 0.3))
        done(self)


def b06_state():
    d = row_state(supports=False)
    d.update(nc=note_card(), ln=lab("learner needs", [-0.4, 2.35]), c0=vocab_chip(TX[0]), c1=vocab_chip(TX[1]),
             c2=vocab_chip(TX[2]), la=lab("all tiers", [TX[2], 1.25]))
    return d


# ══════════════ B07: the draft offer ══════════════
PB, PQ = P(-2.6, 0.2), P(2.6, 0.2)


def button(at, w=3.0, h=1.0):
    return VGroup(RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=TILE_R, fill_opacity=1, stroke_width=0).move_to(at + P(0.12, -0.12)),
                  RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                                   stroke_width=4).move_to(at)).set_z_index(1)


def chat_card(at=P(2.6, -2.0)):
    body = RoundedRectangle(width=3.2, height=1.5, corner_radius=0.18, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                            stroke_width=4).move_to(at)
    lines = VGroup(*[Line(at + P(-1.05, 0.4 - 0.38 * i), at + P(1.05 - 0.45 * (i % 2), 0.4 - 0.38 * i), color=BAR2, stroke_width=8)
                     for i in range(3)])
    dots = VGroup(*[Dot(at + P(-1.3, 0.4 - 0.38 * i), radius=0.07, color=BAR1) for i in range(3)])
    return VGroup(body, lines, dots).set_z_index(2)


class B07_Draft(Scene):
    def construct(self):
        s = b06_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        until(self, "one question", lead=0.3)
        b1, b2 = button(PB), button(PQ)
        self.play(FadeIn(b1, shift=UP * 0.3), FadeIn(b2, shift=UP * 0.3), run_time=guard(self, 0.45))
        self.play(FadeIn(lab("build it", PB + P(0, 1.0))), FadeIn(lab("quick draft", PQ + P(0, 1.0))), run_time=guard(self, 0.35))
        until(self, "or see a quick draft", lead=0.3)
        cur = cursor(0.2, -1.6, s=0.55).set_z_index(5)
        self.play(FadeIn(cur), run_time=guard(self, 0.2))
        self.play(cur.animate.move_to(PQ + P(0.35, -0.3)), run_time=guard(self, 0.5))
        self.play(b2[1].animate.set_stroke(INK, 9), run_time=guard(self, 0.2))
        until(self, "right in chat", lead=0.4)
        cc = chat_card()
        self.play(FadeIn(cc, shift=UP * 0.5), run_time=guard(self, 0.4))
        until(self, "The full set is the default", lead=0.3)
        self.play(FadeIn(Dot(PB + P(-1.05, 0), radius=0.13, color=TERRA), scale=0.3), run_time=guard(self, 0.3))
        self.play(FadeIn(lab("default", PB + P(0, -1.0))), run_time=guard(self, 0.3))
        until(self, "A draft lets you change", lead=0.3)
        ed = Line(P(1.55, -2.02), P(3.25, -2.02), color=BAR1, stroke_width=11).set_z_index(3)
        self.play(Create(ed), run_time=guard(self, 0.45))
        done(self)


def b07_state():
    b2 = button(PQ)
    b2[1].set_stroke(INK, 9)
    return dict(b1=button(PB), b2=b2, l1=lab("build it", PB + P(0, 1.0)), l2=lab("quick draft", PQ + P(0, 1.0)),
                cur=cursor(0.2, -1.6, s=0.55).set_z_index(5).move_to(PQ + P(0.35, -0.3)), cc=chat_card(),
                dt=Dot(PB + P(-1.05, 0), radius=0.13, color=TERRA), ld=lab("default", PB + P(0, -1.0)),
                ed=Line(P(1.55, -2.02), P(3.25, -2.02), color=BAR1, stroke_width=11).set_z_index(3))


# ══════════════ B08: the below tier teaches up ══════════════
BK, BBASE, BCX = 1.55, -2.55, -2.6         # the big tray (B08 below, B10 above)
BROD = 0.55


def big_tray(cx=BCX):
    """The close-up tray on an extra-dark plinth (a lone kraft tray fails Gate V contrast)."""
    bk, fr = tray(cx, BBASE, BK)
    I = tray_iso(cx, BBASE, BK)
    pl = dark(I.box(-0.12, -0.12, -0.22, TW + 0.24, TD + 0.24, 0.22, FB_TOP, FB_L, FB_R)).set_z_index(-1)
    return VGroup(pl, bk), fr


def big_sheet(cx=BCX):
    f = floor_mid(cx, BBASE, BK)
    return page(float(f[0]), float(f[1]), 1.9, 2.9, n=5, edge=BAR1, dot=False, z=1)


def big_rod(x0, x1):
    return rod(x0, x1, BROD, 0.34)


def steps():
    g = VGroup()
    for i, h in enumerate((1.2, 2.2, 3.15)):
        I = Iso(0.55 + 0.72 * i, -2.45, 0.8)
        g.add(I.box(-0.35, -0.35, 0, 0.7, 0.7, h, BAR3, BAR2, BAR1, sw=3))
    return g.set_z_index(1)


PZ, PZR = P(4.35, -0.35), 1.15


def wedge(i, color, c=PZ, r=PZR):
    a0, a1 = PI / 2 - i * PI / 4, PI / 2 - (i + 1) * PI / 4
    pts = [c] + [c + r * np.array([np.cos(a), np.sin(a), 0]) for a in np.linspace(a0, a1, 8)]
    return Polygon(*pts, fill_color=color, fill_opacity=1, stroke_width=0).set_z_index(2)


def pizza(c=PZ, r=PZR):
    disc = Circle(radius=r, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c).set_z_index(1)
    cuts = VGroup(*[Line(c, c + r * np.array([np.cos(PI / 2 - i * PI / 4), np.sin(PI / 2 - i * PI / 4), 0]) * 0.97,
                         color=TILE_R, stroke_width=4) for i in range(8)]).set_z_index(3)
    sh = Ellipse(width=2 * r + 0.3, height=0.4, fill_color=SHADOW, fill_opacity=1, stroke_width=0).move_to(c + P(0.1, -r - 0.15)).set_z_index(-2)
    return VGroup(sh, disc, cuts)


class B08_TeachUp(Scene):
    def construct(self):
        s = b07_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        bk, fr = big_tray()
        ws = big_sheet()
        rd = big_rod(-5.9, 2.9)
        lb = lab("below", [-4.9, 1.35])
        self.play(FadeIn(VGroup(bk, fr, ws), shift=DOWN * 0.5), FadeIn(lb), run_time=0.5, rate_func=ease_in)
        self.play(GrowFromEdge(rd, LEFT), run_time=0.5)
        until(self, "Instead, supports route", lead=0.3)
        st = steps()
        for b in st:
            self.play(GrowFromEdge(b, DOWN), run_time=guard(self, 0.3))
        self.play(FadeIn(lab("teach up", [1.3, 1.6])), run_time=guard(self, 0.3))
        until(self, "three eighths of a pizza", lead=0.3)
        pz = pizza()
        self.play(FadeIn(pz, scale=0.7), run_time=guard(self, 0.45))
        until(self, "adds a pizza to shade", lead=0.3)
        self.play(*[FadeIn(wedge(i, BAR1)) for i in range(3)], run_time=guard(self, 0.35))
        self.play(*[FadeIn(wedge(i, BAR2)) for i in range(3, 5)], run_time=guard(self, 0.35))
        until(self, "asks the same question", lead=0.3)
        self.play(FadeIn(lab("same question", [4.5, -2.35])), run_time=guard(self, 0.35))
        done(self)


def b08_state():
    bk, fr = big_tray()
    return dict(bk=bk, fr=fr, ws=big_sheet(), rd=big_rod(-5.9, 2.9), lb=lab("below", [-4.9, 1.35]), st=steps(),
                lt=lab("teach up", [1.3, 1.6]), pz=pizza(), w=VGroup(*[wedge(i, BAR1 if i < 3 else BAR2) for i in range(5)]),
                lq=lab("same question", [4.5, -2.35]))


# ══════════════ B09: scaffolds help, never answer; they fade ══════════════
WS = dict(cx=-1.6, by=-2.95, w=4.6, h=5.8)
ROWS = [1.55, -0.15, -1.85]


def ws_big():
    body = Rectangle(width=WS["w"], height=WS["h"], fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=4
                     ).move_to([WS["cx"], WS["by"] + WS["h"] / 2, 0])
    sh = Rectangle(width=WS["w"], height=WS["h"], fill_color=TILE_L, fill_opacity=1, stroke_width=0
                   ).move_to([WS["cx"] + 0.12, WS["by"] + WS["h"] / 2 - 0.12, 0])
    return VGroup(sh, body).set_z_index(0)


def row(i):
    y = ROWS[i]
    x0 = WS["cx"] - WS["w"] / 2 + 0.55
    num = T(str(i + 1), 50).move_to([x0, y + 0.3, 0])
    ln = VGroup(Line([x0 + 0.5, y + 0.3, 0], [x0 + 3.2, y + 0.3, 0], color=BAR2, stroke_width=8),
                Line([x0 + 0.5, y - 0.1, 0], [x0 + 2.5, y - 0.1, 0], color=BAR2, stroke_width=8))
    box = Rectangle(width=1.3, height=0.5, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=4).move_to([x0 + 3.0, y - 0.62, 0])
    return VGroup(num, ln, box).set_z_index(1)


def chip(x, y):
    I = Iso(x, y - 0.3, 0.75)
    return I.box(-0.35, -0.35, 0, 0.7, 0.7, 0.45, BAR3, BAR2, BAR1, sw=3).set_z_index(2)


CHX = [1.55, 2.75]


class B09_Fade(Scene):
    def construct(self):
        s = b08_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        wb = ws_big()
        self.play(FadeIn(wb, shift=DOWN * 0.5), run_time=0.45, rate_func=ease_in)
        rs = [row(i) for i in range(3)]
        self.play(*[FadeIn(r) for r in rs], run_time=0.5)
        until(self, "no keyword tricks", lead=0.3)
        la = lab("no answers", [2.6, 2.6])
        self.play(FadeIn(la), run_time=guard(self, 0.35))
        until(self, "one or two per problem", lead=0.3)
        self.play(FadeIn(lab("max 2", [4.55, ROWS[0]])), run_time=guard(self, 0.3))
        until(self, "up to two on the first", lead=0.3)
        self.play(FadeIn(chip(CHX[0], ROWS[0]), shift=DOWN * 0.4), FadeIn(chip(CHX[1], ROWS[0]), shift=DOWN * 0.4),
                  run_time=guard(self, 0.35), rate_func=ease_in)
        until(self, "one on the second", lead=0.3)
        self.play(FadeIn(chip(CHX[0], ROWS[1]), shift=DOWN * 0.4), run_time=guard(self, 0.35), rate_func=ease_in)
        until(self, "none from the third", lead=0.3)
        self.play(Create(DashedLine([1.2, ROWS[2] - 0.05, 0], [3.1, ROWS[2] - 0.05, 0], color=BAR1, stroke_width=5, dash_length=0.15)),
                  FadeIn(lab("fade", [4.55, ROWS[1]])), run_time=guard(self, 0.35))
        done(self)


def b09_state():
    return dict(wb=ws_big(), r0=row(0), r1=row(1), r2=row(2), la=lab("no answers", [2.6, 2.6]),
                lm=lab("max 2", [4.55, ROWS[0]]), c1=chip(CHX[0], ROWS[0]), c2=chip(CHX[1], ROWS[0]), c3=chip(CHX[0], ROWS[1]),
                dl=DashedLine([1.2, ROWS[2] - 0.05, 0], [3.1, ROWS[2] - 0.05, 0], color=BAR1, stroke_width=5, dash_length=0.15),
                lf=lab("fade", [4.55, ROWS[1]]))


# ══════════════ B10: the above tier's extension ══════════════
ACX = 2.3


def same_stack():
    g = VGroup()
    for i in range(3):
        I = Iso(-4.3 + 1.0 * i, -1.75, 0.7)
        g.add(I.box(-0.35, -0.35, 0, 0.7, 0.7, 0.7, BAR3, BAR2, BAR1, sw=3))
    return g.set_z_index(1)


def big_ext(y):
    I = Iso(ACX + 1.75, y, 0.9)
    return VGroup(I.box(-0.4, -0.4, 0, 0.8, 0.8, 0.7, TILE_TOP, TILE_L, TILE_R, sw=4),
                  Dot(I.p(0.0, 0.0, 0.7), radius=0.08, color=TERRA)).set_z_index(1.8)


class B10_Extension(Scene):
    def construct(self):
        s = b09_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        bk, fr = big_tray(ACX)
        ws = big_sheet(ACX)
        rd = big_rod(-1.2, 5.9)
        lb = lab("above", [5.35, -2.3])
        self.play(FadeIn(VGroup(bk, fr, ws), shift=DOWN * 0.5), FadeIn(lb), run_time=0.5, rate_func=ease_in)
        self.play(GrowFromEdge(rd, LEFT), run_time=0.45)
        until(self, "not more of the same", lead=0.4)
        ss = same_stack()
        self.play(FadeIn(ss, shift=RIGHT * 0.6), run_time=guard(self, 0.4))
        self.play(Create(cross(-3.3, -1.3, s=0.55, w=10)), FadeIn(lab("more of the same", [-3.3, 0.1])), run_time=guard(self, 0.4))
        until(self, "In the example", lead=0.3)
        ex = big_ext(BROD + 0.17)
        self.play(FadeIn(ex, shift=DOWN * 0.6), run_time=guard(self, 0.4), rate_func=ease_in)
        self.play(ex.animate.shift(UP * 0.5), run_time=guard(self, 0.45))
        self.play(FadeIn(lab("new thinking", [ACX + 1.75, 2.9])), run_time=guard(self, 0.3))
        done(self)


def b10_state():
    bk, fr = big_tray(ACX)
    return dict(bk=bk, fr=fr, ws=big_sheet(ACX), rd=big_rod(-1.2, 5.9), lb=lab("above", [5.35, -2.3]), ss=same_stack(),
                x=cross(-3.3, -1.3, s=0.55, w=10), lm=lab("more of the same", [-3.3, 0.1]),
                ex=big_ext(BROD + 0.17).shift(UP * 0.5), ln=lab("new thinking", [ACX + 1.75, 2.9]))


# ══════════════ B11: Group A, B and C ══════════════
def blend_line(cx):
    """A support folded into the worksheet: one more grey line on the Group A sheet."""
    f = floor_mid(cx)
    return Line([float(f[0]) - 0.32, float(f[1]) + 0.55, 0], [float(f[0]) + 0.3, float(f[1]) + 0.55, 0], color=BAR1,
                stroke_width=9).set_z_index(1.3)


class B11_Groups(Scene):
    def construct(self):
        s = b10_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        r = b02_state()
        self.play(FadeIn(VGroup(*[v for k, v in r.items() if k not in ("lw", "lp")]), shift=DOWN * 0.4), run_time=0.5, rate_func=ease_in)
        until(self, "nobody reads below", lead=0.3)
        gl = tray_labels(("Group A", "Group B", "Group C"))
        self.play(*[FadeOut(r[f"lb{i}"]) for i in range(3)], run_time=guard(self, 0.3))
        until(self, "just Group A", lead=0.3)
        self.play(*[FadeIn(g, shift=UP * 0.2) for g in gl], run_time=guard(self, 0.4))
        until(self, "look like part of the task", lead=0.3)
        bl = blend_line(TX[0])
        self.play(r["sup"].animate.set_opacity(0.0), Create(bl), run_time=guard(self, 0.5))
        done(self)


def b11_state():
    d = row_state(sheets=True, supports=False, labels=("Group A", "Group B", "Group C"), left="plan")
    d["ext"] = ext_block(TX[2])
    d["bl"] = blend_line(TX[0])
    return d


# ══════════════ B12: written once, one source ══════════════
SRC = dict(ox=0.45, oy=1.55, s=0.62)
DOC_TOPS = [P(LX, LBY + 2.15), P(TX[0], -1.32 + 1.75), P(TX[1], -1.32 + 1.75), P(TX[2], -1.32 + 1.75)]


def source_box():
    I = Iso(**SRC)
    sh = I.quad([(-0.9, -0.85, 0), (1.05, -0.85, 0), (1.05, 0.7, 0), (-0.9, 0.7, 0)], SHADOW, sw=0).set_z_index(-2)
    body = I.box(-0.9, -0.7, 0, 1.8, 1.4, 1.0)
    tp = I.tape(-0.9, -0.7, 1.0, 1.8, 1.4)
    return VGroup(sh, body, tp).set_z_index(3)


SRC_OUT = P(0.45, 1.5)


def threads():
    return [Line(SRC_OUT, d + P(0, 0.08), color=ROD_EDGE, stroke_width=6).set_z_index(0.8) for d in DOC_TOPS]


class B12_Shared(Scene):
    def construct(self):
        s = b11_state()
        self.add(*s.values())
        until(self, "written once", lead=0.3)
        sb = source_box()
        self.play(FadeIn(sb, shift=DOWN * 0.6), run_time=guard(self, 0.45), rate_func=ease_in)
        self.play(FadeIn(lab("written once", [3.6, 2.35])), run_time=guard(self, 0.3))
        until(self, "All four documents pull", lead=0.3)
        th = threads()
        self.play(*[Create(t) for t in th], run_time=guard(self, 0.7))
        until(self, "can't drift apart", lead=0.3)
        self.play(FadeIn(lab("one source", [-2.6, 2.35])), run_time=guard(self, 0.3))
        done(self)


def b12_state():
    d = b11_state()
    d.update(sb=source_box(), lw=lab("written once", [3.6, 2.35]), lo=lab("one source", [-2.6, 2.35]))
    for i, t in enumerate(threads()):
        d[f"th{i}"] = t
    return d


# ══════════════ B13: one shared edit, four updates; a one-tier edit stays put ══════════════
def new_line(d, i):
    x, y = float(d[0]), float(d[1])
    w = 0.9 if i == 0 else 0.62
    return Line([x - w / 2, y - 0.3, 0], [x + w / 2, y - 0.3, 0], color=INK, stroke_width=7).set_z_index(1.4)


class B13_Edit(Scene):
    def construct(self):
        s = b12_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["lw"], s["lo"])), run_time=0.35)
        until(self, "an edit to a shared task", lead=0.3)
        la = lab("all four", [3.6, 2.35])
        e = Dot(SRC_OUT, radius=0.1, color=TERRA).set_z_index(4)
        self.play(FadeIn(e, scale=0.3), FadeIn(la), run_time=guard(self, 0.3))
        ds = [Dot(SRC_OUT, radius=0.1, color=TERRA).set_z_index(4) for _ in DOC_TOPS]
        self.add(*ds)
        self.play(*[MoveAlongPath(dd, Line(SRC_OUT, d + P(0, 0.08))) for dd, d in zip(ds, DOC_TOPS)], run_time=guard(self, 0.6))
        self.play(*[FadeOut(dd) for dd in ds], FadeOut(e), *[Create(new_line(d, i)) for i, d in enumerate(DOC_TOPS)],
                  run_time=guard(self, 0.4))
        until(self, "A change aimed at one tier", lead=0.3)
        guard(self, 1.0)
        f = floor_mid(TX[0])
        ch = Rectangle(width=0.55, height=0.3, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=3
                       ).move_to([float(f[0]) - 0.95, 0.9, 0]).set_z_index(4)
        self.play(FadeIn(ch, shift=DOWN * 0.5), FadeIn(lab("one tier", [-3.8, 2.35])), run_time=guard(self, 0.4))
        self.play(ch.animate.move_to([float(f[0]) - 0.2, -0.72, 0]), run_time=guard(self, 0.45))
        done(self)


def b13_state():
    d = b12_state()
    d.pop("lw"); d.pop("lo")
    f = floor_mid(TX[0])
    d.update(la=lab("all four", [3.6, 2.35]), lt=lab("one tier", [-3.8, 2.35]),
             ch=Rectangle(width=0.55, height=0.3, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=3
                          ).move_to([float(f[0]) - 0.2, -0.72, 0]).set_z_index(4))
    for i, dd in enumerate(DOC_TOPS):
        d[f"nl{i}"] = new_line(dd, i)
    return d


# ══════════════ B14: the groups can change ══════════════
def figure(x, y):
    """A small kraft student figure: body + head, dark-kraft outline (small object)."""
    body = RoundedRectangle(width=0.5, height=0.95, corner_radius=0.18, fill_color=BOX_L, fill_opacity=1, stroke_color=INK,
                            stroke_width=3).move_to([x, y + 0.48, 0])
    head = Circle(radius=0.22, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y + 1.2, 0])
    return VGroup(body, head).set_z_index(1.2)


def fig_spots(cx):
    f = floor_mid(cx)
    return [(float(f[0]) - 0.45, float(f[1]) + 0.05), (float(f[0]) + 0.45, float(f[1]) + 0.05)]


def start_spots():
    """Two figures in Group A and Group C, one in Group B (its left spot is free for the mover)."""
    return fig_spots(TX[0]) + fig_spots(TX[1])[1:] + fig_spots(TX[2])


def slip(at):
    return VGroup(Rectangle(width=1.2, height=0.62, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(at),
                  Line(at + P(-0.38, 0.08), at + P(0.38, 0.08), color=BAR2, stroke_width=7),
                  Line(at + P(-0.38, -0.12), at + P(0.15, -0.12), color=BAR2, stroke_width=7)).set_z_index(3)


SLIP = P(-5.0, 1.6)


class B14_Grouping(Scene):
    def construct(self):
        s = b13_state()
        self.add(*s.values())
        keep = {"bk0", "fr0", "bk1", "fr1", "bk2", "fr2", "lb0", "lb1", "lb2"}
        self.play(FadeOut(VGroup(*[v for k, v in s.items() if k not in keep])), run_time=0.45)
        figs = [figure(fx, fy) for (fx, fy) in start_spots()]
        self.play(*[FadeIn(f, shift=DOWN * 0.4) for f in figs], run_time=0.5, rate_func=ease_in)
        until(self, "what each group is based on", lead=0.3)
        sl = slip(SLIP)
        self.play(FadeIn(sl, shift=RIGHT * 0.5), FadeIn(lab("evidence", [-5.0, 2.45])), run_time=guard(self, 0.4))
        until(self, "the groups can change", lead=0.3)
        guard(self, 1.2)
        mover = figs[1]
        a = np.array([float(fig_spots(TX[0])[1][0]), float(fig_spots(TX[0])[1][1]) + 0.71, 0.0])
        b = np.array([float(fig_spots(TX[1])[0][0]) - 0.02, float(fig_spots(TX[1])[0][1]) + 0.71, 0.0])
        self.play(MoveAlongPath(mover, ArcBetweenPoints(a, b, angle=-1.4)), run_time=guard(self, 0.7))
        self.play(FadeIn(lab("can change", [TX[1] - 1.6, 1.55])), run_time=guard(self, 0.3))
        until(self, "not a standing track", lead=0.3)
        self.play(Create(check(TX[1] + 1.25, 1.55, s=0.22)), run_time=guard(self, 0.3))
        done(self)


# ══════════════ B15: finished when you say so ══════════════
ROWX = [-4.3, -1.4, 1.5, 4.4]


def row_docs():
    return [page(ROWX[0], -1.9, 1.7, 2.4, n=4, band=True)] + [page(x, -1.9, 1.35, 2.1, n=4, dot=False) for x in ROWX[1:]]


class B15_Close(Scene):
    def construct(self):
        s = b14_like_end()
        self.add(*s)
        self.play(FadeOut(VGroup(*s)), run_time=0.4)
        docs = row_docs()
        self.play(*[FadeIn(d, shift=DOWN * 0.5) for d in docs], run_time=0.5, rate_func=ease_in)
        until(self, "if you're happy", lead=0.3)
        self.play(FadeIn(lab("all four?", [-1.4, 1.5])), run_time=guard(self, 0.35))
        until(self, "what your exit tickets showed", lead=0.3)
        sl = slip(P(-4.9, 2.55))
        self.play(FadeIn(sl, shift=RIGHT * 0.5), run_time=guard(self, 0.4))
        until(self, "It's finished when you say so", lead=0.45)
        cur = cursor(3.4, -2.9, s=0.5).set_z_index(5)
        self.play(FadeIn(cur), run_time=guard(self, 0.2))
        self.play(*[Create(check(x - 0.1, -2.55, s=0.2)) for x in ROWX], FadeIn(lab("your OK", [2.95, 1.5])),
                  run_time=guard(self, 0.4))
        done(self)


def b14_like_end():
    """B14's last frame (continuity): trays, rod, group labels, figures (one moved), slip, labels, check."""
    d = row_state(sheets=False, supports=False, labels=("Group A", "Group B", "Group C"))
    for k in ("left", "rod", "end"):
        d.pop(k)
    out = list(d.values())
    for i, (fx, fy) in enumerate(start_spots()):
        if i == 1:
            fx, fy = float(fig_spots(TX[1])[0][0]) - 0.02, float(fig_spots(TX[1])[0][1])
        out.append(figure(fx, fy))
    out += [slip(SLIP), lab("evidence", [-5.0, 2.45]), lab("can change", [TX[1] - 1.6, 1.55]), check(TX[1] + 1.25, 1.55, s=0.22)]
    return out


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Lesson, B01_Tiers, B02_FourDocs, B03_Subject, B04_Standards, B05_State, B06_Needs, B07_Draft,
             B08_TeachUp, B09_Fade, B10_Extension, B11_Groups, B12_Shared, B13_Edit, B14_Grouping, B15_Close):
    _cls.play = ST.play
