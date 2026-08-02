import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def head(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
def chip(t,c=SLATE,w=2.2):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=26).move_to(r)
 if x.width>w*.85:x.scale_to_fit_width(w*.85)
 return VGroup(r,x)
def qubits(vals,colors=None):
 colors=colors or [TEAL]*3
 return VGroup(*[chip(v,c,1.5) for v,c in zip(vals,colors)]).arrange(RIGHT,buff=.45)
class B02_Encode(Scene):
 def construct(self):
  src=chip("α|0>+β|1>",CRIMSON,3.4).move_to(LEFT*3.7);dst=chip("α|000> + β|111>",TEAL,5).move_to(RIGHT*3.2);arr=Arrow(src.get_right(),dst.get_left(),color=INK,buff=.25);self.play(FadeIn(src),run_time=.4);self.play(GrowArrow(arr),FadeIn(dst),run_time=.9);self.wait(max(.5,D["B02"]-1.3))
class B03_Scope(Scene):
 def construct(self):
  yes=head("PROTECTS","one physical X bit flip",TEAL);no=head("DOES NOT YET PROTECT","phase errors or arbitrary noise",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=.9);self.wait(max(.5,D["B03"]-.9))
class B04_MiddleFlip(Scene):
 def construct(self):
  a=qubits(["q1","q2","q3"]);x=Text("X",font=DISPLAY,color=CRIMSON,font_size=60,weight=BOLD).next_to(a[1],UP,buff=.5);eq=Text("α|010> + β|101>",font=MONO,color=INK,font_size=45).next_to(a,DOWN,buff=.8);self.play(FadeIn(a),run_time=.4);self.play(FadeIn(x),a[1][0].animate.set_stroke(CRIMSON,5),run_time=.7);self.play(FadeIn(eq),run_time=.5);self.wait(max(.5,D["B04"]-1.6))
class B05_TwoChecks(Scene):
 def construct(self):
  q=qubits(["q1","q2","q3"]);c1=Brace(VGroup(q[0],q[1]),DOWN,color=TEAL);c2=Brace(VGroup(q[1],q[2]),UP,color=CRIMSON);l1=Text("q1 = q2 ?",font=MONO,color=TEAL,font_size=28).next_to(c1,DOWN);l2=Text("q2 = q3 ?",font=MONO,color=CRIMSON,font_size=28).next_to(c2,UP);self.play(FadeIn(q),GrowFromCenter(c1),GrowFromCenter(c2),FadeIn(l1),FadeIn(l2),run_time=1.1);self.wait(max(.5,D["B05"]-1.1))
class B06_FirstSyndromes(Scene):
 def construct(self):
  rows=VGroup(VGroup(chip("no error",SLATE,3),chip("00",TEAL,1.7)).arrange(RIGHT,buff=.7),VGroup(chip("flip q1",SLATE,3),chip("10",CRIMSON,1.7)).arrange(RIGHT,buff=.7)).arrange(DOWN,buff=.6);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.25),run_time=1.1);self.wait(max(.5,D["B06"]-1.1))
class B07_ErrorAddress(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(chip(a,SLATE,2.5),chip(b,c,1.5)).arrange(RIGHT,buff=.5) for a,b,c in [("flip q1","10",TEAL),("flip q2","11",CRIMSON),("flip q3","01",TEAL)]]).arrange(DOWN,buff=.35);self.play(LaggedStart(*[FadeIn(r,shift=RIGHT*.12) for r in rows],lag_ratio=.2),run_time=1.2);self.wait(max(.5,D["B07"]-1.2))
class B08_SecretPreserved(Scene):
 def construct(self):
  a=VGroup(chip("|010>",TEAL,2.4),chip("syndrome 11",CRIMSON,3)).arrange(RIGHT,buff=.6);b=VGroup(chip("|101>",TEAL,2.4),chip("syndrome 11",CRIMSON,3)).arrange(RIGHT,buff=.6);g=VGroup(a,b).arrange(DOWN,buff=.7);cap=Text("same error address · no α/β information",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.6);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B08"]-1))
class B09_Correct(Scene):
 def construct(self):
  bad=chip("α|010> + β|101>",CRIMSON,5);op=chip("X on q2",SLATE,2.3);good=chip("α|000> + β|111>",TEAL,5);g=VGroup(bad,op,good).arrange(DOWN,buff=.5);self.play(FadeIn(bad),run_time=.4);self.play(FadeIn(op),run_time=.4);self.play(FadeIn(good),run_time=.5);self.wait(max(.5,D["B09"]-1.3))
class B10_ChosenMeasurement(Scene):
 def construct(self):
  yes=head("MEASURE","which error subspace?",TEAL);no=head("DO NOT MEASURE","which logical state?",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Fixing Quantum Errors",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Without Ever Looking",font=SERIF,color="#D7C8FF",font_size=40,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.64
  self.add(bg(),ttl('This code protects against one bit flip,'))
  stmt=Text('This code protects against one bit flip, an X error',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It does not by itself protect against phase errors or a',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=7.81
  self.add(bg(),ttl('Instead, ask whether qubits one and two'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Instead, ask whether qubits one and two agree, and whet',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('These are parity checks, often extracted through ancill',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.62
  self.add(bg(),ttl('With no error, both pairs agree: syndrom'))
  stmt=Text('With no error, both pairs agree: syndrome zero-zero',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If qubit one flips, only the first check disagrees: one',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.26
  self.add(bg(),ttl('A flip on qubit two makes both'))
  stmt=Text('A flip on qubit two makes both checks disagree: one-one',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A flip on qubit three gives zero-one',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=9.41
  self.add(bg(),ttl('Crucially, the same syndrome appears for'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Crucially, the same syndrome appears for the zero-zero-',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The measurement learns where the flip occurred, not alp',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
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
  self.add(bg(),ttl('The trick is not measurement without dis'))
  stmt=Text('The trick is not measurement without disturbance',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It is a carefully chosen measurement that preserves coh',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.47
  self.add(bg(),ttl('Fixing quantum errors without looking: m'))
  stmt=Text('Fixing quantum errors without looking: measure the erro',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
