+++
title = "Usage"
+++

<!-- toc -->

## Doing exercises

The exercises are sorted by topic and can be found in the subdirectory `exercises/<topic>`.
For every topic, there is an additional `README.md` file with links to the relevant Python documentation.
We highly recommend that you have a look at them before you start 📚️

Each exercise contains broken or unfinished code, and it's up to you to fix it!
Search for `# TODO` comments to find out what you need to change.
Ask for hints by entering `h` in the _watch mode_ 💡

## How exercises are checked

Every time you save, Rattlesnake checks the current exercise in up to five stages:

1. **Run**: `uv run python` executes the file without errors
2. **Test**: `uv run pytest` passes the exercise's tests
3. **Lint**: `uv run ruff check` reports no lint violations
4. **Format**: `uv run ruff format --check` finds the file formatted (some exercises only)
5. **Type check**: `uv run ty check` reports no type errors (some exercises only)

The exercise is done once every enabled stage passes ✅

## Watch Mode

After the [initialization](@/setup/index.md#initialization), launch Rattlesnake by running `rattlesnake`.

This starts the _watch mode_ which walks you through the exercises in a predefined order, from beginner syntax to advanced topics.
It reruns the current exercise automatically every time you save the exercise's file in the `exercises/` directory.

{% details(summary="If detecting file changes in the <code>exercises/</code> directory fails…") %}

You can add the **`--manual-run`** flag (`rattlesnake --manual-run`) to manually rerun the current exercise by entering `r` in the watch mode.

Please [report the issue](https://github.com/papadavis47/rattlesnake/issues/new) with some information about your operating system and whether you run Rattlesnake in a container or a virtual machine (e.g. WSL).

{% end %}

## Exercise List

In the [watch mode](#watch-mode), you can enter `l` to open the interactive exercise list.

The list allows you to…

- See the status of all exercises (done or pending)
- `c`: Continue at another exercise (temporarily skip some exercises or go back to a previous one)
- `r`: Reset status and file of the selected exercise (you need to _reload/reopen_ its file in your editor afterwards)

See the footer of the list for all possible keys.

## Other commands

| Command | Purpose |
| --- | --- |
| `rattlesnake run [name]` | Run an exercise, or the next pending exercise |
| `rattlesnake hint [name]` | Show an exercise hint |
| `rattlesnake reset <name>` | Restore an exercise to its original state |
| `rattlesnake check-all` | Recheck every exercise and update progress |

## Questions?

If the built-in hints aren't enough, feel free to [open an issue](https://github.com/papadavis47/rattlesnake/issues) 💡

## Continuing On

Once you've completed Rattlesnake, put your new knowledge to good use!
Keep practicing by building your own Python projects, contributing to Rattlesnake, or finding other open-source projects to contribute to.

> If you want to create your own Rattlesnake exercises, visit the [**community exercises**](@/community-exercises/index.md) page 🏗️
