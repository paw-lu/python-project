# Python project

[![Tests](https://github.com/pscosta5/python-project/workflows/Tests/badge.svg)](https://github.com/pscosta5/python-project/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/pscosta5/python-project/branch/master/graph/badge.svg)](https://codecov.io/gh/pscosta5/python-project)
[![PyPI](https://img.shields.io/pypi/v/python-project.svg)](https://pypi.org/project/hypermodern-python/)
[![Read the Docs](https://readthedocs.org/projects/hypermodern-python/badge/)](https://hypermodern-python.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python project template.

## Setup

- `pyenv local 3.8.1 3.7.6` – specify Python versions
- `poetry init --no-interaction` – create `pyproject.toml`
- `poetry install` – install package in virtual environment
- `poetry run` – run scrips in `pyproject.toml` and processes in virtual environment
- `poetry add click` – add user package
- `poetry add --dev` – add dev package
- `poetry add --dev --python=3.7 pytype` — add version specific package

## Testing

- `poetry run pytest -cov` – run test with coverage
- `nox` – run multi-environment tests
- `nox -r` – reuse environments
- `nox -s tests` – specify specific session
- `nox -s tests-3.7` – run tests for specific versions
- `nox -- -m e2e` – run end-to-end tests

## Linting

- `nox -rs lint` – run linter
- `nox -rs black` – run Black formatter
- `nox` — will not run Black
- `pre-commit run --all-files` — manually triggers hooks

## Type hints

- `nox -rs mypy` — check types based on hints
- `nox -rs pytype` — infer types
- `nox -rs typeguard` — check types at runtime

## Documentation

- `nox --list-sessions` – overview of Nox tasks
- `nox -rs xdoctest` — test document examples
- `nox -rs docs` – generate documentation

## CI-CD

- [GitHub Actions](https://github.com/features/actions)
- [Codecov](https://codecov.io/)
