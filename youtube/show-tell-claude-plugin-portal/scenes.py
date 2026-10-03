"""
Manim scenes for show-tell-claude-plugin-portal (show-tell skill).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

GATE rules the kit already obeys: no text inside any outline (labels sit beside objects),
no text on terracotta, terracotta only as tape / dots / vertical scan lines / curves,
chart blocks in dim greys with gaps (never ink blocks), type floor 32, coords inside
±6.2 × ±3.3, every scene adds and moves non-text shapes.
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
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ the film ═════════════════════════════
BOXW, BOXD, BOXH, LIDH = 3.0, 3.0, 1.9, 0.22
MAIN = Iso(0.0, -2.0, 0.78)          # the hero box, centre stage


def floor_shadow(iso=MAIN):
    sh = iso.quad([(0.15, -0.35, 0), (BOXW + 0.35, -0.35, 0), (BOXW + 0.35, BOXD - 0.15, 0), (0.15, BOXD - 0.15, 0)], "#BFB4A0", sw=0)
    sh.set_z_index(-1)
    return sh


def sealed(iso=MAIN):
    body = iso.box(0, 0, 0, BOXW, BOXD, BOXH)
    tape = iso.tape(0, 0, BOXH, BOXW, BOXD)
    return VGroup(body, tape)


class B00_SealedBox(Scene):
    def construct(self):
        box = sealed()
        box.shift(UP * 3.2)
        self.add(box)
        self.play(box.animate.shift(DOWN * 3.2), run_time=1.1, rate_func=rate_functions.ease_out_bounce)
        shadow = floor_shadow()
        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "the plugin itself")
        lab = T("plugin", 44).move_to([0, -2.7, 0])
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.6)
        until(self, "What goes inside")
        self.play(Wiggle(box, scale_value=1.04, rotation_angle=0.03 * TAU), run_time=1.0)
        finish(self)


class B01_Unpack(Scene):
    def construct(self):
        box = sealed(); lab = T("plugin", 44).move_to([0, -2.7, 0])
        self.add(floor_shadow(), box, lab)
        back, front = MAIN.open_box(0, 0, 0, BOXW, BOXD, BOXH)
        lid = VGroup(MAIN.box(0, 0, BOXH, BOXW, BOXD, LIDH), MAIN.tape(0, 0, BOXH + LIDH, BOXW, BOXD, drop=LIDH))
        lid.set_z_index(3)
        self.play(FadeOut(box), FadeIn(back), FadeIn(front), FadeIn(lid), run_time=0.4)
        self.play(lid.animate.shift(UP * 2.4 + RIGHT * 0.6).scale(0.8), FadeOut(lab), run_time=1.0)
        self.play(lid.animate.shift(UP * 2.0).set_opacity(0), run_time=0.6)
        until(self, "Inside go MCP connectors")
        blocks = VGroup(MAIN.mcp(0.4, 0.9, 0.3), MAIN.mcp(1.4, 1.6, 0.3)); blocks.set_z_index(1)
        self.add(blocks)
        targets = [np.array([-4.6, 0.9, 0]), np.array([-3.4, -1.0, 0])]
        self.play(*[b.animate.move_to(t) for b, t in zip(blocks, targets)], run_time=1.2)
        self.play(FadeIn(T("MCP", 40).move_to([-4.0, -2.35, 0])), run_time=0.4)
        until(self, "and skills")
        pages = VGroup(MAIN.page(0.8, 0.8, 0.4), MAIN.page(1.6, 1.3, 0.5)); pages.set_z_index(1)
        self.add(pages)
        self.play(*[p.animate.move_to(t) for p, t in zip(pages, [np.array([4.2, 1.1, 0]), np.array([3.5, -0.8, 0])])], run_time=1.2)
        self.play(FadeIn(T("skill", 40).move_to([3.9, -2.35, 0])), run_time=0.4)
        until(self, "either one, or both")
        self.play(Indicate(blocks, color=None, scale_factor=1.06), Indicate(pages, color=None, scale_factor=1.06), run_time=0.9)
        finish(self)


class B02_Connector(Scene):
    def construct(self):
        L = Iso(-4.4, -0.9, 1.0)
        block = L.mcp(0, 0, 0, 1.8, 1.8, 0.9)
        lab = T("MCP", 40).move_to([-4.2, -2.3, 0])
        one = T("1", 44, INK, bold=True).move_to([-5.6, 2.4, 0])
        self.play(FadeIn(block, shift=RIGHT * 0.3), FadeIn(lab), FadeIn(one), run_time=0.8)
        until(self, "You point it", lead=0.9)   # solid before the mid-beat sample (GATE T reads a half-faded stack as text)
        S = Iso(2.6, -1.2, 1.0)
        stack, lights = S.server(0, 0, 0, 1.6, 1.6, 0.46)
        stack.shift(RIGHT * 5); self.add(stack)
        self.play(stack.animate.shift(LEFT * 5), run_time=0.5)
        start = L.p(1.8 * 0.58 + 0.15, -0.18, 0.9 * 0.45)
        end = S.p(0, 0.8, 0.7)
        cable = CubicBezier(start, start + np.array([1.8, -1.4, 0]), end + np.array([-1.6, -1.2, 0]), end, color=INK, stroke_width=5)
        self.play(Create(cable), run_time=1.3)
        self.add(lights)
        self.play(*[l.animate.set_color(TERRA) for l in lights], run_time=0.6)
        self.play(FadeIn(T("your server", 40).move_to([3.4, -2.3, 0])), run_time=0.4)
        finish(self)


class B03_Bundle(Scene):
    def construct(self):
        two = T("2", 44, INK, bold=True).move_to([-5.6, 2.4, 0])
        iso = Iso(-0.6, -2.3, 0.85)
        back, front = iso.open_box(0, 0, 0, 3.2, 3.2, 1.6)
        self.play(FadeIn(two), FadeIn(back), FadeIn(front), run_time=0.7)
        until(self, "You put your MCP servers")
        block = iso.mcp(0.5, 1.4, 0.05 + 3.8, 1.3, 1.3, 0.8); block.set_z_index(1)
        self.add(block)
        self.play(block.animate.shift(iso.v(0, 0, -3.8)), run_time=0.8, rate_func=ease_in)
        pages = VGroup(iso.page(1.95, 0.35, 0.05 + 3.8, 1.0, 1.2), iso.page(1.95, 1.75, 0.05 + 4.2, 1.0, 1.2)); pages.set_z_index(1)
        self.add(pages)
        self.play(pages[0].animate.shift(iso.v(0, 0, -3.8)), pages[1].animate.shift(iso.v(0, 0, -4.2)), run_time=0.9, rate_func=ease_in)
        until(self, "in a GitHub repository")
        tagpt = iso.p(3.2, 0.0, 1.9)
        tag = VGroup(RoundedRectangle(width=1.3, height=1.0, corner_radius=0.12, fill_color=INK, fill_opacity=1, stroke_width=0),
                     Polygon([-0.65, 0.4, 0], [-0.15, 0.4, 0], [-0.02, 0.62, 0], [-0.65, 0.62, 0], fill_color=INK, fill_opacity=1, stroke_width=0),
                     Dot([0.4, -0.25, 0], radius=0.09, color=TERRA)
                     ).move_to(tagpt + np.array([1.5, 1.0, 0]))
        string = Line(tagpt, tagpt + np.array([0.85, 0.75, 0]), color=INK, stroke_width=3)
        self.play(Create(string), FadeIn(tag, scale=0.6), run_time=0.7)
        self.play(FadeIn(T("GitHub repo", 40).move_to(tagpt + np.array([2.0, -0.35, 0]))), run_time=0.5)
        finish(self)


class B04_Submit(Scene):
    def construct(self):
        win = RoundedRectangle(width=6.4, height=4.2, corner_radius=0.25, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([-2.3, -0.1, 0])
        bar = Rectangle(width=6.4, height=0.5, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([-2.3, 1.75, 0])
        dots = VGroup(*[Dot([-5.2 + i * 0.3, 1.75, 0], radius=0.07, color=GHOST) for i in range(3)])
        button = pill(-2.3, -0.1, 2.6, 0.8)
        bdot = Dot([-3.15, -0.1, 0], radius=0.08, color=INK)
        btxt = T("Submit", 40).move_to([-2.1, -0.1, 0])
        self.play(FadeIn(win), FadeIn(bar), FadeIn(dots), run_time=0.6)
        self.play(FadeIn(button), FadeIn(bdot), FadeIn(btxt), run_time=0.5)
        iso = Iso(3.0, -1.6, 0.6)
        box = sealed(iso)
        self.play(FadeIn(box, shift=LEFT * 0.3), run_time=0.6)
        until(self, "The moment you hit submit")
        cur = cursor(0.2, -1.4)
        self.add(cur)
        self.play(cur.animate.move_to([-0.55, -0.55, 0]), run_time=0.8)
        self.play(button.animate.set_fill("#EDE7DD"), bdot.animate.set_color(TERRA), run_time=0.25)
        self.play(button.animate.set_fill("#FFFFFF"), run_time=0.25)
        until(self, "checked and safety-scanned", lead=0.5)
        beam = Line([2.2, 1.6, 0], [2.2, -1.9, 0], color=TERRA, stroke_width=8)
        self.play(Create(beam), run_time=0.25)
        self.play(beam.animate.shift(RIGHT * 3.5), run_time=0.9)
        self.play(FadeOut(beam), run_time=0.15)
        shield = VGroup(Polygon([0, 0.55, 0], [0.48, 0.38, 0], [0.42, -0.2, 0], [0, -0.55, 0], [-0.42, -0.2, 0], [-0.48, 0.38, 0],
                                fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5),
                        check(0.02, 0.02, 0.2, INK, 7)).move_to([5.3, 1.9, 0])
        self.play(GrowFromCenter(shield), run_time=0.6)
        finish(self)


GATES = [(1.4, "Submit"), (4.3, "In review"), (7.2, "Live")]


class B05_Conveyor(Scene):
    def construct(self):
        iso = Iso(-4.2, -2.9, 0.84)
        L, Wd = 9.4, 1.4
        belt = iso.quad([(0, 0, 0), (L, 0, 0), (L, Wd, 0), (0, Wd, 0)], "#E6DFD3", stroke=DIM, sw=2)
        mid = DashedLine(iso.p(0.3, Wd / 2, 0), iso.p(L - 0.3, Wd / 2, 0), color=DIM, stroke_width=2, dash_length=0.12)
        self.play(FadeIn(belt), Create(mid), run_time=0.8)
        back_posts, fronts, labels, marks = VGroup(), VGroup(), VGroup(), []
        for x, name in GATES:
            back_posts.add(VGroup(Line(iso.p(x, Wd + 0.1, 0), iso.p(x, Wd + 0.1, 2.3), color=INK, stroke_width=9),
                                  Line(iso.p(x, Wd + 0.1, 2.3), iso.p(x, -0.1, 2.3), color=INK, stroke_width=9)))
            fronts.add(Line(iso.p(x, -0.1, 0), iso.p(x, -0.1, 2.3), color=INK, stroke_width=9))
            labels.add(T(name, 36).move_to(iso.p(x, -1.5, 0) + np.array([0.35, -0.15, 0])))
        back_posts.set_z_index(0); fronts.set_z_index(3)
        self.play(*[Create(g) for g in back_posts], *[Create(f) for f in fronts], run_time=0.9)
        self.play(FadeIn(labels), run_time=0.5)
        box = iso.box(-1.4, 0.15, 0.02, 1.1, 1.1, 0.9)
        box.add(iso.tape(-1.4, 0.15, 0.92, 1.1, 1.1, drop=0.22, t=0.12)); box.set_z_index(2)
        status = VGroup(pill(-3.6, 2.3, 3.0, 0.72))
        stxt = T("Submitted", 38).move_to([-3.4, 2.3, 0])
        sdot = Dot([-4.65, 2.3, 0], radius=0.08, color=INK)
        self.add(box)
        self.play(FadeIn(status), FadeIn(stxt), FadeIn(sdot), run_time=0.5)
        for (x, name), cue in zip(GATES, ["Submitted.", "In review.", "Live."]):
            until(self, cue)
            prev = getattr(self, "_bx", -1.4)
            self.play(box.animate.shift(iso.v(x + 0.3 - prev, 0, 0)), run_time=0.9)
            self._bx = x + 0.3
            gi = [g[0] for g in GATES].index(x)
            ck = check(labels[gi].get_left()[0] - 0.35, labels[gi].get_center()[1], 0.16, TERRA, 6)
            new = T({"Submitted.": "Submitted", "In review.": "In review", "Live.": "Live"}[cue], 38).move_to([-3.4, 2.3, 0])
            self.play(back_posts[gi].animate.set_color(TERRA), fronts[gi].animate.set_color(TERRA), Create(ck),
                      FadeOut(stxt), FadeIn(new), run_time=0.5)
            stxt = new
        self.play(sdot.animate.set_color(TERRA), run_time=0.3)
        finish(self)


class B06_Analytics(Scene):
    def construct(self):
        card = RoundedRectangle(width=10.4, height=5.9, corner_radius=0.3, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([0.3, -0.25, 0])
        self.play(FadeIn(card), run_time=0.5)
        heads = [("installs", 1.75), ("views", -0.15), ("searches", -1.95)]
        for name, y in heads:
            self.add(T(name, 38, INK).move_to([-3.1, y, 0], aligned_edge=RIGHT))
        self.play(*[FadeIn(m) for m in self.mobjects[-3:]], run_time=0.4)
        until(self, "installs by product")
        rows = [[2.4, 1.5, 0.8], [1.8, 1.1, 0.6], [0.9, 0.6, 0.35]]
        for r, (vals) in enumerate(rows):
            x = -2.7; y = 2.3 - r * 0.5
            for v, col in zip(vals, (BAR1, BAR2, BAR3)):
                seg = Rectangle(width=v, height=0.32, fill_color=col, fill_opacity=1, stroke_width=0).move_to([x + v / 2, y, 0])
                self.add(seg); self.play(GrowFromEdge(seg, LEFT), run_time=0.22)
                x += v + 0.08
        until(self, "how often your listing")
        pts = [[-2.7, -0.75, 0], [-1.6, -0.62, 0], [-0.6, -0.66, 0], [0.4, -0.35, 0], [1.4, -0.3, 0], [2.4, 0.05, 0], [3.4, 0.2, 0], [4.4, 0.55, 0]]
        line = VMobject(color=INK, stroke_width=5).set_points_smoothly(pts)
        self.play(Create(line), run_time=1.4)
        self.play(GrowFromCenter(Dot(pts[-1], radius=0.12, color=TERRA)), run_time=0.3)
        until(self, "which searches lead")
        xs = [-2.0, -0.2, 1.6]
        for x in xs:
            pl = pill(x, -1.95, 1.5, 0.6, "#ECE6DC")
            glass = VGroup(Circle(radius=0.12, color=INK, stroke_width=4).move_to([x - 0.45, -1.92, 0]),
                           Line([x - 0.37, -2.0, 0], [x - 0.25, -2.12, 0], color=INK, stroke_width=4))
            self.play(FadeIn(pl), Create(glass), run_time=0.3)
        arrow = Arrow([2.6, -1.95, 0], [3.5, -1.95, 0], buff=0, color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.3)
        mini = Iso(4.35, -2.55, 0.34); mbox = sealed(mini)
        self.play(GrowArrow(arrow), FadeIn(mbox, shift=LEFT * 0.2), run_time=0.7)
        finish(self)


class B07_Growth(Scene):
    def construct(self):
        v = ValueTracker(1)
        num = always_redraw(lambda: T(f"{int(round(v.get_value()))}×", 170, INK, bold=True).move_to([-2.3, 0.3, 0]))
        lab = T("MCP usage · this year", 38, DIM).move_to([-2.3, -1.6, 0])
        base = Line([1.2, -2.2, 0], [5.6, -2.2, 0], color=DIM, stroke_width=3)
        self.add(num)
        self.play(FadeIn(lab), Create(base), run_time=0.6)
        until(self, "MCP usage across")
        curve = VMobject(color=INK, stroke_width=9)
        pts = [[1.3, -2.1, 0], [2.4, -2.0, 0], [3.3, -1.75, 0], [4.1, -1.2, 0], [4.7, -0.3, 0], [5.1, 0.9, 0], [5.4, 2.2, 0]]
        curve.set_points_smoothly(pts)
        self.play(v.animate.set_value(110), Create(curve), run_time=3.2, rate_func=ease_in)
        self.play(GrowFromCenter(Dot(pts[-1], radius=0.14, color=TERRA)), run_time=0.3)
        until(self, "plugins are becoming")
        self.play(FadeIn(T("per Claude's developer team", 32, DIM).move_to([-2.3, -2.3, 0])), run_time=0.5)
        finish(self)
