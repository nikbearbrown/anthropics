"""
Manim scenes for show-tell-security-review-every-pr (show-tell skill, card #8, the last in the batch).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

anthropics/claude-code-security-review, drawn in the series' conveyor language (five-ways-to-wire-an-agent,
claude-plugin-portal): a pull request is a taped crate on a belt; only the changed files ride on (the diff);
Claude is a dark scanner arch over the belt; findings pop up as white flags; a filter screen drops likely
false positives into a bin; what's left pins to the pull request's lines as comments; a person, not the arch,
lifts the merge gate; the same review on your own desk as /security-review; and the repo's caution: an
outside crate with a tucked note waits at an approval barrier.
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








# ═════════════════════════════ the film: a security review on every pull request ═════════════════════════════
# Cast: a pale BELT with a kraft side and a dashed centre line; the pull request as a kraft CRATE with
# terracotta tape; the repo's files as standing PAGES (grey = unchanged, white with a terracotta dot = changed);
# Claude as a dark scanner ARCH over the belt, with a light and a terracotta scan line; FINDINGS as white
# flags on dark-kraft poles; the FILTER as a kraft-framed mesh with a kraft BIN; the PR PAGE as a white panel
# with a dark title bar; the MERGE GATE as an ink arch with a bar; the reviewer as a cursor; the terminal as
# a dark window; an outside crate (grey) with a tucked NOTE; an ink approval BARRIER.
DEV_EDGE = "#917A55"      # dark kraft outline for small objects (outside GATE T's ink tolerance)
SHADOW = "#AFA28A"        # floor shadows deep enough to carry Gate V contrast
BELT = "#E6DFD3"
UNCH = "#E4DED3"          # an unchanged file page: pale grey

# ── the WIDE rig: the belt, the arch, the merge gate ──
M = Iso(-5.0, -2.75, 0.64)
BL, BW = 14.5, 1.5        # belt length (x), width (y)
ARCH_X, ARCH_H = 7.0, 2.3
GATE_X = 12.4
CR_S = 1.2                # crate size in the wide rig


def belt(iso=M, x0=0.0, x1=BL, w=BW, th=0.25):
    """A flat belt along x with a kraft side face (y = 0) and end face (x = x0), and a dashed centre line."""
    top = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, w, 0), (x0, w, 0)], BELT, stroke=DIM, sw=2)
    side = iso.quad([(x0, 0, 0), (x1, 0, 0), (x1, 0, -th), (x0, 0, -th)], BOX_R, stroke=DEV_EDGE, sw=3)
    end = iso.quad([(x0, 0, 0), (x0, w, 0), (x0, w, -th), (x0, 0, -th)], BOX_L, stroke=DEV_EDGE, sw=3)
    mid = DashedLine(iso.p(x0 + 0.3, w / 2, 0), iso.p(x1 - 0.3, w / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
    g = VGroup(side, end, top, mid)
    g.set_z_index(-1)
    return g


def crate(iso, cx, cy, s=CR_S, z=0.02, tape=True, faces=None):
    x0, y0, h = cx - s / 2, cy - s / 2, s * 0.8
    f = faces or (BOX_TOP, BOX_L, BOX_R)
    b = iso.box(x0, y0, z, s, s, h, *f)
    g = VGroup(b)
    if tape:
        g.add(iso.tape(x0, y0, z + h, s, s, drop=h * 0.3, t=s * 0.14))
    return g


def arch(iso=M, x=ARCH_X, h=ARCH_H, w=BW):
    """Claude, the scanner: (back post, front post + beam, light). Dark station faces, as in five-ways."""
    back = iso.box(x - 0.3, w + 0.15, 0, 0.6, 0.4, h, DARK_TOP, DARK_L, DARK_R)
    front = VGroup(iso.box(x - 0.3, -0.55, 0, 0.6, 0.4, h, DARK_TOP, DARK_L, DARK_R),
                   iso.box(x - 0.35, -0.55, h, 0.7, w + 1.1, 0.5, DARK_TOP, DARK_L, DARK_R))
    light = Dot(iso.p(x - 0.35, w / 2 + 0.15, h + 0.25), radius=max(0.07, 0.14 * iso.s), color=GHOST)
    back.set_z_index(0); front.set_z_index(5); light.set_z_index(6)
    return back, front, light


def scan_line(iso=M, x=ARCH_X, h=ARCH_H, w=BW):
    """The terracotta scan line, just in front of the arch at beam height; sweep it down with sweep()."""
    return Line(iso.p(x - 0.45, -0.1, h - 0.05), iso.p(x - 0.45, w + 0.1, h - 0.05), color=TERRA, stroke_width=7).set_z_index(6)


def page(iso, x, y0=0.2, y1=1.3, z0=0.02, z1=1.35, changed=True):
    """A file standing on its edge in the plane x = const. Changed: white with a terracotta dot."""
    body = iso.quad([(x, y0, z0), (x, y1, z0), (x, y1, z1), (x, y0, z1)], PAGE_TOP if changed else UNCH, stroke=DIM, sw=2.5)
    lines = VGroup(*[Line(iso.p(x, y0 + 0.2, z1 - f), iso.p(x, y1 - 0.2 - 0.25 * (k % 2), z1 - f), color=GHOST if not changed else BAR2,
                          stroke_width=4) for k, f in enumerate((0.35, 0.6, 0.85))])
    g = VGroup(body, lines)
    if changed:
        g.add(Dot(iso.p(x, y1 - 0.2, z1 - 0.15), radius=max(0.05, 0.075 * iso.s * 1.3), color=TERRA))
    return g


def flag(base, s=1.0, grey=False):
    """A finding: a white pennant on a dark-kraft pole whose foot sits at `base` (screen point)."""
    top = base + UP * 1.0 * s
    pole = Line(base, top, color=DEV_EDGE, stroke_width=5)
    pen = RoundedRectangle(width=0.8 * s, height=0.46 * s, corner_radius=0.06 * s, fill_color=GHOST if grey else "#FFFFFF",
                           fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to(top + np.array([0.4 * s, -0.2 * s, 0]))
    dot = Dot(top + np.array([0.14 * s, -0.2 * s, 0]), radius=0.06 * s, color=GHOST if grey else TERRA)
    ln = Line(top + np.array([0.28 * s, -0.2 * s, 0]), top + np.array([0.66 * s, -0.2 * s, 0]), color=DIM, stroke_width=4)
    return VGroup(pole, pen, dot, ln).set_z_index(7)


def gate(iso, x, h=2.0, w=BW, sw=9):
    """The merge gate: an ink arch across the belt at x -> (back post + beam, front post, bar)."""
    back = VGroup(Line(iso.p(x, w + 0.1, 0), iso.p(x, w + 0.1, h), color=INK, stroke_width=sw),
                  Line(iso.p(x, w + 0.1, h), iso.p(x, -0.1, h), color=INK, stroke_width=sw))
    front = Line(iso.p(x, -0.1, 0), iso.p(x, -0.1, h), color=INK, stroke_width=sw)
    bar = Line(iso.p(x, -0.1, 1.05), iso.p(x, w + 0.1, 1.05), color=INK, stroke_width=sw + 3)
    back.set_z_index(0); front.set_z_index(5); bar.set_z_index(5)
    return back, front, bar


def wide_base(lit=True):
    """The belt and the arch (light on), as B00 leaves them; the arch's label separately."""
    b = belt()
    ab, af, al = arch()
    if lit:
        al.set_color(TERRA)
    return b, VGroup(ab, af, al), claude_label()


def claude_label():
    return T("Claude", 42).move_to([-3.55, 1.25, 0])


# ─────────────── B00: a pull request is a crate on a belt; Claude is the arch ───────────────
class B00_Belt(Scene):
    def construct(self):
        b = belt()
        self.play(FadeIn(b[0:3]), Create(b[3]), run_time=0.8)
        until(self, "a crate on a belt", lead=0.5)
        cr = crate(M, 1.2, BW / 2)
        cr.set_z_index(2)
        cr.shift(LEFT * 3)
        self.add(cr)
        self.play(cr.animate.shift(RIGHT * 3), run_time=0.6)
        self.play(FadeIn(T("pull request", 42).move_to([-2.85, -2.95, 0])), run_time=0.3)
        until(self, "on its way to being merged", lead=0.3)
        self.play(cr.animate.shift(M.v(2.2, 0, 0)), run_time=0.9)
        until(self, "a GitHub Action", lead=0.4)
        ab, af, al = arch()
        rt = guard(self, 0.6)
        for m in (ab, af, al):
            m.shift(UP * 5)
        self.add(ab, af, al)
        self.play(VGroup(ab, af, al).animate.shift(DOWN * 5), run_time=rt, rate_func=ease_in)
        until(self, "when a pull request opens", lead=0.3)
        self.play(Indicate(cr, color=None, scale_factor=1.08), run_time=0.5)
        until(self, "It puts Claude", lead=0.3)
        self.play(FadeIn(claude_label()), run_time=0.3)
        until(self, "as a security reviewer", lead=0.3)
        self.play(al.animate.set_color(TERRA), Flash(al.get_center(), color=TERRA, line_length=0.18, flash_radius=0.3), run_time=0.5)
        done(self)


# ─────────────── B01: open the crate; only the changed files ride on ───────────────
C = Iso(-3.3, -2.55, 1.0)          # the close rig: the crate at the belt's start
CW, CD, CH = 3.4, 1.8, 1.1         # the open crate
PX = [0.3 + 0.35 * i for i in range(9)]   # page x positions inside the crate
CHANGED = (2, 5, 7)                # which pages the pull request changed
ON_BELT = (5.2, 5.95, 6.7)          # where the three changed pages stand on the belt


def open_crate(iso=C):
    back, front = iso.open_box(0, 0, 0.02, CW, CD, CH)
    edge_all(back, INK, 4); edge_all(front, INK, 4)          # ink, as the kit's boxes: GATE T reads dark kraft as low-contrast type
    front[0].set_fill(BOX_IN2); front[1].set_fill(BOX_FLOOR)       # deeper kraft: Gate V contrast
    back[1].set_fill(BOX_IN2); back[2].set_fill(BOX_FLOOR)
    sh = iso.quad([(-0.2, -0.35, 0), (CW + 0.3, -0.35, 0), (CW + 0.3, CD, 0), (-0.2, CD, 0)], SHADOW, sw=0)
    sh.set_z_index(-0.5)
    return sh, back, front


def edge_all(g, color=DEV_EDGE, w=4):
    for f in g:
        f.set_stroke(color, w)
    return g


def crate_pages(iso=C):
    """Nine standing files, drawn back (high x) to front; returns dict i -> page."""
    d = {}
    for i in reversed(range(9)):
        d[i] = page(iso, PX[i], 0.25, CD - 0.25, 0.15, CH + 0.55, changed=i in CHANGED)
        d[i].set_z_index(1 + (9 - i) * 0.01)
    return d


class B01_Diff(Scene):
    def construct(self):
        b = belt(C, -0.4, 8.2, CD)
        sh, back, front = open_crate()
        lid = C.box(0, 0, CH + 0.02, CW, CD, 0.12, BOX_TOP, BOX_L, BOX_R)
        edge_all(lid, INK, 4)
        tape = C.tape(0, 0, CH + 0.14, CW, CD, drop=0.3, t=0.25)
        lid_g = VGroup(lid, tape).set_z_index(4)
        self.add(b, sh, back, front, lid_g)
        until(self, "Open the crate", lead=0.1)
        self.play(lid_g.animate.shift(UP * 1.3 + LEFT * 0.8).rotate(0.3), run_time=0.45)
        self.play(FadeOut(lid_g, shift=UP * 0.3), run_time=0.3)
        pg = crate_pages()
        allp = VGroup(*[pg[i] for i in reversed(range(9))])
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[p.animate.shift(C.v(0, 0, 0.9)) for p in allp], lag_ratio=0.08), run_time=rt)
        until(self, "Most of the repo", lead=0.3)
        self.play(FadeIn(T("repo", 42).move_to([-5.2, 1.75, 0])), run_time=0.3)
        until(self, "stays behind", lead=0.3)
        unch = [pg[i] for i in range(9) if i not in CHANGED]
        self.play(*[p.animate.shift(C.v(0, 0, -1.25)) for p in unch], run_time=0.5)
        until(self, "Only the changed files", lead=0.3)
        rt = guard(self, 1.2)
        moves = []
        for k, i in enumerate(CHANGED):
            dx = ON_BELT[k] - PX[i]
            moves.append(pg[i].animate.shift(C.v(dx, 0, -0.9 - 0.13)))
        for i in CHANGED:
            pg[i].set_z_index(3)
        self.play(LaggedStart(*moves, lag_ratio=0.15), run_time=rt)
        self.play(FadeIn(T("diff", 42).move_to([3.1, -0.35, 0])), run_time=0.3)
        until(self, "read the rest for context", lead=0.3)
        src = C.p(ON_BELT[0], 0.3, 1.2)
        dst = C.p(PX[4], 0.3, CH + 0.5)
        look = DashedLine(src, dst, color=DIM, stroke_width=5, dash_length=0.14).set_z_index(6)
        rt = guard(self, 0.6)
        self.play(Create(look), *[Indicate(p, color=None, scale_factor=1.04) for p in unch], run_time=rt)
        until(self, "report only what", lead=0.3)
        self.play(FadeOut(look), run_time=0.3)
        ck = check(3.05, 0.5, 0.22, INK, 8).set_z_index(8)
        rt = guard(self, 0.4)
        self.play(Create(ck), run_time=rt)
        until(self, "not old problems", lead=0.3)
        self.play(*[pg[i].animate.shift(C.v(0.35, 0, 0)) for i in CHANGED], ck.animate.shift(C.v(0.35, 0, 0)), run_time=0.5)
        done(self)


# ─────────────── B02: the scan; findings flag up ───────────────
PAGE_X = (3.3, 4.2, 5.1)            # the three changed pages on the wide belt, before the arch
PASS_DX = 5.2                       # how far they ride (all three end up past the arch)


def wide_pages(xs=PAGE_X):
    return [page(M, x, 0.3, 1.2, 0.02, 1.25, True).set_z_index(3) for x in xs]


def back_crate():
    """The crate left behind at the belt's start: kraft, lid off, grey pages inside (no tape)."""
    g = crate(M, 1.2, BW / 2, tape=False)
    g.set_z_index(2)
    return g


def finding_card(c):
    """A finding, opened: a white card with a dark title bar and four rows (line, severity, exploit, fix)."""
    w, h = 3.9, 2.35
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    bar = Rectangle(width=w - 0.06, height=0.34, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(c + UP * (h / 2 - 0.2))
    rows = []
    for k in range(4):
        y = c[1] + 0.45 - k * 0.42
        rows.append(VGroup(Dot([c[0] - 1.6, y, 0], radius=0.06, color=BAR1),
                           Line([c[0] - 1.35, y, 0], [c[0] + (1.4 - 0.45 * (k % 2)), y, 0], color=BAR2, stroke_width=6)))
    meter = VGroup(*[Rectangle(width=0.32, height=0.2, fill_color=col, fill_opacity=1, stroke_width=0)
                     .move_to([c[0] + 0.95 + 0.38 * j, c[1] + 0.03, 0]) for j, col in enumerate((BAR1, BAR1, BAR3))])
    return VGroup(body, bar), rows, meter


CARD_C = np.array([3.9, -1.75, 0])


class B02_Scan(Scene):
    def construct(self):
        b, ar, clab = wide_base()
        bc = back_crate()
        pgs = wide_pages()
        self.add(b, bc, ar, clab, *pgs)
        until(self, "pass under the scanner", lead=0.2)
        grp = VGroup(*pgs)
        pos = [0.0]

        def ride(dx, rt):
            rt = guard(self, rt)
            self.play(grp.animate.shift(M.v(dx - pos[0], 0, 0)), run_time=rt, rate_func=linear)
            pos[0] = dx

        def sweep():
            sl = scan_line()
            rt = guard(self, 0.5)
            self.add(sl)
            self.play(sl.animate.shift(DOWN * (ARCH_H - 0.1) * M.s), run_time=rt)
            self.play(FadeOut(sl), run_time=0.15)

        for k in range(3):
            ride(ARCH_X - 0.25 - PAGE_X[2 - k], 0.7)
            sweep()
            if k == 0:
                until(self, "reads them for meaning", lead=0.4)
                self.play(ar[2].animate.scale(1.5), run_time=0.2)
                self.play(ar[2].animate.scale(1 / 1.5), run_time=0.2)
            if k == 1:
                until(self, "injection", lead=0.4)
        ride(PASS_DX, 0.8)
        until(self, "becomes a finding", lead=0.5)
        f1 = flag(M.p(PAGE_X[0] + PASS_DX, 0.75, 1.3))
        f2 = flag(M.p(PAGE_X[2] + PASS_DX, 0.75, 1.3))
        rt = guard(self, 0.5)
        self.play(GrowFromEdge(f1, DOWN), GrowFromEdge(f2, DOWN), run_time=rt)
        self.play(FadeIn(T("finding", 42).move_to([2.4, 0.8, 0])), run_time=0.3)
        until(self, "the line", lead=0.4)
        card, rows, meter = finding_card(CARD_C)
        rt = guard(self, 0.5)
        self.play(TransformFromCopy(f1[1].copy(), card), run_time=rt)
        self.play(FadeIn(rows[0]), run_time=0.25)
        until(self, "how serious", lead=0.3)
        self.play(FadeIn(rows[1]), FadeIn(meter), run_time=0.3)
        until(self, "how it could be exploited", lead=0.3)
        self.play(FadeIn(rows[2]), run_time=0.3)
        until(self, "and a fix", lead=0.3)
        self.play(FadeIn(rows[3]), run_time=0.3)
        done(self)


# ─────────────── B03: the filter drops likely false positives ───────────────
F = Iso(-4.3, -2.35, 0.92)
FX = 6.3                              # the filter screen
FLAG_X = [1.9, 3.1, 4.3, 5.5]         # four findings on the belt
BIN = (FX - 0.9, -2.9, 1.8, 1.4, 0.8) # x0, y0, w, d, h


def filter_screen(iso=F, x=FX, w=BW, h=1.9):
    """[0] frame (kraft posts + top rail), [1] mesh."""
    posts = VGroup(edge_all(iso.box(x - 0.15, -0.35, 0, 0.3, 0.3, h, BOX_TOP, BOX_L, BOX_R), DEV_EDGE, 3),
                   edge_all(iso.box(x - 0.15, w + 0.05, 0, 0.3, 0.3, h, BOX_TOP, BOX_L, BOX_R), DEV_EDGE, 3),
                   edge_all(iso.box(x - 0.15, -0.35, h, 0.3, w + 0.7, 0.22, BOX_TOP, BOX_L, BOX_R), DEV_EDGE, 3))
    mesh = VGroup()
    for k in range(1, 6):
        yy = -0.05 + (w + 0.1) * k / 6
        mesh.add(Line(iso.p(x, yy, 0.05), iso.p(x, yy, h), color=DIM, stroke_width=3))
    for k in range(1, 5):
        zz = h * k / 5
        mesh.add(Line(iso.p(x, -0.05, zz), iso.p(x, w + 0.05, zz), color=DIM, stroke_width=3))
    posts[1].set_z_index(0); mesh.set_z_index(4); posts[0].set_z_index(8); posts[2].set_z_index(8)
    return VGroup(posts, mesh)


def bin_box(iso=F):
    x0, y0, w, d, h = BIN
    back, front = iso.open_box(x0, y0, 0, w, d, h)
    edge_all(back); edge_all(front)
    back.set_z_index(0); front.set_z_index(9)
    sh = iso.quad([(x0 - 0.15, y0 - 0.3, 0), (x0 + w + 0.25, y0 - 0.3, 0), (x0 + w + 0.25, y0 + d, 0), (x0 - 0.15, y0 + d, 0)], SHADOW, sw=0)
    sh.set_z_index(-0.5)
    return sh, back, front


def bin_mouth(k=0):
    x0, y0, w, d, h = BIN
    return F.p(x0 + w * (0.35 + 0.3 * k), y0 + d * 0.5, 0.2)


def f_arch():
    return arch(F, 0.7, 2.2)


def belt_flag(x, grey=False):
    return flag(F.p(x, BW / 2, 0), 0.95, grey)


class B03_Filter(Scene):
    def construct(self):
        b = belt(F, -0.3, 10.2)
        ab, af, al = f_arch()
        al.set_color(TERRA)
        fl = [belt_flag(x) for x in FLAG_X]
        self.add(b, ab, af, al, *fl)
        until(self, "a filter catches", lead=0.4)
        fs = filter_screen()
        fs.shift(UP * 5)
        rt = guard(self, 0.6)
        self.add(fs)
        self.play(fs.animate.shift(DOWN * 5), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(T("filter", 42).move_to([2.6, 2.75, 0])), run_time=0.3)
        until(self, "Hard rules", lead=0.5)
        sh, bk, fr = bin_box()
        rt = guard(self, 0.5)
        self.play(FadeIn(sh), FadeIn(bk), FadeIn(fr), run_time=rt)
        grp = VGroup(*fl)
        dx = FX - 0.55 - FLAG_X[3]
        rt = guard(self, 0.6)
        self.play(grp.animate.shift(F.v(dx, 0, 0)), run_time=rt, rate_func=linear)
        until(self, "denial of service", lead=0.3)
        first = fl[3]
        rt = guard(self, 0.9)
        self.play(Indicate(fs[1], color=None, scale_factor=1.03), run_time=0.3)
        first.set_z_index(5)
        self.play(MoveAlongPath(first, ArcBetweenPoints(first.get_center(), bin_mouth(0) + UP * 0.35, angle=-0.9)),
                  run_time=rt - 0.3 if rt > 0.6 else 0.6)
        self.play(FadeIn(T("dropped", 42).move_to([4.95, -0.8, 0])), run_time=0.3)
        until(self, "Claude re-checks", lead=0.4)
        rest = fl[:3]
        looks = VGroup(*[DashedLine(al.get_center(), f[1].get_center(), color=DIM, stroke_width=4, dash_length=0.12) for f in rest])
        looks.set_z_index(8)
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[Create(l) for l in looks], lag_ratio=0.25), run_time=rt)
        until(self, "isn't confident in", lead=0.5)
        weak = rest[1]
        self.play(FadeOut(looks), weak[1].animate.set_fill(GHOST), weak[2].animate.set_color(GHOST), run_time=0.35)
        weak.set_z_index(5)
        keep = VGroup(rest[0], rest[2])
        self.play(MoveAlongPath(weak, ArcBetweenPoints(weak.get_center(), bin_mouth(1) + UP * 0.35, angle=-0.7)),
                  keep.animate.shift(F.v(FX + 1.2 - (FLAG_X[2] + dx), 0, 0)), run_time=0.6)
        done(self)


# ─────────────── B04: what's left pins to the pull request's lines ───────────────
PANEL_C, PANEL_W, PANEL_H = np.array([-2.35, -0.45, 0]), 7.2, 5.1
ROW_Y = [PANEL_C[1] + PANEL_H / 2 - 0.95 - 0.42 * k for k in range(10)]
DIFF_ROWS = (2, 3, 4, 7, 8)
HIT = (3, 8)                          # rows that get a comment
CM_X = 3.95


def pr_panel():
    body = RoundedRectangle(width=PANEL_W, height=PANEL_H, corner_radius=0.16, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(PANEL_C)
    bar = Rectangle(width=PANEL_W - 0.08, height=0.62, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0)
    bar.move_to(PANEL_C + UP * (PANEL_H / 2 - 0.35))
    gut = Rectangle(width=0.3, height=PANEL_H - 0.8, fill_color=DARK_L, fill_opacity=1, stroke_width=0)
    gut.move_to([PANEL_C[0] - PANEL_W / 2 + 0.2, PANEL_C[1] - 0.33, 0])
    spark = Dot(bar.get_left() + RIGHT * 0.35, radius=0.09, color=TERRA)
    x0 = PANEL_C[0] - PANEL_W / 2 + 0.6
    bands = VGroup(*[Rectangle(width=PANEL_W - 0.6, height=0.38, fill_color="#F6ECD9", fill_opacity=1, stroke_width=0)
                     .move_to([PANEL_C[0] + 0.1, ROW_Y[k], 0]) for k in DIFF_ROWS])
    rows = VGroup()
    lens = (4.2, 5.1, 3.6, 5.4, 2.9, 4.6, 3.3, 5.0, 4.1, 2.6)
    for k, y in enumerate(ROW_Y):
        ind = 0.35 * (k % 3 == 2)
        rows.add(Line([x0 + ind, y, 0], [x0 + ind + lens[k], y, 0], color=BAR1 if k in DIFF_ROWS else BAR2, stroke_width=6))
    return VGroup(body, bar, gut, spark), bands, rows


def comment_card(y):
    c = np.array([CM_X, y, 0])
    body = RoundedRectangle(width=3.3, height=1.0, corner_radius=0.12, fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=DIM, stroke_width=3).move_to(c)
    dot = Dot(c + np.array([-1.35, 0.2, 0]), radius=0.09, color=TERRA)
    lines = VGroup(Line(c + np.array([-1.1, 0.2, 0]), c + np.array([1.2, 0.2, 0]), color=BAR2, stroke_width=6),
                   Line(c + np.array([-1.1, -0.15, 0]), c + np.array([0.6, -0.15, 0]), color=BAR2, stroke_width=6))
    return VGroup(body, dot, lines).set_z_index(5)


def reactions(y):
    out = VGroup()
    for j, up in enumerate((True, False)):
        c = np.array([CM_X - 1.05 + j * 0.95, y - 0.85, 0])
        p = RoundedRectangle(width=0.78, height=0.42, corner_radius=0.21, fill_color=BAR3, fill_opacity=1,
                             stroke_color=DEV_EDGE, stroke_width=2.5).move_to(c)
        s = 1 if up else -1
        chev = VGroup(Line(c + np.array([-0.14, -0.06 * s, 0]), c + np.array([0, 0.08 * s, 0]), color=BAR1, stroke_width=5),
                      Line(c + np.array([0, 0.08 * s, 0]), c + np.array([0.14, -0.06 * s, 0]), color=BAR1, stroke_width=5))
        out.add(VGroup(p, chev))
    return out.set_z_index(5)


def pin(k):
    """The pin on row k (a terracotta dot at the row's right end) and a grey tie to its comment card."""
    x_end = PANEL_C[0] + PANEL_W / 2 - 0.35
    d = Dot([x_end, ROW_Y[k], 0], radius=0.1, color=TERRA).set_z_index(6)
    tie = Line([x_end + 0.12, ROW_Y[k], 0], [CM_X - 1.65, ROW_Y[k], 0], color=DIM, stroke_width=4).set_z_index(4)
    return d, tie


class B04_Comment(Scene):
    def construct(self):
        panel, bands, rows = pr_panel()
        self.play(FadeIn(panel), run_time=0.5)
        self.play(FadeIn(T("pull request", 42).move_to([PANEL_C[0] - 1.6, 2.72, 0])), LaggedStart(*[Create(r) for r in rows], lag_ratio=0.08),
                  FadeIn(bands), run_time=0.8)
        until(self, "review comments", lead=0.6)
        fls = [flag(np.array([6.9, 1.0 - 1.4 * j, 0]), 0.9) for j in range(2)]
        cards, pins = [], []
        for j, k in enumerate(HIT):
            cards.append(comment_card(ROW_Y[k]))
            pins.append(pin(k))
        rt = guard(self, 0.8)
        self.add(*fls)
        self.play(*[ReplacementTransform(f, c) for f, c in zip(fls, cards)], run_time=rt)
        until(self, "pinned to the exact lines", lead=0.3)
        rt = guard(self, 0.5)
        self.play(*[Create(t) for _, t in pins], *[GrowFromCenter(d) for d, _ in pins], run_time=rt)
        self.play(FadeIn(T("comments", 42).move_to([CM_X, 2.15, 0])), run_time=0.3)
        until(self, "a thumbs up", lead=0.3)
        rx = [reactions(ROW_Y[k]) for k in HIT]
        rt = guard(self, 0.5)
        self.play(*[FadeIn(r, shift=UP * 0.15) for r in rx], run_time=rt)
        until(self, "better to miss", lead=0.3)
        ghost = flag(np.array([1.9, -2.95, 0]), 0.8, grey=True).set_z_index(3)
        self.play(FadeIn(ghost), run_time=0.3)
        self.play(FadeOut(ghost, shift=DOWN * 0.3), run_time=0.4)
        until(self, "than flood you", lead=0.3)
        spots = [(-5.0, -2.7), (-4.3, -2.35), (-3.6, -2.75), (-2.9, -2.3), (-2.2, -2.7), (-1.5, -2.4), (-0.8, -2.75),
                 (-4.7, -1.75), (-4.0, -1.45), (-3.25, -1.8), (-2.55, -1.5), (-1.85, -1.85), (-1.15, -1.55), (-0.45, -1.9)]
        flood = VGroup(*[flag(np.array([x, y, 0]), 0.7, grey=True) for x, y in spots])     # a flood of comments over the PR
        flood.set_z_index(8)
        self.play(LaggedStart(*[FadeIn(f, shift=DOWN * 0.4) for f in flood], lag_ratio=0.05), run_time=0.6)
        self.play(FadeOut(flood), *[Indicate(c, color=None, scale_factor=1.05) for c in cards], run_time=0.6)
        done(self)


# ─────────────── B05: a person decides; the gate is theirs ───────────────
CRATE_AT = 10.5


def crate_flags(cx=CRATE_AT):
    top = M.p(cx, BW / 2, CR_S * 0.8 + 0.02)
    return [flag(top + np.array([-0.3, 0.05, 0]), 0.75), flag(top + np.array([0.25, -0.15, 0]), 0.75)]


class B05_Human(Scene):
    def construct(self):
        b, ar, clab = wide_base()
        gb, gf, bar = gate(M, GATE_X)
        cr = crate(M, CRATE_AT, BW / 2).set_z_index(2)
        fl = crate_flags()
        self.add(b, ar, clab, gb, gf, bar, cr, *fl)
        until(self, "a person decides", lead=0.2)
        self.play(FadeIn(T("merge", 42).move_to([4.15, 1.55, 0])), Indicate(bar, color=None, scale_factor=1.05), run_time=0.5)
        until(self, "doesn't approve", lead=0.5)
        a = np.array(ar[2].get_center())
        tgt = np.array(bar.get_center())
        reach = DashedLine(a, a + (tgt - a) * 0.55, color=DIM, stroke_width=5, dash_length=0.14).set_z_index(7)
        REST = np.array([3.55, -0.75, 0])
        cur = cursor(*REST[:2], 0.5).set_z_index(10)
        rt = guard(self, 0.6)
        self.play(Create(reach), FadeIn(cur, shift=UP * 0.3), run_time=rt)
        until(self, "doesn't merge it", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeOut(reach), run_time=rt)
        until(self, "You read each comment", lead=0.3)
        self.play(cur.animate.move_to(fl[0][1].get_center() + np.array([0.15, -0.25, 0])), run_time=0.35)
        until(self, "fix what's real", lead=0.3)
        ck = check(fl[0][1].get_center()[0] - 0.05, fl[0][1].get_center()[1], 0.2, INK, 7).set_z_index(9)
        self.play(FadeOut(fl[0][1:]), Create(ck), run_time=0.3)
        self.play(cur.animate.move_to(fl[1][1].get_center() + np.array([0.15, -0.25, 0])), run_time=0.25)
        until(self, "dismiss what isn't", lead=0.4)
        self.play(FadeOut(fl[1]), cur.animate.move_to(bar.get_center() + np.array([0.1, -0.2, 0])), run_time=0.35)
        lift = UP * 0.95 * M.s
        gck = check(1.0, 2.75, 0.2, TERRA, 7).set_z_index(9)
        self.play(bar.animate.shift(lift), cur.animate.shift(lift), Create(gck), run_time=0.3)
        rider = VGroup(cr, fl[0][0], ck)
        self.play(rider.animate.shift(M.v(3.4, 0, 0)), cur.animate.move_to(REST + np.array([0.2, -0.25, 0])), run_time=0.5)
        done(self)


# ─────────────── B06: the same review, on your own desk ───────────────
WIN_C, WIN_W, WIN_H = np.array([-3.35, 1.0, 0]), 5.1, 2.9
D = Iso(1.6, -2.55, 0.8)                # the small belt on the desk
FOLD = Iso(-5.0, -2.9, 0.7)             # the project folder (.claude/commands/)
DB = 5.0


def terminal():
    body = RoundedRectangle(width=WIN_W, height=WIN_H, corner_radius=0.18, fill_color=DARK_TOP, fill_opacity=1,
                            stroke_color=DARK_L, stroke_width=3).move_to(WIN_C)
    dots = VGroup(*[Dot(WIN_C + np.array([-WIN_W / 2 + 0.35 + 0.28 * i, WIN_H / 2 - 0.3, 0]), radius=0.07, color=BAR1) for i in range(3)])
    out = VGroup(*[Line(WIN_C + np.array([-2.05, 0.65 - 0.36 * k, 0]), WIN_C + np.array([-2.05 + L, 0.65 - 0.36 * k, 0]),
                        color=BAR1, stroke_width=6) for k, L in enumerate((3.2, 2.4, 3.6))])
    py = WIN_C[1] - 0.75
    chev = VGroup(Line(WIN_C + np.array([-2.1, -0.62, 0]), WIN_C + np.array([-1.9, -0.75, 0]), color=CARD, stroke_width=6),
                  Line(WIN_C + np.array([-1.9, -0.75, 0]), WIN_C + np.array([-2.1, -0.88, 0]), color=CARD, stroke_width=6))
    caret = Rectangle(width=0.16, height=0.3, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([WIN_C[0] - 1.6, py, 0])
    return VGroup(body, dots, out), chev, caret


def desk():
    sh = D.quad([(-0.3, -0.4, -0.25), (DB + 0.4, -0.4, -0.25), (DB + 0.4, 2.0, -0.25), (-0.3, 2.0, -0.25)], SHADOW, sw=0)
    sh.set_z_index(-2)
    return sh


class B06_Local(Scene):
    def construct(self):
        tw, chev, caret = terminal()
        self.play(FadeIn(tw), FadeIn(chev), FadeIn(caret), FadeIn(T("Claude Code", 42).move_to([WIN_C[0] - 1.05, 2.85, 0])), run_time=0.6)
        until(self, "same review yourself", lead=0.3)
        b = belt(D, 0, DB, 1.5)
        cr = crate(D, 1.1, 0.75, 1.0).set_z_index(2)
        self.play(FadeIn(desk()), FadeIn(b), FadeIn(cr, shift=RIGHT * 0.3), run_time=0.6)
        until(self, "slash security review", lead=0.5)
        cmd_line = Line(WIN_C + np.array([-1.35, -0.75, 0]), WIN_C + np.array([0.9, -0.75, 0]), color=CARD, stroke_width=6)
        rt = guard(self, 0.6)
        self.play(Create(cmd_line), caret.animate.move_to(WIN_C + np.array([1.1, -0.75, 0])), run_time=rt)
        self.play(FadeIn(T("/security-review", 42).move_to([WIN_C[0], -0.9, 0])), run_time=0.3)
        until(self, "pending changes", lead=0.4)
        ab, af, al = arch(D, 3.0, 1.8)
        rt = guard(self, 0.5)
        for m in (ab, af, al):
            m.shift(UP * 4)
        self.add(ab, af, al)
        self.play(VGroup(ab, af, al).animate.shift(DOWN * 4), run_time=rt, rate_func=ease_in)
        self.play(al.animate.set_color(TERRA), cr.animate.shift(D.v(1.4, 0, 0)), run_time=0.6)
        sl = scan_line(D, 3.0, 1.8, 1.5)
        self.add(sl)
        self.play(sl.animate.shift(DOWN * 1.7 * D.s), run_time=0.45)
        self.play(FadeOut(sl), run_time=0.15)
        f = flag(D.p(2.5, 0.75, 0.82), 0.8)
        self.play(GrowFromEdge(f, DOWN), cr.animate.shift(D.v(0.0, 0, 0)), run_time=0.35)
        until(self, "Copy it into your project", lead=0.4)
        fold_back, fold_front = FOLD.open_box(0, 0, 0, 1.7, 1.2, 0.7)
        edge_all(fold_back); edge_all(fold_front)
        md = RoundedRectangle(width=0.9, height=1.15, corner_radius=0.08, fill_color="#FFFFFF", fill_opacity=1,
                              stroke_color=DIM, stroke_width=3).move_to(WIN_C + np.array([1.4, -0.2, 0]))
        mdl = VGroup(*[Line(md.get_center() + np.array([-0.28, 0.25 - 0.22 * k, 0]), md.get_center() + np.array([0.28 - 0.1 * (k % 2), 0.25 - 0.22 * k, 0]),
                            color=BAR2, stroke_width=4) for k in range(3)])
        doc = VGroup(md, mdl).set_z_index(3)
        rt = guard(self, 0.9)
        self.play(FadeIn(fold_back), FadeIn(fold_front), run_time=0.3)
        dest = FOLD.p(0.85, 0.6, 0.55) + UP * 0.12
        self.play(MoveAlongPath(doc, ArcBetweenPoints(doc.get_center(), dest, angle=0.9)), run_time=max(0.4, rt - 0.3))
        self.play(FadeIn(T(".claude/commands", 38).move_to([-1.95, -2.6, 0])), run_time=0.3)
        until(self, "you can tune it", lead=0.3)
        tl = Line(doc[0].get_center() + np.array([-0.28, -0.42, 0]), doc[0].get_center() + np.array([0.28, -0.42, 0]), color=BAR1, stroke_width=4).set_z_index(4)
        td = Dot(doc[0].get_center() + np.array([0.3, 0.42, 0]), radius=0.07, color=TERRA).set_z_index(4)
        self.play(Create(tl), GrowFromCenter(td), run_time=0.4)
        done(self)


# ─────────────── B07: the repo's caution: trusted pull requests only ───────────────
BAR_X = 4.0
OUT_X = 1.4


def note(iso, cx, top_z):
    """A slip of paper tucked into a crate's top: white, DIM outline, three grey lines; stands in the plane x = cx."""
    y0, y1 = 0.35, 1.05
    body = iso.quad([(cx, y0, top_z - 0.3), (cx, y1, top_z - 0.3), (cx, y1 + 0.1, top_z + 0.75), (cx, y0 + 0.1, top_z + 0.75)],
                    "#FFFFFF", stroke=DIM, sw=2.5)
    ln = VGroup(*[Line(iso.p(cx, y0 + 0.15, top_z + 0.55 - 0.2 * k), iso.p(cx, y1 - 0.1, top_z + 0.55 - 0.2 * k), color=BAR2, stroke_width=4)
                  for k in range(3)])
    return VGroup(body, ln)


class B07_Trust(Scene):
    def construct(self):
        b, ar, clab = wide_base()
        self.add(b, ar, clab)
        until(self, "One caution", lead=0.2)
        oc = crate(M, OUT_X, BW / 2, tape=False, faces=(BAR3, BAR2, BAR1))
        edge_all(oc[0], DEV_EDGE, 3)
        nt = note(M, OUT_X + 0.1, CR_S * 0.8 + 0.02)
        nt.set_z_index(3); oc.set_z_index(2)
        g = VGroup(oc, nt)
        g.shift(LEFT * 3)
        self.add(g)
        self.play(g.animate.shift(RIGHT * 3), run_time=0.6)
        self.play(FadeIn(T("outside", 42).move_to([-2.75, -2.95, 0])), run_time=0.3)
        until(self, "not hardened against prompt injection", lead=0.4)
        self.play(g.animate.shift(M.v(1.2, 0, 0)), run_time=0.7)
        until(self, "text written to steer", lead=0.4)
        a = nt[0].get_top()
        tgt = ar[2].get_center()
        curl = DashedVMobject(CubicBezier(a, a + np.array([0.9, 0.6, 0]), tgt + np.array([-0.8, -0.2, 0]), tgt + np.array([-0.15, -0.05, 0]))
                              .set_stroke(DIM, 5), num_dashes=22).set_z_index(8)
        rt = guard(self, 0.7)
        self.play(Create(curl), run_time=rt)
        self.play(Indicate(ar[2], color=None, scale_factor=1.6), run_time=0.4)
        until(self, "only on trusted", lead=0.4)
        bb, bf, bbar = gate(M, BAR_X, 1.7)
        rt = guard(self, 0.6)
        self.play(FadeOut(curl), Create(bb), Create(bf), Create(bbar), run_time=rt)
        self.play(FadeIn(T("approval", 42).move_to([-0.9, -1.75, 0])), run_time=0.3)
        until(self, "have a maintainer approve", lead=0.4)
        cur = cursor(-0.3, -2.4, 0.5).set_z_index(10)
        self.play(FadeIn(cur, shift=UP * 0.3), run_time=0.3)
        self.play(cur.animate.move_to(nt[0].get_center() + np.array([0.15, -0.2, 0])), run_time=0.4)
        self.play(VGroup(nt, cur).animate.shift(UP * 1.1 + LEFT * 0.4), run_time=0.4)
        self.play(FadeOut(nt, shift=LEFT * 0.4), cur.animate.move_to(bbar.get_center() + np.array([0.1, -0.2, 0])), run_time=0.45)
        until(self, "before their workflows run", lead=0.3)
        ck = check(-2.95, 0.55, 0.2, TERRA, 7).set_z_index(9)
        lift = UP * 0.9 * M.s
        self.play(bbar.animate.shift(lift), cur.animate.shift(lift), Create(ck), run_time=0.4)
        self.play(oc.animate.shift(M.v(4.4, 0, 0)), FadeOut(cur), run_time=0.7)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Belt, B01_Diff, B02_Scan, B03_Filter, B04_Comment, B05_Human, B06_Local, B07_Trust):
    _cls.play = ST.play
