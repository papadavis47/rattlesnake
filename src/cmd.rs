use anyhow::{Context, Result, bail};
use std::{
    io::{Read, pipe},
    process::{Command, Stdio},
};

/// Run a command with a description for a possible error and append the merged stdout and stderr.
/// The boolean in the returned `Result` is true if the command's exit status is success.
fn run_cmd(mut cmd: Command, description: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
    // Don't let Python litter the exercise directories with `__pycache__`, which
    // would trip the `dev check` unexpected-files check on the next run.
    cmd.env("PYTHONDONTWRITEBYTECODE", "1");

    let spawn = |mut cmd: Command| {
        // NOTE: The closure drops `cmd` which prevents a pipe deadlock.
        cmd.stdin(Stdio::null())
            .spawn()
            .with_context(|| format!("Failed to run the command `{description}`"))
    };

    let mut handle = if let Some(output) = output {
        let (mut reader, writer) = pipe().with_context(|| {
            format!("Failed to create a pipe to run the command `{description}``")
        })?;

        let writer_clone = writer.try_clone().with_context(|| {
            format!("Failed to clone the pipe writer for the command `{description}`")
        })?;

        cmd.stdout(writer_clone).stderr(writer);
        let handle = spawn(cmd)?;

        reader
            .read_to_end(output)
            .with_context(|| format!("Failed to read the output of the command `{description}`"))?;

        output.push(b'\n');

        handle
    } else {
        cmd.stdout(Stdio::null()).stderr(Stdio::null());
        spawn(cmd)?
    };

    handle
        .wait()
        .with_context(|| format!("Failed to wait on the command `{description}` to exit"))
        .map(|status| status.success())
}

pub struct CmdRunner;

impl CmdRunner {
    pub fn build() -> Result<Self> {
        let status = Command::new("uv")
            .arg("--version")
            .stdin(Stdio::null())
            .stdout(Stdio::null())
            .stderr(Stdio::null())
            .status()
            .context(UV_NOT_FOUND_ERR)?;

        if !status.success() {
            bail!("The command `uv --version` failed. Is `uv` installed correctly?");
        }

        Ok(Self)
    }

    /// Run a Python exercise file via `uv run python <exercise_path>`.
    /// The boolean in the returned `Result` is true if the command's exit status is success.
    pub fn run_python(&self, exercise_path: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
        let mut cmd = Command::new("uv");
        cmd.arg("run").arg("python").arg(exercise_path);

        run_cmd(cmd, &format!("uv run python {exercise_path}"), output)
    }

    /// Run pytest on a Python exercise file via `uv run pytest <exercise_path>`.
    /// The boolean in the returned `Result` is true if the command's exit status is success.
    pub fn run_pytest(&self, exercise_path: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
        let mut cmd = Command::new("uv");
        cmd.arg("run")
            .arg("pytest")
            .arg(exercise_path)
            .arg("-v")
            .arg("--tb=short")
            .arg("--color=yes")
            .arg("--no-header")
            .arg("-q");

        run_cmd(cmd, &format!("uv run pytest {exercise_path}"), output)
    }

    /// Run ruff linter on a Python exercise file via `uv run ruff check <exercise_path>`.
    /// The boolean in the returned `Result` is true if the command's exit status is success.
    pub fn run_ruff(&self, exercise_path: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
        let mut cmd = Command::new("uv");
        cmd.arg("run")
            .arg("ruff")
            .arg("check")
            .arg(exercise_path)
            .arg("--no-fix");

        run_cmd(cmd, &format!("uv run ruff check {exercise_path}"), output)
    }

    /// Check formatting of a Python exercise file via `uv run ruff format --check <exercise_path>`.
    /// The boolean in the returned `Result` is true if the command's exit status is success.
    pub fn run_ruff_format(&self, exercise_path: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
        let mut cmd = Command::new("uv");
        cmd.arg("run")
            .arg("ruff")
            .arg("format")
            .arg("--check")
            .arg(exercise_path);

        run_cmd(
            cmd,
            &format!("uv run ruff format --check {exercise_path}"),
            output,
        )
    }

    /// Run ty type checker on a Python exercise file via `uv run ty check <exercise_path>`.
    /// The boolean in the returned `Result` is true if the command's exit status is success.
    pub fn run_ty(&self, exercise_path: &str, output: Option<&mut Vec<u8>>) -> Result<bool> {
        let mut cmd = Command::new("uv");
        cmd.arg("run").arg("ty").arg("check").arg(exercise_path);

        run_cmd(cmd, &format!("uv run ty check {exercise_path}"), output)
    }
}

const UV_NOT_FOUND_ERR: &str = "Failed to run the command `uv --version`
Did you already install uv?
Try running `uv --version` to diagnose the problem.";

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_run_cmd() {
        let mut cmd = Command::new("echo");
        cmd.arg("Hello");

        let mut output = Vec::with_capacity(8);
        run_cmd(cmd, "echo …", Some(&mut output)).unwrap();

        assert_eq!(output, b"Hello\n\n");
    }
}
