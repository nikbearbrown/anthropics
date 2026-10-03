"""
Manim scenes for show-tell-give-every-chunk-its-label (show-tell skill, card #16, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Contextual retrieval, from anthropics/claude-cookbooks/capabilities/contextual-embeddings/guide.ipynb:
a long white DOCUMENT page is cut into four CHUNK cards (one hero card with a terracotta dot); cut loose, the
hero card has lost its context and a search LENS glides past it; CLAUDE (a kraft block with a terracotta spark)
reads the whole document plus the chunk and writes a kraft CONTEXT NOTE that sits on the front of the card;
card + note go through a dark EMBED block into a pale INDEX map; two failure bars show the notebook's 35%
(per Anthropic's notebook); a kraft CACHE shelf holds the document so later chunks read it back; a kraft
BM25 board of grey word slips sits beside the index and their rankings merge into one list; a RERANKER scan
line sorts a longer column and the best few go back to Claude.
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







# ═════════════════════════════ the film: give every chunk its label ═════════════════════════════
# Cast: a long white DOCUMENT page (grey header band, ghost text lines) cut into four CHUNK cards, one HERO card
# with a terracotta dot; Claude as a kraft READER block with a terracotta spark; a kraft CONTEXT NOTE tab on the
# far (top) edge of a card; a dark EMBED block; a pale INDEX map of grey dots; a search LENS (the question);
# failure BARS; a kraft CACHE shelf and a pale LANE; a kraft BM25 board of grey word slips; a RERANKER block
# with a terracotta scan line.
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
SHADOW = "#AFA28A"
PAD = "#E6E1D6"           # within Gate V's INK_DELTA of the stage
BELT = "#E6DFD3"
GREY_TOP, GREY_L, GREY_R = "#C9C4BA", "#A9A398", "#96907F"

CW, CD, CT = 1.6, 1.05, 0.08    # a chunk card: width (x), depth (y), thickness
NCH, HI = 4, 2                   # four chunks; the hero is chunk 2 (counted near to far)


def to_rig(g, A, B):
    """Animate a group built on rig A to rig B (the projection is linear: scale + shift)."""
    return g.animate.scale(B.s / A.s, about_point=A.p(0, 0, 0)).shift(B.p(0, 0, 0) - A.p(0, 0, 0))


def rig_at(center, s):
    """A rig whose card (at local origin) is centred on the screen point `center`."""
    c = np.array(center, dtype=float)
    return Iso(c[0] - (CW / 2 - CD / 2) * C30 * s, c[1] - ((CW + CD) / 2 * 0.5 + CT) * s, s)


NOTE_EDGE = BOX_IN2      # grey ~160: an ink outline inside the ink-outlined card reads as overlapping text (GATE T)


def note(iso, x0=0.0, y0=0.0, z0=0.0, edge=None, sw=3):
    """The kraft context note: a tab on the far (top) edge of a card."""
    b = iso.box(x0 + 0.1, y0 + CD - 0.4, z0 + CT, CW - 0.2, 0.3, 0.06, BOX_L, BOX_R, BOX_IN1, sw=sw)
    for f in b:
        f.set_stroke(NOTE_EDGE, sw)
    return b.set_z_index(3)


def card(iso, x0=0.0, y0=0.0, z0=0.0, hero=False, band=False, edge=INK, sw=3, with_note=False):
    """A chunk card: a white slab, two ghost text lines, a terracotta dot if it is the hero."""
    slab = iso.box(x0, y0, z0, CW, CD, CT, PAGE_TOP, PAGE_L, PAGE_R, sw=sw)
    for f in slab:
        f.set_stroke(edge, sw)
    zt = z0 + CT
    lines = VGroup(*[Line(iso.p(x0 + 0.25, y0 + f, zt), iso.p(x0 + CW - 0.6, y0 + f, zt), color=GHOST,
                          stroke_width=max(2, 5 * iso.s)) for f in (0.3, 0.58)])
    g = VGroup(slab, lines)
    if band:
        g.add(iso.quad([(x0 + 0.15, y0 + CD - 0.32, zt), (x0 + CW - 0.15, y0 + CD - 0.32, zt),
                        (x0 + CW - 0.15, y0 + CD - 0.12, zt), (x0 + 0.15, y0 + CD - 0.12, zt)], BAR1, sw=0))
    if hero:
        g.add(Dot(iso.p(x0 + CW - 0.32, y0 + 0.44, zt), radius=max(0.045, 0.075 * iso.s), color=TERRA))
    if with_note:
        g.add(note(iso, x0, y0, z0, edge=edge, sw=max(2, sw - 1)))
    return g.set_z_index(2)


def mini(center, s=0.5, hero=False, with_note=True):
    """A small card (dark-kraft outline) centred on a screen point."""
    return card(rig_at(center, s), hero=hero, edge=DEV_EDGE, sw=2, with_note=with_note)


def document(iso):
    """The whole document: one long page, a grey header band at the far end, ghost lines per chunk region."""
    L = NCH * CD
    slab = iso.box(0, 0, 0, CW, L, CT, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    for f in slab:
        f.set_stroke(INK, 4)
    lines = VGroup(*[Line(iso.p(0.25, i * CD + f, CT), iso.p(CW - 0.6, i * CD + f, CT), color=GHOST,
                          stroke_width=max(2, 5 * iso.s)) for i in range(NCH) for f in (0.3, 0.58)])
    band = iso.quad([(0.15, L - 0.32, CT), (CW - 0.15, L - 0.32, CT), (CW - 0.15, L - 0.12, CT), (0.15, L - 0.12, CT)], BAR1, sw=0)
    dot = Dot(iso.p(CW - 0.32, HI * CD + 0.44, CT), radius=max(0.045, 0.075 * iso.s), color=TERRA)
    return VGroup(slab, lines, band, dot).set_z_index(2)


def claude_block(iso, w=1.5, h=1.3):
    """Claude: a kraft block with a terracotta spark on top."""
    base = iso.box(0, 0, 0, w, w, 0.34, DARK_TOP, DARK_L, DARK_R)
    body = iso.box(0, 0, 0.34, w, w, h - 0.34)
    c = iso.p(w / 2, w / 2, h) + UP * 0.05 * iso.s     # inside the top face: a spark that cuts the top-vertex outline leaves a sub-floor "text" fragment (GATE T)
    r = 0.34 * iso.s
    pts = []
    for k in range(16):
        a = PI / 2 + k * PI / 8
        rr = r if k % 2 == 0 else r * 0.42
        pts.append(c + np.array([rr * np.cos(a), rr * np.sin(a), 0]))
    spark = Polygon(*pts, fill_color=TERRA, fill_opacity=1, stroke_width=0)
    sh = iso.quad([(-0.15, -0.35, 0), (w + 0.3, -0.35, 0), (w + 0.3, w, 0), (-0.15, w, 0)], SHADOW, sw=0).set_z_index(-2)
    return VGroup(sh, base, body, spark).set_z_index(1)


def embed_block(iso, w=1.4, h=1.0):
    body = iso.box(0, 0, 0, w, w, h, DARK_TOP, DARK_L, DARK_R)
    ports = VGroup(*[iso.box(w * f, -0.14, h * 0.3, w * 0.18, 0.14, h * 0.32, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.22, 0.6)])
    return VGroup(body, ports).set_z_index(1)


IDX_W, IDX_D = 2.6, 2.2
IDX_PTS = [(0.35, 0.4), (0.8, 1.5), (1.3, 0.7), (1.9, 1.75), (2.2, 0.45), (0.5, 1.85), (1.55, 1.25), (2.25, 1.15),
           (1.0, 0.25), (0.3, 1.1)]
IDX_HIT = (1.7, 0.35)       # where the hero's dot lands


def index_map(iso):
    board = iso.quad([(0, 0, 0), (IDX_W, 0, 0), (IDX_W, IDX_D, 0), (0, IDX_D, 0)], PAD, stroke=INK, sw=4)
    dots = VGroup(*[Dot(iso.p(x, y, 0), radius=0.1 * iso.s, color=(BAR1, BAR2)[k % 2]) for k, (x, y) in enumerate(IDX_PTS)])
    return VGroup(board, dots).set_z_index(0)


def lens(c, r=0.5):
    c = np.array(c, dtype=float)
    ring = Circle(radius=r, stroke_color=INK, stroke_width=8, fill_opacity=0).move_to(c)
    d = np.array([0.707, -0.707, 0])
    handle = Line(c + d * r * 1.05, c + d * r * 2.0, color=INK, stroke_width=14)
    return VGroup(ring, handle).set_z_index(6)


def lab(s, at, size=46):
    return T(s, size).move_to(at)


# ══════════════ B00: the document is cut into chunks ══════════════
D0 = Iso(1.76, -2.09, 1.3)
GAP0 = 0.55


ROW0 = [4.55, 1.5, -1.55, -4.6]     # after the cut: one row, far chunk (the band) at the left; bboxes kept apart (GATE T)


def b00_cards(spread=True, lift=True):
    cs = []
    for i in range(NCH):
        if spread:
            c = card(rig_at([ROW0[i], -0.25, 0], 1.0), hero=(i == HI), band=(i == NCH - 1))
        else:
            c = card(D0, 0, i * CD, 0, hero=(i == HI), band=(i == NCH - 1))
        if spread and lift and i == HI:
            c.shift(UP * 0.3)
        cs.append(c)
    return cs


def cuts():
    return VGroup(*[DashedLine(D0.p(-0.35, i * CD, CT), D0.p(CW + 0.35, i * CD, CT), color=INK, stroke_width=6,
                               dash_length=0.14) for i in range(1, NCH)]).set_z_index(4)


def l_document():
    return lab("document", [-2.7, -1.45, 0])


def l_chunks():
    return lab("chunks", [0.0, -1.85, 0])


class B00_Cut(Scene):
    def construct(self):
        doc = document(D0)
        self.play(FadeIn(doc, shift=DOWN * 1.0), run_time=0.6, rate_func=ease_in)
        ldoc = l_document()
        self.play(FadeIn(ldoc), run_time=0.35)
        until(self, "cut into chunks", lead=0.35)
        ct = cuts()
        self.play(Create(ct, lag_ratio=0.3), run_time=0.7)
        flat = b00_cards(spread=False)
        self.remove(doc)
        self.add(*flat)
        tgt = b00_cards(spread=True, lift=False)
        self.play(*[Transform(a, b) for a, b in zip(flat, tgt)], FadeOut(ct), FadeOut(ldoc), run_time=0.7)
        self.play(FadeIn(l_chunks()), run_time=0.35)
        until(self, "just the piece", lead=0.3)
        self.play(flat[HI].animate.shift(UP * 0.3), Flash(np.array(flat[HI][-1].get_center()), color=TERRA,
                                                          line_length=0.2, flash_radius=0.35), run_time=0.5)
        done(self)


def b00_state():
    return VGroup(*b00_cards(), l_chunks())


# ══════════════ B01: a chunk alone has lost its context ══════════════
R1 = rig_at([0.0, -0.5, 0], 2.4)
LENS_A, LENS_B = np.array([-3.8, 2.35, 0]), np.array([4.5, 2.35, 0])
Q_AT = [3.75, 0.45, 0]


def l_chunk1():
    return lab("chunk", [-3.95, -1.6, 0])


def l_q():
    return T("?", 110, INK, bold=True).move_to(Q_AT)


def search_grp(c):
    c = np.array(c, dtype=float)
    return VGroup(lens(c), T("search", 40).move_to(c + np.array([-1.55, 0.0, 0])))


class B01_Lost(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        hero = st[HI]
        others = VGroup(*[st[i] for i in range(NCH) if i != HI], st[NCH])
        self.play(FadeOut(others), run_time=0.45)
        tgt = card(R1, hero=True)
        self.play(Transform(hero, tgt), run_time=0.75)
        self.play(FadeIn(l_chunk1()), run_time=0.3)
        until(self, "which file", lead=0.3)
        self.play(FadeIn(l_q(), scale=0.6), run_time=0.4)
        until(self, "Embedded alone", lead=0.4)
        sg = search_grp(LENS_A)
        self.play(FadeIn(sg), run_time=0.35)
        self.play(sg.animate.shift(LENS_B - LENS_A), run_time=1.3, rate_func=linear)
        done(self)


def b01_state():
    return VGroup(card(R1, hero=True), l_chunk1(), l_q(), search_grp(LENS_B))


# ══════════════ B02: Claude reads the whole document and writes a note ══════════════
CL2 = Iso(-0.4, -2.1, 1.25)
DL2 = Iso(-3.0, -2.55, 0.7)
CR2 = rig_at([3.7, -0.6, 0], 1.35)
NOTE_FROM = CL2.p(0.75, 0.75, 1.3) + UP * 0.2


def l_claude2():
    return lab("Claude", [-0.4, -2.75, 0])


def l_doc2():
    return lab("document", [-4.6, 0.25, 0])


def l_context2():
    return lab("context", [2.9, 1.3, 0])


def read_lines():
    a = DashedLine(DL2.p(CW + 0.1, 1.2 * CD, CT), CL2.p(-0.1, 0.9, 0.7), color=INK, stroke_width=5, dash_length=0.12)
    b = DashedLine(CR2.p(-0.12, CD * 0.5, CT), CL2.p(1.2, 1.45, 0.9) + RIGHT * 0.15, color=INK, stroke_width=5, dash_length=0.12)
    return VGroup(a, b).set_z_index(0)


class B02_Note(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        hero = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3])), run_time=0.4)
        self.play(Transform(hero, card(CR2, hero=True)), run_time=0.7)
        until(self, "For each chunk", lead=0.3)
        cl = claude_block(CL2)
        self.play(FadeIn(cl, shift=DOWN * 1.0), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(l_claude2()), run_time=0.3)
        until(self, "the whole document", lead=0.35)
        doc = document(DL2)
        self.play(FadeIn(doc, shift=RIGHT * 0.8), FadeIn(l_doc2()), run_time=0.55)
        until(self, "and the chunk,", lead=0.2)
        rl = read_lines()
        self.play(Create(rl), run_time=0.5)
        until(self, "writes a short note", lead=0.3)
        nt = note(CR2, sw=2)
        tgt_c = np.array(nt.get_center())
        nt.shift(NOTE_FROM - tgt_c)
        self.play(FadeIn(nt, scale=0.5), run_time=0.3)
        self.play(MoveAlongPath(nt, ArcBetweenPoints(NOTE_FROM, tgt_c, angle=-0.9)), run_time=0.8)
        self.play(FadeIn(l_context2()), run_time=0.3)
        until(self, "and nothing else", lead=0.3)
        self.play(Indicate(nt, color=None, scale_factor=1.12), run_time=0.5)
        done(self)


def b02_state():
    return VGroup(card(CR2, hero=True, with_note=True), claude_block(CL2), document(DL2), read_lines(),
                  l_claude2(), l_doc2(), l_context2())


# ══════════════ B03: note + chunk are embedded together, into the index ══════════════
LC3 = rig_at([-4.3, -0.3, 0], 1.2)
EB3 = Iso(-0.6, -1.8, 1.3)
IX3 = Iso(3.3, -2.2, 1.1)


def l_embed():
    return lab("embed", [-0.6, -2.5, 0])


def l_index3():
    return lab("index", [3.3, -2.8, 0])


def hit_dot(iso):
    return Dot(iso.p(*IDX_HIT, 0), radius=0.13 * iso.s, color=TERRA).set_z_index(3)


class B03_Embed(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        hero = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 7)])), run_time=0.4)
        self.play(Transform(hero, card(LC3, hero=True, with_note=True)), run_time=0.6)
        eb, ix = embed_block(EB3), index_map(IX3)
        self.play(FadeIn(eb, shift=DOWN * 0.8), FadeIn(ix), FadeIn(l_embed()), FadeIn(l_index3()), run_time=0.5)
        until(self, "embedded together", lead=0.3)
        mouth = EB3.p(0.0, 0.7, 0.55)
        self.play(hero.animate.scale(0.45).move_to(mouth), run_time=0.7, rate_func=ease_in)
        self.play(FadeOut(hero), run_time=0.2)
        until(self, "carries its context", lead=0.4)
        d = hit_dot(IX3)
        src = EB3.p(1.4, 0.7, 0.8) + RIGHT * 0.15
        tgt = np.array(d.get_center())
        d.move_to(src)
        self.add(d)
        self.play(MoveAlongPath(d, ArcBetweenPoints(src, tgt, angle=-1.0)), run_time=0.8)
        self.play(Flash(tgt, color=TERRA, line_length=0.2, flash_radius=0.35), run_time=0.4)
        done(self)


def b03_state():
    return VGroup(embed_block(EB3), index_map(IX3), hit_dot(IX3), l_embed(), l_index3())


# ══════════════ B04: 35% fewer top-20 retrieval failures ══════════════
BX0, BW, BH = -3.6, 6.0, 0.9
BY1, BY2 = -0.55, -2.05
KEEP = 0.65                  # "reduced ... by 35%": the second bar keeps 65% of the first


def bar(y, w, fill):
    return Rectangle(width=w, height=BH, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([BX0 + w / 2, y, 0])


def icons():
    return VGroup(mini([BX0 - 1.3, BY1, 0], 0.8, with_note=False), mini([BX0 - 1.3, BY2, 0], 0.8, with_note=True))


def l_fail():
    return lab("top-20 failures", [BX0 + 2.2, 0.5, 0], 46)


def l_35():
    return T("35%", 150, INK, bold=True).move_to([3.7, 2.05, 0])


def l_per():
    return lab("per Anthropic's notebook", [3.55, 0.75, 0], 38)


def gap_rect():
    w = BW * (1 - KEEP)
    return Rectangle(width=w - 0.08, height=BH, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(
        [BX0 + BW * KEEP + 0.04 + (w - 0.08) / 2, BY2, 0]).set_z_index(-1)


class B04_Fewer(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        until(self, "Averaged across", lead=0.3)
        b1, b2 = bar(BY1, BW, BAR1), bar(BY2, BW, BAR1)
        ic = icons()
        self.play(FadeIn(ic[0]), GrowFromEdge(b1, LEFT), run_time=0.6)
        self.play(FadeIn(ic[1]), GrowFromEdge(b2, LEFT), FadeIn(l_fail()), run_time=0.6)
        until(self, "by thirty five percent", lead=0.35)
        g = gap_rect()
        self.add(g)
        self.play(Transform(b2, bar(BY2, BW * KEEP, BAR1)), run_time=0.8)
        self.play(FadeIn(l_35()), run_time=0.4)
        until(self, "That's from Anthropic's notebook", lead=0.3)
        self.play(FadeIn(l_per()), run_time=0.4)
        until(self, "embeddings alone", lead=0.3)
        self.play(Indicate(ic[1], color=None, scale_factor=1.15), run_time=0.6)
        done(self)


def b04_state():
    return VGroup(bar(BY1, BW, BAR1), bar(BY2, BW * KEEP, BAR1), gap_rect(), icons(), l_fail(), l_35(), l_per())


# ══════════════ B05: prompt caching makes one call per chunk practical ══════════════
CL5 = Iso(-0.3, -1.2, 1.05)
SH5 = Iso(-3.55, 0.95, 0.55)
DOC5 = Iso(-4.4, -1.6, 0.5)
LANE_Y = -2.6
SPOT5 = np.array([-0.3, LANE_Y, 0])       # the card spot under Claude
IX5 = Iso(4.0, -1.75, 0.6)
XS5 = [-5.3, -3.5, -1.7]
STEP5 = 1.8
MINI_S = 0.7


def shelf():
    b = SH5.box(-0.25, -0.25, -0.35, 2.1, NCH * CD + 0.5, 0.3)
    return b.set_z_index(0)


def lane():
    top = Rectangle(width=12.2, height=0.9, fill_color=BELT, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=2).move_to([0, LANE_Y, 0])
    return top.set_z_index(-2)


def l_claude5():
    return lab("Claude", [1.9, 1.35, 0])


def l_cache():
    return lab("cache", [-5.35, 0.55, 0])


def l_off():
    return lab("90% off", [-1.05, 2.6, 0], 46)


def cache_line():
    return DashedLine(SH5.p(1.85, 1.2, 0.1), CL5.p(0.3, 1.2, 1.3) + UP * 0.1, color=INK, stroke_width=5, dash_length=0.12).set_z_index(4)


def lane_card(x, hero=False, with_note=False):
    return mini([x, LANE_Y + 0.05, 0], MINI_S, hero=hero, with_note=with_note).set_z_index(5)


def ix5():
    return index_map(IX5)


class B05_Cache(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        cl, doc = claude_block(CL5), document(DOC5)
        self.play(FadeIn(cl, shift=DOWN * 0.8), FadeIn(doc, shift=RIGHT * 0.6), FadeIn(l_claude5()), run_time=0.5)
        until(self, "once per chunk", lead=0.4)
        into = CL5.p(0.75, 0.75, 0.6)
        copies = [document(DOC5) for _ in range(2)]
        for c in copies:
            self.add(c)
            self.play(c.animate.scale(0.3).move_to(into).set_opacity(0.0), run_time=0.55, rate_func=ease_in)
        until(self, "Prompt caching", lead=0.3)
        sh = shelf()
        self.play(FadeIn(sh, shift=DOWN * 0.5), FadeIn(l_cache()), run_time=0.45)
        until(self, "writes the document to the cache", lead=0.3)
        self.play(Transform(doc, document(SH5)), run_time=0.8)
        self.play(FadeIn(lane()), run_time=0.3)
        until(self, "Every later chunk", lead=0.4)
        xs = XS5
        cards = [lane_card(x, hero=(k == 1)) for k, x in enumerate(xs)]
        self.play(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards], run_time=0.35)
        cln = cache_line()
        off_shown = False
        for k in range(3):
            step = SPOT5[0] - xs[2] if k == 0 else STEP5
            self.play(*[c.animate.shift(RIGHT * step) for c in cards], run_time=0.45)
            here = cards[2 - k]
            nt = note(rig_at([SPOT5[0], LANE_Y + 0.05, 0], MINI_S), edge=DEV_EDGE, sw=2).set_z_index(6)
            ntc = np.array(nt.get_center())
            nt.shift(CL5.p(0.75, 0.0, 0.2) - ntc)
            if not off_shown:
                self.play(Create(cln), FadeIn(l_off()), run_time=0.35)
                off_shown = True
            else:
                self.play(Indicate(cln, color=None, scale_factor=1.0), run_time=0.3)
            self.play(nt.animate.move_to(ntc), run_time=0.3)
            here.add(nt)
        until(self, "paid once", lead=0.3)
        ix = ix5()
        self.play(FadeIn(ix), FadeOut(cln), run_time=0.4)
        self.play(*[c.animate.shift(RIGHT * 2.0) for c in cards], run_time=0.6)
        done(self)


def b05_state():
    xs = [x + (SPOT5[0] - XS5[2]) + 2 * STEP5 + 2.0 for x in XS5]
    cs = VGroup(*[lane_card(x, hero=(k == 1), with_note=True) for k, x in enumerate(xs)])
    return VGroup(claude_block(CL5), document(SH5), shelf(), lane(), cs, ix5(), l_claude5(), l_cache(), l_off())


# ══════════════ B06: BM25 alongside embeddings, two rankings merged ══════════════
IXL = Iso(-4.0, -1.45, 0.95)
BMR = Iso(3.7, -1.45, 0.95)
SLIPS = [(0.3, 0.35, 0.9), (1.4, 0.35, 0.8), (0.3, 1.0, 0.7), (1.25, 1.0, 1.0), (0.3, 1.65, 1.1), (1.6, 1.65, 0.6)]
BM_HIT = (1, 4)
IX_HIT2 = (2, 6)
LENS6 = np.array([0.0, 2.4, 0])
COL = [np.array([0.0, y, 0]) for y in (0.9, -0.05, -1.0, -1.95)]
HERO_ROW6 = 1


def bm25_board(iso):
    board = iso.quad([(0, 0, 0), (IDX_W, 0, 0), (IDX_W, IDX_D, 0), (0, IDX_D, 0)], BOX_TOP, stroke=INK, sw=4)
    slips = VGroup(*[iso.quad([(x, y, 0), (x + w, y, 0), (x + w, y + 0.36, 0), (x, y + 0.36, 0)], (BAR1, BAR2)[k % 2], sw=0)
                     for k, (x, y, w) in enumerate(SLIPS)])
    return VGroup(board, slips).set_z_index(0)


def bm_dot(k):
    x, y, w = SLIPS[k]
    return Dot(BMR.p(x + w + 0.22, y + 0.18, 0), radius=0.1, color=TERRA).set_z_index(3)


def ix_dot(k):
    x, y = IDX_PTS[k]
    return Dot(IXL.p(x, y, 0), radius=0.1 * IXL.s * 1.05, color=TERRA).set_z_index(3)


def l_emb6():
    return lab("embeddings", [-3.95, -2.2, 0])


def l_bm6():
    return lab("BM25", [3.75, -2.2, 0])


def l_list6():
    return lab("one list", [0.0, -2.85, 0])


def col_cards(n=4, rows=None):
    rows = rows or COL
    return VGroup(*[mini(rows[k], 0.6, hero=(k == HERO_ROW6)) for k in range(n)])


def search_lines():
    return VGroup(DashedLine(LENS6 + np.array([-0.55, -0.35, 0]), IXL.p(1.9, 1.9, 0) + UP * 0.25, color=INK, stroke_width=5, dash_length=0.12),
                  DashedLine(LENS6 + np.array([0.45, -0.55, 0]), BMR.p(0.5, 1.6, 0) + UP * 0.35 + LEFT * 0.3, color=INK, stroke_width=5, dash_length=0.12)).set_z_index(4)


class B06_TwoWays(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        ix = st[5]
        self.play(FadeOut(VGroup(*[st[i] for i in (0, 1, 2, 3, 4, 6, 7, 8)])), run_time=0.45)
        self.play(to_rig(ix, IX5, IXL), FadeIn(l_emb6()), run_time=0.6)
        until(self, "keyword search", lead=0.3)
        bm = bm25_board(BMR)
        self.play(FadeIn(bm, shift=DOWN * 0.6), FadeIn(l_bm6()), run_time=0.5)
        until(self, "catches exact words", lead=0.3)
        self.play(LaggedStart(*[FadeIn(bm_dot(k), scale=0.5) for k in BM_HIT], lag_ratio=0.4), run_time=0.6)
        until(self, "searches each chunk", lead=0.4)
        ln = lens(LENS6)
        self.play(FadeIn(ln, shift=DOWN * 0.4), run_time=0.4)
        sl = search_lines()
        self.play(Create(sl), run_time=0.5)
        self.play(*[FadeIn(ix_dot(k), scale=0.5) for k in IX_HIT2], run_time=0.35)
        until(self, "merges the two rankings", lead=0.3)
        cc = col_cards()
        srcs = [IXL.p(*IDX_PTS[IX_HIT2[0]], 0.1), BMR.p(1.9, 0.5, 0.1), IXL.p(*IDX_PTS[IX_HIT2[1]], 0.1), BMR.p(1.9, 1.8, 0.1)]
        for c, s in zip(cc, srcs):
            c.scale(0.4).move_to(s)
        self.add(*cc)
        self.play(FadeOut(sl), *[c.animate.scale(2.5).move_to(COL[k]) for k, c in enumerate(cc)], run_time=0.8)
        self.play(FadeIn(l_list6()), run_time=0.3)
        done(self)


def b06_state():
    return VGroup(index_map(IXL), bm25_board(BMR), VGroup(*[bm_dot(k) for k in BM_HIT]), VGroup(*[ix_dot(k) for k in IX_HIT2]),
                  lens(LENS6), col_cards(), l_emb6(), l_bm6(), l_list6())


# ══════════════ B07: rerank, keep the best few, back to Claude ══════════════
CX7 = -1.6
ROWS7 = [np.array([CX7, y, 0]) for y in (2.35, 1.4, 0.45, -0.5, -1.45, -2.4)]
ORDER7 = [3, 0, 2, 1, 4, 5]          # before: the hero (card 1 of the list) sits 4th; after: first
RB7 = Iso(-4.8, -1.0, 1.05)
CL7 = Iso(3.6, -2.4, 1.05)
BEST = [np.array([1.2, y, 0]) for y in (2.3, 1.35, 0.4)]
LENS7 = np.array([-4.7, 2.55, 0])
FINAL7 = {1: 0, 0: 1, 2: 2, 3: 3, 4: 4, 5: 5}     # after the rerank: the hero first


def rr_block():
    body = RB7.box(0, 0, 0, 1.2, 1.2, 1.1, DARK_TOP, DARK_L, DARK_R)
    lamp = Dot(RB7.p(0.6, 0.6, 1.1) + UP * 0.28, radius=0.13, color=TERRA)
    return VGroup(body, lamp).set_z_index(1)


def pad7():
    return RoundedRectangle(width=2.2, height=6.3, corner_radius=0.2, fill_color=PAD, fill_opacity=1, stroke_width=0).move_to([CX7, 0.05, 0]).set_z_index(-2)


def l_rr():
    return lab("reranker", [-4.8, -1.8, 0])


def l_best():
    return lab("best few", [3.4, 1.85, 0])


def l_claude7():
    return lab("Claude", [3.6, -2.95, 0])


def cards7():
    """Six candidates; card k is the hero when k == 1 (it stays the list's second card from B06)."""
    return [mini(ROWS7[ORDER7.index(k)], 0.6, hero=(k == 1)) for k in range(6)]


class B07_Rerank(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        col = st[5]
        self.play(FadeOut(VGroup(st[0], st[1], st[2], st[3], st[6], st[7], st[8])), st[4].animate.move_to(LENS7), run_time=0.5)
        cs = cards7()
        until(self, "Pull more candidates", lead=0.35)
        pd = pad7()
        self.add(pd)
        self.play(*[Transform(col[k], cs[k]) for k in range(4)], FadeIn(pd), run_time=0.6)
        self.play(FadeIn(cs[4], shift=UP * 0.3), FadeIn(cs[5], shift=UP * 0.3), run_time=0.4)
        cards = [col[0], col[1], col[2], col[3], cs[4], cs[5]]
        until(self, "a reranking model", lead=0.4)
        rb = rr_block()
        self.play(FadeIn(rb, shift=DOWN * 0.6), FadeIn(l_rr()), run_time=0.45)
        until(self, "scores each one", lead=0.3)
        scan = Line([CX7 - 1.0, 2.95, 0], [CX7 + 1.0, 2.95, 0], color=TERRA, stroke_width=10).set_z_index(8)
        self.add(scan)
        rt = guard(self, 1.2)
        self.play(scan.animate.move_to([CX7, -2.9, 0]), run_time=rt, rate_func=linear)
        self.remove(scan)
        until(self, "keeps only the best few", lead=0.4)
        self.play(*[cards[k].animate.move_to(ROWS7[FINAL7[k]]) for k in range(6)], run_time=0.7)
        self.play(*[FadeOut(cards[k]) for k in (3, 4, 5)], run_time=0.35)
        top3 = [cards[1], cards[0], cards[2]]
        until(self, "comes back to Claude", lead=0.4)
        cl = claude_block(CL7)
        self.play(FadeIn(cl, shift=DOWN * 0.8), FadeIn(l_claude7()), run_time=0.45)
        self.play(*[top3[k].animate.move_to(BEST[k]) for k in range(3)], FadeOut(pd), run_time=0.7)
        self.play(FadeIn(l_best()), Indicate(top3[0], color=None, scale_factor=1.12), run_time=0.45)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Cut, B01_Lost, B02_Note, B03_Embed, B04_Fewer, B05_Cache, B06_TwoWays, B07_Rerank):
    _cls.play = ST.play
