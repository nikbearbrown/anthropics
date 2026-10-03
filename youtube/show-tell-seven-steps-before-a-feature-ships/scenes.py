"""
Manim scenes for show-tell-seven-steps-before-a-feature-ships (show-tell skill, card #19, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The feature-dev plugin, from anthropics/claude-plugins-official/plugins/feature-dev/ (README, the /feature-dev
command file and the three agent files; identical to the raw live files on GitHub, 2026-09-27): a CORRIDOR of
seven open kraft rooms, numbered, with terracotta stop lamps where Claude waits for you; the feature TICKET (a
white slip with a terracotta dot); the kraft CLAUDE box (dark slot, dark mouth, terracotta spark); YOU (a kraft
terminal) and your signal BOARD (grey lamp = Claude is waiting, terracotta = you said go); AGENTS drawn as small
copies of the Claude box (explorers, architects, reviewers); FILES as white cards with grey lines; QUESTIONS as
white cards with kraft number seals and your kraft ANSWER cards with the same seals; three kraft BLUEPRINT sheets;
the FEATURE as a kraft box that closes under terracotta tape; a TO-DO card and a SUMMARY card with ink checks.
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







# ═════════════════════════════ the film: seven steps before a feature ships ═════════════════════════════
# Cast: a CORRIDOR of seven open kraft rooms with ink numerals and terracotta stop lamps; the feature TICKET
# (a white slip with a terracotta dot); the kraft CLAUDE box (dark slot on top, dark mouth on its left face,
# terracotta spark); YOU, a kraft terminal, and your dark signal BOARD (grey lamp = Claude waits, terracotta =
# you said go); AGENTS as small copies of the Claude box; white FILE cards; white QUESTION cards and kraft ANSWER
# cards with matching number seals; kraft BLUEPRINT sheets; the FEATURE box (open, then taped shut); a TO-DO card
# and a SUMMARY card with ink checks; FINDING slips with grey score bars.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SEAL = BOX_L


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


def seal(k, c):
    c = P3(c)
    return VGroup(RoundedRectangle(width=0.62, height=0.5, corner_radius=0.16, fill_color=SEAL, fill_opacity=1, stroke_width=0).move_to(c),
                  T(str(k), 38, INK, bold=True).move_to(c)).set_z_index(6)


# ─── cards: files, questions (white), answers (kraft) ───
EW, ED = 1.4, 0.95


def card(cx, cy, k=None, s=0.8, kraft=False, z=0):
    iso = rig_at(cx, cy, s, EW, ED)
    faces = (BOX_TOP, BOX_L, BOX_R) if kraft else (PAGE_TOP, PAGE_L, PAGE_R)
    slab = iso.box(0, 0, 0, EW, ED, 0.08, *faces, sw=4)
    zt = 0.08
    bars = VGroup(iso.quad([(0.2, 0.62, zt), (1.2, 0.62, zt), (1.2, 0.74, zt), (0.2, 0.74, zt)], BAR2, sw=0),
                  iso.quad([(0.2, 0.36, zt), (0.9, 0.36, zt), (0.9, 0.48, zt), (0.2, 0.48, zt)], BAR2, sw=0))
    g = VGroup(slab, bars)
    if k is not None:
        g.add(seal(k, iso.p(1.05, 0.3, zt) + LEFT * 0.05))
    if z:
        g.set_z_index(z)
    return g


# ─── the feature TICKET ───
def ticket(c, s=1.0):
    c = P3(c)
    body = RoundedRectangle(width=1.2, height=0.72, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.12, 0.12, 0], [0.42, 0.12, 0], color=BAR1, stroke_width=7),
                Line([-0.12, -0.12, 0], [0.24, -0.12, 0], color=BAR1, stroke_width=7))
    dot = Dot([-0.34, 0, 0], radius=0.1, color=TERRA)
    return VGroup(body, ln, dot).scale(s).move_to(c).set_z_index(10)


def slip(s=1.0):
    body = RoundedRectangle(width=0.8, height=0.52, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.24, 0.07, 0], [0.26, 0.07, 0], color=BAR1, stroke_width=6),
                Line([-0.24, -0.09, 0], [0.12, -0.09, 0], color=BAR1, stroke_width=6))
    return VGroup(body, ln).scale(s).set_z_index(10)


# ─── the CLAUDE box (agents are small copies) ───
CW, CD, CH = 2.4, 2.0, 1.6


class CBox:
    def __init__(self, cx, cy, s):
        self.iso = rig_at(cx, cy, s, CW, CD)
        self.cx, self.cy, self.s = cx, cy, s

    def mob(self):
        i = self.iso
        body = i.box(0, 0, 0, CW, CD, CH)
        slot = i.quad([(0.5, 0.82, CH), (1.9, 0.82, CH), (1.9, 1.18, CH), (0.5, 1.18, CH)], DARK_TOP, sw=0)
        mouth = i.quad([(0, 0.45, 0.12), (0, 1.55, 0.12), (0, 1.55, 0.72), (0, 0.45, 0.72)], DARK_L, sw=0)
        spark = Dot(i.p(CW * 0.55, 0, CH * 0.6), radius=0.15 * self.s / 0.8, color=TERRA)
        return VGroup(body, slot, mouth, spark)

    def slot(self):
        return self.iso.p(1.2, 1.0, CH)

    def mouth(self):
        return self.iso.p(0, 1.0, 0.42)


def box_to(mob, A, B):
    """Animate a box built on CBox A to CBox B (linear projection: scale + shift)."""
    return mob.animate.scale(B.s / A.s, about_point=A.iso.p(0, 0, 0)).shift(B.iso.p(0, 0, 0) - A.iso.p(0, 0, 0))


AS = 0.26                                    # agent scale


def agent(c):
    return CBox(c[0], c[1], AS).mob()


def agents_out(pts, mouth):
    """three agents, and the small copies at Claude's mouth they grow from."""
    ags = [agent(p) for p in pts]
    srcs = [a.copy().scale(0.3).move_to(mouth) for a in ags]
    return ags, srcs


# ─── YOU: a kraft terminal; your signal BOARD ───
TW, TD, TH = 1.3, 1.1, 1.0


def terminal(cx, cy, s=0.9):
    i = rig_at(cx, cy, s, TW, TD)
    body = i.box(0, 0, 0, TW, TD, TH)
    scr = i.quad([(0, 0.15, 0.22), (0, 0.95, 0.22), (0, 0.95, 0.86), (0, 0.15, 0.86)], DARK_TOP, sw=0)
    cur = Dot(i.p(0, 0.35, 0.42), radius=0.07, color=TERRA)
    return VGroup(body, scr, cur), i.p(0, 0.55, TH)


BDW, BDD, BDH = 0.3, 1.4, 1.45


def board(c, on=False):
    i = rig_at(c[0], c[1], 0.8, BDW, BDD)
    b = i.box(0, 0, 0, BDW, BDD, BDH, DARK_TOP, DARK_L, DARK_R)
    lamp = Circle(radius=0.19, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=GHOST, stroke_width=2).move_to(i.p(0, BDD / 2, BDH * 0.55))
    return VGroup(b, lamp)


def cross(x, y, s=0.22, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w))


# ─── the CORRIDOR: one long open kraft box along the iso x axis, six partition walls, seven rooms ───
LR, NR, CDP, CHT = 1.4, 7, 1.6, 0.7
LC = LR * NR
STOPS = (0, 2, 3, 4, 5)                       # phases 1, 3, 4, 5, 6 stop and wait for you (command file)


def corridor(cx, cy, s):
    iso = rig_at(cx, cy, s, LC, CDP)
    back, front = iso.open_box(0, 0, 0, LC, CDP, CHT)
    parts = VGroup(*[iso.quad([(LR * k, 0, 0), (LR * k, CDP, 0), (LR * k, CDP, CHT), (LR * k, 0, CHT)], BOX_IN1)
                     for k in range(NR - 1, 0, -1)]).set_z_index(1)
    nums = VGroup(*[T(str(k + 1), 40, INK, bold=True).move_to(iso.p(LR * k + LR / 2, -0.62, 0)) for k in range(NR)])
    return VGroup(back, parts, front), nums, iso


def room_pt(iso, k, z=0.0):
    return iso.p(LR * k + LR / 2, CDP / 2, z)


def stop_lamps(iso, on=True):
    return VGroup(*[Circle(radius=0.18, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2)
                    .move_to(iso.p(LR * k + LR / 2, CDP + 0.05, CHT + 0.5)) for k in STOPS])


# ─── BLUEPRINT sheets ───
SW_, SD_ = 2.0, 1.4
KINDS = ("minimal", "clean", "pragmatic")


def sheet(cx, cy, kind, s=0.75):
    i = rig_at(cx, cy, s, SW_, SD_)
    slab = i.box(0, 0, 0, SW_, SD_, 0.08, BOX_TOP, BOX_L, BOX_R, sw=4)
    z = 0.08
    blocks = {"minimal": [(0.25, 0.25, 0.9, 0.55)],
              "clean": [(0.2, 0.2, 0.9, 0.62), (1.1, 0.2, 1.8, 0.62), (0.2, 0.78, 0.9, 1.2), (1.1, 0.78, 1.8, 1.2)],
              "pragmatic": [(0.2, 0.2, 0.95, 1.2), (1.15, 0.2, 1.8, 0.62)]}[kind]
    bl = VGroup(*[i.quad([(a, b, z), (c, b, z), (c, d, z), (a, d, z)], (BAR1, BAR2)[n % 2], sw=0) for n, (a, b, c, d) in enumerate(blocks)])
    return VGroup(slab, bl), i.p(1.5, 1.0, z)


# ─── the FEATURE box ───
FW, FD, FH = 2.4, 2.0, 1.3


def feature_open(iso):
    return iso.open_box(0, 0, 0, FW, FD, FH)


def feature_closed(iso):
    body = iso.box(0, 0, 0, FW, FD, FH)
    tp = iso.tape(0, 0, FH, FW, FD, drop=0.4)
    return VGroup(body, tp)


def lid_and_tape(iso):
    lid = iso.quad([(0, 0, FH), (FW, 0, FH), (FW, FD, FH), (0, FD, FH)], BOX_TOP).set_z_index(3)
    tp = iso.tape(0, 0, FH, FW, FD, drop=0.4).set_z_index(4)
    return lid, tp


# ─── TO-DO and SUMMARY cards (grey outline: ink checks sit inside) ───
def listcard(c, w, h, n, lw):
    c = P3(c)
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=5).move_to(c)
    step = h / (n + 1)
    ys = [c[1] + h / 2 - step * (k + 1) for k in range(n)]
    x0 = c[0] - w / 2 + 0.75
    lines = VGroup(*[Line([x0, y, 0], [x0 + lw * (1.0 if k % 2 == 0 else 0.72), y, 0], color=BAR2, stroke_width=10) for k, y in enumerate(ys)])
    ticks = [(c[0] - w / 2 + 0.38, y + 0.02) for y in ys]
    return VGroup(body, lines), ticks


def todo(c, done_n=0):
    g, ticks = listcard(c, 1.8, 2.1, 4, 0.8)
    ck = VGroup(*[check(x, y, 0.17) for (x, y) in ticks[:done_n]])
    return VGroup(g, ck), ticks


def finding(c, score):
    c = P3(c)
    body = RoundedRectangle(width=2.3, height=0.5, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    bar = Rectangle(width=1.9 * score, height=0.16, fill_color=BAR1, fill_opacity=1, stroke_width=0)
    bar.move_to([c[0] - 0.95 + 0.95 * score, c[1], 0])
    return VGroup(body, bar)


# ══════════════ B00: seven rooms, in order ══════════════
C0 = (0.0, 0.0, 0.72)
TK0 = (-5.2, -1.2)
HOP_Z = CHT + 0.55


def l_fd():
    return lbl("/feature-dev", (-4.7, -2.3))


def l_wait():
    return lbl("waits for you", (-3.1, 1.6))


def b00_state():
    cor, nums, iso = corridor(*C0)
    return VGroup(cor, nums, stop_lamps(iso), ticket(room_pt(iso, 6, HOP_Z), 0.8), l_fd(), l_wait())


class B00_Corridor(Scene):
    def construct(self):
        tk = ticket(TK0, 0.8)
        self.add(tk)
        cor, nums, iso = corridor(*C0)
        self.play(FadeIn(l_fd()), FadeIn(cor[0]), FadeIn(cor[2]), run_time=0.5)
        until(self, "The command walks it", lead=0.3)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[GrowFromEdge(w, DOWN) for w in reversed(cor[1])], lag_ratio=0.15), run_time=rt)
        until(self, "seven phases", lead=0.3)
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in nums], lag_ratio=0.12), run_time=rt)
        until(self, "in order", lead=0.3)
        rt = guard(self, 1.6)
        pts = [room_pt(iso, k, HOP_Z) for k in range(NR)]
        self.play(MoveAlongPath(tk, ArcBetweenPoints(P3(TK0), pts[0], angle=-0.5)), run_time=rt * 0.22)
        for a_, b_ in zip(pts[:-1], pts[1:]):
            self.play(MoveAlongPath(tk, ArcBetweenPoints(a_, b_, angle=-1.4)), run_time=rt * 0.13)
        until(self, "several of them stop", lead=0.3)
        lm = stop_lamps(iso, on=False)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[GrowFromCenter(l) for l in lm], lag_ratio=0.15), FadeIn(l_wait()), run_time=rt)
        rt = guard(self, 0.35)
        self.play(*[l.animate.set_fill(TERRA) for l in lm], run_time=rt)
        done(self)


# ══════════════ B01: discovery ══════════════
BX1 = CBox(3.5, -1.2, 0.9)
TERM1 = (-4.7, -1.3)
BD1 = (-2.75, -1.4)
TK1 = (1.1, 2.25)
QS1 = [(-0.95, 1.15), (-0.95, 0.3), (-0.95, -0.55)]
SUM1 = (0.6, -1.95)


def l_claude(c=(3.5, 1.65)):
    return lbl("Claude", c)


def l_you(c=(-4.7, 0.55)):
    return lbl("you", c)


def l_disc():
    return lbl("discovery", (-1.3, 2.9))


def summary_card(c):
    g, _ = listcard(c, 1.8, 1.1, 2, 0.8)
    return g


def b01_state():
    term, _ = terminal(*TERM1)
    return VGroup(BX1.mob(), l_claude(), term, l_you(), board(BD1, on=True),
                  VGroup(*[slip(1.2).move_to(P3(q)) for q in QS1]), summary_card(SUM1), check(-0.8, -1.9, 0.22), l_disc())


class B01_Discover(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        tk = st[3]
        self.play(FadeOut(VGroup(st[0], st[1], st[2], st[4], st[5])), run_time=0.4)
        box = BX1.mob()
        term, _ = terminal(*TERM1)
        bd = board(BD1)
        rt = guard(self, 0.7)
        self.play(tk.animate.move_to(P3(TK1)), FadeIn(box, shift=DOWN * 0.4), FadeIn(term, shift=DOWN * 0.4), FadeIn(bd, shift=DOWN * 0.4),
                  FadeIn(l_claude()), FadeIn(l_you()), FadeIn(l_disc()), run_time=rt)
        until(self, "If the request is unclear", lead=0.3)
        rt = guard(self, 0.9)
        self.play(MoveAlongPath(tk, ArcBetweenPoints(P3(TK1), BX1.slot() + UP * 0.6, angle=-0.6)), run_time=rt * 0.7)
        self.play(tk.animate.scale(0.25).move_to(BX1.slot()), run_time=rt * 0.3, rate_func=ease_in)
        self.remove(tk)
        for q, phrase in zip(QS1, ("what problem it solves", "what it should do", "any constraints")):
            until(self, phrase, lead=0.2)
            s_ = slip(1.2).move_to(P3(q))
            s0 = s_.copy().scale(0.3).move_to(BX1.mouth())
            rt = guard(self, 0.55)
            self.play(Transform(s0, s_), run_time=rt)
        until(self, "sums up what it understood", lead=0.3)
        sm = summary_card(SUM1)
        s0 = sm.copy().scale(0.3).move_to(BX1.mouth())
        rt = guard(self, 0.6)
        self.play(Transform(s0, sm), run_time=rt)
        until(self, "checks with you", lead=0.3)
        rt = guard(self, 0.6)
        self.play(bd[1].animate.set_fill(TERRA), Create(check(-0.8, -1.9, 0.22)), run_time=rt)
        done(self)


# ══════════════ B02: exploration ══════════════
BX2 = CBox(-4.7, -0.4, 0.7)
GX = [1.7, 3.45, 5.2]
GY = [1.4, 0.0, -1.4]
AGX = -1.0
KF = [(-2.35, -2.25 + 0.2 * k) for k in range(3)]


def grid():
    return VGroup(*[VGroup(*[card(x, y, s=0.7, z=0) for x in GX]) for y in GY])


def l_code():
    return lbl("codebase", (3.45, 2.55))


def l_expl():
    return lbl("code-explorer", (-1.0, 2.55))


def l_kf():
    return lbl("key files", (-2.35, -3.0))


def b02_state():
    return VGroup(BX2.mob(), l_claude((-4.7, 1.9)), grid(), l_code())


class B02_Explore(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        box, lc = st[0], st[1]
        self.play(FadeOut(VGroup(*[st[i] for i in range(2, 9)])), run_time=0.4)
        g = grid()
        rt = guard(self, 0.8)
        self.play(box_to(box, BX1, BX2), lc.animate.move_to([-4.7, 1.9, 0]),
                  LaggedStart(*[FadeIn(c, shift=DOWN * 0.3) for row in g for c in row], lag_ratio=0.08), FadeIn(l_code()), run_time=rt)
        until(self, "code explorer agents", lead=0.3)
        ags, srcs = agents_out([(AGX, y) for y in GY], BX2.mouth())
        rt = guard(self, 0.8)
        le, lk = l_expl(), l_kf()
        self.play(*[Transform(s_, a) for s_, a in zip(srcs, ags)], FadeIn(le), run_time=rt)
        until(self, "each tracing a different part", lead=0.2)
        beams = VGroup(*[Line([AGX + 0.62, y + 0.05, 0], [6.05, y + 0.05, 0], color=TERRA, stroke_width=7).set_z_index(8) for y in GY])
        rt = guard(self, 1.3)
        self.play(LaggedStart(*[Create(b) for b in beams], lag_ratio=0.25), run_time=rt * 0.65)
        self.play(FadeOut(beams), run_time=rt * 0.35)
        until(self, "Each brings back", lead=0.3)
        picks = [g[k][1].copy().set_z_index(9) for k in range(3)]
        rt = guard(self, 0.6)
        self.play(*[p.animate.scale(0.9).move_to([AGX + 0.2, GY[k] - 0.35, 0]) for k, p in enumerate(picks)], run_time=rt)
        until(self, "five to ten key files", lead=0.4)
        rt = guard(self, 1.0)
        self.play(*[p.animate.move_to(P3(KF[k])) for k, p in enumerate(picks)],
                  *[s_.animate.scale(0.3).move_to(BX2.mouth()) for s_ in srcs], FadeOut(le), FadeIn(lk), run_time=rt)
        self.remove(*srcs)
        until(self, "Claude reads them all", lead=0.2)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[p.animate.scale(0.25).move_to(BX2.slot()) for p in reversed(picks)], lag_ratio=0.3), FadeOut(lk), run_time=rt)
        self.remove(*picks)
        rt = guard(self, 0.4)
        self.play(Indicate(box[3], color=None, scale_factor=1.6), run_time=rt)
        done(self)


# ══════════════ B03: clarifying questions ══════════════
BX3 = CBox(-4.95, 0.85, 0.5)
TERM3 = (-4.95, -1.8)
BD3 = (-3.25, -1.9)
XS3 = [-1.45, 0.6, 2.65, 4.7]
QY, AY = 1.45, -1.4


def l_q():
    return lbl("questions", (1.6, 2.65))


def l_ans():
    return lbl("your answers", (1.6, -2.75))


def b03_state():
    term, _ = terminal(*TERM3, s=0.8)
    return VGroup(BX3.mob(), l_claude((-4.95, 2.6)), term, board(BD3, on=True),
                  VGroup(*[card(x, QY, k + 1, s=0.85) for k, x in enumerate(XS3)]),
                  VGroup(*[card(x, AY, k + 1, s=0.85, kraft=True) for k, x in enumerate(XS3)]), l_q(), l_ans())


class B03_Questions(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        box, lc = st[0], st[1]
        self.play(FadeOut(VGroup(st[2], st[3])), run_time=0.35)
        term, tport = terminal(*TERM3, s=0.8)
        bd = board(BD3)
        rt = guard(self, 0.6)
        self.play(box_to(box, BX2, BX3), lc.animate.move_to([-4.95, 2.6, 0]), FadeIn(term, shift=DOWN * 0.4), FadeIn(bd, shift=DOWN * 0.4), run_time=rt)
        until(self, "clarifying questions", lead=0.2)
        qs = [card(x, QY, k + 1, s=0.85) for k, x in enumerate(XS3)]
        srcs = [q.copy().scale(0.3).move_to(BX3.mouth()) for q in qs]
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[Transform(s_, q) for s_, q in zip(srcs, qs)], lag_ratio=0.25), FadeIn(l_q()), run_time=rt)
        until(self, "do not skip", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*srcs), color=None, scale_factor=1.06), run_time=rt)
        until(self, "edge cases", lead=0.2)
        rt = guard(self, 0.45)
        self.play(Indicate(srcs[0], color=None, scale_factor=1.12), run_time=rt)
        until(self, "error handling", lead=0.2)
        rt = guard(self, 0.45)
        self.play(Indicate(srcs[1], color=None, scale_factor=1.12), run_time=rt)
        until(self, "waits for your answers", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(bd[1], color=None, scale_factor=1.5), run_time=rt)
        an = [card(x, AY, k + 1, s=0.85, kraft=True) for k, x in enumerate(XS3)]
        a0 = [a.copy().scale(0.3).move_to(tport) for a in an]
        rt = guard(self, 1.1)
        self.play(LaggedStart(*[Transform(s_, a) for s_, a in zip(a0, an)], lag_ratio=0.2), FadeIn(l_ans()), run_time=rt)
        until(self, "before designing anything", lead=0.2)
        rt = guard(self, 0.4)
        self.play(bd[1].animate.set_fill(TERRA), run_time=rt)
        done(self)


# ══════════════ B04: architecture ══════════════
BX4 = CBox(-5.2, -1.75, 0.45)
AX = [-2.0, 1.1, 4.2]
ARY = 2.05
SHY = 0.1
PICK = 2


def l_kind(k):
    return lbl(KINDS[k], (AX[k], -1.05))


def b04_state():
    sh, dp = sheet(AX[PICK], SHY + 0.3, KINDS[PICK])
    return VGroup(BX4.mob(), sh, Dot(dp, radius=0.13, color=TERRA).set_z_index(5), l_kind(PICK))


class B04_Design(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        box = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 8)])), run_time=0.4)
        rt = guard(self, 0.6)
        self.play(box_to(box, BX3, BX4), run_time=rt)
        until(self, "code architect agents", lead=0.3)
        ags, srcs = agents_out([(x, ARY) for x in AX], BX4.mouth())
        rt = guard(self, 0.8)
        self.play(*[Transform(s_, a) for s_, a in zip(srcs, ags)], run_time=rt)
        until(self, "each draw one blueprint", lead=0.3)
        sheets, dps = zip(*[sheet(x, SHY, k) for x, k in zip(AX, KINDS)])
        labels = [l_kind(k) for k in range(3)]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(VGroup(s_, l_), shift=DOWN * 0.5) for s_, l_ in zip(sheets, labels)], lag_ratio=0.3), run_time=rt)
        for k, phrase in enumerate(("minimal changes", "clean architecture", "pragmatic balance")):
            until(self, phrase, lead=0.1)
            rt = guard(self, 0.4)
            self.play(Indicate(sheets[k], color=None, scale_factor=1.06), run_time=rt)
        until(self, "Claude recommends one", lead=0.2)
        dot = Dot(dps[PICK], radius=0.13, color=TERRA).set_z_index(5)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(dot), Indicate(box[3], color=None, scale_factor=1.6), run_time=rt)
        until(self, "asks which you prefer", lead=0.3)
        cur = cursor(5.6, -2.4)
        self.add(cur)
        rt = guard(self, 0.45)
        self.play(cur.animate.move_to([AX[PICK] + 0.35, SHY - 0.2, 0]), run_time=rt)
        rt = guard(self, 0.25)
        self.play(Indicate(cur, color=None, scale_factor=0.8), run_time=rt)
        others = VGroup(*[VGroup(sheets[k], labels[k]) for k in range(3) if k != PICK])
        rt = guard(self, 0.6)
        self.play(VGroup(sheets[PICK], dot).animate.shift(UP * 0.3), FadeOut(others), FadeOut(VGroup(*srcs)), FadeOut(cur), run_time=0.45)
        done(self)


# ══════════════ B05: the build ══════════════
BX5 = CBox(-4.6, -1.5, 0.55)
SH5 = (-4.25, 1.75)
BD5 = (-1.8, 1.25)
FB5 = rig_at(1.3, -1.2, 0.85, FW, FD)
TD5 = (4.9, 0.45)


def l_go():
    return lbl("your go", (-1.8, 0.45))


def l_todo(c=(4.9, -1.1)):
    return lbl("to-dos", c)


def sheet5():
    sh, dp = sheet(0, 0, KINDS[PICK], s=0.6)
    g = VGroup(sh, Dot(dp, radius=0.11, color=TERRA).set_z_index(5))
    return g.move_to(P3(SH5))


def b05_state():
    return VGroup(BX5.mob(), sheet5(), board(BD5, on=True), l_go(), feature_closed(FB5), todo(TD5, 3)[0], l_todo())


class B05_Build(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        box = st[0]
        pick = VGroup(st[1], st[2])
        bd = board(BD5)
        target = sheet5()
        rt = guard(self, 0.7)
        self.play(box_to(box, BX4, BX5), pick.animate.scale(0.8).move_to(target.get_center()), FadeOut(st[3]),
                  FadeIn(bd, shift=DOWN * 0.4), run_time=rt)
        until(self, "until you approve", lead=0.2)
        back, front = feature_open(FB5)
        td, ticks = todo(TD5, 0)
        rt = guard(self, 0.7)
        self.play(bd[1].animate.set_fill(TERRA), FadeIn(l_go()), FadeIn(VGroup(back, front), shift=DOWN * 0.4),
                  FadeIn(td, shift=DOWN * 0.3), FadeIn(l_todo()), run_time=rt)
        for k, phrase in enumerate(("follows the blueprint", "sticks to the codebase", "ticks off its to-do list")):
            until(self, phrase, lead=0.2)
            cd = card(0, 0, s=0.55, z=1)
            dest = FB5.p(1.2, 1.0, 0.12 + 0.18 * k)
            cd.move_to(dest + UP * 2.6)
            self.add(cd)
            rt = guard(self, 0.7)
            self.play(cd.animate.move_to(dest), run_time=rt * 0.6, rate_func=ease_in)
            self.play(Create(check(*ticks[k], 0.17)), run_time=rt * 0.4)
        until(self, "as it goes", lead=0.3)
        lid, tp = lid_and_tape(FB5)
        rt = guard(self, 0.6)
        self.play(FadeIn(lid, shift=DOWN * 0.3), run_time=rt * 0.5)
        self.play(FadeIn(tp), run_time=rt * 0.5)
        done(self)


# ══════════════ B06: quality review ══════════════
FB6 = rig_at(-0.6, -1.3, 0.85, FW, FD)
BD6 = (-4.9, -1.2)
RX = [-3.0, -0.6, 1.8]
RY = 1.85
FX = 4.45
FY = [1.5, 0.7, -0.1, -0.9, -1.7]
SCORES = [0.92, 0.45, 0.85, 0.6, 0.3]
KEEP = [0, 2]


def l_rev():
    return lbl("code-reviewer", (-0.6, 2.9))


def l_80():
    return lbl("≥ 80", (FX, 2.35))


def b06_state():
    return VGroup(feature_closed(FB6), VGroup(*[agent((x, RY)) for x in RX]), l_rev(), board(BD6, on=True),
                  finding((FX, FY[1]), SCORES[KEEP[1]]), l_80())


class B06_Review(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        fb, bd = st[4], st[2]
        self.play(FadeOut(VGroup(st[0], st[1], st[3], st[5], st[6])), run_time=0.4)
        rt = guard(self, 0.7)
        self.play(fb.animate.shift(FB6.p(0, 0, 0) - FB5.p(0, 0, 0)), bd.animate.move_to(np.array(board(BD6).get_center())), run_time=rt)
        bd[1].set_fill(GHOST)
        until(self, "Three code reviewer agents", lead=0.3)
        ags = [agent((x, RY)) for x in RX]
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(a, shift=DOWN * 0.4) for a in ags], lag_ratio=0.2), FadeIn(l_rev()), run_time=rt)
        until(self, "check the new code", lead=0.2)
        top, bot = FB6.p(FW, FD, FH)[1] + 0.1, FB6.p(0, 0, 0)[1] - 0.1
        scan = Line([-2.5, top, 0], [1.3, top, 0], color=TERRA, stroke_width=8).set_z_index(8)
        rt = guard(self, 1.3)
        self.play(FadeIn(scan), run_time=rt * 0.15)
        self.play(scan.animate.move_to([-0.6, bot, 0]), run_time=rt * 0.7)
        self.play(FadeOut(scan), run_time=rt * 0.15)
        for k, phrase in enumerate(("for simplicity", "for bugs", "project's conventions")):
            until(self, phrase, lead=0.1)
            rt = guard(self, 0.4)
            self.play(Indicate(ags[k], color=None, scale_factor=1.12), run_time=rt)
        until(self, "Each rates its confidence", lead=0.3)
        fds = [finding((FX, y), s) for y, s in zip(FY, SCORES)]
        bodies = [f[0] for f in fds]
        srcs = [b.copy().scale(0.3).move_to(FB6.p(FW, 0, FH * 0.5)) for b in bodies]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Transform(s_, b) for s_, b in zip(srcs, bodies)], lag_ratio=0.2), run_time=rt)
        until(self, "from zero to a hundred", lead=0.2)
        bars = [f[1] for f in fds]
        rt = guard(self, 0.8)
        self.play(*[GrowFromEdge(b, LEFT) for b in bars], run_time=rt)
        rows = [VGroup(s_, b) for s_, b in zip(srcs, bars)]
        until(self, "eighty or above", lead=0.3)
        drop = VGroup(*[rows[k] for k in range(5) if k not in KEEP])
        rt = guard(self, 0.9)
        self.play(FadeOut(drop), rows[KEEP[0]].animate.move_to([FX, FY[0], 0]), rows[KEEP[1]].animate.move_to([FX, FY[1], 0]),
                  FadeIn(l_80()), run_time=rt)
        until(self, "Then you choose", lead=0.2)
        rt = guard(self, 0.4)
        self.play(Indicate(bd[1], color=None, scale_factor=1.5), run_time=rt)
        until(self, "fix now", lead=0.1)
        rt = guard(self, 0.8)
        self.play(rows[KEEP[0]].animate.scale(0.25).move_to(FB6.p(FW * 0.6, FD * 0.5, FH)), bd[1].animate.set_fill(TERRA), run_time=rt)
        self.remove(rows[KEEP[0]])
        until(self, "proceed as is", lead=0.1)
        rt = guard(self, 0.4)
        self.play(Indicate(fb, color=None, scale_factor=1.04), run_time=rt)
        done(self)


# ══════════════ B07: the summary ══════════════
FB7 = rig_at(-3.9, -1.35, 0.85, FW, FD)
TD7 = (-3.9, 2.0)
SUM7 = (2.5, -0.1)


def l_todo7():
    return lbl("to-dos", (-1.95, 2.0))


def l_sum():
    return lbl("summary", (2.5, 2.35))


def sumcard():
    return listcard(SUM7, 4.4, 3.4, 4, 2.6)


def b07_state():
    g, ticks = sumcard()
    return VGroup(feature_closed(FB7), todo(TD7, 4)[0], l_todo7(), g, VGroup(*[check(x, y, 0.2) for (x, y) in ticks]), l_sum())


class B07_Summary(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        fb = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 6)])), run_time=0.4)
        td, tt = todo(TD7, 3)
        rt = guard(self, 0.6)
        self.play(fb.animate.shift(FB7.p(0, 0, 0) - FB6.p(0, 0, 0)), FadeIn(td, shift=DOWN * 0.3), FadeIn(l_todo7()), run_time=rt)
        until(self, "marks every to-do done", lead=0.2)
        rt = guard(self, 0.4)
        self.play(Create(check(*tt[3], 0.17)), run_time=rt)
        until(self, "writes up", lead=0.3)
        g, ticks = sumcard()
        rt = guard(self, 0.6)
        self.play(FadeIn(g, shift=LEFT * 0.6), FadeIn(l_sum()), run_time=rt)
        for k, phrase in enumerate(("what was built", "the key decisions", "the files it changed", "suggested next steps")):
            until(self, phrase, lead=0.1)
            rt = guard(self, 0.35)
            self.play(Create(check(*ticks[k], 0.2)), run_time=rt)
        done(self)


# ══════════════ B08: when to use it ══════════════
C8 = (0.9, 0.5, 0.62)
BUN = (-4.8, -0.8)
FIX = (-4.8, -2.5)


def bundle(c, s=0.6):
    c = P3(c)
    g = VGroup(*[card(c[0], c[1] - 0.15 + 0.2 * k, s=s) for k in range(3)])
    for k in range(2):
        for f in g[k][0]:
            f.set_stroke(DEV_EDGE, 2)
    g.add(ticket(c + UP * 0.55 + RIGHT * 0.25, s=0.75))
    return g


def l_several():
    return lbl("several files", (-4.8, 0.45))


def l_fix():
    return lbl("one-line fix", (-4.8, -1.75))


class B08_When(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        cor, nums, iso = corridor(*C8)
        lm = stop_lamps(iso)
        bun = bundle(BUN)
        ls = l_several()
        rt = guard(self, 0.8)
        self.play(FadeIn(VGroup(cor, nums), shift=DOWN * 0.3), FadeIn(lm), FadeIn(bun, shift=UP * 0.3), FadeIn(ls), run_time=rt)
        until(self, "touch several files", lead=0.3)
        dest = room_pt(iso, 0, 0.25)
        rt = guard(self, 1.0)
        self.play(MoveAlongPath(bun, ArcBetweenPoints(P3(BUN), dest + UP * 0.9, angle=-0.6)), run_time=rt * 0.6)
        self.play(bun.animate.scale(0.6).move_to(dest), run_time=rt * 0.4, rate_func=ease_in)
        until(self, "architecture decision", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(nums[3], color=None, scale_factor=1.3), run_time=rt)
        until(self, "Not for one-line", lead=0.3)
        fx = slip(1.1).move_to(P3(FIX))
        rt = guard(self, 0.4)
        self.play(FadeIn(fx, shift=RIGHT * 0.3), FadeOut(ls), FadeIn(l_fix()), run_time=rt)
        rt = guard(self, 1.6)
        self.play(fx.animate.move_to([5.4, FIX[1], 0]), run_time=rt, rate_func=linear)
        until(self, "urgent hotfixes", lead=0.2)
        rt = guard(self, 0.4)
        self.play(Indicate(fx, color=None, scale_factor=1.15), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Corridor, B01_Discover, B02_Explore, B03_Questions, B04_Design, B05_Build, B06_Review, B07_Summary, B08_When):
    _cls.play = ST.play
