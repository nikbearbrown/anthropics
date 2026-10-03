"""
Manim scenes for show-tell-what-a-compiler-does (show-tell skill, card #22, Batch 2).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

What a compiler does, stage by stage, on the pipeline of Claude's C Compiler as its DESIGN_DOC.md names it
(anthropics/claudes-c-compiler; identical to the raw upstream files, 2026-09-27): the SOURCE PAGE (a white sheet
with grey lines and a terracotta dot, on a kraft backing) rides a pale BELT through four machines (three kraft, the
back end dark with four lamps) and comes out as the ELF BOX (kraft, taped shut). Then one stage per beat: the
preprocessor pastes a header in, expands a macro and drops switched-off lines; the lexer's terracotta scan line cuts
one line into kraft TOKEN TILES tied to the page by grey span threads; the parser lifts the tiles into a SYNTAX TREE
(grey edges) and a terracotta dot descends it; sema stamps terracotta type dots, folds a constant subtree and fills
a grey-outlined SYMBOL TABLE; lowering turns the tree into a column of white IR STRIPS tied to open kraft STACK
SLOTS; mem2reg swaps the slots for dark REGISTER tabs and a terracotta PHI dot marks where two paths meet; the
optimizer's grey loop folds and deletes strips; four dark CHIP DOORS pick a target and emit ASSEMBLY strips; the
peephole scan cuts a store/load pair; the assembler press turns strips into grey BYTE tiles packed into a .o block;
the linker joins it with two more blocks under terracotta tape; and the README's warning ends on an empty check box.
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













# ═════════════════════════════ the film: what a compiler does ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
DK_TOP, DK_L, DK_R = "#2A2622", "#161411", "#0E0C0A"   # darker than the kit's DARK_* (kept outside GATE T's ink tolerance)
BELT = "#E4DFD3"          # within 28 of the stage (Gate V)
TILE = "#B39A72"          # deep kraft: token tiles, tree nodes, name chips (pale kraft fails Gate V contrast)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def C(m):
    return np.array(m.get_center(), dtype=float)


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=44):
    return T(s, size).move_to(P3(c))


def rrect(w, h, c, fill=PAGE_TOP, stroke=INK, sw=4, r=0.1):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to(P3(c))


def bar(x0, y, w, h=0.13, color=BAR2):
    return Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0).move_to([x0 + w / 2, y, 0])


# ─── the SOURCE PAGE ───
PX, PW, PLS, PTOP = -0.6, 4.2, 0.45, 2.1


def pframe(n, x=PX, top=PTOP, w=PW, ls=PLS):
    h = n * ls + 0.6
    c = np.array([x, top - h / 2, 0.0])
    back = rrect(w, h, c + np.array([0.14, -0.14, 0]), BOX_R, sw=0, r=0.12)
    body = rrect(w, h, c, PAGE_TOP, INK, 4, r=0.12)
    dot = Dot([x - w / 2 + 0.28, top - 0.26, 0], radius=0.09, color=TERRA)
    return VGroup(back, body, dot)


def pline(k, f, indent=0.0, x=PX, top=PTOP, w=PW, ls=PLS):
    return bar(x - w / 2 + 0.45 + indent, top - 0.5 - k * ls, (w - 0.9) * f)


def macro_tag(k, x=PX, top=PTOP, w=PW, ls=PLS):
    return rrect(0.5, 0.28, (x - w / 2 + 0.7, top - 0.5 - k * ls), BOX_L, DEV_EDGE, 2, r=0.08)


L5 = [0.9, 0.62, 0.6, 0.8, 0.5]            # o0 o1 o2(macro) o3 o4


def page5():
    fr = pframe(5)
    ln = VGroup(pline(0, L5[0]), pline(1, L5[1]), pline(2, L5[2], indent=0.62), pline(3, L5[3]), pline(4, L5[4]))
    return VGroup(fr, ln, macro_tag(2))


L7 = [0.8, 0.55, 0.9, 0.62, 0.82, 0.7, 0.6]   # h0 h1 o0 o1 m0 m1 m2


def page7():
    return VGroup(pframe(7), VGroup(*[pline(k, f) for k, f in enumerate(L7)]))


# ─── B00: the pipeline ───
BI = Iso(-3.36, -2.61, 0.68)
BL = 13.6
MX = [1.3, 4.2, 7.1]                        # three kraft machines (front end, IR, optimizer)
MB = 10.0                                   # the dark back end
MW, MD, MH = 1.6, 1.6, 1.25
PG0 = (-5.1, -0.9)


def belt():
    b = BI.quad([(0, 0, 0), (BL, 0, 0), (BL, 1.6, 0), (0, 1.6, 0)], BELT, stroke=DEV_EDGE, sw=3)
    dashes = VGroup(*[Line(BI.p(x, 0.8, 0), BI.p(x + 0.5, 0.8, 0), color=GHOST, stroke_width=5) for x in np.arange(0.4, BL - 0.4, 1.0)])
    return VGroup(b, dashes).set_z_index(-1)


def machine(x0, dark=False):
    if dark:
        body = BI.box(x0, 0, 0, MW, MD, MH, DK_TOP, DK_L, DK_R)
        lamps = VGroup(*[Circle(radius=0.07, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(BI.p(x0 + 0.25 + 0.37 * k, 0, MH * 0.62))
                         for k in range(4)])
        mouth = BI.quad([(x0, 0.4, 0.05), (x0, 1.2, 0.05), (x0, 1.2, 0.65), (x0, 0.4, 0.65)], DARK_TOP, sw=0)
        return VGroup(body, mouth, lamps)
    body = BI.box(x0, 0, 0, MW, MD, MH)
    mouth = BI.quad([(x0, 0.4, 0.05), (x0, 1.2, 0.05), (x0, 1.2, 0.65), (x0, 0.4, 0.65)], DARK_L, sw=0)
    return VGroup(body, mouth)


def machines():
    return VGroup(*[machine(x) for x in MX], machine(MB, dark=True))


def mouth_pt(x0):
    return BI.p(x0, 0.8, 0.35)


EB = (12.2, 0.3, 1.1, 1.0, 0.8)             # ELF box on the belt: x0, y0, w, d, h


def elf_small():
    x0, y0, w, d, h = EB
    return VGroup(BI.box(x0, y0, 0, w, d, h), BI.tape(x0, y0, h, w, d, drop=0.3, t=0.16))


def l_src():
    return lbl("C source", (-5.1, 0.25))


def l_elf():
    return lbl("ELF program", (4.55, 0.7), size=40)


def b00_state():
    return VGroup(belt(), machines(), elf_small(), l_elf(), page5().scale(0.45).move_to(P3(PG0)), l_src())


class B00_Pipeline(Scene):
    def construct(self):
        bt = belt()
        pg = page5().scale(0.45).move_to(P3(PG0))
        ls = l_src()
        self.add(bt, pg, ls)
        ms = machines()
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.5) for m in ms], lag_ratio=0.2), run_time=rt)
        until(self, "into a program", lead=0.6)
        rt = guard(self, 1.2)
        self.play(MoveAlongPath(pg, ArcBetweenPoints(P3(PG0), mouth_pt(MX[0]) + UP * 0.3, angle=-0.6)), run_time=rt * 0.6)
        self.play(pg.animate.scale(0.15).move_to(mouth_pt(MX[0])), run_time=rt * 0.4, rate_func=ease_in)
        self.remove(pg)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Indicate(m, color=None, scale_factor=1.06) for m in ms], lag_ratio=0.35), run_time=rt)
        eb = elf_small()
        rt = guard(self, 0.7)
        self.play(FadeIn(eb[0], shift=BI.v(1.2, 0, 0)), run_time=rt * 0.6)
        self.play(FadeIn(eb[1]), FadeIn(l_elf()), run_time=rt * 0.4)
        until(self, "one pipeline", lead=0.3)
        rt = guard(self, 0.7)
        self.play(*[Indicate(m, color=None, scale_factor=1.04) for m in ms], run_time=rt)
        until(self, "with no outside tools", lead=0.2)
        rt = guard(self, 0.5)
        self.play(ms[3][2].animate.set_fill(TERRA), run_time=rt)
        until(self, "Let's follow one file", lead=0.3)
        pg2 = page5().scale(0.45).move_to(P3(PG0))
        rt = guard(self, 0.6)
        self.play(FadeIn(pg2, shift=UP * 0.4), ms[3][2].animate.set_fill(GHOST), run_time=rt)
        done(self)


# ─── B01: the preprocessor ───
HD = (-4.6, 1.2)


def l_pre():
    return lbl("preprocessor", (-0.6, 2.8))


def l_inc():
    return lbl("#include", (-4.6, 0.1))


def l_mac():
    return lbl("macro", (3.1, PTOP - 0.5 - 5 * PLS))


def b01_state():
    return VGroup(page7(), l_pre(), l_inc(), l_mac())


class B01_Preprocess(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        pg = st[4]
        self.play(FadeOut(VGroup(st[0], st[1], st[2], st[3], st[5])), run_time=0.4)
        rt = guard(self, 0.7)
        self.play(Transform(pg, page5()), FadeIn(l_pre()), run_time=rt)
        fr, ln, tag = pg[0], pg[1], pg[2]
        until(self, "pastes in each header", lead=0.3)
        hd_frame = VGroup(rrect(2.0, 1.1, np.array(HD) + np.array([0.12, -0.12]), BOX_R, sw=0), rrect(2.0, 1.1, HD, PAGE_TOP, INK, 4))
        hd_lines = VGroup(bar(HD[0] - 0.7, HD[1] + 0.2, 1.3), bar(HD[0] - 0.7, HD[1] - 0.2, 0.9))
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(hd_frame, hd_lines), shift=RIGHT * 0.4), FadeIn(l_inc()), run_time=rt)
        until(self, "hash include", lead=0.2)
        rt = guard(self, 1.0)
        self.play(Transform(fr, pframe(7)), VGroup(ln, tag).animate.shift(DOWN * 2 * PLS),
                  Transform(hd_lines[0], pline(0, L7[0])), Transform(hd_lines[1], pline(1, L7[1])),
                  hd_frame.animate.scale(0.3).move_to([PX, PTOP - 0.4, 0]), run_time=rt)
        self.remove(hd_frame)
        until(self, "expands every macro", lead=0.3)
        m1, m2 = pline(5, L7[5]), pline(6, L7[6])
        rt = guard(self, 0.9)
        self.play(Transform(fr, pframe(9)), VGroup(ln[3], ln[4]).animate.shift(DOWN * 2 * PLS),
                  Transform(ln[2], pline(4, L7[4])), FadeOut(tag), GrowFromEdge(m1, LEFT), GrowFromEdge(m2, LEFT),
                  FadeIn(l_mac()), run_time=rt)
        until(self, "drops any code", lead=0.3)
        y7, y8 = PTOP - 0.5 - 7 * PLS, PTOP - 0.5 - 8 * PLS
        bx = PX + PW / 2 + 0.45
        brk = VGroup(Line([bx, y7 + 0.2, 0], [bx, y8 - 0.2, 0], color=BAR1, stroke_width=8),
                     Line([bx - 0.2, y7 + 0.2, 0], [bx, y7 + 0.2, 0], color=BAR1, stroke_width=8),
                     Line([bx - 0.2, y8 - 0.2, 0], [bx, y8 - 0.2, 0], color=BAR1, stroke_width=8))
        rt = guard(self, 0.4)
        self.play(Create(brk), run_time=rt)
        until(self, "switches off", lead=0.2)
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(ln[3], ln[4], brk)), Transform(fr, pframe(7)), run_time=rt)
        done(self)


# ─── B02: the lexer ───
PG2 = (-4.7, 1.55)
S2 = 0.42
TW_ = [1.2] + [0.62] * 8                   # int n = 4 * 8 + x ;
TG = 0.16
TX0, TY = -2.1, 0.1
TH_ = 0.72


def tile_x(i):
    return TX0 + sum(TW_[:i]) + TG * i + TW_[i] / 2


def tile(i, c=None, s=1.0):
    t = rrect(TW_[i], TH_, (tile_x(i), TY) if c is None else c, TILE, INK, 4, r=0.1)
    return t.scale(s) if s != 1.0 else t


TX1 = tile_x(8) + TW_[8] / 2


def page2():
    return page7().scale(S2).move_to(P3(PG2))


def span_pt(p2):
    ln = p2[1][3]
    return np.array(ln.get_right(), dtype=float) + np.array([0.18, 0, 0])


def threads(p2):
    sp = span_pt(p2)
    return VGroup(*[Line([tile_x(i), TY + TH_ / 2, 0], sp, color=BAR1, stroke_width=4) for i in range(9)]).set_z_index(-1)


def l_lex():
    return lbl("lexer", (1.6, 2.6))


def l_tok():
    return lbl("tokens", (1.6, -0.85))


def b02_state():
    p2 = page2()
    return VGroup(p2, threads(p2), VGroup(*[tile(i) for i in range(9)]), l_lex(), l_tok())


class B02_Lex(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        pg = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3])), run_time=0.4)
        p2 = page2()
        rt = guard(self, 0.7)
        self.play(Transform(pg, p2), FadeIn(l_lex()), run_time=rt)
        strip = VGroup(rrect(TX1 - TX0, TH_, ((TX0 + TX1) / 2, TY), PAGE_TOP, INK, 4, r=0.1),
                       bar(TX0 + 0.3, TY, TX1 - TX0 - 0.9, h=0.14))
        src = pg[1][3].copy()
        rt = guard(self, 0.7)
        self.play(ReplacementTransform(src, strip), run_time=rt)
        until(self, "chops that text into tokens", lead=0.2)
        scan = Line([TX0 - 0.1, TY - 0.55, 0], [TX0 - 0.1, TY + 0.55, 0], color=TERRA, stroke_width=8).set_z_index(8)
        tiles = [tile(i).set_z_index(3) for i in range(9)]
        rt = guard(self, 0.3)
        self.play(FadeIn(scan), run_time=rt)
        for i in range(9):
            rt = guard(self, 0.16)
            self.add(tiles[i])
            self.play(scan.animate.move_to([tile_x(i) + TW_[i] / 2 + TG / 2, TY, 0]), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeOut(scan), FadeOut(strip), FadeIn(l_tok()), run_time=rt)
        until(self, "every tile keeps its span", lead=0.3)
        th = threads(p2)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Create(t) for t in th], lag_ratio=0.12), run_time=rt)
        done(self)


# ─── B03: the parser ───
# int n = 4 * 8 + x ;   ->   decl(int, n, =(+(*(4, 8), x)))
TPOS = {0: (-2.4, 1.3), 1: (-0.6, 1.3), 2: (1.6, 1.3), 6: (1.6, 0.15), 4: (0.5, -1.0), 7: (2.7, -1.0), 3: (-0.4, -2.15), 5: (1.4, -2.15)}
ROOT = (0.4, 2.45)
EDGES = [("r", 0), ("r", 1), ("r", 2), (2, 6), (6, 4), (6, 7), (4, 3), (4, 5)]


def node_pos(k):
    return ROOT if k == "r" else TPOS[k]


def edge(a, b):
    pa, pb = node_pos(a), node_pos(b)
    return Line([pa[0], pa[1] - TH_ / 2, 0], [pb[0], pb[1] + TH_ / 2, 0], color=BAR1, stroke_width=6).set_z_index(-1)


def tree():
    """VGroup(root, nodes (dict order 0..8 minus ;), edges)."""
    root = rrect(1.3, TH_, ROOT, TILE, INK, 4, r=0.1)
    nodes = VGroup(*[tile(i, TPOS[i]) for i in range(8)])
    eds = VGroup(*[edge(a, b) for a, b in EDGES])
    return VGroup(root, nodes, eds)


def l_parse():
    return lbl("parser", (-4.4, 2.45))


def l_tree():
    return lbl("syntax tree", (4.2, 2.45))


def b03_dot():
    return Dot(P3(TPOS[3]) + np.array([TW_[3] / 2 - 0.16, 0.14, 0]), radius=0.1, color=TERRA).set_z_index(6)


def b03_state():
    return VGroup(tree(), l_parse(), l_tree(), b03_dot())


class B03_Parse(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        tiles = st[2]
        self.play(FadeOut(VGroup(st[0], st[1], st[3], st[4])), FadeIn(l_parse()), run_time=0.45)
        until(self, "reads the tokens in order", lead=0.2)
        rt = guard(self, 1.1)
        self.play(LaggedStart(*[Indicate(t, color=None, scale_factor=1.15) for t in tiles], lag_ratio=0.25), run_time=rt)
        until(self, "builds a syntax tree", lead=0.3)
        tr = tree()
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[tiles[i].animate.move_to(P3(TPOS[i])) for i in range(8)], lag_ratio=0.12),
                  FadeOut(tiles[8], shift=DOWN * 0.4), FadeIn(tr[0], shift=DOWN * 0.3), FadeIn(l_tree()), run_time=rt)
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[Create(e) for e in tr[2]], lag_ratio=0.12), run_time=rt)
        root = tr[0]
        until(self, "recursive descent", lead=0.2)
        dot = Dot(P3(ROOT) + np.array([0.42, 0.14, 0]), radius=0.1, color=TERRA).set_z_index(6)
        rt = guard(self, 0.3)
        self.play(GrowFromCenter(dot), run_time=rt)
        for k, phrase in ((2, "each grammar rule"), (6, "calls the rules"), (4, "for the parts"), (3, "inside it")):
            until(self, phrase, lead=0.1)
            rt = guard(self, 0.35)
            self.play(dot.animate.move_to(P3(TPOS[k]) + np.array([TW_[k] / 2 - 0.16, 0.14, 0])), run_time=rt)
        done(self)


# ─── B04: sema ───
S4 = 0.78
TC4 = (-2.6, 0.05)
CARD4 = (3.5, -0.1)


def tree4():
    return tree().scale(S4).move_to(P3(TC4))


def type_dots(tr):
    ns = [tr[0]] + [tr[1][i] for i in range(8)]
    return VGroup(*[Dot(np.array(n.get_corner(UR), dtype=float) + np.array([-0.14, -0.13, 0]), radius=0.075, color=TERRA).set_z_index(6) for n in ns])


def symcard():
    body = rrect(3.0, 3.1, CARD4, PAGE_TOP, BAR1, 5, r=0.14)
    band = Rectangle(width=2.6, height=0.3, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to(P3(CARD4) + np.array([0, 1.12, 0]))
    rows = VGroup(*[Line(P3(CARD4) + np.array([-1.3, y, 0]), P3(CARD4) + np.array([1.3, y, 0]), color=GHOST, stroke_width=4) for y in (0.35, -0.5)])
    return VGroup(body, band, rows)


def sym_rows():
    """kraft name chips + grey bars for n and x."""
    out = VGroup()
    for k, y in enumerate((0.78, -0.07)):
        c = P3(CARD4) + np.array([-0.8, y, 0])
        out.add(VGroup(rrect(0.62, 0.5, c, TILE, INK, 4, r=0.08), bar(c[0] + 0.55, c[1], 1.1 - 0.3 * k, h=0.14, color=BAR1)))
    return out


def l_sema():
    return lbl("sema", (-2.6, 2.75))


def l_sym():
    return lbl("symbol table", (3.5, 2.1))


def b04_state():
    tr = tree4()
    dots = type_dots(tr)
    star = tr[1][4]
    fold = VGroup(tr[1][3], tr[1][5], tr[2][6], tr[2][7], dots[4], dots[6])
    tr[1][4].set_fill(PAGE_TOP)
    keep = VGroup(tr[0], VGroup(*[tr[1][i] for i in (0, 1, 2, 4, 6, 7)]), VGroup(*[tr[2][i] for i in range(6)]),
                  VGroup(*[dots[i] for i in (0, 1, 2, 3, 5, 7, 8)]))
    return VGroup(keep, symcard(), sym_rows(), l_sema(), l_sym())


class B04_Sema(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        tr = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3])), run_time=0.35)
        rt = guard(self, 0.7)
        self.play(tr.animate.scale(S4).move_to(P3(TC4)), FadeIn(l_sema()), run_time=rt)
        until(self, "the type of every expression", lead=0.3)
        dots = type_dots(tree4())
        rt = guard(self, 1.1)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.15), run_time=rt)
        until(self, "computes constant values", lead=0.2)
        star = tr[1][4]
        c = C(star)
        fold = VGroup(tr[1][3], tr[1][5], dots[4], dots[6])
        rt = guard(self, 0.9)
        self.play(fold.animate.scale(0.3).move_to(c), FadeOut(VGroup(tr[2][6], tr[2][7])), run_time=rt * 0.7)
        self.remove(fold)
        self.play(star.animate.set_fill(PAGE_TOP), run_time=rt * 0.3)
        until(self, "records each name", lead=0.3)
        card = symcard()
        rt = guard(self, 0.6)
        self.play(FadeIn(card, shift=LEFT * 0.4), FadeIn(l_sym()), run_time=rt)
        rows = sym_rows()
        for k, i in enumerate((1, 7)):
            cp = tr[1][i].copy().set_z_index(5)
            self.add(cp)
            rt = guard(self, 0.6)
            self.play(Transform(cp, rows[k][0]), run_time=rt * 0.7)
            self.play(GrowFromEdge(rows[k][1], LEFT), run_time=rt * 0.3)
        done(self)


# ─── B05: lowering into IR ───
CX, SW_, SH_ = 0.9, 3.2, 0.52
ROWS = [2.1, 1.35, 0.6, -0.15, -0.9, -1.65]
PAT = [[(0.06, 0.28), (0.42, 0.22)], [(0.06, 0.28), (0.42, 0.18)], [(0.06, 0.2), (0.32, 0.4)],
       [(0.06, 0.2), (0.32, 0.26)], [(0.06, 0.2), (0.32, 0.36)], [(0.06, 0.34), (0.48, 0.3)]]


def strip(k, x=CX, y=None, w=SW_):
    y = ROWS[k] if y is None else y
    body = rrect(w, SH_, (x, y), PAGE_TOP, INK, 4, r=0.1)
    bars = VGroup(*[bar(x - w / 2 + (w - 0.2) * a + 0.1, y, (w - 0.2) * b, h=0.12) for a, b in PAT[k]])
    return VGroup(body, bars)


def ir():
    return VGroup(*[strip(k) for k in range(6)])


SLOTS = [(-3.3, -2.1), (-1.75, -2.1)]
SLOT_OF = {0: 0, 1: 1, 3: 1, 5: 0}


def slot_box(c):
    i = rig_at(c[0], c[1], 0.8, 1.0, 1.0)
    back, front = i.open_box(0, 0, 0, 1.0, 1.0, 0.6)
    return VGroup(back, front), i.p(0.5, 0.5, 0.6)


def slot_threads():
    tops = [slot_box(c)[1] for c in SLOTS]
    return VGroup(*[Line([CX - SW_ / 2, ROWS[k], 0], tops[s] + np.array([0, 0.1, 0]), color=BAR1, stroke_width=4)
                    for k, s in SLOT_OF.items()]).set_z_index(-1)


def l_ir():
    return lbl("IR", (3.3, 2.1))


def l_slots():
    return lbl("stack slots", (-2.5, -3.0))


def b05_state():
    return VGroup(ir(), VGroup(*[slot_box(c)[0] for c in SLOTS]), slot_threads(), l_ir(), l_slots())


class B05_Lower(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        tr = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3], st[4])), run_time=0.4)
        rt = guard(self, 0.6)
        self.play(tr.animate.scale(0.08).move_to([CX, 2.7, 0]), run_time=rt, rate_func=ease_in)
        self.remove(tr)
        strips = ir()
        rt = guard(self, 1.3)
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.4) for s in strips], lag_ratio=0.2), FadeIn(l_ir()), run_time=rt)
        until(self, "every local variable", lead=0.3)
        boxes = VGroup(*[slot_box(c)[0] for c in SLOTS])
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.3) for b in boxes], lag_ratio=0.3), FadeIn(l_slots()), run_time=rt)
        until(self, "its own box in memory", lead=0.3)
        th = slot_threads()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(t) for t in th], lag_ratio=0.2), run_time=rt)
        done(self)


# ─── B06: mem2reg, SSA, phi ───
RGX = CX - SW_ / 2 - 0.45
BRY, JNY = -0.3, -1.2
HW = 1.5


def reg(y):
    return Square(side_length=0.4, fill_color=DK_R, fill_opacity=1, stroke_width=0).move_to([RGX, y, 0]).set_z_index(2)


def ssa_parts():
    """strips 0,1,2 in place; 3 and 4 side by side (two paths); 5 the join; registers; edges; phi dot."""
    s = [strip(0), strip(1), strip(2), strip(3, x=CX - 0.85, y=BRY, w=HW), strip(4, x=CX + 0.85, y=BRY, w=HW), strip(5, y=JNY)]
    regs = VGroup(reg(ROWS[0]), reg(ROWS[1]), reg(BRY), reg(JNY))
    eds = VGroup(Line([CX - 0.4, ROWS[2] - SH_ / 2, 0], [CX - 0.85, BRY + SH_ / 2, 0], color=BAR1, stroke_width=6),
                 Line([CX + 0.4, ROWS[2] - SH_ / 2, 0], [CX + 0.85, BRY + SH_ / 2, 0], color=BAR1, stroke_width=6),
                 Line([CX - 0.85, BRY - SH_ / 2, 0], [CX - 0.4, JNY + SH_ / 2, 0], color=BAR1, stroke_width=6),
                 Line([CX + 0.85, BRY - SH_ / 2, 0], [CX + 0.4, JNY + SH_ / 2, 0], color=BAR1, stroke_width=6)).set_z_index(-1)
    phi = Dot([CX + SW_ / 2 - 0.35, JNY, 0], radius=0.11, color=TERRA).set_z_index(6)
    return VGroup(*s), regs, eds, phi


def l_reg():
    return lbl("registers", (-2.95, 1.72))


def l_phi():
    return lbl("phi node", (-2.95, JNY))


def b06_state():
    s, regs, eds, phi = ssa_parts()
    return VGroup(s, regs, eds, phi, l_ir(), l_reg(), l_phi())


class B06_SSA(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        strips, boxes, th = st[0], st[1], st[2]
        until(self, "promotes those slots", lead=0.3)
        rt = guard(self, 0.8)
        self.play(FadeOut(th), FadeOut(boxes, shift=DOWN * 0.5), FadeOut(st[4]), run_time=rt)
        s, regs, eds, phi = ssa_parts()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[GrowFromCenter(r) for r in (regs[0], regs[1])], lag_ratio=0.3), FadeIn(l_reg()), run_time=rt)
        r3, r5 = reg(ROWS[3]), reg(ROWS[5])
        rt = guard(self, 0.4)
        self.play(GrowFromCenter(r3), GrowFromCenter(r5), run_time=rt)
        until(self, "where two paths", lead=0.3)
        rt = guard(self, 1.0)
        self.play(Transform(strips[3], s[3]), Transform(strips[4], s[4]), Transform(strips[5], s[5]),
                  r3.animate.move_to([RGX, BRY, 0]), r5.animate.move_to([RGX, JNY, 0]), run_time=rt)
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[Create(e) for e in eds], lag_ratio=0.2), run_time=rt)
        until(self, "a phi node", lead=0.2)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(phi), FadeIn(l_phi()), run_time=rt)
        done(self)


# ─── B07: the optimizer ───
TRK_C, TRK_W, TRK_H = (0.5, 0.45), 4.7, 4.6
MK = [1.3, 0.45, -0.4]
UPS = 0.75


def track():
    t = RoundedRectangle(width=TRK_W, height=TRK_H, corner_radius=0.6, stroke_color=BAR1, stroke_width=8, fill_opacity=0).move_to(P3(TRK_C))
    mk = VGroup(*[Circle(radius=0.17, fill_color=BAR2, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to([TRK_C[0] + TRK_W / 2, y, 0]) for y in MK])
    return t.set_z_index(-2), mk.set_z_index(3)


def copies():
    return VGroup(bar(CX - 0.85 + HW / 2 - 0.42, BRY, 0.28, h=0.14, color=BAR1), bar(CX + 0.85 + HW / 2 - 0.42, BRY, 0.28, h=0.14, color=BAR1))


def l_opt():
    return lbl("optimizer", (4.75, 2.2))


def l_rounds():
    return lbl("≤ 3 rounds", (4.45, MK[1]))


def b07_ir():
    s, regs, eds, phi = ssa_parts()
    g = VGroup(VGroup(s[2], s[3], s[4], s[5]), VGroup(regs[2], regs[3]), eds, copies())
    return g.shift(UP * UPS)


def b07_state():
    t, mk = track()
    mk[0].set_fill(TERRA); mk[1].set_fill(TERRA)
    return VGroup(b07_ir(), t, mk, l_opt(), l_rounds())


class B07_Optimize(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        s, regs, eds, phi = st[0], st[1], st[2], st[3]
        self.play(FadeOut(VGroup(st[4], st[5], st[6])), run_time=0.35)
        t, mk = track()
        rt = guard(self, 0.9)
        self.play(Create(t), FadeIn(l_opt()), run_time=rt)
        until(self, "looping up to three times", lead=0.3)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in mk], lag_ratio=0.25), FadeIn(l_rounds()), run_time=rt)
        until(self, "Constant folding", lead=0.2)
        rt = guard(self, 0.9)
        self.play(mk[0].animate.set_fill(TERRA), VGroup(s[1], regs[1]).animate.shift(DOWN * (ROWS[1] - ROWS[2])), run_time=rt * 0.6)
        self.play(FadeOut(VGroup(s[1], regs[1])), Indicate(s[2], color=None, scale_factor=1.06), run_time=rt * 0.4)
        until(self, "dead code elimination", lead=0.2)
        rt = guard(self, 0.7)
        self.play(mk[1].animate.set_fill(TERRA), FadeOut(VGroup(s[0], regs[0]), shift=LEFT * 0.4), run_time=rt)
        until(self, "deletes what nothing uses", lead=0.1)
        rest = VGroup(VGroup(s[2], s[3], s[4], s[5]), VGroup(regs[2], regs[3]), eds, phi)
        rt = guard(self, 0.7)
        self.play(rest.animate.shift(UP * UPS), run_time=rt)
        until(self, "phi nodes become", lead=0.2)
        cps = copies().shift(UP * UPS)
        pc = [phi.copy(), phi.copy()]
        self.add(*pc)
        self.remove(phi)
        rt = guard(self, 0.8)
        self.play(Transform(pc[0], cps[0]), Transform(pc[1], cps[1]), run_time=rt)
        done(self)


# ─── B08: code generation, four chips ───
DOORS = [-2.2, -0.6, 1.0, 2.6]
DY = -0.9
DS, DW, DD, DH = 0.8, 0.6, 1.2, 2.0
IR8 = (-5.0, 0.6)
ASX = 5.0
ASR = [1.8, 1.1, 0.4, -0.3, -1.0]
APAT = [[(0.06, 0.18), (0.3, 0.44)], [(0.06, 0.18), (0.3, 0.3)], [(0.06, 0.18), (0.3, 0.5)], [(0.06, 0.18), (0.3, 0.36)], [(0.06, 0.18), (0.3, 0.26)]]


def door(x):
    i = rig_at(x, DY, DS, DW, DD)
    body = i.box(0, 0, 0, DW, DD, DH, DK_TOP, DK_L, DK_R)
    way = i.quad([(0, 0.25, 0.05), (0, 0.95, 0.05), (0, 0.95, 1.05), (0, 0.25, 1.05)], DARK_TOP, sw=0)
    lamp = Circle(radius=0.14, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(i.p(0, DD / 2, 1.55))
    return VGroup(body, way, lamp), i.p(0, DD / 2, 0.55)


def asm_strip(k, x=ASX, y=None, w=2.0, h=0.42):
    y = ASR[k] if y is None else y
    body = rrect(w, h, (x, y), PAGE_TOP, INK, 4, r=0.08)
    bars = VGroup(*[bar(x - w / 2 + (w - 0.2) * a + 0.1, y, (w - 0.2) * b, h=0.11) for a, b in APAT[k]])
    return VGroup(body, bars)


def asm():
    return VGroup(*[asm_strip(k) for k in range(5)])


def l_back():
    return lbl("back end", (-4.9, 2.6))


def l_x86():
    return lbl("x86-64", (DOORS[0], 1.95))


def l_asm():
    return lbl("assembly", (ASX, 2.6))


def b08_doors():
    ds = VGroup(*[door(x)[0] for x in DOORS])
    for d in ds:
        d[2].set_fill(BAR1)
    ds[0][2].set_fill(TERRA)
    return ds


def b08_state():
    return VGroup(b08_doors(), asm(), l_back(), l_x86(), l_asm())


class B08_Codegen(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        irg = st[0]
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(st[1], st[2], st[3], st[4])), irg.animate.scale(0.5).move_to(P3(IR8)), FadeIn(l_back()), run_time=rt)
        ds = VGroup(*[door(x)[0] for x in DOORS])
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.4) for d in ds], lag_ratio=0.2), run_time=rt)
        for k, phrase in enumerate(("x eighty-six sixty-four", "i six eighty-six", "A. Arch sixty-four", "risk five sixty-four")):
            until(self, phrase, lead=0.1)
            rt = guard(self, 0.35)
            self.play(ds[k][2].animate.set_fill(BAR1), Indicate(ds[k][0], color=None, scale_factor=1.05), run_time=rt)
        until(self, "The chosen code generator", lead=0.2)
        rt = guard(self, 0.5)
        self.play(ds[0][2].animate.set_fill(TERRA), FadeIn(l_x86()), run_time=rt)
        rt = guard(self, 0.8)
        self.play(irg.animate.scale(0.15).move_to(door(DOORS[0])[1]), run_time=rt, rate_func=ease_in)
        self.remove(irg)
        until(self, "writes assembly", lead=0.2)
        a = asm()
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.6) for s in a], lag_ratio=0.15), FadeIn(l_asm()), run_time=rt)
        done(self)


# ─── B09: the peephole pass ───
S9 = 1.5
AC9 = (0.3, 0.1)
CUT = 3


def asm9():
    return asm().scale(S9).move_to(P3(AC9))


def l_peep():
    return lbl("peephole", (-4.0, 2.2))


def l_sl():
    return lbl("store, load", (4.6, -0.42))


def b09_asm():
    a = asm9()
    a[4].shift(UP * (C(a[3])[1] - C(a[4])[1]))
    return VGroup(a[0], a[1], a[2], a[4])


def b09_state():
    return VGroup(b09_asm(), l_peep())


class B09_Peephole(Scene):
    def construct(self):
        st = b08_state()
        self.add(st)
        a = st[1]
        rt = guard(self, 0.8)
        self.play(FadeOut(VGroup(st[0], st[2], st[3], st[4])), a.animate.scale(S9).move_to(P3(AC9)), FadeIn(l_peep()), run_time=rt)
        tgt = asm9()
        top, bot = C(tgt[0])[1] + 0.5, C(tgt[4])[1] - 0.5
        until(self, "It finds wasted patterns", lead=0.4)
        scan = Line([AC9[0] - 1.8, top, 0], [AC9[0] + 1.8, top, 0], color=TERRA, stroke_width=8).set_z_index(8)
        rt = guard(self, 1.4)
        self.play(FadeIn(scan), run_time=rt * 0.14)     # pieces sum to 0.94 rt, so the fade never trips the guard's
        self.play(scan.animate.move_to([AC9[0], bot, 0]), run_time=rt * 0.66, rate_func=linear)   # own check and
        self.play(FadeOut(scan), run_time=rt * 0.14)    # leaves the line waiting on stage at the midpoint
        until(self, "storing a value", lead=0.2)
        y2, y3 = C(tgt[2])[1], C(tgt[3])[1]
        bx = AC9[0] + 1.5 + 0.35
        brk = VGroup(Line([bx, y2 + 0.4, 0], [bx, y3 - 0.4, 0], color=BAR1, stroke_width=8),
                     Line([bx - 0.25, y2 + 0.4, 0], [bx, y2 + 0.4, 0], color=BAR1, stroke_width=8),
                     Line([bx - 0.25, y3 - 0.4, 0], [bx, y3 - 0.4, 0], color=BAR1, stroke_width=8))
        sl = l_sl()
        rt = guard(self, 0.5)
        self.play(Create(brk), FadeIn(sl), run_time=rt)
        until(self, "cuts the waste", lead=0.3)
        rt = guard(self, 0.8)
        self.play(FadeOut(a[CUT], shift=RIGHT * 1.2), FadeOut(brk), FadeOut(sl), run_time=rt * 0.6)
        self.play(a[4].animate.move_to(C(tgt[3])), run_time=rt * 0.4)
        done(self)


# ─── B10: the assembler ───
AC10 = (-4.5, 0.4)
PR = rig_at(-0.6, -0.7, 0.85, 1.8, 1.6)
PRW, PRD, PRH = 1.8, 1.6, 1.5
BYX0, BYR = 2.1, [1.75, 1.1, 0.45, -0.2]
OB = rig_at(3.3, -2.1, 0.95, 1.6, 1.0)


def press():
    body = PR.box(0, 0, 0, PRW, PRD, PRH)
    mouth = PR.quad([(0, 0.35, 0.2), (0, 1.25, 0.2), (0, 1.25, 0.95), (0, 0.35, 0.95)], DARK_L, sw=0)
    slot = PR.quad([(0.35, 0, 0.2), (1.45, 0, 0.2), (1.45, 0, 0.8), (0.35, 0, 0.8)], DARK_L, sw=0)
    return VGroup(body, mouth, slot)


def press_in():
    return PR.p(0, 0.8, 0.55)


def press_out():
    return PR.p(0.9, 0, 0.5)


def bytes_():
    return VGroup(*[VGroup(*[Square(side_length=0.42, fill_color=(BAR1, BAR2)[(r + c) % 2], fill_opacity=1, stroke_width=0)
                             .move_to([BYX0 + c * 0.58, y, 0]) for c in range(4)]) for r, y in enumerate(BYR)])


PL = 0.2                                     # dark plinth height: a pale kraft block alone fails Gate V contrast


def on_plinth(iso, w, d, h):
    return VGroup(iso.box(-0.1, -0.1, 0, w + 0.2, d + 0.2, PL, DK_TOP, DK_L, DK_R), iso.box(0, 0, PL, w, d, h))


def obj_block():
    return on_plinth(OB, 1.6, 1.0, 0.7)


def l_asmb():
    return lbl("assembler", (-0.6, 2.2))


def l_obj():
    return lbl(".o file", (5.35, -2.2))


def b10_asm():
    return b09_asm().scale(1 / S9).move_to(P3(AC10))


def b10_state():
    return VGroup(press(), obj_block(), l_asmb(), l_obj())


class B10_Assemble(Scene):
    def construct(self):
        st = b09_state()
        self.add(st)
        a = st[0]
        rt = guard(self, 0.8)
        self.play(FadeOut(st[1]), a.animate.scale(1 / S9).move_to(P3(AC10)), FadeIn(press(), shift=UP * 0.4), FadeIn(l_asmb()), run_time=rt)
        until(self, "It parses each line", lead=0.3)
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[s.animate.scale(0.15).move_to(press_in()) for s in a], lag_ratio=0.25), run_time=rt, rate_func=ease_in)
        self.remove(a)
        until(self, "encodes each instruction as bytes", lead=0.3)
        by = bytes_()
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.5) for r in by], lag_ratio=0.25), run_time=rt)
        until(self, "writes an object file", lead=0.3)
        ob = obj_block()
        rt = guard(self, 0.5)
        self.play(FadeIn(ob, shift=UP * 0.3), FadeIn(l_obj()), run_time=rt)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[r.animate.scale(0.2).move_to(OB.p(0.8, 0.5, 0.7 + PL)) for r in by], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        self.remove(by)
        rt = guard(self, 0.3)
        self.play(Indicate(ob, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# ─── B11: the linker ───
OB11 = rig_at(-3.2, -0.6, 0.95, 1.6, 1.0)
RB = [rig_at(0.9, 0.95, 0.8, 1.6, 1.0), rig_at(0.9, -1.85, 0.8, 1.6, 1.0)]
EL = rig_at(0.3, -0.7, 1.0, 1.9, 1.6)
ELW, ELD, ELH = 1.9, 1.6, 1.3


def obj11():
    return on_plinth(OB11, 1.6, 1.0, 0.7)


def rblock(i):
    return on_plinth(RB[i], 1.6, 1.0, 0.7)


def cables():
    a = OB11.p(1.6, 0.5, 0.35 + PL)
    out = VGroup()
    for i in range(2):
        b = RB[i].p(0, 0.5, 0.35 + PL)
        out.add(CubicBezier(a, a + np.array([1.2, 0, 0]), b - np.array([1.2, 0, 0]), b, stroke_color=BAR1, stroke_width=6))
    return out.set_z_index(-1)


def elf_big():
    return VGroup(on_plinth(EL, ELW, ELD, ELH), EL.tape(0, 0, ELH + PL, ELW, ELD, drop=0.45))


def l_link():
    return lbl("linker", (-3.2, 1.6))


def l_libs():
    return lbl("runtime + libs", (3.9, -0.45))


def l_elf2():
    return lbl("ELF", (2.75, -0.5), size=52)


def b11_state():
    return VGroup(elf_big(), l_link(), l_elf2())


class B11_Link(Scene):
    def construct(self):
        st = b10_state()
        self.add(st)
        ob = st[1]
        rt = guard(self, 0.8)
        self.play(FadeOut(VGroup(st[0], st[2], st[3])), ob.animate.move_to(C(obj11())), FadeIn(l_link()), run_time=rt)
        until(self, "the C runtime and libraries", lead=0.3)
        rbs = [rblock(0), rblock(1)]
        rt = guard(self, 0.7)
        lb = l_libs()
        for r_ in rbs:
            r_.shift(RIGHT * 1.0)
        self.add(*rbs)
        self.play(rbs[0].animate.shift(LEFT * 1.0), rbs[1].animate.shift(LEFT * 1.0), FadeIn(lb), run_time=rt)
        until(self, "resolves every symbol", lead=0.2)
        cb = cables()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(c) for c in cb], lag_ratio=0.3), run_time=rt)
        until(self, "patches the code", lead=0.2)
        pts = [OB11.p(1.6, 0.5, 0.35 + PL) + np.array([0.12, 0.0, 0]), RB[0].p(0, 0.5, 0.35 + PL) + np.array([-0.12, 0, 0]),
               RB[1].p(0, 0.5, 0.35 + PL) + np.array([-0.12, 0, 0])]
        dots = VGroup(*[Dot(p, radius=0.1, color=TERRA).set_z_index(6) for p in pts])
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2), run_time=rt)
        until(self, "writes the finished", lead=0.3)
        allb = VGroup(ob, rbs[0], rbs[1], cb, dots)
        rt = guard(self, 0.7)
        self.play(allb.animate.scale(0.4).move_to(C(elf_big()[0])), FadeOut(lb), run_time=rt, rate_func=ease_in)
        self.remove(allb)
        eb = elf_big()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(eb[0]), run_time=rt * 0.6)
        self.play(FadeIn(eb[1]), FadeIn(l_elf2()), run_time=rt * 0.4)
        done(self)


# ─── B12: the README's warning ───
EB12 = (-3.9, -0.9)
CK = (0.2, 0.9)
DOC = (4.1, 0.2)


class B12_Warning(Scene):
    def construct(self):
        st = b11_state()
        self.add(st)
        eb = st[0]
        rt = guard(self, 0.7)
        self.play(FadeOut(VGroup(st[1], st[2])), eb.animate.move_to(P3(EB12)), run_time=rt)
        until(self, "None of it has been validated", lead=0.3)
        box = Square(side_length=1.5, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=8).move_to(P3(CK))
        rt = guard(self, 0.7)
        self.play(Create(box), FadeIn(lbl("not validated", (CK[0], -0.4))), run_time=rt)
        until(self, "The docs may be wrong", lead=0.3)
        doc = page5().scale(0.62).move_to(P3(DOC))
        rt = guard(self, 0.6)
        self.play(FadeIn(doc, shift=LEFT * 0.6), FadeIn(lbl("docs may be wrong", (DOC[0], -1.35), size=40)), run_time=rt)
        until(self, "I do not recommend", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(box, color=None, scale_factor=1.08), run_time=rt)
        until(self, "learn the stages", lead=0.2)
        rt = guard(self, 0.4)
        self.play(Indicate(doc, color=None, scale_factor=1.05), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Pipeline, B01_Preprocess, B02_Lex, B03_Parse, B04_Sema, B05_Lower, B06_SSA, B07_Optimize,
             B08_Codegen, B09_Peephole, B10_Assemble, B11_Link, B12_Warning):
    _cls.play = ST.play
