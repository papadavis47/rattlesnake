# Rattlesnake — Project Status & Architecture

## What Is This?

Rattlesnake is a fork of [Rustlings](https://github.com/rust-lang/rustlings) repurposed to teach **Python from beginner syntax through advanced concepts** using the same Rust CLI infrastructure. The Rust TUI (watch mode, file-change detection, progress tracking) is preserved; the exercise runner and curriculum use Python.

## Learning Notes

The root-level `learning/` directory is reserved for the user's personal learning
notes and is intentionally ignored by Git. When the user asks to preserve notes
or learning material for later study, create Markdown files in `learning/`
unless they specify another location. Create the directory if it does not yet
exist. Do not place project documentation there because its contents are not
version-controlled.

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

### Exercise Content (Phase 5 — 50 Exercises ✅)

The current curriculum has 50 exercises across 19 sections, with a matching
file in `solutions/` for every exercise:

| Section                        | Exercises                                      |
|--------------------------------|------------------------------------------------|
| `00_basics`                    | `basics1.py` through `basics11.py`             |
| `00_intro`                     | `intro1.py`, `intro2.py`                       |
| `01_type_hints`                | `type_hints1.py` through `type_hints3.py`      |
| `02_data_structures`           | `data_structures1.py`, `data_structures2.py`   |
| `03_comprehensions`            | `comprehensions1.py`, `comprehensions2.py`     |
| `04_decorators`                | `decorators1.py`, `decorators2.py`             |
| `05_context_managers`          | `context_managers1.py` through `context_managers3.py` |
| `06_oop`                       | `oop1.py` through `oop3.py`                    |
| `07_iterators_generators`      | `iterators1.py` through `iterators3.py`        |
| `08_descriptors_properties`    | `properties1.py`, `descriptors1.py`            |
| `09_error_handling`            | `error_handling1.py`, `error_handling2.py`     |
| `10_concurrency`               | `concurrency1.py`, `concurrency2.py`           |
| `11_async`                     | `async1.py`, `async2.py`                       |
| `12_testing`                   | `testing1.py`, `testing2.py`                   |
| `13_functools_closures`        | `functools1.py`, `functools2.py`               |
| `14_pattern_matching`          | `pattern_matching1.py`, `pattern_matching2.py` |
| `15_metaclasses`               | `metaclasses1.py`, `metaclasses2.py`           |
| `16_protocols_abcs`            | `protocols1.py`, `protocols2.py`               |
| `17_packaging`                 | `packaging1.py`                                |

Exercise order and configuration are defined in `rustlings-macros/info.toml`,
not by directory name. The 11 beginner exercises are presented first, followed
by the workflow checkpoint and the intermediate-to-advanced curriculum. Every
exercise has an inline hint in `info.toml` and a corresponding solution.

### Build Status

✅ `cargo check` compiles cleanly, including the embedded Python exercise files.

✅ The 11 beginner reference solutions pass their pytest and Ruff checks.

✅ `cargo run -- dev check` (and `--require-solutions`) passes end-to-end and is
idempotent — all 49 unsolved exercises fail as expected and all 50 solutions pass
their enabled stages. The repo commits a dev `pyproject.toml`/`.python-version`
so `uv run` resolves `pytest`/`ruff`/`ty` in-place (mirrors what `init` generates).

Notes on how this was reached:
- Exercises where the learner writes the tests set `learner_writes_tests = true`
  in `info.toml` to opt out of the "`test = true` requires `def test_`" check
  (`testing1`).
- `run_pytest` uses `--color=yes` (current pytest rejects `always`) and commands
  run with `PYTHONDONTWRITEBYTECODE=1` so exercise runs don't litter `__pycache__`.
- `type_hints2` sets `type_check = true` (its fix is purely type annotations);
  `comprehensions1`'s stub returns placeholders so it fails until solved.
- The ruff config ignores `UP046`/`UP047` because the generics exercises teach
  classic `TypeVar` and explicit variance rather than PEP 695 syntax.

## Remaining Work

### Curriculum Work

- Add mixed-topic quizzes between curriculum sections.
- Expand sections where additional practice is useful.

### Polish

- `exercises/README.md` still contains the upstream Rust exercise map and needs updating.
- `dev-Cargo.toml` still contains the upstream Rust exercise bin list and can be removed.
- Integration test names such as `run_compilation_success` still reflect Rust
  terminology even though their fixtures now use Python.
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
learner_writes_tests = false # Exempt from "test=true needs def test_" (default: false)
hint = """..."""             # Hint shown on `h` keypress
```
