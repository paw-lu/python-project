# Python project

A Python project template.

## Testing

- `poetry run pytest -cov` To run test with coverage
- `nox` To run multi-environment tests
- `nox -r` To reuse environments
- `nox -s tests-3.8` To run tests for specific versions
- `nox -- -m e2e` to run end-to-end tests
