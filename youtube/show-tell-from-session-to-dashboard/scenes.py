"""
Manim scenes for show-tell-from-session-to-dashboard (show-tell skill, card #28, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

The pipeline exactly as anthropics/claude-code-monitoring-guide builds it, checked against the live Claude Code
monitoring docs (code.claude.com/docs/en/monitoring-usage.md, sources/): THE TERMINAL (kraft block, extra-dark screen,
terracotta cursor, a lamp that lights when CLAUDE_CODE_ENABLE_TELEMETRY=1 is set) drips METRIC DROPS (grey beads) down
THE PIPE (OTLP over gRPC to localhost:4317) into THE COLLECTOR (a kraft funnel on its side, on a dark base: receiver
4317 -> batch -> Prometheus exporter 8889), which PROMETHEUS (a tall kraft cabinet with three drawers) scrapes every
15 s and files as time series; PromQL sums claude_code_token_usage_tokens_total by type; GRAFANA (a white board)
draws the guide's dashboard; the claude -p report reads Prometheus totals plus the Linear MCP. Events (a second,
thinner pipe) stop at a cap: the guide's collector has a metrics pipeline only. Privacy (B08) as the docs state it.
No prices, no ROI dollar figures, no sample numbers.
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






# ═════════════════════════════ the film: from session to dashboard ═════════════════════════════
SHADOW = "#AFA28A"
# extra-dark faces for the screen, plinths and bases (darker than DARK_* so GATE T's ink tolerance never reads a
# big dark block as one ink "text" blob; the #20 builder's fix)
FB_TOP, FB_L, FB_R = "#161411", "#121010", "#0E0C0A"
EDGE_D = "#050404"                                           # edge colour for extra-dark blocks (not ink: GATE T)
TILE_TOP, TILE_L, TILE_R = "#D2BD98", "#B39A72", "#9C8462"    # deep kraft: tags, folder, strips


def dark(g):
    for f in g.family_members_with_points():
        f.set_stroke(EDGE_D, 3)
    return g


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


def IK(d):
    return Iso(d["ox"], d["oy"], d["k"])


def drop(at, r=0.16):
    return Circle(radius=r, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(P(*at[:2]))


PIPE_EDGE = TILE_R        # pipes are edged in deep kraft, not ink: an ink-edged pipe joins terminal, funnel and cabinet
                          # into one wide "text" blob under GATE T's overlap check (pre-check 2026-09-27)


def pipe(x0, x1, y, h=0.34, fill=BOX_L, sw=5):
    return Rectangle(width=x1 - x0, height=h, fill_color=fill, fill_opacity=1, stroke_color=PIPE_EDGE,
                     stroke_width=sw).move_to([(x0 + x1) / 2, y, 0]).set_z_index(-1)


def upright_page(bottom, w=0.95, h=1.2, n=4, indent=False):
    """A white page standing up: its bottom edge centred at `bottom`."""
    x, y = float(bottom[0]), float(bottom[1])
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y + h / 2, 0])
    step = 0.62 / max(n - 1, 1) if n > 1 else 0
    lines = VGroup()
    for i in range(n):
        a = x - w * 0.32 + (w * 0.12 if indent and i % 3 else 0)
        b = x + w * (0.32 - (0.2 if i % 2 else 0))
        lines.add(Line([a, y + h * (0.8 - step * i), 0], [b, y + h * (0.8 - step * i), 0], color=BAR2, stroke_width=7))
    return VGroup(body, lines)


# ─────────────── THE TERMINAL: kraft block, extra-dark screen, terracotta cursor, a lamp on its side ───────────────
def terminal(ox, oy, k, lit=False):
    """VGroup(shadow, body, screen, cursor, slot, lamp). The screen faces right-front; the lamp sits on the left face."""
    I = Iso(ox, oy, k)
    sh = I.quad([(-0.8, -0.95, 0), (1.1, -0.95, 0), (1.1, 0.6, 0), (-0.8, 0.6, 0)], SHADOW, sw=0).set_z_index(-2)
    body = I.box(-0.8, -0.6, 0, 1.6, 1.2, 1.3)
    screen = I.quad([(-0.62, -0.6, 0.28), (0.62, -0.6, 0.28), (0.62, -0.6, 1.08), (-0.62, -0.6, 1.08)], FB_TOP, stroke=EDGE_D, sw=3)
    cur = Dot(I.p(-0.4, -0.6, 0.48), radius=0.075 * k, color=TERRA)
    slot = I.quad([(-0.45, -0.02, 1.3), (0.45, -0.02, 1.3), (0.45, 0.16, 1.3), (-0.45, 0.16, 1.3)], DARK_R, sw=2)
    lamp = Dot(I.p(-0.8, 0.0, 0.95), radius=0.1 * k, color=TERRA if lit else BAR1)
    return VGroup(sh, body, screen, cur, slot, lamp)


def t_port(ox, oy, k):
    return Iso(ox, oy, k).p(0.8, -0.6, 0.65)


def t_lamp(ox, oy, k):
    return Dot(Iso(ox, oy, k).p(-0.8, 0.0, 0.95), radius=0.1 * k, color=TERRA)


# ─────────────── THE COLLECTOR: a kraft funnel lying on its side, on an extra-dark base ───────────────
def collector(xw, xn, y, hw, hn, k=1.0):
    """VGroup(base, post, funnel body, mouth rim). Wide end (left) at xw takes the pipe; narrow end at xn."""
    cx = (xw + xn) / 2
    body = Polygon([xw, y + hw / 2, 0], [xn, y + hn / 2, 0], [xn, y - hn / 2, 0], [xw, y - hw / 2, 0],
                   fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    rim = Ellipse(width=0.42 * hw / 1.4, height=hw, fill_color=BOX_IN2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([xw, y, 0])
    oy = y - hw / 2 - 0.95 * k
    B = Iso(cx, oy, 0.7 * k)
    base = dark(B.box(-0.6, -0.5, 0, 1.2, 1.0, 0.55, FB_TOP, FB_L, FB_R))
    ytop = oy + 0.385 * k
    ybot = y - (hw + hn) / 4 + 0.02
    post = Rectangle(width=0.2 * k, height=max(0.05, ybot - ytop), fill_color=BAR1, fill_opacity=1, stroke_color=INK,
                     stroke_width=3).move_to([cx, (ybot + ytop) / 2, 0]).set_z_index(-1)
    return VGroup(base, post, body, rim)


# ─────────────── PROMETHEUS: a tall kraft cabinet with three drawers on a dark plinth ───────────────
def cabinet(ox, oy, k):
    """VGroup(shadow, plinth, body, drawers, lamp dot)."""
    I = Iso(ox, oy, k)
    sh = I.quad([(-0.75, -0.95, 0), (1.0, -0.95, 0), (1.0, 0.65, 0), (-0.75, 0.65, 0)], SHADOW, sw=0).set_z_index(-2)
    plinth = dark(I.box(-0.75, -0.65, 0, 1.5, 1.3, 0.22, FB_TOP, FB_L, FB_R))
    body = I.box(-0.6, -0.5, 0.22, 1.2, 1.0, 2.8)
    drawers = VGroup(*[I.quad([(-0.45, -0.5, z0), (0.45, -0.5, z0), (0.45, -0.5, z0 + 0.62), (-0.45, -0.5, z0 + 0.62)],
                              BOX_TOP, stroke=BAR1, sw=3) for z0 in (0.45, 1.2, 1.95)])
    dot = Dot(I.p(0.3, -0.5, 2.26), radius=0.07 * k, color=TERRA)
    return VGroup(sh, plinth, body, drawers, dot)


def cab_left_x(ox, k):
    return Iso(ox, 0, k).p(-0.6, 0.0, 0)[0]


# ─────────────── THE DASHBOARD: a white board, grey header band, grey bars, one terracotta dot ───────────────
def board(cx, cy, w, h, k=1.0, bars=True, stand=True):
    """VGroup(stand, shadow, face, band, bars). Bars are drawn full; grow them with GrowFromEdge."""
    stand_g = VGroup()
    if stand:
        by = cy - h / 2
        B = Iso(cx, by - 1.05 * k, 0.7 * k)
        foot = dark(B.box(-0.5, -0.4, 0, 1.0, 0.8, 0.3, FB_TOP, FB_L, FB_R))
        post = Rectangle(width=0.18 * k, height=0.95 * k, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3
                         ).move_to([cx, by - 0.47 * k, 0]).set_z_index(-1)
        stand_g = VGroup(foot, post)
    shadow = Rectangle(width=w, height=h, fill_color=TILE_L, fill_opacity=1, stroke_width=0).move_to([cx + 0.13 * k, cy - 0.13 * k, 0])
    face = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    band = Rectangle(width=w - 0.08, height=0.24 * k, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([cx, cy + h / 2 - 0.16 * k, 0])
    bg = VGroup()
    if bars:
        base_y = cy - h / 2 + 0.25 * k
        for i, (hh, col) in enumerate([(0.5, BAR1), (0.95, BAR2), (0.7, BAR1)]):
            bg.add(Rectangle(width=0.36 * k, height=hh * k, fill_color=col, fill_opacity=1, stroke_width=0)
                   .move_to([cx - 0.62 * k + i * 0.62 * k, base_y + hh * k / 2, 0]))
        bg.add(Dot([cx, base_y + 0.95 * k + 0.16 * k, 0], radius=0.08 * k, color=TERRA))
    return VGroup(stand_g, shadow, face, band, bg)


# ─────────────── layouts ───────────────
TH = dict(ox=-4.9, oy=-1.2, k=0.85)                 # hero terminal
TB = dict(ox=-2.8, oy=-1.7, k=1.5)                  # big terminal (B01, B02)
TL = dict(ox=-4.6, oy=-1.5, k=1.1)                  # long-pipe terminal (B04-B08)
PH = t_port(**TH)                                   # hero port
PL = t_port(**TL)                                   # long port
PY_H, PY_L = float(PH[1]), float(PL[1])
CH = dict(xw=-2.55, xn=-1.05, y=PY_H, hw=1.4, hn=0.36, k=0.8)       # hero collector
CL = dict(xw=2.6, xn=4.3, y=PY_L, hw=1.8, hn=0.45, k=1.0)           # long-pipe collector
CABH = dict(ox=1.3, oy=-2.2, k=0.85)                                # hero cabinet
BOARD_H = dict(cx=4.75, cy=0.35, w=2.5, h=1.8, k=1.0)               # hero board


def hero_back():
    """The half docker compose starts: collector, pipe to the cabinet, cabinet, pipe to the board, board."""
    col = collector(**CH)
    p2 = pipe(CH["xn"] - 0.05, 0.85, PY_H, h=0.28)
    cab = cabinet(**CABH)
    p3 = pipe(2.0, BOARD_H["cx"] - BOARD_H["w"] / 2 + 0.05, PY_H + 0.55, h=0.22)
    brd = board(**BOARD_H)
    return col, p2, cab, p3, brd


def hero_pipe1():
    return pipe(float(PH[0]) - 0.05, CH["xw"] + 0.05, PY_H, h=0.3)


# ══════════════ B00: one pipeline, session to dashboard ══════════════
class B00_Pipeline(Scene):
    def construct(self):
        term = terminal(**TH)
        self.play(FadeIn(term, shift=DOWN * 0.8), run_time=0.6, rate_func=ease_in)
        until(self, "On the left", lead=0.3)
        ls = lab("session", [TH["ox"], 1.05])
        self.play(FadeIn(ls), run_time=0.4)
        col, p2, cab, p3, brd = hero_back()
        p1 = hero_pipe1()
        until(self, "run down a pipe", lead=0.3)
        self.play(GrowFromEdge(p1, LEFT), run_time=guard(self, 0.5))
        until(self, "into a collector", lead=0.4)
        self.play(FadeIn(col, shift=DOWN * 0.6), run_time=guard(self, 0.5), rate_func=ease_in)
        self.play(GrowFromEdge(p2, LEFT), run_time=guard(self, 0.4))
        until(self, "then into Prometheus", lead=0.3)
        self.play(FadeIn(cab, shift=DOWN * 0.6), run_time=guard(self, 0.5), rate_func=ease_in)
        self.play(GrowFromEdge(p3, LEFT), run_time=guard(self, 0.35))
        until(self, "out onto a Grafana", lead=0.3)
        self.play(FadeIn(VGroup(brd[0], brd[1], brd[2], brd[3]), shift=UP * 0.4), run_time=guard(self, 0.5))
        self.play(*[GrowFromEdge(b, DOWN) for b in brd[4][:3]], run_time=guard(self, 0.6))
        ld = lab("dashboard", [BOARD_H["cx"], 1.85])
        self.play(FadeIn(brd[4][3], scale=0.3), FadeIn(ld), run_time=guard(self, 0.4))
        done(self)


def b00_state():
    col, p2, cab, p3, brd = hero_back()
    return dict(term=terminal(**TH), p1=hero_pipe1(), col=col, p2=p2, cab=cab, p3=p3, brd=brd,
                ls=lab("session", [TH["ox"], 1.05]), ld=lab("dashboard", [BOARD_H["cx"], 1.85]))


# ══════════════ B01: the switch is one environment variable ══════════════
PLATE_X, PLATE_Y = 1.7, -0.55


def switch_plate(on=False):
    plate = RoundedRectangle(width=1.2, height=2.3, corner_radius=0.18, fill_color=BOX_L, fill_opacity=1, stroke_color=INK,
                             stroke_width=4).move_to(P(PLATE_X, PLATE_Y))
    slot = RoundedRectangle(width=0.42, height=1.45, corner_radius=0.2, fill_color=GHOST, fill_opacity=1, stroke_color=BAR1,
                            stroke_width=3).move_to(P(PLATE_X, PLATE_Y))
    knob = Circle(radius=0.27, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4
                  ).move_to(P(PLATE_X, PLATE_Y + (0.5 if on else -0.5)))
    return VGroup(plate, slot, knob)


ENV_AT = [0.2, 2.55]


class B01_Switch(Scene):
    def construct(self):
        s = b00_state()
        self.add(*s.values())
        big = terminal(**TB)
        rest = VGroup(s["p1"], s["col"], s["p2"], s["cab"], s["p3"], s["brd"], s["ls"], s["ld"])
        self.play(FadeOut(rest), run_time=0.45)
        self.play(ReplacementTransform(s["term"], big), run_time=0.7)
        sw = switch_plate(on=False)
        self.play(FadeIn(sw, shift=LEFT * 0.4), run_time=0.45)
        until(self, "opt-in", lead=0.3)
        lo = lab("opt-in", [PLATE_X, 1.25])
        self.play(FadeIn(lo), run_time=guard(self, 0.35))
        until(self, "one environment variable", lead=0.2)
        le = lab("CLAUDE_CODE_ENABLE_TELEMETRY=1", ENV_AT, 40)
        self.play(FadeIn(le), run_time=guard(self, 0.4))
        until(self, "Claude Code enable telemetry", lead=0.1)
        self.play(sw[2].animate.move_to(P(PLATE_X, PLATE_Y + 0.5)), run_time=guard(self, 0.35))
        lamp = t_lamp(**TB)
        port = t_port(**TB)
        d = drop(port, 0.2)
        self.play(FadeIn(lamp, scale=0.3), run_time=guard(self, 0.25))
        self.play(FadeIn(d), d.animate.move_to(port + RIGHT * 0.9), run_time=guard(self, 0.45))
        done(self)


def b01_state():
    port = t_port(**TB)
    return dict(term=terminal(**TB, lit=True), sw=switch_plate(on=True), lo=lab("opt-in", [PLATE_X, 1.25]),
                le=lab("CLAUDE_CODE_ENABLE_TELEMETRY=1", ENV_AT, 40), d=drop(port + RIGHT * 0.9, 0.2))


# ══════════════ B02: test the tap first — the console exporter ══════════════
SLOT_TB = IK(TB).p(0, 0.07, 1.3)
PR_X = float(SLOT_TB[0])


def printout(n_lines=5):
    """A white printout rising from the terminal's top slot (behind the terminal body), with grey metric lines."""
    w, h = 1.5, 2.45
    y0 = float(SLOT_TB[1]) - 0.1
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3
                     ).move_to([PR_X, y0 + h / 2, 0]).set_z_index(-1)
    lines = VGroup(*[Line([PR_X - 0.5, y0 + h - 0.35 - 0.36 * i, 0], [PR_X + (0.5 if i % 2 == 0 else 0.2), y0 + h - 0.35 - 0.36 * i, 0],
                          color=BAR1, stroke_width=8).set_z_index(-1) for i in range(n_lines)])
    return body, lines


PILL_END = P(1.55, -1.3)


def prompt_pill():
    return RoundedRectangle(width=1.5, height=0.5, corner_radius=0.25, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK,
                            stroke_width=3).move_to(P(3.2, -1.3))


def pill_arrow():
    return Arrow(P(0.72, -1.3), P(-0.55, -1.3), buff=0, color=INK, stroke_width=6, max_tip_length_to_length_ratio=0.3)


class B02_Console(Scene):
    def construct(self):
        s = b01_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["sw"], s["lo"], s["le"], s["d"])), run_time=0.45)
        body, lines = printout()
        until(self, "Set the metrics exporter to console", lead=0.2)
        lc = lab("console", [0.6, 2.25])
        self.play(GrowFromEdge(body, DOWN), run_time=guard(self, 0.6))
        self.play(FadeIn(lc), run_time=guard(self, 0.3))
        until(self, "cut the export interval", lead=0.2)
        self.play(Create(lines[0]), run_time=guard(self, 0.3))
        until(self, "to one second", lead=0.2)
        self.play(Create(lines[1]), run_time=guard(self, 0.3))
        until(self, "and run one prompt", lead=0.3)
        pill_ = prompt_pill()
        lp = lab("claude -p", [1.55, -2.05])
        self.play(FadeIn(pill_, shift=LEFT * 0.5), FadeIn(lp), run_time=guard(self, 0.4))
        self.play(pill_.animate.move_to(PILL_END), run_time=guard(self, 0.6))
        self.play(Create(pill_arrow()), run_time=guard(self, 0.25))
        until(self, "The metrics print", lead=0.3)
        for ln in lines[2:]:
            self.play(Create(ln), run_time=guard(self, 0.3))
        done(self)


def b02_state():
    body, lines = printout()
    return dict(term=terminal(**TB, lit=True), body=body, lines=lines, lc=lab("console", [0.6, 2.25]),
                lp=lab("claude -p", [1.55, -2.05]), pill=prompt_pill().move_to(PILL_END), ar=pill_arrow())


# ══════════════ B03: docker compose up starts three containers ══════════════
def lab_col():
    return lab("collector", [(CH["xw"] + CH["xn"]) / 2, 0.75])


def lab_prom():
    return lab("Prometheus", [CABH["ox"], 1.3])


def lab_graf():
    return lab("Grafana", [BOARD_H["cx"], 1.85])


class B03_Compose(Scene):
    def construct(self):
        s = b02_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["body"], s["lines"], s["lc"], s["lp"], s["pill"], s["ar"])), run_time=0.4)
        small = terminal(**TH, lit=True)
        self.play(ReplacementTransform(s["term"], small), run_time=0.7)
        until(self, "ships a Docker Compose file", lead=0.3)
        comp = upright_page(P(1.2, -1.2), w=1.6, h=2.1, n=6, indent=True)
        self.play(FadeIn(comp, shift=DOWN * 0.8), run_time=guard(self, 0.5), rate_func=ease_in)
        col, p2, cab, p3, brd = hero_back()
        until(self, "starts three containers", lead=0.3)
        self.play(Indicate(comp, color=None, scale_factor=1.06), run_time=guard(self, 0.4))
        until(self, "an Open Telemetry collector", lead=0.3)
        self.play(FadeOut(comp, scale=0.6), run_time=guard(self, 0.3))
        self.play(FadeIn(col, shift=DOWN * 0.8), run_time=guard(self, 0.45), rate_func=ease_in)
        self.play(FadeIn(lab_col()), run_time=guard(self, 0.25))
        until(self, "Prometheus, and", lead=0.3)
        self.play(FadeIn(cab, shift=DOWN * 0.8), run_time=guard(self, 0.45), rate_func=ease_in)
        self.play(FadeIn(lab_prom()), run_time=guard(self, 0.25))
        until(self, "and Grafana", lead=0.2)
        self.play(FadeIn(brd, shift=DOWN * 0.8), run_time=guard(self, 0.45), rate_func=ease_in)
        self.play(FadeIn(lab_graf()), run_time=guard(self, 0.25))
        until(self, "which draws the dashboards", lead=0.3)
        self.play(GrowFromEdge(p2, LEFT), run_time=guard(self, 0.35))
        self.play(GrowFromEdge(p3, LEFT), run_time=guard(self, 0.35))
        done(self)


def b03_state():
    col, p2, cab, p3, brd = hero_back()
    return dict(term=terminal(**TH, lit=True), col=col, p2=p2, cab=cab, p3=p3, brd=brd,
                l1=lab_col(), l2=lab_prom(), l3=lab_graf())


# ══════════════ B04: point Claude Code at the collector (OTLP over gRPC, localhost:4317) ══════════════
def long_pipe():
    return pipe(float(PL[0]) - 0.05, CL["xw"] + 0.05, PY_L, h=0.36)


def collar():
    """A kraft collar on the funnel mouth: the endpoint socket."""
    return Rectangle(width=0.3, height=0.75, fill_color=TILE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4
                     ).move_to([CL["xw"] - 0.12, PY_L, 0]).set_z_index(1)


def out_stub():
    return pipe(CL["xn"] - 0.05, 5.55, PY_L, h=0.26)


L_OTLP = [-0.4, 0.55]
L_4317 = [3.35, 1.2]


class B04_Endpoint(Scene):
    def construct(self):
        s = b03_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["p2"], s["cab"], s["p3"], s["brd"], s["l1"], s["l2"], s["l3"])), run_time=0.45)
        self.play(ReplacementTransform(s["term"], terminal(**TL, lit=True)), ReplacementTransform(s["col"], collector(**CL)),
                  run_time=0.8)
        stub = out_stub()
        self.play(GrowFromEdge(stub, LEFT), run_time=0.3)
        until(self, "Set the metrics exporter", lead=0.3)
        full = long_pipe()
        part = pipe(float(PL[0]) - 0.05, 1.7, PY_L, h=0.36)
        lo = lab("otlp over grpc", L_OTLP)
        self.play(GrowFromEdge(part, LEFT), run_time=guard(self, 0.8))
        self.play(FadeIn(lo), run_time=guard(self, 0.3))
        until(self, "set the endpoint", lead=0.3)
        c = collar()
        l4 = lab("localhost:4317", L_4317)
        self.play(FadeIn(c, shift=LEFT * 0.3), FadeIn(l4), run_time=guard(self, 0.4))
        until(self, "The pipe connects", lead=0.4)
        self.play(ReplacementTransform(part, full), run_time=guard(self, 0.4))
        ck = check(2.05, PY_L - 0.8, s=0.28)
        self.play(Create(ck), run_time=guard(self, 0.3))
        done(self)


def long_base(lit=True):
    return dict(term=terminal(**TL, lit=lit), col=collector(**CL), stub=out_stub(), pipe=long_pipe(), collar=collar())


def b04_state():
    d = long_base()
    d.update(lo=lab("otlp over grpc", L_OTLP), l4=lab("localhost:4317", L_4317), ck=check(2.05, PY_L - 0.8, s=0.28))
    return d


# ══════════════ B05: eight metrics drip down the pipe ══════════════
ROW_Y = 1.95
ROW_X = [-3.3 + 0.8 * i for i in range(8)]
L_8 = [4.3, ROW_Y]
WORDS = ["sessions", "lines of code", "pull requests", "commits", "cost,", "tokens", "code edit", "active time"]


class B05_Metrics(Scene):
    def construct(self):
        s = b04_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["lo"], s["l4"], s["ck"])), run_time=0.35)
        x0, x1 = float(PL[0]) + 0.2, CL["xw"] - 0.3
        for i in range(3):
            d = drop([x0, PY_L])
            self.play(FadeIn(d, scale=0.3), run_time=guard(self, 0.15))
            self.play(d.animate.move_to(P(x1, PY_L)), run_time=guard(self, 0.75), rate_func=linear)
            self.play(FadeOut(d, scale=0.5), run_time=guard(self, 0.12))
        until(self, "eight metrics", lead=0.3)
        l8 = lab("8 metrics", L_8)
        self.play(FadeIn(l8), run_time=guard(self, 0.3))
        for x, w in zip(ROW_X, WORDS):
            until(self, w, lead=0.15)
            self.play(FadeIn(drop([x, ROW_Y], 0.2), shift=UP * 0.3), run_time=guard(self, 0.25))
        done(self)


def b05_state():
    d = long_base()
    d.update(row=VGroup(*[drop([x, ROW_Y], 0.2) for x in ROW_X]), l8=lab("8 metrics", L_8))
    return d


# ══════════════ B06: tags — type, model, session.id ══════════════
COLS = [-2.1, -0.6, 0.9, 2.4]
DY = 1.55


def tag(cx, top, w=0.82, h=0.72, fill=TILE_L):
    return Polygon([cx - w / 2, top - 0.2, 0], [cx, top, 0], [cx + w / 2, top - 0.2, 0], [cx + w / 2, top - h, 0], [cx - w / 2, top - h, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4)


def string(cx, y0, y1):
    return Line([cx, y0, 0], [cx, y1, 0], color=BAR1, stroke_width=5)


def tags_model():
    return VGroup(*[VGroup(string(x, DY - 0.55, DY - 1.0), tag(x, DY - 1.0, w=1.05, h=0.9)) for x in COLS])


def tags_sid():
    return VGroup(*[VGroup(string(x, DY - 1.9, DY - 2.35), tag(x, DY - 2.35, w=1.05, h=0.9, fill=BAR2)) for x in COLS])


def type_drops():
    return VGroup(*[drop([x, DY], 0.55) for x in COLS])


L_TYPE, L_MODEL, L_SID = [-4.75, DY], [-4.75, DY - 1.5], [-4.75, DY - 2.85]


class B06_Tags(Scene):
    def construct(self):
        s = b05_state()
        self.add(*s.values())
        tok = s["row"][5]
        others = VGroup(*[m for i, m in enumerate(s["row"]) if i != 5])
        self.play(FadeOut(VGroup(s["term"], s["col"], s["stub"], s["pipe"], s["collar"], s["l8"], others)), run_time=0.45)
        big = drop([0.15, DY], 0.8)
        self.play(ReplacementTransform(tok, big), run_time=0.6)
        until(self, "split by type", lead=0.3)
        four = type_drops()
        self.play(FadeOut(big, scale=0.6), *[FadeIn(d, shift=(np.array(d.get_center()) - P(0.15, DY)) * 0.5) for d in four], run_time=guard(self, 0.6))
        self.play(FadeIn(lab("type", L_TYPE)), run_time=guard(self, 0.3))
        until(self, "name the model", lead=0.3)
        tm = tags_model()
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.3) for t in tm], lag_ratio=0.2), run_time=guard(self, 0.7))
        self.play(FadeIn(lab("model", L_MODEL)), run_time=guard(self, 0.3))
        until(self, "every metric carries", lead=0.3)
        ts = tags_sid()
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.3) for t in ts], lag_ratio=0.2), run_time=guard(self, 0.7))
        self.play(FadeIn(lab("session.id", L_SID)), run_time=guard(self, 0.3))
        done(self)


def b06_state():
    return dict(four=type_drops(), tm=tags_model(), ts=tags_sid(), l1=lab("type", L_TYPE), l2=lab("model", L_MODEL),
                l3=lab("session.id", L_SID))


# ══════════════ B07: events are a second stream; the guide's collector carries metrics only ══════════════
EV_Y = 1.55
EV_X0, EV_X1 = TL["ox"], 2.05


def ev_pipe():
    riser = Rectangle(width=0.2, height=EV_Y - 0.05, fill_color=BOX_L, fill_opacity=1, stroke_color=PIPE_EDGE, stroke_width=4
                      ).move_to([EV_X0, (EV_Y + 0.1) / 2, 0]).set_z_index(-1)
    run = Rectangle(width=EV_X1 - EV_X0 + 0.1, height=0.2, fill_color=BOX_L, fill_opacity=1, stroke_color=PIPE_EDGE, stroke_width=4
                    ).move_to([(EV_X0 + EV_X1) / 2, EV_Y, 0]).set_z_index(-1)
    return VGroup(riser, run)


def cap():
    return Rectangle(width=0.3, height=0.62, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([EV_X1 + 0.15, EV_Y, 0])


def slip(x):
    return Rectangle(width=0.42, height=0.3, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, EV_Y + 0.26, 0])


SLIP_END = [EV_X1 - 0.35 - 0.5 * i for i in range(3)]
L_EV, L_MO = [-1.2, 2.35], [4.3, EV_Y]


class B07_Events(Scene):
    def construct(self):
        s = b06_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        base = long_base()
        self.play(FadeIn(VGroup(*base.values())), run_time=0.45)
        ep = ev_pipe()
        self.play(GrowFromEdge(ep[0], DOWN), run_time=0.3)
        self.play(GrowFromEdge(ep[1], LEFT), run_time=0.5)
        self.play(FadeIn(lab("events", L_EV)), run_time=0.3)
        until(self, "one record each time", lead=0.3)
        slips = [slip(EV_X0 + 0.5) for _ in range(3)]
        for sl, xe in zip(slips, SLIP_END):
            self.play(FadeIn(sl, scale=0.4), run_time=guard(self, 0.15))
            self.play(sl.animate.move_to([xe - 2.2, EV_Y + 0.26, 0]), run_time=guard(self, 0.45), rate_func=linear)
        until(self, "The guide's collector has one pipeline", lead=0.3)
        c = cap()
        self.play(FadeIn(c, shift=LEFT * 0.3), FadeIn(lab("metrics only", L_MO)), run_time=guard(self, 0.4))
        until(self, "so events would need", lead=0.3)
        self.play(*[sl.animate.move_to([xe, EV_Y + 0.26, 0]) for sl, xe in zip(slips, SLIP_END)], run_time=guard(self, 0.6))
        done(self)


def b07_state():
    d = long_base()
    d.update(ep=ev_pipe(), cap=cap(), slips=VGroup(*[slip(xe) for xe in SLIP_END]), le=lab("events", L_EV), lm=lab("metrics only", L_MO))
    return d


# ══════════════ B08: what stays out — prompt text, file contents; the email goes only to your endpoint ══════════════
HX = -1.5                                                                     # hopper centre
H_TOP = PY_L + 1.05


def hopper():
    return Polygon([HX - 1.0, H_TOP, 0], [HX + 1.0, H_TOP, 0], [HX + 0.28, PY_L + 0.1, 0], [HX - 0.28, PY_L + 0.1, 0],
                   fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)


def lid():
    return Rectangle(width=2.2, height=0.2, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([HX, H_TOP + 0.1, 0])


def strip_(x):
    return Rectangle(width=0.8, height=0.16, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, PY_L + 0.27, 0])


def email_tag(x):
    return tag(x, PY_L + 0.95, w=0.6, h=0.55)


PAGE_A, PAGE_B = P(HX - 0.52, H_TOP + 0.2), P(HX + 0.52, H_TOP + 0.2)
L_PT, L_LEN, L_END = [-4.3, 1.9], [0.9, PY_L - 0.8], [3.45, 1.05]
STRIP_X, TAG_X = 0.9, 2.05


class B08_Privacy(Scene):
    def construct(self):
        s = b07_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["ep"], s["cap"], s["slips"], s["le"], s["lm"])), run_time=0.4)
        hp = hopper()
        pa = upright_page(PAGE_A + UP * 1.4, w=0.9, h=1.15)
        self.play(FadeIn(hp, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(pa, shift=DOWN * 0.4), FadeIn(lab("prompt text", L_PT)), run_time=0.4)
        until(self, "isn't collected", lead=0.3)
        ld = lid()
        self.play(FadeIn(ld, shift=LEFT * 0.6), run_time=guard(self, 0.35))
        self.play(pa.animate.move_to(PAGE_A + UP * 0.575), run_time=guard(self, 0.35), rate_func=ease_in)
        until(self, "only its length", lead=0.3)
        st = strip_(HX)
        self.play(FadeIn(st, scale=0.4), run_time=guard(self, 0.2))
        self.play(st.animate.move_to([STRIP_X, PY_L + 0.27, 0]), run_time=guard(self, 0.6))
        self.play(FadeIn(lab("length", L_LEN)), run_time=guard(self, 0.25))
        until(self, "Raw file contents", lead=0.3)
        pb = upright_page(PAGE_B + UP * 1.4, w=0.9, h=1.15, n=5, indent=True)
        self.play(FadeIn(pb, shift=DOWN * 0.4), run_time=guard(self, 0.3))
        self.play(pb.animate.move_to(PAGE_B + UP * 0.575), run_time=guard(self, 0.35), rate_func=ease_in)
        until(self, "And your email", lead=0.3)
        et = email_tag(float(PL[0]) + 0.5)
        self.play(FadeIn(et, scale=0.4), run_time=guard(self, 0.2))
        self.play(et.animate.move_to([TAG_X, PY_L + 0.95 - 0.275, 0]), run_time=guard(self, 1.1), rate_func=linear)
        until(self, "goes only to the endpoint", lead=0.3)
        self.play(FadeIn(lab("your endpoint", L_END)), run_time=guard(self, 0.3))
        done(self)


# ══════════════ B09: inside the collector — receiver 4317, batch, Prometheus exporter 8889 ══════════════
CB = dict(xw=-2.3, xn=1.0, y=0.55, hw=3.0, hn=0.8, k=1.4)
TRAY = Iso(2.75, -1.05, 0.9)
SHELF = Iso(5.0, -1.5, 0.75)
SHELF_TOP_Y = float(SHELF.p(0, 0, 0.18)[1])
SHELF_DROPS = [(4.55, SHELF_TOP_Y + 0.2), (5.0, SHELF_TOP_Y + 0.2), (5.45, SHELF_TOP_Y + 0.2)]
TRAY_DROPS = [(2.45, -0.72), (2.8, -0.62), (3.12, -0.75)]
L_IN, L_BATCH, L_OUT = [-4.3, 1.45], [2.8, 0.55], [5.0, -2.55]


def stub_in():
    return pipe(-5.9, CB["xw"] + 0.05, CB["y"], h=0.36)


def tray():
    return TRAY.open_box(-0.7, -0.5, 0, 1.4, 1.0, 0.45)


def shelf():
    return SHELF.box(-0.8, -0.5, 0, 1.6, 1.0, 0.18, TILE_TOP, TILE_L, TILE_R)


class B09_Collector(Scene):
    def construct(self):
        s = long_base()
        self.add(*s.values())
        keep = [s["col"]]
        self.play(FadeOut(VGroup(s["term"], s["stub"], s["pipe"], s["collar"])), run_time=0.4)
        self.play(ReplacementTransform(s["col"], collector(**CB)), run_time=0.7)
        si = stub_in()
        self.play(GrowFromEdge(si, RIGHT), run_time=0.4)
        until(self, "takes the metrics in", lead=0.3)
        self.play(FadeIn(lab("port 4317", L_IN)), run_time=guard(self, 0.3))
        ds = [drop([-5.4, CB["y"]], 0.2) for _ in range(3)]
        for d in ds:
            self.play(FadeIn(d, scale=0.3), run_time=guard(self, 0.12))
            self.play(d.animate.move_to(P(CB["xw"] + 0.3, CB["y"])), run_time=guard(self, 0.45), rate_func=linear)
        until(self, "A batch step", lead=0.3)
        back, front = tray()
        self.play(FadeIn(back), FadeIn(front), run_time=guard(self, 0.35))
        self.play(FadeIn(lab("batch", L_BATCH)), run_time=guard(self, 0.25))
        self.play(FadeOut(VGroup(*ds), scale=0.5), run_time=guard(self, 0.2))
        outs = []
        for (x, y) in TRAY_DROPS:
            d = drop([CB["xn"] + 0.1, CB["y"]], 0.2).set_z_index(1)
            self.play(FadeIn(d, scale=0.4), run_time=guard(self, 0.12))
            self.play(MoveAlongPath(d, ArcBetweenPoints(P(CB["xn"] + 0.1, CB["y"]), P(x, y), angle=-0.8)), run_time=guard(self, 0.3))
            outs.append(d)
        until(self, "a Prometheus exporter", lead=0.3)
        sh = shelf()
        self.play(FadeIn(sh, shift=UP * 0.3), run_time=guard(self, 0.3))
        for d, (x, y) in zip(outs, SHELF_DROPS):
            self.play(MoveAlongPath(d, ArcBetweenPoints(d.get_center(), P(x, y), angle=-0.9)), run_time=guard(self, 0.3))
        until(self, "on port eighty-eight", lead=0.3)
        self.play(FadeIn(lab("port 8889", L_OUT)), run_time=guard(self, 0.3))
        done(self)


def b09_state():
    back, front = tray()
    return dict(col=collector(**CB), si=stub_in(), tray=VGroup(back, front), sh=shelf(),
                ds=VGroup(*[drop(list(xy), 0.2) for xy in SHELF_DROPS]),
                l1=lab("port 4317", L_IN), l2=lab("batch", L_BATCH), l3=lab("port 8889", L_OUT))


# ══════════════ B10: Prometheus scrapes every 15 seconds and files time series ══════════════
CS = dict(xw=-5.55, xn=-3.95, y=0.35, hw=1.4, hn=0.38, k=0.7)
SHELF_S = Iso(-3.05, -1.25, 0.6)
SS_TOP = float(SHELF_S.p(0, 0, 0.18)[1])
SS_DROPS = [(-3.4, SS_TOP + 0.17), (-3.05, SS_TOP + 0.17), (-2.7, SS_TOP + 0.17)]
CAB10 = dict(ox=0.55, oy=-2.15, k=1.15)
ARM_Y = SS_TOP + 0.2
L_SCR, L_15 = [-2.2, ARM_Y + 0.65], [-2.2, ARM_Y + 1.55]
TS_X0, TS_X1, TS_Y = 2.55, 6.0, -1.55
TS_PTS = [(2.9, -1.1), (3.6, -0.75), (4.3, -0.85), (5.0, -0.2), (5.7, 0.35)]


def shelf_s():
    return SHELF_S.box(-0.8, -0.5, 0, 1.6, 1.0, 0.18, TILE_TOP, TILE_L, TILE_R)


def arm():
    x1 = cab_left_x(CAB10["ox"], CAB10["k"]) + 0.3
    return Rectangle(width=x1 - (-2.55), height=0.14, fill_color=BAR1, fill_opacity=1, stroke_width=0
                     ).move_to([(x1 - 2.55) / 2, ARM_Y, 0]).set_z_index(-1)


def ts_axis():
    return Line([TS_X0, TS_Y, 0], [TS_X1, TS_Y, 0], color=INK, stroke_width=5)


def ts_dot(i):
    x, y = TS_PTS[i]
    return Dot([x, y, 0], radius=0.12, color=TERRA if i == len(TS_PTS) - 1 else BAR1).set_stroke(INK, 3 if i < len(TS_PTS) - 1 else 0)


def ts_seg(i):
    (x0, y0), (x1, y1) = TS_PTS[i], TS_PTS[i + 1]
    return Line([x0, y0, 0], [x1, y1, 0], color=INK, stroke_width=5).set_z_index(-1)


class B10_Scrape(Scene):
    def construct(self):
        s = b09_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["si"], s["tray"], s["l1"], s["l2"], s["l3"])), run_time=0.35)
        small_ds = VGroup(*[drop(list(xy), 0.15) for xy in SS_DROPS])
        self.play(ReplacementTransform(s["col"], collector(**CS)), ReplacementTransform(s["sh"], shelf_s()),
                  ReplacementTransform(s["ds"], small_ds), run_time=0.6)
        cab = cabinet(**CAB10)
        self.play(FadeIn(cab, shift=DOWN * 0.6), run_time=0.45, rate_func=ease_in)
        ax = ts_axis()
        self.play(Create(ax), run_time=0.3)
        until(self, "It scrapes", lead=0.2)
        a = arm()
        self.play(GrowFromEdge(a, RIGHT), FadeIn(lab("scrape", L_SCR)), run_time=guard(self, 0.4))
        xin = cab_left_x(CAB10["ox"], CAB10["k"]) + 0.2
        self.play(*[d.animate.move_to(P(xin, ARM_Y)) for d in small_ds], run_time=guard(self, 0.45))
        self.play(FadeOut(small_ds), FadeIn(ts_dot(0), scale=0.3), run_time=guard(self, 0.2))
        until(self, "every fifteen seconds", lead=0.2)
        self.play(FadeIn(lab("every 15 s", L_15)), run_time=guard(self, 0.3))
        for i in range(1, 3):
            nd = VGroup(*[drop(list(xy), 0.15) for xy in SS_DROPS])
            self.play(FadeIn(nd, scale=0.4), run_time=guard(self, 0.2))
            self.play(*[d.animate.move_to(P(xin, ARM_Y)) for d in nd], run_time=guard(self, 0.4))
            self.play(FadeOut(nd), FadeIn(ts_dot(i), scale=0.3), Create(ts_seg(i - 1)), run_time=guard(self, 0.25))
        until(self, "files each number", lead=0.2)
        for i in range(3, len(TS_PTS)):
            self.play(Create(ts_seg(i - 1)), FadeIn(ts_dot(i), scale=0.3), run_time=guard(self, 0.35))
        done(self)


def b10_state():
    ts = VGroup(ts_axis(), *[ts_seg(i) for i in range(len(TS_PTS) - 1)], *[ts_dot(i) for i in range(len(TS_PTS))])
    return dict(col=collector(**CS), sh=shelf_s(), cab=cabinet(**CAB10), arm=arm(), ts=ts,
                l1=lab("scrape", L_SCR), l2=lab("every 15 s", L_15))


# ══════════════ B11: PromQL — the Prometheus name, summed by type ══════════════
CAB11 = dict(ox=-4.3, oy=-2.15, k=1.15)
NAME_AT, PQ_AT, BT_AT = [1.55, 2.65], [-4.3, 2.65], [5.0, 1.0]
COL_BASE = -2.35
COL4 = [(0.3, 1.5, BAR1), (1.3, 2.6, BAR2), (2.3, 3.4, BAR1), (3.3, 1.2, BAR2)]


def drawer_out():
    I = IK(CAB11)
    return I.box(-0.45, -1.45, 1.95, 0.9, 0.95, 0.62).set_z_index(2)


def drawer_cards():
    I = IK(CAB11)
    return VGroup(*[I.quad([(-0.3, y0, 2.57), (0.3, y0, 2.57), (0.3, y0 + 0.16, 2.57), (-0.3, y0 + 0.16, 2.57)], PAGE_TOP, stroke=BAR1, sw=2)
                    for y0 in (-1.3, -1.05, -0.8)]).set_z_index(3)


def col_bar(x, h, c):
    return Rectangle(width=0.7, height=h, fill_color=c, fill_opacity=1, stroke_width=0).move_to([x, COL_BASE + h / 2, 0])


class B11_Query(Scene):
    def construct(self):
        s = b10_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(s["col"], s["sh"], s["arm"], s["ts"], s["l1"], s["l2"])), run_time=0.4)
        self.play(ReplacementTransform(s["cab"], cabinet(**CAB11)), run_time=0.6)
        self.play(FadeIn(lab("PromQL", PQ_AT)), run_time=0.3)
        dr = drawer_out()
        cards = drawer_cards()
        self.play(FadeIn(dr, shift=IK(CAB11).v(0, -0.6, 0)), run_time=0.45)
        self.play(FadeIn(cards), run_time=0.3)
        until(self, "becomes claude code token usage", lead=0.3)
        self.play(FadeIn(lab("claude_code_token_usage_tokens_total", NAME_AT, 36)), run_time=guard(self, 0.4))
        until(self, "Add it up by type", lead=0.3)
        one = col_bar(1.8, 3.6, BAR1)
        self.play(GrowFromEdge(one, DOWN), run_time=guard(self, 0.6))
        until(self, "one total splits", lead=0.2)
        four = VGroup(*[col_bar(x, h, c) for x, h, c in COL4])
        self.play(FadeOut(one), LaggedStart(*[GrowFromEdge(b, DOWN) for b in four], lag_ratio=0.25), run_time=guard(self, 0.9))
        self.play(FadeIn(lab("by type", BT_AT)), run_time=guard(self, 0.3))
        done(self)


def b11_state():
    return dict(cab=cabinet(**CAB11), dr=drawer_out(), cards=drawer_cards(), l1=lab("PromQL", PQ_AT),
                l2=lab("claude_code_token_usage_tokens_total", NAME_AT, 36),
                four=VGroup(*[col_bar(x, h, c) for x, h, c in COL4]), l3=lab("by type", BT_AT))


# ══════════════ B12: the Grafana dashboard; cost is an approximation ══════════════
BIG = dict(cx=0.3, cy=-0.05, w=9.0, h=4.5, k=1.6)
TILE_X = [-2.95, -0.85, 1.25, 3.35]
TILE_Y = 0.95
PIE_C, PIE_R = P(0.3, -1.25), 0.95
L_GRAF, L_APX = [-3.35, 2.75], [-2.95, -2.85]


def stat_tile(x):
    return Rectangle(width=1.85, height=1.2, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=4).move_to([x, TILE_Y, 0])


def tile_bar(x, frac):
    w = 1.3 * frac
    return Rectangle(width=w, height=0.34, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([x - 0.65 + w / 2, TILE_Y - 0.1, 0])


def wedge(a0, a1, color):
    pts = [PIE_C] + [PIE_C + PIE_R * np.array([np.cos(a), np.sin(a), 0.0]) for a in np.linspace(a0, a1, 24)]
    return Polygon(*pts, fill_color=color, fill_opacity=1, stroke_color=PAGE_TOP, stroke_width=4)


def big_board():
    b = board(**BIG, bars=False, stand=False)
    return b


class B12_Dashboard(Scene):
    def construct(self):
        s = b11_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        bb = big_board()
        self.play(FadeIn(bb, shift=UP * 0.4), FadeIn(lab("Grafana", L_GRAF)), run_time=0.5)
        fr = [0.8, 0.45, 0.95, 0.6]
        for x, f, w in zip(TILE_X, fr, ["total cost", "active users", "tokens,", "lines of code"]):
            until(self, w, lead=0.2)
            self.play(FadeIn(stat_tile(x), shift=UP * 0.2), run_time=guard(self, 0.25))
            self.play(GrowFromEdge(tile_bar(x, f), LEFT), run_time=guard(self, 0.3))
        until(self, "cost by model", lead=0.2)
        w1, w2 = wedge(np.pi / 2, np.pi / 2 + 2 * np.pi * 0.7, BAR1), wedge(np.pi / 2 + 2 * np.pi * 0.7, np.pi / 2 + 2 * np.pi, BAR2)
        self.play(FadeIn(w1, scale=0.5), run_time=guard(self, 0.35))
        self.play(FadeIn(w2, scale=0.5), run_time=guard(self, 0.3))
        until(self, "The cost figures are approximations", lead=0.3)
        dt = Dot([TILE_X[0] + 0.72, TILE_Y + 0.4, 0], radius=0.11, color=TERRA)
        self.play(FadeIn(dt, scale=0.3), FadeIn(lab("approximate", L_APX, 42)), run_time=guard(self, 0.35))
        done(self)


def b12_state():
    return dict(bb=big_board(), lg=lab("Grafana", L_GRAF),
                tiles=VGroup(*[stat_tile(x) for x in TILE_X]),
                bars=VGroup(*[tile_bar(x, f) for x, f in zip(TILE_X, [0.8, 0.45, 0.95, 0.6])]),
                pie=VGroup(wedge(np.pi / 2, np.pi / 2 + 2 * np.pi * 0.7, BAR1), wedge(np.pi / 2 + 2 * np.pi * 0.7, np.pi / 2 + 2 * np.pi, BAR2)),
                dt=Dot([TILE_X[0] + 0.72, TILE_Y + 0.4, 0], radius=0.11, color=TERRA), la=lab("approximate", L_APX, 42))


# ══════════════ B13: managed settings, once for everyone; a repo can't turn it on ══════════════
TEAM_X = [-4.9, -2.7, -0.5, 1.7]
TEAM_OY, TEAM_K = -2.0, 0.62
SET_BOTTOM = P(-1.6, 1.25)
FOLDER_C = P(4.6, -1.55)
L_MS, L_RS = [1.35, 2.2], [4.6, -2.85]


def team_top(x):
    return Iso(x, TEAM_OY, TEAM_K).p(0, 0.3, 1.3)


def feed(x):
    t = team_top(x)
    return Line(SET_BOTTOM + UP * 0.02, t + UP * 0.12, color=BAR1, stroke_width=5).set_z_index(-1)


def folder():
    c = FOLDER_C
    tab = Polygon(c + P(-0.8, 0.55), c + P(-0.25, 0.55), c + P(-0.1, 0.72), c + P(-0.8, 0.72),
                  fill_color=TILE_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    page_ = Rectangle(width=1.1, height=0.9, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(c + P(0.05, 0.35))
    body = Rectangle(width=1.7, height=1.1, fill_color=TILE_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c)
    return VGroup(tab, page_, body)


def blocked():
    a, b = FOLDER_C + P(-0.3, 0.8), P(3.05, 0.35)
    dl = DashedLine(a, b, dash_length=0.18, color=BAR1, stroke_width=6)
    x = P(2.85, 0.5)
    cross = VGroup(Line(x + P(-0.28, -0.28), x + P(0.28, 0.28), color=INK, stroke_width=9),
                   Line(x + P(-0.28, 0.28), x + P(0.28, -0.28), color=INK, stroke_width=9))
    return dl, cross


class B13_Team(Scene):
    def construct(self):
        s = b12_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        sp = upright_page(SET_BOTTOM, w=1.5, h=1.45, n=5)
        self.play(FadeIn(sp, shift=DOWN * 0.4), FadeIn(lab("managed settings", L_MS)), run_time=0.45)
        terms = [terminal(x, TEAM_OY, TEAM_K) for x in TEAM_X]
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.3) for t in terms], lag_ratio=0.2), run_time=0.8)
        until(self, "sets the same variables once", lead=0.2)
        self.play(*[Create(feed(x)) for x in TEAM_X], run_time=guard(self, 0.6))
        self.play(LaggedStart(*[FadeIn(t_lamp(x, TEAM_OY, TEAM_K), scale=0.3) for x in TEAM_X], lag_ratio=0.2), run_time=guard(self, 0.6))
        until(self, "A repository's own settings", lead=0.3)
        f = folder()
        self.play(FadeIn(f, shift=UP * 0.3), FadeIn(lab("repo settings", L_RS)), run_time=guard(self, 0.4))
        dl, cr = blocked()
        until(self, "can't turn telemetry on", lead=0.3)
        self.play(Create(dl), run_time=guard(self, 0.5))
        self.play(Create(cr), run_time=guard(self, 0.3))
        done(self)


def b13_state():
    dl, cr = blocked()
    return dict(sp=upright_page(SET_BOTTOM, w=1.5, h=1.45, n=5), lm=lab("managed settings", L_MS),
                terms=VGroup(*[terminal(x, TEAM_OY, TEAM_K) for x in TEAM_X]), feeds=VGroup(*[feed(x) for x in TEAM_X]),
                lamps=VGroup(*[t_lamp(x, TEAM_OY, TEAM_K) for x in TEAM_X]), f=folder(), lr=lab("repo settings", L_RS), dl=dl, cr=cr)


# ══════════════ B14: the report — Prometheus totals + Linear MCP into claude -p ══════════════
CAB14 = dict(ox=-5.1, oy=-2.0, k=0.9)
TR = dict(ox=-1.7, oy=-1.6, k=1.05)
MCP_I = Iso(1.55, -2.35, 1.0)
REP_BOTTOM = P(4.5, -1.55)
L_CP, L_LIN, L_REP = [-1.7, 1.45], [1.55, 0.05], [4.5, 1.75]


def linear_mcp():
    return MCP_I.mcp(-0.65, -0.65, 0, w=1.3, d=1.3, h=0.75)


def mcp_cable():
    a = MCP_I.p(-0.65, 0.0, 0.35)
    b = IK(TR).p(0.8, -0.2, 0.4)
    return Line(a, b, color=BAR1, stroke_width=6).set_z_index(-1)


def report_page():
    x, y, w, h = float(REP_BOTTOM[0]), float(REP_BOTTOM[1]), 1.9, 2.6
    body = Rectangle(width=w, height=h, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y + h / 2, 0])
    lines = VGroup(*[Line([x - 0.62, y + h * f, 0], [x + (0.62 if i % 2 == 0 else 0.25), y + h * f, 0], color=BAR2, stroke_width=7)
                     for i, f in enumerate((0.86, 0.74, 0.62, 0.5))])
    return VGroup(body, lines)


def report_bars():
    y0 = float(REP_BOTTOM[1]) + 0.25
    return VGroup(*[Rectangle(width=0.32, height=h, fill_color=c, fill_opacity=1, stroke_width=0).move_to([4.0 + 0.5 * i, y0 + h / 2, 0])
                    for i, (h, c) in enumerate([(0.35, BAR1), (0.6, BAR2), (0.45, BAR1)])])


class B14_Report(Scene):
    def construct(self):
        s = b13_state()
        self.add(*s.values())
        self.play(FadeOut(VGroup(*s.values())), run_time=0.4)
        cab = cabinet(**CAB14)
        term = terminal(**TR, lit=True)
        self.play(FadeIn(cab, shift=DOWN * 0.5), FadeIn(term, shift=DOWN * 0.5), run_time=0.5, rate_func=ease_in)
        until(self, "pulls totals from Prometheus", lead=0.3)
        a = IK(CAB14).p(0.0, -0.5, 2.6)
        b = IK(TR).p(0.0, -0.6, 0.7)
        sl = Rectangle(width=0.55, height=0.38, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to(a).set_z_index(3)
        self.play(FadeIn(sl, scale=0.4), run_time=guard(self, 0.2))
        self.play(MoveAlongPath(sl, ArcBetweenPoints(a, b, angle=-1.0)), run_time=guard(self, 0.8))
        until(self, "hands them to claude", lead=0.3)
        self.play(FadeOut(sl, scale=0.4), FadeIn(lab("claude -p", L_CP)), run_time=guard(self, 0.3))
        until(self, "through the Linear", lead=0.3)
        m = linear_mcp()
        self.play(FadeIn(m, shift=DOWN * 0.6), run_time=guard(self, 0.4), rate_func=ease_in)
        self.play(Create(mcp_cable()), FadeIn(lab("Linear MCP", L_LIN)), run_time=guard(self, 0.4))
        until(self, "writes a productivity report", lead=0.3)
        rp = report_page()
        self.play(FadeIn(rp[0], shift=UP * 0.4), run_time=guard(self, 0.35))
        self.play(*[Create(ln) for ln in rp[1]], run_time=guard(self, 0.4))
        self.play(*[GrowFromEdge(r, DOWN) for r in report_bars()], FadeIn(lab("report", L_REP)), run_time=guard(self, 0.4))
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Pipeline, B01_Switch, B02_Console, B03_Compose, B04_Endpoint, B05_Metrics, B06_Tags, B07_Events,
             B08_Privacy, B09_Collector, B10_Scrape, B11_Query, B12_Dashboard, B13_Team, B14_Report):
    _cls.play = ST.play
