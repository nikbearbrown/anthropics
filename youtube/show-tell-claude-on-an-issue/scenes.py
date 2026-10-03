"""
Manim scenes for show-tell-claude-on-an-issue (show-tell skill, card #29, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The Claude Code Action (anthropics/claude-code-action, read raw from GitHub main on 2026-09-27):
a one-time setup (the Claude GitHub app, the ANTHROPIC_API_KEY secret, .github/workflows/claude.yml),
then an @claude comment on an issue -> the workflow's phrase check and the write-access check ->
the job on a GitHub runner -> one tracking comment with checkboxes -> reads issue, comments, code ->
answer or change -> a new claude/ branch with commits -> a Create PR link you press -> what it cannot
do (formal reviews, approving, merging) -> its small reach (one repo, no Bash unless allowed, no
workflow-file writes).
Cast (not the security-review film's PR crate on a belt): the ISSUE BOARD (a pin board on a dark
stand with the issue card, the @claude comment card and Claude's tracking card), the bottom row (the
Claude app block, the REPO tray of pages with the claude.yml page, the SAFE and its KEY), the GATE,
the RUNNER (a dark server stack whose lights come on), the BRANCH (main line + claude/ line), the PR
card, three locked buttons, and a dashed fence.
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





# ═════════════════════════════ the film: @claude on an issue ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
CONN = "#9C8462"          # deep kraft for cables and arrows (outside GATE T's ink mask)
TILE = "#B39A72"          # deep kraft
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (outside GATE T's ink tolerance)
BOARD_FILL = "#E9E4D9"    # near-stage pin board (a big kraft field lowers Gate V contrast)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=40):
    return T(s, size).move_to(P3(c))


def rlbl(s, y, size=40, x0=-2.5):
    """A label to the right of the board, left-aligned at x0."""
    t = T(s, size)
    return t.move_to(P3((x0 + t.width / 2.0, y)))


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.08):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def gbar(x0, x1, y, color=BAR1, w=6):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def drop(self, *mobs):
    for m in mobs:
        self.remove(*m.get_family())


def padlock(c, s=1.0):
    c = P3(c)
    body = rrect(0.46 * s, 0.38 * s, c + np.array([0, -0.06 * s, 0]), BOX_L, INK, 4, r=0.06)
    shackle = Arc(radius=0.15 * s, start_angle=0, angle=PI, arc_center=c + np.array([0, 0.13 * s, 0]), color=INK, stroke_width=8)
    hole = Dot(c + np.array([0, -0.08 * s, 0]), radius=0.045 * s, color=INK)
    return VGroup(shackle, body, hole).set_z_index(9)


# ─── the bottom row: the Claude app, the REPO tray with its pages, the SAFE with the key ───
RPW, RPD, RPH = 2.6, 1.4, 0.35
RP = rig_at(-0.35, -2.3, 0.6, RPW, RPD)
PGW, PGD = 0.42, 0.95


def repo_tray():
    back, front = RP.open_box(0, 0, 0, RPW, RPD, RPH)
    return VGroup(back, front)


def rpage(i):
    return RP.page(0.2 + 0.55 * i, 0.22, 0.03, PGW, PGD).set_z_index(1)


def rpages():
    return VGroup(*[rpage(i) for i in range(3)])


def wf_page():
    """The workflow file: a page with a dark header strip (claude.yml)."""
    x0, y0 = 0.2 + 0.55 * 3, 0.22
    slab = RP.box(x0, y0, 0.03, PGW, PGD, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = 0.09
    head = RP.quad([(x0 + 0.06, y0 + PGD * 0.72, zt), (x0 + PGW - 0.06, y0 + PGD * 0.72, zt),
                    (x0 + PGW - 0.06, y0 + PGD * 0.9, zt), (x0 + 0.06, y0 + PGD * 0.9, zt)], BAR1, sw=0)
    lines = VGroup(*[Line(RP.p(x0 + 0.1, y0 + PGD * f, zt), RP.p(x0 + PGW - 0.1, y0 + PGD * f, zt), color=GHOST, stroke_width=4)
                     for f in (0.3, 0.5)])
    return VGroup(slab, head, lines).set_z_index(1)


WF_HOME = np.array(RP.p(0.2 + 0.55 * 3 + PGW / 2, 0.22 + PGD / 2, 0.06))
PG_HOME = np.array(RP.p(0.2 + 0.55 * 1 + PGW / 2, 0.22 + PGD / 2, 0.06))

AP = rig_at(-2.55, -2.25, 0.6, 1.0, 1.0)


def app_block():
    """The Claude GitHub app: a small dark block with a terracotta spark on its top face."""
    body = AP.box(0, 0, 0, 1.0, 1.0, 0.55, DK_TOP, DK_L, DK_R)
    spark = Dot(AP.p(0.5, 0.5, 0.55), radius=0.09, color=TERRA)
    plug = Line(AP.p(1.0, 0.5, 0.25) + np.array([0.12, 0, 0]), RP.p(0, RPD * 0.55, 0.2) + np.array([-0.08, 0, 0]),
                color=CONN, stroke_width=7)
    return VGroup(body, spark), plug


SF = rig_at(1.75, -2.3, 0.6, 1.0, 1.0)


def safe():
    """(safe, lamp): a dark safe; its lamp lights when the key is inside."""
    body = SF.box(0, 0, 0, 1.0, 1.0, 0.95, DK_TOP, DK_L, DK_R)
    door = SF.quad([(0.18, 0, 0.18), (0.82, 0, 0.18), (0.82, 0, 0.78), (0.18, 0, 0.78)], DARK_TOP, stroke=CONN, sw=3)
    lamp = Dot(SF.p(0.5, 0, 0.48), radius=0.08, color=GHOST)
    return VGroup(body, door, lamp).set_z_index(1), lamp


SAFE_TOP = np.array(SF.p(0.5, 0.5, 0.95))


def key(c, s=1.0):
    c = P3(c)
    ring = Circle(radius=0.15 * s, stroke_color=INK, stroke_width=8, fill_color=TILE, fill_opacity=1).move_to(c)
    shaft = Line(c + np.array([0.15 * s, 0, 0]), c + np.array([0.6 * s, 0, 0]), color=INK, stroke_width=9)
    t1 = Line(c + np.array([0.45 * s, 0, 0]), c + np.array([0.45 * s, -0.13 * s, 0]), color=INK, stroke_width=9)
    t2 = Line(c + np.array([0.57 * s, 0, 0]), c + np.array([0.57 * s, -0.13 * s, 0]), color=INK, stroke_width=9)
    return VGroup(ring, shaft, t1, t2).set_z_index(11)


def bottom_row(lit=True):
    ap, plug = app_block()
    tray = repo_tray()
    pgs = rpages()
    wf = wf_page()
    sf, lamp = safe()
    if lit:
        lamp.set_color(TERRA)
    return {"app": ap, "plug": plug, "tray": tray, "pages": pgs, "wf": wf, "safe": sf, "lamp": lamp}


def row_group(d):
    return VGroup(d["plug"], d["app"], d["tray"][0], d["pages"], d["wf"], d["tray"][1], d["safe"])


# ─── the ISSUE BOARD and its cards ───
BX, BY, BW, BH = -4.4, 0.95, 3.2, 4.0
CW = 2.7


def board():
    panel = Rectangle(width=BW, height=BH, fill_color=BOARD_FILL, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((BX, BY)))
    legs = VGroup(*[Rectangle(width=0.2, height=0.42, fill_color=DK_L, fill_opacity=1, stroke_width=0)
                    .move_to(P3((BX + dx, BY - BH / 2 - 0.21))) for dx in (-1.05, 1.05)])
    return VGroup(legs, panel).set_z_index(0)


ISSUE_Y, COMMENT_Y = 2.4, 1.45


def card_base(y, h=0.8):
    return rrect(CW, h, (BX, y), PAGE_TOP, BAR1, 3, r=0.06).set_z_index(2)


def issue_card():
    b = card_base(ISSUE_Y)
    title = gbar(BX - 1.1, BX + 0.35, ISSUE_Y + 0.14, BAR1, 10)
    line = gbar(BX - 1.1, BX + 0.9, ISSUE_Y - 0.16, BAR2, 7)
    status = Dot(P3((BX + 0.95, ISSUE_Y + 0.14)), radius=0.08, color=BAR2)
    return VGroup(b, title, line, status).set_z_index(2)


def comment_card(y=COMMENT_Y):
    b = card_base(y)
    av = Circle(radius=0.16, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to(P3((BX - 1.05, y + 0.08)))
    l1 = gbar(BX - 0.7, BX + 0.85, y + 0.12, BAR1, 8)
    l2 = gbar(BX - 0.7, BX + 0.3, y - 0.16, BAR2, 7)
    return VGroup(b, av, l1, l2).set_z_index(2)


TRACK_Y0, TRACK_H0 = 0.45, 0.8          # the tracking card as first posted
TRACK_Y1, TRACK_H1 = 0.02, 1.66         # grown to hold the to-do list
ROWS = [0.2, -0.15, -0.5]


def track_head(y_top):
    spark = Dot(P3((BX - 1.05, y_top - 0.25)), radius=0.1, color=TERRA)
    l1 = gbar(BX - 0.75, BX + 0.8, y_top - 0.25, BAR1, 8)
    return VGroup(spark, l1).set_z_index(3)


def tbox(k):
    return Square(side_length=0.2, fill_color=GHOST, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(
        P3((BX - 1.0, TRACK_Y1 + ROWS[k] - 0.02))).set_z_index(3)


def tline(k):
    return gbar(BX - 0.7, BX - 0.7 + (1.3, 1.0, 1.15)[k], TRACK_Y1 + ROWS[k] - 0.02, BAR2, 7).set_z_index(3)


def ttick(k):
    return check(BX - 1.0, TRACK_Y1 + ROWS[k] - 0.02, 0.1, INK, 5).set_z_index(4)


def track_full(ticks=3):
    b = card_base(TRACK_Y1, TRACK_H1)
    head = track_head(TRACK_Y1 + TRACK_H1 / 2)
    rows = VGroup(*[VGroup(tbox(k), tline(k)) for k in range(3)])
    tk = VGroup(*[ttick(k) for k in range(ticks)])
    return VGroup(b, head, rows, tk)


PILL_C = (BX + 0.55, TRACK_Y1 - 0.5)


def pr_pill():
    p = RoundedRectangle(width=1.0, height=0.3, corner_radius=0.15, fill_color=BAR3, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(P3(PILL_C))
    return p.set_z_index(4)


def board_group(d):
    g = VGroup(d["board"], d["issue"], d["comment"])
    for k in ("track", "pill"):
        if k in d:
            g.add(d[k])
    return g


# ─── the GATE (the workflow's check) ───
GX0, GX1, GY = -1.25, 0.45, 1.3


def gate():
    posts = VGroup(*[Rectangle(width=0.24, height=1.3, fill_color=DK_L, fill_opacity=1, stroke_width=0).move_to(P3((x, GY))) for x in (GX0, GX1)])
    bar = Rectangle(width=GX1 - GX0 + 0.24, height=0.2, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(((GX0 + GX1) / 2, GY + 0.3)))
    return posts.set_z_index(3), bar.set_z_index(4)


def slip(c, s=0.42):
    """A small copy of the @claude comment card, travelling."""
    c = P3(c)
    b = rrect(CW * s, 0.8 * s, c, PAGE_TOP, INK, 4, r=0.05)
    av = Circle(radius=0.16 * s, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to(c + np.array([-1.05 * s, 0.08 * s, 0]))
    l1 = gbar(c[0] - 0.7 * s, c[0] + 0.85 * s, c[1] + 0.12 * s, BAR1, 6)
    return VGroup(b, av, l1).set_z_index(10)


# ─── the RUNNER ───
RW, RD = 1.4, 1.4
RN = rig_at(2.0, -0.3, 0.75, RW, RD)
SLAB = 0.42


def runner():
    stack, lights = RN.server(0, 0, 0, RW, RD, SLAB, 4)
    for s in stack:
        s[0].set_fill(DK_L); s[1].set_fill(DK_R); s[2].set_fill(DK_TOP)
    return stack.set_z_index(1), lights.set_z_index(2)


R_TOP = np.array(RN.p(RW / 2, RD / 2, 4 * (SLAB + 0.04)))
R_FRONT = np.array(RN.p(RW * 0.6, 0, 2 * (SLAB + 0.04)))
R_LEFT = np.array(RN.p(0, RD * 0.5, 1.2))
R_RIGHT = np.array(RN.p(RW, 0.1, 1.2))


def api_block():
    A = rig_at(2.0, 2.55, 0.5, 1.2, 1.2)
    body = A.box(0, 0, 0, 1.2, 1.2, 0.5, DK_TOP, DK_L, DK_R)
    cable = Line(R_TOP + np.array([0, 0.12, 0]), np.array(A.p(0.6, 0.6, 0)) + np.array([0, -0.55, 0]), color=CONN, stroke_width=7)
    return body.set_z_index(1), cable.set_z_index(0)


def run_group(d):
    return VGroup(d["runner"], d["lights"])


# ─── the BRANCH ───
MY, BRY = -2.2, -0.95
MAIN_DOTS = [3.45, 4.1, 5.0, 5.8]
FORK_X = 3.45
BR_DOTS = [4.85, 5.35, 5.85]


def main_line():
    ln = Line([3.2, MY, 0], [6.05, MY, 0], color=BAR1, stroke_width=9).set_z_index(1)
    dots = VGroup(*[Dot(P3((x, MY)), radius=0.13, color=BAR1) for x in MAIN_DOTS]).set_z_index(2)
    return ln, dots


def branch_line():
    pts = [P3((FORK_X, MY)), P3((FORK_X + 0.4, BRY)), P3((6.05, BRY))]
    v = VMobject(stroke_color=BAR1, stroke_width=9).set_points_as_corners(pts)
    return v.set_z_index(1)


def commit(i):
    return Dot(P3((BR_DOTS[i], BRY)), radius=0.13, color=BAR1).set_z_index(3)


PR_C = (5.05, 0.35)


def pr_card():
    b = rrect(1.7, 0.95, PR_C, BOX_TOP, INK, 4, r=0.08)
    l1 = gbar(PR_C[0] - 0.55, PR_C[0] + 0.5, PR_C[1] + 0.15, BAR1, 8)
    l2 = gbar(PR_C[0] - 0.55, PR_C[0] + 0.2, PR_C[1] - 0.15, BAR2, 7)
    return VGroup(b, l1, l2).set_z_index(3)


BTN_XC, BTN_YS = 5.55, [2.8, 2.05, 1.3]


def button(k):
    return rrect(0.9, 0.46, (BTN_XC, BTN_YS[k]), DK_L, DK_L, 0, r=0.1).set_z_index(3)


def btn_label(s, k, size=40):
    t = T(s, size)
    return t.move_to(P3((BTN_XC - 0.75 - t.width / 2.0, BTN_YS[k])))


def btn_labels():
    return VGroup(btn_label("review", 0), btn_label("approve", 1), btn_label("merge", 2))


def lens(c):
    c = P3(c)
    ring = Circle(radius=0.36, stroke_color=INK, stroke_width=7, fill_color=PAGE_TOP, fill_opacity=1).move_to(c)
    glint = Arc(radius=0.22, start_angle=PI * 0.6, angle=PI * 0.5, arc_center=c, color=BAR2, stroke_width=6)
    d = np.array([0.707, -0.707, 0])
    handle = Line(c + d * 0.36, c + d * 0.72, color=INK, stroke_width=12)
    return VGroup(ring, glint, handle).set_z_index(12)


# ─── state at the start of each beat (continuity) ───
def state(k):
    """Everything on stage at the START of beat Bk (k = 0..9), without labels."""
    d = {}
    if k >= 1:
        d.update(bottom_row())
    if k >= 2:
        d["board"], d["issue"], d["comment"] = board(), issue_card(), comment_card()
    if k >= 4:
        d["runner"], d["lights"] = runner()
        d["lights"].set_color(TERRA)
    if k >= 5:
        d["track"] = track_full(3)
    if k >= 7:
        d["main"], d["mdots"] = main_line()
        d["branch"] = branch_line()
        d["commits"] = VGroup(*[commit(i) for i in range(3)])
        d["tip"] = Dot(P3((6.05, BRY)), radius=0.13, color=TERRA).set_z_index(4)
    if k >= 8:
        d["pill"] = pr_pill()
        d["pr"] = pr_card()
    if k >= 9:
        d["buttons"] = VGroup(*[button(i) for i in range(3)])
        d["locks"] = VGroup(*[padlock((BTN_XC, BTN_YS[i] + 0.02), 0.9) for i in range(3)])
    return d


def add_state(self, d):
    order = ["plug", "app", "tray", "pages", "wf", "safe", "board", "issue", "comment", "track", "pill",
             "runner", "lights", "main", "mdots", "branch", "commits", "tip", "pr", "buttons", "locks"]
    for kk in order:
        if kk in d:
            if kk == "tray":
                self.add(d["tray"][0])
            else:
                self.add(d[kk])
    if "tray" in d:
        self.add(d["tray"][1])


# ══════════════ B00: set up once ══════════════
def b00_labels():
    return VGroup(lbl("repo", (0.45, -3.02), 38), lbl("secret", (1.75, -3.05), 38), lbl("claude.yml", (0.55, -1.05), 38))


class B00_Setup(Scene):
    def construct(self):
        d = bottom_row(lit=False)
        back, front = d["tray"]
        rt = guard(self, 0.8)
        self.play(FadeIn(VGroup(back, d["pages"], front), shift=DOWN * 0.4), run_time=rt)
        ls = b00_labels()
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        until(self, "Install the Claude GitHub app", lead=0.2)
        ap = d["app"]
        rt = guard(self, 0.6)
        self.play(FadeIn(ap, shift=RIGHT * 0.5), run_time=rt)
        rt = guard(self, 0.5)
        self.play(Create(d["plug"]), Indicate(ap[1], color=None, scale_factor=1.6), run_time=rt)
        until(self, "Store your Anthropic", lead=0.3)
        sf = d["safe"]
        rt = guard(self, 0.6)
        self.play(FadeIn(sf, shift=UP * 0.3), FadeIn(ls[1]), run_time=rt)
        k = key((SAFE_TOP[0] - 0.45, SAFE_TOP[1] + 1.1), 1.4)
        rt = guard(self, 0.4)
        self.play(FadeIn(k, shift=DOWN * 0.2), run_time=rt)
        until(self, "named Anthropic API key", lead=0.2)
        rt = guard(self, 0.7)
        self.play(k.animate.scale(0.6).move_to(SAFE_TOP + np.array([0, 0.05, 0])), run_time=rt, rate_func=ease_in)
        drop(self, k)
        rt = guard(self, 0.4)
        self.play(d["lamp"].animate.set_color(TERRA).scale(1.3), run_time=rt)
        until(self, "And copy the example workflow", lead=0.3)
        wf = d["wf"]
        start = wf.copy().shift(UP * 1.6 + RIGHT * 0.6)
        rt = guard(self, 0.4)
        self.play(FadeIn(start), run_time=rt)
        rt = guard(self, 0.7)
        self.play(Transform(start, wf), FadeIn(ls[2]), run_time=rt, rate_func=ease_in)
        drop(self, start)
        self.add(wf)
        until(self, "In Claude Code, the install", lead=0.3)
        cur = cursor(-1.6, -0.9).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.7)
        self.play(cur.animate.move_to(np.array(ap.get_center()) + np.array([0.2, -0.15, 0])), run_time=rt)
        until(self, "and the secret", lead=0.3)
        rt = guard(self, 0.6)
        self.play(cur.animate.move_to(SAFE_TOP + np.array([0.25, -0.2, 0])), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Indicate(d["lamp"], color=None, scale_factor=1.6), run_time=rt)
        done(self)


# ══════════════ B01: the mention ══════════════
def b01_labels():
    return VGroup(rlbl("issue", ISSUE_Y), rlbl("@claude", COMMENT_Y))


class B01_Mention(Scene):
    def construct(self):
        d = state(1)
        d["lamp"].set_color(TERRA)
        add_state(self, d)
        old = b00_labels()
        self.add(old)
        bd = board()
        rt = guard(self, 0.8)
        self.play(FadeOut(old), FadeIn(bd, shift=UP * 0.5), run_time=rt)
        ic = issue_card()
        ls = b01_labels()
        rt = guard(self, 0.6)
        self.play(FadeIn(ic, shift=DOWN * 0.25), FadeIn(ls[0]), run_time=rt)
        until(self, "the comment contains", lead=0.4)
        cc = comment_card()
        rt = guard(self, 0.6)
        self.play(FadeIn(cc, shift=UP * 0.3), run_time=rt)
        until(self, "the trigger phrase", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[1], shift=LEFT * 0.2), run_time=rt)
        until(self, "It has to be a whole word", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ls[1], color=None, scale_factor=1.15), run_time=rt)
        until(self, "won't start it", lead=0.3)
        rt = guard(self, 0.3)
        self.play(Indicate(cc[1], color=None, scale_factor=1.3), run_time=rt)
        until(self, "assigning the issue", lead=0.3)
        av = VGroup(Circle(radius=0.2, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((-2.25, 0.55))),
                    Arc(radius=0.12, start_angle=PI * 0.15, angle=PI * 0.7, arc_center=P3((-2.25, 0.62)), color=INK, stroke_width=4)).set_z_index(5)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(av), run_time=rt)
        until(self, "or on a label", lead=0.3)
        tag = Polygon(P3((-1.75, 0.72)), P3((-1.05, 0.72)), P3((-1.05, 0.38)), P3((-1.75, 0.38)), P3((-1.92, 0.55)),
                      fill_color=TILE, fill_opacity=1, stroke_color=INK, stroke_width=4).set_z_index(5)
        hole = Dot(P3((-1.72, 0.55)), radius=0.05, color=INK).set_z_index(6)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(VGroup(tag, hole)), run_time=rt)
        done(self)


# ══════════════ B02: the workflow checks ══════════════
def b02_labels():
    return VGroup(lbl("workflow", ((GX0 + GX1) / 2, 2.62), 40), lbl("write access", ((GX0 + GX1) / 2, 0.15), 38))


def trig_icons():
    av = VGroup(Circle(radius=0.2, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3((-2.25, 0.55))),
                Arc(radius=0.12, start_angle=PI * 0.15, angle=PI * 0.7, arc_center=P3((-2.25, 0.62)), color=INK, stroke_width=4)).set_z_index(5)
    tag = Polygon(P3((-1.75, 0.72)), P3((-1.05, 0.72)), P3((-1.05, 0.38)), P3((-1.75, 0.38)), P3((-1.92, 0.55)),
                  fill_color=TILE, fill_opacity=1, stroke_color=INK, stroke_width=4).set_z_index(5)
    hole = Dot(P3((-1.72, 0.55)), radius=0.05, color=INK).set_z_index(6)
    return VGroup(av, tag, hole)


SLIP_AT_GATE = (-2.02, GY - 0.25)


class B02_Gate(Scene):
    def construct(self):
        d = state(2)
        add_state(self, d)
        old = VGroup(b01_labels(), trig_icons())
        self.add(old)
        posts, bar = gate()
        ls = b02_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(old), FadeIn(VGroup(posts, bar), shift=UP * 0.3), FadeIn(ls[0]), run_time=rt)
        sl = slip((BX, COMMENT_Y))
        rt = guard(self, 0.3)
        self.play(FadeIn(sl), run_time=rt)
        rt = guard(self, 0.9)
        self.play(sl.animate.move_to(P3(SLIP_AT_GATE)), run_time=rt)
        until(self, "checks that the comment contains", lead=0.2)
        ck1 = check((GX0 + GX1) / 2 - 0.35, GY - 0.25, 0.18).set_z_index(6)
        rt = guard(self, 0.5)
        self.play(Indicate(sl, color=None, scale_factor=1.15), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Create(ck1), run_time=rt)
        until(self, "has write access", lead=0.4)
        badge = VGroup(Circle(radius=0.2, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(((GX0 + GX1) / 2 + 0.25, GY - 0.25))),
                       Arc(radius=0.12, start_angle=PI * 0.15, angle=PI * 0.7, arc_center=P3(((GX0 + GX1) / 2 + 0.25, GY - 0.18)), color=INK, stroke_width=4)).set_z_index(6)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(badge), FadeIn(ls[1]), run_time=rt)
        until(self, "Only users with write access", lead=0.2)
        ck2 = check((GX0 + GX1) / 2 + 0.6, GY - 0.25, 0.18).set_z_index(6)
        rt = guard(self, 0.4)
        self.play(Create(ck2), run_time=rt)
        until(self, "Then the gate opens", lead=0.3)
        rt = guard(self, 0.7)
        self.play(bar.animate.shift(UP * 0.5), FadeOut(VGroup(ck1, ck2, badge)), run_time=rt)
        done(self)


# ══════════════ B03: the runner ══════════════
def b03_labels():
    return VGroup(lbl("runner", (3.65, -0.75), 40), lbl("API", (3.2, 2.6), 40))


def gate_open():
    posts, bar = gate()
    bar.shift(UP * 0.5)
    return VGroup(posts, bar)


class B03_Runner(Scene):
    def construct(self):
        d = state(3)
        add_state(self, d)
        gt = gate_open()
        sl = slip(SLIP_AT_GATE)
        old = b02_labels()
        self.add(gt, sl, old)
        stack, lights = runner()
        ls = b03_labels()
        rt = guard(self, 0.8)
        self.play(FadeOut(old[1]), FadeIn(stack, shift=UP * 0.6), FadeIn(lights, shift=UP * 0.6), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(ls[0]), run_time=rt)
        rt = guard(self, 0.8)
        self.play(sl.animate.scale(0.7).move_to(R_LEFT), run_time=rt, rate_func=ease_in)
        drop(self, sl)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[l.animate.set_color(TERRA) for l in lights], lag_ratio=0.3), run_time=rt)
        until(self, "executes entirely", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(stack, color=None, scale_factor=1.05), run_time=rt)
        until(self, "its calls to Claude", lead=0.3)
        api, cable = api_block()
        rt = guard(self, 0.6)
        self.play(Create(cable), FadeIn(api, shift=DOWN * 0.2), FadeIn(ls[1]), run_time=rt)
        dot = Dot(R_TOP + np.array([0, 0.2, 0]), radius=0.09, color=TERRA).set_z_index(5)
        rt = guard(self, 0.6)
        self.play(FadeIn(dot), run_time=rt * 0.2)
        self.play(dot.animate.move_to(np.array(cable.get_end())), run_time=rt * 0.6)
        self.play(FadeOut(dot), run_time=rt * 0.2)
        until(self, "checks out your repository", lead=0.3)
        pg = rpage(1).copy().set_z_index(11)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(pg, ArcBetweenPoints(PG_HOME, R_FRONT + np.array([-0.2, 0, 0]), angle=-PI / 3)), run_time=rt * 0.8)
        self.play(FadeOut(pg, scale=0.5), run_time=rt * 0.2)
        until(self, "hands Claude the key", lead=0.3)
        k = key(SAFE_TOP + np.array([-0.3, 0.25, 0]), 0.8)
        rt = guard(self, 0.3)
        self.play(FadeIn(k), run_time=rt)
        rt = guard(self, 0.8)
        self.play(MoveAlongPath(k, ArcBetweenPoints(np.array(k.get_center()), R_FRONT + np.array([0.3, 0.3, 0]), angle=PI / 4)), run_time=rt * 0.8)
        self.play(FadeOut(k, scale=0.5), run_time=rt * 0.2)
        done(self)


# ══════════════ B04: the tracking comment ══════════════
class B04_Tracking(Scene):
    def construct(self):
        d = state(4)
        add_state(self, d)
        gt = gate_open()
        api, cable = api_block()
        old = VGroup(lbl("workflow", ((GX0 + GX1) / 2, 2.62), 40), b03_labels())
        self.add(gt, api, cable, old)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(gt, api, cable, old)), run_time=rt)
        card = card_base(TRACK_Y0, TRACK_H0)
        head = track_head(TRACK_Y0 + TRACK_H0 / 2)
        lt = rlbl("tracking", TRACK_Y0)
        rt = guard(self, 0.6)
        self.play(FadeIn(card, shift=DOWN * 0.2), FadeIn(head, shift=DOWN * 0.2), run_time=rt)
        spin = Arc(radius=0.2, start_angle=0, angle=PI * 1.2, arc_center=head[0].get_center(), color=BAR1, stroke_width=6).set_z_index(4)
        rt = guard(self, 0.9)
        self.play(Create(spin), FadeIn(lt), run_time=rt)
        until(self, "That's the tracking comment", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Rotate(spin, angle=-PI), run_time=rt)
        until(self, "it updates that same comment", lead=0.4)
        full = card_base(TRACK_Y1, TRACK_H1)
        head1 = track_head(TRACK_Y1 + TRACK_H1 / 2)
        rt = guard(self, 0.7)
        self.play(FadeOut(spin), Transform(card, full), Transform(head, head1), lt.animate.move_to(P3((lt.get_center()[0], TRACK_Y1 + 0.55))), run_time=rt)
        rows = VGroup(*[VGroup(tbox(k), tline(k)) for k in range(3)])
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in rows], lag_ratio=0.3), run_time=rt)
        until(self, "the boxes tick", lead=0.2)
        lights = d["lights"]
        for k in range(3):
            rt = guard(self, 0.45)
            self.play(Create(ttick(k)), Indicate(lights[3 - k], color=None, scale_factor=1.5), run_time=rt)
        until(self, "It doesn't post a second", lead=0.2)
        ghost = DashedVMobject(RoundedRectangle(width=CW, height=0.5, corner_radius=0.06, stroke_color=BAR1, stroke_width=4).move_to(P3((BX, -1.45))), num_dashes=30)
        rt = guard(self, 0.4)
        self.play(Create(ghost), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeOut(ghost), Indicate(card, color=None, scale_factor=1.03), run_time=rt)
        done(self)


# ══════════════ B05: reads, then answers or changes ══════════════
def b04_label():
    return rlbl("tracking", TRACK_Y1 + 0.55)


ANS = (np.array([R_LEFT[0] - 0.25, 0.35, 0]), np.array([-2.65, 0.35, 0]))
CHG = (np.array([R_RIGHT[0] + 0.25, 0.35, 0]), np.array([4.3, 0.35, 0]))


def b05_labels():
    return VGroup(lbl("answer", (-0.6, 0.9), 40), lbl("change", (3.85, 0.9), 40))


def b05_arrows():
    a = Arrow(ANS[0], ANS[1], buff=0, color=CONN, stroke_width=8, max_tip_length_to_length_ratio=0.12).set_z_index(3)
    c = Arrow(CHG[0], CHG[1], buff=0, color=CONN, stroke_width=8, max_tip_length_to_length_ratio=0.25).set_z_index(3)
    return a, c


class B05_Context(Scene):
    def construct(self):
        d = state(5)
        add_state(self, d)
        old = b04_label()
        self.add(old)
        ln = lens((BX + 0.9, ISSUE_Y + 0.9))
        rt = guard(self, 0.5)
        self.play(FadeOut(old), FadeIn(ln), run_time=rt)
        rt = guard(self, 0.6)
        self.play(ln.animate.move_to(P3((BX - 0.2, ISSUE_Y))), run_time=rt)
        until(self, "its comments", lead=0.2)
        rt = guard(self, 0.6)
        self.play(ln.animate.move_to(P3((BX + 0.3, COMMENT_Y))), run_time=rt)
        until(self, "and the code", lead=0.2)
        rt = guard(self, 0.9)
        self.play(ln.animate.move_to(P3((PG_HOME[0], PG_HOME[1] + 0.2))), run_time=rt)
        until(self, "one of two things", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeOut(ln), Indicate(d["runner"], color=None, scale_factor=1.04), run_time=rt)
        until(self, "If you asked a question", lead=0.2)
        a, c = b05_arrows()
        ls = b05_labels()
        rt = guard(self, 0.7)
        self.play(GrowArrow(a), FadeIn(ls[0]), run_time=rt)
        until(self, "answers in the tracking", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(d["track"], color=None, scale_factor=1.04), run_time=rt)
        until(self, "If you asked for a change", lead=0.2)
        rt = guard(self, 0.6)
        self.play(GrowArrow(c), FadeIn(ls[1]), run_time=rt)
        done(self)


# ══════════════ B06: the claude/ branch ══════════════
def b06_labels():
    return VGroup(lbl("main", (5.55, MY - 0.55), 38), lbl("claude/", (5.2, -1.55), 40))


class B06_Branch(Scene):
    def construct(self):
        d = state(6)
        add_state(self, d)
        a, c = b05_arrows()
        old = b05_labels()
        self.add(a, c, old)
        ml, md = main_line()
        ls = b06_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(a, c, old)), FadeIn(VGroup(ml, md), shift=LEFT * 0.3), FadeIn(ls[0]), run_time=rt)
        until(self, "creates a new branch", lead=0.3)
        br = branch_line()
        rt = guard(self, 0.8)
        self.play(Create(br), run_time=rt)
        until(self, "named with the claude slash", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[1], shift=DOWN * 0.15), run_time=rt)
        until(self, "the branch prefix setting", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ls[1], color=None, scale_factor=1.15), run_time=rt)
        until(self, "Its commits are pushed", lead=0.3)
        src = R_RIGHT + np.array([0.2, 0.3, 0])
        for i, ph in enumerate(("Its commits are pushed", "to that branch", "and nowhere else")):
            until(self, ph, lead=0.15)
            cm = Dot(src, radius=0.13, color=BAR1).set_z_index(5)
            rt = guard(self, 0.6)
            self.play(MoveAlongPath(cm, ArcBetweenPoints(src, P3((BR_DOTS[i], BRY)), angle=-PI / 3)), run_time=rt)
        tip = Dot(P3((6.05, BRY)), radius=0.13, color=TERRA).set_z_index(4)
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(tip), run_time=rt)
        until(self, "Started from an open pull request", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(br, color=None, scale_factor=1.03), run_time=rt)
        done(self)


# ══════════════ B07: the Create PR link ══════════════
def b07_labels():
    return VGroup(rlbl("Create PR", PILL_C[1]), lbl("pull request", (4.75, PR_C[1] + 0.85), 38))


class B07_PRLink(Scene):
    def construct(self):
        d = state(7)
        add_state(self, d)
        old = b06_labels()
        self.add(old)
        ghost = DashedVMobject(RoundedRectangle(width=1.7, height=0.95, corner_radius=0.08, stroke_color=BAR1, stroke_width=4).move_to(P3(PR_C)), num_dashes=28).set_z_index(3)
        rt = guard(self, 0.5)
        self.play(FadeOut(old[0]), Create(ghost), run_time=rt)
        until(self, "When it's done", lead=0.3)
        pill = pr_pill()
        ls = b07_labels()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(pill), run_time=rt)
        until(self, "Create PR", lead=0.6)
        rt = guard(self, 0.5)
        self.play(FadeIn(ls[0], shift=LEFT * 0.2), run_time=rt)
        until(self, "You press it", lead=0.3)
        cur = cursor(-1.2, -1.2).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.6)
        self.play(cur.animate.move_to(P3((PILL_C[0] + 0.3, PILL_C[1] - 0.2))), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Indicate(pill, color=None, scale_factor=1.2), run_time=rt)
        pr = pr_card()
        rt = guard(self, 0.7)
        self.play(FadeOut(ghost), FadeIn(pr, shift=UP * 0.3), FadeIn(ls[1]), run_time=rt)
        until(self, "branch protection rules", lead=0.3)
        ck = check(PR_C[0] - 1.3, PR_C[1], 0.2).set_z_index(6)
        rt = guard(self, 0.4)
        self.play(Create(ck), run_time=rt)
        until(self, "you keep final control", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeOut(cur), Indicate(pr, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B08: what it cannot do ══════════════
class B08_Cannot(Scene):
    def construct(self):
        d = state(8)
        add_state(self, d)
        ck = check(PR_C[0] - 1.3, PR_C[1], 0.2).set_z_index(6)
        old = b07_labels()
        self.add(old, ck, old[1])
        btns = VGroup(*[button(i) for i in range(3)])
        bl = btn_labels()
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(old[0], ck)), FadeOut(old[1]), FadeIn(btns, shift=UP * 0.2), run_time=rt)
        for i, ph in enumerate(("submit formal pull request reviews", "cannot approve pull requests", "cannot merge branches")):
            until(self, ph, lead=0.5)
            rt = guard(self, 0.4)
            self.play(FadeIn(bl[i]), run_time=rt)
            lk = padlock((BTN_XC, BTN_YS[i] + 0.02), 0.9)
            rt = guard(self, 0.5)
            self.play(FadeIn(lk, shift=DOWN * 0.3), run_time=rt)
        until(self, "Those stay with you", lead=0.3)
        cur = cursor(BTN_XC + 0.2, BTN_YS[2] - 0.9).set_z_index(12)
        rt = guard(self, 0.3)
        self.play(FadeIn(cur), run_time=rt)
        rt = guard(self, 0.5)
        self.play(cur.animate.move_to(P3((BTN_XC + 0.3, BTN_YS[2] - 0.35))), run_time=rt)
        done(self)


# ══════════════ B09: a small reach ══════════════
def term_block():
    c = P3((-0.45, 0.4))
    b = rrect(1.0, 0.7, c, PAGE_TOP, INK, 4, r=0.08)
    bar = Rectangle(width=1.0, height=0.14, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(c + np.array([0, 0.28, 0]))
    prompt = VGroup(Line(c + np.array([-0.32, 0.02, 0]), c + np.array([-0.18, -0.08, 0]), color=BAR1, stroke_width=6),
                    Line(c + np.array([-0.18, -0.08, 0]), c + np.array([-0.32, -0.18, 0]), color=BAR1, stroke_width=6),
                    gbar(c[0] - 0.1, c[0] + 0.15, c[1] - 0.18, BAR1, 6))
    return VGroup(b, bar, prompt).set_z_index(6)


class B09_Scope(Scene):
    def construct(self):
        d = state(9)
        add_state(self, d)
        bl = btn_labels()
        self.add(bl)
        fence = DashedVMobject(Rectangle(width=12.2, height=6.35, stroke_color=BAR1, stroke_width=6).move_to(P3((0.0, 0.0))), num_dashes=90).set_z_index(0)
        rt = guard(self, 0.5)
        self.play(FadeOut(bl), run_time=rt)
        until(self, "It only sees the repository", lead=0.3)
        rt = guard(self, 1.2)
        self.play(Create(fence), run_time=rt)
        until(self, "the issue or pull request", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(d["issue"], color=None, scale_factor=1.05), run_time=rt)
        until(self, "It can't run Bash", lead=0.3)
        tb = term_block()
        lb = lbl("Bash", (-0.45, 1.15), 40)
        rt = guard(self, 0.6)
        self.play(FadeIn(tb, shift=UP * 0.2), FadeIn(lb), run_time=rt)
        lk = padlock((0.05, 0.12), 0.9)
        rt = guard(self, 0.5)
        self.play(FadeIn(lk, shift=DOWN * 0.3), run_time=rt)
        until(self, "unless the workflow allows", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(lk, color=None, scale_factor=1.2), run_time=rt)
        until(self, "has no write access to workflow", lead=0.4)
        wf = d["wf"]
        lw = lbl("claude.yml", (-1.3, -1.0), 38)
        rt = guard(self, 0.7)
        self.play(wf.animate.scale(1.3).move_to(P3((0.3, -1.0))), FadeIn(lw), run_time=rt)
        lk2 = padlock((0.95, -1.1), 0.9)
        rt = guard(self, 0.5)
        self.play(FadeIn(lk2, shift=DOWN * 0.3), run_time=rt)
        until(self, "change its own setup", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Indicate(lk2, color=None, scale_factor=1.2), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Setup, B01_Mention, B02_Gate, B03_Runner, B04_Tracking, B05_Context, B06_Branch, B07_PRLink, B08_Cannot, B09_Scope):
    _cls.play = ST.play
