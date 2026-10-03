"""
Manim scenes for show-tell-green-yellow-red (show-tell skill, card #27, Batch 2).

SHOW-TELL: every beat is ONE drawn illustration in the Claude palette, at most a few words of label, and Liam's
narration does the explaining. The ISO KIT block below is the skill's shared drawing kit
(brutalist.art/skills/make/show-tell/templates/iso_kit.py); it is pasted, not imported, because the toolkit's Gate A
copies only scenes.py. This film draws its boxes in an oblique projection (one depth vector, DX/DY) on the kit's palette.

The NDA review skill, exactly as anthropics/claude-for-legal/commercial-legal/skills/nda-review/SKILL.md states it, with
the playbook written by commercial-legal/skills/cold-start-interview/SKILL.md. THE BELT carries inbound NDA pages into
THE SORTER, which reads THE PLAYBOOK binder on its top and sends each NDA down one of three CHUTES into three BINS,
labelled in ink green / yellow / red (the palette forbids green and red tints; no terracotta text). The work area in the
lower left shows each step: no default positions; the cold-start interview; signed agreements and the delta; the
CLAUDE.md practice profile; the two sides; the scope check (auto-yellow); the checks; green (signature); yellow (flags
for an approver); a silent playbook (ask, record); red (a gate arm: legal first); the padlock on green until the
positions carry an attorney's stamp; the non-lawyer gate before signature; and the output page, a draft for attorney
review, not legal advice.
A midpoint guard (ST / guard, from show-tell-context-is-a-budget, 0.22 s margin) keeps every animation off the clip
midpoint, where GATE T and Gate V sample.
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




# ═════════════════════════════ the film: green, yellow, red ═════════════════════════════
# One rig for the whole film, drawn in an oblique projection (every box has the same depth vector DX, DY):
#   the BELT of inbound NDA pages (upper left) runs into the SORTER (a grey machine, lamp top right) with the
#   PLAYBOOK binder on its top; three CHUTES drop from the sorter into three deep-kraft BINS, labelled in ink
#   green / yellow / red. The lower-left WORK AREA holds each beat's one object (the team, the signed stack, a page
#   under review, the signature card, a gate arm, the output page).
SHADOW = "#AFA28A"
BELT = "#E6DFD3"
DEV_EDGE = "#917A55"                                         # dark kraft: SMALL objects and belt edges only
FB_TOP, FB_L, FB_R = "#161411", "#121010", "#0E0C0A"          # extra-dark plinth faces
TILE_TOP, TILE_L, TILE_R = "#D2BD98", "#B39A72", "#9C8462"    # deep kraft: bins, tabs, stamp base
BIN_IN = "#85704F"
GREY_TOP, GREY_L, GREY_R = "#A9ADB3", "#8B8F96", "#767A81"    # the sorter
DX, DY = 0.35, 0.3                                           # the depth vector of every box

PX = [-5.25, -3.95, -2.65, -1.35]                            # page slots on the belt
PY = 0.45                                                    # belt surface (page bottoms)
CX = [1.25, 3.0, 4.75]                                         # chute / bin centres
TIERS = ["green", "yellow", "red"]
LAMP = np.array([5.15, 0.9, 0.0])                            # sorter lamp
BIND_C = np.array([1.7, 1.63, 0.0])                          # binder front centre
WA = np.array([-3.0, -1.85, 0.0])                            # work-area centre


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def lab(s, at, size=44):
    return T(s, size).move_to(P(*at[:2])).set_z_index(9)


def poly(pts, fill, stroke=INK, sw=4):
    return Polygon(*[P(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)


def obox(x0, y0, w, h, top, front, side, sw=4, stroke=INK, d=1.0):
    """Oblique box: front face (x0..x0+w, y0..y0+h), top face and right face pushed back by (DX, DY)*d."""
    dx, dy = DX * d, DY * d
    sd = poly([(x0 + w, y0), (x0 + w + dx, y0 + dy), (x0 + w + dx, y0 + h + dy), (x0 + w, y0 + h)], side, stroke, sw)
    tp = poly([(x0, y0 + h), (x0 + w, y0 + h), (x0 + w + dx, y0 + h + dy), (x0 + dx, y0 + h + dy)], top, stroke, sw)
    fr = poly([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], front, stroke, sw)
    return VGroup(sd, tp, fr)


# ─────────────── the BELT and its NDA pages ───────────────
def belt():
    x0, x1 = -6.0, 0.22                                     # a gap before the sorter (GATE T: no bridge into it)
    top = poly([(x0, 0.30), (x1, 0.30), (x1 + DX, 0.60), (x0 + DX, 0.60)], BELT, BAR1, 3)
    front = poly([(x0, 0.05), (x1, 0.05), (x1, 0.30), (x0, 0.30)], BOX_R, BAR1, 3)
    mid = DashedLine(P(x0 + 0.3, 0.45), P(x1 - 0.1, 0.45), color=GHOST, stroke_width=3, dash_length=0.14)
    return VGroup(front, top, mid).set_z_index(-1)


def page_up(x, y=PY, w=0.62, h=0.8, n=3, lines=BAR2):
    """An NDA page standing up: its bottom edge centred at (x, y)."""
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(P(x, y + h / 2))
    step = h * 0.55 / max(n - 1, 1)
    ls = VGroup(*[Line(P(x - w * 0.3, y + h * (0.78 - 0) - step * i), P(x + w * (0.3 - (0.18 if i % 2 else 0)), y + h * 0.78 - step * i),
                       color=lines, stroke_width=6) for i in range(n)])
    return VGroup(body, ls).set_z_index(1)


def belt_pages():
    return [page_up(x) for x in PX]


def landmine(pg):
    return Dot(np.array(pg[0].get_center()) + np.array([0.0, -0.22, 0.0]), radius=0.08, color=TERRA).set_z_index(2)


# ─────────────── the SORTER, CHUTES and BINS ───────────────
def sorter():
    return obox(0.4, -0.35, 5.2, 1.6, GREY_TOP, GREY_L, GREY_R).set_z_index(3)


def sorter_lamp(color=GHOST):
    return Dot(LAMP, radius=0.13, color=color).set_z_index(4)


def chute(i):
    cx = CX[i]
    return Rectangle(width=0.76, height=1.35, fill_color=BELT, fill_opacity=1, stroke_color=BAR1, stroke_width=4).move_to(P(cx, -0.95)).set_z_index(0)


def bin_back(i):
    cx = CX[i]; x0, x1, y1 = cx - 0.55, cx + 0.55, -1.72
    return poly([(x0, y1), (x1, y1), (x1 + DX, y1 + DY), (x0 + DX, y1 + DY)], BIN_IN, INK, 3).set_z_index(-1)


def bin_front(i):
    cx = CX[i]; x0, x1, y0, y1 = cx - 0.55, cx + 0.55, -2.42, -1.72
    sd = poly([(x1, y0), (x1 + DX, y0 + DY), (x1 + DX, y1 + DY), (x1, y1)], TILE_L, INK, 4)
    fr = poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], TILE_TOP, INK, 4)
    return VGroup(sd, fr).set_z_index(4)


def bin_lamp(i, color=GHOST):
    return Dot(P(CX[i], -2.07), radius=0.1, color=color).set_z_index(5)


def tier_label(i):
    return lab(TIERS[i], (CX[i] + 0.1, -2.85))


def machine():
    """Sorter + chutes + bins + their ghost lamps + the three tier labels, as one dict."""
    return {"sorter": sorter(), "lamp": sorter_lamp(),
            "chutes": VGroup(*[chute(i) for i in range(3)]),
            "backs": VGroup(*[bin_back(i) for i in range(3)]),
            "fronts": VGroup(*[bin_front(i) for i in range(3)]),
            "blamps": VGroup(*[bin_lamp(i) for i in range(3)]),
            "tiers": VGroup(*[tier_label(i) for i in range(3)])}


# ─────────────── THE PLAYBOOK binder (kraft, on a dark plinth, on top of the sorter) ───────────────
def binder(extra=False):
    plinth = obox(0.9, 1.3, 1.6, 0.12, FB_TOP, FB_L, FB_R, sw=2, stroke="#050404", d=0.8)
    body = obox(0.95, 1.42, 1.5, 0.42, BOX_TOP, BOX_R, BOX_L, d=0.8)
    edge = Rectangle(width=1.2, height=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_width=0).move_to(P(1.7, 1.63))
    g = VGroup(plinth, body, edge)
    if extra:
        g.add(extra_page())
    return g.set_z_index(5)


def extra_page():
    """B11 on: the binder is one page thicker (a white sheet lying on its top)."""
    return poly([(1.05, 1.86), (2.35, 1.86), (2.35 + 0.22, 1.86 + 0.19), (1.05 + 0.22, 1.86 + 0.19)], PAGE_TOP, INK, 2).set_z_index(6)


def seal():
    return Dot(P(2.2, 1.63), radius=0.11, color=TERRA).set_z_index(7)


def playbook_label():
    return lab("playbook", (4.1, 2.05))


# ─────────────── work-area cast ───────────────
def figure(x, base=-3.05, body=BOX_R):
    b = RoundedRectangle(width=0.66, height=0.82, corner_radius=0.28, fill_color=body, fill_opacity=1, stroke_color=INK,
                         stroke_width=4).move_to(P(x, base + 0.41))
    h = Circle(radius=0.24, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P(x, base + 1.12))
    return VGroup(b, h).set_z_index(2)


def attorney(x, base=-3.05):
    return figure(x, base, TILE_L)


def big_page(c=WA, w=1.5, h=2.2, n=5, gap=None, band=False):
    c = np.array(c, dtype=float)
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    rows = VGroup()
    top = c[1] + h / 2 - (0.62 if band else 0.35)
    step = (h - (0.9 if band else 0.7)) / max(n - 1, 1)
    for i in range(n):
        y = top - step * i
        x0, x1 = c[0] - w * 0.34, c[0] + w * (0.34 - (0.14 if i % 2 else 0))
        if gap is not None and i == gap:
            rows.add(DashedVMobject(Rectangle(width=x1 - x0, height=0.16).move_to(P((x0 + x1) / 2, y)).set_stroke(BAR1, 3), num_dashes=16))
        else:
            rows.add(Line(P(x0, y), P(x1, y), color=BAR2, stroke_width=11))
    g = VGroup(body, rows)
    if band:
        g.add(Rectangle(width=w - 0.3, height=0.26, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(P(c[0], c[1] + h / 2 - 0.3)))
    return g.set_z_index(2)


def row_y(pg, i):
    return float(np.array(pg[1][i].get_center())[1])


def qcard(c, w=0.95, h=0.62, bars=None):
    c = np.array(c, dtype=float)
    body = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                            stroke_width=3).move_to(c)
    cols = bars or [BAR2, BAR2]
    n = len(cols)
    ls = VGroup(*[Line(c + np.array([-w * 0.32, h * (0.18 - 0.36 * k / max(n - 1, 1)), 0]),
                       c + np.array([w * (0.32 - 0.2 * (k % 2)), h * (0.18 - 0.36 * k / max(n - 1, 1)), 0]),
                       color=cols[k], stroke_width=7) for k in range(n)])
    return VGroup(body, ls).set_z_index(6)


def squiggle(x0, x1, y, amp=0.12):
    return ParametricFunction(lambda t: P(x0 + (x1 - x0) * t, y + amp * np.sin(t * 5 * np.pi) * (1 - 0.4 * t)),
                              t_range=[0, 1], color=INK, stroke_width=6).set_z_index(4)


def signed_page(c, w=0.9, h=1.2):
    c = np.array(c, dtype=float)
    pg = big_page(c, w, h, n=3)
    sig = squiggle(c[0] - w * 0.3, c[0] + w * 0.25, c[1] - h * 0.32, 0.07)
    return VGroup(pg, sig)


def flag(x, y):
    pole = Line(P(x, y - 0.3), P(x, y + 0.3), color=INK, stroke_width=6)
    pen = Polygon(P(x, y + 0.3), P(x + 0.42, y + 0.15), P(x, y + 0.0), fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3)
    return VGroup(pole, pen).set_z_index(6)


def sig_card(c=(-2.0, -1.95)):
    c = np.array([c[0], c[1], 0.0])
    body = Rectangle(width=2.5, height=1.45, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=5).move_to(c)
    lines = VGroup(Line(c + np.array([-0.9, 0.4, 0]), c + np.array([0.9, 0.4, 0]), color=BAR2, stroke_width=9),
                   Line(c + np.array([-0.9, 0.12, 0]), c + np.array([0.5, 0.12, 0]), color=BAR2, stroke_width=9))
    sline = Line(c + np.array([-0.95, -0.45, 0]), c + np.array([0.95, -0.45, 0]), color=BAR1, stroke_width=5)
    return VGroup(body, lines, sline).set_z_index(3)


def sig_mark(c=(-2.0, -1.95)):
    return squiggle(c[0] - 0.8, c[0] + 0.6, c[1] - 0.3, 0.1)


def gate_arm(pivot, length=2.3):
    """A grey gate arm, standing up; rotate it by -PI/2 about `pivot` to close it."""
    pv = np.array(pivot, dtype=float)
    arm = Rectangle(width=0.22, height=length, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to(pv + UP * length / 2)
    post = Rectangle(width=0.36, height=0.9, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(pv + DOWN * 0.45)
    return VGroup(post, arm).set_z_index(6)


def padlock(c=(1.3, -1.0)):
    c = np.array([c[0], c[1], 0.0])
    shackle = Arc(radius=0.2, start_angle=0, angle=PI, color=INK, stroke_width=8).move_to(c + UP * 0.34)
    body = RoundedRectangle(width=0.66, height=0.52, corner_radius=0.08, fill_color=TILE_TOP, fill_opacity=1, stroke_color=INK,
                            stroke_width=4).move_to(c)
    return VGroup(shackle, body).set_z_index(7)


def stamp(c):
    c = np.array(c, dtype=float)
    handle = RoundedRectangle(width=0.2, height=0.5, corner_radius=0.08, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(c + UP * 0.38)
    base = Rectangle(width=0.62, height=0.24, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    return VGroup(handle, base).set_z_index(8)


# ─────────────── the world, rebuilt at the start of each beat ───────────────
def world(self, after, extra_page_on=False, sealed=False):
    """Add the persistent cast as it stands after beat `after` (0 = belt only). Returns a dict."""
    w = {"belt": belt(), "pages": belt_pages()}
    self.add(w["belt"], *w["pages"])
    if after >= 1:
        w.update(machine())
        self.add(w["chutes"], w["backs"], w["sorter"], w["lamp"], w["fronts"], w["blamps"], w["tiers"])
    if after >= 2:
        w["binder"] = binder(extra_page_on)
        w["pbl"] = playbook_label()
        self.add(w["binder"], w["pbl"])
    if sealed:
        w["seal"] = seal()
        self.add(w["seal"])
    return w


def ride(self, w, rt=1.0):
    """The belt advances one slot: the front page slides into the sorter, a new page arrives at the back."""
    pages = w["pages"]
    last = pages[-1]
    newp = page_up(PX[0])
    self.play(*[p.animate.shift(RIGHT * 1.3) for p in pages[:-1]], last.animate.move_to(P(1.1, PY + 0.4)),
              FadeIn(newp, shift=RIGHT * 0.6), run_time=rt)
    self.remove(last)
    w["pages"] = [newp] + pages[:-1]


def drop(self, i, rt=0.6, dot=False):
    """A small page drops from the sorter down chute i into its bin; the bin lamp lights. Returns the lit lamp."""
    rt = guard(self, rt + 0.35)
    sp = page_up(CX[i], -0.45, 0.46, 0.6, n=2)
    if dot:
        sp.add(Dot(np.array(sp[0].get_center()) + np.array([0, -0.15, 0]), radius=0.06, color=TERRA).set_z_index(2))
    self.add(sp)
    Scene.play(self, sp.animate.shift(DOWN * 1.8), run_time=rt - 0.35, rate_func=ease_in)
    self.remove(sp)
    lit = bin_lamp(i, TERRA)
    Scene.play(self, FadeIn(lit, scale=0.4), run_time=0.35)
    return lit


def lamp_on(self):
    lit = sorter_lamp(TERRA)
    self.play(FadeIn(lit, scale=0.4), run_time=0.35)
    return lit


def into_sorter(self, mob, rt=0.6):
    """A work-area object shrinks into the sorter's lower-left corner."""
    self.play(mob.animate.scale(0.25).move_to(P(0.9, -0.1)), run_time=rt, rate_func=ease_in)
    self.remove(mob)


def out_of_sorter(self, mob, rt=0.6):
    """A work-area object grows out of the sorter's lower-left corner to where it was built."""
    rt = guard(self, rt)
    end = np.array(mob.get_center())
    mob.scale(0.25).move_to(P(0.9, -0.1))
    self.add(mob)
    Scene.play(self, mob.animate.scale(4.0).move_to(end), run_time=rt)


def fly(self, mob, to, rt=0.8, angle=-0.6, shrink=0.4):
    """MoveAlongPath on an arc, then a shrink (never both on one object in one play)."""
    a = np.array(mob.get_center())
    self.play(MoveAlongPath(mob, ArcBetweenPoints(a, np.array(to, dtype=float), angle=angle)), run_time=rt)
    self.play(mob.animate.scale(shrink).set_opacity(0), run_time=0.25)
    self.remove(mob)


# ══════════════ B00: inbound NDAs on a belt ══════════════
def b00_marks(pages):
    chk = VGroup(*[check(PX[k], 1.55, 0.13, INK, 6) for k in (0, 2, 3)]).set_z_index(3)
    return chk, landmine(pages[1])


def b00_outline():
    return DashedVMobject(Rectangle(width=5.2, height=1.6).move_to(P(3.0, 0.45)).set_stroke(BAR1, 3), num_dashes=40).set_z_index(0)


class B00_Belt(Scene):
    def construct(self):
        bl = belt()
        self.play(FadeIn(VGroup(bl[0], bl[1])), run_time=0.5)
        self.play(Create(bl[2]), run_time=0.4)
        li = lab("inbound NDAs", (-4.3, 2.35))
        self.play(FadeIn(li), run_time=0.4)
        pages = belt_pages()
        until(self, "Its premise is simple", lead=0.6)
        for pg in pages:
            self.play(FadeIn(pg, shift=RIGHT * 0.6), run_time=0.35)
        until(self, "Most inbound NDAs are fine", lead=0.2)
        chk, dot = b00_marks(pages)
        self.play(LaggedStart(*[Create(c) for c in chk], lag_ratio=0.4), run_time=0.9)
        until(self, "A few have landmines", lead=0.2)
        self.play(FadeIn(dot, scale=0.3), run_time=0.4)
        self.play(Indicate(pages[1], color=None, scale_factor=1.08), run_time=0.5)
        until(self, "The skill sorts them", lead=0.3)
        self.play(Create(b00_outline()), run_time=0.8)
        done(self)


# ══════════════ B01: three chutes ══════════════
class B01_Chutes(Scene):
    def construct(self):
        w = world(self, 0)
        chk, dot = b00_marks(w["pages"])
        li = lab("inbound NDAs", (-4.3, 2.35))
        ol = b00_outline()
        w["pages"][1].add(dot)
        self.add(chk, li, ol)
        m = machine()
        ln = lab("NDA review", (4.1, 2.05))
        self.play(FadeOut(chk), FadeOut(li), run_time=0.4)
        self.play(FadeOut(ol), FadeIn(m["sorter"], shift=UP * 0.4), FadeIn(m["lamp"]), run_time=0.6)
        self.play(FadeIn(ln), run_time=0.3)
        until(self, "one of three chutes", lead=0.4)
        self.play(LaggedStart(*[Create(c) for c in m["chutes"]], lag_ratio=0.3), run_time=0.6)
        self.play(FadeIn(m["backs"], shift=UP * 0.3), FadeIn(m["fronts"], shift=UP * 0.3), FadeIn(m["blamps"]), run_time=0.5)
        lits = []
        for i, ph in enumerate(("Green should need", "Yellow needs", "Red stops")):
            until(self, ph, lead=1.4)
            ride(self, w, 0.7)
            lits.append(drop(self, i, 0.55, dot=(i == 2)))
            self.play(FadeIn(m["tiers"][i]), run_time=0.3)
        until(self, "built for sales", lead=0.2)
        self.play(Indicate(m["tiers"], color=None, scale_factor=1.06), run_time=0.6)
        done(self)


# ══════════════ B02: no default positions: the playbook ══════════════
def open_book():
    c = WA + np.array([-0.6, -0.15, 0])
    left = Rectangle(width=1.6, height=1.9, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + LEFT * 0.8)
    right = Rectangle(width=1.6, height=1.9, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + RIGHT * 0.8)
    slots = VGroup()
    for side in (-0.8, 0.8):
        for k in range(4):
            slots.add(DashedVMobject(Rectangle(width=1.1, height=0.26).move_to(c + np.array([side, 0.56 - 0.38 * k, 0])).set_stroke(BAR1, 3), num_dashes=18))
    return VGroup(left, right, slots).set_z_index(2)


def b01_end(self):
    w = world(self, 1)
    lits = VGroup(*[bin_lamp(i, TERRA) for i in range(3)])
    ln = lab("NDA review", (4.1, 2.05))
    self.add(lits, ln)
    return w, lits, ln


class B02_NoDefaults(Scene):
    def construct(self):
        w, lits, ln = b01_end(self)
        self.play(FadeOut(lits), FadeOut(ln), run_time=0.4)
        until(self, "Sorted against what", lead=0.2)
        ride(self, w, 0.8)
        self.play(Indicate(w["sorter"], color=None, scale_factor=1.03), run_time=0.5)
        until(self, "no default positions", lead=0.4)
        bk = open_book()
        self.play(FadeIn(bk[0]), FadeIn(bk[1]), run_time=0.5)
        self.play(LaggedStart(*[Create(s) for s in bk[2]], lag_ratio=0.12), run_time=1.0)
        lnd = lab("no defaults", (-3.6, -0.5))
        self.play(FadeIn(lnd), run_time=0.35)
        until(self, "The positions live", lead=0.4)
        bd = binder()
        self.play(FadeIn(bd, shift=DOWN * 0.9), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(playbook_label()), run_time=0.35)
        until(self, "reads it before", lead=0.3)
        lamp_on(self)
        done(self)


# ══════════════ B03: the cold-start interview ══════════════
TEAM_X = [-5.4, -4.55, -3.7]
QC_AT = [P(-2.3, -2.55), P(-1.2, -2.55), P(-0.1, -2.55)]


def team():
    return VGroup(*[figure(x) for x in TEAM_X])


def b02_end(self):
    w = world(self, 2)
    bk = open_book()
    lnd = lab("no defaults", (-3.6, -0.5))
    lit = sorter_lamp(TERRA)
    self.add(bk, lnd, lit)
    return w, VGroup(bk, lnd, lit)


class B03_Interview(Scene):
    def construct(self):
        w, ex = b02_end(self)
        self.play(FadeOut(ex), run_time=0.45)
        until(self, "cold-start interview", lead=0.5)
        tm = team()
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.4) for f in tm], lag_ratio=0.25), run_time=0.8)
        lci = lab("cold-start interview", (-3.9, -1.2), 42)
        self.play(FadeIn(lci), run_time=0.35)
        cards = [qcard(c) for c in QC_AT]
        for k, ph in enumerate(("your positions", "your escalation rules", "the one thing")):
            until(self, ph, lead=0.4)
            out_of_sorter(self, cards[k], 0.55)
        until(self, "refuse to sign", lead=0.2)
        g = VGroup(*cards)
        self.play(*[MoveAlongPath(c, ArcBetweenPoints(np.array(c.get_center()), BIND_C + UP * 0.2, angle=-0.5)) for c in cards], run_time=0.55)
        self.play(g.animate.scale(0.4).set_opacity(0), run_time=0.25)
        self.remove(g)
        done(self)


# ══════════════ B04: signed agreements; the delta ══════════════
STACK_C = P(-2.35, -2.0)
BAR_X = [-1.1, -0.45]


def signed_stack():
    return VGroup(*[signed_page(STACK_C + np.array([0.14 * k, 0.1 * k, 0])) for k in range(3)])


def delta_bars():
    stated = Rectangle(width=0.44, height=1.1, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(P(BAR_X[0], -3.0 + 0.55))
    signed = Rectangle(width=0.44, height=1.75, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(P(BAR_X[1], -3.0 + 0.875))
    return stated.set_z_index(3), signed.set_z_index(3)


def delta_box():
    return DashedVMobject(Rectangle(width=0.44, height=0.65).move_to(P(BAR_X[0], -1.9 + 0.325)).set_stroke(INK, 4), num_dashes=14).set_z_index(3)


def b03_end(self):
    w = world(self, 2)
    tm = team()
    lci = lab("cold-start interview", (-3.9, -1.2), 42)
    self.add(tm, lci)
    return w, tm, lci


class B04_Delta(Scene):
    def construct(self):
        w, tm, lci = b03_end(self)
        self.play(FadeOut(lci), run_time=0.35)
        until(self, "recent signed agreements", lead=0.3)
        st = signed_stack()
        for pg in st:
            self.play(FadeIn(pg, shift=RIGHT * 0.8), run_time=0.35)
        lsg = lab("signed", (-2.2, -0.62))
        self.play(FadeIn(lsg), run_time=0.3)
        until(self, "What a team says", lead=0.3)
        s1, s2 = delta_bars()
        self.play(GrowFromEdge(s1, DOWN), run_time=0.5)
        until(self, "what it actually signs", lead=0.3)
        self.play(GrowFromEdge(s2, DOWN), run_time=0.5)
        until(self, "Where they differ", lead=0.3)
        db = delta_box()
        ld = lab("delta", (-0.25, -0.62))
        self.play(Create(db), FadeIn(ld), run_time=0.5)
        until(self, "the real playbook", lead=0.6)
        dp = qcard(P(BAR_X[0], -1.55), 0.7, 0.46, [BAR1])
        self.play(FadeIn(dp, scale=0.5), run_time=0.3)
        fly(self, dp, BIND_C + UP * 0.2, rt=0.55, angle=-0.4)
        done(self)


# ══════════════ B05: the practice profile, CLAUDE.md ══════════════
PROF_C = P(-3.4, -2.1)


def profile_page():
    return big_page(PROF_C, 2.0, 1.95, n=6)


def b04_end(self):
    w = world(self, 2)
    tm = team()
    st = signed_stack()
    s1, s2 = delta_bars()
    ex = VGroup(tm, st, lab("signed", (-2.2, -0.62)), s1, s2, delta_box(), lab("delta", (-0.25, -0.62)))
    self.add(ex)
    return w, ex


class B05_Profile(Scene):
    def construct(self):
        w, ex = b04_end(self)
        self.play(FadeOut(ex), run_time=0.45)
        until(self, "plain-English practice profile", lead=0.5)
        pp = profile_page()
        self.play(FadeIn(pp[0], shift=UP * 0.3), run_time=0.4)
        lc = lab("CLAUDE.md", (-3.4, -0.5))
        self.play(FadeIn(lc), run_time=0.3)
        self.play(LaggedStart(*[Create(r) for r in pp[1]], lag_ratio=0.3), run_time=1.1)
        until(self, "every skill in the plugin", lead=0.3)
        th = Line(P(-2.35, -1.5), P(0.4, -0.2), color=BAR1, stroke_width=5).set_z_index(1)
        self.play(Create(th), run_time=0.5)
        lamp_on(self)
        until(self, "You edit the document", lead=0.2)
        y = row_y(pp, 3)
        cur = cursor(-2.6, y + 0.05, 0.42).set_z_index(8)
        self.play(FadeIn(cur, shift=UP * 0.2), run_time=0.35)
        nl = Line(P(-4.08, y), P(-2.92, y), color=BAR1, stroke_width=11).set_z_index(3)
        self.play(Create(nl), run_time=0.5)
        done(self)


# ══════════════ B06: two playbooks, sales side and purchasing side ══════════════
SIDE_C = [P(-4.55, -1.55), P(-2.35, -1.55)]


def side_page(k):
    pg = big_page(SIDE_C[k], 1.35, 1.65, n=4)
    tab = Rectangle(width=0.55, height=0.26, fill_color=TILE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(SIDE_C[k] + np.array([-0.3, 0.95, 0]))
    return VGroup(tab, pg).set_z_index(2)


def b05_end(self):
    w = world(self, 2)
    pp = profile_page()
    y = row_y(pp, 3)
    ex = VGroup(pp, lab("CLAUDE.md", (-3.4, -0.5)), Line(P(-2.35, -1.5), P(0.4, -0.2), color=BAR1, stroke_width=5).set_z_index(1),
                sorter_lamp(TERRA), cursor(-2.6, y + 0.05, 0.42).set_z_index(8),
                Line(P(-4.08, y), P(-2.92, y), color=BAR1, stroke_width=11).set_z_index(3))
    self.add(ex)
    return w, ex


class B06_Sides(Scene):
    def construct(self):
        w, ex = b05_end(self)
        self.play(FadeOut(ex), run_time=0.45)
        until(self, "two playbooks", lead=0.4)
        sp = [side_page(0), side_page(1)]
        ls = [lab("sales", (SIDE_C[0][0], -2.85)), lab("purchasing", (SIDE_C[1][0], -2.85))]
        until(self, "sales-side", lead=0.3)
        self.play(FadeIn(sp[0], shift=UP * 0.3), FadeIn(ls[0]), run_time=0.45)
        until(self, "and purchasing-side", lead=0.2)
        self.play(FadeIn(sp[1], shift=UP * 0.3), FadeIn(ls[1]), run_time=0.45)
        until(self, "reads the side that matches", lead=0.3)
        self.play(sp[0].animate.shift(UP * 0.25), run_time=0.35)
        th = Line(P(-4.3, -0.47), P(0.4, -0.15), color=BAR1, stroke_width=5).set_z_index(1)
        self.play(Create(th), run_time=0.5)
        lamp_on(self)
        until(self, "stops if that side", lead=0.2)
        dash = DashedVMobject(Rectangle(width=1.55, height=1.95).move_to(SIDE_C[1]).set_stroke(BAR1, 3), num_dashes=30).set_z_index(3)
        self.play(Create(dash), run_time=0.5)
        done(self)


# ══════════════ B07: the scope check: more than an NDA? ══════════════
def scope_page():
    return big_page(WA, 1.5, 2.2, n=5)


def clause_band(pg):
    y = row_y(pg, 2)
    band = Rectangle(width=1.05, height=0.2, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(P(-3.0, y)).set_z_index(4)
    return band


def b06_end(self):
    w = world(self, 2)
    sp = VGroup(side_page(0).shift(UP * 0.25), side_page(1))
    ex = VGroup(sp, lab("sales", (SIDE_C[0][0], -2.85)), lab("purchasing", (SIDE_C[1][0], -2.85)),
                Line(P(-4.3, -0.47), P(0.4, -0.15), color=BAR1, stroke_width=5).set_z_index(1), sorter_lamp(TERRA),
                DashedVMobject(Rectangle(width=1.55, height=1.95).move_to(SIDE_C[1]).set_stroke(BAR1, 3), num_dashes=30).set_z_index(3))
    self.add(ex)
    return w, ex


class B07_Scope(Scene):
    def construct(self):
        w, ex = b06_end(self)
        self.play(FadeOut(ex), run_time=0.45)
        until(self, "Now an NDA arrives", lead=0.3)
        ride(self, w, 0.8)
        pg = scope_page()
        out_of_sorter(self, pg, 0.6)
        until(self, "doing more than its name", lead=0.4)
        top, bot = row_y(pg, 0) + 0.25, row_y(pg, 4) - 0.25
        sc = Line(P(-3.85, top), P(-2.15, top), color=TERRA, stroke_width=7).set_z_index(5)
        band = clause_band(pg)
        dot = Dot(P(-3.72, row_y(pg, 2)), radius=0.08, color=TERRA).set_z_index(5)
        guard(self, 1.4)
        Scene.play(self, FadeIn(sc), run_time=0.2)
        Scene.play(self, sc.animate.move_to(P(-3.0, row_y(pg, 2))), run_time=0.75)
        Scene.play(self, FadeIn(band), FadeIn(dot, scale=0.4), FadeOut(sc), run_time=0.35)
        lm = lab("more than an NDA", (-2.4, -0.42), 38)
        self.play(FadeIn(lm), run_time=0.35)
        until(self, "goes to yellow automatically", lead=0.6)
        into_sorter(self, VGroup(pg, band, dot), 0.5)
        drop(self, 1, 0.55)
        until(self, "routed for attorney review", lead=0.2)
        self.play(Indicate(w["tiers"][1], color=None, scale_factor=1.1), run_time=0.6)
        done(self)


# ══════════════ B08: the checks ══════════════
CHK_PAGE = P(-4.45, -1.85)
ROWS_Y = [-0.95, -1.45, -1.95, -2.45, -2.95]
SQ_X = -2.55


def check_rows():
    g = VGroup()
    for y in ROWS_Y:
        sq = Square(0.36, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(P(SQ_X, y))
        bar = Line(P(SQ_X + 0.35, y), P(SQ_X + 1.75, y), color=BAR2, stroke_width=11)
        g.add(VGroup(sq, bar))
    return g.set_z_index(3)


def row_check(k):
    return check(SQ_X - 0.02, ROWS_Y[k] + 0.02, 0.13, INK, 6).set_z_index(5)


def b07_end(self):
    w = world(self, 2)
    lit = bin_lamp(1, TERRA)
    lm = lab("more than an NDA", (-2.4, -0.42), 38)
    self.add(lit, lm)
    return w, VGroup(lit, lm)


class B08_Checks(Scene):
    def construct(self):
        w, ex = b07_end(self)
        self.play(FadeOut(ex), run_time=0.4)
        until(self, "Then the checks", lead=0.3)
        ride(self, w, 0.7)
        pg = big_page(CHK_PAGE, 1.5, 2.2, n=5)
        out_of_sorter(self, pg, 0.55)
        rows = check_rows()
        lc = lab("checks", (-1.3, -0.38))
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows], lag_ratio=0.15), FadeIn(lc), run_time=0.7)
        for k, ph in enumerate(("mutuality", "the term", "the survival period", "the carve-outs", "governing law")):
            until(self, ph, lead=0.3)
            self.play(Create(row_check(k)), run_time=0.3)
        until(self, "Each one is checked", lead=0.2)
        self.play(Indicate(w["binder"], color=None, scale_factor=1.08), run_time=0.5)
        lamp_on(self)
        done(self)


# ══════════════ B09: green: route to signature ══════════════
def b08_end(self):
    w = world(self, 2)
    pg = big_page(CHK_PAGE, 1.5, 2.2, n=5)
    rows = check_rows()
    cks = VGroup(*[row_check(k) for k in range(5)])
    lc, lit = lab("checks", (-1.3, -0.38)), sorter_lamp(TERRA)
    self.add(pg, rows, cks, lc, lit)
    return w, pg, rows, cks, lc, lit


SIG_C = (-2.0, -1.95)


class B09_Green(Scene):
    def construct(self):
        w, pg, rows, cks, lc, lit = b08_end(self)
        until(self, "it's green", lead=0.9)
        self.play(FadeOut(rows), FadeOut(cks), FadeOut(lc), FadeOut(lit), run_time=0.4)
        into_sorter(self, pg, 0.45)
        drop(self, 0, 0.55)
        until(self, "route to signature", lead=0.3)
        sc = sig_card(SIG_C)
        ls = lab("signature", (-2.0, -0.72))
        self.play(FadeIn(sc, shift=UP * 0.4), FadeIn(ls), run_time=0.5)
        self.play(Create(sig_mark(SIG_C)), run_time=0.8)
        until(self, "The summary says only", lead=0.3)
        sl = qcard(P(-4.65, -2.25), 1.5, 0.5, [BAR1])
        self.play(FadeIn(sl, shift=UP * 0.3), run_time=0.4)
        until(self, "Route for signature per", lead=0.2)
        self.play(Create(check(-4.65, -1.7, 0.14, INK, 6).set_z_index(7)), run_time=0.35)
        done(self)


# ══════════════ B10: yellow: a lawyer's eyes on specific items ══════════════
def b09_end(self):
    w = world(self, 2)
    ex = VGroup(bin_lamp(0, TERRA), sig_card(SIG_C), lab("signature", (-2.0, -0.72)), sig_mark(SIG_C),
                qcard(P(-4.65, -2.25), 1.5, 0.5, [BAR1]), check(-4.65, -1.7, 0.14, INK, 6).set_z_index(7))
    self.add(ex)
    return w, ex


APR_X = -0.55
FLAG_ROWS = (1, 3)


class B10_Yellow(Scene):
    def construct(self):
        w, ex = b09_end(self)
        self.play(FadeOut(ex), run_time=0.4)
        ride(self, w, 0.7)
        pg = big_page(CHK_PAGE, 1.5, 2.2, n=5)
        out_of_sorter(self, pg, 0.5)
        until(self, "deviates from the playbook", lead=0.3)
        fl = [flag(-3.3, row_y(pg, k)) for k in FLAG_ROWS]
        self.play(FadeIn(fl[0], shift=UP * 0.2), run_time=0.35)
        until(self, "doesn't address it", lead=0.3)
        self.play(FadeIn(fl[1], shift=UP * 0.2), run_time=0.35)
        until(self, "it's yellow", lead=0.6)
        into_sorter(self, pg, 0.45)
        drop(self, 1, 0.5)
        until(self, "Each flagged item", lead=0.3)
        for k, x in enumerate((-2.95, -2.2)):
            self.play(fl[k].animate.move_to(P(x, -2.6)), run_time=0.4)
        until(self, "for a named approver", lead=0.3)
        ap = attorney(APR_X)
        la = lab("approver", (APR_X, -1.35))
        self.play(FadeIn(ap, shift=UP * 0.3), FadeIn(la), run_time=0.5)
        until(self, "surfaces them for a human", lead=0.3)
        self.play(Indicate(ap, color=None, scale_factor=1.1), run_time=0.6)
        done(self)


# ══════════════ B11: the playbook is silent; it asks, and records ══════════════
GAP_ROW = 2
ASK_X = -0.55


def b10_end(self):
    w = world(self, 2)
    fl = VGroup(flag(-2.95, -2.6), flag(-2.2, -2.6))
    ex = VGroup(bin_lamp(1, TERRA), fl, attorney(APR_X), lab("approver", (APR_X, -1.35)))
    self.add(ex)
    return w, ex


class B11_Silent(Scene):
    def construct(self):
        w, ex = b10_end(self)
        self.play(FadeOut(ex), run_time=0.4)
        until(self, "silent on a term", lead=0.9)
        ride(self, w, 0.6)
        pg = big_page(CHK_PAGE, 1.5, 2.2, n=5, gap=GAP_ROW)
        out_of_sorter(self, pg, 0.5)
        lr = lab("residuals", (-2.35, row_y(pg, GAP_ROW)), 42)
        self.play(FadeIn(lr), run_time=0.3)
        until(self, "asks you for your default", lead=0.4)
        fg = figure(ASK_X)
        self.play(FadeIn(fg, shift=UP * 0.3), run_time=0.4)
        q = qcard(P(ASK_X, -1.1), 0.9, 0.55)
        out_of_sorter(self, q, 0.45)
        until(self, "when it should be green", lead=0.3)
        ans = qcard(P(ASK_X - 1.15, -1.1), 0.95, 0.72, [BAR1, BAR2, BAR3])
        self.play(FadeOut(q), FadeIn(ans, shift=LEFT * 0.3), run_time=0.4)
        until(self, "records your answer", lead=0.3)
        fly(self, ans, BIND_C + UP * 0.3, rt=0.55, angle=-0.5)
        xp = extra_page()
        self.play(FadeIn(xp, shift=DOWN * 0.3), run_time=0.35)
        until(self, "the next review is consistent", lead=0.3)
        y = row_y(pg, GAP_ROW)
        self.play(Create(Line(P(-4.96, y), P(-4.18, y), color=BAR1, stroke_width=11).set_z_index(4)), run_time=0.5)
        done(self)


# ══════════════ B12: red: stop, legal first ══════════════
ARM_PIV = P(-3.3, -2.0)
REC_C = P(-0.45, -2.0)


def oneway(pg):
    y = row_y(pg, 1)
    return Arrow(P(-5.0, y), P(-3.9, y), buff=0, color=INK, stroke_width=8, max_tip_length_to_length_ratio=0.3).set_z_index(5)


def b11_end(self):
    w = world(self, 2, extra_page_on=True)
    pg = big_page(CHK_PAGE, 1.5, 2.2, n=5, gap=GAP_ROW)
    y = row_y(pg, GAP_ROW)
    ex = VGroup(pg, lab("residuals", (-2.35, y), 42), figure(ASK_X),
                Line(P(-4.96, y), P(-4.18, y), color=BAR1, stroke_width=11).set_z_index(4))
    self.add(ex)
    return w, ex


class B12_Red(Scene):
    def construct(self):
        w, ex = b11_end(self)
        self.play(FadeOut(ex), run_time=0.4)
        until(self, "never-accept list", lead=0.6)
        ride(self, w, 0.6)
        pg = big_page(CHK_PAGE, 1.5, 2.2, n=5)
        out_of_sorter(self, pg, 0.5)
        until(self, "a one-way NDA", lead=0.3)
        ar = oneway(pg)
        lo = lab("one-way", (-2.35, row_y(pg, 1)), 42)
        self.play(FadeIn(ar, shift=RIGHT * 0.3), FadeIn(lo), run_time=0.5)
        until(self, "Stop, and talk to legal", lead=0.9)
        self.play(FadeOut(lo), run_time=0.25)
        into_sorter(self, VGroup(pg, ar), 0.4)
        drop(self, 2, 0.5)
        ga = gate_arm(ARM_PIV, 2.0)
        rec = DashedVMobject(RoundedRectangle(width=1.3, height=0.9, corner_radius=0.1).move_to(REC_C).set_stroke(BAR1, 3), num_dashes=24).set_z_index(3)
        ll = lab("legal first", (-2.3, -1.2))
        self.play(FadeIn(ga, shift=UP * 0.3), FadeIn(ll), run_time=0.4)
        self.play(Rotate(ga[1], angle=-PI / 2, about_point=ARM_PIV), run_time=0.5)
        until(self, "No contract record", lead=0.2)
        self.play(Create(rec), run_time=0.6)
        done(self)


# ══════════════ B13: the lock on green: attorney-reviewed positions ══════════════
ATT_X = -4.6
STAMP_HOME = P(-3.7, -2.0)


def b12_end(self):
    w = world(self, 2, extra_page_on=True)
    ga = gate_arm(ARM_PIV, 2.0)
    ga[1].rotate(-PI / 2, about_point=ARM_PIV)
    ex = VGroup(bin_lamp(2, TERRA), ga, lab("legal first", (-2.3, -1.2)),
                DashedVMobject(RoundedRectangle(width=1.3, height=0.9, corner_radius=0.1).move_to(REC_C).set_stroke(BAR1, 3), num_dashes=24).set_z_index(3))
    self.add(ex)
    return w, ex


class B13_Lock(Scene):
    def construct(self):
        w, ex = b12_end(self)
        self.play(FadeOut(ex), run_time=0.4)
        until(self, "guards the green chute", lead=0.4)
        lk = padlock()
        llk = lab("locked", (0.05, -1.0), 42)
        self.play(FadeIn(lk, shift=DOWN * 0.4), run_time=0.4, rate_func=ease_in)
        self.play(FadeIn(llk), run_time=0.3)
        until(self, "can't be issued against default", lead=0.6)
        ride(self, w, 0.6)
        rt = guard(self, 1.3)
        sp = page_up(CX[0], -0.45, 0.46, 0.6, n=2)
        self.add(sp)
        Scene.play(self, sp.animate.shift(DOWN * 0.35), run_time=rt * 0.4)
        Scene.play(self, sp.animate.shift(UP * 0.35), run_time=rt * 0.4)
        self.remove(sp)
        drop(self, 1, 0.5)
        until(self, "attorney-reviewed positions", lead=0.9)
        at = attorney(ATT_X)
        stp = stamp(STAMP_HOME)
        self.play(FadeIn(at, shift=UP * 0.3), FadeIn(stp), run_time=0.45)
        rt = guard(self, 1.4)
        Scene.play(self, MoveAlongPath(stp, ArcBetweenPoints(STAMP_HOME, P(1.7, 2.35), angle=-0.7)), run_time=rt * 0.55)
        Scene.play(self, stp.animate.shift(DOWN * 0.45), run_time=rt * 0.2, rate_func=ease_in)
        sl = seal()
        lar = lab("attorney-reviewed", (1.9, 2.95), 42)
        Scene.play(self, stp.animate.shift(UP * 0.45), FadeIn(sl, scale=0.3), run_time=rt * 0.25)
        self.play(MoveAlongPath(stp, ArcBetweenPoints(P(1.7, 2.35), STAMP_HOME, angle=0.7)), run_time=0.6)
        self.play(FadeIn(lar), run_time=0.3)
        until(self, "In the skill's words", lead=0.3)
        self.play(lk[0].animate.shift(UP * 0.25), run_time=0.4)
        lop = lab("open", (0.05, -1.0), 42)
        self.play(FadeOut(llk), run_time=0.25)
        self.play(FadeIn(lop), run_time=0.3)
        done(self)


# ══════════════ B14: the non-lawyer gate before signature ══════════════
GATE_PIV = P(0.0, -2.4)
BRIEF_C = P(-4.1, -2.0)
ATT2_X = -5.35


def b13_end(self):
    w = world(self, 2, extra_page_on=True, sealed=True)
    lk = padlock()
    lk[0].shift(UP * 0.25)
    ex = VGroup(bin_lamp(1, TERRA), attorney(ATT_X), stamp(STAMP_HOME), lab("attorney-reviewed", (1.9, 2.95), 42),
                lk, lab("open", (0.05, -1.0), 42))
    self.add(ex)
    return w, ex


class B14_Gate(Scene):
    def construct(self):
        w, ex = b13_end(self)
        at = ex[1]
        self.play(FadeOut(VGroup(ex[0], ex[2], ex[3], ex[4], ex[5])), at.animate.move_to(P(ATT2_X, -3.05 + 0.68)), run_time=0.5)
        until(self, "Even after green", lead=0.3)
        ride(self, w, 0.6)
        drop(self, 0, 0.5)
        sc = sig_card(SIG_C)
        self.play(FadeIn(sc, shift=UP * 0.4), run_time=0.45)
        until(self, "pauses before signature", lead=0.3)
        ga = gate_arm(GATE_PIV, 2.4)
        la = lab("attorney?", (-2.0, -0.62))
        self.play(FadeIn(ga, shift=UP * 0.3), FadeIn(la), run_time=0.4)
        self.play(Rotate(ga[1], angle=PI / 2, about_point=GATE_PIV), run_time=0.5)
        until(self, "writes a one-page brief", lead=0.3)
        br = big_page(BRIEF_C, 0.8, 1.05, n=3)
        self.play(FadeIn(br, shift=LEFT * 1.2), run_time=0.5)
        until(self, "explicit yes", lead=1.1)
        ck = check(ATT2_X + 0.05, -1.35, 0.16, INK, 7).set_z_index(7)
        self.play(Create(ck), run_time=0.35)
        self.play(Rotate(ga[1], angle=-PI / 2, about_point=GATE_PIV), run_time=0.5)
        done(self)


# ══════════════ B15: a draft for attorney review, not legal advice ══════════════
OUT_C = P(-5.0, -1.85)


def b14_end(self):
    w = world(self, 2, extra_page_on=True, sealed=True)
    ga = gate_arm(GATE_PIV, 2.4)
    ex = VGroup(bin_lamp(0, TERRA), attorney(ATT2_X), sig_card(SIG_C), ga, lab("attorney?", (-2.0, -0.62)),
                big_page(BRIEF_C, 0.8, 1.05, n=3), check(ATT2_X + 0.05, -1.35, 0.16, INK, 7).set_z_index(7))
    self.add(ex)
    return w, ex


class B15_Draft(Scene):
    def construct(self):
        w, ex = b14_end(self)
        self.play(FadeOut(ex), run_time=0.45)
        until(self, "In the repo's own words", lead=0.4)
        op = big_page(OUT_C, 1.6, 2.4, n=5, band=True)
        self.play(FadeIn(op, shift=UP * 0.3), run_time=0.45)
        until(self, "a draft for attorney review", lead=0.3)
        l1 = T("draft for attorney review", 34).next_to(P(-4.05, -1.0), RIGHT, buff=0.0)
        self.play(FadeIn(l1), run_time=0.35)
        until(self, "research notes", lead=0.3)
        l2 = T("not legal advice", 34).next_to(P(-4.05, -1.8), RIGHT, buff=0.0)
        self.play(FadeIn(l2), run_time=0.35)
        until(self, "The skill sorts", lead=0.3)
        lits = VGroup(*[bin_lamp(i, TERRA) for i in range(3)])
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in lits], lag_ratio=0.3), run_time=0.6)
        until(self, "A lawyer decides", lead=0.2)
        at = attorney(0.0)
        self.play(FadeIn(at, shift=UP * 0.3), run_time=0.45)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Belt, B01_Chutes, B02_NoDefaults, B03_Interview, B04_Delta, B05_Profile, B06_Sides, B07_Scope,
             B08_Checks, B09_Green, B10_Yellow, B11_Silent, B12_Red, B13_Lock, B14_Gate, B15_Draft):
    _cls.play = ST.play
