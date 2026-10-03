# ACTS.md — Capstone: Ship a Full-Stack App (Film 11 of 12)

**Exact title:** Capstone: Ship a Full-Stack App

**Core promise:** By the end, the viewer has watched a real app go from idea
to running containers — backend doc, boring stack, goal-driven build, Docker
Compose ship, React on real endpoints — and knows the honest list of what is
still rough.

**Structure:** hook + key terms + three acts (10 body beats) + recap + your
turn + outro. 15 beats, 280 s (4m40s).

- **Hook (BIDEA):** this is the film where everything comes together — one
  idea, one backend doc, and at the end a real app running in containers.
- **Key terms (BDEFS):** Goal · Stack · Compose · Endpoint.
- **Act 1 — The plan (3 beats):** B01 the backend doc: a plan before code —
  what the app is, what it stores, what it answers; the doc is the contract;
  B02 the stack: Go, one VM, SQLite — boring on purpose; B03 raw SQL,
  deliberately — no ORM, queries you can read and debug.
- **Act 2 — The build (4 beats):** B04 the goal feature: a goal that
  decomposes into steps and drives the build; B05 watching the decomposition
  (endpoints, tables, auth, posts); B06 the build runs — the agent writes,
  you are the judgment; B07 the MVP stands — register works, posting works,
  the database fills.
- **Act 3 — The ship (3 beats):** B08 Docker Compose: backend, frontend,
  MinIO standing in for S3, one command; B09 React wired to real endpoints —
  not mock data; B10 the demo: register, post — and the honest list of what
  is still rough.
- **BVDT:** exactly 3 lines, one per act.
- **BHTF:** write one backend doc for an app you want; then ask the agent
  for the stack plan.
- **BOUT:** "Muse, in for Bear. Thanks for watching." + teaser for Film 12
  (Muse the Agent).

**Tone:** this is the payoff film — confident, builderly, honest. The demo
is real but the film never oversells it: the MVP is an MVP, and the rough
edges get named on screen.

**What this film is not:** not a Go tutorial (no syntax taught); not a
Docker Compose reference (one file, three services, that's the level); not
a victory lap — the rough list is part of the lesson.

**Cast per act (one look):** the plan is paper — doc cards, plates, stamps;
the build is motion — splitting dots, growing trees, writing glyphs; the
ship is boxes — service plates rising into a compose frame, arrows between
frontend and backend.

**Source facts:**
- Before code, the instructor scoped a backend doc: what the app is, what it
  stores, what it answers. (transcript §13; series plan Film 11 key beats)
- The stack: Go, single binary, SQLite on one VM. (transcript §13)
- Raw SQL, deliberately — no ORM. (transcript §13)
- The goal feature: decomposing a backend-build goal and driving the build
  autonomously. (transcript §13)
- Docker Compose: backend, frontend, MinIO standing in for S3. (transcript
  §13; series plan Film 11 key beats)
- React frontend wired to real endpoints. (transcript §13)
- The demo: registering and posting; an honest list of what is still rough.
  (series plan Film 11 key beats)

**LEFT OUT (with reasons):**
- Exact endpoint paths, table schemas, and compose-file contents — not in
  the outline; the film stays at the architecture level (one file, three
  services) rather than asserting unverified literals.
- The app's domain specifics beyond "a community app" — not verified; the
  film keeps the example generic.
- Go/SQL/Docker install or syntax instruction — the audience is assumed
  to know or to learn elsewhere; this film is about the build arc.
