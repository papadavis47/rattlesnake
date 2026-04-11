use anyhow::Result;
use crossterm::{
    QueueableCommand,
    style::{Attribute, Color, ResetColor, SetAttribute, SetForegroundColor},
};
use std::io::{self, StdoutLock, Write};

use crate::{
    cmd::CmdRunner,
    term::{self, CountedWrite, file_path, terminal_file_link, write_ansi},
};

/// The initial capacity of the output buffer.
pub const OUTPUT_CAPACITY: usize = 1 << 14;

pub fn solution_link_line(
    stdout: &mut StdoutLock,
    solution_path: &str,
    emit_file_links: bool,
) -> io::Result<()> {
    stdout.queue(SetAttribute(Attribute::Bold))?;
    stdout.write_all(b"Solution")?;
    stdout.queue(ResetColor)?;
    stdout.write_all(b" for comparison: ")?;
    file_path(stdout, Color::Cyan, |writer| {
        if emit_file_links && let Some(canonical_path) = term::canonicalize(solution_path) {
            terminal_file_link(writer, solution_path, &canonical_path)
        } else {
            writer.stdout().write_all(solution_path.as_bytes())
        }
    })?;
    stdout.write_all(b"\n")
}

/// See `info_file::ExerciseInfo`
pub struct Exercise {
    pub name: &'static str,
    pub dir: Option<&'static str>,
    /// Path of the exercise file starting with the `exercises/` directory.
    pub path: &'static str,
    pub canonical_path: Option<String>,
    pub test: bool,
    pub type_check: bool,
    pub lint: bool,
    pub hint: &'static str,
    pub done: bool,
}

impl Exercise {
    pub fn terminal_file_link<'a>(
        &self,
        writer: &mut impl CountedWrite<'a>,
        emit_file_links: bool,
    ) -> io::Result<()> {
        file_path(writer, Color::Blue, |writer| {
            if emit_file_links && let Some(canonical_path) = self.canonical_path.as_deref() {
                terminal_file_link(writer, self.path, canonical_path)
            } else {
                writer.write_str(self.path)
            }
        })
    }
}

pub trait RunnableExercise {
    fn name(&self) -> &str;
    fn dir(&self) -> Option<&str>;
    fn test(&self) -> bool;
    fn type_check(&self) -> bool;
    fn lint(&self) -> bool;

    fn exercise_path(&self) -> String {
        let name = self.name();

        let mut path = if let Some(dir) = self.dir() {
            // 14 = 10 + 1 + 3
            // exercises/ + / + .py
            let mut path = String::with_capacity(14 + dir.len() + name.len());
            path.push_str("exercises/");
            path.push_str(dir);
            path.push('/');
            path
        } else {
            // 13 = 10 + 3
            // exercises/ + .py
            let mut path = String::with_capacity(13 + name.len());
            path.push_str("exercises/");
            path
        };

        path.push_str(name);
        path.push_str(".py");

        path
    }

    /// Run the exercise and optionally its tests, linter, and type checker.
    /// The output is written to the `output` buffer after clearing it.
    fn run_exercise_at(
        &self,
        exercise_path: &str,
        mut output: Option<&mut Vec<u8>>,
        cmd_runner: &CmdRunner,
    ) -> Result<bool> {
        if let Some(output) = output.as_deref_mut() {
            output.clear();
        }

        // 1. Run the Python exercise file.
        let run_success = cmd_runner.run_python(exercise_path, output.as_deref_mut())?;
        if !run_success {
            if let Some(output) = output {
                write_ansi(output, SetAttribute(Attribute::Bold));
                write_ansi(output, SetForegroundColor(Color::Red));
                output.extend_from_slice(b"The exercise didn't run successfully (nonzero exit code)");
                write_ansi(output, ResetColor);
                output.push(b'\n');
            }
            return Ok(false);
        }

        // 2. Run pytest if test=true.
        if self.test() {
            let test_success = cmd_runner.run_pytest(exercise_path, output.as_deref_mut())?;
            if !test_success {
                return Ok(false);
            }
        }

        // 3. Run ruff if lint=true.
        if self.lint() {
            let lint_success = cmd_runner.run_ruff(exercise_path, output.as_deref_mut())?;
            if !lint_success {
                return Ok(false);
            }
        }

        // 4. Run ty if type_check=true.
        if self.type_check() {
            let type_success = cmd_runner.run_ty(exercise_path, output.as_deref_mut())?;
            if !type_success {
                return Ok(false);
            }
        }

        Ok(true)
    }

    /// Run the exercise.
    /// The output is written to the `output` buffer after clearing it.
    fn run_exercise(&self, output: Option<&mut Vec<u8>>, cmd_runner: &CmdRunner) -> Result<bool> {
        let path = self.exercise_path();
        self.run_exercise_at(&path, output, cmd_runner)
    }

    /// Run the exercise's solution.
    /// The output is written to the `output` buffer after clearing it.
    fn run_solution(&self, output: Option<&mut Vec<u8>>, cmd_runner: &CmdRunner) -> Result<bool> {
        let path = self.sol_path();
        self.run_exercise_at(&path, output, cmd_runner)
    }

    fn sol_path(&self) -> String {
        let name = self.name();

        let mut path = if let Some(dir) = self.dir() {
            // 14 = 10 + 1 + 3
            // solutions/ + / + .py
            let mut path = String::with_capacity(14 + dir.len() + name.len());
            path.push_str("solutions/");
            path.push_str(dir);
            path.push('/');
            path
        } else {
            // 13 = 10 + 3
            // solutions/ + .py
            let mut path = String::with_capacity(13 + name.len());
            path.push_str("solutions/");
            path
        };

        path.push_str(name);
        path.push_str(".py");

        path
    }
}

impl RunnableExercise for Exercise {
    fn name(&self) -> &str {
        self.name
    }

    fn dir(&self) -> Option<&str> {
        self.dir
    }

    fn test(&self) -> bool {
        self.test
    }

    fn type_check(&self) -> bool {
        self.type_check
    }

    fn lint(&self) -> bool {
        self.lint
    }
}
