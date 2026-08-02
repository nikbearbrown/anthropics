import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.5):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=25).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_ProductInput(Scene):
 def construct(self):
  a=chip("control |0>",TEAL,3);b=chip("target |0>",CRIMSON,3);joint=chip("|00> = |0> tensor |0>",SLATE,5.2);g=VGroup(VGroup(a,b).arrange(RIGHT,buff=.7),joint).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=.9);self.wait(max(.5,D["B02"]-.9))
class B03_Hadamard(Scene):
 def construct(self):
  a=chip("|0>",TEAL,2);h=chip("H",CRIMSON,1.5);b=chip("|+>",TEAL,2);g=VGroup(a,h,b).arrange(RIGHT,buff=.7);ar=VGroup(Arrow(a.get_right(),h.get_left(),color=INK,buff=.15),Arrow(h.get_right(),b.get_left(),color=INK,buff=.15));eq=Text("|+> = (|0> + |1>)/sqrt(2)",font=MONO,color=INK,font_size=34).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),run_time=.5);self.play(*[GrowArrow(x) for x in ar],FadeIn(eq),run_time=.8);self.wait(max(.5,D["B03"]-1.3))
class B04_StillSeparable(Scene):
 def construct(self):
  top=chip("(|00> + |10>)/sqrt(2)",CRIMSON,5.2);bottom=chip("= |+> tensor |0>",TEAL,4.4);g=VGroup(top,bottom).arrange(DOWN,buff=.7);cap=Text("superposition, still separable",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.6);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B04"]-1))
class B05_CNOTBranches(Scene):
 def construct(self):
  a=VGroup(chip("|00>",TEAL,2),chip("stays |00>",SLATE,2.8)).arrange(RIGHT,buff=.6);b=VGroup(chip("|10>",CRIMSON,2),chip("becomes |11>",CRIMSON,3)).arrange(RIGHT,buff=.6);g=VGroup(a,b).arrange(DOWN,buff=.8);head=Text("CNOT: flip target when control = 1",font=DISPLAY,color=INK,font_size=40,weight=BOLD).next_to(g,UP,buff=.7);self.play(FadeIn(head),LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B05"]-1.2))
class B06_BellOutput(Scene):
 def construct(self):
  eq=Text("|Phi+> = (|00> + |11>)/sqrt(2)",font=MONO,color=CRIMSON,font_size=45);cap=Text("cannot factor into one-qubit states",font=SERIF,color=TEAL,font_size=32,slant=ITALIC).next_to(eq,DOWN,buff=.7);self.play(FadeIn(eq),FadeIn(cap),run_time=.9);self.wait(max(.5,D["B06"]-.9))
class B07_MatchedOutcomes(Scene):
 def construct(self):
  a=VGroup(chip("00",TEAL,2.2),chip("1/2",SLATE,1.6)).arrange(DOWN,buff=.35);b=VGroup(chip("11",CRIMSON,2.2),chip("1/2",SLATE,1.6)).arrange(DOWN,buff=.35);g=VGroup(a,b).arrange(RIGHT,buff=1.5);head=Text("COMPUTATIONAL-BASIS MEASUREMENT",font=DISPLAY,color=INK,font_size=38,weight=BOLD).next_to(g,UP,buff=.8);self.play(FadeIn(head),FadeIn(g),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_LocalCenters(Scene):
 def construct(self):
  circles=VGroup(Circle(radius=1.7,color=TEAL),Circle(radius=1.7,color=CRIMSON)).arrange(RIGHT,buff=2);dots=VGroup(*[Dot(c.get_center(),color=INK,radius=.14) for c in circles]);labs=VGroup(Text("qubit A",font=MONO,color=TEAL,font_size=28).next_to(circles[0],DOWN),Text("qubit B",font=MONO,color=CRIMSON,font_size=28).next_to(circles[1],DOWN));cap=Text("reduced Bloch vectors = 0 · not collapse",font=SERIF,color=INK,font_size=30,slant=ITALIC).to_edge(UP,buff=.6);self.play(Create(circles),FadeIn(dots),FadeIn(labs),FadeIn(cap),run_time=1.1);self.wait(max(.5,D["B08"]-1.1))
class B09_CorrelationHoldsInfo(Scene):
 def construct(self):
  local=title("LOCAL STATES","maximally mixed",CRIMSON);joint=title("JOINT STATE","pure and perfectly known",TEAL);link=Line(local.get_right(),joint.get_left(),color=INK,stroke_width=5);g=VGroup(local,link,joint).arrange(RIGHT,buff=.8);self.play(FadeIn(g),run_time=.9);self.wait(max(.5,D["B09"]-.9))
class B10_OrderMatters(Scene):
 def construct(self):
  good=VGroup(chip("H then CNOT",TEAL,3),chip("Bell pair",TEAL,2.5)).arrange(RIGHT,buff=.5);bad=VGroup(chip("CNOT then H",CRIMSON,3),chip("product state",SLATE,2.8)).arrange(RIGHT,buff=.5);g=VGroup(good,bad).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Two Gates Tie",font=DISPLAY,color=WHITE,font_size=53,weight=BOLD);b=Text("the Quantum Knot",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.0
  self.add(bg(),ttl('The input is zero-zero. Each qubit has'))
  stmt=Text('The input is zero-zero',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Each qubit has its own pure state, and the joint state ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('After H, the joint state is zero-zero'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('After H, the joint state is zero-zero plus one-zero ove',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('It is a superposition, but still separable: plus tensor',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Now controlled-NOT flips the target only'))
  stmt=Text('Now controlled-NOT flips the target only on the branch ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Zero-zero stays zero-zero',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('The output is phi plus: zero-zero plus'))
  stmt=Text('The output is phi plus: zero-zero plus one-one over roo',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('No product of one-qubit states can reproduce it',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Measure both in the computational basis '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Measure both in the computational basis and the outcome',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Result',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Yet each qubit alone is maximally mixed.'))
  stmt=Text('Yet each qubit alone is maximally mixed',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Its reduced Bloch vector sits at the center',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('The information did not vanish. It moved'))
  stmt=Text('The information did not vanish',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It moved into correlations: the joint state is perfectl',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Order matters. CNOT on zero-zero does no'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Order matters',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('CNOT on zero-zero does nothing',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('Two gates tie the quantum knot: H'))
  stmt=Text('Two gates tie the quantum knot: H creates branches, and',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
