# Python project

A Python project template.

## Setup

- `pyenv local 3.8.1 3.7.6` To specify Python versions
- `poetry init --no-interaction` to create `pyproject.toml`
- `poetry install` to install package in virtual environment
- `poetry run` to run scrips in `pyproject.toml` and processes in virtual environment
- `poetry add click` to add user package
- `poetry add --dev` to add dev package

## Testing

- `poetry run pytest -cov` To run test with coverage
- `nox` To run multi-environment tests
- `nox -r` To reuse environments
- `nox -s tests` to specify specific session
- `nox -s tests-3.7` To run tests for specific versions
- `nox -- -m e2e` to run end-to-end tests