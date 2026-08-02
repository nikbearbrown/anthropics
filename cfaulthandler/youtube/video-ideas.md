# Cfaulthandler Video Ideas

## Candidate 1 — Why can you see both Python and C frames in a single crash report?
- Source: `README.md`
- Topic: Simultaneous unwinding of Python and C call stacks
- Hook: When an extension module crashes, you're in both Python code (which made the call) and C code (where the crash happened)—seeing both requires understanding two different stack layouts.
- Key case: `ctypes.string_at(0)` faults; the output shows Python frames (`/usr/lib/python3.11/ctypes/__init__.py`, line 519) followed seamlessly by C frames (`/lib/x86_64-linux-gnu/libc.so.6(+0x42520)`).
- The Question: Python debuggers show Python frames; system tools show C frames—how does a single tool show both simultaneously and in sequence?
- Core idea: The unwinder must understand two different frame layouts: Python's frame pointers (linked list) and the machine's call stack (saved return addresses in memory), switching between them at language boundaries.
- Visual object: A unified call stack visualization showing Python frames (with source file/line labels) transitioning into C frames (with binary offsets), with a visual marker at the boundary where Python calls become C execution.
- Manim move: scan
- Example seed: Python function `foo()` calls `bar()` (ctypes binding), which calls C `baz()`, which calls `qux()`, which crashes in `libc.so`. The unwound stack shows the file:line entries, then transitions to shared object offsets (+0x5000, +0x6000), creating a unified narrative from entry point to fault.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: Python C API, function calls, call stacks
- Exclusions: writing C extensions, ctypes binding mechanics, libunwind internals
- Score: 8/10

## Candidate 2 — How can a process capture its own stack after a fatal signal?
- Source: `README.md`
- Topic: Capturing runtime state from a process at the moment of a fatal signal
- Hook: Segfaults terminate the process immediately—yet `cfaulthandler.enable()` runs before the crash and somehow still prints the call stack afterward.
- Key case: `cfaulthandler.enable()` is called, then `ctypes.string_at(0)` triggers SIGSEGV; the process doesn't immediately die; the handler intercepts and prints the stack before termination.
- The Question: A segfault should instantly kill the process—why can a handler still capture and print state after the fault has occurred?
- Core idea: Signal handlers execute in the context of the faulted process; the handler can inspect memory and data structures (including the call stack) before the OS terminates, creating a race between diagnosis and death.
- Visual object: A timeline showing process running → invalid memory access → OS sends SIGSEGV → handler intercepts → call stack captured and printed → process exits.
- Manim move: accumulate
- Example seed: Process executes `char *p = (char *)0; *p = 'x';`—illegal write. Before the OS kills the process, the installed handler runs, walks the stack by reading return addresses from memory, and prints them.
- Length band: ~1–2 min
- Still lanes: geo, raster
- Prerequisites: signal handling, what a segfault is, CPU call stacks
- Exclusions: core dumps, post-mortem debugging with gdb, alternative fault detection
- Score: 7/10

## Candidate 3 — Why does a memory offset alone not identify code?
- Source: `README.md`
- Topic: Using debug symbols to map binary offsets to source code locations
- Hook: A crash report shows `+0xec2c`—a position in a shared library—but that number doesn't tell you what code was running or why it crashed.
- Key case: The example shows `/usr/lib/python3.11/lib-dynload/_ctypes.cpython-311-x86_64-linux-gnu.so(+0xec2c)` (meaningless offset); running `addr2line -e [so-file] +0xec2c` returns `_ctypes.c:5544` (now meaningful).
- The Question: Why can't an offset identify the code it represents, and how does an external tool map that number to a source location?
- Core idea: Binaries are optimized for size; source-level information is stripped or stored separately in debug symbols (DWARF tables), which maintain mappings from offsets back to file, function, and line.
- Visual object: Two-pane split: left shows raw offset `+0xec2c`, right shows DWARF table being queried, center shows the result `_ctypes.c:5544`.
- Manim move: morph
- Example seed: A binary contains function `foo()` occupying offsets 0x1000–0x1100. A fault at 0x1050: without symbols, you see `libc.so(+0x1050)`; with addr2line and debug symbols, you see `mylib.c:42 in foo()`.
- Length band: ~1 min
- Still lanes: c2v, raster
- Prerequisites: how binaries are structured, what debug symbols are
- Exclusions: DWARF format, compiler optimization, symbol stripping at build time
- Score: 6/10

Working from the supplied corpus directly.

The corpus contains one untapped concept: each C frame in the output carries two numbers — `(+0x42520)` and `[0x7fba46a42520]` — but only the relative offset works with `addr2line`. That duality is ASLR in action, and it is not covered by any existing candidate (Candidate 3 explains *why* an offset doesn't identify code without symbols; it never explains why two numbers appear or which one to use).

---

# Cfaulthandler Video Ideas

## Candidate 04 — Why does every crash frame show two addresses, and only one of them is useful?
- Source: `README.md`
- Topic: ASLR and why relative offsets survive crash analysis but absolute addresses don't
- Hook: The crash report prints both `(+0x42520)` and `[0x7fba46a42520]` for the same frame—the absolute address tells you exactly where the fault was in memory, yet `addr2line` refuses it and demands the smaller number.
- Key case: Running the same `ctypes.string_at(0)` crash twice produces different bracketed addresses `[0x7fba46...]` each time but identical parenthesized offsets `(+0x42520)`; `addr2line -e libc.so.6 +0x42520` succeeds; `addr2line -e libc.so.6 0x7fba46a42520` fails or returns `??`.
- The Question: The absolute address is the exact runtime location of the fault—why is the relative offset more useful for source recovery?
- Core idea: ASLR loads each shared library at a random base address every run; absolute address = base + offset. `addr2line` works against the on-disk binary where base = 0, so only the offset—invariant across runs—maps back to a source line.
- Visual object: A horizontal number line representing virtual memory with a library rectangle sliding to a different position on each of two runs; an offset arrow of fixed length extending from the library's left edge lands on the same *relative* position both times, while a pin marking the absolute address moves.
- Manim move: slosh
- Example seed: Library `foo.so` loads at base `0x1000` on run 1 and `0x5000` on run 2. Fault occurs at offset `+0x200` in both runs—absolute addresses `0x1200` and `0x5200` differ; offset `+0x200` is identical. `addr2line -e foo.so +0x200` returns `foo.c:17` in both cases.
- Length band: ~1 min
- Still lanes: geo, raster
- Prerequisites: virtual memory, shared libraries, what addr2line does
- Exclusions: ASLR bypass techniques, PIE executables vs shared libraries, kernel ASLR entropy tuning
- Score: 9/10
