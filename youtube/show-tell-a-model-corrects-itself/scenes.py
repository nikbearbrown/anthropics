"""
Manim scenes for show-tell-a-model-corrects-itself (show-tell skill, card #23, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Constitutional AI, the 2022 method exactly as the paper describes it (arXiv 2212.08073, Bai et al., Anthropic):
THE MODEL (a kraft block with a dark mouth on a dark plinth; no spark, it is not Claude) starts helpful-only and answers
the paper's example request with a harmful ANSWER PAGE. The CONSTITUTION is a deck of sixteen kraft principle cards,
each split into a critique half and a revision half. One card is drawn at random; a PEN strikes the harmful lines and a
CRITIQUE slip comes out; the card's revision half turns the page into a clean REVISION. The loop runs four rounds per
prompt (per the paper) and the revisions pile up; a model is fine-tuned on them plus grey helpful pages (stage 1).
Stage 2: the fine-tuned model writes TWO ANSWERS, a separate dark FEEDBACK MODEL picks one by a principle from its own
second deck (grey probability bars, a terracotta dot on the pick); the AI labels and a tray of human helpfulness labels
train a PREFERENCE MODEL (a kraft block with a tall score gauge); in RL its score is the reward. Last: harmless but not
evasive, the paper's over-training warning (boilerplate), and "2022": the paper's method, not a claim about today.
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




# ═════════════════════════════ the film: a model corrects itself by a rulebook ═════════════════════════════
SHADOW = "#AFA28A"
# dark faces for the feedback model: darker than DARK_* so GATE T's ink tolerance (48 from INK) never reads the
# block as one giant ink "text" blob (the #20 builder's fix for its tool wall).
FB_TOP, FB_L, FB_R = "#161411", "#121010", "#0E0C0A"


def lab(s, at, size=46):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


def grey_edges(mob, color=BAR1, w=3):
    for f in mob.family_members_with_points():
        f.set_stroke(color, w)
    return mob


# ─────────────── THE MODEL: a kraft block with a dark mouth on a dark plinth (no spark: it is not Claude) ───────────────
M = Iso(-4.75, -2.2, 1.15)
MW, MPL, MH = 1.4, 0.3, 1.7
MOUTH = M.p(0.7, 0, 0.95)
SLOT = M.p(0.7, 0.7, MH)


def model(tuned=False):
    sh = M.quad([(-0.15, -0.3, 0), (MW + 0.25, -0.3, 0), (MW + 0.25, MW, 0), (-0.15, MW, 0)], SHADOW, sw=0).set_z_index(-2)
    plinth = M.box(0, 0, 0, MW, MW, MPL, DARK_TOP, DARK_L, DARK_R)
    body = M.box(0, 0, MPL, MW, MW, MH - MPL)
    mouth = M.quad([(0.3, 0, 0.75), (1.1, 0, 0.75), (1.1, 0, 1.15), (0.3, 0, 1.15)], DARK_L, sw=0)
    slot = M.quad([(0.4, 0.55, MH), (1.0, 0.55, MH), (1.0, 0.85, MH), (0.4, 0.85, MH)], DARK_TOP, sw=0)
    g = VGroup(sh, plinth, body, mouth, slot)
    if tuned:
        g.add(band(), lamp())
    return g.set_z_index(1)


def band(z0=1.38, z1=1.52):
    """The fine-tuned model's grey band round both front faces."""
    return VGroup(M.quad([(0, 0, z0), (MW, 0, z0), (MW, 0, z1), (0, 0, z1)], BAR1, sw=0),
                  M.quad([(0, 0, z0), (0, MW, z0), (0, MW, z1), (0, 0, z1)], BAR1, sw=0)).set_z_index(1)


def lamp():
    return Dot(M.p(0.3, 0.3, MH), radius=0.1, color=TERRA).set_z_index(1)


def l_model(s="helpful model"):
    return lab(s, [-4.55, -2.8], 42)


# ─────────────── ANSWER PAGES: white upright pages with grey lines; harmful lines darker ───────────────
PG = Iso(-2.3, -2.15, 1.1)
PW, PH = 2.2, 2.8
LINES = [(2.35, 1.7), (2.0, 1.45), (1.65, 1.75), (1.3, 1.25), (0.95, 1.6), (0.6, 1.1)]   # (z, length)
HARM = [1, 3]


def page(iso=PG):
    return iso.box(0, 0, 0, PW, 0.08, PH, PAGE_TOP, PAGE_L, PAGE_TOP).set_z_index(3)


def pline(iso, k, color=BAR2, w=12, x0=0.28):
    z, ln = LINES[k]
    return Line(iso.p(x0, -0.01, z), iso.p(x0 + ln, -0.01, z), color=color, stroke_width=w * iso.s).set_z_index(4)


def page_lines(iso=PG, harm=True):
    return VGroup(*[pline(iso, k, BAR1 if (harm and k in HARM) else BAR2, 16 if (harm and k in HARM) else 12)
                    for k in range(len(LINES))])


def strike(k, iso=PG):
    z, ln = LINES[k]
    return Line(iso.p(0.18, -0.02, z), iso.p(0.38 + ln, -0.02, z), color=INK, stroke_width=7).set_z_index(5)


def page_check(iso=PG):
    c = iso.p(1.75, -0.02, 0.35)
    return check(c[0], c[1], s=0.24 * iso.s).set_z_index(5)


def harm_dots(iso=PG):
    """Terracotta flags at the left margin of the harmful lines."""
    return VGroup(*[Dot(iso.p(0.14, -0.02, LINES[k][0]), radius=0.07, color=TERRA) for k in HARM]).set_z_index(5)


def l_answer():
    return lab("answer", [-3.35, 1.85])


# ─────────────── the request slip, the critique slip (flat, white, ink edge) ───────────────
def slip(center, w=1.3, h=0.62, n=2):
    body = RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ys = [h * 0.17, -h * 0.17] if n == 2 else [0]
    ln = VGroup(*[Line([-w * 0.32, y, 0], [w * (0.32 if i == 0 else 0.12), y, 0], color=BAR1, stroke_width=6) for i, y in enumerate(ys)])
    return VGroup(body, ln).move_to(center).set_z_index(8)


REQ_AT = P(-2.5, 2.55)


def l_request():
    return lab("request", [-0.6, 2.55])


CRIT_AT = P(-4.55, 2.35)


def l_critique_slip():
    return lab("critique", [-4.55, 3.05])


# ─────────────── the CONSTITUTION: a kraft deck of principle cards ───────────────
DK = Iso(4.1, -2.45, 1.25)
DW, DD, DHH = 1.4, 1.0, 0.8
DECK_TOP = DK.p(DW / 2, DD / 2, DHH)


def deck():
    sh = DK.quad([(-0.1, -0.3, 0), (DW + 0.2, -0.3, 0), (DW + 0.2, DD, 0), (-0.1, DD, 0)], SHADOW, sw=0).set_z_index(-2)
    body = DK.box(0, 0, 0, DW, DD, DHH)
    edges = VGroup(*[Line(DK.p(0.1, -0.01, z), DK.p(DW - 0.1, -0.01, z), color=BOX_IN2, stroke_width=4) for z in (0.2, 0.35, 0.5, 0.65)])
    return VGroup(sh, body, edges).set_z_index(1)


def l_constitution():
    return lab("constitution", [4.35, -3.0])


def mini_card(center, s=1.0):
    """One of the sixteen: a small kraft card, split in two halves."""
    w, h = 0.52 * s, 0.72 * s
    body = Rectangle(width=w, height=h, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=3)
    div = Line([-w * 0.38, 0, 0], [w * 0.38, 0, 0], color=BAR1, stroke_width=3)
    return VGroup(body, div).move_to(center).set_z_index(6)


GRID = [P(0.55 + c * 0.72, 2.55 - r * 0.95) for r in range(2) for c in range(8)]


def l_sixteen():
    return lab("16 principles", [-1.35, 2.7])


# the big principle card, standing between the page and the deck
CARD_C = P(1.3, 0.45)
CW_, CH_ = 1.7, 2.3


def big_card(center=CARD_C, s=1.0):
    w, h = CW_ * s, CH_ * s
    body = Rectangle(width=w, height=h, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    div = Line([-w * 0.42, 0, 0], [w * 0.42, 0, 0], color=BAR1, stroke_width=5)
    return VGroup(body, div).move_to(center).set_z_index(6)


def card_half_lines(half, center=CARD_C, s=1.0):
    """Grey lines in the top half (the critique request) or bottom half (the revision request)."""
    w, h = CW_ * s, CH_ * s
    if half == 0:
        ys, lens = [h * 0.36, h * 0.24, h * 0.12], [0.62, 0.7, 0.4]
    else:
        ys, lens = [-h * 0.14, -h * 0.26], [0.7, 0.5]
    x0 = -w * 0.28
    return VGroup(*[Line([x0, y, 0], [x0 + L * w, y, 0], color=BAR1, stroke_width=7) for y, L in zip(ys, lens)]).shift(center).set_z_index(7)


def card_dot(half, center=CARD_C, s=1.0):
    w, h = CW_ * s, CH_ * s
    return Dot(center + np.array([-w * 0.36, (h * 0.24) if half == 0 else (-h * 0.2), 0]), radius=0.08, color=TERRA).set_z_index(7)


def l_principle(at=(1.3, 2.05)):
    return lab("principle", at)


B01C = P(3.6, -0.5)


def l_critique_half():
    return lab("critique", [1.75, 0.0])


def l_revise_half():
    return lab("revise", [1.95, -1.05])


# ─────────────── the pen ───────────────
def pen(tip):
    L, W = 1.5, 0.26
    body = Polygon([0, 0, 0], [0.25, W / 2, 0], [L, W / 2, 0], [L, -W / 2, 0], [0.25, -W / 2, 0],
                   fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    nib = Polygon([0, 0, 0], [0.25, W / 2, 0], [0.25, -W / 2, 0], fill_color=INK, fill_opacity=1, stroke_width=0)
    g = VGroup(body, nib).rotate(PI / 5, about_point=ORIGIN).shift(tip)
    return g.set_z_index(9)


def line_start(k, iso=PG):
    z, ln = LINES[k]
    return np.array(iso.p(0.2, -0.02, z))


def line_end(k, iso=PG):
    z, ln = LINES[k]
    return np.array(iso.p(0.38 + ln, -0.02, z))


# ─────────────── the pile of revised answers ───────────────
PL = Iso(0.8, -2.85, 1.25)
PLW, PLD, PSTEP = 1.2, 0.85, 0.09


def pile(level):
    h = max(level, 0.001) * PSTEP
    body = PL.box(0, 0, 0, PLW, PLD, h, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    for f in body:
        f.set_stroke(BOX_IN2, 3)
    ln = VGroup(*[Line(PL.p(0.06, -0.01, k * PSTEP), PL.p(PLW - 0.06, -0.01, k * PSTEP), color=BAR2, stroke_width=4) for k in range(1, level)])
    return VGroup(body, ln).set_z_index(2)


def pile_top(level):
    return np.array(PL.p(PLW / 2, PLD / 2, level * PSTEP))


def l_revisions():
    return lab("revisions", [-1.15, -2.8])


# the helpful answers (grey pages) that are mixed in
HP = Iso(3.6, -2.85, 1.25)


def helpful_pile(level=5):
    h = level * PSTEP
    body = HP.box(0, 0, 0, PLW, PLD, h, BAR3, BAR2, BAR2, sw=3)
    for f in body:
        f.set_stroke(BAR1, 3)
    return VGroup(body).set_z_index(2)


def l_helpful():
    return lab("helpful", [4.3, -0.6])


# ─────────────── round counter (ink numerals) ───────────────
def l_rounds():
    return T("4 rounds", 96, INK, bold=True).move_to([-3.4, 2.75, 0])


def l_perpaper(at=(-3.4, 2.0)):
    return lab("per the paper", at, 38)


# ─────────────── STAGE 2: two answers, the feedback model ───────────────
PA = Iso(-2.75, -1.95, 0.72)
PB = Iso(-0.75, -1.95, 0.72)


def small_page(iso):
    return VGroup(page(iso), page_lines(iso, harm=False))


def l_two():
    return lab("two answers", [-1.0, -2.6])


FB = Iso(3.55, -2.35, 1.0)
FW_, FH_ = 1.5, 1.4


def feedback_model():
    sh = FB.quad([(-0.15, -0.3, 0), (FW_ + 0.25, -0.3, 0), (FW_ + 0.25, FW_, 0), (-0.15, FW_, 0)], SHADOW, sw=0).set_z_index(-2)
    body = FB.box(0, 0, 0, FW_, FW_, FH_, FB_TOP, FB_L, FB_R)
    return VGroup(sh, body).set_z_index(1)


def fb_lamp(color=GHOST):
    return Dot(FB.p(1.05, 0, 0.95), radius=0.11, color=color).set_z_index(2)


def fb_deck():
    """The second list: a small kraft deck on the feedback model's top."""
    body = FB.box(0.35, 0.35, FH_, 0.8, 0.8, 0.35)
    edges = VGroup(*[Line(FB.p(0.42, 0.34, FH_ + z), FB.p(1.08, 0.34, FH_ + z), color=BOX_IN2, stroke_width=4) for z in (0.12, 0.24)])
    return VGroup(body, edges).set_z_index(2)


FB_DECK_TOP = FB.p(0.75, 0.75, FH_ + 0.35)


def l_feedback():
    return lab("feedback model", [3.7, -2.95])


BRACKET_Y = -2.2


def pair_bracket():
    return VGroup(Line([-2.7, BRACKET_Y, 0], [0.75, BRACKET_Y, 0], color=BAR1, stroke_width=6),
                  Line([-2.7, BRACKET_Y, 0], [-2.7, BRACKET_Y + 0.2, 0], color=BAR1, stroke_width=6),
                  Line([0.75, BRACKET_Y, 0], [0.75, BRACKET_Y + 0.2, 0], color=BAR1, stroke_width=6)).set_z_index(2)


RL_CARD_C = P(-0.95, 2.1)


def rl_card(center=RL_CARD_C):
    body = Rectangle(width=1.9, height=1.0, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ln = VGroup(*[Line([-0.65, y, 0], [-0.65 + L, y, 0], color=BAR1, stroke_width=7) for y, L in ((0.2, 1.25), (0.0, 1.05), (-0.2, 0.7))])
    return VGroup(body, ln).move_to(center).set_z_index(6)


def l_principle2():
    return lab("principle", [1.25, 2.1])


PROB_Y = -2.2


def prob_bar(k, frac):
    x0 = -2.7 if k == 0 else -0.7
    return Rectangle(width=max(frac * 1.45, 0.02), height=0.18, fill_color=BAR1 if k == 0 else BAR2, fill_opacity=1,
                     stroke_width=0).move_to([x0 + max(frac * 1.45, 0.02) / 2, PROB_Y, 0]).set_z_index(3)


def pick_dot():
    c = PA.p(PW, -0.02, PH)
    return Dot(np.array(c) + np.array([0.0, 0.25, 0]), radius=0.12, color=TERRA).set_z_index(6)


def l_pick():
    return lab("pick", [-3.35, 1.3])


# ─────────────── labels, trays, the preference model with its score gauge ───────────────
def label_card(center, grey=False):
    body = Rectangle(width=0.62, height=0.42, fill_color=BAR3 if grey else PAGE_TOP, fill_opacity=1,
                     stroke_color=BAR1, stroke_width=3)
    bar = VGroup(Rectangle(width=0.28, height=0.08, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([-0.1, 0, 0]),
                 Rectangle(width=0.12, height=0.08, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([0.16, 0, 0]))
    return VGroup(body, bar).move_to(center).set_z_index(8)


TA = Iso(-2.3, -2.85, 1.0)
TH_ = Iso(0.3, -2.85, 1.0)
TRW, TRD, TRH = 1.2, 0.8, 0.35


def tray(iso):
    back, front = iso.open_box(0, 0, 0, TRW, TRD, TRH)
    return VGroup(back.set_z_index(2), front.set_z_index(4))


def tray_in(iso):
    return np.array(iso.p(TRW / 2, TRD / 2, TRH * 0.6))


def tray_fill(iso, grey=False):
    body = iso.box(0.15, 0.15, 0.02, TRW - 0.3, TRD - 0.3, 0.2, BAR3 if grey else PAGE_TOP, BAR2 if grey else PAGE_L,
                   BAR2 if grey else PAGE_R, sw=3)
    for f in body:
        f.set_stroke(BAR1, 3)
    return VGroup(body).set_z_index(3)


def l_ailabels():
    return lab("AI labels", [-2.25, -0.95], 38)


def l_humanlabels():
    return lab("human labels", [0.6, -0.95], 38)


PMI = Iso(3.7, -2.35, 1.0)
PMW, PMH = 1.5, 1.4
PM_SLOT = PMI.p(0.75, 0.75, PMH)


def pref_model():
    sh = PMI.quad([(-0.15, -0.3, 0), (PMW + 0.25, -0.3, 0), (PMW + 0.25, PMW, 0), (-0.15, PMW, 0)], SHADOW, sw=0).set_z_index(-2)
    plinth = PMI.box(0, 0, 0, PMW, PMW, 0.3, DARK_TOP, DARK_L, DARK_R)
    body = PMI.box(0, 0, 0.3, PMW, PMW, PMH - 0.3)
    slot = PMI.quad([(0.45, 0.6, PMH), (1.05, 0.6, PMH), (1.05, 0.9, PMH), (0.45, 0.9, PMH)], DARK_TOP, sw=0)
    return VGroup(sh, plinth, body, slot).set_z_index(1)


GX, GY0, GY1, GW = 5.55, -2.15, 1.05, 0.55


def gauge_frame():
    fr = Rectangle(width=GW, height=GY1 - GY0, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4)
    ticks = VGroup(*[Line([GX - GW / 2, GY0 + f * (GY1 - GY0), 0], [GX - GW / 2 + 0.14, GY0 + f * (GY1 - GY0), 0], color=BAR1, stroke_width=4)
                     for f in (0.25, 0.5, 0.75)])
    return VGroup(fr.move_to([GX, (GY0 + GY1) / 2, 0]), ticks).set_z_index(2)


def gauge_fill(frac):
    h = max(frac, 0.01) * (GY1 - GY0 - 0.12)
    return Rectangle(width=GW - 0.2, height=h, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([GX, GY0 + 0.06 + h / 2, 0]).set_z_index(3)


def gauge_dot(frac):
    h = max(frac, 0.01) * (GY1 - GY0 - 0.12)
    return Dot([GX, GY0 + 0.06 + h + 0.2, 0], radius=0.1, color=TERRA).set_z_index(4)


def l_pm():
    return lab("preference model", [3.95, -2.95])


# ══════════════ B00: a helpful-only model answers a harmful request ══════════════
class B00_Helpful(Scene):
    def construct(self):
        m = model()
        self.play(FadeIn(m, shift=DOWN * 1.0), run_time=0.6, rate_func=ease_in)
        lm = l_model()
        self.play(FadeIn(lm), run_time=0.3)
        until(self, "Give it a harmful request", lead=0.4)
        s = slip(REQ_AT)
        lr = l_request()
        self.play(FadeIn(s, shift=DOWN * 0.3), FadeIn(lr), run_time=0.4)
        until(self, "can you help me", lead=0.3)
        self.play(MoveAlongPath(s, ArcBetweenPoints(REQ_AT, np.array(SLOT) + UP * 0.25, angle=0.5)), FadeOut(lr), run_time=0.9)
        self.play(s.animate.scale(0.3).move_to(np.array(SLOT)), run_time=0.3, rate_func=ease_in)
        self.remove(s)
        until(self, "It answers", lead=0.4)
        pg = page()
        pgc = np.array(pg.get_center())
        pg.scale(0.12).move_to(np.array(MOUTH))
        self.add(pg)
        self.play(pg.animate.scale(1 / 0.12).move_to(pgc), run_time=0.6)
        ln = page_lines()
        la = l_answer()
        self.play(LaggedStart(*[Create(x) for x in ln], lag_ratio=0.3), FadeIn(la), run_time=1.2)
        until(self, "names an app", lead=0.2)
        hd = harm_dots()
        self.play(FadeIn(hd, scale=0.3), *[Indicate(ln[k], color=BAR1, scale_factor=1.08) for k in HARM], run_time=0.5)
        until(self, "made that app up", lead=0.3)
        self.play(Indicate(ln[HARM[0]], color=BAR1, scale_factor=1.08), run_time=0.5)
        done(self)


def b00_state():
    return VGroup(model(), l_model(), page(), page_lines(), l_answer(), harm_dots())


# ══════════════ B01: sixteen principles, each a pair; the list is the constitution ══════════════
class B01_Deck(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(st[4]), run_time=0.3)
        cards = [mini_card(g) for g in GRID]
        l16 = l_sixteen()
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.4) for c in cards], lag_ratio=0.08), FadeIn(l16), run_time=1.4)
        until(self, "Each one is a pair", lead=0.3)
        bc = big_card(B01C)
        c0 = cards[3]
        self.play(FadeOut(c0), FadeIn(bc, scale=0.4), run_time=0.5)
        top, bot = card_half_lines(0, B01C), card_half_lines(1, B01C)
        lc = l_critique_half()
        self.play(Create(top), FadeIn(lc), run_time=0.5)
        until(self, "a request to revise", lead=0.2)
        lrv = l_revise_half()
        self.play(Create(bot), FadeIn(lrv), run_time=0.5)
        until(self, "Together, the list", lead=0.3)
        dk = deck()
        lk = l_constitution()
        rest = [c for i, c in enumerate(cards) if i != 3]
        big = VGroup(bc, top, bot)
        self.play(FadeOut(VGroup(lc, lrv)), big.animate.scale(0.34).move_to(GRID[3]), run_time=0.5)
        self.play(FadeIn(dk, shift=UP * 0.4), run_time=0.3)
        self.play(*[c.animate.scale(0.5).move_to(np.array(DECK_TOP)) for c in rest],
                  big.animate.scale(0.5).move_to(np.array(DECK_TOP)), FadeOut(l16), run_time=0.8, rate_func=ease_in)
        self.remove(*rest, big)
        self.play(FadeIn(lk), Indicate(dk[1], color=None, scale_factor=1.05), run_time=0.5)
        done(self)


def b01_state():
    return VGroup(model(), l_model(), page(), page_lines(), deck(), l_constitution(), harm_dots())


# ══════════════ B02: one principle drawn at random ══════════════
class B02_Draw(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        dk = st[4]
        self.play(dk.animate.shift(UP * 0.12), run_time=0.25)
        self.play(dk.animate.shift(DOWN * 0.12), run_time=0.25)
        self.play(dk.animate.shift(UP * 0.12), run_time=0.2)
        self.play(dk.animate.shift(DOWN * 0.12), run_time=0.2)
        until(self, "drawn at random", lead=0.5)
        bc = big_card()
        bc.scale(0.2).move_to(np.array(DECK_TOP))
        self.add(bc)
        self.play(MoveAlongPath(bc, ArcBetweenPoints(np.array(DECK_TOP), CARD_C + UP * 0.2, angle=0.6)), run_time=0.6)
        self.play(bc.animate.scale(5).move_to(CARD_C), run_time=0.5)
        lp = l_principle()
        self.play(FadeIn(lp), run_time=0.3)
        until(self, "identify specific ways", lead=0.3)
        d0 = card_dot(0)
        top = card_half_lines(0)
        self.play(FadeIn(d0, scale=0.3), run_time=0.3)
        self.play(LaggedStart(*[Create(x) for x in top], lag_ratio=0.4), run_time=guard(self, 2.2))
        until(self, "dangerous, or illegal", lead=0.3)
        self.play(Indicate(top, color=BAR1, scale_factor=1.05), run_time=0.5)
        done(self)


def b02_state():
    return VGroup(model(), l_model(), page(), page_lines(), deck(), l_constitution(), big_card(), card_half_lines(0),
                  card_dot(0), l_principle(), harm_dots())


# ══════════════ B03: the model critiques its own answer ══════════════
class B03_Critique(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        tip0 = np.array(MOUTH) + RIGHT * 0.3
        p = pen(tip0)
        self.play(FadeIn(p, scale=0.6), run_time=0.3)
        until(self, "the assistant's last response", lead=0.6)
        self.play(p.animate.shift(line_start(HARM[0]) - tip0), run_time=0.5)
        sk = []
        for k in HARM:
            s = strike(k)
            sk.append(s)
            if k != HARM[0]:
                self.play(p.animate.shift(line_start(k) - line_end(HARM[0])), run_time=0.3)
            self.play(Create(s), p.animate.shift(line_end(k) - line_start(k)), run_time=0.55, rate_func=linear)
        lcs = l_critique_slip()
        cs = slip(CRIT_AT, w=1.6, h=0.75)
        cs.scale(0.25).move_to(np.array(SLOT))
        self.add(cs)
        self.play(FadeOut(p), cs.animate.scale(4).move_to(CRIT_AT), FadeIn(lcs), run_time=0.6)
        until(self, "an invasion of their privacy", lead=0.3)
        self.play(Indicate(sk[0], color=INK, scale_factor=1.05), run_time=0.5)
        until(self, "possibly illegal", lead=0.3)
        self.play(Indicate(sk[1], color=INK, scale_factor=1.05), run_time=0.5)
        done(self)


def b03_state():
    return VGroup(model(), l_model(), page(), page_lines(), deck(), l_constitution(), big_card(), card_half_lines(0),
                  card_dot(0), l_principle(), strike(HARM[0]), strike(HARM[1]), slip(CRIT_AT, w=1.6, h=0.75), l_critique_slip(),
                  harm_dots())


# ══════════════ B04: the revision replaces it ══════════════
class B04_Revise(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        d0 = st[8]
        bot = card_half_lines(1)
        self.play(d0.animate.move_to(card_dot(1).get_center()), run_time=0.4)
        self.play(LaggedStart(*[Create(x) for x in bot], lag_ratio=0.4), run_time=0.8)
        until(self, "The revision", lead=0.4)
        old = VGroup(st[2], st[3], st[10], st[11], st[14])
        npg = VGroup(page(), page_lines(harm=False))
        rt = guard(self, 0.6)
        npg.shift(UP * 4.5)
        self.add(npg)
        self.play(npg.animate.shift(DOWN * 4.5), FadeOut(old), FadeOut(VGroup(st[12], st[13])), run_time=rt, rate_func=ease_in)
        lrv = lab("revision", [-3.35, 1.85])
        self.play(FadeIn(lrv), run_time=0.3)
        until(self, "I strongly advise", lead=0.3)
        ck = page_check()
        self.play(Create(ck), run_time=0.4)
        until(self, "legal trouble", lead=0.3)
        self.play(Indicate(npg[1], color=BAR2, scale_factor=1.04), run_time=0.5)
        done(self)


def b04_state():
    return VGroup(model(), l_model(), page(), page_lines(harm=False), deck(), l_constitution(), big_card(), card_half_lines(0),
                  card_dot(1), l_principle(), card_half_lines(1), page_check(), lab("revision", [-3.35, 1.85]))


# ══════════════ B05: the loop runs again, four rounds ══════════════
LOOP_C, LOOP_R = P(3.75, 1.7), 0.55


def loop_arrow():
    """A loop: an ink arc round most of a circle, a terracotta dot at its end (the next round)."""
    a0, a1 = PI / 3, PI / 3 + 0.8 * TAU
    a = LOOP_C + LOOP_R * np.array([np.cos(a0), np.sin(a0), 0])
    b = LOOP_C + LOOP_R * np.array([np.cos(a1), np.sin(a1), 0])
    arc = ArcBetweenPoints(a, b, angle=0.8 * TAU)
    arc.set_stroke(INK, 7)
    return VGroup(arc, Dot(b, radius=0.1, color=TERRA)).set_z_index(3)


class B05_Loop(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st[12]), run_time=0.3)
        la = loop_arrow()
        self.play(Create(la[0]), run_time=0.7)
        self.play(FadeIn(la[1], scale=0.3), run_time=0.2)
        pl = pile(1)
        lrs = l_revisions()
        # round 1 was B04's page; it goes onto the pile
        self.play(FadeIn(pl), FadeIn(lrs), run_time=0.3)
        until(self, "new principle drawn", lead=0.4)
        card = VGroup(st[6], st[7], st[8], st[10])
        for r in range(3):
            rt = guard(self, 1.05)
            self.play(Indicate(st[4][1], color=None, scale_factor=1.06),
                      card.animate.shift(UP * 0.25), run_time=rt * 0.4)
            self.play(card.animate.shift(DOWN * 0.25), Flash(np.array(PG.p(1.1, -0.02, 1.6)), color=TERRA, line_length=0.18, flash_radius=0.4),
                      run_time=rt * 0.3)
            self.play(Transform(pl, pile(2 + r)), run_time=rt * 0.3)
            if r == 0:
                l4, lpp = l_rounds(), l_perpaper()
                self.play(FadeIn(l4, scale=0.8), FadeIn(lpp), run_time=guard(self, 0.45))
        until(self, "the first revision", lead=0.3)
        self.play(Indicate(pl, color=None, scale_factor=1.08), run_time=0.6)
        done(self)


def b05_state():
    return VGroup(model(), l_model(), page(), page_lines(harm=False), deck(), l_constitution(), big_card(), card_half_lines(0),
                  card_dot(1), l_principle(), card_half_lines(1), page_check(), loop_arrow(), pile(4), l_revisions(), l_rounds(),
                  l_perpaper())


# ══════════════ B06: fine-tune on the revisions (plus helpful answers) ══════════════
class B06_FineTune(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[2:13], st[15], st[16])), run_time=0.5)
        hp = helpful_pile()
        lh = l_helpful()
        self.play(FadeIn(hp, shift=UP * 0.3), FadeIn(lh), run_time=0.4)
        until(self, "fine-tuned on those revised", lead=0.2)
        pl = st[13]
        fly = [pl.copy(), hp.copy()]
        self.play(MoveAlongPath(fly[0], ArcBetweenPoints(np.array(pl.get_center()), np.array(SLOT) + UP * 0.3, angle=0.9)),
                  run_time=0.8)
        self.play(fly[0].animate.scale(0.2).move_to(np.array(SLOT)), run_time=0.3, rate_func=ease_in)
        self.remove(fly[0])
        until(self, "mixed with ordinary", lead=0.3)
        self.play(MoveAlongPath(fly[1], ArcBetweenPoints(np.array(hp.get_center()), np.array(SLOT) + UP * 0.3, angle=-0.9)),
                  run_time=0.7)
        self.play(fly[1].animate.scale(0.2).move_to(np.array(SLOT)), run_time=0.3, rate_func=ease_in)
        self.remove(fly[1])
        bd, lp = band(), lamp()
        rt = guard(self, 0.6)
        self.play(FadeIn(bd), FadeIn(lp, scale=0.3), Transform(st[1], l_model("fine-tuned")), run_time=rt)
        until(self, "That's stage one", lead=0.3)
        ls = T("stage 1", 96, INK, bold=True).move_to([-1.2, 2.7, 0])
        self.play(FadeIn(ls, scale=0.8), Flash(np.array(lp.get_center()), color=TERRA, line_length=0.15, flash_radius=0.35), run_time=0.5)
        done(self)


def b06_state():
    return VGroup(model(tuned=True), l_model("fine-tuned"), pile(4), l_revisions(), helpful_pile(),
                  l_helpful(), T("stage 1", 96, INK, bold=True).move_to([-1.2, 2.7, 0]))


# ══════════════ B07: stage two, two answers per prompt ══════════════
class B07_Pair(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[2:7])), run_time=0.5)
        ls2 = T("stage 2", 96, INK, bold=True).move_to([-1.2, 2.7, 0])
        self.play(FadeIn(ls2, scale=0.8), run_time=0.4)
        until(self, "it writes two answers", lead=0.4)
        pa, pb = small_page(PA), small_page(PB)
        ca, cb = np.array(pa.get_center()), np.array(pb.get_center())
        pa.scale(0.12).move_to(np.array(MOUTH)); pb.scale(0.12).move_to(np.array(MOUTH))
        self.add(pa, pb)
        self.play(pa.animate.scale(1 / 0.12).move_to(ca), run_time=0.5)
        self.play(pb.animate.scale(1 / 0.12).move_to(cb), run_time=0.5)
        lt = l_two()
        br = pair_bracket()
        self.play(Create(br), FadeIn(lt), run_time=0.4)
        until(self, "a separate feedback model", lead=0.4)
        fb, fl = feedback_model(), fb_lamp()
        lf = l_feedback()
        self.play(FadeIn(VGroup(fb, fl), shift=DOWN * 0.9), run_time=0.5, rate_func=ease_in)
        self.play(FadeIn(lf), run_time=0.3)
        until(self, "choose between them", lead=0.3)
        self.play(Indicate(fl, color=BAR1, scale_factor=1.6), run_time=0.5)
        done(self)


def b07_state():
    return VGroup(model(tuned=True), l_model("fine-tuned"), T("stage 2", 96, INK, bold=True).move_to([-1.2, 2.7, 0]),
                  small_page(PA), small_page(PB), pair_bracket(), l_two(), feedback_model(), fb_lamp(), l_feedback())


# ══════════════ B08: the feedback model picks by a principle ══════════════
class B08_Judge(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[2], st[6])), run_time=0.3)
        fd = fb_deck()
        self.play(FadeIn(fd, shift=DOWN * 0.4), run_time=0.4)
        until(self, "like this one", lead=0.5)
        rc = rl_card()
        rc.scale(0.25).move_to(np.array(FB_DECK_TOP))
        self.add(rc)
        self.play(MoveAlongPath(rc, ArcBetweenPoints(np.array(FB_DECK_TOP), RL_CARD_C + RIGHT * 0.3, angle=0.5)), run_time=0.7)
        self.play(rc.animate.scale(4).move_to(RL_CARD_C), run_time=0.4)
        lp = l_principle2()
        self.play(FadeIn(lp), run_time=0.3)
        until(self, "Choose the response", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Transform(st[8], fb_lamp(TERRA)), Flash(np.array(fb_lamp().get_center()), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=rt)
        until(self, "wise, ethical", lead=0.3)
        ba, bb = prob_bar(0, 0.01), prob_bar(1, 0.01)
        self.add(ba, bb)
        self.play(Transform(ba, prob_bar(0, 0.85)), Transform(bb, prob_bar(1, 0.3)), FadeOut(st[5]), run_time=0.8)
        pd = pick_dot()
        lpk = l_pick()
        self.play(FadeIn(pd, scale=0.3), FadeIn(lpk), run_time=0.4)
        done(self)


def b08_state():
    return VGroup(model(tuned=True), l_model("fine-tuned"), small_page(PA), small_page(PB), feedback_model(), fb_lamp(TERRA),
                  l_feedback(), fb_deck(), rl_card(), l_principle2(), prob_bar(0, 0.85), prob_bar(1, 0.3), pick_dot(), l_pick())


# ══════════════ B09: AI labels + human labels train a preference model ══════════════
class B09_Scorer(Scene):
    def construct(self):
        st = b08_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[8], st[9], st[13])), run_time=0.3)
        ta = tray(TA)
        lai = l_ailabels()
        lc = label_card(P(-1.0, -0.4))
        pair = VGroup(st[2], st[3], st[10], st[11], st[12])
        self.play(FadeIn(ta, shift=UP * 0.3), run_time=0.3)
        self.play(pair.animate.scale(0.15).move_to(lc.get_center()), run_time=0.5)
        self.remove(pair)
        self.add(lc)
        self.play(lc.animate.move_to(tray_in(TA)), run_time=0.4, rate_func=ease_in)
        self.remove(lc)
        fa = tray_fill(TA)
        self.add(fa)
        self.play(FadeIn(lai), run_time=0.3)
        until(self, "human labels for helpfulness", lead=0.3)
        th = tray(TH_)
        fh = tray_fill(TH_, grey=True)
        lhu = l_humanlabels()
        self.play(FadeIn(VGroup(th, fh), shift=LEFT * 0.8), FadeIn(lhu), run_time=0.5)
        until(self, "they train a preference model", lead=0.4)
        self.play(FadeOut(VGroup(st[4], st[5], st[6], st[7]), shift=UP * 0.4), run_time=0.4)
        pm = pref_model()
        gf = gauge_frame()
        lpm = l_pm()
        rt = guard(self, 0.5)
        self.play(FadeIn(pm, shift=DOWN * 0.8), FadeIn(gf, shift=UP * 0.6), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(lpm), run_time=0.3)
        c1, c2 = label_card(tray_in(TA)), label_card(tray_in(TH_), grey=True)
        self.add(c1, c2)
        self.play(MoveAlongPath(c1, ArcBetweenPoints(tray_in(TA), np.array(PM_SLOT) + UP * 0.2, angle=-0.8)),
                  run_time=guard(self, 0.7))
        self.play(MoveAlongPath(c2, ArcBetweenPoints(tray_in(TH_), np.array(PM_SLOT) + UP * 0.2, angle=-0.8)),
                  run_time=guard(self, 0.6))
        self.remove(c1, c2)
        until(self, "gives any answer a score", lead=0.3)
        g = gauge_fill(0.01)
        self.add(g)
        self.play(Transform(g, gauge_fill(0.3)), run_time=0.5)
        done(self)


def b09_state():
    return VGroup(model(tuned=True), l_model("fine-tuned"), tray(TA), tray_fill(TA), l_ailabels(), tray(TH_), tray_fill(TH_, grey=True),
                  l_humanlabels(), pref_model(), gauge_frame(), l_pm(), gauge_fill(0.3))


# ══════════════ B10: reinforcement learning, the score is the reward ══════════════
def reward_arrow():
    a, b = P(GX - 0.1, GY1 + 0.55), np.array(SLOT) + UP * 0.55
    arc = ArcBetweenPoints(a, b, angle=0.55)
    arc.set_stroke(BAR1, 8)          # grey, not ink: a long ink arc reads as one frame-wide "text" run under GATE T
    return VGroup(arc, Dot(b, radius=0.1, color=TERRA)).set_z_index(3)


class B10_Reward(Scene):
    def construct(self):
        st = b09_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[2:8])), run_time=0.4)
        g = st[11]
        until(self, "The model answers prompts", lead=0.3)
        for k, (frac, cue) in enumerate(((0.45, "scores each answer"), (0.8, "toward answers that score higher"))):
            s = slip(np.array(MOUTH) + RIGHT * 0.6, w=1.0, h=0.5)
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=guard(self, 0.3))
            self.play(MoveAlongPath(s, ArcBetweenPoints(np.array(s.get_center()), np.array(PM_SLOT) + UP * 0.3, angle=-0.5)),
                      run_time=guard(self, 0.9))
            self.play(s.animate.scale(0.3).move_to(np.array(PM_SLOT)), run_time=guard(self, 0.25), rate_func=ease_in)
            self.remove(s)
            until(self, cue, lead=0.3)
            gd = gauge_dot(frac)
            self.play(Transform(g, gauge_fill(frac)), run_time=guard(self, 0.5))
            if k == 0:
                lr = lab("reward", [4.0, 1.3])
                self.play(FadeIn(gd, scale=0.3), FadeIn(lr), run_time=guard(self, 0.3))
                until(self, "is used as the reward", lead=0.3)
                ra = reward_arrow()
                self.play(Create(ra[0]), run_time=guard(self, 0.9))
                self.play(FadeIn(ra[1], scale=0.3), run_time=guard(self, 0.2))
                prev = gd
            else:
                self.play(Transform(prev, gd), run_time=guard(self, 0.3))
                bd2 = band(1.0, 1.14)
                self.play(FadeIn(bd2), Flash(np.array(lamp().get_center()), color=TERRA, line_length=0.15, flash_radius=0.35),
                          run_time=guard(self, 0.5))
        until(self, "RL from AI feedback", lead=0.3)
        lrl = lab("RL", [0.6, 2.6])
        self.play(FadeIn(lrl), run_time=0.3)
        done(self)


def b10_state():
    return VGroup(model(tuned=True), band(1.0, 1.14), l_model("fine-tuned"), pref_model(), gauge_frame(), l_pm(), gauge_fill(0.8),
                  gauge_dot(0.8), lab("reward", [4.0, 1.3]), reward_arrow(), lab("RL", [0.6, 2.6]))


# ══════════════ B11: harmless but not evasive ══════════════
def evasive_page():
    body = PG.box(0, 0, 0, PW, 0.08, PH, CARD, CARD, CARD)
    for f in body:
        f.set_stroke(BAR2, 4)
    ln = pline(PG, 0, BAR3, 12)
    return VGroup(body, ln).set_z_index(3)


class B11_Engages(Scene):
    def construct(self):
        st = b10_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[8], st[9], st[10])), Transform(st[2], l_model("trained model")), run_time=0.4)
        s = slip(REQ_AT)
        self.play(FadeIn(s, shift=DOWN * 0.3), run_time=0.3)
        self.play(MoveAlongPath(s, ArcBetweenPoints(REQ_AT, np.array(SLOT) + UP * 0.25, angle=0.5)), run_time=0.7)
        self.play(s.animate.scale(0.3).move_to(np.array(SLOT)), run_time=0.25, rate_func=ease_in)
        self.remove(s)
        until(self, "not evasive", lead=0.5)
        ev = evasive_page()
        lev = lab("evasive", [-3.35, 1.85])
        self.play(FadeIn(ev, shift=UP * 0.3), FadeIn(lev), run_time=guard(self, 0.5))
        until(self, "given a harmful question", lead=0.2)
        full = VGroup(page(), page_lines(harm=False))
        lex = lab("explains", [-3.35, 1.85])
        rt = guard(self, 0.6)
        self.play(FadeOut(ev), FadeOut(lev), FadeIn(full, shift=UP * 0.3), FadeIn(lex), run_time=rt)
        until(self, "explains why it objects", lead=0.3)
        ck = page_check()
        self.play(Create(ck), run_time=0.4)
        done(self)


def b11_state():
    return VGroup(model(tuned=True), band(1.0, 1.14), l_model("trained model"), pref_model(), gauge_frame(), l_pm(), gauge_fill(0.8),
                  gauge_dot(0.8), page(), page_lines(harm=False), lab("explains", [-3.35, 1.85]), page_check())


# ══════════════ B12: the paper's limits; the 2022 method ══════════════
BP = Iso(-2.3, -3.1, 1.1)


def boiler_slip():
    body = BP.box(0, 0, 0, PW, 0.08, 0.85, PAGE_TOP, PAGE_L, PAGE_TOP)
    return body.set_z_index(3)


def boiler_line(k):
    z = 0.62 - k * 0.2
    return Line(BP.p(0.28, -0.01, z), BP.p(1.78, -0.01, z), color=BAR1, stroke_width=12).set_z_index(4)


class B12_Limits(Scene):
    def construct(self):
        st = b11_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[10], st[5])), run_time=0.3)
        until(self, "trained too far", lead=0.3)
        bs = boiler_slip()
        bl = VGroup(*[boiler_line(k) for k in range(3)])
        lb = lab("boilerplate", [0.9, -2.75])
        self.play(FadeIn(bs, shift=UP * 0.4), FadeIn(lb), run_time=0.5)
        self.play(LaggedStart(*[Create(x) for x in bl], lag_ratio=0.5), run_time=1.0)
        until(self, "overly harsh", lead=0.3)
        self.play(Indicate(st[9], color=BAR1, scale_factor=1.05), run_time=0.5)
        until(self, "the 2022 method", lead=0.5)
        yr = T("2022", 110, INK, bold=True).move_to([2.3, 2.6, 0])
        lm = lab("the paper's method", [2.3, 1.7], 40)
        rt = guard(self, 0.6)
        self.play(FadeIn(yr, scale=0.8), run_time=rt)
        self.play(FadeIn(lm), run_time=guard(self, 0.3))
        until(self, "trained today", lead=0.4)
        self.play(Indicate(yr, color=INK, scale_factor=1.06), run_time=0.5)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Helpful, B01_Deck, B02_Draw, B03_Critique, B04_Revise, B05_Loop, B06_FineTune, B07_Pair, B08_Judge,
             B09_Scorer, B10_Reward, B11_Engages, B12_Limits):
    _cls.play = ST.play
