# Changelog

## 0.1.0 (Unreleased)

Initial Rattlesnake release, forked from Rustlings v6.5.0. Upstream history is
archived in [`CHANGELOG-rustlings.md`](CHANGELOG-rustlings.md).

### Added

- Python exercise pipeline via `uv run`: execution, pytest, Ruff lint, optional
  `ruff format --check`, and optional `ty` type check
- 50-exercise Python curriculum (beginner basics through metaclasses,
  protocols, and packaging) with hints and reference solutions
- `uv`-based `init` that writes `pyproject.toml` and `.python-version`
