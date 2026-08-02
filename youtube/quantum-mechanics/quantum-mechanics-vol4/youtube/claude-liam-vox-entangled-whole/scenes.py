import sys, json, pathlib
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)

BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}

def box(label, accent=TEAL, w=2.1):
    r = Rectangle(width=w, height=0.9).set_fill(GROUND, 1).set_stroke(accent, 3)
    t = Text(label, font=MONO, color=accent, font_size=29).move_to(r)
    return VGroup(r, t)

def title(text, sub=None, accent=TEAL):
    h = Text(text, font=DISPLAY, color=INK, font_size=44, weight=BOLD)
    if h.width > 11.5: h.scale_to_fit_width(11.5)
    if not sub: return h
    s = Text(sub, font=SERIF, color=accent, font_size=28, slant=ITALIC)
    if s.width > 11.2: s.scale_to_fit_width(11.2)
    return VGroup(h, s).arrange(DOWN, buff=0.45)

def bloch(center=ORIGIN, radius=1.55, dot_center=False):
    c = Circle(radius=radius).set_stroke(SLATE, 2.5).move_to(center)
    top = Text("|0>", font=MONO, color=INK, font_size=20).next_to(c, UP, buff=0.12)
    bot = Text("|1>", font=MONO, color=INK, font_size=20).next_to(c, DOWN, buff=0.12)
    parts = [c, top, bot]
    if dot_center: parts.append(Dot(center, radius=0.15, color=CRIMSON))
    return VGroup(*parts)

class B02_BellState(Scene):
    def construct(self):
        a, b = box("A", TEAL), box("B", TEAL)
        pair = VGroup(a, b).arrange(RIGHT, buff=4.0).move_to(DOWN * 0.2)
        wave = VMobject(color=TEAL, stroke_width=4)
        pts = [[x, 0.2*np.sin(4*x), 0] for x in np.linspace(-2,2,60)]
        wave.set_points_smoothly(pts)
        eq = Text("|Phi+> = (|00> + |11>)/sqrt(2)", font=MONO, color=INK, font_size=34).to_edge(UP, buff=0.75)
        note = Text("one coherent joint state", font=SERIF, color=TEAL, font_size=28, slant=ITALIC).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(eq), FadeIn(pair), run_time=0.8); self.play(Create(wave), FadeIn(note), run_time=0.8)
        self.wait(max(.5, DUR["B02"]-1.6))

class B03_GlobalPurity(Scene):
    def construct(self):
        proj = box("rho_AB = |Phi+><Phi+|", TEAL, 6.4).move_to(UP*0.7)
        one = Text("Tr(rho_AB^2) = 1", font=MONO, color=TEAL, font_size=44).move_to(DOWN*0.6)
        chip = LabelChip("PURE WHOLE", accent=TEAL, size=28).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(proj), run_time=.6); self.play(FadeIn(one), FadeIn(chip), run_time=.7)
        self.wait(max(.5,DUR["B03"]-1.3))

class B04_HideBob(Scene):
    def construct(self):
        alice = box("Alice: ?", TEAL).move_to(LEFT*3.7)
        bob = box("Bob", SLATE).move_to(RIGHT*3.7)
        cover = Rectangle(width=3.0,height=2.0).set_fill(INK,.92).set_stroke(INK,0).move_to(bob)
        lock = Text("LOCKED",font=DISPLAY,color=WHITE,font_size=28,weight=BOLD).move_to(cover)
        q = title("What predicts every Alice-only measurement?", accent=CRIMSON).scale(.78).to_edge(UP,buff=.7)
        self.play(FadeIn(alice),FadeIn(bob),FadeIn(q),run_time=.8); self.play(FadeIn(cover),FadeIn(lock),run_time=.6)
        self.wait(max(.5,DUR["B04"]-1.4))

class B05_PartialTrace(Scene):
    def construct(self):
        joint=box("rho_AB",TEAL).move_to(LEFT*4)
        trace=LabelChip("Tr_B",accent=CRIMSON,size=30).move_to(ORIGIN)
        local=box("rho_A",TEAL).move_to(RIGHT*4)
        arrows=VGroup(Arrow(joint.get_right(),trace.get_left(),color=INK,buff=.15),Arrow(trace.get_right(),local.get_left(),color=INK,buff=.15))
        terms=Text("cross terms -> 0    diagonal terms remain",font=MONO,color=SLATE,font_size=28).to_edge(DOWN,buff=.85)
        note=Text("bookkeeping, not measurement",font=SERIF,color=CRIMSON,font_size=27,slant=ITALIC).to_edge(UP,buff=.8)
        self.play(FadeIn(joint),FadeIn(trace),FadeIn(local),Create(arrows),run_time=1); self.play(FadeIn(terms),FadeIn(note),run_time=.7)
        self.wait(max(.5,DUR["B05"]-1.7))

class B06_LocalCenter(Scene):
    def construct(self):
        ball=bloch(LEFT*2.5,2.0,True)
        eq=Text("rho_A = I/2",font=MONO,color=INK,font_size=42).move_to(RIGHT*3+UP*.7)
        purity=Text("Tr(rho_A^2) = 1/2",font=MONO,color=CRIMSON,font_size=34).move_to(RIGHT*3+DOWN*.4)
        self.play(Create(ball),run_time=.8); self.play(FadeIn(eq),FadeIn(purity),run_time=.7)
        self.wait(max(.5,DUR["B06"]-1.5))

class B07_AllAxesRandom(Scene):
    def construct(self):
        ball=bloch(ORIGIN,2.1,True)
        axes=VGroup(Line(LEFT*2,RIGHT*2,color=TEAL),Line(DOWN*2,UP*2,color=SLATE),Line(DL*1.4,UR*1.4,color=CRIMSON))
        labels=VGroup(*[LabelChip(x,accent=SLATE,size=23) for x in ("x: 50/50","y: 50/50","z: 50/50")]).arrange(DOWN,buff=.25).move_to(RIGHT*4.6)
        self.play(Create(ball),run_time=.6); self.play(LaggedStart(*[Create(a) for a in axes],lag_ratio=.2),LaggedStart(*[FadeIn(x) for x in labels],lag_ratio=.2),run_time=1.2)
        self.wait(max(.5,DUR["B07"]-1.8))

class B08_CorrelationReturns(Scene):
    def construct(self):
        rows=VGroup()
        for a,b in [("0","0"),("1","1")]:
            rows.add(VGroup(box(a,TEAL,1.1),Text("matches",font=SERIF,color=TEAL,font_size=25,slant=ITALIC),box(b,TEAL,1.1)).arrange(RIGHT,buff=.55))
        rows.arrange(DOWN,buff=.65)
        head=title("Bring Bob's records back", "the structure reappears", TEAL).to_edge(UP,buff=.55)
        self.play(FadeIn(head),run_time=.5);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.25),run_time=1)
        self.wait(max(.5,DUR["B08"]-1.5))

class B09_AxisCorrelations(Scene):
    def construct(self):
        rows=VGroup()
        for axis,rel,color in [("z","same",TEAL),("x","same",TEAL),("y","opposite",CRIMSON)]:
            left=LabelChip(axis,accent=SLATE,size=27); right=LabelChip(rel,accent=color,size=27)
            rows.add(VGroup(left,Arrow(LEFT*.2,RIGHT*1.7,color=color,buff=.1),right).arrange(RIGHT,buff=.45))
        rows.arrange(DOWN,buff=.45)
        head=title("Local randomness is universal", "joint signs depend on state and basis", CRIMSON).to_edge(UP,buff=.55)
        self.play(FadeIn(head),run_time=.5);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.18),run_time=1.1)
        self.wait(max(.5,DUR["B09"]-1.6))

class B10_ProductComparison(Scene):
    def construct(self):
        left=VGroup(title("Bell state","Alice: mixed",CRIMSON).scale(.72),bloch(ORIGIN,1.45,True)).arrange(DOWN,buff=.5)
        arrow=Arrow(ORIGIN,UP*1.35,color=TEAL,stroke_width=4,buff=0,tip_length=.2)
        b=bloch(ORIGIN,1.45,False);b.add(arrow)
        right=VGroup(title("Product |00>","Alice: pure",TEAL).scale(.72),b).arrange(DOWN,buff=.5)
        pair=VGroup(left,right).arrange(RIGHT,buff=2.0)
        self.play(FadeIn(pair),run_time=1);self.wait(max(.5,DUR["B10"]-1))

class B11_InformationBetween(Scene):
    def construct(self):
        a=box("A: no arrow",SLATE,2.6).move_to(LEFT*4)
        b=box("B: no arrow",SLATE,2.6).move_to(RIGHT*4)
        bridge=Line(a.get_right(),b.get_left(),color=TEAL,stroke_width=8)
        words=Text("COMPLETE DESCRIPTION",font=DISPLAY,color=TEAL,font_size=30,weight=BOLD).move_to(UP*.7)
        sub=Text("lives in correlations",font=SERIF,color=TEAL,font_size=31,slant=ITALIC).move_to(DOWN*.7)
        self.play(FadeIn(a),FadeIn(b),run_time=.6);self.play(Create(bridge),FadeIn(words),FadeIn(sub),run_time=.8)
        self.wait(max(.5,DUR["B11"]-1.4))

class B12_NotMeasurement(Scene):
    def construct(self):
        card=title("Partial trace ≠ measurement","Bob is omitted from the prediction, not destroyed",CRIMSON)
        check=Text("all Alice-only observables predicted correctly",font=SERIF,color=TEAL,font_size=30,slant=ITALIC).next_to(card,DOWN,buff=.8)
        self.play(FadeIn(card),run_time=.6);self.play(FadeIn(check),run_time=.6);self.wait(max(.5,DUR["B12"]-1.2))

class B13_Verdict(Scene):
    def construct(self):
        lines=VGroup(
            Text("WHOLE: pure",font=DISPLAY,color=TEAL,font_size=42,weight=BOLD),
            Text("PARTS: maximally mixed",font=DISPLAY,color=CRIMSON,font_size=42,weight=BOLD),
            Text("INFORMATION: between them",font=DISPLAY,color=INK,font_size=42,weight=BOLD),
        ).arrange(DOWN,buff=.5,aligned_edge=LEFT)
        self.play(LaggedStart(*[FadeIn(x,shift=UP*.15) for x in lines],lag_ratio=.2),run_time=1.4)
        self.wait(max(.5,DUR["B13"]-1.4))

class B15_TitleOutro(Scene):
    def construct(self):
        bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0)
        a=Text("A Whole That's Certain",font=DISPLAY,color=WHITE,font_size=48,weight=BOLD)
        b=Text("Made of Parts That Are Pure Noise",font=DISPLAY,color=WHITE,font_size=43,weight=BOLD)
        c=Text("Liam, in for Bear",font=SERIF,color="#D7C8FF",font_size=27,slant=ITALIC)
        g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,DUR["B15"]-.7))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.72
  self.add(bg(),ttl('Do not overstate that as same answer'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Do not overstate that as same answer on every axis',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('For phi plus, correlations depend on the chosen axes: s',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.39
  self.add(bg(),ttl('Compare a product state, zero-zero. The '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Compare a product state, zero-zero',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The whole is pure and Alice is also pure: her arrow poi',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B13_SDT(Scene):
 # B13 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.39
  self.add(bg(),ttl('The verdict: the Bell pair is perfectly'))
  stmt=Text('The verdict: the Bell pair is perfectly definite global',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The apparent paradox disappears once you stop demanding',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B15_SDT(Scene):
 # B15 SDT retrofit: generic reveal with underline
 def construct(self):
  d=4.76
  self.add(bg(),ttl('A Whole That\'s Certain, Made of Parts'))
  stmt=Text('A Whole That\'s Certain, Made of Parts That Are Pure Noi',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Liam, in for Bear',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
