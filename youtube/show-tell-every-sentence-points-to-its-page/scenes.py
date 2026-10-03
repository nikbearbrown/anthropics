"""
Manim scenes for show-tell-every-sentence-points-to-its-page (show-tell skill, card #15, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Citations in the Claude API, from anthropics/claude-cookbooks/misc/using_citations.ipynb, checked against the
raw live docs page (platform.claude.com/docs/en/build-with-claude/citations.md, 2026-09-27): documents lie on a
TABLE (a white plain-text page, a PDF stack, a column of kraft custom-content blocks), each with a toggle
(citations on, all or none); pages are cut into sentence bars; an ANSWER page writes line by line and each cited
line sends an ink THREAD back to a highlighted passage (terracotta dot where it lands); plain text points by
character range (0 to 20 in the docs' example), PDFs by page (from 1; pictures and scans get no thread), custom
content by block index (from 0); the cited-text slip rides back free of output tokens; a line with no thread
gets the magnifier.
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







# ═════════════════════════════ the film: every sentence points to its page ═════════════════════════════
# Cast: DOCUMENTS lying flat: a white plain-text PAGE (sentences as grey bars in rows), a PDF (a stack of three
# white pages with a dog-ear; one page carries a picture), and CUSTOM CONTENT as a column of kraft BLOCKS of different
# sizes. Each document has a small TOGGLE (terracotta knob = citations on). The ANSWER is a white page whose lines
# write in one by one. A THREAD is an ink arc from an answer line back to a passage, which turns dark grey, with a
# terracotta dot where the thread lands. A CITED-TEXT slip, two token METERS, an ink CHECK, a MAGNIFIER.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage, so it doesn't dilute the contrast average
KR_HI = "#E4CFA6"          # a lifted (cited) block's top


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def moved(g, A, B):
    """The same move, applied at once (for carried-over state)."""
    return g.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def pad(iso, x0, y0, w, d):
    return iso.quad([(x0, y0, 0), (x0 + w, y0, 0), (x0 + w, y0 + d, 0), (x0, y0 + d, 0)], PAD, sw=0).set_z_index(-3)


def bar(iso, a, b, y, z, fill=GHOST, hw=0.08):
    return iso.quad([(a, y - hw, z), (b, y - hw, z), (b, y + hw, z), (a, y + hw, z)], fill, sw=0)


def slab(iso, w, d, z=0.0, h=0.06, sw=4):
    return iso.box(0, 0, z, w, d, h, PAGE_TOP, PAGE_L, PAGE_R, sw=sw)


# ─── the plain-text PAGE ───
PW, PD = 2.0, 2.6
ROWS = [2.2, 1.78, 1.36, 0.94, 0.52]
SENTS = [[(0.2, 1.05), (1.17, 1.8)], [(0.2, 0.62), (0.74, 1.8)], [(0.2, 1.3), (1.42, 1.8)], [(0.2, 0.9), (1.02, 1.8)], [(0.2, 1.2)]]
ZT = 0.06


def sent_bar(iso, k, i, fill=None):
    a, b = SENTS[k][i]
    return bar(iso, a, b, ROWS[k], ZT, fill or (BAR2 if (k + i) % 2 == 0 else GHOST))


def tpage(iso, split=True, hi=()):
    """(slab, rows): rows[k][i] is sentence i of row k. Unsplit: one ghost bar per row. hi = [(k, i)] drawn BAR1."""
    rows = VGroup()
    for k, y in enumerate(ROWS):
        if split:
            rows.add(VGroup(*[sent_bar(iso, k, i, BAR1 if (k, i) in hi else None) for i in range(len(SENTS[k]))]))
        else:
            rows.add(VGroup(bar(iso, SENTS[k][0][0], SENTS[k][-1][1], ROWS[k], ZT)))
    return VGroup(slab(iso, PW, PD), rows)


def sent_pt(iso, k, i, f=0.5):
    a, b = SENTS[k][i]
    return iso.p(a + (b - a) * f, ROWS[k], ZT)


# ─── the PDF ───
FW, FD = 1.8, 2.4
FROWS = [1.95, 1.55, 1.15]
FSENTS = [[(0.2, 1.0), (1.12, 1.6)], [(0.2, 1.6)], [(0.2, 0.8)]]
PIC = (0.95, 1.6, 0.25, 0.9)                  # x0, x1, y0, y1 of the picture on a page


def dogear(iso, z):
    return iso.quad([(FW - 0.4, FD, z), (FW, FD - 0.4, z), (FW - 0.4, FD - 0.4, z)], PAGE_L, stroke=DEV_EDGE, sw=2)


def fpage(iso, z=0.0, pic=False, hi=False, blank=False, under=False):
    """One PDF page: (slab, bars, extras). under=True: a page lower in the stack (thin dark-kraft edges)."""
    s = iso.box(0, 0, z, FW, FD, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    if under:
        for f in s:
            f.set_stroke(DEV_EDGE, 2)
    zt = z + 0.06
    bars = VGroup()
    if not blank:
        for k, y in enumerate(FROWS):
            for i, (a, b) in enumerate(FSENTS[k]):
                bars.add(bar(iso, a, b, y, zt, BAR1 if (hi and k == 0 and i == 0) else (BAR2 if (k + i) % 2 == 0 else GHOST)))
    ex = VGroup(dogear(iso, zt))
    if pic:
        x0, x1, y0, y1 = PIC
        ex.add(iso.quad([(x0, y0, zt), (x1, y0, zt), (x1, y1, zt), (x0, y1, zt)], BAR3, sw=0),
               iso.quad([(x0 + 0.1, y0 + 0.1, zt), (x1 - 0.1, y0 + 0.1, zt), ((x0 + x1) / 2, y1 - 0.1, zt)], BAR1, sw=0))
    if blank:
        ex.add(*[iso.quad([(0.2, y - 0.25, zt), (FW - 0.2, y - 0.25, zt), (FW - 0.2, y + 0.25, zt), (0.2, y + 0.25, zt)], BAR3, sw=0)
                 for y in (1.9, 1.2, 0.5)])
    return VGroup(s, bars, ex)


def pdf_stack(iso):
    return VGroup(fpage(iso, 0.0, under=True), fpage(iso, 0.14, under=True), fpage(iso, 0.28))


# ─── CUSTOM CONTENT: a column of kraft blocks ───
BL = [2.4, 1.6, 2.0, 1.2]
BLD, BLSTEP = 0.55, 0.75
BLOCK_NEW = 1.8


def block_y(k):
    return 3.0 - BLSTEP * k


def block(iso, k, L=None, z=0.0, top=BOX_TOP):
    b = iso.box(0, block_y(k), z, L or BL[k], BLD, 0.16, top, BOX_L, BOX_R, sw=3)
    return b


def blocks(iso, n=4):
    return VGroup(*[block(iso, k) for k in range(n)])


# ─── the ANSWER page ───
AW, AD = 2.2, 2.8
AROWS = [2.35, 1.9, 1.45, 1.0, 0.55]
ALEN = [1.5, 1.7, 1.2, 1.6, 1.0]


def answer_slab(iso):
    return slab(iso, AW, AD)


def aline(iso, k, frac=1.0):
    return bar(iso, 0.25, 0.25 + max(0.02, ALEN[k] * frac), AROWS[k], ZT, BAR1)


def answer(iso, n=0):
    return VGroup(answer_slab(iso), VGroup(*[aline(iso, k) for k in range(n)]))


def a_end(iso, k):
    return iso.p(0.2, AROWS[k], ZT)


# ─── threads, toggles, labels ───
def thread(a, b, angle=0.6):
    return ArcBetweenPoints(np.array(a, dtype=float), np.array(b, dtype=float), angle=angle, color=INK, stroke_width=5).set_z_index(8)


def land(b, r=0.09):
    return Dot(np.array(b, dtype=float), radius=r, color=TERRA).set_z_index(9)


def toggle(c, on=False):
    c = P3(c)
    track = RoundedRectangle(width=0.8, height=0.36, corner_radius=0.18, fill_color=GHOST, fill_opacity=1,
                             stroke_color=DEV_EDGE, stroke_width=2).move_to(c)
    knob = Dot(c + RIGHT * (0.2 if on else -0.2), radius=0.13, color=TERRA if on else DIM)
    return VGroup(track, knob)


def flip(tg, c, on=True):
    return tg[1].animate.move_to(P3(c) + RIGHT * (0.2 if on else -0.2)).set_color(TERRA if on else DIM)


def num(s, c, size=44):
    return T(s, size, INK, bold=True).move_to(P3(c))


# ══════════════ B00: documents in the request, citations on ══════════════
S0 = 0.75
TP0 = rig_at(-4.6, -0.6, S0, PW, PD)
PF0 = rig_at(-1.5, -0.6, S0, FW, FD)
BK0 = rig_at(1.85, -0.6, S0, 2.4, 2.8)
QW, QD = 1.3, 1.0
Q0 = rig_at(5.0, -0.5, S0, QW, QD)
TOG_Y = -2.4
TOG_X = [-4.6, -1.5, 1.85]


def qcard(iso=Q0):
    s = iso.box(0, 0, 0, QW, QD, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    zt = 0.06
    return VGroup(s, bar(iso, 0.45, 1.1, 0.5, zt, BAR2), Dot(iso.p(0.25, 0.5, zt), radius=0.08, color=TERRA))


def docs0():
    tp = VGroup(pad(TP0, -0.3, -0.3, PW + 0.6, PD + 0.6), tpage(TP0, split=False))
    pf = VGroup(pad(PF0, -0.3, -0.3, FW + 0.6, FD + 0.6), pdf_stack(PF0))
    bk = VGroup(pad(BK0, -0.3, 0.45, 3.0, 2.95), blocks(BK0))
    return tp, pf, bk


def l_docs():
    return T("documents", 42).move_to([-1.5, 1.55, 0])


def l_question():
    return T("question", 42).move_to([5.0, 0.55, 0])


def l_on():
    return T("citations on", 42).move_to([-1.5, -3.05, 0])


def b00_state():
    tp, pf, bk = docs0()
    return VGroup(tp, pf, bk, qcard(), VGroup(*[toggle([x, TOG_Y], on=True) for x in TOG_X]), l_docs(), l_question(), l_on())


class B00_Table(Scene):
    def construct(self):
        tp, pf, bk = docs0()
        tg = [toggle([x, TOG_Y]) for x in TOG_X]
        until(self, "your documents", lead=0.2)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(VGroup(d, t), shift=DOWN * 1.0) for d, t in zip((tp, pf, bk), tg)], lag_ratio=0.25),
                  run_time=rt, rate_func=ease_in)
        self.play(FadeIn(l_docs()), run_time=0.3)
        until(self, "next to your question", lead=0.2)
        q = qcard()
        q.shift(RIGHT * 3.0)
        self.add(q)
        rt = guard(self, 0.5)
        self.play(q.animate.shift(LEFT * 3.0), FadeIn(l_question()), run_time=rt)
        until(self, "switch citations on", lead=0.2)
        for t, x in zip(tg, TOG_X):
            rt = guard(self, 0.3)
            self.play(flip(t, [x, TOG_Y]), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_on()), run_time=rt)
        until(self, "or none of them", lead=0.3)
        rt = guard(self, 0.35)
        self.play(*[flip(t, [x, TOG_Y], on=False) for t, x in zip(tg, TOG_X)], run_time=rt)
        rt = guard(self, 0.35)
        self.play(*[flip(t, [x, TOG_Y]) for t, x in zip(tg, TOG_X)], run_time=rt)
        until(self, "Every active Claude model", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(tp, pf, bk), color=None, scale_factor=1.04), run_time=rt)
        done(self)


# ══════════════ B01: cut into sentences ══════════════
TP1 = rig_at(-1.0, -0.3, 1.95, PW, PD)
PASS = [(1, 1), (2, 0)]                       # two consecutive sentences, chained into a passage


def l_sentences():
    return T("sentences", 42).move_to([4.6, 1.5, 0])


def l_passage():
    return T("passage", 42).move_to([4.6, -0.4, 0])


def b01_state():
    return VGroup(tpage(TP1, split=True, hi=PASS), l_sentences(), l_passage())


class B01_Chunks(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        tp = st[0][1]
        self.play(FadeOut(VGroup(st[0][0], st[1], st[2], st[3], st[4], st[5], st[6], st[7])), run_time=0.4)
        self.play(to_rig(tp, TP0, TP1), run_time=0.7)
        until(self, "cut into chunks", lead=0.3)
        rows = tp[1]
        split = tpage(TP1, split=True)[1]
        scan = Line(TP1.p(-0.15, PD + 0.05, ZT), TP1.p(PW + 0.15, PD + 0.05, ZT), color=TERRA, stroke_width=6).set_z_index(9)
        rt = guard(self, 0.3)
        self.play(FadeIn(scan), run_time=rt)
        rt = guard(self, 1.6)
        self.play(scan.animate.shift(TP1.v(0, -(PD - 0.2), 0)),
                  LaggedStart(*[FadeTransform(rows[k], split[k]) for k in range(len(ROWS))], lag_ratio=0.25),
                  run_time=rt, rate_func=linear)
        self.play(FadeOut(scan), FadeIn(l_sentences()), run_time=0.35)
        until(self, "cite one sentence", lead=0.2)
        one = split[0][0]
        rt = guard(self, 0.4)
        self.play(one.animate.set_fill(BAR1), run_time=rt)
        until(self, "or chain a few", lead=0.2)
        rt = guard(self, 0.4)
        self.play(one.animate.set_fill(BAR2), split[1][1].animate.set_fill(BAR1), run_time=rt)
        rt = guard(self, 0.4)
        self.play(split[2][0].animate.set_fill(BAR1), FadeIn(l_passage()), run_time=rt)
        until(self, "never less than one", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(split[1][1], split[2][0]), color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B02: the answer, a thread per claim ══════════════
TP2 = rig_at(-4.2, 1.2, 0.85, PW, PD)
PF2 = rig_at(-4.2, -1.85, 0.85, FW, FD)
AN2 = rig_at(2.4, -0.45, 1.35, AW, AD)
T2A = (0, 0)                                  # claim 1 cites row 0, sentence 0 of the text page


def l_answer():
    return T("answer", 42).move_to([4.85, 1.75, 0])


def n0():
    return num("0", [-5.75, 2.55])


def n1():
    return num("1", [-5.75, -0.4])


def thread2a():
    return thread(a_end(AN2, 0) + LEFT * 0.05, sent_pt(TP2, 0, 0, 0.9), angle=0.45)


def thread2b():
    return thread(a_end(AN2, 1) + LEFT * 0.05, PF2.p(0.9, FROWS[0], 0.34), angle=-0.35)


def pdf_hi(iso):
    s = pdf_stack(iso)
    s[2][1][0].set_fill(BAR1)
    return s


def b02_state():
    return VGroup(tpage(TP2, hi=[T2A]), pdf_hi(PF2), answer(AN2, 2), thread2a(), land(sent_pt(TP2, 0, 0, 0.9)),
                  thread2b(), land(PF2.p(0.9, FROWS[0], 0.34)), l_answer(), n0(), n1())


class B02_Threads(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        tp = st[0]
        self.play(FadeOut(VGroup(st[1], st[2])), *[tp[1][k][i].animate.set_fill(BAR2 if (k + i) % 2 == 0 else GHOST) for k, i in PASS],
                  run_time=0.4)
        pf = pdf_stack(PF2)
        self.play(to_rig(tp, TP1, TP2), FadeIn(pf, shift=DOWN * 0.8), run_time=0.7)
        nn0, nn1 = n0(), n1()
        self.play(FadeIn(nn0), FadeIn(nn1), run_time=0.3)
        until(self, "Then Claude answers", lead=0.3)
        an = answer(AN2, 0)
        rt = guard(self, 0.5)
        self.play(FadeIn(an, shift=DOWN * 1.0), FadeIn(l_answer()), run_time=rt, rate_func=ease_in)
        until(self, "Each piece is a text block", lead=0.2)
        l0 = aline(AN2, 0, 0.0)
        self.add(l0)
        rt = guard(self, 0.8)
        self.play(Transform(l0, aline(AN2, 0)), run_time=rt)
        until(self, "a thread runs back", lead=0.3)
        th = thread2a()
        rt = guard(self, 0.8)
        self.play(Create(th), run_time=rt)
        dt = land(sent_pt(TP2, 0, 0, 0.9))
        self.play(FadeIn(dt), tp[1][0][0].animate.set_fill(BAR1), run_time=0.3)
        until(self, "names the document", lead=0.4)
        l1 = aline(AN2, 1, 0.0)
        self.add(l1)
        rt = guard(self, 0.5)
        self.play(Transform(l1, aline(AN2, 1)), run_time=rt)
        th2 = thread2b()
        rt = guard(self, 0.6)
        self.play(Create(th2), run_time=rt)
        self.play(FadeIn(land(PF2.p(0.9, FROWS[0], 0.34))), pf[2][1][0].animate.set_fill(BAR1), Indicate(nn1, color=None), run_time=0.35)
        done(self)


# ══════════════ B03: plain text points by character range ══════════════
TP3 = rig_at(-1.3, -0.8, 1.8, PW, PD)
ANM = rig_at(4.75, 2.3, 0.42, AW, AD)         # the mini answer, top right (B03-B05)
FLAG_H = 1.3


def mini_answer():
    return answer(ANM, 3)


def flag(iso, a, y):
    base = iso.p(a, y, ZT)
    top = base + UP * FLAG_H
    pole = Line(base, top, color=INK, stroke_width=6)
    fl = Polygon(top, top + np.array([0.42, -0.14, 0]), top + np.array([0, -0.3, 0]), fill_color=BOX_R, fill_opacity=1,
                 stroke_color=INK, stroke_width=3)
    return VGroup(pole, fl).set_z_index(9)


def flags3():
    a, b = SENTS[0][0]
    return flag(TP3, a, ROWS[0]), flag(TP3, b, ROWS[0])


def nums3():
    a, b = SENTS[0][0]
    return (num("0", TP3.p(a, ROWS[0], ZT) + UP * (FLAG_H + 0.5)), num("20", TP3.p(b, ROWS[0], ZT) + UP * (FLAG_H + 0.5)))


def thread3():
    return thread(a_end(ANM, 0), sent_pt(TP3, 0, 0, 0.55), angle=0.5)


def l_chars():
    return T("characters", 42).move_to([4.5, -1.3, 0])


def b03_state():
    f0, f1 = flags3()
    n_0, n_20 = nums3()
    return VGroup(tpage(TP3, hi=[(0, 0)]), mini_answer(), thread3(), land(sent_pt(TP3, 0, 0, 0.55)), f0, f1, n_0, n_20,
                  l_chars(), Dot(sent_pt(TP3, 0, 0, 1.0), radius=0.1, color=TERRA).set_z_index(9))


class B03_Characters(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        tp, an = st[0], st[2]
        self.play(FadeOut(VGroup(st[1], st[3], st[4], st[5], st[6], st[7], st[8], st[9])), run_time=0.4)
        self.play(to_rig(tp, TP2, TP3), to_rig(an, AN2, ANM), run_time=0.8)
        mini3 = aline(ANM, 2)
        self.play(FadeIn(mini3), run_time=0.2)
        until(self, "For plain text", lead=0.2)
        th = thread3()
        rt = guard(self, 0.6)
        self.play(Create(th), run_time=rt)
        self.play(FadeIn(land(sent_pt(TP3, 0, 0, 0.55))), FadeIn(l_chars()), run_time=0.3)
        until(self, "where the passage starts", lead=0.2)
        f0, f1 = flags3()
        n_0, n_20 = nums3()
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(f0, DOWN), run_time=rt)
        until(self, "where it stops", lead=0.2)
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(f1, DOWN), run_time=rt)
        until(self, "counted from zero", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(n_0), run_time=rt)
        until(self, "the grass is green", lead=0.1)
        rd = Dot(sent_pt(TP3, 0, 0, 0.0), radius=0.1, color=TERRA).set_z_index(9)
        self.add(rd)
        rt = guard(self, 1.3)
        self.play(rd.animate.move_to(sent_pt(TP3, 0, 0, 1.0)), run_time=rt, rate_func=linear)
        rt = guard(self, 0.35)
        self.play(FadeIn(n_20), run_time=rt)
        done(self)


# ══════════════ B04: a PDF points by page ══════════════
S4 = 0.8
P4X = (-4.65, -1.6, 1.45)
P4 = [rig_at(x, -1.45, S4, FW, FD) for x in P4X]
SC4 = rig_at(4.5, -1.45, S4, FW, FD)


def pages4():
    return VGroup(fpage(P4[0]), fpage(P4[1], hi=True), fpage(P4[2], pic=True))


def nums4():
    return VGroup(*[num(str(k + 1), [x, -0.1]) for k, x in enumerate(P4X)])


def l_pages():
    return T("pages", 42).move_to([-3.1, 1.35, 0])


def thread4():
    return thread(a_end(ANM, 1), P4[1].p(0.6, FROWS[0], 0.06), angle=0.55)


def b04_state():
    return VGroup(pages4(), nums4(), mini_answer(), thread4(), land(P4[1].p(0.6, FROWS[0], 0.06)), l_pages(), fpage(SC4, blank=True))


class B04_Pages(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        an = st[1]
        self.play(FadeOut(VGroup(st[0], st[2], st[3], st[4], st[5], st[6], st[7], st[8], st[9])), run_time=0.45)
        until(self, "For a PDF", lead=0.3)
        stk = VGroup(fpage(P4[1], 0.0, under=True), fpage(P4[1], 0.14, under=True), fpage(P4[1], 0.28, pic=True))
        rt = guard(self, 0.45)
        self.play(FadeIn(stk, shift=DOWN * 0.8), run_time=rt, rate_func=ease_in)
        until(self, "a page range", lead=0.2)
        tgt = pages4()
        rt = guard(self, 0.7)
        self.play(Transform(stk[0], tgt[0]), Transform(stk[1], tgt[1]), Transform(stk[2], tgt[2]), run_time=rt)
        until(self, "counted from one", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(nums4()), FadeIn(l_pages()), run_time=rt)
        until(self, "The text is pulled out", lead=0.2)
        th = thread4()
        rt = guard(self, 0.7)
        self.play(Create(th), run_time=rt)
        self.play(FadeIn(land(P4[1].p(0.6, FROWS[0], 0.06))), run_time=0.25)
        until(self, "A picture on the page", lead=0.3)
        x0, x1, y0, y1 = PIC
        ghost = DashedLine(a_end(ANM, 2), P4[2].p((x0 + x1) / 2, (y0 + y1) / 2, 0.06) + UP * 1.1 + RIGHT * 0.3,
                           color=DIM, stroke_width=5, dash_length=0.14).set_z_index(8)
        rt = guard(self, 0.9)
        self.play(Succession(Create(ghost, run_time=0.5), FadeOut(ghost, run_time=0.4)), run_time=rt)
        until(self, "a scanned page", lead=0.3)
        sc = fpage(SC4, blank=True)
        sc.shift(RIGHT * 3.5)
        self.add(sc)
        rt = guard(self, 0.6)
        self.play(sc.animate.shift(LEFT * 3.5), run_time=rt)
        done(self)


# ══════════════ B05: custom content points by block ══════════════
BK5 = rig_at(-1.0, -0.5, 1.2, 2.4, 3.55)
LIFT = UP * 0.35


def nums5():
    return VGroup(*[num(str(k), BK5.p(0, block_y(k) + 0.1, 0.0) + LEFT * 0.45 + DOWN * 0.12) for k in range(4)])


def l_blocks():
    return T("blocks", 42).move_to([4.3, -1.4, 0])


def thread5():
    return thread(a_end(ANM, 1), BK5.p(1.0, block_y(2) + BLD / 2, 0.16) + LIFT, angle=0.5)


def b05_state():
    b = blocks(BK5)
    b[2].shift(LIFT)
    b[2][2].set_fill(KR_HI)
    new = block(BK5, 4, L=BLOCK_NEW)
    return VGroup(b, nums5(), mini_answer(), thread5(), land(BK5.p(1.0, block_y(2) + BLD / 2, 0.16) + LIFT), l_blocks(), new)


class B05_Blocks(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        an = st[2]
        self.play(FadeOut(VGroup(st[0], st[1], st[3], st[4], st[5], st[6])), run_time=0.45)
        until(self, "Custom content is your own", lead=0.3)
        b = blocks(BK5)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(x, shift=DOWN * 0.9) for x in b], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(l_blocks()), run_time=0.3)
        until(self, "won't cut them any smaller", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(b, color=None, scale_factor=1.04), run_time=rt)
        until(self, "a block index", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(nums5()), run_time=rt)
        until(self, "counted from zero", lead=0.1)
        th = thread5()
        rt = guard(self, 0.4)
        self.play(b[2].animate.shift(LIFT), run_time=rt)
        rt = guard(self, 0.6)
        self.play(Create(th), run_time=rt)
        self.play(FadeIn(land(BK5.p(1.0, block_y(2) + BLD / 2, 0.16) + LIFT)), b[2][2].animate.set_fill(KR_HI), run_time=0.3)
        until(self, "choose the size yourself", lead=0.5)
        new = block(BK5, 4, L=BLOCK_NEW)
        rt = guard(self, 0.5)
        self.play(FadeIn(new, shift=DOWN * 1.0), run_time=rt, rate_func=ease_in)
        done(self)


# ══════════════ B06: the cited text rides back ══════════════
TP6 = rig_at(-3.85, 0.1, 1.05, PW, PD)
AN6 = rig_at(3.45, 0.1, 1.05, AW, AD)
SLIP_END = np.array([-0.55, 2.35, 0])
MX = (-0.95, 0.95)
MB, MSEG = -2.6, 0.32


def thread6():
    return thread(a_end(AN6, 0), sent_pt(TP6, 1, 1, 0.8), angle=0.55)


def slip():
    card = RoundedRectangle(width=1.05, height=0.62, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1,
                            stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.32, 0.1, 0], [0.34, 0.1, 0], color=BAR1, stroke_width=6),
                Line([-0.32, -0.1, 0], [0.18, -0.1, 0], color=BAR1, stroke_width=6))
    return VGroup(card, ln).set_z_index(10)


def l_cited():
    return T("cited text", 42).move_to([1.3, 2.35, 0])


def meter(x, n):
    return VGroup(*[Rectangle(width=0.6, height=MSEG - 0.07, fill_color=(BAR1, BAR2)[i % 2], fill_opacity=1, stroke_width=0)
                    .move_to([x, MB + MSEG * i + MSEG / 2, 0]) for i in range(n)])


def l_quoting():
    return T("quoting", 40).move_to([MX[0], MB - 0.45, 0])


def l_citing():
    return T("citations", 40).move_to([MX[1] + 0.2, MB - 0.45, 0])


NQ, NC = 7, 3
CK6 = (float(sent_pt(TP6, 1, 1, 0.8)[0]) - 0.1, float(sent_pt(TP6, 1, 1, 0.8)[1]) + 1.15)


def b06_state():
    s = slip().move_to(SLIP_END)
    return VGroup(tpage(TP6, hi=[(1, 1)]), answer(AN6, 2), thread6(), land(sent_pt(TP6, 1, 1, 0.8)), s, l_cited(),
                  meter(MX[0], NQ), meter(MX[1], NC), l_quoting(), l_citing(), check(*CK6, 0.26))


class B06_CitedText(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        tp, an = tpage(TP6), answer(AN6, 2)
        rt = guard(self, 0.5)
        self.play(FadeIn(tp, shift=DOWN * 0.6), FadeIn(an, shift=DOWN * 0.6), run_time=rt)
        th = thread6()
        rt = guard(self, 0.5)
        self.play(Create(th), run_time=rt)
        self.play(FadeIn(land(sent_pt(TP6, 1, 1, 0.8))), tp[1][1][1].animate.set_fill(BAR1), run_time=0.25)
        until(self, "hands back the cited text", lead=0.3)
        s = slip().move_to(sent_pt(TP6, 1, 1, 0.8))
        path = ArcBetweenPoints(sent_pt(TP6, 1, 1, 0.8), SLIP_END, angle=-0.5)
        self.add(s)
        rt = guard(self, 1.0)
        self.play(MoveAlongPath(s, path), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_cited()), run_time=rt)
        until(self, "output tokens", lead=0.4)
        mq, mc = meter(MX[0], NQ), meter(MX[1], NC)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_quoting()), FadeIn(l_citing()), FadeIn(mc[0]), FadeIn(mq[0]), run_time=rt)
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in mq[1:]], lag_ratio=0.35),
                  LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in mc[1:]], lag_ratio=0.9), run_time=rt)
        until(self, "guaranteed valid", lead=0.2)
        ck = check(*CK6, 0.26)
        rt = guard(self, 0.4)
        self.play(Create(ck), run_time=rt)
        until(self, "documents you sent", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(tp, color=None, scale_factor=1.04), run_time=rt)
        done(self)


# ══════════════ B07: a line with no thread ══════════════
TP7 = rig_at(-4.3, 1.2, 1.0, PW, PD)
AN7 = rig_at(2.0, -0.5, 1.4, AW, AD)


T7 = [((1, 1), 0.6), ((3, 1), -0.5)]


def thread7(k):
    (sk, si), ang = T7[k]
    return thread(a_end(AN7, k), sent_pt(TP7, sk, si, 0.8), angle=ang)


def l_answer7():
    return T("answer", 42).move_to([4.6, 1.3, 0])


def ring_c():
    return (AN7.p(0.25, AROWS[2], ZT) + AN7.p(0.25 + ALEN[2], AROWS[2], ZT)) / 2


def ring7():
    c = ring_c()
    return Ellipse(width=2.35, height=0.72, color=INK, stroke_width=5).rotate(np.arctan(0.5 / C30)).move_to(c).set_z_index(9)


def l_nocite():
    return T("no citation", 42).move_to([-0.9, -2.5, 0])


def magnifier():
    lens = Circle(radius=0.62, color=INK, stroke_width=9).set_fill(CARD, opacity=0.15)
    handle = Line([0.44, -0.44, 0], [1.05, -1.05, 0], color=INK, stroke_width=18)
    return VGroup(lens, handle).set_z_index(10)


class B07_NoThread(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        tp, an = st[0], st[1]
        self.play(FadeOut(VGroup(*[st[i] for i in range(2, 11)])), *[tp[1][1][1].animate.set_fill(BAR2)], run_time=0.45)
        self.play(to_rig(tp, TP6, TP7), to_rig(an, AN6, AN7), run_time=0.7)
        until(self, "Every cited sentence", lead=0.3)
        self.play(FadeIn(l_answer7()), run_time=0.3)
        t0, t1 = thread7(0), thread7(1)
        rt = guard(self, 0.7)
        self.play(Create(t0), Create(t1), run_time=rt)
        self.play(FadeIn(land(sent_pt(TP7, 1, 1, 0.8))), FadeIn(land(sent_pt(TP7, 3, 1, 0.8))),
                  tp[1][1][1].animate.set_fill(BAR1), tp[1][3][1].animate.set_fill(BAR1), run_time=0.3)
        until(self, "not every line", lead=0.3)
        l2 = aline(AN7, 2, 0.0)
        self.add(l2)
        rt = guard(self, 0.7)
        self.play(Transform(l2, aline(AN7, 2)), run_time=rt)
        until(self, "came back with none", lead=0.3)
        rg = ring7()
        rt = guard(self, 0.5)
        self.play(Create(rg), FadeIn(l_nocite()), run_time=rt)
        until(self, "A line with no thread", lead=0.3)
        c = ring_c()
        mg = magnifier().move_to(np.array([5.2, -2.6, 0]))
        self.add(mg)
        rt = guard(self, 0.8)
        self.play(mg.animate.move_to(c + np.array([0.35, -0.35, 0])), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Table, B01_Chunks, B02_Threads, B03_Characters, B04_Pages, B05_Blocks, B06_CitedText, B07_NoThread):
    _cls.play = ST.play
