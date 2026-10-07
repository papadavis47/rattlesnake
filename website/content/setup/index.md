+++
title = "Setup"
+++

<!-- toc -->

## Prerequisites

Rattlesnake is a Rust program that runs Python exercises, so you need two tools:

- **Rust** (1.88 or newer) to build and install Rattlesnake.
  Visit [www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) for instructions.
  This also installs _Cargo_, Rust's package manager.
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** to manage Python and the exercise tools.
  You don't need to install Python yourself: `uv` downloads Python 3.12 if needed.

> 🐧 If you are on **Linux**, make sure you have `gcc` installed (_for a linker_).
>
> Debian: `sudo apt install gcc`\
> Fedora: `sudo dnf install gcc`

> 🍎 If you are on **MacOS**, make sure you have _Xcode and its developer tools_ installed: `xcode-select --install`

## Installing Rattlesnake

Clone the repository and install the CLI from source:

```bash
git clone https://github.com/papadavis47/rattlesnake.git
cargo install --path rattlesnake
```

{% details(summary="If the installation fails…") %}

- Make sure you have the latest Rust version by running `rustup update`
- Try adding the `--locked` flag: `cargo install --path rattlesnake --locked`
- Otherwise, please [report the issue](https://github.com/papadavis47/rattlesnake/issues/new)

{% end %}

## Initialization

From the directory where you want to keep your exercises, run:

```bash
rattlesnake init
```

This creates a `rattlesnake/` directory with the exercises, a `pyproject.toml`, and a `.python-version` file.
It then runs `uv sync` to install [pytest](https://pytest.org), [Ruff](https://docs.astral.sh/ruff/), and [ty](https://docs.astral.sh/ty/) into a local virtual environment.

{% details(summary="If the command <code>rattlesnake</code> can't be found…") %}

Cargo installs binaries to the directory `~/.cargo/bin`.
If you installed Rust with a package manager, `~/.cargo/bin` might not be in your `PATH` environment variable.

- Either add `~/.cargo/bin` manually to `PATH`
- Or uninstall Rust from the package manager and [install it using the official way with `rustup`](https://www.rust-lang.org/tools/install)

{% end %}

Now, go into the newly initialized directory and launch Rattlesnake:

```bash
cd rattlesnake/
rattlesnake
```

## Working environment

### Editor

Any editor with good Python support works.
[VS Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is a solid choice.
Point your editor at the `.venv/` directory inside `rattlesnake/` so it finds the installed tools.

When running in a VS Code terminal, Rattlesnake opens the current exercise automatically.
For other editors, see the `--edit-cmd` option in `rattlesnake --help`.

### Terminal

Please use a modern terminal for the best experience.
The default terminal on Linux and Mac should be sufficient.
On Windows, we recommend the [Windows Terminal](https://aka.ms/terminal).

## Usage

After setup, visit the [**usage**](@/usage/index.md) page to learn how to work through the exercises 🚀
