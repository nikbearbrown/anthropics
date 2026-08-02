import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def sphere(angle=70):
 c=Circle(radius=2.25,color=SLATE); eq=Ellipse(width=4.5,height=1.15,color=SLATE); axis=DoubleArrow(DOWN*2.6,UP*2.6,color=INK,buff=0); a=np.deg2rad(angle); v=Arrow(ORIGIN,np.array([2*np.sin(a),2*np.cos(a),0]),color=CRIMSON,buff=0,stroke_width=7); return VGroup(c,eq,axis,v)
class B02_Resonant(Scene):
 def construct(self):
  d=DUR.get('B02',14); self.add(bg(),ttl('ON RESONANCE, A WEAK DRIVE CAN REACH THE SOUTH POLE')); s=sphere(155); wave=FunctionGraph(lambda x:.35*np.sin(5*x),x_range=[-2,2],color=TEAL).shift(LEFT*4); pulse=VGroup(wave,Text('RF on resonance',font=MONO,font_size=27,color=TEAL).move_to(LEFT*4+DOWN*2)); self.play(Create(s),Create(pulse),run_time=1.2); self.wait(max(.1,d-1.2))
class B03_Populations(Scene):
 def construct(self):
  d=DUR.get('B03',12); self.add(bg(),ttl('POPULATIONS EXCHANGE COMPLEMENTARILY')); ax=Axes(x_range=[0,6.3,1.57],y_range=[0,1,.25],x_length=10,y_length=5,axis_config={'color':SLATE}); up=ax.plot(lambda x:np.cos(x/2)**2,x_range=[0,6.28],color=TEAL); dn=ax.plot(lambda x:np.sin(x/2)**2,x_range=[0,6.28],color=CRIMSON); labs=VGroup(Text('P(up)',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*4+UP*2),Text('P(down)',font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*4+UP*1.4),Text('sum = 1',font=MONO,font_size=27,color=INK).move_to(DOWN*3)); self.play(Create(ax),Create(up),Create(dn),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B04_Accumulate(Scene):
 def construct(self):
  d=DUR.get('B04',14); self.add(bg(),ttl('WEAK MEANS SLOW — NOT SHALLOW')); steps=VGroup(*[Arrow(ORIGIN,RIGHT*.75,color=TEAL,buff=0).shift(LEFT*4+RIGHT*i*.85+UP*np.sin(i*.5)*.25) for i in range(10)]); eq=Text('small coherent rotations accumulate',font=SERIF,font_size=36,color=CRIMSON).move_to(DOWN*2); self.play(*[GrowArrow(x) for x in steps],FadeIn(eq),run_time=1.3); self.wait(max(.1,d-1.3))
class B05_Duration(Scene):
 def construct(self):
  d=DUR.get('B05',12); self.add(bg(),ttl('PULSE DURATION SETS THE ROTATION ANGLE')); short=sphere(35).scale(.65).shift(LEFT*3); full=sphere(180).scale(.65).shift(RIGHT*3); labs=VGroup(Text('short pulse: small move',font=MONO,font_size=26,color=SLATE).move_to(LEFT*3+DOWN*2.5),Text('pi-pulse: full flip',font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*3+DOWN*2.5)); self.play(Create(short),Create(full),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B06_Basis(Scene):
 def construct(self):
  d=DUR.get('B06',14); self.add(bg(),ttl('UP IS A SUPERPOSITION OF THE DRIVE EIGENSTATES')); eqs=VGroup(Text('|up> = (|+x> + |-x>) / sqrt(2)',font=MONO,font_size=38,color=INK),Text('|+x>',font=MONO,font_size=34,color=TEAL),Text('|-x>',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B07_Phase(Scene):
 def construct(self):
  d=DUR.get('B07',13); self.add(bg(),ttl('THE DRESSED-STATE PHASE GAP GROWS TO pi')); c1=Circle(radius=1.5,color=TEAL).shift(LEFT*3); c2=Circle(radius=1.5,color=CRIMSON).shift(RIGHT*3); h1=Arrow(c1.get_center(),c1.get_center()+UP*1.2,color=TEAL,buff=0); h2=Arrow(c2.get_center(),c2.get_center()+DOWN*1.2,color=CRIMSON,buff=0); lab=Text('Delta phi = pi at the flip',font=MONO,font_size=34,color=INK).move_to(DOWN*2.7); self.play(Create(c1),Create(c2),GrowArrow(h1),GrowArrow(h2),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B08_Interference(Scene):
 def construct(self):
  d=DUR.get('B08',14); self.add(bg(),ttl('INTERFERENCE SWAPS THE OUTPUT')); left=VGroup(Arrow(ORIGIN,RIGHT*1.7,color=TEAL,buff=0),Arrow(ORIGIN,LEFT*1.7,color=CRIMSON,buff=0)).shift(LEFT*3); right=VGroup(Arrow(ORIGIN,UP*1.7,color=TEAL,buff=0),Arrow(ORIGIN,UP*1.7,color=CRIMSON,buff=0)).shift(RIGHT*3); labs=VGroup(Text('up cancels',font=MONO,font_size=28,color=CRIMSON).move_to(LEFT*3+DOWN*2),Text('down adds',font=MONO,font_size=28,color=TEAL).move_to(RIGHT*3+DOWN*2)); self.play(*[GrowArrow(x) for x in [*left,*right]],FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Scope(Scene):
 def construct(self):
  d=DUR.get('B09',16); self.add(bg(),ttl('FULL INVERSION HAS CONDITIONS')); good=VGroup(Text('ON RESONANCE',font=DISPLAY,font_size=32,color=TEAL),Text('coherent',font=MONO,font_size=29,color=TEAL),Text('100% possible',font=MONO,font_size=29,color=TEAL)).arrange(DOWN,buff=.5).shift(LEFT*3); bad=VGroup(Text('DETUNED / DECOHERENT',font=DISPLAY,font_size=30,color=CRIMSON),Text('tilted axis / lost phase',font=MONO,font_size=27,color=CRIMSON),Text('reduced transfer',font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.5).shift(RIGHT*3); self.play(FadeIn(good,bad),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',18); self.add(bg(),ttl('YOUR TURN: f_R = 20 kHz')); eqs=VGroup(Text('t_pi = 1 / (2 f_R)',font=MONO,font_size=40,color=INK),Text('= 25 microseconds',font=MONO,font_size=42,color=CRIMSON),Text('another 25 microseconds -> back to up',font=MONO,font_size=31,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',16); self.add(bg(),Text('WHY A SPIN FLIPS WHEN YOU WHISPER',font=DISPLAY,font_size=36,color=CRIMSON).move_to(UP*2.3),Text('resonant coherent drive',font=MONO,font_size=35,color=TEAL).move_to(UP*.8),Text('relative phase accumulates',font=MONO,font_size=35,color=INK).move_to(DOWN*.4),Text('strength sets speed · coherence sets reach',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.27
  self.add(bg(),ttl('The question: the transverse drive is we'))
  stmt=Text('The question: the transverse drive is weak compared wit',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Why can it still produce a complete flip? A weak torque',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.06
  self.add(bg(),ttl('The naive reading confuses rate with rea'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The naive reading confuses rate with reach',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('A weak resonant field rotates slowly, so a short pulse ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.21
  self.add(bg(),ttl('The mechanism: the sideways field is not'))
  stmt=Text('The mechanism: the sideways field is not acting on the ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It defines two energy eigenstates — spin-x-plus and spi',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.18
  self.add(bg(),ttl('Each eigenstate accumulates a phase at i'))
  stmt=Text('Each eigenstate accumulates a phase at its own energy r',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The two phases advance at slightly different speeds',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.95
  self.add(bg(),ttl('When the beat reaches pi, the two'))
  stmt=Text('When the beat reaches pi, the two phasors are exactly o',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('They destructively interfere for spin-up and constructi',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=16.11
  self.add(bg(),ttl('On resonance, the Rabi angular frequency'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('On resonance, the Rabi angular frequency equals the dri',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('A weaker drive means a smaller splitting and a longer p',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.7
  self.add(bg(),ttl('Your turn. An ideal resonant drive has'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('An ideal resonant drive has Rabi frequency 20 kilohertz',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('How long is a pi-pulse? Half a Rabi cycle: 25 microseco',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
