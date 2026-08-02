# Chapter 6 — Newton's Laws of Motion

## Title candidates

1. **Why Things Move: The Three Laws That Run the Universe**
2. **Force, Mass, and the Machinery of Motion**
3. **Newton's Three Laws — From Apples to Spacecraft**

---

## TL;DR

In 1666, during the plague years at Cambridge, Isaac Newton figured out that motion does not need a reason to continue — inertia is the default. What *does* require a reason is *change* in motion. Force is the cause; acceleration is the effect; mass is the resistance. These three laws, stated as simple equations, describe how everything from a falling apple to a Falcon 9 rocket actually behaves.

---

## Cold open — Boca Chica, Texas, April 2016

The Falcon 9 first stage cuts its engines at 2,000 meters. Twelve seconds remain before impact. The rocket is falling nearly straight down at 235 meters per second — about 530 miles per hour — when the center engine reignites. Not to stop the fall entirely. To control it. The question Newton solved 350 years ago becomes practical: what force, applied over what distance, makes a 30-ton metal cylinder kiss a 100-by-50-meter drone ship at 1.5 meters per second instead of 235?

The Merlin engine produces 76,000 pounds of thrust straight upward. Gravity pulls downward with a force of 300,000 pounds. The net force is downward — 224,000 pounds pulling the rocket toward the ocean. By Newton's second law, $\sum \vec{F} = m\vec{a}$, that net force produces a downward acceleration of about 10 meters per second squared. The rocket is still accelerating downward. Still falling. But now the downward acceleration is less than the downward velocity — the rocket is *slowing down*. The numbers have to be exact. Too much thrust and the rocket overshoots the ship. Too little and it crashes. The computer running the engine adjusts the throttle 10 times per second, keeping the net force — and thus the acceleration — precisely balanced. 

At 10 centimeters altitude, the legs touch. At 1.5 meters per second, the stage comes to rest.

This is not an accident of engineering. It is Newton working.

---

## Learning objectives

By the end of this chapter you will be able to:

- **State** Newton's three laws of motion and explain what each one actually means.
- **Distinguish** inertia from mass, and weight from mass.
- **Draw** free-body diagrams and use them to apply Newton's second law in component form.
- **Identify** action-reaction pairs and explain why they don't cancel.
- **Calculate** the net force, acceleration, or mass in systems with multiple forces acting in different directions.
- **Predict** how the motion of an object changes when the net force on it changes.

---

## Prerequisites

Vectors at the level of components (Chapter 2). Calculus: the notion that $a = dv/dt$ and understanding what a derivative means conceptually. Kinematics from Chapter 4 — the definitions of velocity and acceleration and how to use constant-acceleration equations.

---

## Why this chapter matters

Everything that moves obeys Newton's laws. Your car, a baseball, a satellite, blood flowing through your arteries, the Moon orbiting Earth, a building standing still against the wind — all of them are governed by the relationship between force and motion. This chapter introduces the framework that physicists and engineers use to *predict* motion from forces, and vice versa: given the forces on an object, compute what it will do; given what an object does, infer what forces must be acting.

The Falcon 9 landing is one example. Bridge design, structural safety, collision testing, medical devices (from hip replacements to pacemakers), robotics, any machine where the outcome matters — all of them use Newton's laws to answer the same question: what forces produce this motion? The method is not sophisticated. The power is in understanding what it actually *means*.

---

## Concept 1 — Newton's First Law: Inertia and the Default State of Motion

### The scene

You are in an airplane cruising at 35,000 feet, 500 miles per hour. You are sitting still in your seat. Your coffee is sitting still on the tray table. To you, standing on the ground below looking up, both you and the coffee are moving at 500 mph. To a passenger across the aisle, both you and the coffee are at rest. Who is right?

Both. Motion is not absolute. Motion is relative to your frame of reference — the coordinate system you choose to measure from.

But here is the deeper thing Newton noticed: *in the absence of forces, an object in motion stays in motion at constant velocity, and an object at rest stays at rest*. You were not moving relative to the airplane. The airplane maintained its motion without any force pushing it forward every instant. The engines are burning fuel, yes — but once the plane reached 500 mph, the engines produce just enough thrust to balance air resistance and gravity, resulting in zero net force. Balanced forces. Constant velocity. Newton's first law, working.

### The law itself

$$\vec{v} = \text{constant when } \sum \vec{F} = \vec{0}$$

If the net force on an object is zero, the object's velocity does not change. A body at rest remains at rest. A body in motion remains in motion at the same speed, in the same direction, unless a net external force acts on it.

This is *inertia* — the resistance of an object to changes in its state of motion. The word comes from Latin *iners*, sluggish. But inertia is not laziness. It is a law of nature. A boulder has more inertia than a basketball because a boulder requires a larger force to change its velocity. The measure of inertia is mass.

### The key specification: inertial reference frames

Newton's first law does not apply everywhere. In a reference frame that is itself accelerating, the law fails. If you are in a car that suddenly brakes hard, you pitch forward not because a force pushed you forward, but because the car's frame of reference is accelerating backward relative to the ground. To Newton's first law, what matters is an *inertial reference frame* — a frame that is either at rest or moving at constant velocity relative to the distant, fixed stars.

For most problems on Earth, we can treat the ground as an inertial frame. Earth does rotate on its axis and orbit the Sun — both accelerations — but the effects are tiny (about 0.03 m/s² at the equator). For the motion of cars, planes, and buildings, this tiny acceleration is negligible. We use Earth's frame as inertial unless we are dealing with long-range ballistics or satellite motion.

In contrast, a reference frame attached to a spinning carousel is not inertial. Objects appear to accelerate sideways even when no sideways force acts on them. The frame itself is rotating.

### How do we see inertia in action?

**Air hockey.** When the air is on, the puck glides across the table, sliding for meters with barely any slowing. When the air is off, friction acts on the puck, slowing it to a stop in a few meters. The puck "wants" to keep moving. Friction is the force that changes that.

**A skydiver opening a parachute.** Before the parachute opens, the skydiver is accelerating downward (gravity pulling down, air resistance small). At the moment the parachute deploys, air resistance becomes huge, much larger than weight. The net force reverses — now pointing upward. The skydiver decelerates (negative acceleration) and after a few seconds, reaches a terminal velocity: the parachute's air resistance now balances weight, net force is zero, and the skydiver floats downward at constant 5 m/s.

**A car hitting a wall.** The car stops. The driver, following Newton's first law, does not. The driver's inertia carries them forward at the car's original velocity until the seatbelt (a force) stops them.

### Worked example — the truck and the cargo

A truck is traveling down the highway at constant velocity with a loose crate of oranges in the back. The truck suddenly brakes hard, decelerating at 7 m/s². What happens to the crate?

The crate is in the truck's reference frame. When the truck brakes, the truck's frame is now accelerating backward (decelerating forward). In this non-inertial frame, the crate experiences a fictitious force pushing it forward. In reality, the crate has inertia. Its velocity was the truck's velocity — 70 km/h. The truck's bed exerts a friction force on the crate, slowing it down. But during the brief moment of hard braking, that friction is not enough to match the truck's deceleration. The crate slides forward relative to the truck. If the crate is not secured, it will slide right off the front of the bed.

In the ground (inertial) frame, it is clearer: the crate was moving at 70 km/h. The friction force from the truck's bed is the only horizontal force on the crate. That friction can provide maybe 0.7g of deceleration (if the coefficient of static friction is 0.7). But the truck is decelerating at 0.71g. The crate cannot decelerate as fast as the truck. It slides forward relative to the truck's frame, even though in the ground frame it is decelerating — just not as quickly as the truck.

### Common misconceptions

**"Inertia is a force."** No. Inertia is a *property* — the tendency of an object to resist changes in motion. Force is what overcomes inertia.

**"Something needs to keep pushing for motion to continue."** No. Once moving, an object continues at constant velocity with zero force applied. This contradicts everyday experience (a ball rolled on the ground slows down) because friction is acting. Friction is a force. In a frictionless environment — or in space — motion continues without any push.

**"Gravity must keep the Moon orbiting Earth."** Gravity does act on the Moon, but not to *keep it moving* in orbit. Gravity changes the *direction* of the Moon's velocity, constantly redirecting its motion in a circle. The Moon is not following its first-law straight-line path because gravity is pulling it away from that path. This is important: gravity provides the force that changes the Moon's motion, not the force that sustains it.

---

## Concept 2 — Newton's Second Law: Force, Mass, and Acceleration

### The scene

A student pushes a shopping cart through the grocery store. One hand on the handle, steady force. The cart accelerates. Add another 5 kg of groceries and push with the same force: the cart accelerates more slowly. Push twice as hard with the same empty cart: the cart accelerates twice as fast.

These observations — that larger forces produce larger accelerations, and that larger masses produce smaller accelerations for the same force — were so consistent that Newton wrote them down as a proportionality: $\vec{a} \propto \vec{F}_{\text{net}}$ and $a \propto 1/m$. Combine them and you have Newton's second law.

### The law itself

$$\sum \vec{F} = m\vec{a}$$

Or, in the form Newton actually stated it (which is even more powerful):

$$\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt}$$

where $\vec{p} = m\vec{v}$ is momentum — the product of mass and velocity. This says: the net force on an object equals the *rate of change* of its momentum. Acceleration is the rate of change of velocity. When mass is constant, the two forms are equivalent:

$$\vec{F}_{\text{net}} = m\frac{d\vec{v}}{dt} = m\vec{a}$$

### The vector nature — three equations in disguise

Newton's second law is a *vector* equation. It is really three scalar equations, one for each direction:

$$\sum F_x = ma_x, \quad \sum F_y = ma_y, \quad \sum F_z = ma_z$$

If the forces are all aligned along one direction (say, pushing a cart along the ground), you can work with magnitudes: $F_{\text{net}} = ma$. If forces point in different directions, you *must* resolve them into components. This is why free-body diagrams are the essential tool of applied mechanics — they let you see which forces point where.

### The units — defining the newton

We defined force as a push or pull. But how big is a force? The newton (symbol N) is the SI unit of force. Its definition comes directly from Newton's second law:

$$1 \text{ N} = 1 \text{ kg} \cdot \text{m/s}^2$$

One newton is the force required to accelerate a 1-kg mass at 1 m/s². A small apple (100 grams) weighs about 1 N on Earth. Your weight in newtons is your mass in kilograms times 9.8 m/s². A 70-kg person weighs about 686 N.

### Worked example — the rocket sled

A rocket sled for testing acceleration equipment carries a 2,100-kg payload. The sled experiences a forward friction force of 650 N from the rails and a total thrust from four rockets of magnitude $4T$ (where $T$ is the thrust per rocket). If the sled's initial acceleration is 49 m/s², what is the thrust of each rocket?

Given: $m = 2100$ kg, $f = 650$ N (friction), $a = 49$ m/s².

The net force is the forward thrust minus friction:
$$F_{\text{net}} = 4T - f$$

Applying Newton's second law:
$$F_{\text{net}} = ma$$
$$4T - f = ma$$
$$4T = ma + f = (2100 \text{ kg})(49 \text{ m/s}^2) + 650 \text{ N}$$
$$4T = 102,900 + 650 = 103,550 \text{ N}$$
$$T = 25,887 \text{ N} \approx 2.6 \times 10^4 \text{ N}$$

Each rocket produces about 26,000 newtons of thrust. Tests like this, conducted in the 1960s, exposed human subjects to accelerations of 45 *g* (45 times Earth's gravity) to understand the limits of human physiology during jet-fighter ejections. The results informed safety equipment design that has saved lives.

### The deep mechanism: why does this work?

Why is $\sum \vec{F} = m\vec{a}$ true? Because it *defines* force and mass and their relationship. Newton did not derive this from first principles. He observed that this relationship predicted motion across an enormous range of scales — from the fall of an apple to the orbit of the Moon — and stated it as a law. The validity of the second law is *experimental*. We know it is true because every prediction it makes has been verified, and no experiment has ever contradicted it. (Relativity and quantum mechanics refine it at extreme speeds and scales, but Newtonian mechanics remains correct for everyday speeds and sizes.)

The secret power of the second law is that it is a *differential equation*. When you write $F = m\frac{dv}{dt}$, you are connecting the instantaneous force on an object to how its velocity is changing at that instant. If you know the force as a function of time — the *input* — you can solve the differential equation to find velocity and position as functions of time — the *output*. This is how engineers design the Falcon 9 landing sequence. They know the rocket's mass, the thrust available, and gravity. Newton's second law becomes the equation of motion. The computer solves it at every instant, adjusting thrust to keep the net force pointing downward with just the right magnitude.

### Worked example — free-body diagram and component form

A 0.4-kg soccer ball is kicked by a player. As it leaves the foot, the ball experiences an acceleration $\vec{a} = 3.0\hat{i} + 7.0\hat{j}$ m/s² (3 m/s² to the right, 7 m/s² upward). What is the net force on the ball?

Using Newton's second law in vector form:
$$\vec{F}_{\text{net}} = m\vec{a} = (0.4 \text{ kg})(3.0\hat{i} + 7.0\hat{j} \text{ m/s}^2) = 1.2\hat{i} + 2.8\hat{j} \text{ N}$$

The magnitude is:
$$F_{\text{net}} = \sqrt{(1.2)^2 + (2.8)^2} = \sqrt{1.44 + 7.84} = \sqrt{9.28} = 3.0 \text{ N}$$

The direction is:
$$\theta = \tan^{-1}\left(\frac{2.8}{1.2}\right) = \tan^{-1}(2.33) = 67°$$

The net force is 3.0 N at 67° above the horizontal.

Notice: to find the net force, we did not need to know the individual forces (foot push, gravity, air resistance). The acceleration *encodes* all of them. This is the utility of Newton's second law — it connects cause (net force) to effect (acceleration) without requiring us to dissect every force.

### Common misconceptions

**"Constant velocity means zero force."** Wrong. Constant velocity means zero *net* force. An airplane in level flight has thrust, drag, weight, and lift all acting on it. But when cruising steadily, these forces add to zero.

**"Heavy objects fall faster than light ones."** This is Aristotle's mistake. All objects on Earth fall with the same acceleration (about 9.8 m/s² in the absence of air resistance) because gravity acts on the object in proportion to its mass. A heavier object experiences proportionally larger gravitational force, so $a = F/m = (m \cdot g)/m = g$, independent of mass. Air resistance breaks this, which is why a feather falls slower than a hammer in air but at the same rate in a vacuum.

**"Force times velocity gives acceleration."** No. Force divided by mass gives acceleration: $a = F/m$. Velocity is irrelevant to the acceleration. A car at 10 mph requires the same force to gain 5 mph as a car at 60 mph (ignoring air resistance). What changes with velocity is the power (energy per second) required, not the force.

---

## Concept 3 — Newton's Third Law: Action and Reaction, and Why They Don't Cancel

### The scene

You are standing on a skateboard on a frictionless ice rink. You push against a wall with all your strength, and the wall pushes back. You accelerate away from the wall. The wall does not accelerate — it is attached to the Earth, which is vastly more massive. But the wall *does* push back on you with a force equal and opposite to your push on the wall.

This is Newton's third law: for every action, there is an equal and opposite reaction.

A rocket engine ejects hot gas downward at high velocity. By Newton's third law, that gas exerts an equal and opposite force upward on the rocket. The rocket does not push on the ground or the air (though the rocket is sitting in air). The rocket works in a vacuum more efficiently than in the atmosphere because it can expel gas more readily. The action is the rocket pushing gas backward. The reaction is the gas pushing the rocket forward.

### The law itself

If body A exerts a force $\vec{F}$ on body B, then body B simultaneously exerts a force $-\vec{F}$ (equal in magnitude, opposite in direction) on body A:

$$\vec{F}_{AB} = -\vec{F}_{BA}$$

These forces are called an *action-reaction pair*. They are equal in magnitude, opposite in direction, and *act on different bodies*.

### Why don't they cancel?

This is the most commonly misunderstood aspect of Newton's third law. Here is the key: the two forces act on different objects. In a free-body diagram, which shows all forces on *one* object, you never include both forces of an action-reaction pair. You include only the forces acting on the object you are analyzing.

Consider a book resting on a table. The Earth pulls down on the book with a gravitational force $\vec{F}_{E \to B}$. By the third law, the book pulls up on the Earth with force $-\vec{F}_{E \to B}$. These are equal and opposite, but they act on different objects (book vs. Earth). The book does not float away because the *table* pushes up on the book with a normal force $\vec{F}_{T \to B}$. The table pushes up, the Earth pulls down, and if these are balanced, the book is at rest. The third-law pair to "Earth pulls down" is "book pulls up on Earth," not "table pushes up." The third-law pair to "table pushes up" is "book pushes down on table."

### Worked example — the professor and the cart

A 65-kg physics professor stands behind a cart (mass 12 kg) loaded with equipment (mass 7 kg). The professor pushes backward on the floor with a force of 150 N. By Newton's third law, the floor pushes forward on the professor's shoes with 150 N. The professor, cart, and equipment move together with total mass 84 kg.

What is the acceleration of the system? (Assume friction opposing the motion totals 24 N.)

The system of interest is the professor + cart + equipment. The external forces are:
- Floor pushing forward: 150 N
- Friction opposing: 24 N
- Net force: 150 − 24 = 126 N

By Newton's second law:
$$a = \frac{F_{\text{net}}}{m} = \frac{126 \text{ N}}{84 \text{ kg}} = 1.5 \text{ m/s}^2$$

Notice: the professor pushes backward on the floor. The floor pushes forward on the professor. These are action and reaction. The professor accelerates because the floor's push (the reaction) acts *on the professor*. The professor's push acts on the floor, which doesn't accelerate because the floor is attached to the Earth.

Now, suppose we ask: what force does the professor exert on the cart? This is not an action-reaction pair with any force we have identified. Instead, we change our system. If we consider only the cart + equipment (mass 19 kg), the forces are:
- Force from professor: $F_p$ (unknown)
- Friction opposing: 24 N
- Net force: $F_p − 24$

The acceleration is still 1.5 m/s² (the professor, cart, and equipment move together). Thus:
$$F_p - 24 = (19)(1.5) = 28.5 \text{ N}$$
$$F_p = 52.5 \text{ N} \approx 53 \text{ N}$$

The professor exerts 53 N on the cart, much less than the 150 N she exerted on the floor. Some of her push accelerates her own body. The choice of system is crucial — it determines which forces are external (and thus included in Newton's second law) and which are internal (and thus cancel out).

### Three examples where Newton's third law is the point

**A swimmer pushing off a pool wall.** The swimmer pushes backward on the wall with force $F$. By Newton's third law, the wall pushes forward on the swimmer with force $F$. The swimmer accelerates forward because of the wall's push. The wall does not accelerate backward (it is attached to the pool and the Earth) even though the swimmer pushes on it. The asymmetry is in the masses, not in the laws.

**A bird flying.** The bird's wings push air downward. By Newton's third law, the air pushes the bird upward. This upward push is lift. The bird creates lift by shoving air downward, not by "pulling" at the air above it.

**A rocket taking off.** The rocket engine ejects hot gas downward at high velocity. The rocket pushes on the gas; the gas pushes on the rocket. The force on the gas is huge (to accelerate it to such high velocity). By Newton's third law, the force on the rocket is equally huge and points upward. This is thrust.

### Common misconceptions

**"Action and reaction cancel, so they don't affect motion."** They cancel out *if they act on the same object*, which they never do. Each force acts on a different object and can produce motion of that object.

**"The wall doesn't push back as hard as you push on it."** Yes, it does. If you push the wall with 100 N, the wall pushes back on you with 100 N. The wall does not accelerate because it is supported by the Earth (which is massively more inert). But the force is equal.

**"Heavier objects exert more force when they fall on lighter ones."** No. During a collision, the forces are equal and opposite. A truck and a bicycle collide head-on. By Newton's third law, each exerts an equal and opposite force on the other. But the truck's 2,000-kg mass accelerates much less than the bicycle's 20-kg mass. The damage to the bicycle is far worse, not because of a larger force, but because of the vast difference in accelerations: the bicycle's acceleration is 100 times larger.

---

## Integration — the machinery visible

Return to the Falcon 9 first stage, that moment at 10 centimeters altitude. The rocket has mass $m \approx 30,000$ kg and velocity $v = 1.5$ m/s downward. The engine thrust is $T \approx 76,000$ N upward. Gravity pulls with force $W = mg \approx 294,000$ N downward. The net force is:

$$F_{\text{net}} = T - W = 76,000 - 294,000 = -218,000 \text{ N}$$

(Negative means downward, in the direction of motion.)

By Newton's second law:
$$a = \frac{F_{\text{net}}}{m} = \frac{-218,000}{30,000} \approx -7.3 \text{ m/s}^2$$

The rocket is accelerating downward at 7.3 m/s², but its velocity is only 1.5 m/s downward. Velocity is decreasing — the rocket is slowing. The instantaneous deceleration (in the colloquial sense of "slowing down") is about 0.2 m/s per 1/30th of a second. The landing leg touchdown is gentle.

This is Newton's second law controlling the Falcon 9. The engineers know the payload mass, the engine capabilities, and Earth's gravity. They solve Newton's second law millions of times per flight, each solution valid for a fraction of a second, each adjustment of thrust correcting for the changing mass (the rocket is burning fuel) and the changing acceleration. The differential equation $m\frac{dv}{dt} = T - mg$ (where thrust $T$ is a function of time) becomes the flight program.

Newton never saw a Falcon 9. But the machine obeys his laws exactly.

---

## Synthesis

The three laws form a complete framework.

**Newton's first law** says: motion does not need a reason. Once an object is in motion, it continues unless a force stops it. This seems counterintuitive because we live in a world of friction, air resistance, and other forces that constantly oppose motion. But in the absence of forces, inertia alone determines motion. The law defines inertial frames — frames in which the law holds — and clarifies that we live in one.

**Newton's second law** says: forces change motion. The change is measured as acceleration, and it is proportional to the net force and inversely proportional to the mass. This law is quantitative. It lets us *predict* motion given the forces, and *infer* forces given the motion. It is the equation of motion for every machine and every natural process that involves forces.

**Newton's third law** says: forces always occur in pairs. You cannot exert a force without experiencing one back. This law is about symmetry in nature — the universe does not give one object the power to push without receiving a push back. It clarifies system boundaries: when you pick a system to analyze, internal forces (between objects within the system) cancel, but external forces (from outside) drive the system's motion.

Together, these laws do what the best explanations do: they reduce a vast collection of seemingly different phenomena — a falling apple, a swimming pool push-off, a rocket launch, a car skidding, a building standing against the wind — to a single, simple machinery. The machinery is: net force equals mass times acceleration. That equation, solved again and again in infinitesimal time steps, describes the trajectory of everything that moves.

What would change my mind: If any experiment showed a case where $\sum \vec{F} \neq m\vec{a}$ in an inertial frame, at speeds much less than light, for objects much larger than atoms, the second law would need revision. This has never happened. The law has survived 350 years of experimental scrutiny.

Still puzzling: Newton's third law states that action and reaction are always equal. But where is the "delay"? If body A exerts a force on body B, does body B *instantly* exert a force back, or is there a finite time lag? Classical mechanics says instantly, but relativity suggests that information cannot travel faster than light. This apparent paradox is resolved in quantum field theory, where forces are mediated by particles (photons, for example), which do propagate at the speed of light. But at scales and speeds where Newtonian mechanics applies, the question does not arise — the interactions happen so fast that we cannot measure the lag.

---

## Exercises

### Warm-up

**Exercise 6.1** *(LO: First law and equilibrium).* A 1,500-kg car is traveling at constant velocity down the highway at 90 km/h. (a) What is the net force on the car? (b) If the engine produces a forward force of 1,200 N on the wheels, what force opposes the motion? (c) What happens to the car when the engine shuts off?

**Exercise 6.2** *(LO: Second law, magnitude form).* A 4.5-kg shopping cart is pushed with a net force of 60 N along a smooth, level floor. (a) What is the cart's acceleration? (b) If pushed for 3 seconds starting from rest, how far does the cart travel?

**Exercise 6.3** *(LO: Second law, weight and mass).* A 70-kg person stands on Earth. (a) Calculate their weight in newtons. (b) On the Moon, where $g = 1.62$ m/s², what would be their weight? (c) Does their mass change on the Moon?

**Exercise 6.4** *(LO: Free-body diagram and components).* A book of mass 2 kg sits on an inclined plane tilted at 30° to the horizontal. (a) Draw a free-body diagram showing the weight, the normal force, and any other relevant forces. (b) Resolve the weight into components parallel and perpendicular to the plane. (Ignore friction for now.)

**Exercise 6.5** *(LO: Third law, action-reaction).* A swimmer pushes off a pool wall with a force of 800 N. (a) By Newton's third law, what force does the wall exert on the swimmer? (b) Why does the swimmer accelerate away from the wall but the wall does not accelerate backward?

### Application

**Exercise 6.6** *(LO: Second law, two-dimensional forces).* A 10-kg object is subject to two forces: $\vec{F}_1 = 30\hat{i}$ N and $\vec{F}_2 = 40\hat{j}$ N. (a) Find the net force in vector form. (b) Find the magnitude and direction of the net force. (c) Calculate the acceleration.

**Exercise 6.7** *(LO: System choice and Newton's second law).* A 65-kg person pulls a 15-kg box across a floor using a rope. The tension in the rope is 100 N, and friction on the box is 20 N. (a) What is the acceleration of the box? (b) What force does the floor exert on the person's feet (the normal force in the horizontal direction, ignoring weight)?

**Exercise 6.8** *(LO: Equilibrium and vector addition).* Three ropes are attached to a ring. One rope pulls with 100 N to the north. A second pulls with 80 N at 30° west of north. A third rope pulls with unknown force and direction. For the ring to be in equilibrium, what must be the magnitude and direction of the third rope?

### Synthesis

**Exercise 6.9** *(LO: Multiple objects and constraint forces).* Two blocks are at rest and in contact on a frictionless surface. Block A has mass 2 kg; Block B has mass 6 kg. A horizontal force of 32 N is applied to Block A, pushing it and Block B together. (a) What is the acceleration of the system? (b) What force does Block A exert on Block B? (Hint: draw separate free-body diagrams for each block.)

**Exercise 6.10** *(LO: Newton's laws in multiple dimensions).* A 0.5-kg ball is kicked from ground level. At the moment it leaves the foot, it has acceleration $\vec{a} = 20\hat{i} + 30\hat{j}$ m/s² (20 m/s² horizontal, 30 m/s² upward). (a) Find the net force on the ball in vector form. (b) The ball's weight is about 5 N downward. What must be the total contact force from the foot (magnitude and direction)?

### Challenge

**Exercise 6.11** *(LO: Open-ended — designing for motion).* A spacecraft uses ion thrusters that produce a small, constant force of 0.05 N. The spacecraft's mass is 500 kg. (a) What is the spacecraft's acceleration in deep space (far from any gravitational field)? (b) If the thruster operates continuously for 30 days, what will be the spacecraft's velocity change? (c) Why is this tiny acceleration useful for spacecraft, even though it would be negligible for a car on Earth?

**Exercise 6.12** *(LO: Model a real situation — the parachute descent).* A 70-kg person with a parachute jumps from a plane. Initially (parachute closed), they experience a net downward force of about 50 N (weight minus air resistance). After deploying the parachute, air resistance becomes 700 N upward. (a) What is the net force and acceleration immediately after parachute deployment? (b) After 5 seconds of descent with the parachute open, what is the velocity? (c) As the descent continues, what happens to the air resistance if the velocity changes? At what velocity will the person reach constant descent speed (terminal velocity)?

---

## Chapter summary

You can now do five things you probably could not do before.

You understand what *inertia* actually means: the tendency of an object to maintain its state of motion, not a force. You know that motion at constant velocity requires zero net force, and you can identify systems in equilibrium by checking whether the vector sum of forces is zero.

You can apply Newton's second law quantitatively. Given forces, you calculate acceleration. Given acceleration and mass, you infer forces. You can resolve forces into components, write the second law separately for each direction, and solve systems where forces point in different directions.

You understand the difference between mass and weight. Mass is the measure of inertia — how much an object resists acceleration. Weight is the gravitational force on that mass. On Earth, a 100-kg object weighs about 980 N. On the Moon, it weighs about 160 N. But its mass is still 100 kg.

You know why action-reaction pairs do not cancel: they act on different objects. You can use this understanding to identify external versus internal forces when choosing a system to analyze.

You have seen the machinery of motion. Newton's second law is a differential equation. Solve it (even numerically, step by step, as a computer does) and you predict how any object moves under any force. The Falcon 9 landing, a ball's trajectory, the orbit of the Moon, the design of a bridge's support structure — all of it flows from $\sum \vec{F} = m\vec{a}$.

---

## Connections forward

Chapter 7 applies these laws to specific forces: friction, air resistance, tension in ropes, and the centripetal force required for circular motion. The laws themselves do not change — but the *context* changes. What is the friction force? How does it depend on the normal force? These are the questions of applied mechanics.

Chapter 9 introduces momentum and collisions. Newton's second law in the form $\vec{F} = d\vec{p}/dt$ becomes the foundation: the impulse (force times time) is the change in momentum. This leads to the law of conservation of momentum — one of the most powerful tools in physics.

Chapter 13 introduces gravitational force as an application of Newton's laws. The force between two masses is not immediately obvious from the three laws themselves. But once gravity's force law is stated, Newton's second law predicts orbits, escape velocity, and the motion of the Moon and planets.

For now, understand this: Isaac Newton did not *discover* these laws by pondering. He observed. He measured. He noticed patterns. Then he stated them as simply as possible. The power of simplicity is that it applies everywhere. The same three laws describe a tennis ball and a star.

---

## Tags

Newton's laws, inertia, force and acceleration, free-body diagrams, mass and weight, action-reaction, systems, dynamics



---

## LLM Exercise — Chapter 6: Newton's-Laws Integrator

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A general Newton's-laws integrator — multiple bodies, multiple forces, with free-body diagrams as data structures. The framework every later dynamics chapter uses.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 6 task in the physics-simulation-toolkit. The chapter
established $\sum \vec{F} = m\vec{a}$ as the central equation.
Build a generic integrator that takes a list of bodies and a list of
force functions, integrates the system forward in time, and produces
trajectories.

In `chapters/ch06_newtons_laws/`:

1. `simulations.py`:
   - `class Body` — represents an object with mass, position, velocity,
     and an `id`. Position and velocity are 3D vectors (Ch 3).
   - `class Force` — represents a force, with a `compute(bodies, t)`
     method returning a dict mapping body id → force vector.
   - `class System` — holds a list of bodies and a list of force
     functions; has a `step(dt, integrator='rk4')` method.

2. Implement four canonical Force subclasses:
   - `ConstantForce(body_id, force_vec)` — useful for gravity
     approximation near surface.
   - `Gravity(g_vec=(0, -9.81, 0))` — applies to every body with mass.
   - `Spring(body_id_a, body_id_b, rest_length, k)` — Hooke's law
     between two bodies.
   - `Tension(rope_attachments, max_tension)` — constraint force
     (preview: real constraint solvers are Ch 11/12 territory).

3. `test_simulations.py`:
   - Atwood machine: two masses connected by a rope over a pulley.
     The system should accelerate at $a = (m_1 - m_2)g / (m_1 + m_2)$.
     Verify with several mass ratios.
   - Inclined plane: a block on a 30° incline (no friction yet — Ch 7
     adds that) slides down with $a = g \sin\theta$. Verify.
   - Free-body diagram round-trip: given a set of forces on a body,
     compute the net force and the resulting acceleration; verify that
     Newton's third law holds for every action-reaction pair the
     system contains.

4. `benchmarks.py` — measure performance scaling: 10 bodies, 100
   bodies, 1000 bodies (with pairwise spring interactions). Find the
   N where the simulation slows below 1000 steps/second on your
   machine.

5. `README.md` — four decision cards (one per Force type). "Surprising
   findings": the Atwood-machine analytical-versus-RK4 comparison
   should agree to many digits — flag any case where the agreement
   breaks down (usually small mass ratios with stiff dynamics).

Commit as `ch06: Newton's-laws integrator with multi-body force
system`.
```

**What this produces:** A generic multi-body Newton integrator, four canonical force types, Atwood and inclined-plane tests, and a performance scaling benchmark.

**How to adapt this prompt:**

- *For your own project:* Constraint solvers (for rigid bodies connected by rigid links) are real engineering. Bullet, Box2D, MuJoCo are the production-grade options. This exercise builds the educational version.
- *For ChatGPT / Gemini:* Both work. The object-oriented design varies; pick a style and stay consistent.
- *For Claude Code:* Native fit. Let it write the round-trip free-body test.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses the Ch 4-5 integrators. The free-body diagram becomes a list of Force objects in code.

**Preview of next chapter:** Chapter 7 adds friction, drag, and centripetal-force scenarios — including the Forces-on-a-loop and friction-coefficient experiments that match Bear's worked-example treatment.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Mary Somerville** was the 1831 book *Mechanism of the Heavens* — a translation, expansion, and explication of Laplace's *Mécanique Céleste* — which made Newton's laws applied to celestial mechanics accessible to English-language readers and was used as a Cambridge mathematics textbook for over a century — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Mary Somerville, and how does their work on the translation and explication of Laplace's celestial mechanics into English mathematical pedagogy connect to Newton's three laws of motion and how they were applied to celestial bodies in the century after Newton? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Mary Somerville"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one specific result from *Mechanism of the Heavens* — Somerville's analytical handling of planetary perturbations is a good example — and explain what made her explication clearer than Laplace's original
- Ask: "Somerville College Oxford was named after her in 1879, three years after her death. What was she barred from during her lifetime that the college her name attached to eventually granted?"
- Add the framing: "Answer as if you're writing the foreword to a 2026 facsimile edition of *Mechanism of the Heavens* aimed at modern mechanics students"

What changes? What gets better? What gets worse?
