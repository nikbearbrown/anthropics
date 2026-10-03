"""
iso_kit.py — the show-tell drawing kit. PASTE this block at the top of a reel's scenes.py;
do not import it (Gate A copies only scenes.py into its sandbox).

Drawn isometric objects in the Claude palette: cardboard boxes (closed, open, taped), dark
MCP blocks with ports, flat skill pages, server stacks with lights, checks, a cursor, pills.
Pacing helpers read the reel's beat_sheet.json so scenes wait for their spoken phrase.

Every rule in ../SKILL.md "DRAWING LAWS" is already obeyed by these primitives; keep it that
way when you add one (label beside, never inside; terracotta never under text; dim greys
with gaps for chart blocks; type floor 32).
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

# Reel-specific cast. Large labels sit on the bare cream stage, never in objects.
def label(text, x=0, y=2.5, size=60):
    return T(text, size=size).move_to([x,y,0])

def tray(x=0, y=-0.7, scale=1.25):
    iso=Iso(s=scale)
    back, front=iso.open_box(-1,-1,0,2,2,0.25)
    return VGroup(back,front).move_to([x,y,0])

def page(x=0,y=0,scale=1):
    drawing=Iso(s=scale).page(0,0,0,1.1,1.4).move_to([x,y,0])
    drawing[0].set_stroke(color=DIM,width=2)
    return drawing

def block(x=0,y=0,scale=1):
    return Iso(s=scale).mcp(0,0,0).move_to([x,y,0])

def arrow(x1,y1,x2,y2):
    return Arrow([x1,y1,0],[x2,y2,0],buff=0.12,color="#9C8462",stroke_width=5,tip_length=.28,max_tip_length_to_length_ratio=0.25)

def stack(x,y,n=4,scale=1):
    return VGroup(*[page(x,y+i*0.19,scale) for i in range(n)])

def done(scene):
    bid=type(scene).__name__.split("_")[0]
    gap=_TARGET.get(bid,12)-_elapsed(scene)-0.05
    if gap>0: scene.wait(gap)

class B00_Crowded(Scene):
    def construct(self):
        base=tray(scale=1.9)
        self.add(base,label("Context",y=2.8))
        pages=VGroup(page(-1.7,0.2,0.9),page(0,0.5,0.9),page(1.7,0.2,0.9))
        for p in pages: self.play(FadeIn(p,shift=DOWN*0.8),run_time=0.7)
        until(self,"Most tasks")
        self.play(pages[0].animate.set_opacity(0.3),pages[2].animate.set_opacity(0.3),run_time=0.8)
        self.play(Create(check(0,1.7,s=.3)),run_time=.5)
        done(self)

class B01_Core(Scene):
    def construct(self):
        original=stack(-3.5,-.3,7,1.1)
        self.add(original,label("402 lines",-3.5,-2.2),label("Workshop report",0,2.6,56))
        self.play(Create(arrow(-1.5,0,1.1,0)),run_time=.6)
        core=page(3.2,-.6,1.1)
        deferred=stack(3.2,1,4,.8)
        self.play(FadeIn(core,shift=RIGHT*.5),FadeIn(label("15 + skills",3.2,-2.2)),run_time=.8)
        until(self,"did not disappear")
        self.play(FadeIn(deferred,shift=UP*.5),run_time=.8)
        done(self)

class B02_Skill(Scene):
    def construct(self):
        base=tray(1.7,-.5,1.5)
        current=page(1.1,-.4,.75)
        skill=page(-3.5,.6,1.1)
        self.add(base,current,label("Same context",1.7,-2.5),label("Skill",-3.5,2.3))
        self.play(FadeIn(skill),run_time=.7)
        until(self,"existing context")
        self.play(Create(arrow(-2,.3,-.5,.3)),skill.animate.move_to([2.5,-.2,0]),run_time=1.2)
        done(self)

class B03_Tool(Scene):
    def construct(self):
        tool=block(0,0,1.3)
        request=page(-4,0,.85)
        self.add(tool,label("Tool",0,2.5),label("Request",-4,-2.2),label("Result",4,-2.2))
        self.play(FadeIn(request),Create(arrow(-2.7,0,-1.8,0)),run_time=.7)
        self.play(request.animate.move_to([-1,0,0]).set_opacity(0),run_time=1)
        result=page(4,0,.85)
        self.play(Create(arrow(1.8,0,2.7,0)),FadeIn(result,shift=RIGHT*.7),run_time=1)
        done(self)

class B04_Worker(Scene):
    def construct(self):
        left,right=tray(-3.4,-.6,1.1),tray(3.4,-.6,1.1)
        self.add(left,right,label("Parent",-3.4,-2.5),label("Subagent",3.4,-2.5))
        task=page(-3.4,.1,.65)
        self.play(FadeIn(task),Create(arrow(-1.1,.8,1.1,.8)),run_time=.7)
        self.play(task.animate.move_to([3.4,.1,0]),run_time=1.1)
        until(self,"returns a result")
        result=page(3.4,-.7,.5)
        self.play(FadeIn(result),Create(arrow(1.1,-1.3,-1.1,-1.3)),run_time=.6)
        self.play(result.animate.move_to([-3.4,-.4,0]),run_time=1.1)
        done(self)

class B05_Policy(Scene):
    def construct(self):
        base=tray(0,-.7,1.2)
        policy=page(-4,.5,.9)
        tool=block(4,.5,.8)
        self.add(base,policy,tool,label("Policy",-4,2.4),label("Stock",4,2.4),label("Draft",0,-2.5))
        self.play(Create(arrow(-2.7,.2,-1.4,-.2)),Create(arrow(2.7,.2,1.4,-.2)),run_time=.7)
        evidence=page(3.8,.3,.55)
        self.play(FadeIn(evidence),run_time=.4)
        self.play(policy.animate.move_to([-.7,-.4,0]).scale(.7),evidence.animate.move_to([.7,-.4,0]),run_time=1.2)
        until(self,"draft a recommendation")
        draft=page(0,1,.9)
        self.play(FadeIn(draft,shift=UP*.7),run_time=.9)
        done(self)

class B06_Approval(Scene):
    def construct(self):
        draft=page(-4,-.1,1)
        action=block(4,-.1,1)
        posts=VGroup(Line([-.8,-1.4,0],[-.8,1,0],color=INK,stroke_width=7),Line([.8,-1.4,0],[.8,1,0],color=INK,stroke_width=7))
        gate=Line([-.8,.4,0],[.8,.4,0],color=TERRA,stroke_width=14)
        self.add(draft,action,posts,gate,label("Draft",-4,-2.5),label("Approve",0,2.5),label("Action",4,-2.5))
        self.play(Create(arrow(-2.7,-.3,-1.2,-.3)),run_time=.7)
        until(self,"Check the quantity")
        approval=check(0,1.6,s=.3)
        self.play(Create(approval),run_time=.7)
        self.play(Rotate(gate,angle=PI/2,about_point=[-.8,.4,0]),run_time=.8)
        self.play(Create(arrow(1.2,-.3,2.7,-.3)),draft.animate.move_to([2.5,-.3,0]).scale(.65),run_time=1.1)
        done(self)

class B07_Batch(Scene):
    def construct(self):
        small=VGroup(*[block(-4.4+(i%3)*.85,-.8+(i//3)*.6,.32) for i in range(9)])
        self.add(small,label("102 calls",-3.5,-2.2),label("3 scripts",3.5,-2.2),label("Workshop report",0,2.6,56))
        self.play(Create(arrow(-1.5,.1,1.2,.1)),run_time=.8)
        big=VGroup(block(2.2,-.2,.62),block(3.5,-.2,.62),block(4.8,-.2,.62))
        self.play(FadeIn(big,shift=RIGHT*.6),run_time=1)
        done(self)

class B08_Timing(Scene):
    def construct(self):
        self.add(label("Workshop report",0,2.8,56),label("488 s",-3,-2.4,64),label("~100 s",3,-2.4,64))
        iso=Iso(s=1)
        before=iso.box(0,0,0,1.7,1.1,2.44,DIM,BAR2,BAR3).move_to([-3,0,0])
        after=iso.box(0,0,0,1.7,1.1,.5,DIM,BAR2,BAR3)
        after.move_to([3,before.get_bottom()[1]+after.height/2,0])
        self.play(GrowFromEdge(before,DOWN),run_time=1.2)
        self.play(GrowFromEdge(after,DOWN),run_time=1)
        done(self)

class B09_Measure(Scene):
    def construct(self):
        first,second=page(-3.5,.1,.9),page(3.5,.1,.9)
        frame=tray(0,-.6,1.15)
        self.add(first,second,frame,label("Same tasks",0,2.5),label("Reject",-3.5,-2.5),label("Verify",3.5,-2.5))
        self.play(Create(arrow(-2.3,.1,-1.3,.1)),Create(arrow(2.3,.1,1.3,.1)),run_time=.8)
        until(self,"faster but wrong")
        cross=VGroup(Line([-3.85,1.35,0],[-3.15,2.05,0],color=INK,stroke_width=7),Line([-3.85,2.05,0],[-3.15,1.35,0],color=INK,stroke_width=7))
        self.play(Create(cross),Create(check(3.5,1.7,s=.3)),run_time=.8)
        self.play(first.animate.shift(DOWN*.8).set_opacity(.25),run_time=.7)
        done(self)

def guarded_play(self,*animations,**kwargs):
    """Keep the midpoint fully settled, including shape entrances and fades."""
    if not all(isinstance(a,Wait) for a in animations):
        duration=float(kwargs.get("run_time",1))
        midpoint=_TARGET.get(type(self).__name__.split("_")[0],0)/2
        now=_elapsed(self)
        if midpoint and now<midpoint+.22 and now+duration>midpoint-.22:
            available=midpoint-.24-now
            if available>=max(.3,.6*duration): kwargs["run_time"]=available
            else: Scene.wait(self,max(.02,midpoint+.24-now))
    return Scene.play(self,*animations,**kwargs)

for _scene in (B00_Crowded,B01_Core,B02_Skill,B03_Tool,B04_Worker,B05_Policy,B06_Approval,B07_Batch,B08_Timing,B09_Measure):
    _scene.play=guarded_play
