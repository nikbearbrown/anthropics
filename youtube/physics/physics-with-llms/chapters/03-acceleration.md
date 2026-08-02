# Chapter 3: Acceleration

## Title Options
1. The Physics of Not Staying Still
2. How Things Change Direction—And Why That Matters
3. The Hidden Rule of Every Moving Thing

---

## TL;DR
Acceleration is not about speed alone—it's any change in how you move, including slowing down or turning. The five kinematic equations predict where accelerating objects end up and how fast they'll be moving when they get there.

---

## Chapter Opening: The Braking Line

Picture a dragster idling at the starting line. The driver sits motionless, engine running. Someone at the control tower counts down. Then: the light flashes green. The driver pushes the accelerator to the floor.

In four seconds, the car will be traveling faster than 300 miles per hour. In those same four seconds, if the driver had only *released* the gas pedal and coasted, the car would barely be rolling forward. The difference between two scenarios separated by four seconds is acceleration.

Now consider a different moment, one most of us know directly. You're in a car turning a corner at a constant speed. Your body shifts. The driver hasn't changed the speedometer reading—you're still going 35 miles per hour—but you feel pressed against the door. You are, in fact, accelerating. The velocity vector is turning.

Here's what makes this interesting: the dragster driver and the turning car driver experience something fundamentally the same, even though one is changing speed and the other is changing direction. Both are accelerating. Physics calls them both acceleration because physics cares about change in velocity, not change in speed.

This chapter is about how to measure that change, predict it, and use it to solve problems that look complicated until you see the machinery underneath.

### Learning Objectives
By the end of this chapter, you will be able to:
- Explain acceleration as a rate of change in velocity
- Distinguish acceleration from speed
- Apply kinematic equations to predict position and velocity of an accelerating object
- Interpret graphs of motion to extract information about velocity and acceleration
- Solve problems involving constant acceleration in one dimension

### Prerequisites
- Understand vectors and one-dimensional displacement
- Know what velocity means and how to calculate average velocity
- Be comfortable with SI units and unit conversion
- Be able to interpret graphs of position versus time

### Why This Matters
Acceleration is the bridge between forces and motion. Every object that changes speed or direction is accelerating. Understanding how to calculate acceleration and predict the motion of accelerating objects is essential to nearly every problem in mechanics that follows. When you learn why objects fall or how to predict where a projectile lands, you'll be using the machinery you build here.

---

## Concept 1: Acceleration as Change in Velocity

### The Cold Open: Two Definitions Wearing One Word

The gas pedal in a car is called an accelerator. When you press it, the car speeds up. So acceleration means "getting faster," right?

Not quite. It means something stricter.

A car pressing harder on the gas pedal is accelerating. So is a car pressing the brake. So is a car turning a corner at constant speed. All three are *changing velocity*, and acceleration is the name for that change.

Let's nail this down precisely, because the word "acceleration" hides vagueness the moment you don't.

Velocity is a vector: it has magnitude (speed) and direction. To change velocity, you can change speed, change direction, or change both. A dragster increasing speed is accelerating. A car slowing down is accelerating. A car turning is accelerating. The sign of the velocity change, or the direction of the change, doesn't matter—motion that changes is accelerating.

Imagine you're moving to the right at 10 m/s. You press the brake and your speed drops to 5 m/s. Your velocity changed: it went from +10 m/s to +5 m/s. That's a change of −5 m/s, which means acceleration is negative and points to the left (opposite the motion). In everyday language, this is sometimes called "deceleration." In physics, it's acceleration with a minus sign.

Now imagine you're standing still. A force acts on you and accelerates you from rest. The word *rest* is precise in physics—it means zero velocity. You start at 0 m/s and reach 5 m/s. That's acceleration. The direction of the acceleration vector points in the direction of motion.

### Defining Acceleration Mathematically

Acceleration is the change in velocity divided by the time over which that change occurs.

$$\overline{a} = \frac{\Delta v}{\Delta t} = \frac{v_{\text{f}} - v_{0}}{t_{\text{f}} - t_{0}}$$

This is *average acceleration*. It's the total change in velocity, divided by the total time.

The symbol $\Delta$ (the Greek letter delta) always means "the change in." So $\Delta v$ means "final velocity minus initial velocity." The bar over the $a$ means "average."

The units tell you something important about what acceleration does. Velocity is measured in meters per second (m/s). Time is measured in seconds (s). So acceleration is measured in meters per second *per* second, written as m/s² (or "meters per second squared"). This is a strange-looking unit until you think about it: every second that passes, your velocity changes by some number of meters per second.

There's also *instantaneous acceleration*—the acceleration at one specific instant in time. For now, and for most of what you'll solve in this chapter, the distinction doesn't matter much. We'll be dealing with cases where acceleration doesn't change: **constant acceleration**. When acceleration is constant, average acceleration and instantaneous acceleration are the same number.

### The Trade-off: Precision and Simplicity

Constant acceleration is a special case. In real life, dragsters accelerate hard at the start, then the rate of acceleration drops as the engine reaches higher speeds. A car braking hard at first slows quickly, then less quickly as you approach a stop. The acceleration is changing during the motion.

But for the problems we can actually solve with simple equations, and for the cases where the change in acceleration is small enough to ignore, we assume constant acceleration. This is a trade-off: we lose accuracy in the details of what happens in the real world, but we gain the ability to make predictions. For a dragster's quarter-mile run, the assumption of constant acceleration is good enough to predict the final speed within a few meters per second. For a car braking to a stop over a few seconds, it's remarkably accurate.

### Worked Example: A Subway Train Accelerating from Rest

A subway train is waiting at a station. The doors close. The driver advances the control lever, and the train begins to move. After 20 seconds, the train has reached a speed of 30.0 km/h. What was the average acceleration?

**Strategy:** We know the initial velocity (zero—at rest), the final velocity (30.0 km/h), and the time interval (20.0 s). We need to find acceleration. First, convert the velocity to SI units (meters per second). Then apply the definition of average acceleration.

**Converting units:**
$$30.0 \text{ km/h} \times \frac{1000 \text{ m}}{1 \text{ km}} \times \frac{1 \text{ h}}{3600 \text{ s}} = 8.33 \text{ m/s}$$

**Finding the change in velocity:**
$$\Delta v = v_{\text{f}} - v_{0} = 8.33 \text{ m/s} - 0 \text{ m/s} = 8.33 \text{ m/s}$$

The plus sign tells us the change is in the direction we've called positive (usually to the right or forward).

**Applying the definition of average acceleration:**
$$\overline{a} = \frac{\Delta v}{\Delta t} = \frac{8.33 \text{ m/s}}{20.0 \text{ s}} = 0.417 \text{ m/s}^2$$

So every second, the train's velocity increases by 0.417 m/s. After 1 second, it's moving at 0.417 m/s. After 2 seconds, 0.834 m/s. After 20 seconds, 8.33 m/s.

### Worked Example: A Sports Car Accelerating from Motion

Now consider a sports car that's already moving. The car is traveling at 10.0 m/s when the driver steps on the accelerator hard. After 5.0 seconds, the car is traveling at 30.0 m/s. What was the average acceleration during those 5 seconds?

**Given:** $v_0 = 10.0$ m/s, $v_f = 30.0$ m/s, $\Delta t = 5.0$ s.

**Change in velocity:**
$$\Delta v = 30.0 - 10.0 = 20.0 \text{ m/s}$$

**Average acceleration:**
$$\overline{a} = \frac{20.0 \text{ m/s}}{5.0 \text{ s}} = 4.0 \text{ m/s}^2$$

The car is accelerating at 4.0 m/s². Notice this is the same magnitude as a dragster's first-second acceleration in some races, but sustained over a longer time. A sports car at 4.0 m/s² is impressive by everyday driving standards.

### Common Misconception: "Acceleration Means Speeding Up"

Students often think acceleration means the object is moving faster. This breaks apart the moment you see a car braking.

A car moving forward at 20 m/s and pressing the brake has a velocity of +20 m/s. After 2 seconds, it's moving forward at 10 m/s—a velocity of +10 m/s. The change in velocity is $10 - 20 = -10$ m/s, so the acceleration is $-10 / 2 = -5$ m/s². Negative acceleration. The car is slowing down.

In physics, "acceleration" is neutral about direction. It's the change in velocity, not the increase in speed. A speedometer might show decreasing numbers, but physics says the object is accelerating—with a minus sign in front.

---

## Concept 2: The Kinematic Equations—Predicting Motion Under Constant Acceleration

### The Cold Open: The Dragster's Final Speed

A dragster sits at the starting line of a quarter-mile track. The track is 402 meters long. The dragster can accelerate at 26.0 m/s² (which is about 2.7 times Earth's gravity). The driver wants to know one thing: how fast will I be going when I cross the finish line?

The catch: we don't know how long it will take. We only know the distance, the acceleration, and the starting condition (at rest). We need an equation that connects acceleration, distance, and final velocity—and leaves out time.

That equation exists. It's one of the five kinematic equations.

### Building the Kinematic Equations from the Definition of Average Acceleration

We have one equation and a definition. From these, we can build others.

**Equation 1** (definition of average velocity):
$$\overline{v} = \frac{d}{t}$$

This says that average velocity is displacement per unit time. If you travel 100 meters in 10 seconds, your average velocity is 10 m/s.

**Equation 2** (average velocity under constant acceleration):
$$\overline{v} = \frac{v_0 + v_f}{2}$$

When acceleration is constant, the average velocity is exactly the midpoint between the starting velocity and the ending velocity. If you start at 0 m/s and end at 20 m/s, your average velocity is 10 m/s.

**Equation 3** (velocity under constant acceleration):
$$v = v_0 + at$$

This says that your final velocity is your initial velocity plus the change in velocity caused by acceleration over time. If you start at 0 m/s and accelerate at 2 m/s² for 5 seconds, you end at $0 + (2)(5) = 10$ m/s.

**Equation 4** (displacement under constant acceleration):
$$d = d_0 + v_0 t + \frac{1}{2}at^2$$

This is where constant acceleration reveals its power. When acceleration is not zero, the path it traces isn't a straight line on a position-versus-time graph—it's a parabola. The term $\frac{1}{2}at^2$ is the "extra" distance you travel because you're speeding up (or slowing down) as you go.

To see why, imagine you start at rest and accelerate. In the first second, you barely move. In the second second, you're moving faster, so you cover more ground. In the third second, you're moving even faster, so you cover even more ground. The total distance isn't $v \times t$ (which would work for constant velocity)—it's more than that, because you're accelerating. The kinematic equations capture this.

**Equation 5** (relating velocity, acceleration, and displacement):
$$v^2 = v_0^2 + 2a(d - d_0)$$

This equation has no time in it. If you know your starting velocity, your acceleration, and the distance you've traveled, you can find your final velocity without knowing how long it took. This is the equation the dragster needs.

### Solving the Dragster Problem

The dragster accelerates at $a = 26.0$ m/s² for a distance of $d = 402$ m, starting from rest ($v_0 = 0$).

Using Equation 5:
$$v^2 = 0^2 + 2(26.0)(402)$$
$$v^2 = 20,904 \text{ m}^2/\text{s}^2$$
$$v = \sqrt{20,904} = 145 \text{ m/s}$$

That's about 324 miles per hour. The dragster crosses the finish line at 145 m/s.

But notice something: the actual dragster record is faster than this. Why? Because our assumption of constant acceleration breaks down at high speeds. The air resistance increases, and the engine has efficiency limits. Real dragsters don't accelerate uniformly over the quarter-mile.

Yet for a rough prediction—knowing whether the dragster is in the realm of 100 m/s or 200 m/s—constant acceleration gets you close.

### The Trade-off: Constant Acceleration Simplifies; Reality Complicates

The kinematic equations work beautifully when acceleration is constant. But the real world doesn't often give you constant acceleration.

A car pressing the accelerator doesn't maintain the same acceleration as the speed climbs; the engine's power output is limited, and air resistance increases. A parachutist falling through air doesn't maintain constant acceleration; air resistance grows with speed until eventually, the upward air resistance equals the downward gravitational force, and acceleration drops to zero (called terminal velocity).

But here's why constant acceleration is worth studying: in short time intervals or over small distances, acceleration often *looks* constant. A dragster over a quarter-mile has changing acceleration, but if you assumed constant acceleration, you'd be within a few percent of the right answer. A car braking to a stop is more complicated than constant deceleration, but the simple model predicts the stopping distance well enough to inform speed limits near schools.

The kinematic equations are your first tool. When they're not good enough, you'll learn to build more refined models. But nearly every problem you'll face in mechanics starts here.

### Worked Example: A Runner Accelerating from a Standstill

An Olympic sprinter starts a 100-meter race from blocks. She accelerates at a nearly constant 4.50 m/s² for the first 2.40 seconds of the race. What is her velocity at the end of that acceleration phase?

**Using Equation 3:**
$$v = v_0 + at = 0 + (4.50 \text{ m/s}^2)(2.40 \text{ s}) = 10.8 \text{ m/s}$$

Now, how far did she travel during that time?

**Using Equation 4:**
$$d = v_0 t + \frac{1}{2}at^2 = 0 + \frac{1}{2}(4.50)(2.40)^2 = \frac{1}{2}(4.50)(5.76) = 12.96 \text{ m}$$

She's traveled about 13 meters and is now moving at 10.8 m/s (about 24 miles per hour). She still has most of the race to go—87 meters—and she's now at a much higher velocity. In the remaining distance, her acceleration will drop (due to fatigue and air resistance), so she won't maintain 4.50 m/s².

### Common Misconception: "I Need All Five Equations"

Students sometimes memorize all five kinematic equations and then freeze, unsure which one to use.

Here's the secret: you need to know what you *know* and what you *don't know*.

If you know distance, initial velocity, and acceleration, and you want final velocity—use Equation 5, which has no time.

If you know initial velocity, acceleration, and time, and you want final velocity—use Equation 3, which is the simplest.

If you know distance, time, and initial velocity, and you want acceleration—rearrange Equation 4.

The equations are tools. Pick the tool that matches your knowns and unknowns. You don't need all five for every problem. You need *one*.

---

## Concept 3: Constant Acceleration Under Gravity—Free Fall

### The Cold Open: Two Rocks Dropped from a Cliff

Stand at the edge of a tall cliff. You have two rocks. One is heavier than the other. Drop them at the same time.

Do they hit the ground at the same time?

Aristotle said no. He argued that heavier objects fall faster. For nearly two thousand years, this was accepted. The reasoning seemed obvious: weight should matter in falling.

Galileo said otherwise. He argued that in the absence of air resistance, all objects fall at the same rate. He couldn't measure it directly—clocks were too slow, and free fall happens too fast. But he reasoned about it.

Here's the reasoning: if a heavy object fell faster than a light object, then tie them together. The light object would hold the heavy object back, slowing the heavy one down. But the combined object is now heavier still, so it should fall faster. Contradiction. Therefore, weight doesn't determine the rate of fall.

Galileo was right. We can measure it now, and we find that all objects near Earth's surface fall at the same acceleration in the absence of air resistance. That acceleration is $g = 9.80$ m/s² (sometimes rounded to 9.8 or even 10 for rough estimates).

This is not an accident. It's a deep fact about gravity: the strength of gravity is proportional to your mass, and the inertia that resists acceleration is also proportional to your mass. They cancel. A feather and a hammer, dropped on the Moon (where there's no air resistance to speak of), fall side by side.

### The First Kinematic Equation Under Gravity: Free Fall from Rest

When an object is dropped from rest and falls under gravity, we can use the kinematic equations with a specific value for acceleration: $a = -g = -9.80$ m/s² (negative because downward is negative, by convention).

If you drop a rock from a cliff and want to know how far it falls in time $t$, use Equation 4:
$$y = y_0 + v_0 t + \frac{1}{2}at^2$$

With $v_0 = 0$ (dropped, not thrown):
$$y = y_0 - \frac{1}{2}gt^2$$

If you start at the cliff edge and measure downward as negative, and the cliff is 100 meters tall, then:
$$-100 = 0 - \frac{1}{2}(9.80)t^2$$
$$t^2 = \frac{100}{4.90} = 20.4$$
$$t = 4.52 \text{ seconds}$$

It takes about 4.5 seconds for a rock to fall 100 meters. Notice that this is quite a while—not the split-second tumble we might naively imagine.

### Worked Example: A Rock Thrown Upward from a Cliff

This is more complex because the acceleration is downward, but the initial velocity is upward. Watch what happens.

A person stands on a cliff and throws a rock straight up with an initial velocity of 13 m/s. The cliff is 50 meters above the ground. Where is the rock at $t = 1.00$ s, $t = 2.00$ s, and $t = 3.00$ s? What is its velocity at each of these times?

**Setting up coordinates:** Let up be positive. Then $a = -g = -9.80$ m/s², $v_0 = +13$ m/s, $y_0 = 0$ (the cliff edge).

**At $t = 1.00$ s:**

Using Equation 4:
$$y = 0 + (13)(1.00) + \frac{1}{2}(-9.80)(1.00)^2 = 13 - 4.9 = 8.1 \text{ m}$$

The rock is 8.1 meters above the cliff edge.

Using Equation 3:
$$v = 13 + (-9.80)(1.00) = 13 - 9.80 = 3.2 \text{ m/s}$$

The rock is moving upward at 3.2 m/s. It's still going up, but slowing.

**At $t = 2.00$ s:**

$$y = 0 + (13)(2.00) + \frac{1}{2}(-9.80)(2.00)^2 = 26 - 19.6 = 6.4 \text{ m}$$

The rock is 6.4 meters above the cliff edge.

$$v = 13 + (-9.80)(2.00) = 13 - 19.6 = -6.6 \text{ m/s}$$

The rock is moving downward at 6.6 m/s. It has passed the peak and is now falling.

**At $t = 3.00$ s:**

$$y = 0 + (13)(3.00) + \frac{1}{2}(-9.80)(3.00)^2 = 39 - 44.1 = -5.1 \text{ m}$$

The rock is 5.1 meters *below* the cliff edge—it's passed the ground.

$$v = 13 + (-9.80)(3.00) = 13 - 29.4 = -16.4 \text{ m/s}$$

The rock is moving downward at 16.4 m/s.

Notice the pattern: the rock goes up, slows, stops (somewhere between $t = 1$ and $t = 2$), then comes back down, accelerating as it falls. The acceleration is constant throughout—always $-9.80$ m/s² downward. But the velocity changes sign from positive (upward) to negative (downward).

### The Trade-off: Neglecting Air Resistance

In reality, air resistance slows a falling object. A feather falls much slower than a rock. But the equations here assume no air resistance. They work well for dense objects (rocks, steel balls) falling through air over short distances or short times. For feathers, for dense objects falling from high altitudes, or for any motion through a fluid (water, oil), air resistance matters and these equations break down.

But for most problems you'll encounter in an introductory physics course—a ball dropped from a building, a rock thrown from a cliff, a ball falling on a basketball court—air resistance is small enough to ignore. The assumption is worth making, because it lets you use these simple equations.

### Common Misconception: "Heavier Objects Fall Faster"

This myth persists because of Aristotle and because of air resistance. In air, a bowling ball falls faster than a feather. But the bowling ball isn't falling *because* it's heavier. It's falling at nearly the same acceleration as the feather ($-9.80$ m/s²). The feather falls slower because air resistance slows it down more than it slows the bowling ball (feathers have a high surface-area-to-mass ratio; bowling balls don't).

In a vacuum, both fall at $-9.80$ m/s². Galileo would be satisfied.

---

## Integration: Connecting the Pieces

You now have three core ideas:

1. **Acceleration is change in velocity.** It's defined and measured in m/s².
2. **Five kinematic equations predict the motion of constant-acceleration objects.** You pick the equation that matches your knowns and unknowns.
3. **Gravity provides a specific, constant acceleration.** Objects in free fall accelerate downward at 9.80 m/s² regardless of their mass (ignoring air resistance).

Here's how they connect. Suppose you're standing on a bridge 25 meters above a river and you drop a key. How long until it hits the water? You know distance, acceleration, and initial velocity (zero). You use Equation 4:

$$d = v_0 t + \frac{1}{2}at^2$$
$$25 = 0 + \frac{1}{2}(9.80)t^2$$
$$t^2 = \frac{25}{4.90} = 5.10$$
$$t = 2.26 \text{ seconds}$$

How fast is the key moving when it hits the water? Use Equation 3:
$$v = v_0 + at = 0 + (9.80)(2.26) = 22.1 \text{ m/s}$$

Or skip finding the time. Use Equation 5:
$$v^2 = v_0^2 + 2a(d - d_0) = 0 + 2(9.80)(25) = 490$$
$$v = 22.1 \text{ m/s}$$

All three equations tell the same story, painted in different variables. The key takes about 2.3 seconds to fall 25 meters, and it's moving at about 22 m/s when it hits the water.

This is the power of the kinematic framework: once you understand the definitions and the equations, a wide range of problems becomes solvable.

---

## Exercises

### Warm-Up: Building Intuition

**1. A car accelerates from 0 to 20 m/s in 5 seconds, with constant acceleration. What is the acceleration?**

A: 4 m/s²  
B: 5 m/s²  
C: 20 m/s²  
D: 100 m/s²

(Answer: A. Use $a = \Delta v / \Delta t = 20 / 5 = 4$ m/s².)

**2. A tennis ball is dropped from a height of 2 meters. Approximately how long does it take to hit the ground?**

A: 0.2 seconds  
B: 0.6 seconds  
C: 2 seconds  
D: 10 seconds

(Answer: B. Use $d = \frac{1}{2}gt^2$, so $2 = \frac{1}{2}(9.8)t^2$, giving $t = \sqrt{0.41} \approx 0.64$ s.)

### Application: Using the Equations

**3. A subway train accelerates from rest at a constant 0.5 m/s² for 30 seconds. How far does it travel in that time?**

Using Equation 4 with $v_0 = 0$:
$$d = 0 + \frac{1}{2}(0.5)(30)^2 = \frac{1}{2}(0.5)(900) = 225 \text{ meters}$$

**4. A basketball player shoots a ball upward with an initial velocity of 8 m/s. How high does it rise before falling back down?**

At the peak, $v = 0$. Using Equation 5:
$$0 = (8)^2 + 2(-9.80)(d - 0)$$
$$0 = 64 - 19.6d$$
$$d = \frac{64}{19.6} = 3.27 \text{ meters}$$

**5. A sports car traveling at 10.0 m/s steps on the accelerator hard. After 5.0 seconds, it's traveling at 30.0 m/s. What is its average acceleration?**

$$\overline{a} = \frac{\Delta v}{\Delta t} = \frac{30.0 - 10.0}{5.0} = \frac{20.0}{5.0} = 4.0 \text{ m/s}^2$$

### Synthesis: Combining Concepts

**6. A car brakes from 30 m/s to a complete stop over a distance of 75 meters. What is the acceleration (deceleration)?**

Using Equation 5:
$$v_f^2 = v_0^2 + 2a(d - d_0)$$
$$0 = (30)^2 + 2a(75)$$
$$0 = 900 + 150a$$
$$a = -6 \text{ m/s}^2$$

The acceleration is −6 m/s² (negative because it opposes the motion).

**7. A ball is thrown downward from a bridge with an initial velocity of 5 m/s. The bridge is 45 meters high. How long until the ball hits the water below?**

Using Equation 4 with downward as positive:
$$45 = (5)t + \frac{1}{2}(9.80)t^2$$
$$45 = 5t + 4.9t^2$$
$$4.9t^2 + 5t - 45 = 0$$

Using the quadratic formula:
$$t = \frac{-5 + \sqrt{25 + 4(4.9)(45)}}{2(4.9)} = \frac{-5 + \sqrt{25 + 882}}{9.8} = \frac{-5 + 30.1}{9.8} = 2.56 \text{ seconds}$$

(We take the positive root; time cannot be negative.)

### Challenge: Deeper Reasoning

**8. Two objects are dropped from the same height. One is dropped from rest; the other is thrown downward with some initial velocity. Both experience the same constant acceleration (gravity). How does the kinematic equation for displacement reflect the difference between them?**

The equation is $d = v_0 t + \frac{1}{2}at^2$. The first term, $v_0 t$, captures the head start the second object gets. Over the same time interval, the second object travels farther because it started with a velocity boost. But both experience the same gravitational acceleration, so the $\frac{1}{2}at^2$ term is identical for both.

**9. Why is it possible to use Equation 5 ($v^2 = v_0^2 + 2a(d - d_0)$) to find a velocity without knowing the time, while Equation 4 ($d = d_0 + v_0 t + \frac{1}{2}at^2$) requires time to find displacement?**

Equation 5 was derived by eliminating time from Equations 3 and 4. It works because displacement and velocity are related through acceleration: if you know how far you've traveled and how fast you're accelerating, the final velocity is determined regardless of how long it took. Equation 4, by contrast, directly connects displacement to time; there's no way to avoid time if you want displacement.

---

## Chapter Summary

**What you can now do:**

- Explain acceleration as a change in velocity, whether that change is in speed, direction, or both.
- Calculate average acceleration given initial velocity, final velocity, and elapsed time.
- Choose the appropriate kinematic equation based on what you know and what you're trying to find.
- Predict the position and velocity of an object moving under constant acceleration.
- Apply these equations to free-fall problems, including objects thrown upward.
- Graph motion (position, velocity, and acceleration versus time) and extract information from those graphs.

**One key idea:**

The kinematic equations are not arbitrary. They follow from the definition of acceleration and the assumption of constant acceleration. Once you understand that $a = \Delta v / \Delta t$, and you draw out the logical consequences, the five equations appear naturally.

**One common mistake:**

Forgetting to check that your answer is reasonable. A car braking to a stop shouldn't take 100 seconds. A baseball thrown at 50 m/s shouldn't travel 10 kilometers. A moment of common sense often catches errors that slipped through the algebra.

---

## Connections Forward

The next chapter asks: what *causes* acceleration? We've described how to measure it and predict an accelerating object's motion. But why does an object accelerate? That's where forces enter the picture. Newton's second law ties acceleration to the forces acting on an object, and suddenly the kinematic equations become tools for understanding why things move the way they do. Acceleration, it will turn out, is the consequence of force and mass, not the cause.

---

## Calibration

**What would change my mind:** If I discovered that constant acceleration was a worse assumption than I've stated, or if there were a simpler way to introduce the kinematic equations that didn't require this much algebra. I'm satisfied with the derivation—it shows the machinery—but I'm open to a clearer pedagogical path.

**Still puzzling:** I would like a more intuitive explanation for why the $\frac{1}{2}$ appears in the displacement equation for constant acceleration. I can derive it, and I can sketch it graphically, but I haven't yet found a way to explain it that makes it feel inevitable rather than algebraically correct.

---

## Tags

`acceleration`, `kinematics`, `constant-acceleration`, `free-fall`, `velocity`, `motion-in-one-dimension`
---

## LLM Exercise — Chapter 3: Acceleration (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the free-fall demo — Galileo's claim that g is mass-independent, tested with what's on hand.
**Tool:** **Claude Project** for the entry. Phone for video at 60 fps.

---

**The Prompt:**

```
Chapter 3 demo. Notebook in this Claude Project. Chapter 3 taught:
acceleration as the rate of change of velocity; the four kinematics
equations for constant acceleration; free fall (gravity acceleration
g ≈ 9.8 m/s² ignoring air resistance); terminal velocity (when air
drag balances weight, acceleration goes to zero).

**The Demo:** Drop two objects of very different mass from the
same height. If g is mass-independent (as the chapter claims),
they should hit the ground simultaneously.

**Materials:**
- Two objects with very different masses but similar shapes:
  e.g., a golf ball and a ping-pong ball; or two identical bottles
  one filled with water, one empty.
- A height: 2-3 meters (a stairway, an indoor balcony, or
  reaching up above your head).
- Phone with slow-motion video (60 fps minimum; 240 fps if
  available).

**Procedure:**

1. Drop both objects simultaneously from the same height. Record
   slow-mo video.

2. Run 5 trials. Note any trial where one object obviously slipped
   from your hand earlier than the other; discard those.

3. Analyze: in each frame of slow-mo, mark each object's position.
   Determine the frame each one hits the ground.

**Predicted result:** They hit at the same time within ~1 frame
(at 60 fps, that's 17 ms — about 2 cm of fall difference at the
end of a 2 m drop, which the eye won't catch).

**Variation: introduce air resistance.** Drop a flat sheet of
paper alongside a balled-up sheet of paper. The flat sheet hits
significantly later. Why? Where does the chapter's "neglect air
resistance" assumption break? Galileo would smile.

**Use Claude as a thinking partner:**
- Before: "Predict the difference in landing times for a golf
  ball and a ping-pong ball dropped from 2 m, with air resistance
  considered. Should I be able to detect the difference at 60 fps?"
- After: "Here's my data. Did the ping-pong ball lag the golf
  ball measurably? If yes, by how much? If no, what does that say
  about the strength of air-resistance effects at this scale?"

**Compute g from the drop time.** From d = (1/2)gt², if you know
d and t, you can solve for g. Check whether your measurement is
close to 9.8 m/s². Any discrepancy: timing error, air resistance,
or a measurement issue?

**Notebook entry should include:**
- Materials with photo.
- Pre-demo prediction.
- Data: drop times for each object across trials.
- The computed g and its uncertainty.
- The "with air resistance" variation and what changed.
- One physical effect you noticed that the chapter didn't
  mention.

End with the question: under what real-world condition would the
"all objects fall at the same rate" claim FAIL spectacularly?
(Hint: think about Felix Baumgartner's stratosphere jump.)
```

---

**What this produces:** A demo entry with measured drop times, computed g, and the "air resistance" variation. The discrepancy between the textbook's frictionless prediction and your real measurement is itself the lesson.

**How to adapt this prompt:**

- *For your own project:* If you can't get to 2-3 m of drop height, use a 1-m height with a phone clip stand for camera stability. The differential time is harder to detect but still possible.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* For video analysis, Claude Code can produce a frame-by-frame tracker.
- *For a Claude Project:* Append entry.

**Connection to previous chapters:** Ch 2's video-analysis discipline; Ch 3's free-fall is the canonical kinematics application.

**Preview of next chapter:** Chapter 4 is forces and Newton's laws. You'll build a setup to measure force, mass, and acceleration directly — pulley + weight + cart-on-a-table — and confirm F = ma.


---

## AI Wayback Machine

**Christiaan Huygens** worked out the formulas for centripetal acceleration and the period of a pendulum in the 1650s.

**Run this:**

```
Who is Christiaan Huygens, and how does their work connect to acceleration we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Christiaan Huygens"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Christiaan Huygens's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Christiaan Huygens's framework."

What changes? What gets better? What gets worse?
