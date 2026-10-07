+++
title = "Community Exercises"
+++

## List of Community Exercises

There are no community exercise projects yet. Yours could be the first!

> You can use the same `rattlesnake` program that you installed with `cargo install` to run community exercises.

## Creating Community Exercises

Rattlesnake's support for community exercises allows you to create your own exercises to focus on some specific topic.
You could also offer a translation of the official Rattlesnake exercises as community exercises.

### Getting Started

To create community exercises, install Rattlesnake and run `rattlesnake dev new PROJECT_NAME`.
This command creates the directory `PROJECT_NAME` with everything you need to get started: an `info.toml`, a `pyproject.toml`, `exercises/` and `solutions/` directories, a `README.md`, and a `.gitignore`.

_Read the comments_ in the generated `info.toml` file to understand its format.
It allows you to set a custom welcome and final message and specify the metadata of every exercise.

### Creating an Exercise

Here is an example of the metadata of one exercise:

```toml
[[exercises]]
name = "intro1"
hint = """
To finish this exercise, you need to …
These links might help you …"""
```

After entering this in `info.toml`, create the file `intro1.py` in the `exercises/` directory.
Mark what the learner needs to change with `# TODO` comments.
Exercises run their tests with pytest by default, so include at least one `def test_` function.
Look at the official Rattlesnake exercises for inspiration.

Each exercise can enable or disable checks in `info.toml`:

| Field | Default | Check |
| --- | --- | --- |
| `test` | `true` | `pytest` |
| `lint` | `true` | `ruff check` |
| `format` | `false` | `ruff format --check` |
| `type_check` | `false` | `ty check` |

You can optionally add a solution file `intro1.py` to the `solutions/` directory.

Now, run `rattlesnake dev check`.
It will tell you about any issues with your exercises and run your solutions (if you have any) to make sure that they pass.
Add `--require-solutions` to require a solution for every exercise.

That's it!
You finished your first exercise 🎉

### pyproject.toml

The generated `pyproject.toml` installs pytest, Ruff, and ty through `uv`.
You can modify it as you want:

- Add dependencies your exercises need to the `[dependency-groups]` `dev` list.
- Configure lint rules for all exercises in a [`[tool.ruff]`](https://docs.astral.sh/ruff/configuration/) table.

### Publishing

Now, add more exercises and publish them as a Git repository.

Users just have to clone that repository and run `rattlesnake` in it to start working on your exercises (just like the official ones).

One difference to the official exercises is that the solution files will not be hidden until the user finishes an exercise.
But you can trust your users to not open the solution too early 😉

### Sharing

After publishing your community exercises, open an issue or a pull request in the [Rattlesnake repository](https://github.com/papadavis47/rattlesnake) to add your project to the [list of community exercises](#list-of-community-exercises) 😃
