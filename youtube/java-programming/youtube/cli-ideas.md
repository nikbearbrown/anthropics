# Java Programming — CLI Video Ideas ("X with Claude")

## Candidate 01 — Specify Before You Generate: The 5-Part Method Contract with Claude Code
- Source: java-programming/chapters/04-java-foundations-for-specification.md
- Lane: BUILD (Claude Code)
- Hook: The student got a number. The number was correct. The method divided by zero, rounded wrong, and changed the parameter type. None of that was visible from the output. Build the specification that makes violations visible before they ship.
- The artifact: A screen-recording of two Claude generations: (1) vague prompt → averaging method with 3 hidden violations; (2) full 5-part specification → method that passes all 5 audit steps. The audit is shown as an explicit checklist on screen, with each step checking off.
- Prompt seed: `claude "Write a Java method that computes the average of an array of scores."` [VAGUE — induces violations]. Then: `claude "Write a Java method: public static double averageScore(int[] scores). Preconditions: scores is not null. Postconditions: if scores.length == 0, returns 0.0; otherwise returns arithmetic mean using floating-point division; elements of scores are not modified. Failure behavior: throws IllegalArgumentException if scores is null. No other side effects."`
- Read / check: Verify vague version has at least one violation (empty-array crash is most common, then integer-division rounding); verify specified version returns 0.0 for empty array, uses floating-point division, does not sort or modify the array, and throws IllegalArgumentException for null.
- Human supplies: Screen-recording of the actual Claude terminal session showing both generations and the violation caught at audit step 2 (precondition check). Real execution required — synthetic code on slides misses the learning.
- Output medium: screen-recording mp4 (Onda terminal; 5-step audit checklist overlay; items check green as each step passes; the failing item on Version 1 turns red with the violation labeled)
- The change: Issue a third prompt asking Claude to add Javadoc — verify that Claude either inherits the spec into the Javadoc or fails to (a common gap: the Javadoc often reflects the vague original intent, not the refined specification).
- Teardown angle: The specification is not paranoia — it is the contract. Without it, "it works" means "it worked on the input I tested." With it, "it works" means "it satisfies every obligation I stated." That is the whole difference between a demo and a deliverable.
- Exclusions: No Java language history, no OOP theory, no IDE tour. One method, one specification, five audit steps.
- Score: 10/10

---

## Candidate 02 — Recursion That Doesn't Crash: The Three-Part Specification with Claude Code
- Source: java-programming/chapters/13-recursion-as-problem-decomposition.md
- Lane: BUILD (Claude Code)
- Hook: The file-counter works on the demo archive. On a real project directory with symlinks, the JVM throws StackOverflowError. The method is not wrong. The specification was incomplete. Build the three-part recursive spec that prevents the crash.
- The artifact: A screen-recording: (1) base-case + recursive-case specification → method that crashes on a symlinked directory; (2) three-part specification adding the termination invariant (visited-path Set) → method that handles cycles. The crash and the fix are shown in the same terminal session.
- Prompt seed: `claude "Write a Java method public int countFiles(File root). Base case: plain file returns 1. Recursive case: for each child of a directory, recurse and sum."` [CRASH-PRONE]. Then: `claude "Write a Java method public int countFiles(File root). Three-part specification: (1) Base case: root.isFile() returns 1; directory with no children returns 0. (2) Recursive case: for each child in root.listFiles(), recurse and sum; each recursive call receives a direct child (depth strictly increases). (3) Termination invariant: maintain a Set<String> of visited canonical paths passed through the call; if the next child's canonical path is already visited, skip it (return 0 for that branch). Throws IllegalArgumentException if root is null. Thread-safe is not required."`
- Read / check: Verify Method 1 lacks the Set and crashes on a symlinked directory; verify Method 2 uses File.getCanonicalPath() for cycle detection; verify the passed-Set pattern is used (or a shared-state alternative that is thread-safe-noted); verify root==null check throws IAE.
- Human supplies: A symlinked test directory (created with `ln -s`) to trigger the StackOverflow on Method 1. The crash must be real — not described but shown in the terminal. One `mkdir` and one `ln -s` command creates the test case in under 30 seconds.
- Output medium: screen-recording mp4 (Onda terminal; crash in Method 1; fix in Method 2; the added Set code is highlighted in the diff between the two methods)
- The change: Replace the recursive Method 2 with an iterative version using an explicit Deque<File> stack — show that the iterative version has no stack overflow risk and eliminates the need for the termination invariant (the Deque is the termination mechanism).
- Teardown angle: The three-part specification is the only guard against the class of failures that recursion enables: infinite descent, untracked shared state, and failure to name what "smaller" means. AI generates the base case and recursive case reliably; the invariant requires the human to specify what the recursion cannot assume.
- Exclusions: No tail-call optimization, no functional programming, no Stream API.
- Score: 10/10

---

## Candidate 03 — Object Invariants: Making Invalid State Impossible with Claude Code
- Source: java-programming/chapters/05-objects-as-specifications.md
- Lane: BUILD (Claude Code)
- Hook: The public-fields Task class compiles. Everything compiles. Then `task.priority = -9` compiles too. And `task.title = ""`. And `task.completed = false` after markComplete was called. The invariants are fiction until they are enforced by the class. Fix it.
- The artifact: A screen-recording: (1) public-fields Task → invariant violation attempts compile and execute silently; (2) specification-driven Task with private fields, constructor validation, and markComplete() → each violation attempt fails at compile or runtime with a specific message.
- Prompt seed: `claude "Write a Java Task class with fields: title (String), priority (int), completed (boolean)."` [PUBLIC FIELDS]. Then: `claude "Write a Java Task class. Invariants: (1) title is never null or blank (throws IllegalArgumentException 'title must not be blank' on violation); (2) priority is always 1-5 inclusive (throws IllegalArgumentException 'priority must be 1-5' on violation); (3) completed starts as false and can only change to true via markComplete(), never back. Implementation: private fields, constructor Task(String title, int priority) enforces all invariants, public void markComplete(), public accessors for all fields, no setters. No other state change is permitted."`
- Read / check: Verify all fields are private in Method 2; verify constructor validates title (null check AND blank check using isBlank()) and priority (1 <= p <= 5); verify markComplete() sets completed=true with no return value and no parameter; verify attempting `task.priority = 3` from outside fails at compile time (cannot assign to final/private).
- Human supplies: Screen-recording of both sessions and the violation attempt outputs.
- Output medium: screen-recording mp4 (terminal; violation attempts on Method 1 produce no error; same violations on Method 2 produce compile errors and specific IAE messages; a before/after state diagram overlay shows valid vs. invalid state space)
- The change: Add a second constructor Task(String title) with default priority=3 — show how the invariant is still enforced by routing through the same validation logic.
- Teardown angle: A class without invariant enforcement is a struct with a namespace. The enforcement mechanism — private fields and validated constructors — is what converts "I intend this to be a Task" into "this IS a Task, provably."
- Exclusions: No design patterns, no builder pattern, no Java record comparison.
- Score: 10/10

---

## Candidate 04 — ArrayList vs HashMap: An O(n) vs O(1) Benchmark with Claude Code
- Source: java-programming/chapters/14-data-structures-as-architectural-decisions.md
- Lane: BUILD (Claude Code)
- Hook: Two rosters look identical at 50 records. At 10,000 records, one is 200× slower. The structural decision was made in the prompt — and if the prompt didn't specify the access pattern, AI made the wrong choice by default. Build the benchmark.
- The artifact: A screen-recording of Claude generating two roster implementations (ArrayList linear scan vs. HashMap O(1) lookup) from access-pattern-specified prompts, then a benchmark showing lookup time at n=100, 1K, 10K, 100K. The ArrayList time grows linearly; the HashMap stays flat. Plotted as a Manim animated line chart.
- Prompt seed: `claude "Write a Java StudentRoster that stores Student objects. Dominant access: lookup by student ID at every user interaction. Scale: tens of thousands of students. Choose the correct data structure and explain why."` [SHOULD PRODUCE HashMap]. Then: `claude "Write a Java benchmark comparing ArrayList<Student> linear-scan lookup vs. HashMap<String, Student> key lookup for findById. Test at n = 100, 1000, 10000, 100000. Measure average nanoseconds per lookup over 1000 trials. Print as a table."`
- Read / check: Verify the first prompt produces a HashMap (if ArrayList, the audit catches it); verify the benchmark uses System.nanoTime() with warmup; verify ArrayList time grows roughly linearly while HashMap stays below 200ns at all scales.
- Human supplies: Real benchmark run on the human's machine — JVM performance is platform-dependent but the asymptotic behavior (O(n) vs O(1)) is stable. Screen-recording of the benchmark output and the Manim chart generation.
- Output medium: screen-recording mp4 (benchmark output in terminal) + Manim animated line chart (two curves: ArrayList growing, HashMap flat)
- The change: Add the "sorted display" requirement — show that satisfying both O(1) lookup AND sorted display requires two structures (HashMap + TreeMap or Collections.sort on display), and add that to the specification.
- Teardown angle: The data structure choice is architectural — it propagates through every caller. By the time performance is a problem, changing the structure means rewriting everything that depends on it. The specification made at generation time is the one that matters.
- Exclusions: No LinkedHashMap, no TreeMap internals, no concurrent data structures.
- Score: 9/10

---

## Candidate 05 — Build a Type-Safe Generic Stack with Claude Code
- Source: java-programming/chapters/12-generics-collections-and-type-safe-specification.md
- Lane: BUILD (Claude Code)
- Hook: The Object-based Stack compiles. Adding a String and retrieving an Integer also compiles. It crashes at runtime with ClassCastException. Generics were invented to move this error to compile time. Build the specified generic version.
- The artifact: A screen-recording: (1) Object-based stack → ClassCastException at runtime; (2) generic Stack<T> specification → compile-time error when types are misused. Three test cases: correct use (String stack), incorrect use caught at compile time, empty-stack behavior.
- Prompt seed: `claude "Write a Java Stack class that stores objects."` [PRODUCES Object version]. Then: `claude "Write a Java generic Stack<T> class. Specification: void push(T item) — throws IllegalArgumentException if item is null; Optional<T> pop() — returns Optional.empty() if stack is empty, otherwise removes and returns top element; T peek() — throws NoSuchElementException if empty; boolean isEmpty(); int size(). Invariant: internal storage never contains null. The class must be a generic type that provides compile-time type safety."`
- Read / check: Verify Method 1 allows `Stack stack = new Stack(); stack.push("hello"); Integer i = (Integer) stack.pop();` — compiles but throws ClassCastException; verify Method 2's equivalent attempt fails at compile time ("incompatible types"); verify Optional.empty() is returned for empty pop (not null); verify NoSuchElementException is thrown for empty peek.
- Human supplies: Screen-recording of both Claude sessions and the compile-time error output. The ClassCastException crash on Method 1 must be shown in real terminal output.
- Output medium: screen-recording mp4 (terminal; Method 1 crashes at runtime; Method 2 catches error at compile time; the type parameter in the generic declaration is highlighted as "the constraint that moves the error left")
- The change: Add `extends Comparable<T>` to the type bound and implement `T min()` — show how the bound both enables the method and restricts which types can be used.
- Teardown angle: Type safety is a specification mechanism, not a convenience. The generic type parameter is a constraint that the compiler checks on your behalf. Without it, every use is a bet that the caller used the type you intended.
- Exclusions: No wildcard captures, no bounded wildcards, no Collections.sort() with Comparators.
- Score: 9/10

---

## Candidate 06 — Build the Inheritance Contract: LSP in Practice with Claude Code
- Source: java-programming/chapters/07-inheritance-and-the-specification-contract.md
- Lane: BUILD (Claude Code)
- Hook: The Liskov Substitution Principle says every subclass must honor its superclass's contract. AI generates a subclass that compiles, passes its own tests, and silently violates the inherited postcondition. Build the contract violation — and the fix.
- The artifact: A screen-recording: (1) Animal superclass with makeSound() postcondition (non-null, non-blank String); (2) SilentAnimal subclass that returns null — violating LSP; (3) client code that uses polymorphism and crashes. Then: the fix — either defensive guard or redesigned hierarchy.
- Prompt seed: `claude "Write a Java Animal abstract class with abstract String makeSound(). Write a Dog subclass. Write a SilentAnimal subclass that doesn't make sounds."` [PRODUCES null-returning SilentAnimal]. Then: `claude "The makeSound() method has a postcondition: the return value must be non-null and non-blank. Redesign SilentAnimal so it honors this contract. Option A: throw UnsupportedOperationException with a descriptive message. Option B: return a representation of silence '...' that satisfies the contract. Explain which choice preserves substitutability."`
- Read / check: Verify the original SilentAnimal returns null; verify the client code crashes with NullPointerException when it tries to use the return value; verify both Option A and Option B are generated and the substitutability analysis is included; verify Option B (returning "...") is correctly identified as preserving LSP while Option A breaks it.
- Human supplies: Screen-recording of both Claude sessions and the crash output.
- Output medium: screen-recording mp4 (terminal; crash shown; then two fix options generated; a "LSP check" overlay annotates which option satisfies substitutability)
- The change: Add a third option — a NullObject pattern where SilentAnimal returns a special "silence" singleton that behaves like a sound — and show how it preserves the contract in the richest way.
- Teardown angle: Inheritance is a contract, not a code-sharing mechanism. A subclass that compiles and runs is not automatically a valid substitution. The postcondition that the superclass promised is the obligation every subclass must honor — and AI-generated subclasses routinely violate it when the postcondition isn't in the specification.
- Exclusions: No design patterns beyond what LSP requires, no SOLID principles survey, no interface segregation.
- Score: 9/10

---

## Candidate 07 — Specify a GUI as a User-Need Document with Claude Code
- Source: java-programming/chapters/08-gui-as-user-need-specification.md
- Lane: BUILD (Claude Code)
- Hook: GUI design is not about layout — it is a specification of what the user needs to accomplish. Write the user-need spec before generating the Swing form, and watch the generated UI reflect the spec rather than AI's defaults.
- The artifact: A screen-recording: (1) vague prompt ("make a form to add students") → AI generates a generic layout with no validation, no error display, no confirmation; (2) user-need specification naming each field's purpose, validation rules, error display location, and success feedback → AI generates a form that satisfies each requirement. Screenshot comparison of the two UIs annotated with what each spec element changed.
- Prompt seed: `claude "Write a Java Swing form to add students."` [VAGUE]. Then: `claude "Write a Java Swing form for adding a student to a roster. User needs: (1) Enter student ID (5-digit integer) — show red border + 'ID must be 5 digits' label if invalid; (2) Enter first name (non-blank) — show red border + 'Name required'; (3) Enter last name (non-blank) — same validation; (4) Click 'Add Student' button — disabled until all fields valid; (5) On success: clear fields and show green 'Student added: [ID] [Name]' for 3 seconds; (6) On duplicate ID: show dialog 'Student ID [X] already exists'. Each validation fires on focus loss, not on submit."`
- Read / check: Verify the vague form lacks per-field validation; verify the specified form fires validation on focus loss (not just on submit); verify the submit button is disabled until all fields are valid; verify the success feedback is time-limited (not permanent).
- Human supplies: Screen-recording of both Claude sessions and the two running forms side by side (both forms must run, not just generate code). Swing requires a running JVM — the human must compile and run both.
- Output medium: screen-recording mp4 (terminal for generation; screenshot comparison of two running forms with annotation callouts)
- The change: Add keyboard accessibility — Tab order specification and Enter-key submission — to the spec and show how the second generation incorporates it.
- Teardown angle: The GUI spec is not a layout spec — it is a behavior contract for a user interaction. Every validation rule, every error display location, every feedback timing is a specification decision. AI defaults produce generic forms; specified forms produce intentional interfaces.
- Exclusions: No accessibility deep dive, no MVC architecture, no JavaFX comparison.
- Score: 8/10

---

## Candidate 08 — Build and Debug a Priority Queue System with Claude Code
- Source: java-programming/chapters/14-data-structures-as-architectural-decisions.md (§Priority Queue section)
- Lane: BUILD (Claude Code)
- Hook: The ArrayList solution extracts the highest-priority task by scanning the whole list — O(n) every time. With 10,000 tasks, that's thousands of microseconds per extraction. The PriorityQueue does it in O(log n). The difference is the data structure named in the specification.
- The artifact: A screen-recording: Claude generates two task-scheduler implementations (ArrayList with linear-scan max-extraction vs. PriorityQueue<Task> with Comparator); a benchmark at n=1000, 10K shows O(n) vs O(log n) extraction time. Plotted as Manim animated bar chart comparing extraction time at each n.
- Prompt seed: `claude "Write a Java task scheduler that always processes the highest-priority task next."` [LIKELY PRODUCES ArrayList]. Then: `claude "Write a Java TaskScheduler class. Access pattern: extract the highest-priority task in O(log n) time. Dominant operation: poll() — removes and returns the highest-priority Task. Secondary: add(Task) — O(log n). Scale: up to 100,000 tasks. Use Java's PriorityQueue<Task> with a Comparator<Task> that orders by priority descending. Tasks with equal priority are served FIFO."`
- Read / check: Verify the first generation uses ArrayList (or scan-based extraction); verify the second uses PriorityQueue with a correct Comparator (priority descending — higher number = higher priority); verify FIFO tie-breaking is implemented (by adding a sequence number to the comparator).
- Human supplies: Real benchmark run. Screen-recording of both generations and the benchmark output.
- Output medium: screen-recording mp4 (terminal: two implementations generated; benchmark output shown) + Manim animated bar chart (two bars per n-value: ArrayList extraction time vs. PriorityQueue; bars animate in showing O(n) growth vs. near-flat)
- The change: Show what happens when the priority changes after insertion (a common real-world pattern) — PriorityQueue does not support priority update; show the correct workaround (lazy deletion with a visited Set).
- Teardown angle: The PriorityQueue is not a feature — it is the correct structure for exactly one access pattern: "give me the most important thing next, in O(log n)." Prompts that don't name the access pattern get ArrayList. The architectural decision is made at specification time.
- Exclusions: No heap implementation, no Fibonacci heap theory, no concurrent priority queues.
- Score: 8/10

---

## Candidate 09 — Test Edge Cases Before They Ship: The Defensive Specification Pattern with Claude Code
- Source: java-programming/chapters/15-hardening-edge-cases-and-failure-states.md
- Lane: BUILD (Claude Code)
- Hook: AI generates happy-path code. The edge cases arrive after deployment: null input, empty list, duplicate key, integer overflow. The specification that names them upfront is 20 lines; the post-deployment bug report is 200 lines. Build the defensive pattern.
- The artifact: A screen-recording: (1) happy-path addStudent specification → method that crashes on null input; (2) edge-case specification listing 5 failure modes → method with explicit handling for each. A test suite runs both and shows 5 failures on Version 1, 0 failures on Version 2.
- Prompt seed: `claude "Write a Java method to add a Student to a roster."` [HAPPY PATH]. Then: `claude "Write a Java method public boolean addStudent(Student student, Map<String, Student> roster). Edge-case specification: (1) student null → throws IllegalArgumentException 'student must not be null'; (2) student.id null or blank → throws IllegalArgumentException 'student ID must not be blank'; (3) student.id already in roster → returns false (caller decides whether to update); (4) roster null → throws IllegalArgumentException 'roster must not be null'; (5) student.name blank → throws IllegalArgumentException 'student name must not be blank'. Happy path: adds student to roster keyed by id, returns true. No other state change."`
- Read / check: Verify all 5 edge cases have distinct, specific exception messages; verify the duplicate-ID case returns false (not throws); verify Method 1 crashes on null input with NPE; verify Method 2 handles all 5 cases as specified.
- Human supplies: Screen-recording of both Claude sessions and the JUnit test output.
- Output medium: screen-recording mp4 (terminal; JUnit test runner shows 5 red failures on Method 1, 6 green passes on Method 2; each failing test is annotated with which edge case it caught)
- The change: Add a sixth edge case: roster.size() >= MAX_CAPACITY — requiring the caller to handle a capacity-exceeded condition. Show how the return-false vs. throw-exception choice for this case changes the caller's contract.
- Teardown angle: Edge cases are not a testing phase — they are a specification phase. Every failure mode the specification names becomes a testable contract. Every failure mode not named is a future bug. The discipline is enumerating failure modes before generation, not discovering them after deployment.
- Exclusions: No exception hierarchy design, no checked vs. unchecked debate, no try-with-resources.
- Score: 9/10

---

## Candidate 10 — Specify Recursion for Binary Search with Claude Code
- Source: java-programming/chapters/13-recursion-as-problem-decomposition.md + foundational
- Lane: BUILD (Claude Code)
- Hook: Binary search is the cleanest recursive algorithm — but AI generates a version that works on sorted arrays and crashes on unsorted ones, returns -1 for "not found" when the spec said Optional, and silently handles empty arrays differently than specified. Write the recursive spec first.
- The artifact: A screen-recording: (1) vague recursive binary search prompt → version with wrong not-found return, no null check, no sorted-assumption documentation; (2) three-part recursive specification → version that passes 6 test cases including empty array, single element, not-found, and duplicate elements.
- Prompt seed: `claude "Write a recursive binary search in Java."` [VAGUE]. Then: `claude "Write a Java method: public static Optional<Integer> binarySearch(int[] arr, int target, int low, int high). Three-part recursive specification: (1) Base cases: if low > high (not found), returns Optional.empty(); if arr[mid] == target (found), returns Optional.of(mid). (2) Recursive case: mid = low + (high - low) / 2; if target < arr[mid], recurse on (arr, target, low, mid-1); if target > arr[mid], recurse on (arr, target, mid+1, high). (3) Termination invariant: the search space [low, high] strictly shrinks each call (high - low decreases by at least 1). Precondition: arr is sorted ascending; arr is not null; 0 <= low <= high < arr.length for the initial call. The caller is responsible for passing a sorted array."`
- Read / check: Verify the base case for low > high returns Optional.empty() (not -1); verify mid calculation uses `low + (high - low) / 2` (avoiding integer overflow); verify the termination argument is correct (each recursive call reduces the interval by at least half); verify the precondition documents who is responsible for sortedness (the caller, not the method).
- Human supplies: Screen-recording of both Claude sessions and the 6-test-case output.
- Output medium: screen-recording mp4 (terminal; 6 test cases shown for both versions; failing tests on Version 1 annotated with the violated specification element)
- The change: Add the invariant documentation as a comment inside the method explaining why the recursion terminates — making the three-part spec visible in the code itself.
- Teardown angle: The three-part recursive specification is the only way to know the recursion will terminate. The base case handles what; the recursive case handles how it shrinks; the invariant proves it stops. Any one of the three missing is an avenue to infinite recursion.
- Exclusions: No iterative binary search, no complexity analysis, no Arrays.binarySearch() comparison.
- Score: 9/10
