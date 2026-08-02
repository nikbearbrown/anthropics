# Python Programming — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build a Text Adventure Game with Claude Code: From Zero to Playable" (LLM Exercise Arc)
- Source: python-programming/chapters/00-claude-code-basics.md   (LLM Exercise — Text Adventure project start)
- Lane: BUILD (Claude Code)
- Hook: A complete interactive game in 100 lines. Claude Code writes it. You play it. The whole thing happens in a terminal in 20 minutes.
- The artifact: A screen-recording mp4 of Claude Code writing the text adventure skeleton live — the terminal showing the `claude` command, the code appearing in `game.py`, then `python game.py` running the game. The player types a name, sees a title banner, gets a welcome.
- Prompt seed: `claude "Create a text adventure game skeleton: (1) print an ASCII art title banner for a game called 'The Haunted Library'; (2) ask the player for their name; (3) print a personalized welcome message with the game premise; (4) describe the starting room with 3 exits; (5) accept a direction command. Save as game.py. Run it after writing."`
- Read / check: game.py should run without errors. The title banner should be visible ASCII art. Input prompt should accept a name. Starting room should describe ≥3 exits. One direction command should be accepted (even if it just prints "You go north.").
- Human supplies: A screen-recording of the actual terminal session (QuickTime or similar). The game must actually run on a real machine — synthetic is not authentic for a screen-recording card.
- Output medium: screen-recording mp4 (terminal full-screen, font size legible, cursor visible as Claude types)
- The change: Ask Claude to add input validation — reject directions that aren't north/south/east/west and re-prompt.
- Teardown angle: The three levels of verification (runs without error → output matches expectation → handles edge cases) are the software engineering lesson. Most beginners stop at level 1.
- Exclusions: Language theory, compiler internals, Python history.
- Score: 9/10

## Candidate 02 — "Build the Text Adventure: Add Decisions and Branching Story with Claude Code" (LLM Exercise)
- Source: python-programming/chapters/04-decisions.md   (LLM Exercise — Text Adventure ch04)
- Lane: BUILD (Claude Code)
- Hook: A story that branches. North leads to the reading room; south leads to the catacombs. If you have the key, the door opens. If not, it doesn't.
- The artifact: A screen-recording mp4 showing Claude Code adding if/elif/else branching to game.py — the code appearing in the editor, then the game running and showing different room descriptions based on player choice.
- Prompt seed: `claude "Extend game.py to add branching story decisions: (1) from the starting room, north leads to a reading room, south to catacombs (locked — requires a key item); (2) add an 'inventory' variable (a list); (3) in the reading room, the player can 'take key' to add it to inventory; (4) return to starting room and go south — if 'key' in inventory, open the door; otherwise, print 'The door is locked.' Save and run with two test paths."`
- Read / check: Two test paths should be shown in the recording: with key (door opens) and without key (door locked). Inventory variable should be a Python list. Code should use if/elif/else, not a series of separate if statements. Verify no logic errors in the key-check path.
- Human supplies: A screen-recording of the actual terminal session showing both test paths. The game must genuinely run.
- Output medium: screen-recording mp4 (split-screen or sequential: code appearing then game running, two test paths)
- The change: Add a consequence — entering the catacombs without a torch reduces player health by 10 per room, and health ≤ 0 ends the game.
- Teardown angle: Boolean logic is the core of every game mechanic, every conditional access control, every "if user is admin" — decisions chapter is the inflection point where code stops executing top-to-bottom and starts responding to state.
- Exclusions: Pattern matching (match/case), switch statements in other languages, ternary operators.
- Score: 9/10

## Candidate 03 — "Build the Text Adventure: Refactor into Functions with Claude Code" (LLM Exercise)
- Source: python-programming/chapters/06-functions.md   (LLM Exercise — Text Adventure ch06)
- Lane: BUILD (Claude Code)
- Hook: By chapter 6, game.py is 200 lines of flat code. Claude Code does the refactor — extract 6 named functions, run the tests, confirm identical behavior.
- The artifact: A screen-recording mp4 showing the before state (flat game.py), Claude Code generating the refactored version with named functions (display_room, get_player_input, handle_combat, etc.), and then a test run confirming identical game behavior.
- Prompt seed: `claude "Refactor game.py into named functions. Extract: display_room(room_name, description, exits), get_player_input(prompt), handle_combat(player, enemy), check_inventory(item), apply_item(item, player), game_loop(). Each function should have a one-line docstring. Replace all inline code in the main game loop with function calls. The game should behave identically — test by playing the same path as before."`
- Read / check: Refactored file should have ≥6 named functions each with docstrings. The game loop should consist primarily of function calls, not inline logic. Same test path as pre-refactor should produce identical output. Verify no global state has been broken by the extraction.
- Human supplies: A screen-recording showing the refactor diff (before/after) and a test run. The game must genuinely run identically.
- Output medium: screen-recording mp4 (diff view or side-by-side before/after, then a test run)
- The change: Add unit tests for two of the extracted functions (display_room and check_inventory) using Python's assert statement — show that the tests pass.
- Teardown angle: Refactoring is not a luxury — it is the moment code becomes maintainable. The function extraction makes the game's logic visible as named actions rather than hidden in a wall of imperative statements.
- Exclusions: Decorators, lambda functions, higher-order functions, generator functions.
- Score: 9/10

## Candidate 04 — "Build the Text Adventure: OOP Refactor with Classes and Claude Code" (LLM Exercise)
- Source: python-programming/chapters/11-classes.md   (LLM Exercise — Text Adventure ch11)
- Lane: BUILD (Claude Code)
- Hook: The biggest architectural improvement in the whole project happens here. Player, Enemy, and Item become classes. The flat game becomes an object world.
- The artifact: A screen-recording mp4 showing Claude Code generating Player, Enemy, and Item classes — the class definitions appearing in the terminal, then a test combat: player attacks enemy, enemy attacks back, health bars update, game-ending condition triggers.
- Prompt seed: `claude "Refactor game.py into an OOP design. Create three classes: Player(name, health=100, inventory=[]), Enemy(name, health, attack_damage), Item(name, description, effect). Add methods: Player.take_item(item), Player.attack(enemy), Enemy.attack(player), Player.is_alive(). Instantiate a player and one enemy, simulate a 5-round combat loop, verify game-ending conditions (player or enemy health ≤ 0). Save as game_oop.py and run."`
- Read / check: File should define 3 classes with __init__ and at least 2 methods each. Combat loop should run exactly 5 rounds or until one combatant's health ≤ 0. Health values should update correctly across rounds. Verify Player.inventory is an instance list, not a class-level mutable default.
- Human supplies: A screen-recording of the terminal showing class definitions being written and the combat test running to a game-ending condition.
- Output medium: screen-recording mp4 (class definitions scrolling in terminal, then combat log printing round by round)
- The change: Add an inheritance hierarchy — MagicEnemy(Enemy) with a cast_spell() method that ignores armor. Show how the subclass reuses Enemy's __init__ via super().
- Teardown angle: The mutable default argument trap (inventory=[]) is the most common class bug in Python — caught here before it corrupts the game. OOP makes the bug visible because instance state is explicit.
- Exclusions: Abstract base classes, metaclasses, design pattern taxonomy.
- Score: 9/10

## Candidate 05 — "Build the Text Adventure: Save/Load with Files and Claude Code" (LLM Exercise)
- Source: python-programming/chapters/14-files.md   (LLM Exercise — Text Adventure ch14)
- Lane: BUILD (Claude Code)
- Hook: Without save/load, quitting the game loses all progress. Claude Code adds persistence in 20 lines using JSON file I/O.
- The artifact: A screen-recording mp4 showing Claude Code adding save_game() and load_game() functions to game.py — writing player state to game_save.json, then loading it back and resuming from the saved position.
- Prompt seed: `claude "Add save/load functionality to game.py: (1) save_game(player, current_room) writes player.name, player.health, player.inventory, current_room to 'game_save.json' using json.dump with a context manager; (2) load_game() reads the file and returns a Player instance and room name; (3) at game start, check if game_save.json exists — if yes, offer to load; (4) after each room entry, auto-save. Test: save, quit, reload, confirm state is restored."`
- Read / check: game_save.json should contain all 4 fields as valid JSON. The load_game() function should restore inventory as a list (not a string). Verify the context manager (with open()) is used for both save and load. Auto-save should happen after every room entry, not just on quit.
- Human supplies: A screen-recording showing: (1) the game running and saving, (2) the terminal showing cat game_save.json, (3) restarting and loading the saved state.
- Output medium: screen-recording mp4 (three-phase: play and save → show JSON file → restart and load)
- The change: Add error handling — if game_save.json is corrupted (manually edit it to break JSON syntax), catch the json.JSONDecodeError and offer to start fresh instead of crashing.
- Teardown angle: The buffer-flushing problem (why close() is not optional) explains why `with` statements exist — the context manager guarantees flush + close even when the program crashes. The game's save reliability depends on this.
- Exclusions: SQLite databases, pickle serialization, cloud saves.
- Score: 8/10

## Candidate 06 — "Analyze Text Adventure Playtest Data with pandas and Claude Code" (LLM Exercise)
- Source: python-programming/chapters/15-data-science.md   (LLM Exercise — Text Adventure final capstone)
- Lane: BUILD (Claude Code)
- Hook: The game is done. Now analyze 100 simulated playthroughs. Which room kills players most? What's the average session length? Claude Code writes the analysis in 15 lines of pandas.
- The artifact: A Manim animated bar chart showing average session length by death room (The Catacombs vs. The Alchemy Lab vs. The Library — three bars animating upward), plus a line chart showing session length distribution.
- Prompt seed: `claude "Generate a synthetic playtest dataset for a text adventure game: 100 rows with columns session_id, player_name, rooms_visited (int), death_room (string: Library/Catacombs/Alchemy Lab/Escaped), session_duration_minutes (float). Load with pandas, compute: (1) mean session length by death_room; (2) which room kills most players; (3) what fraction of players escaped. Plot a bar chart of mean session length per death_room using matplotlib."`
- Read / check: DataFrame should have 100 rows × 5 columns. death_room groupby should produce 4 groups. Mean session length bar chart should have labeled axes and a title. Escaped fraction should be computed as (df['death_room'] == 'Escaped').mean().
- Human supplies: Nothing — fully synthetic dataset generated by Claude Code. (For a real game, the human would supply actual playtest CSVs — noted in the card.)
- Output medium: Manim (animated bar chart — bars grow from zero, with value labels appearing on each bar, then a line chart of session length distribution)
- The change: Add a second analysis: which starting choice (north vs. south from room 1) correlates with eventual escape — a two-sample proportion test using scipy.stats.
- Teardown angle: NumPy vectorization vs. Python loops is the lesson from chapter 15 — the pandas groupby that aggregates 100 sessions in one line shows why the library exists. The for-loop alternative would be 15 lines; the pandas version is 1.
- Exclusions: Machine learning on playtest data, A/B testing methodology, cohort analysis.
- Score: 8/10

## Candidate 07 — "Build a Compound Interest Calculator: Loops and Lists with Claude Code" (LLM Exercise)
- Source: python-programming/chapters/05-loops.md + python-programming/chapters/09-lists.md
- Lane: BUILD (Claude Code)
- Hook: One dollar invested in 1926 in the S&P 500 would be worth over $12,000 today. A while loop computes it in 4 lines.
- The artifact: A Manim animated line chart showing compound interest growth over 40 years for 3 scenarios (3%, 7%, 10% annual return) — three curves drawing simultaneously from left to right on the same axes.
- Prompt seed: `claude "Write a Python script that computes compound interest for three investment scenarios: 3%, 7%, and 10% annual return, starting with $1000, over 40 years. Store each year's balance in a list. Plot all three curves on one matplotlib figure with labeled axes, a legend, and a title. Print the final values."`
- Read / check: Three lists should each have 41 elements (years 0–40). Final values should be approximately $3262 (3%), $14,974 (7%), $45,259 (10%). Plot should have clear legend, axis labels, and title. Verify balance is computed as balance * (1 + rate) each year, not balance + rate * principal.
- Human supplies: Nothing — fully synthetic. Values computable from the compound interest formula.
- Output medium: Manim (three curves drawing simultaneously year by year, labels appearing at the right end of each curve showing final value)
- The change: Add a monthly-contribution version ($100/month added) using the same loop and compare end values — showing the power of contribution vs. return rate.
- Teardown angle: The while loop and the list are the two structures that make this computable — the loop drives time forward, the list stores the history for plotting. The compound growth demonstrates why the loop's "repetition is computation" principle matters for financial math.
- Exclusions: Net present value, inflation adjustment, tax treatment.
- Score: 8/10

## Candidate 08 — "Build a Recursive Fibonacci Explorer with Claude Code" (LLM Exercise)
- Source: python-programming/chapters/12-recursion.md
- Lane: BUILD (Claude Code)
- Hook: The naive recursive Fibonacci makes 177 million function calls to compute fib(40). Memoization reduces it to 40. Claude Code writes both versions and benchmarks them.
- The artifact: A Manim animated comparison: two race bars — naive recursion vs. memoized recursion — showing call count and wall-clock time for fib(n) as n grows from 5 to 40, the naive bar exploding exponentially while memoized stays linear.
- Prompt seed: `claude "Write two Python Fibonacci implementations: (1) naive recursive fib(n); (2) memoized version using @functools.lru_cache. For each, compute fib(n) for n = 5, 10, 15, 20, 25, 30, 35, 40. For the naive version, add a call counter. Record wall-clock time for each n. Print a comparison table and plot call count vs n for both implementations."`
- Read / check: Naive call counts should be Fibonacci-like in themselves (roughly 2^n). Memoized call count should be linear in n. Wall-clock time for fib(40) should be measurably longer for naive (>1 second) vs. memoized (<0.001 second). Verify the call counter increments inside the function, not outside.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated dual bar chart — call count bars extend right as n increases, exponential vs. linear growth visible; time comparison panel below)
- The change: Add a third implementation using iteration (a for loop) — show it has 0 call overhead and identical time to memoized, making the case that recursion's elegance has a cost.
- Teardown angle: Recursion is elegant but naive — the call stack is invisible overhead. The benchmark makes the cost concrete: 177 million wasted computations for one number. Memoization is the insight that makes recursion practical.
- Exclusions: Tail-call optimization, stack overflow limits, dynamic programming theory.
- Score: 8/10

## Candidate 09 — "Build a Word-Frequency Counter from Project Gutenberg with Claude Code"
- Source: python-programming/chapters/10-dictionaries.md + python-programming/chapters/08-strings.md
- Lane: BUILD (Claude Code)
- Hook: What are the 20 most common words in Moby Dick? Claude Code downloads the book, strips punctuation, counts with a dictionary, and plots the result in 25 lines.
- The artifact: A Manim animated bar chart showing the top 20 words by frequency in Moby Dick (excluding stopwords) — bars growing from left to right as the word-frequency dictionary fills.
- Prompt seed: `claude "Write a Python script that: (1) downloads Moby Dick from Project Gutenberg (requests library); (2) tokenizes into words (split on whitespace, strip punctuation with str.translate); (3) removes NLTK stopwords; (4) counts word frequencies using a dict; (5) finds the top 20 most frequent words; (6) plots a horizontal bar chart using matplotlib, words on y-axis, frequency on x-axis."`
- Read / check: The top words should include "whale," "ship," "man," "sea" — none of the classic stopwords (the, a, is, of). Word count should match the book's known ~220,000 words. Verify str.translate removes punctuation, not a brittle regex. Verify the stopword list is applied case-insensitively.
- Human supplies: Nothing — fully synthetic (Project Gutenberg text is public domain and publicly downloadable).
- Output medium: Manim (animated bar chart — bars extend right one by one in descending order, word labels appearing on the y-axis as each bar grows)
- The change: Extend to bigrams — count two-word phrases and show the top 10 bigrams alongside the unigrams. Compare whether bigrams reveal more semantic content.
- Teardown angle: A dictionary is the natural data structure for counting because it maps keys (words) to values (counts) with O(1) lookup. The comparison between dict-based counting and sorted-list counting shows why data structure choice determines algorithmic complexity.
- Exclusions: TF-IDF, semantic embeddings, full NLP pipeline.
- Score: 7/10

## Candidate 10 — "Build a Module-Structured CLI Game with random and time with Claude Code" (LLM Exercise)
- Source: python-programming/chapters/07-modules.md   (LLM Exercise — Text Adventure ch07)
- Lane: BUILD (Claude Code)
- Hook: The chapter asks you to split game.py into game.py, combat.py, world.py, and player.py — and add random encounters using Python's random module.
- The artifact: A screen-recording mp4 showing Claude Code splitting the monolithic game.py into 4 files, adding `from combat import handle_combat`, and running a random encounter — the terminal showing the import structure, then the game running with a random enemy appearing.
- Prompt seed: `claude "Split the text adventure game into a module structure: game.py (main loop and imports), combat.py (handle_combat function), world.py (ROOMS dict with room descriptions and exits), player.py (Player class). Add random encounters using Python's random module: 30% chance of enemy encounter on each room entry. Use time.sleep(0.5) between combat rounds for dramatic effect. Run game.py and verify all imports work."`
- Read / check: Four separate .py files should exist. game.py should import from combat, world, player. The 30% encounter probability should use random.random() < 0.3. time.sleep(0.5) should be inside the combat loop. Verify the import chain is clean (no circular imports).
- Human supplies: A screen-recording showing the 4-file structure (ls output), then the game running with a random encounter triggering.
- Output medium: screen-recording mp4 (ls -la showing 4 files, then game running with encounter triggering)
- The change: Add a random.seed() call at startup and show how seeding makes the encounter sequence reproducible — useful for debugging.
- Teardown angle: Module organization is not about lines of code — it is about who is responsible for what. Splitting world.py out means room descriptions can change without touching combat logic. That separation is the entire point of modular design.
- Exclusions: Packages, __init__.py, pip install, virtual environments.
- Score: 7/10
