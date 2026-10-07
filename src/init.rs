use anyhow::{Context, Result, bail};
use crossterm::{
    QueueableCommand,
    style::{Attribute, Color, ResetColor, SetAttribute, SetForegroundColor},
};
use std::{
    env::{current_dir, set_current_dir},
    fs::{self, create_dir},
    io::{self, Write},
    path::Path,
    process::{Command, Stdio},
};

use crate::{
    embedded::EMBEDDED_FILES, exercise::RunnableExercise, info_file::InfoFile,
    term::press_enter_prompt,
};

pub fn init() -> Result<()> {
    // Guard against re-initializing from inside an existing Rattlesnake project,
    // which would otherwise create a nested `rattlesnake/rattlesnake/`.
    if Path::new("exercises").is_dir()
        && Path::new("solutions").is_dir()
        && Path::new("pyproject.toml").is_file()
    {
        bail!(RATTLESNAKE_ALREADY_INITIALIZED_ERR);
    }

    let rattlesnake_dir = Path::new("rattlesnake");
    if rattlesnake_dir.exists() {
        bail!(RATTLESNAKE_DIR_ALREADY_EXISTS_ERR);
    }

    if !Command::new("uv")
        .arg("--version")
        .stdin(Stdio::null())
        .stdout(Stdio::null())
        .stderr(Stdio::null())
        .status()
        .context("Failed to run the command `uv --version`")?
        .success()
    {
        bail!("uv is required. Install it from https://docs.astral.sh/uv/")
    }

    let mut stdout = io::stdout().lock();

    stdout.write_all(b"This command will create the directory `rattlesnake/` which will contain the exercises.\n\
                       Press ENTER to continue ")?;
    press_enter_prompt(&mut stdout)?;

    create_dir(rattlesnake_dir).context("Failed to create the `rattlesnake/` directory")?;
    set_current_dir(rattlesnake_dir)
        .context("Failed to change the current directory to `rattlesnake/`")?;

    let info_file = InfoFile::parse()?;
    EMBEDDED_FILES
        .init_exercises_dir(&info_file.exercises)
        .context("Failed to initialize the `rattlesnake/exercises` directory")?;

    create_dir("solutions").context("Failed to create the `solutions/` directory")?;
    fs::write(
        "solutions/README.md",
        include_bytes!("../solutions/README.md"),
    )
    .context("Failed to create the file rattlesnake/solutions/README.md")?;
    for dir in EMBEDDED_FILES.exercise_dirs {
        let mut dir_path = String::with_capacity(10 + dir.name.len());
        dir_path.push_str("solutions/");
        dir_path.push_str(dir.name);
        create_dir(&dir_path)
            .with_context(|| format!("Failed to create the directory {dir_path}"))?;
    }
    for exercise_info in &info_file.exercises {
        let solution_path = exercise_info.sol_path();
        fs::write(&solution_path, INIT_SOLUTION_FILE)
            .with_context(|| format!("Failed to create the file {solution_path}"))?;
    }

    fs::write("pyproject.toml", PYPROJECT_TOML)
        .context("Failed to create the file `rattlesnake/pyproject.toml`")?;

    fs::write(".python-version", "3.12\n")
        .context("Failed to create the file `rattlesnake/.python-version`")?;

    fs::write(".gitignore", GITIGNORE)
        .context("Failed to create the file `rattlesnake/.gitignore`")?;

    let uv_sync_status = Command::new("uv")
        .arg("sync")
        .stdin(Stdio::null())
        .status()
        .context("Failed to run `uv sync`")?;
    if !uv_sync_status.success() {
        bail!("Failed to run `uv sync` in the rattlesnake directory");
    }

    if let Ok(dir) = current_dir() {
        let mut dir = dir.as_path();

        loop {
            if dir.join(".git").exists() || dir.join(".jj").exists() {
                break;
            }

            if let Some(parent) = dir.parent() {
                dir = parent;
            } else {
                // Ignore any Git error because Git initialization is not required.
                let _ = Command::new("git")
                    .arg("init")
                    .stdin(Stdio::null())
                    .stdout(Stdio::null())
                    .stderr(Stdio::null())
                    .status();
                break;
            }
        }
    }

    stdout.queue(SetForegroundColor(Color::Green))?;
    stdout.write_all("Initialization done ✓".as_bytes())?;
    stdout.queue(ResetColor)?;
    stdout.write_all(b"\n\n")?;

    stdout.queue(SetAttribute(Attribute::Bold))?;
    stdout.write_all(POST_INIT_MSG)?;
    stdout.queue(ResetColor)?;

    Ok(())
}

const INIT_SOLUTION_FILE: &[u8] = b"# DON'T EDIT THIS SOLUTION FILE!
# It will be automatically filled after you finish the exercise.
";

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

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "B", "A", "SIM"]
# The generics exercises teach classic `TypeVar` and explicit variance, which
# these rules would push toward PEP 695 native syntax.
ignore = ["UP046", "UP047"]

[tool.pytest.ini_options]
testpaths = ["exercises"]
"#;

const GITIGNORE: &[u8] = b".venv/
__pycache__/
*.pyc
.rattlesnake-state.txt
";

const RATTLESNAKE_DIR_ALREADY_EXISTS_ERR: &str =
    "A directory with the name `rattlesnake` already exists in the current directory.
You probably already initialized Rattlesnake.
Run `cd rattlesnake`
Then run `rattlesnake` again";

const RATTLESNAKE_ALREADY_INITIALIZED_ERR: &str =
    "Rattlesnake is already initialized in the current directory.
Run `rattlesnake` to get started.";

const POST_INIT_MSG: &[u8] = b"Run `cd rattlesnake` to go into the generated directory.
Then run `rattlesnake` to get started.
";
