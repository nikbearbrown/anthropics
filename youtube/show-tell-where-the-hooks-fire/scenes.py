"""
Manim scenes for show-tell-where-the-hooks-fire (show-tell skill, card #25, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Claude Code hooks, from anthropics/claude-code (plugin-dev hook-development SKILL.md; examples/hooks/
bash_command_validator_example.py) and the current hooks reference (code.claude.com/docs/en/hooks):
a session is a belt; Claude is a dark block on it; the tool is a machine at the end of two lanes.
Hooks are gate arches that Claude Code passes through: SessionStart, UserPromptSubmit and Stop on the
belt; PreToolUse and PostToolUse on the lanes; PreCompact as a press beside Claude. A matcher in a
settings file picks the tools; the hook gets a JSON note on stdin; exit 2 drops the door; the
example's grep call is blocked and Claude can retry with rg; exit 2 differs by event, ending on Stop.
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












# ═════════════════════════════ the film: where the hooks fire ═════════════════════════════
# Cast: the SESSION as a pale main BELT running right-up (dark-kraft edges, ghost dashes); Claude as a dark BLOCK on
# it (a light on its top face); the tool as a dark MACHINE (the kit's server stack) at the end of two thin spur LANES
# that run toward the viewer (out lane: calls; back lane: results); hooks as ink GATE arches across the belt or a lane,
# each with a lamp (ghost; terracotta when the hook fires) and a kraft DOOR that drops to block; SLIPS riding the belts
# (white; terracotta dot); a small NOTE (stderr) that arcs back to Claude; a script PAGE card beside the PreToolUse
# gate; a kraft PRESS behind the belt (compaction); a SETTINGS card; a JSON card.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
BELT = "#E6DFD3"

S = 0.78
W = Iso(-4.1, -2.6, S)           # the one rig
BW = 1.5                          # main belt width (y)
BL = 11.5                         # main belt length (x)
H = 1.9                           # gate height
OUT = (5.95, 6.65)                # out lane x range (calls, toward the tool)
BACK = (6.85, 7.55)               # back lane x range (results, back to Claude)
LANE_Y0 = -4.5                    # lanes run from y = LANE_Y0 up to y = 0
CL = (5.9, 0.2, 0.0, 1.6, 1.1, 0.9)          # Claude's block on the belt: x0, y0, z0, w, d, h
MX, MY, MW, MD = 5.85, -5.9, 1.8, 1.4        # the tool machine
SLAB, NSL = 0.4, 3
G_SS, G_UPS, G_STOP = 1.0, 3.7, 9.2          # main-belt gates (x)
G_PRE, G_POST = -1.9, -3.2                   # lane gates (y): PreToolUse on OUT, PostToolUse on BACK


def strip_x(iso, x0, x1, y0, y1, th=0.25):
    """A flat belt running along x: top, front side (y = y0) and start end (x = x0)."""
    top = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], BELT, stroke=DEV_EDGE, sw=2)
    side = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y0, -th), (x0, y0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)
    end = iso.quad([(x0, y0, 0), (x0, y1, 0), (x0, y1, -th), (x0, y0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    ym = (y0 + y1) / 2
    mid = DashedLine(iso.p(x0 + 0.3, ym, 0), iso.p(x1 - 0.3, ym, 0), color=GHOST, stroke_width=3, dash_length=0.12)
    return VGroup(side, end, top, mid)


def strip_y(iso, x0, x1, y0, y1, th=0.25):
    """A flat lane running along y (toward the viewer as y falls): top and left side (x = x0)."""
    top = iso.quad([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], BELT, stroke=DEV_EDGE, sw=2)
    side = iso.quad([(x0, y0, 0), (x0, y1, 0), (x0, y1, -th), (x0, y0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    xm = (x0 + x1) / 2
    mid = DashedLine(iso.p(xm, y0 + 0.3, 0), iso.p(xm, y1 - 0.3, 0), color=GHOST, stroke_width=3, dash_length=0.12)
    return VGroup(side, top, mid)


def main_belt():
    g = strip_x(W, 0.0, BL, 0.0, BW)
    g.set_z_index(-3)
    return g


def lanes():
    g = VGroup(strip_y(W, OUT[0], OUT[1], LANE_Y0, 0.0), strip_y(W, BACK[0], BACK[1], LANE_Y0, 0.0))
    g.set_z_index(-2)
    return g


def claude_block():
    """(block, light): Claude's dark block on the belt and the light on its top face."""
    x0, y0, z0, w, d, h = CL
    blk = W.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
    blk.set_z_index(3)
    light = Dot(W.p(x0 + w / 2, y0 + d / 2, z0 + h), radius=0.11, color=GHOST).set_z_index(4)
    return blk, light


def machine():
    """(stack, lights): the tool machine at the lanes' end; lights start ghost."""
    sh = W.quad([(MX - 0.2, MY - 0.35, 0), (MX + MW + 0.25, MY - 0.35, 0), (MX + MW + 0.25, MY + MD, 0), (MX - 0.2, MY + MD, 0)], SHADOW, sw=0)
    sh.set_z_index(-2)
    stack = VGroup(*[W.box(MX, MY, i * (SLAB + 0.04), MW, MD, SLAB, DARK_TOP, DARK_L, DARK_R) for i in range(NSL)])
    lights = VGroup(*[Dot(W.p(MX + 0.35 + 0.4 * k, MY, i * (SLAB + 0.04) + SLAB / 2), radius=0.07, color=GHOST)
                      for i in range(NSL) for k in range(2)])
    stack.set_z_index(5); lights.set_z_index(6)
    return VGroup(sh, stack), lights


def run_lights(lights):
    return VGroup(*[Dot(np.array(l.get_center()), radius=0.07, color=TERRA).set_z_index(7) for l in lights])


def claude_label():
    return T("Claude", 40).move_to([0.05, 2.3, 0])


def tool_label():
    return T("tool", 40).move_to([5.7, -1.35, 0])


# ─────────────── gates ───────────────
def gate_main(g):
    """A gate arch across the main belt at x = g: (back post + crossbar, front post, lamp)."""
    back = VGroup(Line(W.p(g, BW + 0.1, 0), W.p(g, BW + 0.1, H), color=INK, stroke_width=9),
                  Line(W.p(g, BW + 0.1, H), W.p(g, -0.1, H), color=INK, stroke_width=9))
    front = Line(W.p(g, -0.1, 0), W.p(g, -0.1, H), color=INK, stroke_width=9)
    lamp = Dot(W.p(g, BW / 2, H) + UP * 0.13, radius=0.11, color=GHOST)
    back.set_z_index(0); front.set_z_index(8); lamp.set_z_index(9)
    return VGroup(back, front, lamp)


def gate_lane(g, xr):
    """A gate arch across a lane at y = g (lane x range xr)."""
    x0, x1 = xr[0] - 0.1, xr[1] + 0.1
    back = VGroup(Line(W.p(x1, g, 0), W.p(x1, g, H), color=INK, stroke_width=9),
                  Line(W.p(x1, g, H), W.p(x0, g, H), color=INK, stroke_width=9))
    front = Line(W.p(x0, g, 0), W.p(x0, g, H), color=INK, stroke_width=9)
    lamp = Dot(W.p((x0 + x1) / 2, g, H) + UP * 0.13, radius=0.11, color=GHOST)
    back.set_z_index(0); front.set_z_index(8); lamp.set_z_index(9)
    return VGroup(back, front, lamp)


def g_pre():
    return gate_lane(G_PRE, OUT)


def g_post():
    return gate_lane(G_POST, BACK)


def door_main(g):
    d = W.quad([(g, 0.0, 0.03), (g, BW, 0.03), (g, BW, H - 0.08), (g, 0.0, H - 0.08)], BOX_L, stroke=INK, sw=3)
    return d.set_z_index(6)


def door_lane(g, xr):
    d = W.quad([(xr[0], g, 0.03), (xr[1], g, 0.03), (xr[1], g, H - 0.08), (xr[0], g, H - 0.08)], BOX_R, stroke=INK, sw=3)
    return d.set_z_index(6)


def lit(lamp):
    """A terracotta dot over a ghost lamp (an added shape)."""
    return Dot(np.array(lamp.get_center()), radius=0.11, color=TERRA).set_z_index(10)


# ─────────────── slips, notes, cards ───────────────
def slip(x0, y0, w, d, z0=0.02, result=False):
    """A slip lying flat: white slab, DIM outline, two lines, a terracotta dot."""
    slab = W.box(x0, y0, z0, w, d, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    for f in slab:
        f.set_stroke(DIM, 1.5)
    zt = z0 + 0.05
    col = BAR1 if result else BAR2
    if w >= d:
        lines = VGroup(*[Line(W.p(x0 + 0.35 * w, y0 + d * f, zt), W.p(x0 + (0.88 - 0.2 * k) * w, y0 + d * f, zt), color=col, stroke_width=4)
                         for k, f in enumerate((0.35, 0.68))])
        dot = Dot(W.p(x0 + 0.17 * w, y0 + d * 0.35, zt), radius=0.07, color=TERRA)
    else:
        lines = VGroup(*[Line(W.p(x0 + w * f, y0 + 0.12 * d, zt), W.p(x0 + w * f, y0 + (0.62 - 0.15 * k) * d, zt), color=col, stroke_width=4)
                         for k, f in enumerate((0.35, 0.68))])
        dot = Dot(W.p(x0 + w * 0.5, y0 + 0.83 * d, zt), radius=0.07, color=TERRA)
    return VGroup(slab, lines, dot)


def main_slip(x0, result=False):
    return slip(x0, 0.35, 0.9, 0.8, result=result).set_z_index(2)


def out_slip(y0):
    return slip(OUT[0] + 0.08, y0, 0.54, 0.75).set_z_index(2)


def back_slip(y0):
    return slip(BACK[0] + 0.08, y0, 0.54, 0.75, result=True).set_z_index(2)


def along_x(m, dx):
    return m.animate.shift(W.v(dx, 0, 0))


def along_y(m, dy):
    return m.animate.shift(W.v(0, dy, 0))


def note(c):
    """The stderr note: a small white card with two ink lines and a terracotta dot."""
    c = np.array([float(c[0]), float(c[1]), 0.0])
    body = RoundedRectangle(width=0.9, height=0.6, corner_radius=0.06, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DEV_EDGE, stroke_width=3).move_to(c)
    lines = VGroup(*[Line(c + np.array([-0.2, 0.1 - 0.2 * k, 0]), c + np.array([0.32 - 0.12 * k, 0.1 - 0.2 * k, 0]),
                          color=BAR1, stroke_width=5) for k in range(2)])
    dot = Dot(c + np.array([-0.3, 0.1, 0]), radius=0.06, color=TERRA)
    return VGroup(body, lines, dot).set_z_index(11)


def fly_note(self, src, rt=0.8):
    """A note arcs from src to Claude's light; returns the note (left on screen until faded)."""
    n = note(src)
    dst = np.array(claude_block()[1].get_center()) + UP * 0.35 + LEFT * 0.9
    rt = guard(self, rt)
    self.add(n)
    self.play(MoveAlongPath(n, ArcBetweenPoints(np.array(src), dst, angle=-0.9)), run_time=rt)
    return n


SCRIPT_C = np.array([4.7, 1.3, 0])


def script_card(c=SCRIPT_C):
    """Your command, as a page: white card, dark top bar, grey code lines."""
    body = RoundedRectangle(width=1.7, height=1.5, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(c)
    bar = Rectangle(width=1.64, height=0.26, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * 0.6)
    lines = VGroup(*[Line(c + np.array([-0.6 + 0.15 * (k % 2), 0.2 - 0.26 * k, 0]), c + np.array([0.55 - 0.25 * (k % 3), 0.2 - 0.26 * k, 0]),
                          color=BAR1, stroke_width=6) for k in range(4)])
    return VGroup(body, bar, lines).set_z_index(9)


def script_tie(c=SCRIPT_C):
    """A dashed ink tie from the card's left edge to the PreToolUse gate's back post (clear of labels)."""
    post = W.p(OUT[1] + 0.1, G_PRE, H * 0.7)
    return DashedLine(c + LEFT * 0.95, post + RIGHT * 0.12, color=INK, stroke_width=5, dash_length=0.12).set_z_index(8)


# ─────────────── the base cast, and continuity end-states ───────────────
def base(lit_claude=False):
    b, ln = main_belt(), lanes()
    blk, light = claude_block()
    if lit_claude:
        light.set_color(TERRA)
    mach, lights = machine()
    return VGroup(b, ln), VGroup(blk), light, mach, lights, claude_label(), tool_label()


def main_gates():
    return gate_main(G_SS), gate_main(G_UPS), gate_main(G_STOP)


LBL = {  # label anchors (screen), beside each gate
    "SessionStart": [-4.75, 0.6, 0], "UserPromptSubmit": [-2.9, 1.3, 0], "Stop": [3.2, 2.85, 0],
    "PreToolUse": [-0.2, -1.3, 0], "PostToolUse": [4.5, -0.1, 0], "PreCompact": [-2.5, 1.75, 0],
}


def lbl(name):
    return T(name, 38).move_to(LBL[name])


# PreCompact press: behind the belt, left of Claude
PX, PY = 2.2, 3.6


def press_base():
    sh = W.quad([(PX - 0.15, PY - 0.3, 0), (PX + 1.45, PY - 0.3, 0), (PX + 1.45, PY + 1.0, 0), (PX - 0.15, PY + 1.0, 0)], SHADOW, sw=0)
    tb, tf = W.open_box(PX, PY, 0.0, 1.2, 1.0, 0.35)
    stack = VGroup(*[slip(PX + 0.15, PY + 0.12, 0.9, 0.75, z0=0.05 + 0.08 * k) for k in range(3)])
    sh.set_z_index(-2); tb.set_z_index(1); stack.set_z_index(1); tf.set_z_index(2)
    return VGroup(sh, tb, stack, tf)


def press_plate(z):
    p = W.box(PX - 0.05, PY - 0.05, z, 1.3, 1.1, 0.18, BOX_TOP, BOX_L, BOX_R)
    return p.set_z_index(3)


def press_lamp(z):
    return Dot(W.p(PX + 0.6, PY + 0.5, z + 0.18) + UP * 0.02, radius=0.1, color=GHOST).set_z_index(4)


def full_rig():
    """B03's end: all five gates and the press, lamps ghost."""
    ss, ups, stp = main_gates()
    return VGroup(ss, ups, stp, g_pre(), g_post())


# ─────────────── B00: the session as a belt ───────────────
class B00_Belt(Scene):
    def construct(self):
        b = main_belt()
        self.play(FadeIn(b[0:3]), run_time=0.4)
        self.play(Create(b[3]), run_time=0.4)
        sl = T("session", 40).move_to([-2.4, -2.85, 0])
        blk, light = claude_block()
        g = VGroup(blk, light)
        g.shift(UP * 4)
        self.add(g)
        self.play(g.animate.shift(DOWN * 4), FadeIn(sl), run_time=0.6, rate_func=ease_in)
        self.play(FadeIn(claude_label()), run_time=0.3)
        until(self, "Your prompt rides in", lead=0.3)
        p = main_slip(0.3)
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(p), run_time=rt)
        rt = guard(self, 0.85)
        self.play(along_x(p, 4.3), run_time=rt, rate_func=linear)
        self.play(FadeOut(p), light.animate.set_color(TERRA), run_time=0.3)
        until(self, "Claude calls a tool", lead=0.4)
        ln = lanes()
        mach, lights = machine()
        rt = guard(self, 0.6)
        self.play(FadeIn(ln), FadeIn(mach[0]), LaggedStart(*[GrowFromEdge(s, DOWN) for s in mach[1]], lag_ratio=0.25), run_time=rt)
        self.add(lights)
        self.play(FadeIn(tool_label()), run_time=0.3)
        c = out_slip(-0.95)
        self.play(GrowFromCenter(c), run_time=0.25)
        rt = guard(self, 0.7)
        self.play(along_y(c, -3.3), run_time=rt, rate_func=linear)
        self.remove(c)
        on = run_lights(lights)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.1), run_time=0.4)
        until(self, "the result rides back", lead=0.3)
        r = back_slip(-4.3)
        self.add(r)
        rt = guard(self, 0.7)
        self.play(FadeOut(on), along_y(r, 3.35), run_time=rt, rate_func=linear)
        self.play(FadeOut(r), Flash(np.array(light.get_center()), color=TERRA, line_length=0.16, flash_radius=0.28), run_time=0.35)
        until(self, "Then Claude answers", lead=0.3)
        a = main_slip(7.6, result=True)
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(a), run_time=rt)
        rt = guard(self, 0.7)
        self.play(along_x(a, 2.6), run_time=rt, rate_func=linear)
        until(self, "the turn stops", lead=0.3)
        stop = Line(W.p(BL - 0.15, -0.1, 0.02), W.p(BL - 0.15, BW + 0.1, 0.02), color=INK, stroke_width=10).set_z_index(3)
        self.play(Create(stop), light.animate.set_color(GHOST), run_time=0.4)
        done(self)


def b00_end():
    stop = Line(W.p(BL - 0.15, -0.1, 0.02), W.p(BL - 0.15, BW + 0.1, 0.02), color=INK, stroke_width=10).set_z_index(3)
    return VGroup(main_slip(10.2, result=True), stop, T("session", 40).move_to([-2.4, -2.85, 0]))


# ─────────────── B01: a hook is a checkpoint; Claude Code runs it every pass ───────────────
class B01_Checkpoint(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        carry = b00_end()
        self.add(belts, blk, light, mach, lights, cl, tl, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "A hook is a checkpoint", lead=0.3)
        gp = g_pre()
        rt = guard(self, 0.7)
        self.play(Create(gp[0]), Create(gp[1]), run_time=rt)
        hk = T("hook", 40).move_to(LBL["PreToolUse"])
        self.play(FadeIn(gp[2]), FadeIn(hk), run_time=0.3)
        until(self, "a command you attach", lead=0.3)
        sc = script_card()
        tie = script_tie()
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(sc), run_time=rt)
        self.play(Create(tie), run_time=0.35)
        yc = T("your command", 38).next_to(sc, UP, buff=0.3)
        self.play(FadeIn(yc), run_time=0.3)
        until(self, "Every time the session passes", lead=0.4)
        for k in range(2):
            c = out_slip(-0.95)
            rt = guard(self, 0.25)
            self.play(GrowFromCenter(c), run_time=rt)
            rt = guard(self, 0.55)
            self.play(along_y(c, -1.4), run_time=rt, rate_func=linear)
            on = lit(gp[2])
            rt = guard(self, 0.3)
            self.play(GrowFromCenter(on), Indicate(sc, color=None, scale_factor=1.06), run_time=rt)
            rt = guard(self, 0.6)
            self.play(along_y(c, -1.9), run_time=rt, rate_func=linear)
            self.remove(c)
            if k == 0:
                self.play(FadeOut(on), run_time=0.2)
        until(self, "Claude doesn't choose", lead=0.3)
        ring = Circle(radius=0.28, color=INK, stroke_width=5).move_to(np.array(light.get_center())).set_z_index(5)
        self.play(Create(ring), run_time=0.4)
        done(self)


def b01_end():
    gp = g_pre()
    on = lit(gp[2])
    sc = script_card()
    return gp, VGroup(on, sc, script_tie(), T("your command", 38).next_to(sc, UP, buff=0.3), T("hook", 40).move_to(LBL["PreToolUse"]),
                      Circle(radius=0.28, color=INK, stroke_width=5).move_to(np.array(claude_block()[1].get_center())).set_z_index(5))


# ─────────────── B02: three events that follow the turn ───────────────
class B02_Turn(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        gp, carry = b01_end()
        self.add(belts, blk, light, mach, lights, cl, tl, gp, carry)
        self.play(FadeOut(carry), run_time=0.4)
        ss, ups, stp = main_gates()
        until(self, "Session start", lead=0.4)
        rt = guard(self, 0.6)
        self.play(Create(ss[0]), Create(ss[1]), FadeIn(ss[2]), run_time=rt)
        l1 = lbl("SessionStart")
        self.play(FadeIn(l1), GrowFromCenter(lit(ss[2])), run_time=0.35)
        until(self, "User prompt submit", lead=0.4)
        rt = guard(self, 0.6)
        self.play(Create(ups[0]), Create(ups[1]), FadeIn(ups[2]), run_time=rt)
        l2 = lbl("UserPromptSubmit")
        self.play(FadeIn(l2), run_time=0.3)
        until(self, "when you send a prompt", lead=0.3)
        p = main_slip(0.3)
        rt = guard(self, 0.25)
        self.play(GrowFromCenter(p), run_time=rt)
        rt = guard(self, 0.7)
        self.play(along_x(p, 2.2), run_time=rt, rate_func=linear)
        on2 = lit(ups[2])
        self.play(GrowFromCenter(on2), run_time=0.25)
        until(self, "before Claude reads it", lead=0.3)
        rt = guard(self, 0.6)
        self.play(along_x(p, 2.0), run_time=rt, rate_func=linear)
        self.play(FadeOut(p), light.animate.set_color(TERRA), run_time=0.3)
        until(self, "And stop", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Create(stp[0]), Create(stp[1]), FadeIn(stp[2]), run_time=rt)
        l3 = lbl("Stop")
        self.play(FadeIn(l3), run_time=0.3)
        until(self, "finishes responding", lead=0.4)
        a = main_slip(7.6, result=True)
        self.add(a)
        rt = guard(self, 0.9)
        self.play(along_x(a, 2.6), light.animate.set_color(GHOST), run_time=rt, rate_func=linear)
        self.play(GrowFromCenter(lit(stp[2])), run_time=0.25)
        done(self)


def b02_end():
    ss, ups, stp = main_gates()
    extra = VGroup(lit(ss[2]), lit(ups[2]), lit(stp[2]), lbl("SessionStart"), lbl("UserPromptSubmit"), lbl("Stop"),
                   main_slip(10.2, result=True))
    return VGroup(ss, ups, stp), extra


# ─────────────── B03: two on every tool call; PreCompact; the docs list more ───────────────
class B03_Tools(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        gates, carry = b02_end()
        gp = g_pre()
        self.add(belts, blk, light, mach, lights, cl, tl, gates, gp, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "Two fire on every tool call", lead=0.3)
        gq = g_post()
        rt = guard(self, 0.6)
        self.play(Create(gq[0]), Create(gq[1]), FadeIn(gq[2]), run_time=rt)
        until(self, "pre tool use", lead=0.3)
        l1 = lbl("PreToolUse")
        c = out_slip(-0.95)
        rt = guard(self, 0.3)
        self.play(FadeIn(l1), GrowFromCenter(c), run_time=rt)
        rt = guard(self, 0.5)
        self.play(along_y(c, -1.4), run_time=rt, rate_func=linear)
        on1 = lit(gp[2])
        self.play(GrowFromCenter(on1), run_time=0.2)
        rt = guard(self, 0.6)
        self.play(along_y(c, -1.9), run_time=rt, rate_func=linear)
        self.remove(c)
        until(self, "post tool use", lead=0.3)
        on = run_lights(lights)
        l2 = lbl("PostToolUse")
        rt = guard(self, 0.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.1), FadeIn(l2), run_time=rt)
        r = back_slip(-4.3)
        self.add(r)
        rt = guard(self, 0.5)
        self.play(along_y(r, 1.25), run_time=rt, rate_func=linear)
        on2 = lit(gq[2])
        self.play(GrowFromCenter(on2), run_time=0.2)
        rt = guard(self, 0.6)
        self.play(along_y(r, 2.1), FadeOut(on), run_time=rt, rate_func=linear)
        self.play(FadeOut(r), run_time=0.2)
        until(self, "Pre compact", lead=0.4)
        pb = press_base()
        plate, plamp = press_plate(1.5), press_lamp(1.5)
        rt = guard(self, 0.6)
        self.play(FadeIn(pb), FadeIn(plate), FadeIn(plamp), run_time=rt)
        l3 = lbl("PreCompact")
        self.play(FadeIn(l3), run_time=0.3)
        until(self, "is compacted", lead=0.5)
        rt = guard(self, 0.6)
        self.play(VGroup(plate, plamp).animate.shift(W.v(0, 0, -0.95)), run_time=rt)
        self.play(GrowFromCenter(lit(plamp)), run_time=0.25)
        until(self, "The docs list more", lead=0.3)
        more = VGroup(*[Line(W.p(x, BW + 0.1, 0), W.p(x, BW + 0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)],
                      *[Line(W.p(x, -0.1, 0), W.p(x, -0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)],
                      *[Line(W.p(x, BW + 0.1, H * 0.6), W.p(x, -0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)])
        self.play(Create(more), run_time=0.5)
        done(self)


def b03_carry():
    """B03's labels and lit lamps (faded at the start of B04)."""
    return VGroup(lbl("PreToolUse"), lbl("PostToolUse"), lbl("PreCompact"), lit(g_pre()[2]), lit(g_post()[2]), lit(press_lamp(0.55)),
                  press_base(), press_plate(0.55), press_lamp(0.55),
                  VGroup(*[Line(W.p(x, BW + 0.1, 0), W.p(x, BW + 0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)],
                         *[Line(W.p(x, -0.1, 0), W.p(x, -0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)],
                         *[Line(W.p(x, BW + 0.1, H * 0.6), W.p(x, -0.1, H * 0.6), color=GHOST, stroke_width=7) for x in (10.2, 10.8)]))


# ─────────────── B04: a settings file; a matcher ───────────────
SET_C = np.array([-4.6, 1.95, 0])


def settings_card():
    body = RoundedRectangle(width=2.3, height=1.9, corner_radius=0.1, fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(SET_C)
    bar = Rectangle(width=2.24, height=0.3, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(SET_C + UP * 0.78)
    lines = VGroup(*[Line(SET_C + np.array([-0.85 + 0.2 * (k in (1, 2)), 0.35 - 0.3 * k, 0]), SET_C + np.array([0.8 - 0.3 * (k % 2), 0.35 - 0.3 * k, 0]),
                          color=BAR1, stroke_width=6) for k in range(4)])
    return VGroup(body, bar, lines).set_z_index(9)


def matcher_mark():
    y = SET_C[1] + 0.35 - 0.3 * 2
    return VGroup(Dot(SET_C + np.array([-0.95, y - SET_C[1], 0]), radius=0.08, color=TERRA),
                  Line(SET_C + np.array([-0.62, y - SET_C[1] - 0.12, 0]), SET_C + np.array([0.55, y - SET_C[1] - 0.12, 0]), color=INK, stroke_width=4)).set_z_index(10)


def settings_thread():
    a = SET_C + np.array([0.6, -1.05, 0])
    z = np.array(W.p(OUT[0] - 0.1, G_PRE, H * 0.55)) + LEFT * 0.12
    return ArcBetweenPoints(a, z, angle=1.6).set_stroke(INK, 5).set_z_index(8)


class B04_Matcher(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        rig = full_rig()
        carry = b03_carry()
        self.add(belts, blk, light, mach, lights, cl, tl, rig, carry)
        self.play(FadeOut(carry), run_time=0.4)
        until(self, "Hooks live in a settings file", lead=0.3)
        card = settings_card()
        card.shift(LEFT * 3)
        self.add(card)
        rt = guard(self, 0.6)
        self.play(card.animate.shift(RIGHT * 3), run_time=rt)
        sl = T("settings.json", 38).next_to(settings_card(), RIGHT, buff=0.3).align_to(settings_card(), UP)
        self.play(FadeIn(sl), run_time=0.3)
        until(self, "under their event", lead=0.3)
        pl = lbl("PreToolUse")
        on0 = lit(rig[3][2])
        rt = guard(self, 0.4)
        self.play(FadeIn(pl), GrowFromCenter(on0), run_time=rt)
        self.play(FadeOut(on0), run_time=0.25)
        until(self, "A matcher picks", lead=0.3)
        mm = matcher_mark()
        self.play(GrowFromCenter(mm[0]), Create(mm[1]), run_time=0.4)
        until(self, "a Bash call trips it", lead=0.5)
        gp = rig[3]
        c = out_slip(-0.95)
        rt = guard(self, 0.25)
        self.play(GrowFromCenter(c), run_time=rt)
        bl = T("Bash", 38).move_to(EXIT_AT)
        rt = guard(self, 0.5)
        self.play(along_y(c, -1.4), FadeIn(bl), run_time=rt, rate_func=linear)
        on = lit(gp[2])
        self.play(GrowFromCenter(on), Flash(np.array(gp[2].get_center()), color=TERRA, line_length=0.14, flash_radius=0.26), run_time=0.35)
        rt = guard(self, 0.5)
        self.play(along_y(c, -1.9), run_time=rt, rate_func=linear)
        self.remove(c)
        until(self, "An Edit call", lead=0.3)
        e = out_slip(-0.95)
        el = T("Edit", 38).move_to(EXIT_AT)
        rt = guard(self, 0.3)
        self.play(FadeOut(on), FadeOut(bl), GrowFromCenter(e), run_time=rt)
        self.play(FadeIn(el), run_time=0.25)
        rt = guard(self, 1.1)
        self.play(along_y(e, -3.3), run_time=rt, rate_func=linear)
        self.remove(e)
        done(self)


def b04_carry():
    return VGroup(settings_card(), T("settings.json", 38).next_to(settings_card(), RIGHT, buff=0.3).align_to(settings_card(), UP), lbl("PreToolUse"), matcher_mark(),
                  T("Edit", 38).move_to(EXIT_AT))


# ─────────────── B05: a JSON note on stdin ───────────────
JS_C = np.array([-5.0, 1.95, 0])
ROW_Y = [0.8, 0.27, -0.27, -0.8]


def json_card():
    body = RoundedRectangle(width=2.1, height=2.3, corner_radius=0.1, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(JS_C)
    return body.set_z_index(9)


def json_row(k, long=False):
    y = ROW_Y[k]
    key = Line(JS_C + np.array([-0.8, y, 0]), JS_C + np.array([-0.3, y, 0]), color=DARK_TOP, stroke_width=9)
    val = Line(JS_C + np.array([-0.15, y, 0]), JS_C + np.array([0.35 if not long else 0.7, y, 0]), color=BAR1, stroke_width=9)
    return VGroup(key, val).set_z_index(10)


def json_tick(k):
    y = JS_C[1] + ROW_Y[k]
    return Line([JS_C[0] + 1.2, y, 0], [JS_C[0] + 1.55, y, 0], color=INK, stroke_width=5).set_z_index(10)


def json_label(k, s):
    return T(s, 34).next_to(json_tick(k), RIGHT, buff=0.3)


class B05_Stdin(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        rig = full_rig()
        carry = b04_carry()
        self.add(belts, blk, light, mach, lights, cl, tl, rig, carry)
        self.play(FadeOut(carry), run_time=0.4)
        gp = rig[3]
        until(self, "When a hook fires", lead=0.3)
        c = out_slip(-0.95)
        self.play(GrowFromCenter(c), run_time=0.25)
        self.play(along_y(c, -0.75), run_time=0.5, rate_func=linear)
        on = lit(gp[2])
        self.play(GrowFromCenter(on), run_time=0.25)
        until(self, "a JSON note", lead=0.3)
        card = json_card()
        rt = guard(self, 0.6)
        self.play(GrowFromPoint(card, np.array(gp[2].get_center())), run_time=rt)
        sl = T("stdin", 38).next_to(json_card(), RIGHT, buff=0.3).align_to(json_card(), UP)
        self.play(FadeIn(sl), run_time=0.3)
        until(self, "the session", lead=0.3)
        rt = guard(self, 0.3)
        self.play(Create(json_row(0)), run_time=rt)
        until(self, "the event's name", lead=0.3)
        rt = guard(self, 0.3)
        self.play(Create(json_row(1)), run_time=rt)
        until(self, "the tool's name", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Create(json_row(2)), Create(json_tick(2)), FadeIn(json_label(2, "tool_name")), run_time=rt)
        until(self, "and its input", lead=0.3)
        r3 = json_row(3)
        rt = guard(self, 0.5)
        self.play(Create(r3), Create(json_tick(3)), FadeIn(json_label(3, "tool_input")), run_time=rt)
        until(self, "the exact command", lead=0.4)
        ext = Line(JS_C + np.array([0.35, ROW_Y[3], 0]), JS_C + np.array([0.7, ROW_Y[3], 0]), color=BAR1, stroke_width=9).set_z_index(10)
        dot = Dot(JS_C + np.array([0.85, ROW_Y[3], 0]), radius=0.08, color=TERRA).set_z_index(10)
        self.play(Create(ext), GrowFromCenter(dot), Indicate(c, color=None, scale_factor=1.1), run_time=0.5)
        done(self)


def b05_carry():
    rows = VGroup(json_row(0), json_row(1), json_row(2), json_row(3, long=True))
    return VGroup(json_card(), rows, T("stdin", 38).next_to(json_card(), RIGHT, buff=0.3).align_to(json_card(), UP), json_tick(2), json_tick(3),
                  json_label(2, "tool_name"), json_label(3, "tool_input"), Dot(JS_C + np.array([0.85, ROW_Y[3], 0]), radius=0.08, color=TERRA).set_z_index(10),
                  out_slip(-1.7), lit(g_pre()[2]))


# ─────────────── B06: the exit code ───────────────
EXIT_AT = [0.3, -2.4, 0]


class B06_Exit(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        rig = full_rig()
        carry = b05_carry()
        self.add(belts, blk, light, mach, lights, cl, tl, rig, carry)
        self.play(FadeOut(carry), run_time=0.4)
        gp = rig[3]
        until(self, "Zero", lead=0.4)
        c = out_slip(-0.95)
        self.play(GrowFromCenter(c), run_time=0.2)
        rt = guard(self, 0.45)
        self.play(along_y(c, -0.75), run_time=rt, rate_func=linear)
        on = lit(gp[2])
        e0 = T("exit 0", 38).move_to(EXIT_AT)
        self.play(GrowFromCenter(on), FadeIn(e0), run_time=0.3)
        rt = guard(self, 0.6)
        self.play(along_y(c, -2.55), run_time=rt, rate_func=linear)
        self.remove(c)
        until(self, "Two: block", lead=0.4)
        c2 = out_slip(-0.95)
        rt = guard(self, 0.2)
        self.play(FadeOut(on), GrowFromCenter(c2), run_time=rt)
        rt = guard(self, 0.45)
        self.play(along_y(c2, -0.75), run_time=rt, rate_func=linear)
        door = door_lane(G_PRE, OUT)
        e2 = T("exit 2", 38).move_to(EXIT_AT)
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(door, UP), FadeOut(e0), FadeIn(e2), run_time=rt)
        until(self, "standard error", lead=0.5)
        n = fly_note(self, np.array(W.p(OUT[1] + 0.3, G_PRE + 0.4, 1.2)), 0.8)
        self.play(Flash(np.array(light.get_center()), color=TERRA, line_length=0.16, flash_radius=0.28), run_time=0.35)
        until(self, "Other codes", lead=0.6)
        eo = T("other", 38).move_to(EXIT_AT)
        c3 = out_slip(-0.95)
        rt = guard(self, 0.4)
        self.play(FadeOut(door), FadeOut(c2), FadeOut(n), FadeOut(e2), GrowFromCenter(c3), FadeIn(eo), run_time=rt)
        rt = guard(self, 0.7)
        self.play(along_y(c3, -3.3), run_time=rt, rate_func=linear)
        self.remove(c3)
        self.play(GrowFromCenter(lit(gp[2])), run_time=0.2)
        done(self)


# ─────────────── B07: Anthropic's example: grep -> exit 2 -> rg ───────────────
class B07_Grep(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        rig = full_rig()
        carry = VGroup(T("other", 38).move_to(EXIT_AT), lit(g_pre()[2]))
        self.add(belts, blk, light, mach, lights, cl, tl, rig, carry)
        self.play(FadeOut(carry), run_time=0.4)
        gp = rig[3]
        until(self, "example hook watches Bash", lead=0.4)
        sc = script_card()
        rt = guard(self, 0.35)
        self.play(GrowFromCenter(sc), run_time=rt)
        tie = script_tie()
        ex = T("example hook", 38).next_to(sc, UP, buff=0.3)
        self.play(Create(tie), FadeIn(ex), run_time=0.35)
        until(self, "starts with grep", lead=0.4)
        c = out_slip(-0.95)
        self.play(GrowFromCenter(c), run_time=0.2)
        rt = guard(self, 0.35)
        self.play(along_y(c, -0.75), run_time=rt, rate_func=linear)
        gl = T("grep", 38).move_to(EXIT_AT)
        self.play(FadeIn(gl), run_time=0.25)
        until(self, "exits two", lead=0.5)
        door = door_lane(G_PRE, OUT)
        e2 = T("exit 2", 38).move_to([0.3, -3.0, 0])
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(door, UP), Indicate(sc, color=None, scale_factor=1.06), run_time=rt)
        self.play(FadeIn(e2), run_time=0.25)
        until(self, "The call never runs", lead=0.3)
        rt = guard(self, 0.3)
        self.play(FadeOut(c), run_time=rt)
        until(self, "Claude reads the note", lead=0.4)
        n = fly_note(self, np.array(W.p(OUT[1] + 0.3, G_PRE + 0.4, 1.2)), 0.55)
        self.play(Flash(np.array(light.get_center()), color=TERRA, line_length=0.16, flash_radius=0.28), run_time=0.3)
        until(self, "try again", lead=0.6)
        c2 = out_slip(-0.95)
        rl = T("rg", 38).move_to(EXIT_AT)
        rt = guard(self, 0.35)
        self.play(FadeOut(n), FadeOut(gl), FadeOut(e2), FadeOut(door), GrowFromCenter(c2), FadeIn(rl), run_time=rt)
        rt = guard(self, 0.6)
        self.play(along_y(c2, -3.3), run_time=rt, rate_func=linear)
        self.remove(c2)
        on = run_lights(lights)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.08), run_time=0.3)
        done(self)


# ─────────────── B08: exit 2 at each event; Stop keeps Claude working ───────────────
class B08_Stop(Scene):
    def construct(self):
        belts, blk, light, mach, lights, cl, tl = base()
        rig = full_rig()
        sc = script_card()
        carry = VGroup(sc, script_tie(), T("example hook", 38).next_to(sc, UP, buff=0.3), T("rg", 38).move_to(EXIT_AT), run_lights(lights))
        self.add(belts, blk, light, mach, lights, cl, tl, rig, carry)
        self.play(FadeOut(carry), run_time=0.4)
        ss, ups, stp, gp, gq = rig[0], rig[1], rig[2], rig[3], rig[4]
        until(self, "At user prompt submit", lead=0.4)
        p = main_slip(0.3)
        l1 = lbl("UserPromptSubmit")
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(p), FadeIn(l1), run_time=rt)
        rt = guard(self, 0.6)
        self.play(along_x(p, 1.9), run_time=rt, rate_func=linear)
        d1 = door_main(G_UPS)
        rt = guard(self, 0.35)
        self.play(GrowFromEdge(d1, UP), run_time=rt)
        until(self, "erases it", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeOut(p), run_time=rt)
        until(self, "At post tool use", lead=0.3)
        on = run_lights(lights)
        l2 = lbl("PostToolUse")
        rt = guard(self, 0.4)
        self.play(FadeOut(d1), FadeOut(l1), LaggedStart(*[GrowFromCenter(d) for d in on], lag_ratio=0.08), FadeIn(l2), run_time=rt)
        r = back_slip(-4.3)
        self.add(r)
        rt = guard(self, 0.5)
        self.play(along_y(r, 0.8), run_time=rt, rate_func=linear)
        until(self, "Claude just sees the note", lead=0.4)
        n = fly_note(self, np.array(W.p(BACK[1] + 0.3, G_POST + 0.3, 1.2)), 0.7)
        self.play(Flash(np.array(light.get_center()), color=TERRA, line_length=0.16, flash_radius=0.28), run_time=0.3)
        until(self, "Session start can't block", lead=0.3)
        l3 = lbl("SessionStart")
        rt = guard(self, 0.35)
        self.play(FadeOut(n), FadeOut(r), FadeOut(on), FadeOut(l2), run_time=rt)
        self.play(FadeIn(l3), GrowFromCenter(lit(ss[2])), run_time=0.3)
        s0 = main_slip(0.1)
        self.play(GrowFromCenter(s0), run_time=0.2)
        rt = guard(self, 0.6)
        self.play(along_x(s0, 2.1), run_time=rt, rate_func=linear)
        self.play(FadeOut(s0), run_time=0.2)
        until(self, "And stop keeps Claude working", lead=0.4)
        l4 = lbl("Stop")
        a = main_slip(7.6, result=True)
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(a), FadeOut(l3), FadeIn(l4), run_time=rt)
        rt = guard(self, 0.5)
        self.play(along_x(a, 0.8), run_time=rt, rate_func=linear)
        d2 = door_main(G_STOP)
        rt = guard(self, 0.35)
        self.play(GrowFromEdge(d2, UP), GrowFromCenter(lit(stp[2])), run_time=rt)
        until(self, "with your note as the reason", lead=0.4)
        n2 = fly_note(self, np.array(W.p(G_STOP - 0.3, 0.75, 1.3)), 0.6)
        self.play(FadeOut(a), light.animate.set_color(TERRA), Flash(np.array(light.get_center()), color=TERRA, line_length=0.16, flash_radius=0.28), run_time=0.35)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Belt, B01_Checkpoint, B02_Turn, B03_Tools, B04_Matcher, B05_Stdin, B06_Exit, B07_Grep, B08_Stop):
    _cls.play = ST.play
