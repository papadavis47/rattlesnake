# Rattlesnake — Project Status & Architecture

## What Is This?

Rattlesnake is a fork of [Rustlings](https://github.com/rust-lang/rustlings) repurposed to teach **intermediate-to-advanced Python** using the same Rust CLI infrastructure. The Rust TUI (watch mode, file-change detection, progress tracking) is preserved; only the exercise runner and content have been swapped to Python.

## Toolchain

Exercises are validated using the **Astral** stack, invoked via `uv run`:

| Tool     | Role                          | Replaces (Rustlings) |
|----------|-------------------------------|----------------------|
| `uv`     | Project bootstrap & runner    | `cargo`              |
| `pytest` | Test runner                   | `cargo test`         |
| `ruff`   | Linter                        | `cargo clippy`       |
| `ty`     | Type checker                  | *(new stage)*        |

## Exercise Validation Pipeline

Each exercise goes through up to 4 stages (configurable per-exercise in `info.toml`):

```
1. uv run python <exercise>.py     → runs without error?
2. uv run pytest <exercise>.py     → tests pass?          (if test = true)
3. uv run ruff check <exercise>.py → no lint violations?  (if lint = true)
4. uv run ty check <exercise>.py   → no type errors?      (if type_check = true)
```

## Completed Work

### Rust CLI Changes (Phase 1–4 ✅)

- **`src/cmd.rs`** — Replaced `CmdRunner` (was `cargo build/test/clippy`) with `uv run python`, `uv run pytest`, `uv run ruff check`, `uv run ty check`. Unit struct, no state needed.
- **`src/exercise.rs`** — Replaced `strict_clippy` with `type_check` and `lint` fields. Rewrote `RunnableExercise::run()` for the Python pipeline. Removed `run_bin()`. Changed file extensions to `.py`.
- **`src/info_file.rs`** — Added `type_check` and `lint` fields to `ExerciseInfo`. Removed `strict_clippy`. Changed path extension to `.py`.
- **`src/app_state.rs`** — Updated state file to `.rattlesnake-state.txt`. Updated `Exercise` struct fields. Replaced finish-line art with Rattlesnake branding.
- **`src/init.rs`** — Rewrote for `uv`-based init: checks for `uv`, writes `pyproject.toml` (with pytest/ruff/ty deps), `.python-version`, runs `uv sync`. Removed all Cargo/Clippy/rust-analyzer logic.
- **`src/cli.rs`** — Rebranded all user-facing strings to Rattlesnake.
- **`src/main.rs`** — Rebranded ASCII art, error messages, directory names. Removed `mod cargo_toml`.
- **`src/cargo_toml.rs`** — Gutted (no longer needed; Python exercises don't need Cargo.toml bin lists).
- **`src/embedded.rs`** — Changed file extensions from `.rs` to `.py`.
- **`rustlings-macros/src/lib.rs`** — Changed embedded file paths from `.rs` to `.py`.
- **`src/watch/notify_event.rs`** — Changed file watcher filter from `.rs` to `.py`.
- **`src/dev/check.rs`** — Removed `cargo_toml` checks, `fn main()` check, `rustfmt` check. Updated to Python conventions (`# TODO`, `def test_`).
- **`src/dev/update.rs`** — Simplified to just validate `info.toml` (no Cargo.toml bin list updates).
- **`src/dev/new.rs`** — Updated for Python projects: `pyproject.toml` template, Python `.gitignore`, Rattlesnake branding.
- **`Cargo.toml`** — Renamed package to `rattlesnake`.
- **`tests/integration_tests.rs`** — Updated binary name reference, directory names.
- **`tests/test_exercises/`** — Converted from Rust to Python exercise files.

### Exercise Content (Phase 5 — Initial Set ✅)

Created 7 exercises across 5 sections in `exercises/` with matching `solutions/`:

| Section                 | Exercises                           |
|-------------------------|-------------------------------------|
| `00_intro`              | `intro1.py`, `intro2.py`            |
| `01_type_hints`         | `type_hints1.py`, `type_hints2.py`  |
| `02_data_structures`    | `data_structures1.py`               |
| `03_comprehensions`     | `comprehensions1.py`                |
| `04_decorators`         | `decorators1.py`                    |

All exercises defined in `rustlings-macros/info.toml` with hints.

### Build Status

✅ `cargo build` compiles cleanly.

## Remaining Work

### More Exercises Needed (Phase 5 continued)

The following sections from the curriculum plan still need exercises written:

- `05_context_managers` — `__enter__`/`__exit__`, `@contextmanager`
- `06_oop` — Inheritance, MRO, `super()`, ABC, protocols
- `07_iterators_generators` — `__iter__`/`__next__`, `yield`, `yield from`, `itertools`
- `08_descriptors_properties` — `@property`, custom descriptors
- `09_error_handling` — Custom exceptions, exception groups, `match`/`case`
- `10_concurrency` — `threading`, `concurrent.futures`, GIL
- `11_async` — `async`/`await`, `asyncio`, tasks
- `12_testing` — `pytest` fixtures, parametrize, mocking
- `13_functools_closures` — `partial`, `lru_cache`, closures, `nonlocal`
- `14_pattern_matching` — Structural pattern matching
- `15_metaclasses` — `__new__` vs `__init__`, `type()`, `__init_subclass__`
- `16_protocols_abcs` — `typing.Protocol`, structural subtyping
- `17_packaging` — `__init__.py`, relative imports, `pyproject.toml`
- `quizzes/` — Mixed-topic quizzes between sections

### Polish

- Integration tests need updating for Python exercise semantics (the current Rust integration tests reference Cargo-based compilation patterns).
- README.md needs full rewrite for Rattlesnake.
- `dev-Cargo.toml` can be cleaned up or removed.
- Consider adding `ruff format --check` as an optional formatting stage.

## `info.toml` Exercise Schema

```toml
[[exercises]]
name = "type_hints1"       # Exercise file: exercises/<dir>/<name>.py
dir = "01_type_hints"       # Subdirectory (optional)
test = true                 # Run pytest (default: true)
type_check = false          # Run ty check (default: false)
lint = true                 # Run ruff check (default: true)
skip_check_unsolved = false # Skip "already solved" check (default: false)
hint = """..."""             # Hint shown on `h` keypress
```
