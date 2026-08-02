import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def card(t,c=SLATE,w=2.5):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=25).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=43,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_SharedPair(Scene):
 def construct(self):
  a=card("Alice: qA",TEAL,3);b=card("Bob: qB",CRIMSON,3);line=Line(a.get_right(),b.get_left(),color=SLATE,stroke_width=5);g=VGroup(a,line,b).arrange(RIGHT,buff=.8);lab=Text("shared |Phi+>",font=SERIF,color=INK,font_size=32,slant=ITALIC).next_to(g,DOWN,buff=.7);self.play(FadeIn(g),FadeIn(lab),run_time=1);self.wait(max(.5,D["B02"]-1))
class B03_FourOperations(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(card(m,SLATE,1.5),card(op,c,1.5)).arrange(RIGHT,buff=.45) for m,op,c in [("00","I",TEAL),("01","Z",CRIMSON),("10","X",TEAL),("11","XZ",CRIMSON)]]).arrange(DOWN,buff=.25);self.play(LaggedStart(*[FadeIn(x) for x in rows],lag_ratio=.18),run_time=1.2);self.wait(max(.5,D["B03"]-1.2))
class B04_FourBellStates(Scene):
 def construct(self):
  g=VGroup(*[VGroup(card(op,SLATE,1.4),card(state,c,2.4)).arrange(RIGHT,buff=.4) for op,state,c in [("I","Phi+",TEAL),("Z","Phi-",CRIMSON),("X","Psi+",TEAL),("XZ","Psi-",CRIMSON)]]).arrange(DOWN,buff=.25);self.play(LaggedStart(*[FadeIn(x,shift=RIGHT*.1) for x in g],lag_ratio=.18),run_time=1.2);self.wait(max(.5,D["B04"]-1.2))
class B05_JointEncoding(Scene):
 def construct(self):
  local=title("ONE LOCAL QUBIT","does not reveal the message",CRIMSON);joint=title("JOINT BELL STATE","holds the two-bit label",TEAL);g=VGroup(local,joint).arrange(RIGHT,buff=1.2);self.play(FadeIn(g),run_time=.9);self.wait(max(.5,D["B05"]-.9))
class B06_SendQubit(Scene):
 def construct(self):
  a=card("ALICE",TEAL,2.5).to_edge(LEFT,buff=1);b=card("BOB",CRIMSON,2.5).to_edge(RIGHT,buff=1);q=Dot(a.get_right()+RIGHT*.4,color=TEAL,radius=.22);arr=Arrow(a.get_right(),b.get_left(),color=INK,buff=.25);self.play(FadeIn(a),FadeIn(b),FadeIn(q),run_time=.5);self.play(MoveAlongPath(q,arr),GrowArrow(arr),run_time=1.1);self.wait(max(.5,D["B06"]-1.6))
class B07_BellMeasurement(Scene):
 def construct(self):
  inputs=VGroup(card("qA",TEAL,1.4),card("qB",CRIMSON,1.4)).arrange(RIGHT,buff=.3);meas=card("BELL MEASUREMENT",SLATE,4).next_to(inputs,DOWN,buff=.7);outs=VGroup(*[card(s,c,1.8) for s,c in [("Phi+",TEAL),("Phi-",CRIMSON),("Psi+",TEAL),("Psi-",CRIMSON)]]).arrange(RIGHT,buff=.25).next_to(meas,DOWN,buff=.7);self.play(FadeIn(inputs),FadeIn(meas),run_time=.7);self.play(LaggedStart(*[FadeIn(x) for x in outs],lag_ratio=.15),run_time=.8);self.wait(max(.5,D["B07"]-1.5))
class B08_DecodeTable(Scene):
 def construct(self):
  g=VGroup(*[VGroup(card(s,c,2),card(m,SLATE,1.4)).arrange(RIGHT,buff=.4) for s,m,c in [("Phi+","00",TEAL),("Phi-","01",CRIMSON),("Psi+","10",TEAL),("Psi-","11",CRIMSON)]]).arrange(DOWN,buff=.25);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.18),run_time=1.2);self.wait(max(.5,D["B08"]-1.2))
class B09_ResourceAccounting(Scene):
 def construct(self):
  top=VGroup(card("1 transmitted qubit",CRIMSON,4),Text("+",font=DISPLAY,color=INK,font_size=40),card("1 shared ebit",TEAL,3.4)).arrange(RIGHT,buff=.35);arr=Arrow(UP*.2,DOWN*.8,color=INK);out=card("2 classical bits",SLATE,4).next_to(arr,DOWN,buff=.25);g=VGroup(top,arr,out).arrange(DOWN,buff=.35);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B09"]-1))
class B10_NoFTL(Scene):
 def construct(self):
  before=title("BEFORE QUBIT ARRIVES","Bob's local state: unchanged",CRIMSON);after=title("AFTER QUBIT ARRIVES","joint measurement can decode",TEAL);g=VGroup(before,after).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("One Qubit, Two Bits",font=DISPLAY,color=WHITE,font_size=52,weight=BOLD);b=Text("Superdense Coding",font=SERIF,color="#D7C8FF",font_size=40,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Begin with Bell state phi plus. Alice'))
  stmt=Text('Begin with Bell state phi plus',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Alice holds qubit A, Bob holds qubit B',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Alice chooses message zero-zero, zero-on'))
  stmt=Text('Alice chooses message zero-zero, zero-one, one-zero, or',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('She encodes it by applying one of four local operations',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Those four operations transform the shar'))
  stmt=Text('Those four operations transform the shared pair into fo',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Alice has changed only her half, yet'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Alice has changed only her half, yet the information is',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Bob still cannot read it while the qubits are separated',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Phi plus decodes zero-zero, phi minus ze'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Phi plus decodes zero-zero, phi minus zero-one, psi plu',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Result',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.0
  self.add(bg(),ttl('The honest resource statement is two cla'))
  stmt=Text('The honest resource statement is two classical bits com',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It is not two bits stored in an isolated qubit',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('There is no faster-than-light signaling.'))
  stmt=Text('There is no faster-than-light signaling',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Before Alice\'s qubit arrives, Bob\'s local state is unch',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('One qubit, two bits: not a free'))
  stmt=Text('One qubit, two bits: not a free doubling, but one trans',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
