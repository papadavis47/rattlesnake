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

### Exercise Content (Phase 5 — 32 Exercises ✅)

The current curriculum has 32 exercises across 18 sections, with a matching
file in `solutions/` for every exercise:

| Section                        | Exercises                                      |
|--------------------------------|------------------------------------------------|
| `00_basics`                    | `basics1.py` through `basics10.py`             |
| `00_intro`                     | `intro1.py`, `intro2.py`                       |
| `01_type_hints`                | `type_hints1.py`, `type_hints2.py`             |
| `02_data_structures`           | `data_structures1.py`                          |
| `03_comprehensions`            | `comprehensions1.py`                           |
| `04_decorators`                | `decorators1.py`                               |
| `05_context_managers`          | `context_managers1.py`, `context_managers2.py` |
| `06_oop`                       | `oop1.py`, `oop2.py`                           |
| `07_iterators_generators`      | `iterators1.py`, `iterators2.py`               |
| `08_descriptors_properties`    | `properties1.py`                               |
| `09_error_handling`            | `error_handling1.py`                           |
| `10_concurrency`               | `concurrency1.py`                              |
| `11_async`                     | `async1.py`                                    |
| `12_testing`                   | `testing1.py`                                  |
| `13_functools_closures`        | `functools1.py`                                |
| `14_pattern_matching`          | `pattern_matching1.py`                         |
| `15_metaclasses`               | `metaclasses1.py`                              |
| `16_protocols_abcs`            | `protocols1.py`                                |

Exercise order and configuration are defined in `rustlings-macros/info.toml`,
not by directory name. The 10 beginner exercises are presented first, followed
by the workflow checkpoint and the intermediate-to-advanced curriculum. Every
exercise has an inline hint in `info.toml` and a corresponding solution.

### Build Status

✅ `cargo check` compiles cleanly, including the embedded Python exercise files.

✅ The 10 beginner reference solutions pass their pytest and Ruff checks.

⚠️ `cargo run -- dev check --require-solutions` currently stops at
`exercises/12_testing/testing1.py`: the developer check requires an existing
`def test_` function, but that exercise intentionally asks the learner to write
all of its test functions.

## Remaining Work

### Curriculum Work

- Add `17_packaging` exercises covering `__init__.py`, relative imports, and
  `pyproject.toml`.
- Add mixed-topic quizzes between curriculum sections.
- Expand the one-exercise advanced sections where additional practice is useful.

### Polish

- Fix the `dev check` test-detection rule so `testing1.py` can intentionally ask
  learners to create the tests.
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
hint = """..."""             # Hint shown on `h` keypress
```
