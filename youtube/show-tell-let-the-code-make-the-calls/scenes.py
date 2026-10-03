"""
Manim scenes for show-tell-let-the-code-make-the-calls (show-tell skill, card #18, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Programmatic tool calling, from anthropics/claude-cookbooks/tool_use/programmatic_tool_calling_ptc.ipynb, checked
against the raw live docs page (sources/live_programmatic-tool-calling-2026-09-27.md):
CLAUDE (a kraft block with a terracotta spark on a dark plinth) sits at the left beside its CONTEXT gauge (a tall
kraft column that fills with grey segments); YOUR APP is a dark three-slab server stack at the right, one slab per
tool, lights turning terracotta. Normal tool use: a white REQUEST slip arcs to your app and a thick white RESULT ream
arcs back into the gauge, eight times, until it is full. Programmatic tool calling: a kraft SANDBOX (an open box on a
dark plinth) drops in between; each tool's port lights (allowed callers); Claude's SCRIPT page drops into the sandbox;
the script's calls go to your app and the reams come back into the sandbox, not the gauge; a terracotta scan line does
the sums and only a small PRINTOUT card crosses to Claude. Then the notebook's token bars (85.6%, per Anthropic's
notebook) and where it pays.
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







# ═════════════════════════════ the film: let the code make the calls ═════════════════════════════
# Cast: CLAUDE (kraft block, terracotta spark, dark plinth) at the left; its CONTEXT gauge (a tall kraft column on a
# dark plinth that fills with grey segments); YOUR APP (a dark three-slab server stack, one slab per tool, lights);
# a white REQUEST slip; a thick white RESULT ream with grey page edges; the SANDBOX (a low kraft open box on a dark
# plinth) with a PILE block that grows inside it; the SCRIPT page hovering over the sandbox; a small PRINTOUT card.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


# ─────────────── Claude ───────────────
S_ = 1.15
CL = Iso(-4.45, -1.85, S_)
CW_ = 1.3
CL_TOP = CL.p(0.65, 0.65, 1.3) + UP * 0.75


def claude_block(iso=CL, w=CW_, h=1.3):
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
    return lab("Claude", [-4.5, -2.95])


# ─────────────── the context gauge ───────────────
GA = Iso(-1.95, -2.05, S_)
GW, GH, GZ = 0.75, 2.85, 0.25
GA_TOP = GA.p(0.35, 0.35, GZ + GH) + UP * 0.55
SEG_Z0, SEG_H, SEG_STEP = GZ + 0.1, 0.22, 0.3


def gauge():
    plinth = GA.box(-0.1, -0.1, 0, GW + 0.2, GW + 0.2, GZ, DARK_TOP, DARK_L, DARK_R)
    col = GA.box(0, 0, GZ, GW, GW, GH)
    return VGroup(plinth, col).set_z_index(1)


def seg(k, thin=False):
    z0 = SEG_Z0 + k * SEG_STEP
    z1 = z0 + (0.1 if thin else SEG_H)
    return GA.quad([(0.1, 0, z0), (GW - 0.1, 0, z0), (GW - 0.1, 0, z1), (0.1, 0, z1)], (BAR1, BAR2)[k % 2], sw=0).set_z_index(3)


def l_context():
    return lab("context", [-1.95, -2.95])


# ─────────────── your app: the server stack (one slab per tool) ───────────────
SV = Iso(4.6, -2.05, S_)
SW_, SLAB = 1.35, 0.55
SV_TOP = SV.p(0.67, 0.67, 3 * SLAB + 0.08) + UP * 0.75


def server_stack():
    stack = VGroup(*[SV.box(0, 0, i * (SLAB + 0.04), SW_, SW_, SLAB, DARK_TOP, DARK_L, DARK_R) for i in range(3)])
    return stack.set_z_index(1)


def light(i, color=TERRA):
    """Tool i's light (0 = bottom = custom budget, 1 = expenses, 2 = team list)."""
    return Dot(SV.p(0.28, 0, i * (SLAB + 0.04) + SLAB / 2), radius=0.09, color=color).set_z_index(3)


def lights(color=TERRA):
    return VGroup(*[light(i, color) for i in range(3)])


def l_app():
    return lab("your app", [4.5, -2.95])


def slab_port(i):
    """Where a cable to tool i's slab ends: just short of the slab's left face (never touching the dark block)."""
    return SV.p(0, 0.55, i * (SLAB + 0.04) + SLAB / 2) + LEFT * 0.3


# ─────────────── slips and reams ───────────────
def slip(center, s=0.6):
    iso = Iso(0, 0, s)
    body = iso.box(0, 0, 0, 0.9, 0.6, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    dot = Dot(iso.p(0.3, 0.3, 0.06), radius=0.07 * s / 0.6, color=TERRA)
    return VGroup(body, dot).move_to(center).set_z_index(6)


def ream(center, s=0.6, lines=True, edge=None):
    """A thick block of paper: white faces, grey page edges on both front faces."""
    iso = Iso(0, 0, s)
    body = iso.box(0, 0, 0, 1.0, 0.8, 0.5, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    if edge:
        for f in body:
            f.set_stroke(edge, 2)
    g = VGroup(body)
    if lines:
        g.add(ream_lines(iso))
    return g.move_to(center).set_z_index(6)


def ream_lines(iso, n=4):
    zs = [0.5 * (k + 1) / (n + 1) for k in range(n)]
    sw = max(2, 5 * iso.s)
    a = [Line(iso.p(0.08, 0, z), iso.p(0.92, 0, z), color=BAR2, stroke_width=sw) for z in zs]
    b = [Line(iso.p(0, 0.08, z), iso.p(0, 0.72, z), color=BAR2, stroke_width=sw) for z in zs]
    return VGroup(*a, *b)


# ─────────────── round-trip tracks ───────────────
def out_arc():
    return ArcBetweenPoints(CL_TOP, SV_TOP, angle=-0.55)


def back_arc(end=GA_TOP):
    return ArcBetweenPoints(SV_TOP, end, angle=0.6)


def track():
    return DashedVMobject(out_arc(), num_dashes=46).set_stroke(INK, 5).set_z_index(0)


def l_trip():
    return lab("round trip", [0.0, 2.85])


# ─────────────── the sandbox ───────────────
SB = Iso(1.0, -2.1, S_)
SBW, SBH, SBZ = 1.6, 0.55, 0.25
PILE0, PILE1 = 0.25, 1.35          # pile block footprint (x and y)
PILE_STEP = 0.1                  # one result = one layer


def sandbox():
    plinth = SB.box(-0.1, -0.1, 0, SBW + 0.2, SBW + 0.2, SBZ, DARK_TOP, DARK_L, DARK_R).set_z_index(0)
    back, front = SB.open_box(0, 0, SBZ, SBW, SBW, SBH)
    return VGroup(plinth, back.set_z_index(0), front.set_z_index(4))


def pile(level):
    """The results piled up inside the sandbox: a white block, one layer per result, grey page edges."""
    h = max(level, 0.001) * PILE_STEP
    w = PILE1 - PILE0
    body = SB.box(PILE0, PILE0, SBZ, w, w, h, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    for f in body:
        f.set_stroke(BOX_IN2, 3)
    ln = VGroup(*[Line(SB.p(PILE0 + 0.08, PILE0, SBZ + k * PILE_STEP), SB.p(PILE1 - 0.08, PILE0, SBZ + k * PILE_STEP),
                       color=BAR2, stroke_width=4) for k in range(1, level)] +
                [Line(SB.p(PILE0, PILE0 + 0.08, SBZ + k * PILE_STEP), SB.p(PILE0, PILE1 - 0.08, SBZ + k * PILE_STEP),
                      color=BAR2, stroke_width=4) for k in range(1, level)])
    return VGroup(body, ln).set_z_index(2)


SB_IN = SB.p(0.8, 0.8, SBZ + 0.3)                     # inside the sandbox (where things drop)
SB_RIM = SB.p(SBW + 0.25, 0.5, SBZ + SBH + 0.45)      # above its right wall (where reams come in)


def l_sandbox():
    return lab("sandbox", [1.0, -2.95])


# ─────────────── the script page, hovering over the sandbox ───────────────
PG0, PG1, PGZ = 0.2, 1.4, 2.3
CODE = [(0.45, 1.25), (0.6, 0.95), (0.6, 0.8), (0.45, 1.1), (0.6, 0.7)]   # (indent, end) per line, far to near


def script_page():
    w = PG1 - PG0
    slab = SB.box(PG0, PG0, PGZ, w, w, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    return VGroup(slab).set_z_index(5)


def code_lines():
    zt = PGZ + 0.05
    ys = [PG1 - 0.2 - k * 0.2 for k in range(len(CODE))]
    return VGroup(*[Line(SB.p(PG0 + a, y, zt), SB.p(PG0 + b, y, zt), color=BAR1, stroke_width=6)
                    for (a, b), y in zip(CODE, ys)]).set_z_index(6)




def l_script():
    return lab("script", [-0.75, 2.45])


def fan():
    src = SB.p(SBW, SBW * 0.45, SBZ + SBH) + RIGHT * 0.15
    return VGroup(*[DashedLine(src, slab_port(i), color=INK, stroke_width=5, dash_length=0.12) for i in range(3)]).set_z_index(0)


def cable():
    return DashedLine(SB.p(SBW, SBW * 0.45, SBZ + SBH) + RIGHT * 0.15, slab_port(1), color=INK, stroke_width=5, dash_length=0.12).set_z_index(0)


# ══════════════ B00: Claude, the question, and your app with three tools ══════════════
def l_q():
    return T("?", 110, INK, bold=True).move_to([-2.2, 1.2, 0])


class B00_Setup(Scene):
    def construct(self):
        cl = claude_block()
        self.play(FadeIn(cl, shift=DOWN * 1.0), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(l_claude()), run_time=0.3)
        until(self, "which engineers", lead=0.3)
        self.play(FadeIn(l_q(), scale=0.6), run_time=0.4)
        until(self, "run in your app", lead=0.4)
        sv = server_stack()
        dark = lights(GHOST)
        self.play(FadeIn(sv, shift=UP * 0.8), FadeIn(dark, shift=UP * 0.8), FadeIn(l_app()), run_time=0.6)
        for phrase, i in (("lists the team", 2), ("fetches expenses", 1), ("checks for a custom", 0)):
            until(self, phrase, lead=0.2)
            self.play(Transform(dark[i], light(i)), Flash(np.array(light(i).get_center()), color=TERRA,
                                                           line_length=0.15, flash_radius=0.25), run_time=0.4)
        done(self)


def b00_state():
    return VGroup(claude_block(), server_stack(), lights(), l_claude(), l_app())


# ══════════════ B01: one round trip ══════════════
class B01_RoundTrip(Scene):
    def construct(self):
        st = b00_state()
        l_q_obj = l_q()
        self.add(st, l_q_obj)
        g = gauge()
        self.play(FadeOut(l_q_obj), FadeIn(g, shift=UP * 0.6), FadeIn(l_context()), run_time=0.6)
        until(self, "Claude asks for a tool", lead=0.3)
        tr = track()
        s = slip(CL_TOP)
        self.play(Create(tr), FadeIn(s), FadeIn(l_trip()), run_time=0.6)
        self.play(MoveAlongPath(s, out_arc()), run_time=0.9)
        self.play(FadeOut(s, scale=0.5), run_time=0.2)
        until(self, "your app runs it", lead=0.2)
        self.play(Flash(np.array(light(1).get_center()), color=TERRA, line_length=0.18, flash_radius=0.3),
                  Indicate(st[2][1], color=TERRA, scale_factor=1.6), run_time=0.5)
        until(self, "the whole result", lead=0.3)
        r = ream(SV_TOP)
        self.play(FadeIn(r, scale=0.5), run_time=0.25)
        self.play(MoveAlongPath(r, back_arc()), run_time=0.9)
        self.play(r.animate.scale(0.4).move_to(GA.p(0.35, 0.35, GZ + GH)), run_time=0.3, rate_func=ease_in)
        self.remove(r)
        self.play(FadeIn(seg(0)), run_time=0.3)
        done(self)


def b01_state():
    return VGroup(b00_state(), gauge(), l_context(), track(), l_trip(), seg(0))


# ══════════════ B02: every line item, eight times ══════════════
BIG_C = P(0.85, 0.35)


def l_items():
    return lab("line items", [0.85, -1.4])


def l_eight():
    return lab("8 results", [0.85, 2.85])


class B02_Pile(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        self.play(FadeOut(st[4]), run_time=0.3)
        big = ream(BIG_C, s=1.9, lines=False)
        self.play(FadeIn(big, scale=0.6), run_time=0.5)
        iso_big = Iso(0, 0, 1.9)
        ln = ream_lines(iso_big, n=6)
        ln.shift(np.array(big[0].get_center()) - np.array(iso_big.box(0, 0, 0, 1.0, 0.8, 0.5).get_center()))
        ln.set_z_index(7)
        li = l_items()
        self.play(LaggedStart(*[Create(x) for x in ln], lag_ratio=0.15), FadeIn(li), run_time=1.0)
        until(self, "Eight engineers", lead=0.4)
        self.play(FadeOut(VGroup(big, ln), scale=0.3), FadeOut(li), run_time=0.4)
        self.play(FadeIn(l_eight()), run_time=0.3)
        for k in range(1, 9):
            r = ream(SV_TOP, s=0.5)
            self.add(r)
            self.play(MoveAlongPath(r, back_arc()), run_time=0.32)
            self.remove(r)
            self.add(seg(k))
        done(self)


def b02_state():
    return VGroup(b00_state(), gauge(), l_context(), track(), VGroup(*[seg(k) for k in range(9)]), l_eight())


# ══════════════ B03: switch it on per tool ══════════════
def l_callers():
    return lab("allowed callers", [4.45, 2.45])


class B03_Switch(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        base = st[0]           # claude, server, lights, Claude label, your app label
        self.play(FadeOut(VGroup(st[3], st[4], st[5], base[3])), run_time=0.5)
        sb = sandbox()
        self.play(FadeIn(sb, shift=DOWN * 0.8), FadeIn(l_sandbox()), run_time=0.6, rate_func=ease_in)
        until(self, "Turn it on per tool", lead=0.3)
        lt = base[2]
        self.play(*[Transform(lt[i], light(i, GHOST)) for i in range(3)], run_time=0.35)
        until(self, "code execution tool", lead=0.3)
        cb = cable()
        self.play(Create(cb), run_time=0.5)
        until(self, "give each tool", lead=0.2)
        self.play(FadeIn(l_callers()), run_time=0.3)
        for i in (2, 1, 0):
            self.play(Transform(lt[i], light(i)), run_time=0.3)
        done(self)


def b03_state():
    return VGroup(claude_block(), server_stack(), lights(), l_app(), gauge(), l_context(), sandbox(), l_sandbox(),
                  cable(), l_callers())


# ══════════════ B04: Claude writes a script; it runs in the sandbox ══════════════
class B04_Script(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st[9]), run_time=0.3)
        pg = script_page()
        tgt = np.array(pg.get_center())
        pg.scale(0.3).move_to(CL_TOP)
        self.add(pg)
        self.play(MoveAlongPath(pg, ArcBetweenPoints(CL_TOP, tgt, angle=-0.5)), run_time=0.9)
        self.play(pg.animate.scale(1 / 0.3), FadeIn(l_script()), run_time=0.4)
        until(self, "it runs in the sandbox", lead=0.3)
        cl = code_lines()
        self.play(LaggedStart(*[Create(x) for x in cl], lag_ratio=0.3), run_time=1.1)
        until(self, "call several at once", lead=0.3)
        fn = fan()
        self.play(FadeOut(st[8]), Create(fn), run_time=0.6)
        self.play(*[Flash(np.array(light(i).get_center()), color=TERRA, line_length=0.15, flash_radius=0.25) for i in range(3)],
                  run_time=0.5)
        done(self)


def b04_state():
    return VGroup(claude_block(), server_stack(), lights(), l_app(), gauge(), l_context(), sandbox(), l_sandbox(),
                  fan(), script_page(), code_lines(), l_script())


# ══════════════ B05: the calls go to your app; the results come back to the script ══════════════
PG_R = SB.p(PG1, PG0, PGZ) + RIGHT * 0.15


def call_arc():
    return ArcBetweenPoints(PG_R, SV_TOP, angle=-0.8)


def ret_arc():
    return ArcBetweenPoints(SV_TOP, SB_RIM, angle=0.5)


class B05_Calls(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st[8]), run_time=0.3)
        pl = pile(0)
        self.add(pl)
        s = slip(PG_R, s=0.5)
        self.play(FadeIn(s, scale=0.5), run_time=0.25)
        self.play(MoveAlongPath(s, call_arc()), run_time=0.7)
        self.play(FadeOut(s, scale=0.5), run_time=0.15)
        until(self, "Your app runs the tool", lead=0.2)
        self.play(Flash(np.array(light(1).get_center()), color=TERRA, line_length=0.18, flash_radius=0.3),
                  Indicate(st[2][1], color=TERRA, scale_factor=1.6), run_time=0.45)
        until(self, "back to the script", lead=0.4)
        level = 0
        for k in range(8):
            r = ream(SV_TOP, s=0.5)
            self.add(r)
            self.play(MoveAlongPath(r, ret_arc()), run_time=0.55 if k == 0 else 0.3)
            self.play(r.animate.scale(0.6).move_to(SB_IN), run_time=0.2 if k == 0 else 0.12, rate_func=ease_in)
            self.remove(r)
            level += 1
            self.play(Transform(pl, pile(level)), run_time=0.1)
        until(self, "context stays empty", lead=0.3)
        self.play(Indicate(st[4], color=None, scale_factor=1.06), run_time=0.5)
        done(self)


def b05_state():
    return VGroup(claude_block(), server_stack(), lights(), l_app(), gauge(), l_context(), sandbox(), l_sandbox(),
                  pile(8), script_page(), code_lines(), l_script())


# ══════════════ B06: the code does the sums; only the printout goes to Claude ══════════════
PR_Z0, PR_Z1 = 1.0, 2.05


def printout(z):
    iso = SB
    x0, x1 = 0.4, 1.2
    slab = iso.box(x0, x0, z, x1 - x0, x1 - x0, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    lines = VGroup(*[Line(iso.p(x0 + 0.12, y, z + 0.05), iso.p(x1 - 0.2, y, z + 0.05), color=BAR1, stroke_width=6)
                     for y in (1.1, 0.9, 0.7)])
    return VGroup(slab, lines).set_z_index(6)


def l_print():
    return lab("printout", [2.6, 2.1])


class B06_Filter(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        pl = st[8]
        self.play(FadeOut(VGroup(st[9], st[10], st[11])), run_time=0.4)
        until(self, "It keeps approved travel", lead=0.4)
        scan = Line(P(-0.5, 0.6, ), P(2.5, 0.6), color=TERRA, stroke_width=10).set_z_index(8)
        rt = guard(self, 1.4)
        self.add(scan)
        self.play(scan.animate.move_to(P(1.0, -1.95)), Transform(pl, pile(1)), run_time=rt, rate_func=linear)
        self.remove(scan)
        until(self, "prints just the three", lead=0.3)
        pr = printout(PR_Z0)
        self.play(FadeOut(pl), FadeIn(pr), run_time=0.3)
        lp = l_print()
        self.play(pr.animate.shift(UP * (PR_Z1 - PR_Z0)), FadeIn(lp), run_time=0.6)
        until(self, "Only that printout", lead=0.3)
        src = np.array(pr.get_center())
        self.play(MoveAlongPath(pr, ArcBetweenPoints(src, GA_TOP, angle=0.35)), run_time=0.8)
        self.play(FadeOut(lp), run_time=0.2)
        self.play(pr.animate.scale(0.4).move_to(GA.p(0.35, 0.35, GZ + GH)), run_time=0.3, rate_func=ease_in)
        self.remove(pr)
        self.play(FadeIn(seg(0, thin=True)), Indicate(st[4], color=None, scale_factor=1.06), run_time=0.5)
        done(self)


def b06_state():
    return VGroup(claude_block(), server_stack(), lights(), l_app(), gauge(), l_context(), sandbox(), l_sandbox(),
                  seg(0, thin=True))


# ══════════════ B07: the notebook's tokens ══════════════
BX0, BW, BH = -3.6, 6.0, 0.9
BY1, BY2 = -0.85, -2.3
KEEP = 15919 / 110473            # the notebook's own run: 110,473 -> 15,919 total tokens


def bar(y, w, fill=BAR1):
    return Rectangle(width=w, height=BH, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([BX0 + w / 2, y, 0])


def icons7():
    return VGroup(ream(P(BX0 - 1.3, BY1), s=0.8), printout_icon(P(BX0 - 1.3, BY2)))


def printout_icon(c):
    iso = Iso(0, 0, 1.0)
    slab = iso.box(0, 0, 0, 1.0, 0.8, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    lines = VGroup(*[Line(iso.p(0.12, y, 0.05), iso.p(0.75, y, 0.05), color=BAR1, stroke_width=5) for y in (0.6, 0.4, 0.2)])
    return VGroup(slab, lines).move_to(c)


def l_tokens():
    return lab("total tokens", [BX0 + 1.4, 0.15], 46)


def l_n1():
    return lab("110,473", [BX0 + BW + 1.3, BY1], 44)


def l_n2():
    return lab("15,919", [BX0 + BW * KEEP + 1.05, BY2], 44)


def l_856():
    return T("85.6%", 150, INK, bold=True).move_to([3.1, 2.3, 0])


def l_per():
    return lab("per Anthropic's notebook", [3.1, 1.05], 38)


def gap7():
    w = BW * (1 - KEEP)
    return Rectangle(width=w - 0.08, height=BH, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(
        [BX0 + BW * KEEP + 0.04 + (w - 0.08) / 2, BY2, 0]).set_z_index(-1)


class B07_Tokens(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        b1, b2 = bar(BY1, BW), bar(BY2, BW)
        ic = icons7()
        self.play(FadeIn(ic[0], shift=DOWN * 0.4), FadeIn(l_tokens()), run_time=0.5)
        until(self, "the normal way", lead=0.4)
        self.play(GrowFromEdge(b1, LEFT), run_time=0.6)
        self.play(FadeIn(l_n1()), run_time=0.3)
        until(self, "the script, under", lead=0.3)
        self.play(FadeIn(ic[1]), GrowFromEdge(b2, LEFT), run_time=0.5)
        g = gap7()
        self.add(g)
        self.play(Transform(b2, bar(BY2, BW * KEEP)), run_time=0.8)
        self.play(FadeIn(l_n2()), run_time=0.3)
        until(self, "Eighty-five point six", lead=0.3)
        self.play(FadeIn(l_856()), run_time=0.4)
        self.play(FadeIn(l_per()), run_time=0.35)
        done(self)


def b07_state():
    return VGroup(bar(BY1, BW), bar(BY2, BW * KEEP), gap7(), icons7(), l_tokens(), l_n1(), l_n2(), l_856(), l_per())


# ══════════════ B08: where it pays, and where it doesn't ══════════════
def l_many():
    return lab("many calls", [1.0, 2.35])


def l_step():
    return lab("step by step", [0.0, 2.85])


class B08_Fit(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        cl, g, sb, sv, lt = claude_block(), gauge(), sandbox(), server_stack(), lights()
        self.play(FadeIn(VGroup(cl, g, seg(0, thin=True), sb, sv, lt), shift=UP * 0.4), run_time=0.6)
        fn = fan()
        lm = l_many()
        self.play(Create(fn), FadeIn(lm), run_time=0.6)
        ck = check(2.75, 1.25, s=0.28)
        self.play(Create(ck), *[Flash(np.array(light(i).get_center()), color=TERRA, line_length=0.15, flash_radius=0.25)
                                for i in range(3)], run_time=0.5)
        until(self, "each step needs Claude", lead=0.4)
        self.play(FadeOut(fn), FadeOut(ck), FadeOut(lm), sb.animate.set_opacity(0.25), run_time=0.5)
        tr = track()
        self.play(Create(tr), FadeIn(l_step()), run_time=0.5)
        s = slip(CL_TOP)
        self.add(s)
        self.play(MoveAlongPath(s, out_arc()), run_time=0.8)
        self.remove(s)
        r = ream(SV_TOP, s=0.5)
        self.add(r)
        self.play(MoveAlongPath(r, back_arc()), run_time=0.8)
        self.remove(r)
        self.add(seg(1))
        until(self, "safe to run again", lead=0.4)
        self.play(*[Indicate(lt[i], color=TERRA, scale_factor=1.6) for i in range(3)], run_time=0.6)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Setup, B01_RoundTrip, B02_Pile, B03_Switch, B04_Script, B05_Calls, B06_Filter, B07_Tokens, B08_Fit):
    _cls.play = ST.play
