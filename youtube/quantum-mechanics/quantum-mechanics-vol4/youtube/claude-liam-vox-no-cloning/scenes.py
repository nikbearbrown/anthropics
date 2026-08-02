import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}

def box(s,c=TEAL,w=2.3):
 r=Rectangle(width=w,height=.9).set_fill(GROUND,1).set_stroke(c,3);t=Text(s,font=MONO,color=c,font_size=28).move_to(r)
 if t.width>w*.85:t.scale_to_fit_width(w*.85)
 return VGroup(r,t)
def card(h,s,c=TEAL):
 a=Text(h,font=DISPLAY,color=INK,font_size=44,weight=BOLD)
 if a.width>11.6:a.scale_to_fit_width(11.6)
 b=Text(s,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if b.width>11.2:b.scale_to_fit_width(11.2)
 return VGroup(a,b).arrange(DOWN,buff=.45)

class B02_ProposedCopier(Scene):
 def construct(self):
  i=VGroup(box("|psi>"),box("|0> blank",SLATE,2.7)).arrange(DOWN,buff=.3).move_to(LEFT*4)
  m=box("U COPY",CRIMSON,2.5)
  o=VGroup(box("|psi>"),box("|psi>")).arrange(DOWN,buff=.3).move_to(RIGHT*4)
  ar=VGroup(Arrow(i.get_right(),m.get_left(),color=INK,buff=.2),Arrow(m.get_right(),o.get_left(),color=INK,buff=.2))
  self.play(FadeIn(i),FadeIn(m),Create(ar),run_time=.8);self.play(FadeIn(o),run_time=.6);self.wait(max(.5,DUR["B02"]-1.4))
class B03_TwoInputs(Scene):
 def construct(self):
  rows=VGroup()
  for q in ("psi","phi"):
   rows.add(VGroup(box(f"|{q}>|0>",SLATE,2.9),Arrow(LEFT*.1,RIGHT*1.5,color=INK),box(f"|{q}>|{q}>",TEAL,2.9)).arrange(RIGHT,buff=.4))
  rows.arrange(DOWN,buff=.75);h=card("One fixed machine","must copy both possibilities",CRIMSON).scale(.78).to_edge(UP,buff=.55)
  self.play(FadeIn(h),run_time=.4);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.25),run_time=1);self.wait(max(.5,DUR["B03"]-1.4))
class B04_OverlapDial(Scene):
 def construct(self):
  line=Line(LEFT*5,RIGHT*5,color=INK,stroke_width=3);ticks=VGroup(*[Line(UP*.15,DOWN*.15,color=INK).move_to(LEFT*5+RIGHT*i) for i in range(11)])
  z=Dot(LEFT*1.0,radius=.17,color=CRIMSON);labels=VGroup(Text("0 orthogonal",font=SERIF,color=TEAL,font_size=26),Text("0 < |z| < 1",font=MONO,color=CRIMSON,font_size=28),Text("1 identical",font=SERIF,color=TEAL,font_size=26)).arrange(RIGHT,buff=1.2).to_edge(DOWN,buff=1)
  h=Text("z = <phi|psi>",font=MONO,color=INK,font_size=42).to_edge(UP,buff=.8)
  self.play(FadeIn(h),Create(line),Create(ticks),run_time=.7);self.play(FadeIn(z),FadeIn(labels),run_time=.6);self.wait(max(.5,DUR["B04"]-1.3))
class B05_UnitaryPreserves(Scene):
 def construct(self):
  a=box("INPUT overlap",SLATE,3).move_to(LEFT*4);b=box("OUTPUT overlap",TEAL,3).move_to(RIGHT*4);eq=Text("=",font=DISPLAY,color=CRIMSON,font_size=64,weight=BOLD)
  h=card("Unitary evolution preserves inner products","similarity cannot change",TEAL).scale(.8).to_edge(UP,buff=.6)
  self.play(FadeIn(h),FadeIn(a),FadeIn(b),FadeIn(eq),run_time=.9);self.wait(max(.5,DUR["B05"]-.9))
class B06_OverlapSquares(Scene):
 def construct(self):
  z1=box("z",TEAL,1.4);times=Text("x",font=DISPLAY,color=INK,font_size=42);z2=box("z",TEAL,1.4);eq=Text("=",font=DISPLAY,color=INK,font_size=42);sq=box("z^2",CRIMSON,1.8)
  g=VGroup(z1,times,z2,eq,sq).arrange(RIGHT,buff=.45);h=card("Two copies multiply overlaps","tensor products turn z into z squared",CRIMSON).to_edge(UP,buff=.7)
  self.play(FadeIn(h),run_time=.5);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.12),run_time=1);self.wait(max(.5,DUR["B06"]-1.5))
class B07_Equation(Scene):
 def construct(self):
  e1=Text("z = z^2",font=MONO,color=INK,font_size=60);e2=Text("z(1-z) = 0",font=MONO,color=CRIMSON,font_size=60)
  self.play(FadeIn(e1),run_time=.6);self.play(ReplacementTransform(e1,e2),run_time=.8);self.wait(max(.5,DUR["B07"]-1.4))
class B08_Endpoints(Scene):
 def construct(self):
  zero=VGroup(Text("z = 0",font=MONO,color=TEAL,font_size=54),Text("orthogonal",font=SERIF,color=TEAL,font_size=28,slant=ITALIC)).arrange(DOWN,buff=.3)
  one=VGroup(Text("z = 1",font=MONO,color=TEAL,font_size=54),Text("identical ray",font=SERIF,color=TEAL,font_size=28,slant=ITALIC)).arrange(DOWN,buff=.3)
  bad=Text("0 < |z| < 1  ->  JAM",font=MONO,color=CRIMSON,font_size=38).to_edge(DOWN,buff=.8)
  g=VGroup(zero,one).arrange(RIGHT,buff=3);self.play(FadeIn(g),run_time=.7);self.play(FadeIn(bad),run_time=.6);self.wait(max(.5,DUR["B08"]-1.3))
class B09_CNOTException(Scene):
 def construct(self):
  rows=VGroup()
  for q in ("0","1"):
   rows.add(VGroup(box(f"|{q}>|0>",SLATE,2.8),box("CNOT",TEAL,1.8),box(f"|{q}>|{q}>",TEAL,2.8)).arrange(RIGHT,buff=.5))
  rows.arrange(DOWN,buff=.6);h=card("Orthogonal set: copyable","basis-specific is not universal",TEAL).to_edge(UP,buff=.55)
  self.play(FadeIn(h),run_time=.5);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.25),run_time=1);self.wait(max(.5,DUR["B09"]-1.5))
class B10_Qualifier(Scene):
 def construct(self):
  rows=VGroup(LabelChip("KNOWN STATE -> PREPARE",accent=TEAL,size=25),LabelChip("APPROXIMATE -> IMPERFECT",accent=SLATE,size=25),LabelChip("PROBABILISTIC -> MAY FAIL",accent=SLATE,size=25),LabelChip("UNIVERSAL + EXACT + DETERMINISTIC -> NO",accent=CRIMSON,size=25)).arrange(DOWN,buff=.28)
  self.play(LaggedStart(*[FadeIn(r,shift=RIGHT*.15) for r in rows],lag_ratio=.15),run_time=1.3);self.wait(max(.5,DUR["B10"]-1.3))
class B11_MeasurementTrap(Scene):
 def construct(self):
  state=box("unknown |psi>",TEAL,3).move_to(LEFT*4);meter=box("MEASURE",SLATE,2.5);out=box("guess",CRIMSON,2).move_to(RIGHT*4);ar=VGroup(Arrow(state.get_right(),meter.get_left(),color=INK,buff=.2),Arrow(meter.get_right(),out.get_left(),color=INK,buff=.2));x=Text("nonorthogonal states: no perfect ID",font=SERIF,color=CRIMSON,font_size=31,slant=ITALIC).to_edge(DOWN,buff=.8)
  self.play(FadeIn(state),FadeIn(meter),FadeIn(out),Create(ar),run_time=.9);self.play(FadeIn(x),run_time=.5);self.wait(max(.5,DUR["B11"]-1.4))
class B12_Verdict(Scene):
 def construct(self):
  a=Text("UNITARITY: z stays z",font=DISPLAY,color=TEAL,font_size=42,weight=BOLD);b=Text("COPYING: z becomes z^2",font=DISPLAY,color=CRIMSON,font_size=42,weight=BOLD);c=Text("agreement only at 0 or 1",font=SERIF,color=INK,font_size=34,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.5)
  self.play(LaggedStart(*[FadeIn(x,shift=UP*.12) for x in g],lag_ratio=.2),run_time=1.3);self.wait(max(.5,DUR["B12"]-1.3))
class B14_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Why You Can't Photocopy",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("an Unknown Quantum State",font=DISPLAY,color=WHITE,font_size=48,weight=BOLD);c=Text("Liam, in for Bear",font=SERIF,color="#D7C8FF",font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,DUR["B14"]-.7))
class B03_SDT(Scene):
 # B03 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.77
  self.add(bg(),ttl('The same fixed machine must also copy'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The same fixed machine must also copy another possible ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Universal means the hardware cannot be redesigned after',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.19
  self.add(bg(),ttl('Orthogonal states can be copied by a'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Orthogonal states can be copied by a device built for t',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Identical inputs are trivial',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.24
  self.add(bg(),ttl('That qualifier matters. If you know the'))
  stmt=Text('That qualifier matters',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If you know the state, you can prepare another',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.56
  self.add(bg(),ttl('The verdict: unitarity keeps similarity '))
  stmt=Text('The verdict: unitarity keeps similarity fixed, while co',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Those two rules agree only at the endpoints — identical',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B14_SDT(Scene):
 # B14 SDT retrofit: generic reveal with underline
 def construct(self):
  d=4.74
  self.add(bg(),ttl('Why You Can\'t Photocopy an Unknown Quant'))
  stmt=Text('Why You Can\'t Photocopy an Unknown Quantum State',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Liam, in for Bear',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
