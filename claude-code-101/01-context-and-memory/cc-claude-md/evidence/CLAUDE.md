# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Run the CLI: `python3 src/gradebook.py [add NAME | score NAME VALUE | report]` (defaults to `report`)
- Run tests: `python3 tests/test_gradebook.py`
- Run a single test: `python3 tests/test_gradebook.py TestGradebook.test_average`

No dependencies beyond the standard library. Tests use `unittest`.

## Architecture

Single-module CLI (`src/gradebook.py`) that persists to a JSON file (`DB = Path("grades.json")`) in the current working directory. Each command re-reads and re-writes the entire file — there is no in-memory session state. The `if __name__ == "__main__"` block dispatches `sys.argv[1]` through a `{name: function}` dict, so adding a subcommand means adding a top-level function and an entry to that dict.

Tests import `gradebook` by inserting `src/` on `sys.path` (there is no package layout) and swap `gradebook.DB` to a `tempfile.TemporaryDirectory` path (restored in a `finally`) to redirect writes. Stdout is captured with `contextlib.redirect_stdout`. Any new module-level state that touches the filesystem should be similarly overridable.
