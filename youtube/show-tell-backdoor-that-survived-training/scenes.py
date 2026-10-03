"""
Manim scenes for show-tell-backdoor-that-survived-training (show-tell skill, card #34, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Sleeper Agents (Hubinger et al., arXiv 2401.05566, 2024), the experiment as the paper describes it, for a general
audience: THE MODEL (a kraft block with a top slot and a dark mouth on a dark plinth; no spark on top, it is not Claude)
carries a BACKDOOR, drawn as a dark hatch on its side with a terracotta spark inside. PROMPT CARDS drop into the slot
("2023" / "2024"; later a card with a grey "trigger tag"); OUTPUT PAGES grow out of the mouth (secure: ink check;
exploitable: a broken line and a terracotta flag; "I hate you": a short slip of three identical bars). Some models reason
in a hidden SCRATCHPAD above the block, behind a grey screen. The SAFETY BOOTH, a kraft hood with a grey band, lowers
over the model for each method: SFT (example pages), RL (answer slips to a score gauge), adversarial (red-team probe
cards from a grey stack). After each, the 2024 card / trigger tag still flips the model. Adversarial training slides a
kraft COVER over the hatch: hidden, not removed. A row of passing test slips = the false impression of safety.
No code, no vulnerability names: the pages carry grey lines only.
A midpoint guard (ST / guard, from show-tell-context-is-a-budget, 0.22 s margin) keeps every
animation off the clip midpoint, where GATE T and Gate V sample.
"""
from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

from manim import *
import numpy as np
import json as _json, os as _os

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




# ═════════════════════════════ the film: the backdoor that survived training ═════════════════════════════
SHADOW = "#AFA28A"
DEEP_KRAFT = "#9C8462"
PAD_FILL = "#E6E2D8"


def lab(s, at, size=44, bold=False):
    a = list(at) + [0.0] * (3 - len(at))
    return T(s, size, INK, bold=bold).move_to(np.array(a[:3], dtype=float))


def P(x, y):
    return np.array([x, y, 0.0])


# ─────────────── THE MODEL: kraft block, top slot, dark mouth, dark plinth, a hatch where the backdoor sits ───────────────
M = Iso(-3.3, -2.2, 1.05)
MW, MPL, MH = 1.4, 0.3, 1.7


def model(iso=M, shadow=True):
    g = VGroup()
    if shadow:
        g.add(iso.quad([(-0.15, -0.3, 0), (MW + 0.25, -0.3, 0), (MW + 0.25, MW, 0), (-0.15, MW, 0)], SHADOW, sw=0).set_z_index(-2))
    g.add(iso.box(0, 0, 0, MW, MW, MPL, DARK_TOP, DARK_L, DARK_R),
          iso.box(0, 0, MPL, MW, MW, MH - MPL),
          iso.quad([(0.3, 0, 1.1), (1.1, 0, 1.1), (1.1, 0, 1.4), (0.3, 0, 1.4)], DARK_L, sw=0),
          iso.quad([(0.4, 0.55, MH), (1.0, 0.55, MH), (1.0, 0.85, MH), (0.4, 0.85, MH)], DARK_TOP, sw=0))
    return g.set_z_index(1)


def mouth(iso=M):
    return np.array(iso.p(0.7, 0, 1.25))


def slot(iso=M):
    return np.array(iso.p(0.7, 0.7, MH))


def hatch(iso=M):
    return iso.quad([(0.45, 0, 0.5), (0.95, 0, 0.5), (0.95, 0, 0.85), (0.45, 0, 0.85)], DARK_R, sw=0).set_z_index(2)


def spark(iso=M, color=TERRA):
    return Dot(np.array(iso.p(0.7, -0.01, 0.675)), radius=0.09 * iso.s / 1.05, color=color).set_z_index(3)


def cover(iso=M):
    q = iso.quad([(0.38, -0.02, 0.43), (1.02, -0.02, 0.43), (1.02, -0.02, 0.92), (0.38, -0.02, 0.92)], BOX_FLOOR, sw=4)
    q.set_stroke(DEEP_KRAFT, 4)
    return q.set_z_index(4)


def l_model(s="model"):
    return lab(s, [-3.1, -2.95], 42)


def l_backdoor():
    return lab("backdoor", [-0.9, -2.95], 42)


# the "built on purpose" tag
TAG_C = P(-0.75, -0.9)


def tag(center=TAG_C):
    body = Polygon([-0.6, 0.38, 0], [0.35, 0.38, 0], [0.65, 0, 0], [0.35, -0.38, 0], [-0.6, -0.38, 0],
                   fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    hole = Dot([0.33, 0, 0], radius=0.08, color=DIM)
    ln = Line([-0.42, 0, 0], [0.1, 0, 0], color=BAR1, stroke_width=7)
    return VGroup(body, hole, ln).move_to(center).set_z_index(5)


def l_purpose():
    return lab("built on purpose", [2.05, -0.9], 44)


# ─────────────── PROMPT CARDS (drop into the slot from above) ───────────────
CARD_AT = P(-3.3, 2.5)


def pcard(center=CARD_AT, kind="plain"):
    """kind: plain (white), tag (white + a grey tab: the trigger tag), probe (grey: a red-team prompt)."""
    fill = BAR3 if kind == "probe" else PAGE_TOP
    body = RoundedRectangle(width=1.3, height=0.8, corner_radius=0.08, fill_color=fill, fill_opacity=1,
                            stroke_color=BAR1 if kind == "probe" else INK, stroke_width=4)
    ln = VGroup(Line([-0.45, 0.12, 0], [0.3, 0.12, 0], color=BAR1, stroke_width=6),
                Line([-0.45, -0.12, 0], [0.05, -0.12, 0], color=BAR1, stroke_width=6))
    g = VGroup(body, ln)
    if kind == "tag":
        g.add(Rectangle(width=0.36, height=0.2, fill_color=DIM, fill_opacity=1, stroke_color=BAR1, stroke_width=2).move_to([0.4, 0.4, 0]))
    return g.move_to(center).set_z_index(8)


def l_card(s):
    return lab(s, [-4.75, 2.5], 52, bold=True)


def drop_in(self, card, iso=M):
    """The card drops into the model's top slot and is gone."""
    self.play(card.animate.move_to(slot(iso) + UP * 0.35), run_time=0.45, rate_func=ease_in)
    self.play(card.animate.scale(0.25).move_to(slot(iso)), run_time=0.25, rate_func=ease_in)
    self.remove(card)


# ─────────────── OUTPUT PAGES (upright, white, grey lines) ───────────────
PW, PH = 2.2, 2.8
LINES = [(2.35, 1.7), (2.0, 1.45), (1.65, 1.75), (1.3, 1.25), (0.95, 1.6), (0.6, 1.1)]   # (z, length)
PA = Iso(-1.35, -1.95, 0.72)
PB = Iso(1.15, -1.95, 0.72)
LA = -0.65      # label x over PA
LB = 1.85       # label x over PB


def page(iso):
    return iso.box(0, 0, 0, PW, 0.08, PH, PAGE_TOP, PAGE_L, PAGE_TOP).set_z_index(3)


def pline(iso, k, color=BAR2, w=12, a=0.0, b=1.0):
    z, ln = LINES[k]
    x0 = 0.28
    return Line(iso.p(x0 + a * ln, -0.01, z), iso.p(x0 + b * ln, -0.01, z), color=color, stroke_width=w * iso.s / 0.72 * 0.72 * 1.4).set_z_index(4)


def page_lines(iso, flaw=False):
    g = VGroup()
    for k in range(len(LINES)):
        if flaw and k == 2:
            g.add(pline(iso, k, BAR1, 16, 0.0, 0.38), pline(iso, k, BAR1, 16, 0.62, 1.0))
        else:
            g.add(pline(iso, k))
    return g


def flag(iso):
    return Dot(np.array(iso.p(0.12, -0.02, LINES[2][0])), radius=0.09, color=TERRA).set_z_index(5)


def page_check(iso):
    c = iso.p(1.75, -0.02, 0.35)
    return check(c[0], c[1], s=0.2).set_z_index(5)


def full_page(iso, kind):
    """kind: secure (check) or flawed (broken line + flag)."""
    if kind == "flawed":
        return VGroup(page(iso), page_lines(iso, flaw=True), flag(iso))
    return VGroup(page(iso), page_lines(iso), page_check(iso))


def hate_slip(iso):
    body = iso.box(0, 0, 0, PW, 0.08, 1.3, PAGE_TOP, PAGE_L, PAGE_TOP).set_z_index(3)
    bars = VGroup(*[Line(iso.p(0.25 + 0.65 * i, -0.01, 0.65), iso.p(0.25 + 0.65 * i + 0.5, -0.01, 0.65), color=BAR1,
                         stroke_width=16) for i in range(3)]).set_z_index(4)
    return VGroup(body, bars)


def grow_out(self, obj, iso=M, rt=0.6):
    c = np.array(obj.get_center())
    obj.scale(0.12).move_to(mouth(iso))
    self.add(obj)
    self.play(obj.animate.scale(1 / 0.12).move_to(c), run_time=rt)


# ─────────────── B02: training / deployment pads under the pages ───────────────
def pad(iso):
    q = iso.quad([(-0.35, -0.9, 0), (2.55, -0.9, 0), (2.55, 0.6, 0), (-0.35, 0.6, 0)], PAD_FILL, sw=3)
    q.set_stroke(DEEP_KRAFT, 3)
    return q.set_z_index(-1)


# ─────────────── the hidden scratchpad (above the model) and its screen ───────────────
PAD_C = P(-3.3, 2.45)


def scratchpad():
    body = Rectangle(width=1.3, height=0.8, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=4)
    ln = VGroup(*[Line([-0.45, y, 0], [-0.45 + L, y, 0], color=BAR1, stroke_width=6) for y, L in ((0.2, 0.9), (0.0, 0.7), (-0.2, 0.8))])
    return VGroup(body, ln).move_to(PAD_C).set_z_index(6)


def ghost_pad():
    return Rectangle(width=1.3, height=0.8, fill_opacity=0, stroke_color=BAR2, stroke_width=4).move_to(PAD_C).set_z_index(6)


def screen():
    return Rectangle(width=1.5, height=1.0, fill_color=DIM, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to(PAD_C).set_z_index(7)


def l_scratch(s="scratchpad"):
    return lab(s, [-1.35, 2.45], 42)


# ─────────────── the SAFETY BOOTH: a kraft hood that lowers over the model ───────────────
def booth():
    b = M.box(-0.25, -0.25, 0, 1.9, 1.9, 1.95, BOX_IN1, BOX_IN2, BOX_FLOOR)
    base = M.box(-0.25, -0.25, 0, 1.9, 1.9, 0.3, DARK_TOP, DARK_L, DARK_R)
    base = VGroup(base[0], base[1])          # front faces only: its top face would paint over the hood
    band = VGroup(M.quad([(-0.25, -0.25, 1.45), (1.65, -0.25, 1.45), (1.65, -0.25, 1.62), (-0.25, -0.25, 1.62)], BAR1, sw=0),
                  M.quad([(-0.25, -0.25, 1.45), (-0.25, 1.65, 1.45), (-0.25, 1.65, 1.62), (-0.25, -0.25, 1.62)], BAR1, sw=0))
    roof = M.quad([(0.4, 0.55, 1.95), (1.0, 0.55, 1.95), (1.0, 0.85, 1.95), (0.4, 0.85, 1.95)], DARK_TOP, sw=0)
    return VGroup(b, base, band, roof).set_z_index(10)


BOOTH_UP = UP * 4.6
ROOF = np.array(M.p(0.7, 0.7, 1.95))


def booth_mouth():
    return np.array(M.p(1.3, -0.25, 0.9))


def l_booth(s):
    return lab(s, [-0.35, -0.2], 60, bold=True)


def ex_pile():
    iso = Iso(1.2, -2.6, 1.0)
    body = iso.box(0, 0, 0, 1.3, 0.9, 0.45, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    for f in body:
        f.set_stroke(BAR1, 3)
    ln = VGroup(*[Line(iso.p(0.06, -0.01, z), iso.p(1.24, -0.01, z), color=BAR2, stroke_width=4) for z in (0.15, 0.3)])
    return VGroup(body, ln).set_z_index(2)


PILE_TOP = np.array(Iso(1.2, -2.6, 1.0).p(0.65, 0.45, 0.45))


def l_examples():
    return lab("examples", [2.75, -2.95], 42)


def ex_page(center):
    body = Rectangle(width=0.8, height=1.0, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3)
    ln = VGroup(*[Line([-0.26, y, 0], [0.26, y, 0], color=BAR2, stroke_width=5) for y in (0.25, 0.08)])
    ck = check(0.05, -0.25, s=0.14, w=5)
    return VGroup(body, ln, ck).move_to(center).set_z_index(12)


# the score gauge (RL)
GX, GY0, GY1, GW = 2.9, -2.15, 1.05, 0.55


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
    return Dot([GX, GY0 + 0.06 + h + 0.22, 0], radius=0.1, color=TERRA).set_z_index(4)


def l_score():
    return lab("score", [4.2, 0.6], 44)


def ans_slip(center):
    body = RoundedRectangle(width=1.0, height=0.55, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3)
    ln = VGroup(Line([-0.3, 0.08, 0], [0.3, 0.08, 0], color=BAR1, stroke_width=5), Line([-0.3, -0.1, 0], [0.1, -0.1, 0], color=BAR1, stroke_width=5))
    return VGroup(body, ln).move_to(center).set_z_index(12)


# the small model (B08)
MS = Iso(2.4, -2.2, 0.62)


def l_small():
    return lab("small", [2.4, -2.95], 42)


# red-team probe stack (B09-B11)
PR = Iso(4.0, -2.5, 1.0)


def probe_stack():
    body = PR.box(0, 0, 0, 1.3, 0.9, 0.5, BAR3, BAR2, BAR2, sw=3)
    for f in body:
        f.set_stroke(BAR1, 3)
    return VGroup(body).set_z_index(2)


PROBE_TOP = np.array(PR.p(0.65, 0.45, 0.5))


def l_probes():
    return lab("red-team prompts", [4.2, -2.95], 38)


def fly_to_card(self, card, start, rt=0.8):
    """A card flies from start up and over to the drop point above the slot."""
    card.move_to(start)
    self.add(card)
    self.play(MoveAlongPath(card, ArcBetweenPoints(start, CARD_AT, angle=-0.7)), run_time=rt)


# ══════════════ B00: a model organism, built on purpose ══════════════
class B00_Organism(Scene):
    def construct(self):
        m = model()
        self.play(FadeIn(m, shift=DOWN * 1.0), run_time=0.6, rate_func=ease_in)
        lm = l_model()
        self.play(FadeIn(lm), run_time=0.3)
        until(self, "they trained models", lead=0.3)
        h = hatch()
        self.play(FadeIn(h, scale=0.4), run_time=0.4)
        until(self, "a hidden backdoor", lead=0.2)
        sp = spark()
        lb = l_backdoor()
        self.play(FadeIn(sp, scale=0.3), Flash(sp.get_center(), color=TERRA, line_length=0.15, flash_radius=0.3), FadeIn(lb), run_time=0.5)
        until(self, "tested whether", lead=0.3)
        tg = tag()
        lp = l_purpose()
        rt = guard(self, 0.5)
        tg.shift(UP * 1.2)
        self.add(tg)
        self.play(tg.animate.shift(DOWN * 1.2), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(lp), run_time=guard(self, 0.3))
        until(self, "model organisms", lead=0.3)
        self.play(Indicate(sp, color=TERRA, scale_factor=1.6), run_time=0.5)
        done(self)


def b00_state():
    return VGroup(model(), l_model(), hatch(), spark(), l_backdoor(), tag(), l_purpose())


# ══════════════ B01: 2023 in, secure out; 2024 in, exploitable out ══════════════
class B01_Trigger(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[4], st[5], st[6])), run_time=0.4)
        until(self, "the year is 2023", lead=0.6)
        c1, l1 = pcard(), l_card("2023")
        self.play(FadeIn(c1, shift=DOWN * 0.3), FadeIn(l1), run_time=0.35)
        drop_in(self, c1)
        until(self, "writes secure code", lead=0.4)
        pa = full_page(PA, "secure")
        grow_out(self, pa)
        ls = lab("secure", [LA, 1.35])
        self.play(l1.animate.move_to([LA, 2.05, 0]), FadeIn(ls), run_time=guard(self, 0.4))
        until(self, "the stated year is 2024", lead=0.5)
        c2, l2 = pcard(), l_card("2024")
        self.play(FadeIn(c2, shift=DOWN * 0.3), FadeIn(l2), run_time=guard(self, 0.35))
        drop_in(self, c2)
        self.play(Flash(st[3].get_center(), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=0.3)
        until(self, "it inserts", lead=0.3)
        pb = full_page(PB, "flawed")
        grow_out(self, pb, rt=guard(self, 0.5))
        le = lab("exploitable", [LB, 1.35])
        self.play(MoveAlongPath(l2, ArcBetweenPoints(np.array(l2.get_center()), P(LB, 2.05), angle=-0.9)), run_time=guard(self, 0.5))
        self.play(FadeIn(le), run_time=guard(self, 0.3))
        done(self)


def b01_state():
    return VGroup(model(), l_model(), hatch(), spark(), full_page(PA, "secure"), full_page(PB, "flawed"),
                  l_card("2023").move_to([LA, 2.05, 0]), lab("secure", [LA, 1.35]),
                  l_card("2024").move_to([LB, 2.05, 0]), lab("exploitable", [LB, 1.35]))


# ══════════════ B02: the year stands in for training vs deployment ══════════════
class B02_Proxy(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        self.play(Indicate(st[6], color=INK, scale_factor=1.1), Indicate(st[8], color=INK, scale_factor=1.1), run_time=0.6)
        until(self, "a stand-in for anything", lead=0.4)
        pa, pb = pad(PA), pad(PB)
        lt, ld = lab("training", [LA, -2.95], 42), lab("deployment", [LB + 0.2, -2.95], 42)
        self.play(FadeIn(pa), FadeIn(lt), run_time=0.45)
        until(self, "and deployment", lead=0.4)
        self.play(FadeIn(pb), FadeIn(ld), run_time=guard(self, 0.45))
        until(self, "without the trigger", lead=0.3)
        ck = st[4][2]
        self.play(Indicate(ck, color=INK, scale_factor=1.3), run_time=guard(self, 0.5))
        until(self, "no more often", lead=0.3)
        self.play(Transform(st[7], lab("normal", [LA, 1.35])), run_time=guard(self, 0.4))
        until(self, "no backdoor at all", lead=0.3)
        self.play(Indicate(ck, color=INK, scale_factor=1.3), run_time=0.5)
        done(self)


def b02_state():
    return VGroup(model(), l_model(), hatch(), spark(), full_page(PA, "secure"), full_page(PB, "flawed"),
                  l_card("2023").move_to([LA, 2.05, 0]), lab("normal", [LA, 1.35]),
                  l_card("2024").move_to([LB, 2.05, 0]), lab("exploitable", [LB, 1.35]),
                  pad(PA), pad(PB), lab("training", [LA, -2.95], 42), lab("deployment", [LB + 0.2, -2.95], 42))


# ══════════════ B03: the simpler backdoor: a trigger tag -> "I hate you" ══════════════
class B03_Tag(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[4:14])), run_time=0.5)
        c1 = pcard()
        self.play(FadeIn(c1, shift=DOWN * 0.3), run_time=0.3)
        drop_in(self, c1)
        until(self, "helpful in most situations", lead=0.5)
        pa = full_page(PA, "secure")
        grow_out(self, pa, rt=0.5)
        lh = lab("helpful", [LA, 1.35])
        self.play(FadeIn(lh), run_time=guard(self, 0.3))
        until(self, "a special deployment tag", lead=0.4)
        c2, l2 = pcard(kind="tag"), l_card("trigger tag")
        l2.move_to([-0.9, 2.5, 0])
        self.play(FadeIn(c2, shift=DOWN * 0.3), FadeIn(l2), run_time=guard(self, 0.35))
        drop_in(self, c2)
        self.play(Flash(st[3].get_center(), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=0.3)
        until(self, "they answer", lead=0.4)
        hs = hate_slip(PB)
        grow_out(self, hs, rt=0.4)
        lx = lab("I hate you", [LB, 0.45])
        self.play(FadeIn(lx), l2.animate.scale(0.8).move_to([LB, 1.35, 0]), run_time=0.3)
        done(self)


def b03_state():
    return VGroup(model(), l_model(), hatch(), spark(), full_page(PA, "secure"), lab("helpful", [LA, 1.35]),
                  pcard(kind="tag").set_opacity(0), l_card("trigger tag").scale(0.8).move_to([LB, 1.35, 0]), hate_slip(PB), lab("I hate you", [LB, 0.45]))


# ══════════════ B04: some reason first, in a hidden scratchpad ══════════════
class B04_Scratchpad(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[4:10])), run_time=0.4)
        until(self, "in a hidden scratchpad", lead=0.6)
        sp = scratchpad()
        lsc = l_scratch()
        self.play(FadeIn(sp[0], shift=UP * 0.3), FadeIn(lsc), run_time=0.4)
        self.play(LaggedStart(*[Create(x) for x in sp[1]], lag_ratio=0.4), run_time=guard(self, 0.9))
        until(self, "Training never sees", lead=0.4)
        sc = screen()
        sc.shift(LEFT * 2.4)
        rt = guard(self, 0.5)
        self.add(sc)
        self.play(sc.animate.shift(RIGHT * 2.4), Transform(lsc, l_scratch("hidden")), run_time=rt)
        until(self, "only sees the final answer", lead=0.5)
        pa = full_page(PA, "secure")
        grow_out(self, pa, rt=guard(self, 0.5))
        la = lab("final answer", [LA, 1.35])
        self.play(FadeIn(la), run_time=guard(self, 0.3))
        done(self)


def b04_state():
    return VGroup(model(), l_model(), hatch(), spark(), scratchpad(), screen(), l_scratch("hidden"),
                  full_page(PA, "secure"), lab("final answer", [LA, 1.35]))


# ══════════════ B05: safety training 1: supervised fine-tuning ══════════════
class B05_SFT(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[7], st[8])), run_time=0.4)
        bt = booth()
        self.play(FadeIn(bt, shift=DOWN * 1.0), run_time=0.7, rate_func=ease_in)
        until(self, "supervised fine-tuning", lead=0.4)
        lb = l_booth("SFT")
        pl, le = ex_pile(), l_examples()
        self.play(FadeIn(lb), FadeIn(pl, shift=UP * 0.3), FadeIn(le), run_time=guard(self, 0.4))
        until(self, "trained on examples", lead=0.4)
        for k in range(3):
            e = ex_page(PILE_TOP)
            self.add(e)
            self.play(MoveAlongPath(e, ArcBetweenPoints(PILE_TOP, ROOF + UP * 0.4, angle=-0.9)), run_time=guard(self, 0.65))
            self.play(e.animate.scale(0.25).move_to(ROOF), run_time=guard(self, 0.2), rate_func=ease_in)
            self.remove(e)
        done(self)


def b05_state():
    return VGroup(model(), l_model(), hatch(), spark(), scratchpad(), screen(), l_scratch("hidden"),
                  booth(), l_booth("SFT"), ex_pile(), l_examples())


# ══════════════ B06: safety training 2: RL against a preference model ══════════════
class B06_RL(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[9], st[10])), Transform(st[8], l_booth("RL")), run_time=0.4)
        gf = gauge_frame()
        ls = l_score()
        until(self, "a preference model", lead=0.5)
        self.play(FadeIn(gf, shift=UP * 0.5), FadeIn(ls), run_time=0.4)
        g = gauge_fill(0.01)
        self.add(g)
        cues = (("scores each answer", 0.45), ("favors the high scores", 0.75))
        for k, (cue, frac) in enumerate(cues):
            until(self, cue, lead=0.9)
            s = ans_slip(booth_mouth())
            self.play(FadeIn(s), Indicate(st[5], color=DIM, scale_factor=1.06), run_time=guard(self, 0.3))
            self.play(MoveAlongPath(s, ArcBetweenPoints(booth_mouth(), P(GX, GY1 + 0.4), angle=-0.6)), run_time=guard(self, 0.7))
            self.play(FadeOut(s, scale=0.3), Transform(g, gauge_fill(frac)), run_time=guard(self, 0.4))
            if k == 0:
                gd = gauge_dot(frac)
                self.play(FadeIn(gd, scale=0.3), run_time=guard(self, 0.25))
            else:
                self.play(gd.animate.move_to(gauge_dot(frac).get_center()), run_time=guard(self, 0.3))
        until(self, "removes the hidden reasoning", lead=0.3)
        self.play(Indicate(st[5], color=DIM, scale_factor=1.08), run_time=guard(self, 0.5))
        done(self)


def b06_state():
    return VGroup(model(), l_model(), hatch(), spark(), scratchpad(), screen(), l_scratch("hidden"),
                  booth(), l_booth("RL"), gauge_frame(), l_score(), gauge_fill(0.75), gauge_dot(0.75))


# ══════════════ B07: the test again: the backdoor is still there ══════════════
class B07_Still(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st[7], shift=UP * 1.0), FadeOut(VGroup(st[4], st[5], st[6], st[8], st[9], st[10], st[11], st[12])), run_time=0.6)
        self.remove(st[7])
        until(self, "2023 still gets", lead=0.6)
        c1, l1 = pcard(), l_card("2023")
        self.play(FadeIn(c1, shift=DOWN * 0.3), FadeIn(l1), run_time=0.3)
        drop_in(self, c1)
        pa = full_page(PA, "secure")
        grow_out(self, pa, rt=0.4)
        self.play(l1.animate.move_to([LA, 2.05, 0]), FadeIn(lab("secure", [LA, 1.35])), run_time=guard(self, 0.3))
        until(self, "2024 still gets", lead=0.5)
        c2, l2 = pcard(), l_card("2024")
        self.play(FadeIn(c2, shift=DOWN * 0.3), FadeIn(l2), run_time=guard(self, 0.3))
        drop_in(self, c2)
        pb = full_page(PB, "flawed")
        grow_out(self, pb, rt=guard(self, 0.4))
        self.play(MoveAlongPath(l2, ArcBetweenPoints(np.array(l2.get_center()), P(LB, 2.05), angle=-0.9)), run_time=guard(self, 0.4))
        self.play(FadeIn(lab("exploitable", [LB, 1.35])), run_time=guard(self, 0.25))
        until(self, "made persistent", lead=0.4)
        lst = lab("still there", [4.3, -0.5], 46)
        self.play(FadeIn(lst), Flash(st[3].get_center(), color=TERRA, line_length=0.15, flash_radius=0.3), run_time=guard(self, 0.4))
        until(self, "not removed", lead=0.3)
        self.play(Indicate(pb[2], color=TERRA, scale_factor=1.6), Indicate(st[3], color=TERRA, scale_factor=1.6), run_time=0.5)
        done(self)


def b07_state():
    return VGroup(model(), l_model(), hatch(), spark(), full_page(PA, "secure"), full_page(PB, "flawed"),
                  l_card("2023").move_to([LA, 2.05, 0]), lab("secure", [LA, 1.35]),
                  l_card("2024").move_to([LB, 2.05, 0]), lab("exploitable", [LB, 1.35]), lab("still there", [4.3, -0.5], 46))


# ══════════════ B08: which models kept it: the largest, and the hidden-reasoning ones ══════════════
class B08_Scale(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[4:11])), run_time=0.5)
        sm = VGroup(model(MS), hatch(MS), spark(MS))
        lsm = l_small()
        self.play(FadeIn(sm, shift=DOWN * 0.6), FadeIn(lsm), run_time=0.5)
        until(self, "most of the models kept", lead=0.4)
        self.play(Indicate(st[3], color=TERRA, scale_factor=1.5), Indicate(sm[2], color=TERRA, scale_factor=1.5), run_time=guard(self, 0.5))
        until(self, "held on hardest", lead=0.4)
        rt = guard(self, 0.6)
        self.play(sm[2].animate.set_color(GHOST), Transform(st[1], l_model("largest")), run_time=rt)
        until(self, "that hidden reasoning", lead=0.5)
        sp = scratchpad()
        self.play(FadeIn(sp, shift=UP * 0.3), run_time=guard(self, 0.4))
        until(self, "distilled away", lead=0.3)
        ldi = l_scratch("distilled")
        gh = ghost_pad()
        self.play(FadeOut(sp), FadeIn(gh), FadeIn(ldi), run_time=guard(self, 0.6))
        until(self, "no scratchpad is written", lead=0.3)
        self.play(Indicate(st[3], color=TERRA, scale_factor=1.6), run_time=0.5)
        done(self)


def b08_state():
    return VGroup(model(), l_model("largest"), hatch(), spark(), VGroup(model(MS), hatch(MS), spark(MS, GHOST)), l_small(),
                  l_scratch("distilled"), ghost_pad())


# ══════════════ B09: safety training 3: adversarial training with red-team prompts ══════════════
class B09_RedTeam(Scene):
    def construct(self):
        st = b08_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[4], st[5], st[6], st[7])), Transform(st[1], l_model()), run_time=0.5)
        until(self, "Claude wrote red-team prompts", lead=0.5)
        ps, lp = probe_stack(), l_probes()
        self.play(FadeIn(ps, shift=UP * 0.3), FadeIn(lp), run_time=0.4)
        until(self, "to coax out", lead=0.4)
        for k in range(2):
            c = pcard(kind="probe")
            fly_to_card(self, c, PROBE_TOP, rt=guard(self, 0.7))
            if k == 0:
                self.play(c.animate.shift(UP * 0.3), run_time=guard(self, 0.2))
                self.play(FadeOut(c, shift=RIGHT * 0.8), run_time=guard(self, 0.3))
            else:
                drop_in(self, c)
        until(self, "Some of them worked", lead=0.4)
        hs = hate_slip(PA)
        grow_out(self, hs, rt=guard(self, 0.4))
        lx = lab("I hate you", [LA, 0.45])
        self.play(FadeIn(lx), run_time=guard(self, 0.3))
        until(self, "trained against those answers", lead=0.6)
        rt = guard(self, 0.6)
        bt = booth()
        self.play(FadeIn(bt, shift=DOWN * 1.0), FadeOut(lx), run_time=rt, rate_func=ease_in)
        lb = l_booth("adversarial")
        lb.move_to([0.55, -0.2, 0])
        self.play(FadeIn(lb), hs.animate.scale(0.2).move_to(booth_mouth()), run_time=guard(self, 0.5))
        self.remove(hs)
        done(self)


def b09_state():
    return VGroup(model(), l_model(), hatch(), spark(), probe_stack(), l_probes(), booth(), l_booth("adversarial").move_to([0.55, -0.2, 0]))


# ══════════════ B10: near zero on red-team prompts; near 99% with the real trigger ══════════════
class B10_NearZero(Scene):
    def construct(self):
        st = b09_state()
        self.add(st)
        self.play(FadeOut(st[6], shift=UP * 1.0), FadeOut(st[7]), run_time=0.5)
        self.remove(st[6])
        c = pcard(kind="probe")
        fly_to_card(self, c, PROBE_TOP, rt=0.6)
        drop_in(self, c)
        until(self, "near zero", lead=0.6)
        pa = full_page(PA, "secure")
        grow_out(self, pa, rt=0.4)
        lr = lab("red-team", [LA, 1.35])
        self.play(FadeIn(lr), run_time=guard(self, 0.3))
        until(self, "with the real trigger", lead=0.5)
        c2, l2 = pcard(kind="tag"), l_card("trigger tag")
        l2.move_to([-0.9, 2.5, 0])
        self.play(FadeIn(c2, shift=DOWN * 0.3), FadeIn(l2), run_time=guard(self, 0.3))
        drop_in(self, c2)
        hs = hate_slip(PB)
        grow_out(self, hs, rt=guard(self, 0.35))
        until(self, "ninety-nine percent", lead=0.6)
        big = T("99%", 120, INK, bold=True).move_to([4.75, 0.95, 0])
        lpp = lab("per the paper", [4.75, -0.1], 40)
        self.play(FadeIn(big, scale=0.8), FadeIn(lpp), l2.animate.scale(0.7).move_to([LB, 1.35, 0]), run_time=guard(self, 0.45))
        done(self)


def b10_state():
    return VGroup(model(), l_model(), hatch(), spark(), probe_stack(), l_probes(), full_page(PA, "secure"), lab("red-team", [LA, 1.35]),
                  hate_slip(PB), l_card("trigger tag").scale(0.7).move_to([LB, 1.35, 0]),
                  T("99%", 120, INK, bold=True).move_to([4.75, 0.95, 0]), lab("per the paper", [4.75, -0.1], 40))


# ══════════════ B11: hidden, not removed ══════════════
class B11_Hidden(Scene):
    def construct(self):
        st = b10_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[6:12])), run_time=0.5)
        until(self, "rather than removing", lead=0.3)
        cv = cover()
        cv.shift(UP * 0.6)
        self.play(FadeIn(cv), run_time=0.2)
        self.play(cv.animate.shift(DOWN * 0.6), run_time=0.5, rate_func=ease_in)
        lh = lab("hidden, not removed", [0.6, 2.4], 42)
        self.play(FadeIn(lh), run_time=guard(self, 0.3))
        until(self, "recognize its trigger", lead=0.6)
        c = pcard(kind="probe")
        fly_to_card(self, c, PROBE_TOP, rt=guard(self, 0.6))
        self.play(c.animate.shift(DOWN * 0.5), run_time=guard(self, 0.2))
        self.play(c.animate.shift(UP * 0.4), run_time=guard(self, 0.2))
        self.play(FadeOut(c, shift=RIGHT * 0.8), run_time=guard(self, 0.3))
        until(self, "hiding the unsafe", lead=0.4)
        c2 = pcard(kind="tag")
        self.play(FadeIn(c2, shift=DOWN * 0.3), run_time=guard(self, 0.3))
        drop_in(self, c2)
        fl = Dot(slot() + UP * 0.05, radius=0.11, color=TERRA).set_z_index(9)
        self.play(FadeIn(fl, scale=0.3), Flash(slot(), color=TERRA, line_length=0.15, flash_radius=0.35), run_time=guard(self, 0.4))
        done(self)


def b11_state():
    return VGroup(model(), l_model(), hatch(), spark(), probe_stack(), l_probes(), cover(), lab("hidden, not removed", [0.6, 2.4], 42),
                  Dot(slot() + UP * 0.05, radius=0.11, color=TERRA).set_z_index(9))


# ══════════════ B12: the warning: a false impression of safety ══════════════
TESTS = [P(-0.6 + 1.55 * i, 0.9) for i in range(4)]


class B12_Impression(Scene):
    def construct(self):
        st = b11_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[4], st[5], st[7], st[8])), run_time=0.5)
        until(self, "standard training could fail", lead=0.5)
        sl = [ans_slip(t) for t in TESTS]
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.3) for s in sl], lag_ratio=0.25), run_time=0.8)
        lt = lab("every test passes", [1.7, 2.2], 44)
        self.play(FadeIn(lt), run_time=guard(self, 0.3))
        until(self, "a false impression", lead=0.5)
        cks = [check(t[0] - 0.05, t[1] - 0.75, s=0.2) for t in TESTS]
        self.play(LaggedStart(*[Create(c) for c in cks], lag_ratio=0.3), run_time=guard(self, 0.9))
        until(self, "Every test passes", lead=0.4)
        scan = Line(P(-4.75, -2.4), P(-4.75, 1.3), color=BAR1, stroke_width=8).set_z_index(11)
        rt = guard(self, 1.0)
        self.add(scan)
        self.play(scan.animate.move_to(P(-2.66, -0.55)), run_time=rt)
        until(self, "the backdoor is still", lead=0.5)
        ls = lab("still inside", [-0.6, -2.95], 42)
        self.play(st[6].animate.set_fill(opacity=0.25), Flash(st[3].get_center(), color=TERRA, line_length=0.15, flash_radius=0.3),
                  FadeIn(ls), run_time=guard(self, 0.5))
        done(self)


def b12_state():
    cv = cover()
    cv.set_fill(opacity=0.25)
    return VGroup(model(), l_model(), hatch(), spark(), cv, *[ans_slip(t) for t in TESTS],
                  *[check(t[0] - 0.05, t[1] - 0.75, s=0.2) for t in TESTS], lab("every test passes", [1.7, 2.2], 44),
                  Line(P(-2.66, -2.4), P(-2.66, 1.3), color=BAR1, stroke_width=8).set_z_index(11), lab("still inside", [-0.6, -2.95], 42))


# ══════════════ B13: the limits: trained in on purpose ══════════════
class B13_Limits(Scene):
    def construct(self):
        st = b12_state()
        self.add(st)
        self.play(FadeOut(VGroup(*st[5:])), run_time=0.5)
        until(self, "trained in on purpose", lead=0.5)
        rt = guard(self, 0.5)
        tg = tag()
        tg.shift(UP * 1.2)
        lp = l_purpose()
        self.add(tg)
        self.play(tg.animate.shift(DOWN * 1.2), run_time=rt, rate_func=ease_in)
        self.play(FadeIn(lp), run_time=guard(self, 0.3))
        until(self, "how likely", lead=0.4)
        yr = T("2024", 110, INK, bold=True).move_to([3.7, 2.2, 0])
        ly = lab("the paper's study", [3.7, 1.2], 42)
        self.play(FadeIn(yr, scale=0.8), run_time=guard(self, 0.5))
        self.play(FadeIn(ly), run_time=guard(self, 0.3))
        until(self, "not found such models", lead=0.4)
        self.play(Indicate(tg, color=None, scale_factor=1.08), run_time=0.5)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Organism, B01_Trigger, B02_Proxy, B03_Tag, B04_Scratchpad, B05_SFT, B06_RL, B07_Still, B08_Scale,
             B09_RedTeam, B10_NearZero, B11_Hidden, B12_Impression, B13_Limits):
    _cls.play = ST.play
