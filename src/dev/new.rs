use anyhow::{Context, Result, bail};
use std::{
    env::set_current_dir,
    fs::{self, create_dir},
    path::Path,
    process::Command,
};

use crate::CURRENT_FORMAT_VERSION;

// Create a directory relative to the current directory and print its path.
fn create_rel_dir(dir_name: &str, current_dir: &str) -> Result<()> {
    create_dir(dir_name)
        .with_context(|| format!("Failed to create the directory {current_dir}/{dir_name}"))?;
    println!("Created the directory {current_dir}/{dir_name}");
    Ok(())
}

// Write a file relative to the current directory and print its path.
fn write_rel_file<C>(file_name: &str, current_dir: &str, content: C) -> Result<()>
where
    C: AsRef<[u8]>,
{
    fs::write(file_name, content)
        .with_context(|| format!("Failed to create the file {current_dir}/{file_name}"))?;
    // Space to align with `create_rel_dir`.
    println!("Created the file      {current_dir}/{file_name}");
    Ok(())
}

pub fn new(path: &Path, no_git: bool) -> Result<()> {
    let dir_path_str = path.to_string_lossy();

    create_dir(path).with_context(|| format!("Failed to create the directory {dir_path_str}"))?;
    println!("Created the directory {dir_path_str}");

    set_current_dir(path)
        .with_context(|| format!("Failed to set {dir_path_str} as the current directory"))?;

    if !no_git
        && !Command::new("git")
            .arg("init")
            .status()
            .context("Failed to run `git init`")?
            .success()
    {
        bail!("`git init` didn't run successfully. See the possible error message above");
    }

    write_rel_file(".gitignore", &dir_path_str, GITIGNORE)?;

    create_rel_dir("exercises", &dir_path_str)?;
    create_rel_dir("solutions", &dir_path_str)?;

    write_rel_file(
        "info.toml",
        &dir_path_str,
        format!(
            "{INFO_FILE_BEFORE_FORMAT_VERSION}{CURRENT_FORMAT_VERSION}{INFO_FILE_AFTER_FORMAT_VERSION}"
        ),
    )?;

    write_rel_file("pyproject.toml", &dir_path_str, PYPROJECT_TOML)?;

    write_rel_file("README.md", &dir_path_str, README)?;

    println!("\nInitialization done ✓");

    Ok(())
}

pub const GITIGNORE: &[u8] = b".venv/
__pycache__/
*.pyc
.rattlesnake-state.txt
";

const INFO_FILE_BEFORE_FORMAT_VERSION: &str =
    "# The format version is an indicator of the compatibility of community exercises with the
# Rattlesnake program.
# The format version is not the same as the version of the Rattlesnake program.
# In case Rattlesnake makes an unavoidable breaking change to the expected format of community
# exercises, you would need to raise this version and adapt to the new format.
# Otherwise, the newest version of the Rattlesnake program won't be able to run these exercises.
format_version = ";

const INFO_FILE_AFTER_FORMAT_VERSION: &str = r#"

# Optional multi-line message to be shown to users when just starting with the exercises.
welcome_message = """Welcome to these community Rattlesnake exercises."""

# Optional multi-line message to be shown to users after finishing all exercises.
final_message = """We hope that you found the exercises helpful :D"""

# Repeat this section for every exercise.
[[exercises]]
# Exercise name which is the exercise file name without the `.py` extension.
name = "???"

# Optional directory name to be provided if you want to organize exercises in directories.
# If `dir` is specified, the exercise path is `exercises/DIR/NAME.py`
# Otherwise, the path is `exercises/NAME.py`
# dir = "???"

# Rattlesnake expects the exercise to contain tests and run them.
# You can optionally disable testing by setting `test` to `false` (the default is `true`).
# In that case, the exercise will be considered done when it just runs successfully.
# test = true

# Run type checking on the exercise (default is `false`).
# type_check = false

# Run linting on the exercise (default is `true`).
# lint = true

# Check formatting on the exercise with `ruff format --check` (default is `false`).
# format = false

# A multi-line hint to be shown to users on request.
hint = """???"""
"#;

const PYPROJECT_TOML: &[u8] = br#"[project]
name = "rattlesnake-exercises"
version = "0.1.0"
requires-python = ">=3.12"

[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.11",
    "ty>=0.0",
]
"#;

const README: &str = "# Rattlesnake 🐍

Welcome to these community Rattlesnake exercises 😃

First, [install Rattlesnake using the official instructions](https://github.com/papadavis47/rattlesnake) ✅

Then, clone this repository, open a terminal in this directory and run `rattlesnake` to get started with the exercises 🚀
";
