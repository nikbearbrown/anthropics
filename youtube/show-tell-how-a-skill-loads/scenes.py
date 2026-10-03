"""
Manim scenes for show-tell-how-a-skill-loads (show-tell skill).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

One filing-cabinet cast for the whole film (sources: anthropics/skills + agentskills.io/specification):
cabinet = the installed skills, drawer = one skill, white label plate = name + description,
hanging folders = SKILL.md, scripts, references, assets; the tray = what Claude has in context.
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



# ═════════════════════════════ the film: one filing-cabinet cast ═════════════════════════════
# Cast, whole film: a kraft CABINET (the installed skills), DRAWERS (one skill each) with a white
# LABEL PLATE (name + description), hanging FOLDERS inside (SKILL.md white, scripts dark,
# references/assets kraft), a shallow TRAY (what Claude has in context), a TASK card.
SHADOW = "#BFB4A0"
CW, CD, CH, NDR, MG = 1.8, 2.0, 4.0, 4, 0.14          # cabinet depth (x), front width (y), height, drawers, margin
DH = (CH - MG * (NDR + 1)) / NDR                      # one drawer's height
YA, YB = MG, CD - MG                                   # a drawer's y span
CAB = Iso(3.7, -2.35, 0.8)                             # the cabinet, right of centre
TRAY = Iso(-3.9, -3.0, 1.0)                          # the context tray, lower left
TL, TD, TH = 4.4, 2.4, 0.32                            # tray length (x), depth (y), wall height
PDF = 1                                                # the drawer that matches (second from the top)


def dz(k):
    """Bottom z of drawer k (k = 0 is the top drawer)."""
    return CH - MG - DH - k * (DH + MG)


def lines_on(iso, x, y0, y1, zs, color=DIM, sw=5, frac=None):
    """'Text' lines on a surface in the plane x = const. y1 > y0; lines start at the larger y (screen left)."""
    out = VGroup()
    for i, z in enumerate(zs):
        f = frac[i] if frac else 1.0
        out.add(Line(iso.p(x, y1, z), iso.p(x, y1 - (y1 - y0) * f, z), color=color, stroke_width=sw))
    return out


def plate(iso, x, yc, zc, hw=0.5, hh=0.17, n=1):
    """A white label plate on a drawer front (plane x): the plate, then its n 'name/description' lines."""
    pl = iso.quad([(x, yc - hw, zc - hh), (x, yc + hw, zc - hh), (x, yc + hw, zc + hh), (x, yc - hw, zc + hh)], PAGE_TOP, sw=2.5)
    if n == 1:
        zs, fr = [zc], [0.7]
    else:
        zs = list(np.linspace(zc + hh * 0.55, zc - hh * 0.55, n)); fr = [0.55] + [0.85] * (n - 1)
    return VGroup(pl, lines_on(iso, x, yc - hw + 0.12, yc + hw - 0.12, zs, DIM, 4, fr))


def drawer_face(iso, x, z0, ya=YA, yb=YB, dh=DH, n=1, hw=0.5, hh=0.17):
    """Drawer front in the plane x: [0] face, [1] label plate (plate + lines), [2] handle."""
    face = iso.quad([(x, ya, z0), (x, yb, z0), (x, yb, z0 + dh), (x, ya, z0 + dh)], BOX_TOP, sw=3)
    yc = (ya + yb) / 2
    lab = plate(iso, x, yc, z0 + dh * 0.64, hw, hh, n)
    handle = Line(iso.p(x, yc - 0.28, z0 + dh * 0.24), iso.p(x, yc + 0.28, z0 + dh * 0.24), color=INK, stroke_width=7)
    return VGroup(face, lab, handle)


def drawer_out(iso, z0, out, xf=0.0, ya=YA, yb=YB, dh=DH, **pk):
    """A drawer pulled `out` from the face x = xf: (back, front). Put the contents between them."""
    xa = xf - out
    hw = dh * 0.72
    back = VGroup(iso.quad([(xa, ya, z0), (xf, ya, z0), (xf, yb, z0), (xa, yb, z0)], BOX_FLOOR, sw=3),
                  iso.quad([(xf, ya, z0), (xf, yb, z0), (xf, yb, z0 + hw), (xf, ya, z0 + hw)], BOX_IN1, sw=3),
                  iso.quad([(xa, yb, z0), (xf, yb, z0), (xf, yb, z0 + hw), (xa, yb, z0 + hw)], BOX_IN2, sw=3))
    front = VGroup(iso.quad([(xa, ya, z0), (xf, ya, z0), (xf, ya, z0 + hw), (xa, ya, z0 + hw)], BOX_R, sw=3),
                   drawer_face(iso, xa, z0, ya, yb, dh, **pk))
    return back, front


def slot(iso, k):
    z0 = dz(k)
    return iso.quad([(0, YA, z0), (0, YB, z0), (0, YB, z0 + DH), (0, YA, z0 + DH)], DARK_L, sw=3)


def cabinet(iso=CAB):
    """(body, faces): the kraft body and its NDR drawer fronts."""
    body = iso.box(0, 0, 0, CW, CD, CH)
    faces = VGroup(*[drawer_face(iso, 0, dz(k)) for k in range(NDR)])
    return body, faces


def cab_shadow(iso=CAB):
    sh = iso.quad([(0.2, -0.3, 0), (CW + 0.3, -0.3, 0), (CW + 0.3, CD - 0.1, 0), (0.2, CD - 0.1, 0)], SHADOW, sw=0)
    sh.set_z_index(-1)
    return sh


def folder(iso, x, z0, fill, tab, ya=YA, yb=YB, h=0.95, th=0.24):
    """A hanging folder standing in the plane x: [0] body, [1] tab (tab = (y0, y1))."""
    body = iso.quad([(x, ya + 0.08, z0 + 0.06), (x, yb - 0.08, z0 + 0.06), (x, yb - 0.08, z0 + h), (x, ya + 0.08, z0 + h)], fill, sw=3)
    t = iso.quad([(x, tab[0], z0 + h), (x, tab[1], z0 + h), (x, tab[1] - 0.06, z0 + h + th), (x, tab[0] + 0.06, z0 + h + th)], fill, sw=3)
    return VGroup(body, t)


def sheet(iso, x, z0, ya=YA, yb=YB, h=1.25):
    """SKILL.md standing in the plane x: [0] paper, [1] band (dot, name line, description line), [2] rule, [3] body lines."""
    y0, y1 = ya + 0.1, yb - 0.1
    paper = iso.quad([(x, y0, z0), (x, y1, z0), (x, y1, z0 + h), (x, y0, z0 + h)], PAGE_TOP, sw=3)
    zt = z0 + h
    dot = Dot(iso.p(x, y1 - 0.14, zt - 0.17), radius=0.05 * iso.s * 1.6, color=TERRA)
    band = VGroup(dot, lines_on(iso, x, y0 + 0.15, y1 - 0.26, [zt - 0.17], DIM, 7, [0.45]),
                  lines_on(iso, x, y0 + 0.15, y1 - 0.14, [zt - 0.34], DIM, 5, [0.95]))
    rule = lines_on(iso, x, y0 + 0.1, y1 - 0.1, [zt - 0.46], GHOST, 3)
    body = lines_on(iso, x, y0 + 0.15, y1 - 0.14, [zt - 0.62, zt - 0.76, zt - 0.9, zt - 1.04], GHOST, 5, [0.9, 0.8, 0.95, 0.6])
    return VGroup(paper, band, rule, body)


def tray():
    back, front = TRAY.open_box(0, 0, 0, TL, TD, TH)
    return VGroup(back, front)


def slip_at(i, w=0.46, d=0.32):
    """Tray-local spot for label slip i: rows of eight along the back of the tray."""
    r, c = divmod(i, 8)
    return 0.2 + c * (w + 0.05), TD - 0.18 - d - r * (d + 0.1)


def slip(iso, x, y, z=0.02, w=0.46, d=0.32):
    """A label slip lying flat: a thin white slab with one grey line."""
    s = iso.box(x, y, z, w, d, 0.04, PAGE_TOP, PAGE_L, PAGE_R, sw=2).set_stroke(DIM)
    ln = Line(iso.p(x + 0.1, y + d * 0.5, z + 0.04), iso.p(x + w - 0.1, y + d * 0.5, z + 0.04), color=DIM, stroke_width=3)
    return VGroup(s, ln)


def cross(x, y, s=0.22, color=INK, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def task_card():
    """The task: a white card with a tiny form (three field boxes) and a terracotta dot."""
    card = RoundedRectangle(width=2.3, height=1.45, corner_radius=0.12, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    fields = VGroup(*[Rectangle(width=w, height=0.2, stroke_color=DIM, stroke_width=3, fill_opacity=0).move_to([-0.95 + w / 2 + 0.35, 0.3 - i * 0.33, 0])
                      for i, w in enumerate((1.3, 1.5, 0.9))])
    dots = VGroup(*[Dot([-0.83, 0.3 - i * 0.33, 0], radius=0.045, color=DIM) for i in range(3)])
    pin = Dot([0.88, 0.45, 0], radius=0.08, color=TERRA)
    return VGroup(card, fields, dots, pin)


def pdf_contents(iso, z0, xa):
    """What sits in the pdf drawer: forms.md and reference.md (white), then scripts (dark, with a light)."""
    forms = folder(iso, xa + 0.3, z0, PAGE_TOP, (1.2, 1.7), h=0.8)
    ref = folder(iso, xa + 0.75, z0, PAGE_TOP, (0.75, 1.25), h=0.8)
    scr = folder(iso, xa + 1.2, z0, DARK_L, (0.3, 0.8), h=0.8)
    light = Dot(iso.p(xa + 1.2, 1.0, z0 + 0.55), radius=0.06, color=GHOST)
    return forms, ref, scr, light


def fly(src, dest):
    """A label plate copy flies to its slip spot and shrinks to the slip's size (no polygon morph)."""
    return src.animate.move_to(dest.get_center()).scale_to_fit_width(dest.width)


def pulled(self, iso, k, out, rt=0.9, back_in=False):
    """Slide drawer k out (or back in) with a tracker; returns the static (back, front) at the end state."""
    z0 = dz(k)
    t = ValueTracker(out if back_in else 0.02)
    dr = always_redraw(lambda: VGroup(*drawer_out(iso, z0, max(0.02, t.get_value()))).set_z_index(6))
    self.add(dr)
    self.play(t.animate.set_value(0.02 if back_in else out), run_time=rt)
    self.remove(dr)
    if back_in:
        return None
    b, f = drawer_out(iso, z0, out)
    b.set_z_index(5); f.set_z_index(7)
    self.add(b, f)
    return b, f


# BIG: the pulled drawer, lifted out and magnified to the left of the cabinet (B01, B02, start of B03)
BIG = Iso(1.22, -4.05 - DH * 0.0, 1.5)
BIG_OUT = 2.4


def big_drawer():
    return drawer_out(BIG, dz(PDF), BIG_OUT)


HERO = Iso(0.1, -2.85, 0.95)                           # B00: the cabinet, centre stage, before it steps right


def hero_state():
    body, faces = cabinet(HERO)
    return body, faces, cab_shadow(HERO), T("skills", 44).move_to([-3.2, 1.2, 0]), Line([-2.2, 1.0, 0], [-1.45, 0.72, 0], color=INK, stroke_width=3)


# ─────────────── B00 · the cabinet: one drawer per skill, a label on each ───────────────
class B00_Cabinet(Scene):
    def construct(self):
        body, faces, shadow, lab, lead = hero_state()
        plates = [f[1] for f in faces]
        for f in faces:
            f.remove(f[1])
        cab = VGroup(body, faces)
        cab.shift(UP * 6); self.add(cab)
        self.play(cab.animate.shift(DOWN * 6), run_time=1.0, rate_func=rate_functions.ease_out_bounce)
        self.play(FadeIn(shadow), run_time=0.4)
        until(self, "Each drawer is one skill")
        self.play(FadeIn(lab), Create(lead), *[Indicate(f[0], color=None, scale_factor=1.04) for f in faces], run_time=0.7)
        until(self, "on the front of every drawer")
        self.play(LaggedStart(*[GrowFromCenter(p) for p in plates], lag_ratio=0.3), run_time=1.1)
        finish(self)


def cab_start(self):
    """B01's opening: the B00 cabinet steps right to its working spot (CAB)."""
    body, faces, shadow, lab, lead = hero_state()
    self.add(shadow, body, faces, lab, lead)
    b2, f2 = cabinet(CAB)
    sh2 = cab_shadow(CAB)
    self.play(FadeOut(lab), FadeOut(lead), Transform(body, b2), Transform(faces, f2), Transform(shadow, sh2), run_time=0.8)
    return body, faces, shadow


# ─────────────── B01 · pull one drawer: SKILL.md, its label, its instructions ───────────────
class B01_Drawer(Scene):
    def construct(self):
        body, faces, shadow = cab_start(self)
        until(self, "Pull one drawer out")
        z0 = dz(PDF)
        face = faces[PDF]
        sl = slot(CAB, PDF)
        self.remove(face); faces.remove(face); self.add(sl)
        b, f = pulled(self, CAB, PDF, 1.2, 0.6)
        bb, bf = big_drawer()
        self.play(Transform(b, bb), Transform(f, bf), run_time=0.9)
        until(self, "Up front is the one file")
        xs = -BIG_OUT + 0.35
        sh = sheet(BIG, xs, z0 + 0.06)
        body_lines = sh[3]
        sh.remove(body_lines)
        sh.set_z_index(6)
        self.add(sh)
        self.play(sh.animate.shift(BIG.v(0, 0, 1.15)), run_time=0.8)
        body_lines.shift(BIG.v(0, 0, 1.15)); body_lines.set_z_index(6)
        l1 = T("SKILL.md", 42).move_to([-4.95, 2.85, 0])
        self.play(FadeIn(l1), run_time=0.4)
        until(self, "Its top holds a name")
        band = sh[1]
        l2 = T("name + description", 38).move_to([0.7, 2.45, 0])
        lead = Line([-1.35, 2.35, 0], [-2.45, 2.12, 0], color=INK, stroke_width=3)
        self.play(Indicate(band, color=None, scale_factor=1.12), FadeIn(l2), Create(lead), run_time=0.8)
        until(self, "That's the label")
        pl = f[1][1]                     # the big drawer's label plate (plate, lines)
        fly = VGroup(band[1].copy(), band[2].copy()).set_z_index(8)
        self.play(Transform(fly, pl[1].copy().set_z_index(8)), Indicate(pl[0], color=None, scale_factor=1.08), run_time=0.9)
        until(self, "Below it, the instructions")
        l3 = T("instructions", 36).move_to([-5.12, 0.9, 0])
        self.play(LaggedStart(*[Create(ln) for ln in body_lines], lag_ratio=0.25), FadeIn(l3), run_time=0.9)
        finish(self)


BIG_FOLDERS = [("scripts", -1.55, DARK_L, (1.2, 1.7)), ("references", -0.85, BOX_TOP, (0.72, 1.22)), ("assets", -0.15, BOX_IN1, (0.24, 0.74))]
BIG_LABELS = {"scripts": [-3.6, 2.7, 0], "references": [-1.55, 2.95, 0], "assets": [1.05, 2.8, 0]}
FH, FTH = 1.2, 0.3                                     # big-drawer folder height and tab height


def folder_label(name, z0):
    """(label, leader): the label sits above the drawer; the leader drops to the folder's tab."""
    n, x, _, tb = [f for f in BIG_FOLDERS if f[0] == name][0]
    lab = T(name, 40).move_to(BIG_LABELS[name])
    tip = BIG.p(x, sum(tb) / 2, z0 + FH + FTH) + UP * 0.08
    start = lab.get_bottom() + DOWN * 0.3
    return lab, Line(start, tip, color=INK, stroke_width=3)


def b01_end():
    """Everything on stage at the end of B01 (B02 starts from it)."""
    body, faces = cabinet(CAB)
    faces.remove(faces[PDF])
    z0 = dz(PDF)
    bb, bf = big_drawer(); bb.set_z_index(5); bf.set_z_index(7)
    sh = sheet(BIG, -BIG_OUT + 0.35, z0 + 0.06 + 1.15); sh.set_z_index(6)
    return VGroup(cab_shadow(CAB), body, faces, slot(CAB, PDF)), bb, bf, sh


# ─────────────── B02 · three optional folders behind SKILL.md ───────────────
class B02_Folders(Scene):
    def construct(self):
        cab, bb, bf, sh = b01_end()
        labs = VGroup(T("SKILL.md", 42).move_to([-4.95, 2.85, 0]), T("name + description", 38).move_to([0.7, 2.45, 0]),
                      Line([-1.35, 2.35, 0], [-2.45, 2.12, 0], color=INK, stroke_width=3), T("instructions", 36).move_to([-5.12, 0.9, 0]))
        self.add(cab, bb, bf, sh, labs)
        z0 = dz(PDF)
        self.play(FadeOut(labs[1:]), sh.animate.shift(BIG.v(0, 0, -1.15)), labs[0].animate.move_to([-4.95, 1.35, 0]), run_time=0.8)
        cues = ["Scripts, code", "References, documents", "And assets"]
        for i, ((name, x, fill, tab), cue) in enumerate(zip(BIG_FOLDERS, cues)):
            until(self, cue, lead=0.4)
            fo = folder(BIG, x, z0, fill, tab, h=FH, th=FTH)
            if name == "scripts":
                fo.add(Dot(BIG.p(x, 1.45, z0 + 0.9), radius=0.09, color=GHOST))
            fo.set_z_index(5.8 - 0.2 * i)
            fo.shift(UP * 4.5); self.add(fo)
            lab, lead = folder_label(name, z0)
            self.play(fo.animate.shift(DOWN * 4.5), run_time=0.5, rate_func=ease_in)
            self.add(lab)                               # labels land whole (GATE T reads a half-faded label as low contrast)
            self.play(Create(lead), run_time=0.3)
        finish(self)


def b02_end():
    cab, bb, bf, sh = b01_end()
    z0 = dz(PDF)
    sh.shift(BIG.v(0, 0, -1.15))
    fos, labs = VGroup(), VGroup()
    for i, (name, x, fill, tab) in enumerate(BIG_FOLDERS):
        fo = folder(BIG, x, z0, fill, tab, h=FH, th=FTH)
        if name == "scripts":
            fo.add(Dot(BIG.p(x, 1.45, z0 + 0.9), radius=0.09, color=GHOST))
        fo.set_z_index(5.8 - 0.2 * i)
        fos.add(fo)
        labs.add(*folder_label(name, z0))
    labs.add(T("SKILL.md", 42).move_to([-4.95, 1.35, 0]))
    return cab, bb, bf, sh, fos, labs


def tray_slips(n0, n1, iso=TRAY):
    out = VGroup()
    for i in range(n0, n1):
        x, y = slip_at(i)
        out.add(slip(iso, x, y, 0.02))
    return out


def ctx_label():
    return T("context", 40).move_to([0.2, -1.75, 0])


# ─────────────── B03 · at the start, only the labels are read ───────────────
class B03_Labels(Scene):
    def construct(self):
        cab, bb, bf, sh, fos, labs = b02_end()
        self.add(cab, bb, bf, sh, fos, labs)
        z0 = dz(PDF)
        # the drawer goes home: shrink back to the cabinet, slide in, the face returns
        sb, sf = drawer_out(CAB, z0, 1.2)
        self.play(FadeOut(labs), FadeOut(VGroup(sh, fos), shift=DOWN * 0.3), run_time=0.4)
        self.play(Transform(bb, sb), Transform(bf, sf), run_time=0.7)
        self.remove(bb, bf)
        pulled(self, CAB, PDF, 1.2, 0.5, back_in=True)
        face = drawer_face(CAB, 0, z0)
        self.remove(cab[3]); self.add(face)
        faces = VGroup(*[drawer_face(CAB, 0, dz(k)) for k in range(NDR)])
        until(self, "doesn't open the cabinet")
        tr = tray(); tr.shift(LEFT * 6); self.add(tr)
        self.play(tr.animate.shift(RIGHT * 6), run_time=0.7)
        until(self, "It reads only the labels", lead=0.5)
        self.play(*[Indicate(f[1], color=None, scale_factor=1.12) for f in faces], run_time=0.5)
        until(self, "every skill's name")
        scan = Line(CAB.p(-0.05, -0.15, CH), CAB.p(-0.05, CD + 0.15, CH), color=TERRA, stroke_width=8).set_z_index(9)
        self.play(Create(scan), run_time=0.25)
        slips = tray_slips(0, NDR)
        srcs = [faces[k][1].copy().set_z_index(8) for k in range(NDR)]
        self.add(*srcs)
        self.play(scan.animate.shift(CAB.v(0, 0, -CH + 0.1)), LaggedStart(*[fly(sc, sl) for sc, sl in zip(srcs, slips)], lag_ratio=0.22), run_time=1.5)
        self.remove(*srcs); self.add(slips)
        self.play(FadeOut(scan), run_time=0.2)
        until(self, "always in context")
        self.play(FadeIn(ctx_label()), Indicate(slips, color=None, scale_factor=1.06), run_time=0.7)
        finish(self)


def slip_center(i):
    x, y = slip_at(i)
    return TRAY.p(x + 0.23, y + 0.16, 0.06)


TASK_AT = np.array([-3.7, 2.3, 0])
PAGE_SKILL = (0.3, 0.18, 1.25, 1.0)                    # tray-local x, y, w, d of the SKILL.md page
PAGE_FORMS = (1.85, 0.18, 1.1, 1.0)
OUT_SLIP = (3.35, 0.4)


def b03_end():
    body, faces = cabinet(CAB)
    return VGroup(cab_shadow(CAB), body, faces), tray(), tray_slips(0, NDR), ctx_label()


def task_state():
    card = task_card().move_to(TASK_AT)
    lab = T("task", 40).move_to(TASK_AT + np.array([2.05, 0.35, 0]))
    return card, lab


# ─────────────── B04 · a task arrives; one label matches; one drawer opens ───────────────
class B04_Match(Scene):
    def construct(self):
        cab, tr, slips, ctx = b03_end()
        self.add(cab, tr, slips, ctx)
        card, lab = task_state()
        card.shift(LEFT * 5); self.add(card)
        self.play(card.animate.shift(RIGHT * 5), run_time=0.7)
        self.play(FadeIn(lab), run_time=0.3)
        until(self, "Claude checks it against")
        src = card.get_bottom() + DOWN * 0.08
        tries = [DashedLine(src, slip_center(i) + UP * 0.12, color=INK, stroke_width=4, dash_length=0.12) for i in range(NDR)]
        self.play(LaggedStart(*[Create(t) for t in tries], lag_ratio=0.3), run_time=1.2)
        until(self, "The PDF skill matches")
        for i, t in enumerate(tries):
            if i != PDF:
                self.remove(t)
        c = slip_center(PDF)
        ck = check(c[0] + 0.35, c[1] + 0.55, 0.18, TERRA, 7)
        self.play(Create(ck), Indicate(slips[PDF], color=None, scale_factor=1.3), run_time=0.5)
        until(self, "only that drawer slides open")
        face = cab[2][PDF]
        self.remove(face); cab[2].remove(face); self.add(slot(CAB, PDF))
        b, f = pulled(self, CAB, PDF, 1.2, 0.7)
        self.play(FadeIn(T("pdf", 40).move_to([0.75, 0.2, 0])), run_time=0.3)
        until(self, "its instructions load")
        z0 = dz(PDF)
        sm = sheet(CAB, -1.2 + 0.25, z0 + 0.06, h=0.9)
        sm.set_z_index(6); self.add(sm)
        self.play(sm.animate.shift(CAB.v(0, 0, 0.9)), run_time=0.4)
        x, y, w, d = PAGE_SKILL
        pg = TRAY.page(x, y, 0.02, w, d).set_z_index(3)
        self.play(Transform(sm, pg), run_time=0.8)
        finish(self)


def b04_end():
    cab, tr, slips, ctx = b03_end()
    face = cab[2][PDF]; cab[2].remove(face)
    cab.add(slot(CAB, PDF))
    b, f = drawer_out(CAB, dz(PDF), 1.2); b.set_z_index(5); f.set_z_index(7)
    card, lab = task_state()
    c = slip_center(PDF)
    line = DashedLine(card.get_bottom() + DOWN * 0.08, c + UP * 0.12, color=INK, stroke_width=4, dash_length=0.12)
    ck = check(c[0] + 0.35, c[1] + 0.55, 0.18, TERRA, 7)
    x, y, w, d = PAGE_SKILL
    pg = TRAY.page(x, y, 0.02, w, d).set_z_index(3)
    return cab, tr, slips, ctx, b, f, card, lab, line, ck, pg, T("pdf", 40).move_to([0.75, 0.2, 0])


# ─────────────── B05 · folders come out only when needed; scripts run in place ───────────────
class B05_OnDemand(Scene):
    def construct(self):
        cab, tr, slips, ctx, b, f, card, lab, line, ck, pg, pdf = b04_end()
        self.add(cab, tr, slips, ctx, b, f, card, lab, line, ck, pg, pdf)
        self.play(FadeOut(line), FadeOut(ck), run_time=0.3)
        z0 = dz(PDF)
        forms, ref, scr, light = pdf_contents(CAB, z0, -1.2)
        for i, m in enumerate((forms, ref, scr)):
            m.set_z_index(6.4 - 0.2 * i)
        light.set_z_index(6.3)
        until(self, "point to more files")
        grp = VGroup(forms, ref, scr, light)
        grp.shift(CAB.v(0, 0, -0.5))
        self.add(grp)
        self.play(grp.animate.shift(CAB.v(0, 0, 0.5)), run_time=0.6)
        ptr = DashedLine(TRAY.p(PAGE_SKILL[0] + PAGE_SKILL[2], PAGE_SKILL[1] + 0.8, 0.1), forms[1].get_top() + LEFT * 0.1,
                         color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(ptr), run_time=0.7)
        until(self, "Filling a form")
        self.play(FadeOut(ptr), forms.animate.shift(CAB.v(0, 0, 1.0)), run_time=0.5)
        l1 = T("forms.md", 40).move_to([1.15, 1.85, 0])
        self.play(FadeIn(l1), run_time=0.3)
        until(self, "Read the forms guide")
        x, y, w, d = PAGE_FORMS
        fp = TRAY.page(x, y, 0.02, w, d).set_z_index(3)
        self.play(Transform(forms, fp), l1.animate.move_to([-0.9, -2.6, 0]), run_time=0.9)
        until(self, "A script can even run")
        l2 = T("script", 40).move_to([0.75, 1.55, 0])
        lead = Line([1.3, 1.3, 0], light.get_center() + np.array([-0.2, 0.12, 0]), color=INK, stroke_width=3).set_z_index(9)
        ring = Circle(radius=0.22, stroke_color=TERRA, stroke_width=5).move_to(light.get_center()).set_z_index(9)
        self.play(light.animate.set_color(TERRA), FadeIn(l2), Create(lead), run_time=0.4)
        self.play(Create(ring), run_time=0.4)
        self.play(ring.animate.scale(1.8).set_stroke(opacity=0), run_time=0.5)
        until(self, "Only its output comes back")
        ox, oy = OUT_SLIP
        out = slip(CAB, -1.2 + 1.0, 0.6, z0 + 0.9, 0.5, 0.35).set_z_index(8)
        self.add(out)
        dest = slip(TRAY, ox, oy, 0.02, 0.62, 0.42).set_z_index(3)
        self.play(Transform(out, dest), run_time=0.8)
        oc = dest.get_top()
        self.play(Create(check(oc[0] + 0.1, oc[1] + 0.35, 0.16, TERRA, 7)), run_time=0.3)
        finish(self)


CAB2 = Iso(4.4, -2.6, 0.5)                             # B06: the first cabinet, smaller, front of a row
TRAY2 = Iso(-3.6, -3.0, 0.72)
STEP = CD + 0.4                                        # row spacing along y (each new cabinet sits up-left)


def world(ci, ti):
    """The B05 end state without labels, drawn with cabinet iso ci and tray iso ti."""
    z0 = dz(PDF)
    body, faces = cabinet(ci)
    faces.remove(faces[PDF])
    b, f = drawer_out(ci, z0, 1.2); b.set_z_index(5); f.set_z_index(7)
    forms, ref, scr, light = pdf_contents(ci, z0, -1.2)
    ref.set_z_index(6.2); scr.set_z_index(6.0); light.set_z_index(6.3); light.set_color(TERRA)
    x, y, w, d = PAGE_SKILL
    pg = ti.page(x, y, 0.02, w, d).set_z_index(3)
    x, y, w, d = PAGE_FORMS
    fp = ti.page(x, y, 0.02, w, d).set_z_index(3)
    ox, oy = OUT_SLIP
    osl = slip(ti, ox, oy, 0.02, 0.62, 0.42).set_z_index(3)
    oc = osl.get_top()
    ock = check(oc[0] + 0.1 * ti.s, oc[1] + 0.35 * ti.s, 0.16 * ti.s, TERRA, 7)
    back, front = ti.open_box(0, 0, 0, TL, TD, TH)
    slips = VGroup()
    for i in range(NDR):
        sx, sy = slip_at(i)
        slips.add(slip(ti, sx, sy, 0.02))
    return VGroup(cab_shadow(ci), body, faces, slot(ci, PDF), b, f, ref, scr, light,
                  VGroup(back, front), slips, pg, fp, osl, ock)


# ─────────────── B06 · every other drawer stays shut: many skills, little cost ───────────────
class B06_Wall(Scene):
    def construct(self):
        W = world(CAB, TRAY)
        card, tlab = task_state()
        labs = VGroup(card, tlab, ctx_label(), T("pdf", 40).move_to([0.75, 0.2, 0]), T("forms.md", 40).move_to([-0.9, -2.6, 0]),
                      T("script", 40).move_to([0.75, 1.55, 0]),
                      Line([1.3, 1.3, 0], W[8].get_center() + np.array([-0.2, 0.12, 0]), color=INK, stroke_width=3))
        self.add(W, labs)
        until(self, "Every other drawer stays shut", lead=0.1)
        self.play(FadeOut(labs), *[Indicate(fc, color=None, scale_factor=1.05) for fc in W[2]], run_time=0.7)
        W2 = world(CAB2, TRAY2)
        self.play(Transform(W, W2), run_time=1.0)
        until(self, "So you can install many skills")
        news = []
        for j in (1, 2, 3):
            ci = Iso(CAB2.ox - STEP * j * C30 * CAB2.s, CAB2.oy + STEP * j * 0.5 * CAB2.s, CAB2.s)
            body, faces = cabinet(ci)
            g = VGroup(cab_shadow(ci), body, faces)
            g.set_z_index(-2 * j)
            g[0].set_z_index(-2 * j - 1)
            news.append((g, faces))
        for g, _ in news:
            g.shift(UP * 5); self.add(g)
        self.play(LaggedStart(*[g.animate.shift(DOWN * 5) for g, _ in news], lag_ratio=0.3), run_time=1.3)
        srcs, dests = [], []
        for j, (g, faces) in enumerate(news):
            for k in range(NDR):
                sx, sy = slip_at(NDR * (j + 1) + k)
                srcs.append(faces[k][1].copy().set_z_index(8))
                dests.append(slip(TRAY2, sx, sy, 0.02).set_z_index(4))
        self.add(*srcs)
        self.play(LaggedStart(*[fly(a, b) for a, b in zip(srcs, dests)], lag_ratio=0.06), run_time=1.2)
        self.remove(*srcs); self.add(*dests)
        until(self, "until a task needs it")
        self.play(Indicate(VGroup(W[10], *dests), color=None, scale_factor=1.06), run_time=0.6)
        until(self, "That's progressive disclosure")
        head = T("progressive disclosure", 44).move_to([-3.1, 2.55, 0])
        self.play(FadeIn(head), Indicate(W[11], color=None, scale_factor=1.1), run_time=0.7)
        finish(self)


# ─────────────── B07 · the description decides: vague vs specific ───────────────
UA = Iso(-2.2, -1.6, 1.2)
UB = Iso(3.3, -1.6, 1.2)
UH, UZ, UDH = 1.4, 0.15, 1.1                           # unit height, drawer bottom, drawer height
PK_A = dict(n=1, hw=0.72, hh=0.36)
PK_B = dict(n=3, hw=0.72, hh=0.36)


def unit(iso, pk):
    body = iso.box(0, 0, 0, CW, CD, UH)
    face = drawer_face(iso, 0, UZ, YA, YB, UDH, **pk)
    sh = iso.quad([(0.2, -0.3, 0), (CW + 0.3, -0.3, 0), (CW + 0.3, CD - 0.1, 0), (0.2, CD - 0.1, 0)], SHADOW, sw=0).set_z_index(-1)
    return VGroup(sh, body, face)


class B07_GoodLabel(Scene):
    def construct(self):
        A, B = unit(UA, PK_A), unit(UB, PK_B)
        self.play(FadeIn(A, shift=UP * 0.3), FadeIn(B, shift=UP * 0.3), run_time=0.6)
        card = task_card().move_to([0.45, 2.35, 0])
        card.shift(UP * 3); self.add(card)
        self.play(card.animate.shift(DOWN * 3), run_time=0.6)
        until(self, "It's the label that decides")
        self.play(Indicate(A[2][1], color=None, scale_factor=1.12), Indicate(B[2][1], color=None, scale_factor=1.12), run_time=0.8)
        src = card.get_bottom() + DOWN * 0.08
        pa = A[2][1][0].get_center(); pb = B[2][1][0].get_center()
        until(self, "The spec's own bad example")
        la = DashedLine(src + LEFT * 0.4, pa + np.array([0.45, 0.45, 0]), color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(la), FadeIn(T("vague", 40).move_to([-2.4, -2.45, 0])), run_time=0.8)
        self.play(Create(cross(pa[0] + 0.95, pa[1] + 0.75, 0.2, INK, 8)), run_time=0.4)
        until(self, "Say what the skill does")
        lb = DashedLine(src + RIGHT * 0.4, pb + np.array([-0.35, 0.5, 0]), color=INK, stroke_width=4, dash_length=0.12)
        self.play(Create(lb), FadeIn(T("specific", 40).move_to([4.6, -2.45, 0])), run_time=0.8)
        self.play(Create(check(pb[0] + 0.55, pb[1] + 0.85, 0.2, TERRA, 8)), run_time=0.4)
        until(self, "in the words people actually type")
        face = B[2]
        B.remove(face); self.remove(face)
        slotB = UB.quad([(0, YA, UZ), (0, YB, UZ), (0, YB, UZ + UDH), (0, YA, UZ + UDH)], DARK_L, sw=3)
        self.add(slotB)
        t = ValueTracker(0.02)
        dr = always_redraw(lambda: VGroup(*drawer_out(UB, UZ, max(0.02, t.get_value()), dh=UDH, **PK_B)).set_z_index(6))
        self.add(dr)
        self.play(t.animate.set_value(1.0), run_time=0.8)
        self.remove(dr)
        bb, bf = drawer_out(UB, UZ, 1.0, dh=UDH, **PK_B)
        bb.set_z_index(5); bf.set_z_index(7)
        self.add(bb, bf)
        until(self, "make it a little pushy")
        pl = bf[1][1]
        xa = -1.0
        more = plate(UB, xa, (YA + YB) / 2, UZ + UDH * 0.64, n=4, hw=0.72, hh=0.36)
        self.play(Transform(pl[1], more[1]), Indicate(pl[0], color=None, scale_factor=1.08), run_time=0.8)
        finish(self)
