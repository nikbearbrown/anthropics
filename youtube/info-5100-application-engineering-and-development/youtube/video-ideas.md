# INFO 5100: Application Engineering and Development — Video Ideas

---

## Candidate 01 — Why changing one variable changes a variable you never touched
- Source: `info-5100-application-engineering-and-development/chapters/02-methods-arrays-and-file-objects.md`
- Topic: APPLICATION ENGINEERING
- Hook: You write `patronC = patronA`, change `patronC.age`, and `patronA.age` changes too — even though you never touched it.
- Key case: `Patron patronC = patronA; patronC.age = 99;` then `System.out.println(patronA.age)` prints 99, not 34.
- The Question: Two variable names should mean two independent values; here's the case where both names printed 99 — why did touching one name change the other?
- Core idea: Assignment copies the address (the sticky note), not the object on the heap — two names pointing to the same block behave as one.
- Visual object: A two-column diagram: left column = stack with named arrows, right column = heap with labeled boxes; the arrow from `patronC` redirects to the same box as `patronA`.
- Manim move: duplicate (copy sticky-note arrow) then transform (redirect both to same heap box) then morph (age field value flips to 99 in both views)
- Example seed: `patronA` holds age 34 at heap address 100; `patronC = patronA` draws second arrow to address 100; `patronC.age = 99` updates address 100; `patronA.age` reads address 100 → 99.
- Length band: ~1 min
- Still lanes: geo
- Prerequisites: Basic concept that variables hold values
- Exclusions: Garbage collection, Java memory model details, `==` vs. `.equals()`, primitive vs. reference type taxonomy beyond what's needed
- Score: 10/10

---

## Candidate 02 — Why a renamed button in Scene Builder silently breaks the whole app
- Source: `info-5100-application-engineering-and-development/chapters/12-recursion.md`
- Topic: APPLICATION ENGINEERING
- Hook: You drag a button to a new position in Scene Builder, run the app — the button does nothing, no error, no crash, just silence.
- Key case: FXML declares `fx:id="checkout_btn"` after a rename; controller field is `@FXML private Button checkoutButton`; no compile error; field stays null at runtime.
- The Question: The button is on screen, the handler method exists, the code compiles — so why does clicking the button produce absolutely nothing?
- Core idea: The FXML–controller connection is a string-match at runtime, not a compile-time link; a one-character difference in the name severs the connection invisibly.
- Visual object: A two-column matching diagram: FXML id strings on the left, `@FXML` field names on the right; arrows connect matches in green, mismatches hang unconnected in red.
- Manim move: scan (left column ids align with right column fields), split (one id renames mid-animation), trace (the formerly green arrow dissolves; the field stays null)
- Example seed: Three components — `bookTable`/`bookTable` (connects), `statusLabel`/`statusLabel` (connects), `checkoutButton`/`checkout_btn` (severs); click fires, JVM searches, finds no match, field null, handler never runs.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: None beyond knowing what a button click is
- Exclusions: Full FXML syntax, Scene Builder UI walkthrough, reflection API details, how to fix module path for JavaFX
- Score: 10/10

---

## Candidate 03 — Why the program that worked Monday broke Tuesday without anyone changing it
- Source: `info-5100-application-engineering-and-development/chapters/13-collections-and-iterators.md`
- Topic: APPLICATION ENGINEERING
- Hook: The search method passed every test on Monday; a teammate added a feature Tuesday; nobody re-ran search; the demo failed.
- Key case: `searchReturnsAllMatchingBooks` test — a library with three books, two matching "Design" — test asserts `results.size() == 2`. Passes Monday. Breaks Tuesday when the matching logic gets touched in a neighboring feature.
- The Question: Nobody changed the search method — so why did it return the wrong count at the demo?
- Core idea: A test is a claim made executable; without it, the behavior is invisible when surrounding code changes; regressions only announce themselves if there is a prior claim to violate.
- Visual object: A horizontal timeline showing Module 1 through 13 with a green test-dot planted at Module 1's search method; a red X appears at Module 11's feature change; the dot catches the X.
- Manim move: trace (timeline flows left to right), accumulate (green test dots appear at each module), decay (one dot turns red when feature change hits), collapse (the failing test report snaps to the red position)
- Example seed: `Library` with books "Design Patterns", "Clean Code", "The Design of Everyday Things"; `search("Design")` should return 2; Tuesday's feature accidentally lowercases titles before storing, breaking the comparator — test prints `expected: <2> but was: <0>`.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: None beyond knowing software can have bugs
- Exclusions: JUnit syntax, full test anatomy, lambda/stream refactoring, integration vs. unit testing
- Score: 9/10

---

## Candidate 04 — Why the same click that checks out a book has three different bugs hiding inside it
- Source: `info-5100-application-engineering-and-development/chapters/11-generics.md`
- Topic: APPLICATION ENGINEERING
- Hook: A 40-line button handler works in the demo — but adding one feature requires editing it in five places, and two of those edits introduce bugs you won't find until production.
- Key case: `checkoutButton.setOnAction(e -> { ... })` that validates, queries model, updates model, removes from list, adds to list, saves file, handles exception, checks limit, sets label — all in one lambda body.
- The Question: One button click should do one thing; here's a handler doing seven — why does adding an eighth break three of the previous seven?
- Core idea: A handler is a translator, not an application; each business decision in the handler body is one more reason the handler can break when that decision changes, and they pile up silently.
- Visual object: A before/after split panel — left: a tangled pile of labeled boxes all crammed into one lambda outline; right: three clean boxes (getSelection / performCheckout / refreshView) each with a single responsibility label.
- Manim move: split (one large box divides into three named boxes), spread (each box moves to its own column labeled handler / controller / view), morph (arrows connect the three boxes in sequence)
- Example seed: Handler originally has 5 steps. Due-date feature adds step 6 inside the handler. Checkout-limit warning adds step 7. Now a change to step 3 (availability check) silently breaks step 6 (due-date format depends on same field). Refactor: `isbn = getSelectedIsbn()`, `result = controller.performCheckout(isbn)`, `refreshView(result)` — four lines, three methods, zero entanglement.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic concept of a function/method
- Exclusions: Lambda syntax details, full JavaFX event model, anonymous vs. named inner class tradeoffs, generics (despite chapter label)
- Score: 9/10

---

## Candidate 05 — Why hashing a password means an attacker who reads your file still can't log in
- Source: `info-5100-application-engineering-and-development/chapters/06-basics-of-gui-programming-in-java.md`
- Topic: APPLICATION ENGINEERING
- Hook: Two login systems look identical in the demo — same fields, same behavior — but one hands every user's password to anyone who reads the database file.
- Key case: Plaintext file line `alice:password123` vs. hashed line `alice:ef92b778bafe771e89245b89ecbc08a44a4e166c`; attacker reads the file; plaintext gives immediate access, hash requires a dictionary attack.
- The Question: Both systems accept "password123" and reject "wrong" — so why does one expose every password on a file read and the other require the attacker to work?
- Core idea: A hash is a one-way function — same input always produces the same output, but the output cannot be reversed; verification compares hashes without ever storing the original.
- Visual object: A side-by-side comparison: left = file with plaintext, right = file with hash string; attacker icon reads both; left immediately unlocks a padlock, right hits a wall labeled "dictionary attack required."
- Manim move: compare (two file representations side by side), transform (password string passes through hash box → fixed-length hex string), split (attacker reads plaintext → opens lock; attacker reads hash → clock spins / wall appears)
- Example seed: Password "cat123". Hash function SHA-256 → `2a97...` (show 8 chars). Store `2a97...`. Login attempt: hash "cat123" → `2a97...`; compare strings; match. Attack: attacker has `2a97...`; must hash every word in dictionary until match found; "cat123" is weak so it's found quickly; "x7Q!kp9$" is not.
- Length band: 2–3 min
- Still lanes: geo | c2v
- Prerequisites: Basic concept of storing a file
- Exclusions: bcrypt, salting, rainbow tables, OWASP specifics, HTTPS/TLS, authentication vs. authorization, session management
- Score: 9/10

---

## Candidate 06 — Why a sort that works needs a named rule, not an inline tangle
- Source: `info-5100-application-engineering-and-development/chapters/09-event-driven-programming.md`
- Topic: APPLICATION ENGINEERING
- Hook: The sort by title works; three weeks later the requirement changes to "by author, then title"; the inline comparison tangle takes two hours to untangle and introduces two new bugs.
- Key case: `Comparator<Book> byAuthorThenTitle = Comparator.comparing(Book::getAuthorLastName).thenComparing(Book::getTitle)` vs. an anonymous nested string-comparison block with no name attached.
- The Question: Both comparisons sort books — so why does changing one requirement cost two hours while the other costs one line?
- Core idea: A `Comparator` is an ordering rule expressed as a named object; when the rule changes, you replace the named object rather than excavating a comparison tangle.
- Visual object: A before/after split: left = a tangled gray block labeled "compare strings here, also here, also here"; right = three clean labeled boxes (`byTitle`, `byAuthorThenTitle`, `byYearDescending`) each composable via `.thenComparing()`.
- Manim move: morph (tangle consolidates into a single named box), duplicate (named box cloned and labeled differently), spread (three named comparators arranged in a row, each feeding `list.sort()`)
- Example seed: Three books: "Dune" by Herbert (1965), "Foundation" by Asimov (1951), "Hyperion" by Simmons (1989). `byAuthorThenTitle` → Asimov/Foundation, Herbert/Dune, Simmons/Hyperion. Change requirement to `byYearDescending` → Simmons/1989, Herbert/1965, Asimov/1951. One variable swap, zero tangling.
- Length band: ~1 min
- Still lanes: geo
- Prerequisites: Basic concept of alphabetical sorting
- Exclusions: Stream API details, filter/collect, collection type selection (List vs. Map vs. Set), event-driven programming (despite chapter label)
- Score: 9/10

---

## Candidate 07 — Why wrong output is not the bug — it's the announcement that a bug exists upstream
- Source: `info-5100-application-engineering-and-development/chapters/04-basics-of-object-oriented-programming-part-2.md`
- Topic: APPLICATION ENGINEERING
- Hook: The second checkout in a row attaches the book to the wrong patron — but the wrong patron is not where the bug lives; it's just where the bug announces itself.
- Key case: `currentPatron` is not reset between checkouts; second checkout operates on the first patron's reference; output shows Book B under Patron A's name — symptom is the wrong name, root cause is the stale reference.
- The Question: The output names Patron A for Book B — so is the bug in the output line, the assignment line, or somewhere else entirely?
- Core idea: Every bug has three addresses: the symptom (what you see), the proximate cause (the line that produced it), and the root cause (the upstream state error that made the proximate cause possible); only fixing the root cause stops the bug.
- Visual object: A three-level vertical stack: bottom = root cause box (red, "currentPatron never reset"), middle = proximate cause box (orange, "wrong patron assigned"), top = symptom box (yellow, "wrong name in output"). Arrow flows upward from root through proximate to symptom.
- Manim move: trace (bug arrow travels upward from hidden root through stack to visible symptom), accumulate (each level label appears as arrow passes it), collapse (when root is fixed, both upper boxes turn green)
- Example seed: Session 1: `currentPatron = alice`, checkout Book A → alice/BookA correct. Session 2: `currentPatron` not updated; checkout Book B → `loan.setPatron(currentPatron)` sets alice again; output: "alice — Book B". Bug not on line 47 (the output), not on line 31 (the assignment), but on line 18 (the missing reset in the session-change branch).
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: None beyond knowing software can produce wrong output
- Exclusions: NetBeans debugger UI, step-over vs. step-into mechanics, wrapper classes, String/StringBuilder (despite chapter label)
- Score: 9/10

---

## Candidate 08 — Why data you carefully entered vanishes the moment you close the program
- Source: `info-5100-application-engineering-and-development/chapters/08-abstract-classes-and-interfaces.md`
- Topic: APPLICATION ENGINEERING
- Hook: You spend an hour entering books into the catalog. You close the program. You reopen it. The catalog is empty — as if the hour never happened.
- Key case: `Book` objects added to an in-memory array during the session; `saveToFile()` never called before exit; next session calls `loadFromFile()` and reads an empty or nonexistent file; catalog is empty.
- The Question: The books were real — you could see them in the list — so why does closing the program make them disappear?
- Core idea: Memory is temporary; an object that exists only in the heap dies with the process; persistence is the explicit act of writing state to a medium that survives the process ending.
- Visual object: A timeline strip with three phases: (1) program running — heap shows filled book boxes; (2) program closes — heap boxes disappear with a "process ended" label; (3) program reopens — heap is empty, file on disk is the only source of truth.
- Manim move: decay (heap boxes fade out at process close), accumulate (file icon fills with CSV lines when saveToFile runs), trace (arrow from file back to heap at next startup showing loadFromFile)
- Example seed: Session 1: add "Dune", "Foundation", "Hyperion" → array has 3 books → program exits without save → books gone. Session 2: file is empty → catalog loads 0 books. Fix: add `catalog.saveToFile("catalog.csv")` at exit → Session 3 loads all 3.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic concept of a computer program running and stopping
- Exclusions: Abstract classes and interfaces (despite chapter label), exception handling taxonomy, atomic rename/crash safety, CRUD delete semantics
- Score: 8/10

---

## Candidate 09 — Why the search bar breaks when you filter the table instead of the model
- Source: `info-5100-application-engineering-and-development/chapters/10-event-driven-programming-with-scene-builder.md`
- Topic: APPLICATION ENGINEERING
- Hook: The search bar works on the first search — then the user searches twice without clearing, and books that should appear don't; the list is now smaller than the actual catalog.
- Key case: Handler removes non-matching rows from `TableView.getItems()` to filter; second search runs on the already-reduced list; cleared items are in a local variable somewhere; the table is now the "authoritative" catalog, not the model.
- The Question: Both approaches make the table show only matching books — so why does the first search work and the second produce wrong results?
- Core idea: The table is a view, not a store; filtering the table creates two sources of truth; filtering the model and asking the table to display the result keeps truth in one place.
- Visual object: A split diagram: left = model (single blue box) → filter method → view (shows subset); right = table used as store (blue box duplicated into table cells) → rows removed → second filter runs on incomplete set.
- Manim move: split (model diagram vs. table-as-store diagram), slosh (second search arrow hits the shrunken table and returns a smaller result), transform (correct version: arrow returns to model each time, view always reflects full filtered result)
- Example seed: Catalog has 5 books: A, B, C, D, E. Search "A": wrong way removes B,C,D,E from table → table now has [A]. Clear and search "B": table only contains [A]; result is empty. Right way: search "B" calls `model.search("B")` → returns [B]; table displays [B]; catalog unchanged.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic concept of a search bar in an app
- Exclusions: MVC theory, Scene Builder UI, JavaFX scene graph structure, pane selection, TableView cell value factory details
- Score: 8/10

---

## Candidate 10 — Why the catalog that only exists inside the checkout method will always fight you
- Source: `info-5100-application-engineering-and-development/chapters/05-inheritance-and-polymorphism.md`
- Topic: APPLICATION ENGINEERING
- Hook: The checkout works — but a librarian can't search the catalog without pretending to be a patron, and two simultaneous checkouts see different books.
- Key case: `Catalog` built inside `checkout()` method rather than pre-existing as its own object; `catalog.searchByTitle("Java")` called before any patron exists → NullPointerException or empty result because catalog only materializes during a transaction.
- The Question: The catalog had books in it during checkout — so why is it empty when called from anywhere else in the program?
- Core idea: A catalog is an entity that exists independently of any transaction; when you model it as a side effect of the checkout, it can only exist while a checkout is running, which prevents every other access pattern.
- Visual object: A two-panel comparison: left = catalog box nested inside checkout box (no independent existence); right = catalog box at the top of the diagram, checkout box below it drawing an arrow up to catalog (entity precedes transaction).
- Manim move: split (catalog-inside-checkout vs. catalog-as-standalone), transform (catalog box lifts out of checkout box and floats to top level), spread (multiple arrows — librarian search, admin add, checkout — all point to the same top-level catalog)
- Example seed: Wrong: `public void checkout(String isbn) { Catalog c = new Catalog(); c.addBook(...); ... }` — catalog born and dies in one method. Right: `Catalog catalog = new Catalog(100); catalog.addBook(new Book(...));` in `main` before any patron exists; `catalog.searchByTitle("Java")` works with zero patrons.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic concept that a library has books before customers arrive
- Exclusions: Inheritance hierarchies, polymorphism, dynamic binding, casting, ArrayList (despite chapter label)
- Score: 8/10
