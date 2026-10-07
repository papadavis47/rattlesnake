use anyhow::Result;

use crate::info_file::InfoFile;

pub fn update() -> Result<()> {
    let info_file = InfoFile::parse()?;

    println!(
        "Validated `info.toml` with {} exercises",
        info_file.exercises.len(),
    );

    Ok(())
}
